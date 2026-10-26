// Renders the six App Store screenshots (1206 x 2622, iPhone 6.9"/6.3" Pro class) from the real
// App Store bundle (ios/www) behind the simulated Capacitor bridge, then frames each with a caption.
// Run after `npm run build:www`:  node qa/store-shots.mjs   -> ios/store/1-reference.png ...
import { chromium } from 'playwright';
import { readFileSync, mkdirSync } from 'fs';
import { fileURLToPath, pathToFileURL } from 'url';
import path from 'path';

const IOS = path.dirname(path.dirname(fileURLToPath(import.meta.url)));
const URL_ = pathToFileURL(path.join(IOS, 'www', 'index.html')).href;
const MOCK = readFileSync(path.join(IOS, 'qa', 'bridge-mock.js'), 'utf8');
const OUT = path.join(IOS, 'store');
mkdirSync(OUT, { recursive: true });

// Sample profiles for the Patients screens (invented animals, no real people).
const day = 864e5, now = Date.now();
const t8 = new Date(now + day); t8.setHours(8, 0, 0, 0);
const SEED = [
  { id: 'p1', name: 'Bella', species: 'dog', weightKg: 12.4, weightDate: new Date(now - 5 * day).toISOString().slice(0, 10),
    notes: 'Spayed, 6 years. Right eye tearing since Monday.', created: now - 9 * day, updated: now,
    recheck: { at: t8.getTime(), reason: 'Right eye: squinting, discharge', alert: true },
    log: [{ t: now - 2 * day, text: 'Right eye watery, no squint.' }, { t: now - day, text: 'Squinting in bright light. Called the clinic.' }, { t: now - 3 * 3600e3, text: 'Ate half her breakfast. Eye less squinty.' }] },
  { id: 'p2', name: 'Ewe 214', species: 'sheep', weightKg: 68, weightDate: new Date(now - 20 * day).toISOString().slice(0, 10),
    notes: 'Twins last spring. Lame left fore.', created: now - 30 * day, updated: now - 2 * day, recheck: null,
    log: [{ t: now - 2 * day, text: 'Hoof trimmed, foot bath.' }] },
  { id: 'p3', name: 'Duke', species: 'horse', weightKg: null, weightDate: '', notes: 'Gelding, 14. Shows in spring.', created: now - 40 * day, updated: now - 6 * day, recheck: null, log: [] }
];

const browser = await chromium.launch();
const ctx = await browser.newContext({ viewport: { width: 402, height: 874 }, deviceScaleFactor: 3, isMobile: true, hasTouch: true });
await ctx.route('**/*', r => (r.request().url().startsWith('file:') || r.request().url().startsWith('data:')) ? r.continue() : r.abort());
const app = await ctx.newPage();
const errors = [];
app.on('pageerror', e => errors.push(String(e)));
await app.addInitScript(MOCK + `\nwindow.__mock.patients=${JSON.stringify(SEED)};window.__mock.permission='granted';localStorage.setItem('smv.activePatient','"p1"');`);
await app.goto(URL_);
await app.waitForFunction(() => window.SMV_IOS && window.SMV_IOS.ready(), null, { timeout: 15000 });
await app.waitForTimeout(700);
const route = async r => { await app.evaluate(r => window.SMV_IOS.go(r), r); await app.waitForTimeout(350); };
const openCard = async (scope, name) => {
  await app.evaluate(([scope, name]) => {
    const c = [...document.querySelectorAll(scope + ' .card')].find(c => c.querySelector('.name').textContent === name);
    c.classList.add('open'); c.querySelector('.head').setAttribute('aria-expanded', 'true');
    window.scrollTo(0, c.getBoundingClientRect().top + window.scrollY - 70);
  }, [scope, name]);
  await app.waitForTimeout(250);
};
const shot = async () => (await app.screenshot()).toString('base64');

