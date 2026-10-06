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

Note: `template.html` is older than `index.html` (the v0.2 template changes exist only as
`tools/template_v020.diff`, which no longer applies). Running `build.py` today would overwrite the
web `index.html` with older code. Do not run it until the template is brought up to v0.2.0.

## Build and upload
GitHub Actions > "iOS build (App Store)" > Run workflow, with the marketing version.
Build number = workflow run number. Signing is automatic with an App Store Connect API key.

Repository secrets (entered by the account holder): `APPSTORE_API_KEY_ID`,
`APPSTORE_API_ISSUER_ID`, `APPSTORE_API_PRIVATE_KEY`, `APPLE_TEAM_ID`.
Same values as the TOXCARD repository; the same key works for every app on the team.

## Files
- `scripts/build-store.py` — web bundle for the App Store build
- `scripts/native-setup.py` — icon, splash, Info.plist, iPhone only, privacy manifest, iOS 15
- `scripts/make-icon.py` — draws `icons/icon-1024.png` from the web icon design
- `capacitor.config.json`, `package.json`, `package-lock.json`
