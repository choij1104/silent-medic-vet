# Changelog

## v0.1.3 — 2026-09-20
- Tier 6: Osteopathic manipulative treatment (OMT) — dog and horse (evidence C, 4 PMIDs) and Physical therapy / veterinary rehabilitation — dog and horse (evidence B, 4 PMIDs). Texas 22 TAC 573.14 alternate-therapy acknowledgment noted. Other species marked outside scope. Existing chiropractic/osteopathic and controlled-exercise cards unchanged.
- Knowledge base 72 -> 74 entries.

## v0.1.2 — 2026-09-14
- Added 8 DVM prescribing/dispensing reference cards: VCPR; prescription elements and refills; dispensed-drug label; AMDUCA extra-label conditions and records; controlled substances (DEA + Texas); compounding (FDA GFI #256); VFD and GFI #263; prescription portability and online pharmacies. Regulatory text verified against eCFR, FDA, TBVME and AVMA sources. No doses.
- Touch targets: species chips, tier filters, mode switch, decision-support option buttons and weight input raised to 44 px minimum height.
- Knowledge base 64 -> 72 entries. README and docs/v0.2_plan.md (section 3e) updated.

## v0.1.1 — 2026-09-07
- Withdrawal completeness rule appended to kb.py: 211 food-animal cells lacking a withdrawal string now show FARAD, Per label, a topical statement, or n/a for procedures. No existing cell edited; no new label numbers.
- backup/ folder with pre-edit v0.1.0 copies.

## v0.1.0 — 2026-09-06
- Initial release: 64 entries x 13 species, 6 treatment tiers, evidence grades A-D/X, Tier 3C red band, 21 CFR 530.41 card, 11 problem flows, offline single-file PWA with gzip+base64 KB and SHA-256 integrity check.
