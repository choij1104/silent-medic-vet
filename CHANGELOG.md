# Changelog

## v0.2.0 — 2026-09-24
- **Conditions tab (new).** Disease cards with a triage band (Emergency / 24 h / Book a visit / Home care), escalation signs, species-specific notes, at-risk breeds, owner actions, do-nots, human medicines at home, and — in Veterinarian view — diagnostics, treatment direction, and linked KB entries. Zoonosis and Texas badges. Ophthalmic pilot: 12 conditions (corneal ulcer/SCCED, KCS, glaucoma, uveitis, conjunctivitis, eyelid/hair disorders, cherry eye, FHV-1, cataract vs nuclear sclerosis, proptosis, lens luxation, epiphora). Species: dog and cat; rabbit and horse where applicable.
- **Breed search.** Typing a breed in Conditions (e.g. Shih Tzu) lists the conditions it is predisposed to and flags the match inside the card.
- **Tier 7 — Human medicines at home (new).** 13 cross-reference cards for human products an owner may already have, graded per species ok / caution / do not use: artificial tears, redness-relief drops (do not use), ketotifen/olopatadine drops, fluoroquinolone drops, triple antibiotic ophthalmic (feline anaphylaxis), steroid drops, latanoprost, dorzolamide/timolol, atropine, cyclosporine, famciclovir, L-lysine (not effective), cetirizine/loratadine (never '-D'). Formulation traps and AMDUCA extra-label note on each. KB 81 -> 94.
- **Decision support: Eye flow (new, 12th problem).** Red flags, do/do-not, three-test prompt (STT, fluorescein, IOP), onset-specific notes, possible causes ordered by urgency (tap to open the condition), human medicines at home with species status, species notes for rabbit, horse, cattle (pinkeye), and poultry.
- Two-way links: condition -> human medicine / KB entry; human medicine -> related conditions; plan -> condition.
- Knowledge payload is now {kb, cond} under the same gzip+base64 SHA-256 integrity check; build.py validates every cross-link before writing index.html.
- References added (PubMed-verified): PMIDs 21906985, 26573523, 14982589, 7768741, 27556267, 27463546, 25542064, 22520040.
- Nothing removed: all 81 prior entries, 11 problem flows, both views, and every species/tier are unchanged. kb.py is untouched (tier 7 is appended by build.py). v0.1.9 sources are preserved in git history (commit 460c436).
- template.html changes ship as tools/template_v020.diff (git apply, verified byte-identical); .github/workflows/build.yml applies pending diffs, runs build.py, and commits template.html, index.html and sw.js.

## v0.1.9 — 2026-09-20
- Decision support: the Lameness / joint / muscle plan for dog and horse now includes a 'Rehabilitation, manual and integrative therapy' section linking the physical therapy, acupuncture, OMT, chiropractic, holistic and laser/PEMF/shockwave cards, with the Texas 573.14/573.16 note.
- Tier 5: Holistic / integrative veterinary medicine — dog and horse (framework card; evidence C overall, modality grades referenced; Texas 573.16 veterinarian-only and acknowledgment; PMIDs 27200270, 25576265). KB 80 -> 81.
- Rehab & Manual Therapy view now preselects tiers 4, 5 and 6 (nutraceutical, herbal/holistic, manual). The URL hash is no longer written when the view is selected, and a deep-link hash is cleared after it is applied, so reloads, bookmarks and the installed app always open on All (13 species, 6 tiers). Nothing was removed from the knowledge base at any point.

## v0.1.8 — 2026-09-20
- Progressive Web App: manifest.webmanifest, sw.js (cache-first with background revalidation, cache name stamped with the app version by build.py), icon-192/512, install button in the footer (shown when the browser offers install). Installs to the home screen on iOS, Android and desktop; opens with no network after the first visit. No content change.

## v0.1.7 — 2026-09-20
- Visual redesign matching the SILENT MEDIC family: cobalt header/footer (#0d47a1), white panels on a cool grey ground, bold high-contrast type (16 px base), monospace for doses, KB status and hints, blue primary controls, status badges with tinted backgrounds. Markup IDs, logic, content and 44 px targets unchanged.

## v0.1.6 — 2026-09-20
- v0.2 ruminant/swine batch 1 (Tier 1 OTC): albendazole (Valbazen NADA 110-048), levamisole (Prohibit ANADA 200-225), morantel tartrate (Rumatel NADA 092-444), moxidectin (Cydectin NADA 141-099/141-220/141-247), decoquinate (Deccox NADA 039-417). Doses, withdrawals and restrictions taken from DailyMed labels; extra-label cells carry FARAD. KB 75 -> 80.

## v0.1.5 — 2026-09-20
- Acupuncture card: regulatory text updated to Texas 22 TAC 573.16 (2026 combined acupuncture/holistic/homeopathy rule: veterinarian only, conventional-treatment disclosure, signed owner acknowledgment); evidence note and 2 verified PMIDs (17867976, 20513202) added.
- New DVM reference card: Alternate therapies — Texas law (573.14 manipulation; 573.16 acupuncture/holistic/homeopathy). KB 74 -> 75.

## v0.1.4 — 2026-09-20
- View presets: 'All' and 'Rehab & Manual Therapy' (dog and horse only, tiers 4 and 6 preselected, note on Texas 22 TAC 573.14). Deep link `#view=rehab`. Additive — every species and tier remains available under 'All'.

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
