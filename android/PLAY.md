# SILENT MEDIC VET — Google Play build

Free app. Application ID `com.hakoya.silentmedicvet`. Publisher: HAKOYA LLC.

The Google Play build uses the same web bundle as the App Store build (`ios/www`, built by
`ios/scripts/build-store.py`): no Tier 3C entries, no weight-based dose computation, no network,
no PWA install wording. See `ios/APPSTORE.md` for how that bundle differs from the web app.

## Build
GitHub Actions → "Android build (Google Play)". Runs on a push to `android-build` or by manual
dispatch. It produces an **unsigned** App Bundle, kept as a workflow artifact and committed to the
`android-artifacts` branch at `dist/silent-medic-vet-<version>-<code>-unsigned.aab`
(`dist/LATEST` names the newest). versionCode = workflow run number.

## Sign
The HAKOYA LLC upload key (same key as TOXCARD; kept by the account holder, backed up in
Google Drive 00_CLAUDE_HQ/TOXCARD_Android_UploadKey) signs the bundle before upload:

    jarsigner -keystore toxcard-upload.jks -signedjar out-signed.aab in-unsigned.aab toxcard-upload
    jarsigner -verify out-signed.aab

Google re-signs with the app signing key (Play App Signing).

## Files
- `scripts/native-setup.py` — launcher and adaptive icons, splash, version, ID and targetSdk checks
- `capacitor.config.json`, `package.json`, `package-lock.json`
