// Simulated Capacitor iOS bridge for pre-upload checks of ios/www in a desktop browser.
// Mirrors what the native side provides: window.webkit.messageHandlers.bridge (so capacitor.js
// reports the "ios" platform), Capacitor.PluginHeaders for the app's own plugins, and
// nativePromise / nativeCallback answering like the Swift plugins in ios/native.
(() => {
  const M = window.__mock = {
    calls: [], patients: [], reminders: {}, indexed: null, route: (window.__initialRoute || ''),
    permission: 'prompt', listeners: {}
  };
  const P = (name, methods) => ({ name, methods: methods.map(m => ({ name: m, rtype: 'promise' }))
    .concat([{ name: 'addListener', rtype: 'callback' }, { name: 'removeListener', rtype: 'promise' }]) });
  window.webkit = { messageHandlers: { bridge: { postMessage() {} } } };
  window.Capacitor = window.Capacitor || {};
  window.Capacitor.PluginHeaders = [
    P('FieldRoute', ['take']),
    P('KnowledgeIndex', ['index', 'clear']),
    P('PatientChart', ['list', 'save', 'remove']),
    P('Recheck', ['permission', 'request', 'schedule', 'cancel', 'pending']),
    P('FieldHaptics', ['selection', 'impact', 'notify'])
  ];
  const impl = {
    FieldRoute: { take() { const r = M.route; M.route = ''; return { route: r }; } },
    KnowledgeIndex: {
      index(o) { M.indexed = o; return { indexed: o.items.length, skipped: false }; },
      clear() { M.indexed = null; return {}; }
    },
    PatientChart: {
      list() { return { patients: JSON.parse(JSON.stringify(M.patients)) }; },
      save(o) {
        if (!o.patient || !o.patient.id) throw new Error('A patient with an id is required');
        const i = M.patients.findIndex(p => p.id === o.patient.id);
        if (i >= 0) M.patients[i] = o.patient; else M.patients.push(o.patient);
        return { patients: JSON.parse(JSON.stringify(M.patients)) };
      },
      remove(o) { M.patients = M.patients.filter(p => p.id !== o.id); return { patients: JSON.parse(JSON.stringify(M.patients)) }; }
    },
    Recheck: {
      permission() { return { status: M.permission }; },
      request() { M.permission = 'granted'; return { granted: true }; },
      schedule(o) {
        if (!o.id || !(o.at > Date.now() + 30e3)) throw new Error('Pick a time in the future');
        M.reminders[o.id] = o; return { id: o.id, at: o.at };
      },
      cancel(o) { delete M.reminders[o.id]; return {}; },
      pending() { return { reminders: Object.values(M.reminders) }; }
    },
    FieldHaptics: { selection() { return {}; }, impact() { return {}; }, notify() { return {}; } }
  };
  let cbId = 0;
  window.Capacitor.nativePromise = (plugin, method, options) => {
    M.calls.push([plugin, method, options]);
    return new Promise((res, rej) => setTimeout(() => {
      try { res(impl[plugin][method](options || {})); } catch (e) { rej(e); }
    }, 5));
  };
  window.Capacitor.nativeCallback = (plugin, method, options, cb) => {
    M.calls.push([plugin, method, options]);
    const id = String(++cbId);
    if (method === 'addListener') (M.listeners[plugin + ':' + options.eventName] ||= []).push(cb);
    return id;
  };
  M.emit = (plugin, eventName, data) => (M.listeners[plugin + ':' + eventName] || []).forEach(cb => cb(data));
})();
