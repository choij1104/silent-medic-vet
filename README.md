# SILENT MEDIC VET

Offline veterinary decision support for owners and veterinarians. Single-file PWA (`index.html`), no network calls, knowledge base embedded as gzip+base64 with SHA-256 integrity check.

**Species (13):** dog, cat, rabbit · horse · cattle, sheep, goat, deer · pig · chicken, duck, turkey, peafowl
**Modes:** Owner (OTC/supplement/first aid, red flags, "Rx exists") · Veterinarian (mg/kg reference doses, AMDUCA/withdrawal, DVM notes)
**Treatment tiers:** 1 OTC drug · 2 Rx small molecule · 3 Peptide/biologic (3A approved veterinary · 3B human-approved extra-label · 3C unapproved/research — red band, reference only) · 4 Nutraceutical · 5 Herbal/TCVM · 6 Manual/physical
**Prescribing reference (DVM, v0.1.2):** VCPR · prescription elements & refills · dispensed-drug label · AMDUCA extra-label conditions & records · controlled substances (DEA + Texas) · compounding (GFI #256) · VFD / GFI #263 · prescription portability & online pharmacies. Federal + Texas; substitute your state practice act.
**Views:** All · Rehab & Manual Therapy (dog and horse, tiers 4+6; deep link `index.html#view=rehab`).
**Evidence grades:** A strong in-species data · B some controlled data / label · C extrapolated/anecdotal · D traditional/marketed only · X evidence of harm

## Install as an app
Open the GitHub Pages URL once, then: iPhone — Share → Add to Home Screen; Android / desktop Chrome — Install. The service worker caches the app's own files only; nothing is transmitted.

## Build
```
python3 build.py        # kb.py + template.html -> index.html
```
Edit `kb.py` to add entries (schema documented at the top of the file). Bump `VERSION` in `build.py`.

## Deploy
GitHub Pages: push `index.html` to `main`, enable Pages (root).

## Disclaimer
Prototype. Doses are reference values from labels and published formularies; verify against current labels, Plumb's, and FARAD. Not a substitute for a licensed veterinarian. Tier 3C substances are not recommended by this tool.

© 2026 Jae H. Choi, MSc, PhD, DVSc · Auravyx Systems
