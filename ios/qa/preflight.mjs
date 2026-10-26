// Pre-upload check of the App Store bundle (ios/www) behind a simulated Capacitor iOS bridge.
// Run after `npm run build:www`:  node qa/preflight.mjs
// Fails on any page error, any network request, or any native path that does not behave.
import { chromium } from 'playwright';
import { readFileSync } from 'fs';
import { fileURLToPath, pathToFileURL } from 'url';
import path from 'path';

const IOS = path.dirname(path.dirname(fileURLToPath(import.meta.url)));
const URL_ = pathToFileURL(path.join(IOS, 'www', 'index.html')).href;
const MOCK = readFileSync(path.join(IOS, 'qa', 'bridge-mock.js'), 'utf8');
const results = [];
const ok = (cond, what) => { results.push([!!cond, what]); if (!cond) console.error('FAIL', what); };

const browser = await chromium.launch();
const ctx = await browser.newContext({ viewport: { width: 402, height: 874 }, deviceScaleFactor: 1, isMobile: true, hasTouch: true });
const errors = [], net = [];
await ctx.route('**/*', r => { const u = r.request().url(); if (u.startsWith('file:') || u.startsWith('data:')) return r.continue(); net.push(u); return r.abort(); });
const page = await ctx.newPage();
page.on('pageerror', e => errors.push(String(e)));
page.on('console', m => { if (m.type() === 'error') errors.push('console: ' + m.text()); });
page.on('dialog', d => d.accept());
await page.addInitScript(`window.__initialRoute='lookup:horse:phenylbutazone';\n${MOCK}`);
await page.goto(URL_);
await page.waitForFunction(() => window.SMV_IOS && window.SMV_IOS.ready(), null, { timeout: 15000 });
await page.waitForTimeout(600);

// Platform and opening screen
ok(await page.evaluate(() => window.SMV_IOS.native), 'native platform detected through the bridge');
ok(await page.evaluate(() => !document.getElementById('boot')), 'opening screen dismissed after integrity check');
ok(await page.evaluate(() => state.kbOk), 'knowledge-base integrity verified');
ok(await page.locator('.smvBar .smvTab').count() === 4, 'bottom tab bar with 4 tabs');

// Route queued before launch (Siri / Shortcuts "Look up a drug for horse")
ok(await page.evaluate(() => state.species === 'horse' && document.getElementById('q').value === 'phenylbutazone'), 'lookup route: horse + search term');
ok(await page.locator('#refPanel.active #results .card .name', { hasText: 'Phenylbutazone' }).count() >= 1, 'lookup route: Phenylbutazone card shown');

// Spotlight indexing
const idx = await page.evaluate(() => window.__mock.indexed);
ok(idx && idx.items.length === (await page.evaluate(() => state.kb.length + state.cond.length)), 'Spotlight: every entry and condition indexed');
ok(idx && idx.items.every(i => /^(kb|cond):/.test(i.id) && i.title), 'Spotlight: identifiers are routes');
ok(idx && !idx.items.some(i => /BPC-157|TB-500/.test(i.title)), 'Spotlight: no Tier 3C entries');

// Route arriving while running (Spotlight tap on a condition)
await page.evaluate(() => { window.__mock.route = 'cond:glaucoma'; window.__mock.emit('FieldRoute', 'route', { pending: true }); });
await page.waitForTimeout(300);
ok(await page.evaluate(() => document.getElementById('condPanel').classList.contains('active') && !!document.querySelector('[data-cond-id="glaucoma"].open')), 'route event: condition card opened');
ok(await page.evaluate(() => document.querySelector('.smvTab[data-tab="cond"]').getAttribute('aria-selected') === 'true'), 'bottom bar follows route');

// Spotlight tap on a reference entry
const carp = await page.evaluate(() => state.kb.find(e => e.n === 'Carprofen').i);
await page.evaluate(id => { window.__mock.route = 'kb:' + id; window.__mock.emit('FieldRoute', 'route', {}); }, carp);
await page.waitForTimeout(300);
ok(await page.evaluate(() => !!document.querySelector('#refPanel.active .card.open') && document.querySelector('#refPanel .card.open .name').textContent === 'Carprofen'), 'route event: reference entry opened');

// Patients: create
await page.click('.smvTab[data-tab="pat"]');
ok(await page.locator('#patPanel.active').count() === 1, 'Patients tab opens');
ok(await page.locator('.smvEmpty').count() === 1, 'Patients: empty state');
await page.click('#patNew');
await page.fill('#pfName', 'Bella');
await page.selectOption('#pfSp', 'dog');
await page.fill('#pfW', '12.4');
await page.fill('#pfWd', '2026-10-20');
await page.fill('#pfN', 'Spayed. Right eye tearing since Monday.');
await page.click('#patForm button[type=submit]');
await page.waitForTimeout(200);
let pats = await page.evaluate(() => window.__mock.patients);
ok(pats.length === 1 && pats[0].name === 'Bella' && pats[0].weightKg === 12.4 && pats[0].species === 'dog', 'PatientChart.save stores the profile natively');
ok(await page.locator('.pat .pn', { hasText: 'Bella' }).count() === 1, 'Patients: card shown');
ok(await page.evaluate(() => state.species === 'dog' && /Bella/.test(document.getElementById('smvCtx').textContent)), 'first patient becomes the active animal');