const shots = [];
// 1 Reference: is it safe for this animal?
await route('lookup:dog:ibuprofen');
await openCard('#refPanel', (await app.evaluate(() => document.querySelector('#results .card .name').textContent)));
shots.push(['1-reference', 'Is it safe for<br>this animal?', 'Drugs, supplements and home medicines rated for 13 species', await shot()]);
// 2 Conditions
await route('cond:glaucoma');
await app.evaluate(() => { const c = document.querySelector('[data-cond-id="glaucoma"]'); window.scrollTo(0, c.getBoundingClientRect().top + window.scrollY - 70); });
await app.waitForTimeout(200);
shots.push(['2-conditions', 'Know when it<br>can’t wait', 'Triage bands, warning signs and breeds at risk', await shot()]);
// 3 Triage plan
await route('plan:dog');
await app.evaluate(() => {
  const pick = (id, re) => [...document.querySelectorAll('#' + id + ' .opt')].find(b => re.test(b.textContent)).click();
  pick('dsSyn', /^Eye/); pick('dsOnset', /^Today$/); pick('dsRes', /^First-aid kit$/);
  document.getElementById('dsGo').click();
  const p = document.getElementById('plan'); window.scrollTo(0, p.getBoundingClientRect().top + window.scrollY - 70);
});
await app.waitForTimeout(300);
shots.push(['3-triage', 'A plan in<br>seconds', 'Red flags first, then what to do and what not to do', await shot()]);
// 4 Patients
await route('patients');
await app.evaluate(() => window.scrollTo(0, 0));
shots.push(['4-patients', 'A profile for<br>every animal', 'Species, weight noted, notes and a log, kept on your iPhone', await shot()]);
// 5 Recheck reminder
await app.click('.pat[data-pid="p1"] [data-act="recheck"]');
await app.click('.pat[data-pid="p1"] .quick [data-q="tm8"]');
await app.evaluate(() => { const s = document.querySelector('.pat[data-pid="p1"] .rc'); window.scrollTo(0, s.getBoundingClientRect().top + window.scrollY - 90); });
await app.waitForTimeout(250);
shots.push(['5-recheck', 'Never miss<br>a recheck', 'Reminders that open the right patient. Or ask Siri.', await shot()]);
// 6 Veterinarian view, food animal
await app.click('.pat[data-pid="p1"] [data-act="close"]');
await app.click('#modeDvm');
await route('lookup:cattle:flunixin');
await openCard('#refPanel', 'Flunixin meglumine');
shots.push(['6-veterinarian', 'Veterinarian<br>view', 'Reference doses as sources state them, with withdrawal times', await shot()]);

// Frame and caption
const frame = await (await browser.newContext({ viewport: { width: 1206, height: 2622 }, deviceScaleFactor: 1 })).newPage();
for (const [name, title, sub, b64] of shots) {
  await frame.setContent(`<!doctype html><html><head><style>
    *{margin:0;box-sizing:border-box}
    body{width:1206px;height:2622px;overflow:hidden;background:radial-gradient(130% 70% at 50% 0%,#2f6b4f 0%,#18392b 55%,#11291f 100%);font-family:'Inter Display','Inter',sans-serif;color:#f4efe2}
    .cap{position:absolute;top:118px;left:96px;right:96px}
    h1{font-weight:800;font-size:104px;line-height:1.02;letter-spacing:-2px}
    p{margin-top:28px;font-size:44px;line-height:1.25;color:#cfe2d3;font-weight:500}
    .dot{display:inline-block;width:26px;height:26px;border-radius:50%;background:#d68046;margin-right:18px;vertical-align:10px}
    .ph{position:absolute;left:153px;top:612px;width:900px;height:1957px;border-radius:70px;overflow:hidden;box-shadow:0 0 0 14px #0c1f17,0 40px 90px rgba(0,0,0,.45)}
    .ph img{width:900px;display:block}
  </style></head><body><div class="cap"><h1><span class="dot"></span>${title}</h1><p>${sub}</p></div>
  <div class="ph"><img src="data:image/png;base64,${b64}"></div></body></html>`);
  await frame.waitForTimeout(150);
  await frame.screenshot({ path: path.join(OUT, name + '.png') });
  console.log('wrote', name + '.png');
}
await browser.close();
if (errors.length) { console.error('page errors:', errors); process.exit(1); }
