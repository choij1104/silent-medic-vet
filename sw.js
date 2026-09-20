// SILENT MEDIC VET service worker
// Purpose: make the app openable with no network at all once it has been visited once.
// It caches only this app's own files, never contacts another origin, and never transmits
// anything — the app itself makes no network requests at runtime.
// CACHE is stamped with the app version by build.py so a new release replaces the old cache.
const CACHE = 'silent-medic-vet-v0.1.8';
const ASSETS = ['./', './index.html', './manifest.webmanifest', './icon-192.png', './icon-512.png'];

self.addEventListener('install', e => {
  e.waitUntil(
    caches.open(CACHE)
      .then(c => c.addAll(ASSETS).catch(() => c.addAll(['./index.html'])))
      .then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', e => {
  e.waitUntil(
    caches.keys()
      .then(keys => Promise.all(keys.filter(k => k !== CACHE).map(k => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

// Cache-first with background revalidation: the cached copy is authoritative offline,
// and is refreshed silently whenever the device happens to be online.
self.addEventListener('fetch', e => {
  const req = e.request;
  if (req.method !== 'GET' || new URL(req.url).origin !== self.location.origin) return;
  e.respondWith(
    caches.match(req).then(hit => {
      const net = fetch(req)
        .then(res => { if (res && res.ok) caches.open(CACHE).then(c => c.put(req, res.clone())); return res; })
        .catch(() => hit);
      return hit || net;
    })
  );
});