// Observation log
await page.click('.pat [data-act="obs"]');
await page.fill('.pat .obTxt', 'Ate half her breakfast. Right eye less squinty.');
await page.click('.pat [data-act="obAdd"]');
await page.waitForTimeout(200);
pats = await page.evaluate(() => window.__mock.patients);
ok(pats[0].log && pats[0].log.length === 1, 'observation saved to the log');

// Recheck reminder
await page.click('.pat [data-act="recheck"]');
await page.click('.pat .quick [data-q="tm8"]');
await page.fill('.pat .rcWhy', 'Right eye');
await page.click('.pat [data-act="rcSet"]');
await page.waitForTimeout(300);
const rem = await page.evaluate(() => Object.values(window.__mock.reminders));
ok(rem.length === 1 && rem[0].route === 'patient:' + pats[0].id && /Recheck: Bella \(Dog\)/.test(rem[0].title) && rem[0].body === 'Right eye', 'Recheck.schedule called with title, body and patient route');
ok(await page.evaluate(() => window.__mock.permission === 'granted'), 'notification permission requested when needed');
ok(await page.locator('.pat .rc', { hasText: 'Recheck' }).count() === 1, 'recheck shown on the card');

// Reminder tap -> patient
await page.click('.smvTab[data-tab="ref"]');
await page.evaluate(id => { window.__mock.route = 'patient:' + id; window.__mock.emit('FieldRoute', 'route', {}); }, pats[0].id);
await page.waitForTimeout(300);
ok(await page.evaluate(() => document.getElementById('patPanel').classList.contains('active')), 'reminder route opens the patient');

// Chart this animal with a second patient, then plan route for another species
await page.click('#patNew');
await page.fill('#pfName', 'Ewe 214');
await page.selectOption('#pfSp', 'sheep');
await page.click('#patForm button[type=submit]');
await page.waitForTimeout(200);
await page.locator('.pat', { hasText: 'Ewe 214' }).locator('[data-act="use"]').click();
await page.waitForTimeout(200);
ok(await page.evaluate(() => state.species === 'sheep' && document.getElementById('refPanel').classList.contains('active')), 'Chart this animal switches species and opens Reference');
ok(await page.evaluate(() => !document.getElementById('foodNote').hidden), 'food-animal withdrawal note shown for sheep');
await page.evaluate(() => { window.__mock.route = 'plan:cat'; window.__mock.emit('FieldRoute', 'route', {}); });
await page.waitForTimeout(300);
ok(await page.evaluate(() => state.species === 'cat' && document.getElementById('dsPanel').classList.contains('active')), 'plan route: triage builder for cat');
await page.click('#dsSyn .opt >> nth=0');
await page.click('#dsOnset .opt >> nth=1');
await page.click('#dsGo');
await page.waitForTimeout(200);
ok(await page.locator('#plan section.red').count() === 1, 'triage plan builds');
ok(!(await page.evaluate(() => document.body.innerText)).includes('→ at'), 'no weight-based dose computation anywhere');
ok(await page.evaluate(() => !document.querySelector('input[type=number]#weight')), 'no dosing weight field');

// Patients route, delete
await page.evaluate(() => { window.__mock.route = 'patients'; window.__mock.emit('FieldRoute', 'route', {}); });
await page.waitForTimeout(200);
await page.locator('.pat', { hasText: 'Bella' }).locator('[data-act="del"]').click();
await page.waitForTimeout(200);
ok((await page.evaluate(() => window.__mock.patients)).length === 1 && Object.keys(await page.evaluate(() => window.__mock.reminders)).length === 0, 'delete removes the profile and cancels its reminder');

// Haptics and text rules
const calls = await page.evaluate(() => window.__mock.calls.filter(c => c[0] === 'FieldHaptics').length);
ok(calls >= 5, `haptics fired (${calls})`);
const html = readFileSync(path.join(IOS, 'www', 'index.html'), 'utf8');
for (const bad of ['NAMRU', 'TCCC-grade', 'Prototype', 'pilot', 'Tier 3C', 'BPC-157']) ok(!html.includes(bad), `bundle free of "${bad}"`);

// Second launch reads profiles back (cold start) with no route
const page2 = await ctx.newPage();
page2.on('pageerror', e => errors.push('page2: ' + String(e)));
await page2.addInitScript(MOCK + `\nwindow.__mock.patients=${JSON.stringify(await page.evaluate(() => window.__mock.patients))};`);
await page2.goto(URL_);
await page2.waitForFunction(() => window.SMV_IOS && window.SMV_IOS.ready(), null, { timeout: 15000 });
await page2.click('.smvTab[data-tab="pat"]');
ok(await page2.locator('.pat .pn', { hasText: 'Ewe 214' }).count() === 1, 'profiles survive a relaunch');

ok(errors.length === 0, 'no page errors' + (errors.length ? ': ' + errors.join(' | ') : ''));
ok(net.length === 0, 'no network requests' + (net.length ? ': ' + net.join(' ') : ''));
await browser.close();
const failed = results.filter(r => !r[0]);
console.log(`preflight: ${results.length - failed.length}/${results.length} checks passed`);
process.exit(failed.length ? 1 : 0);
