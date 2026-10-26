# SILENT MEDIC VET — App Store build

Free app. Bundle ID `com.hakoya.silentmedicvet`. Publisher: HAKOYA LLC. iPhone only, iOS 15.0+.

## How the App Store build differs from the web build
Built by `scripts/build-store.py` from the repository's `index.html` (the web app as published).
The web files are never modified.

| | Web | App Store |
|---|---|---|
| Tier 3C (unapproved research peptides) | 5 entries | removed (decision 2026-10-06) |
| Knowledge base | 94 entries | 89 entries, integrity hash recomputed |
| Weight-based dose computation | yes | none; doses shown only as the source states them (Guideline 1.4.2) |
| "Prototype" wording, PWA install button | yes | removed |
| Patients, reminders, Spotlight, Siri, haptics, own look | no | yes (1.1) |

Note: `template.html` is older than `index.html` (the v0.2 template changes exist only as
`tools/template_v020.diff`, which no longer applies). Running `build.py` today would overwrite the
web `index.html` with older code. Do not run it until the template is brought up to v0.2.0.

## Version 1.1 — native iPhone app (rework after the 2026-10-16 Guideline 4.3 / 4.2.6 review)
Everything in 1.0 is kept. Added, all on the device, no network:

| | Where | What |
|---|---|---|
| Patients tab | `native/PatientChartPlugin.swift`, `web/smv-ios.js` | Animal profiles (name or tag, species, weight noted with date, notes, observation log) in a Data Protection file in Application Support. The weight is a note; no dose is computed from it. "Chart this animal" sets the species everywhere. |
| Recheck reminders | `native/RecheckPlugin.swift` | Local notifications (UNUserNotificationCenter) per patient; tapping one opens that patient. |
| Spotlight | `native/KnowledgeIndexPlugin.swift` | Every reference entry and condition card in the iPhone's Spotlight index; a result opens the card. Re-indexed only when the knowledge base hash changes. |
| Siri / Shortcuts | `native/VetShortcuts.swift` | App Intents (iOS 16+) and App Shortcuts with Siri phrases (iOS 17+): look up a drug for an animal, build a triage plan, open my patients. |
| Routing | `native/FieldRouter.swift` | Spotlight activity, intents and reminder taps become one route string the web layer takes (`FieldRoute.take()`, `route` event). AppDelegate is patched by `native-setup.py`. |
| Haptics | `native/FieldHapticsPlugin.swift` | Taptic feedback on selections, plan building, saves and reminders. |
| Look | `web/smv-ios.css`, `scripts/make-icon.py` | Own identity: evergreen / sage / copper, rounded type, bottom tab bar, paw-and-cross icon. |

`npm run preflight` (Playwright, after `npm run build:www`) checks the bundle behind a simulated
Capacitor bridge (`qa/bridge-mock.js`): every route, patient save/edit/delete, reminders,
Spotlight items, haptics, no page errors and no network requests. If Playwright is installed
globally: `ln -s $(npm root -g)/playwright node_modules/playwright`.

Store listing texts and screenshots: `store/` (`description.txt`, `promo.txt`, `review-notes.txt`,
six 1206 x 2622 screenshots made by `qa/store-shots.mjs` from the real bundle).

## Build and upload
GitHub Actions > "iOS build (App Store)" > Run workflow, with the marketing version.
Build number = workflow run number. Signing is automatic with an App Store Connect API key.

Repository secrets (entered by the account holder): `APPSTORE_API_KEY_ID`,
`APPSTORE_API_ISSUER_ID`, `APPSTORE_API_PRIVATE_KEY`, `APPLE_TEAM_ID`.
Same values as the TOXCARD repository; the same key works for every app on the team.

## Files
- `scripts/build-store.py` — web bundle for the App Store build
- `scripts/native-setup.py` — icon, splash, Info.plist, iPhone only, privacy manifest, iOS 15, native sources wired into the app target with fixed project IDs
- `scripts/make-icon.py` — draws `icons/icon-1024.png` (1.1 paw-and-cross design)
- `native/` — Swift plugins and App Intents; `web/` — the iPhone layer injected by build-store.py
- `qa/` — preflight check and store screenshot renderer
- `capacitor.config.json`, `package.json`, `package-lock.json`
