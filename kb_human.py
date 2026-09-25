# SILENT MEDIC VET — Tier 7 · Human medicines at home (v0.2.0, ophthalmic pilot)
# Human products an owner may already have. Same schema as kb.py; `cond` links to condition ids in cond.py.
# Status: ok = used in veterinary practice (dose differs) | caution = conditional | no = do not use.
# Doses appear in Veterinarian mode only for rx products; OTC items show "Typical use" to owners.

FOODNOTE = "Human product in a food animal is extra-label — VCPR and FARAD withdrawal required."

def _food(s="caution", n=FOODNOTE, w="FARAD"):
    return {"s": s, "n": n, "w": w}

def extend(add, FOOD):
    F = lambda **k: {sp: _food(**k) for sp in FOOD}

    add(n="Artificial tears / lubricating eye drops and gels", a=["Refresh", "Systane", "GenTeal", "carboxymethylcellulose", "hyaluronate eye drops", "lubricant eye gel"],
        tier=7, cls="Human medicine — ophthalmic lubricant", rx="otc",
        ind=["dry eye", "KCS", "eye irritation", "tearing", "eye", "conjunctivitis", "exposure", "proptosis", "lubricant"], ev="C",
        evn="Standard supportive care for tear-film disorders; controlled data in animals are limited. Preservative-free single-dose vials are preferred for frequent use.",
        sp={"dog": {"s": "ok", "d": "1 drop q4-6h, or gel q6-8h", "n": "Plain lubricant only — not 'redness relief'."},
            "cat": {"s": "ok", "d": "1 drop q4-6h, or gel q6-8h", "n": "Plain lubricant only."},
            "rabbit": {"s": "ok", "d": "1 drop q6-8h", "n": "Plain lubricant only."},
            "horse": {"s": "ok", "d": "Per veterinarian (subpalpebral lavage systems are common)", "n": "Painful equine eyes need an exam first."}}
           | F(s="ok", n="Lubricant only; no drug residue expected.", w="None (lubricant)"),
        owner="Plain lubricating drops or gel from any pharmacy are safe and soothing. They relieve symptoms; they do not treat the cause. Avoid anything labeled 'redness relief' or 'get the red out'.",
        dvm="Adjunct for KCS (with a lacrimomimetic), exposure keratopathy, proptosis before replacement, and post-anesthesia. Hyaluronate-based products have better retention.",
        rf="Eye held shut, cloudy, bulging, or painful — lubricant is not treatment.",
        cond=["kcs", "conjunctivitis", "corneal-ulcer", "proptosis", "epiphora"])

    add(n="Redness-relief eye drops (tetrahydrozoline, naphazoline) — DO NOT USE", a=["Visine", "Clear Eyes", "Naphcon", "Opcon-A", "get the red out"],
        tier=7, cls="Human medicine — imidazoline decongestant (toxic)", rx="otc",
        ind=["red eye", "eye", "redness", "visine", "poisoning", "chewed bottle"], ev="X",
        evn="Imidazoline decongestants mask redness without treating the cause. Ingestion (a chewed bottle) causes vomiting, bradycardia, hypotension or hypertension, and CNS depression in dogs and cats.",
        sp={k: {"s": "no", "n": "Do not use. Chewed bottle = call poison control."} for k in ["dog", "cat", "rabbit", "horse"]}
           | F(s="no", n="Do not use.", w="n/a — do not use"),
        owner="Never put 'redness relief' drops in an animal's eye — they hide the problem the vet needs to see. If a pet chews the bottle, call ASPCA Poison Control (888-426-4435) or Pet Poison Helpline (855-764-7661) now.",
        dvm="Imidazoline (alpha-2 agonist) toxicosis after ingestion: bradycardia, hypotension (occasionally hypertension), CNS depression, vomiting. Supportive care; atipamezole or yohimbine have been used for reversal.",
        rf="Chewed bottle; slow heartbeat, weakness, wobbling, or vomiting after exposure.",
        cond=["conjunctivitis"])

    add(n="Antihistamine eye drops (ketotifen, olopatadine)", a=["Zaditor", "Alaway", "Pataday", "Patanol", "allergy eye drops"],
        tier=7, cls="Human medicine — ophthalmic H1 antihistamine / mast-cell stabilizer", rx="otc",
        ind=["allergic conjunctivitis", "itchy eyes", "allergy", "eye", "red eye", "atopy", "tearing"], ev="C",
        evn="Extra-label; extrapolated from human data and clinical use. Topical dosing avoids the anticholinergic effects of oral first-generation antihistamines.",
        sp={"dog": {"s": "caution", "d": "Ketotifen 0.025%: 1 drop q12h. Olopatadine 0.1%: q12h; 0.2-0.7%: q24h", "n": "Only after glaucoma, ulcer, and dry eye are ruled out. Stop if no improvement in 3-5 days."},
            "cat": {"s": "caution", "d": "Ketotifen 0.025%: 1 drop q12h", "n": "Allergic conjunctivitis is uncommon in cats — herpesvirus is far more likely."},
            "rabbit": {"s": "caution", "n": "Limited data; eye discharge in rabbits is usually dental or tear-duct related."},
            "horse": {"s": "caution", "n": "Limited data; painful equine eyes need an exam first."}} | F(),
        owner="Pharmacy allergy eye drops can help an itchy, watery eye when both eyes are affected and there is no squinting or cloudiness. If nothing changes in 3-5 days, it is not allergy — see the vet.",
        dvm="Reasonable trial for bilateral allergic conjunctivitis in atopic dogs once fluorescein, STT, and IOP are normal. Separate from other drops by 5 min.",
        rf="Squinting, cloudy cornea, unequal pupils, one eye only with pain.",
        cond=["conjunctivitis", "epiphora"])

    add(n="Fluoroquinolone eye drops (ofloxacin, ciprofloxacin, moxifloxacin)", a=["Ocuflox", "Ciloxan", "Vigamox", "ofloxacin 0.3%"],
        tier=7, cls="Human medicine — ophthalmic fluoroquinolone antibiotic", rx="rx",
        ind=["corneal ulcer", "bacterial conjunctivitis", "eye infection", "eye", "ulcer", "melting ulcer"], ev="B",
        evn="Widely used in veterinary ophthalmology for corneal ulcers; good Gram-negative (including Pseudomonas) coverage. Topical fluoroquinolones do not carry the retinal risk of systemic enrofloxacin in cats.",
        sp={"dog": {"s": "ok", "d": "1 drop q6-8h (uncomplicated ulcer); q1-2h loading for infected or melting ulcers per ophthalmologist", "n": "No improvement on an antibiotic usually means the cause is not bacterial — look for hair, dry eye, glaucoma, or an indolent ulcer."},
            "cat": {"s": "ok", "d": "1 drop q6-8h", "n": "Topical use acceptable. Herpesvirus is the usual cause of feline ulcers — add antiviral therapy, not just antibiotic."},
            "rabbit": {"s": "ok", "d": "1 drop q6-8h", "n": "Commonly used."},
            "horse": {"s": "ok", "d": "Per veterinarian; often via subpalpebral lavage", "n": "Equine ulcers can turn fungal — needs cytology/culture."}} | F(),
        owner="A prescription antibiotic drop. Using a family member's bottle is not a substitute for an exam: if the eye has not improved in 2-3 days, the problem is probably not infection.",
        dvm="Prophylaxis for superficial ulcers; q1-2h for infected/melting stromal ulcers with anti-collagenase therapy. Using a human prescription in an animal is extra-label (AMDUCA) and requires a veterinarian's order.",
        reg="Human Rx product; animal use is extra-label under AMDUCA (21 CFR 530) and requires a VCPR.",
        rf="Cloudy or gel-like cornea, a visible pit, bulging eye, or no improvement after 48 h.",
        cond=["corneal-ulcer", "conjunctivitis", "fhv1"])

    add(n="Triple antibiotic eye ointment (neomycin, polymyxin B, bacitracin)", a=["Neosporin Ophthalmic", "NPB ophthalmic", "BNP ointment", "Terramycin (oxytetracycline-polymyxin)"],
        tier=7, cls="Human medicine — ophthalmic antibiotic combination", rx="rx",
        ind=["corneal ulcer", "bacterial conjunctivitis", "eye infection", "eye"], ev="B",
        evn="Common first-line topical antibiotic in dogs. In cats, anaphylaxis within 4 h of ophthalmic antibiotic application has been reported (61 cats; polymyxin B present in every case).",
        sp={"dog": {"s": "ok", "d": "1/4-inch strip q6-8h", "n": "Ophthalmic tube only."},
            "cat": {"s": "caution", "d": "Per veterinarian", "n": "Anaphylaxis reported with polymyxin B-containing eye products (PMID 21906985). Observe closely after first doses."},
            "rabbit": {"s": "ok", "d": "1/4-inch strip q8h", "n": ""},
            "horse": {"s": "ok", "d": "Per veterinarian", "n": ""}} | F(),
        owner="Only the tube labeled 'ophthalmic' can go in an eye. The skin ointment (regular Neosporin) is not sterile or formulated for eyes. In cats, use only if your vet prescribes it and watch for vomiting, drooling, or breathing trouble.",
        dvm="Cats: rare but serious anaphylaxis, usually within 10 min. Prefer alternatives when practical and counsel owners.",
        refs=["Hume-Smith KM, Groth AD, Rishniw M, et al. Anaphylactic events observed within 4 h of ocular application of an antibiotic-containing ophthalmic preparation: 61 cats (1993-2010). J Feline Med Surg. 2011;13(10):744-751. PMID 21906985"],
        rf="Cat that collapses, vomits, drools, or struggles to breathe after an eye ointment — emergency.",
        cond=["corneal-ulcer", "conjunctivitis"])

    add(n="Steroid or steroid-antibiotic eye drops (prednisolone, dexamethasone)", a=["Pred Forte", "Maxitrol", "TobraDex", "neomycin-polymyxin-dexamethasone"],
        tier=7, cls="Human medicine — ophthalmic corticosteroid", rx="rx",
        ind=["uveitis", "allergic conjunctivitis", "eye inflammation", "eye", "red eye"], ev="B",
        evn="Effective anti-inflammatory for uveitis and allergic conjunctivitis — and the most dangerous drop to use without a stain test: it delays healing and can turn a corneal ulcer into a perforation.",
        sp={"dog": {"s": "caution", "d": "Prednisolone acetate 1%: 1 drop q6-12h ONLY after a negative fluorescein stain", "n": "Never with a corneal ulcer."},
            "cat": {"s": "caution", "d": "Per veterinarian after a negative stain", "n": "Can reactivate feline herpesvirus."},
            "rabbit": {"s": "caution", "n": "Rabbits are corticosteroid-sensitive; systemic absorption from drops is possible."},
            "horse": {"s": "caution", "n": "Never with an ulcer — fungal keratitis risk. Used for recurrent uveitis under veterinary care."}} | F(),
        owner="Do not use any eye drop containing a steroid (prednisolone, dexamethasone, 'Maxitrol', 'TobraDex') unless a vet has just stained the eye and found no ulcer. On an ulcer it can cause the eye to rupture.",
        dvm="Confirm fluorescein-negative before every new course. Topical NSAIDs (flurbiprofen, diclofenac) are an alternative when steroid is contraindicated, with caution on the ulcerated cornea.",
        reg="Human Rx product; extra-label under AMDUCA.",
        rf="Eye gets more painful, cloudy, or bulging after starting a steroid drop — stop and go now.",
        cond=["uveitis", "conjunctivitis", "corneal-ulcer"])

    add(n="Latanoprost (prostaglandin glaucoma drops)", a=["Xalatan", "latanoprost 0.005%", "Lumigan (bimatoprost)", "Travatan (travoprost)"],
        tier=7, cls="Human medicine — ophthalmic prostaglandin analogue", rx="rx",
        ind=["glaucoma", "high eye pressure", "IOP", "eye", "lens luxation"], ev="B",
        evn="Lowers IOP substantially in dogs with primary glaucoma; minimal IOP effect in cats. Causes marked miosis.",
        sp={"dog": {"s": "caution", "d": "1 drop q12-24h (acute primary glaucoma per ophthalmologist)", "n": "Contraindicated with uveitis or anterior lens luxation (pupil block)."},
            "cat": {"s": "no", "n": "Little IOP effect in cats; feline glaucoma is usually secondary to uveitis."},
            "rabbit": {"s": "caution", "n": "Limited data; referral."},
            "horse": {"s": "caution", "n": "Not first-line — equine glaucoma usually follows uveitis, which prostaglandins can worsen."}} | F(),
        owner="A human glaucoma drop that vets do use in dogs — but only after the eye pressure has been measured and the lens checked. Never start it on your own.",
        dvm="Primary angle-closure glaucoma in dogs: combine with dorzolamide ± timolol, mannitol if needed, same-day ophthalmology referral. Prophylaxis of the fellow eye delays onset.",
        reg="Human Rx product; extra-label under AMDUCA.",
        rf="Red, cloudy, painful eye with a dilated pupil — emergency.",
        cond=["glaucoma", "lens-luxation"])

    add(n="Dorzolamide / dorzolamide-timolol (glaucoma drops)", a=["Trusopt", "Cosopt", "timolol 0.5%"],
        tier=7, cls="Human medicine — ophthalmic carbonic anhydrase inhibitor ± beta-blocker", rx="rx",
        ind=["glaucoma", "high eye pressure", "IOP", "eye"], ev="B",
        evn="Lowers aqueous production; mainstay for primary and secondary glaucoma in dogs, cats, and horses. Timolol adds systemic beta-blockade.",
        sp={"dog": {"s": "ok", "d": "Dorzolamide 2%: 1 drop q8h; dorzolamide-timolol: 1 drop q8-12h", "n": "Timolol: caution in small dogs (bradycardia) and with heart or airway disease."},
            "cat": {"s": "caution", "d": "Dorzolamide 2%: 1 drop q8h", "n": "Avoid timolol in asthmatic cats (bronchospasm) and small cats (bradycardia)."},
            "rabbit": {"s": "caution", "n": "Limited data."},
            "horse": {"s": "ok", "d": "Dorzolamide-timolol q8-12h per veterinarian", "n": "Preferred IOP-lowering drop in horses."}} | F(),
        owner="A human glaucoma drop used in pets after the eye pressure has been measured.",
        dvm="Maintenance and fellow-eye prophylaxis. Monitor heart rate with timolol.",
        reg="Human Rx product; extra-label under AMDUCA.",
        rf="Weakness, slow heartbeat, or breathing difficulty after drops.",
        cond=["glaucoma", "uveitis", "lens-luxation"])

    add(n="Atropine 1% eye drops or ointment", a=["Isopto Atropine", "atropine sulfate ophthalmic"],
        tier=7, cls="Human medicine — ophthalmic anticholinergic (cycloplegic)", rx="rx",
        ind=["corneal ulcer pain", "uveitis", "ciliary spasm", "eye pain", "eye"], ev="B",
        evn="Relieves ciliary spasm pain and stabilizes the blood-aqueous barrier. Reduces tear production and can raise IOP.",
        sp={"dog": {"s": "caution", "d": "1 drop q12-24h to effect (pupil dilated)", "n": "Contraindicated in glaucoma, lens luxation, and dry eye."},
            "cat": {"s": "caution", "d": "Ointment q12-24h preferred", "n": "Bitter drops reach the mouth via the tear duct — cats foam and drool (not toxicity)."},
            "rabbit": {"s": "caution", "n": "Many rabbits carry atropinesterase — effect may be weak or absent."},
            "horse": {"s": "caution", "d": "Per veterinarian", "n": "Frequent dosing can slow gut motility — monitor manure and gut sounds (colic risk)."}} | F(),
        owner="A prescription drop that relieves eye pain by relaxing the eye muscle. It can trigger glaucoma in the wrong eye — only after an exam.",
        dvm="Measure IOP and STT first. Taper once the pupil stays dilated.",
        reg="Human Rx product; extra-label under AMDUCA.",
        rf="Eye becomes cloudier or more painful after atropine (possible IOP spike).",
        cond=["corneal-ulcer", "uveitis"])

    add(n="Cyclosporine eye drops (human 0.05-0.1%)", a=["Restasis", "Cequa", "Optimmune (veterinary 0.2%)", "tacrolimus (compounded)"],
        tier=7, cls="Human medicine — ophthalmic immunomodulator (lacrimomimetic)", rx="rx",
        ind=["dry eye", "KCS", "keratoconjunctivitis sicca", "pannus", "eye"], ev="C",
        evn="Canine KCS is treated with veterinary cyclosporine 0.2% ointment (Optimmune, FDA-approved for dogs) or compounded tacrolimus. Human 0.05-0.1% products are lower strength and extra-label.",
        sp={"dog": {"s": "caution", "d": "Veterinary cyclosporine 0.2% ointment q12h is standard; human 0.05% is a lower-strength substitute", "n": "Lifelong therapy; recheck tear test at 4-6 weeks."},
            "cat": {"s": "caution", "n": "KCS is uncommon in cats; often herpesvirus-related."},
            "rabbit": {"s": "caution", "n": "Limited data."},
            "horse": {"s": "caution", "n": "Used in immune-mediated keratitis under an ophthalmologist."}} | F(),
        owner="Dry eye in dogs is lifelong and needs a tear-stimulating drug, not just antibiotics. The veterinary version (Optimmune) is stronger than human Restasis.",
        dvm="If STT does not rise after 6-8 weeks on cyclosporine, switch to tacrolimus 0.02-0.03%. Neurogenic KCS (dry nostril on the same side): oral pilocarpine. Refractory: parotid duct transposition.",
        reg="Human Rx product; extra-label under AMDUCA. Veterinary cyclosporine 0.2% is FDA-approved for dogs.",
        rf="Thick discharge with a cloudy, painful eye — possible ulcer on top of dry eye.",
        cond=["kcs"])

    add(n="Famciclovir (Famvir, oral antiviral)", a=["Famvir", "famciclovir 125 mg", "famciclovir 250 mg", "famciclovir 500 mg"],
        tier=7, cls="Human medicine — oral antiviral (penciclovir prodrug)", rx="rx",
        ind=["feline herpesvirus", "FHV-1", "herpes eye cat", "cat conjunctivitis", "cat corneal ulcer", "cat upper respiratory"], ev="B",
        evn="Cats with presumed FHV-1 improved in a 59-case series; pharmacokinetic work supports 90 mg/kg q12h to reach tear concentrations. A single dose at shelter intake was not effective.",
        sp={"dog": {"s": "no", "n": "Not indicated."},
            "cat": {"s": "ok", "d": "90 mg/kg PO q12h", "n": "Generic human tablets are what vets dispense. Continue until 1 week after signs resolve."},
            "rabbit": {"s": "no", "n": "Not indicated."},
            "horse": {"s": "caution", "n": "Equine herpesvirus keratitis — specialist use only."}} | F(s="no", n="Not indicated; human antiviral in a food animal.", w="n/a — do not use"),
        owner="A human antiviral pill that vets prescribe for cats with herpes eye flare-ups. Never share a person's prescription without the vet setting the dose.",
        dvm="Most useful in herpetic keratitis/conjunctivitis and dermatitis. Mild GI signs and polyuria reported.",
        reg="Human Rx product; extra-label under AMDUCA.",
        refs=["Thomasy SM, Shull O, Outerbridge CA, et al. Oral administration of famciclovir for treatment of spontaneous ocular, respiratory, or dermatologic disease attributed to feline herpesvirus type 1: 59 cases (2006-2013). J Am Vet Med Assoc. 2016;249(5):526-538. PMID 27556267",
              "Sebbag L, Thomasy SM, Woodward AP, et al. Pharmacokinetic modeling of penciclovir and BRL42359 in the plasma and tears of healthy cats to optimize dosage recommendations for oral administration of famciclovir. Am J Vet Res. 2016;77(8):833-845. PMID 27463546",
              "Litster AL, Lohr BR, Bukowy RA, Thomasy SM, Maggs DJ. Clinical and antiviral effect of a single oral dose of famciclovir administered to cats at intake to a shelter. Vet J. 2015;203(2):199-204. PMID 25542064"],
        rf="Kitten not eating, eyes sealed shut, or a cloudy cornea.",
        cond=["fhv1", "corneal-ulcer", "conjunctivitis"])

    add(n="L-lysine (supplement)", a=["Viralys", "Enisyl-F", "lysine treats", "lysine gel"],
        tier=7, cls="Human/pet supplement — amino acid", rx="supp",
        ind=["feline herpesvirus", "FHV-1", "cat eye", "cat sneezing", "herpes"], ev="X",
        evn="A systematic review found no evidence of efficacy for prevention or treatment of FHV-1 in cats; some studies reported more frequent or more severe disease with supplementation.",
        sp={"dog": {"s": "no", "n": "No indication."},
            "cat": {"s": "no", "n": "Not effective; some studies reported worse disease."},
            "rabbit": {"s": "no", "n": "No indication."},
            "horse": {"s": "no", "n": "No indication."}} | F(s="no", n="No indication.", w="n/a — do not use"),
        owner="Lysine is widely sold for cats with herpes, but the evidence shows it does not work. Spend the money on a vet visit and a proven antiviral instead.",
        dvm="Recommend discontinuation (Bol and Bunnik 2015).",
        refs=["Bol S, Bunnik EM. Lysine supplementation is not effective for the prevention or treatment of feline herpesvirus 1 infection in cats: a systematic review. BMC Vet Res. 2015;11:284. PMID 26573523"],
        rf="",
        cond=["fhv1"])

    add(n="Cetirizine / loratadine (plain, non-drowsy antihistamines)", a=["Zyrtec", "Claritin", "Allegra (fexofenadine)", "Zyrtec-D / Claritin-D (NEVER)"],
        tier=7, cls="Human medicine — oral second-generation H1 antihistamine", rx="otc",
        ind=["allergy", "itching", "allergic conjunctivitis", "hives", "atopy", "eye"], ev="C",
        evn="Modest benefit at best for canine atopic itch; widely used. Little anticholinergic effect, unlike diphenhydramine. The '-D' versions contain pseudoephedrine, which is toxic.",
        sp={"dog": {"s": "caution", "d": "Cetirizine 1 mg/kg PO q12-24h; loratadine per veterinarian", "n": "Plain product only — check the box for '-D' or pseudoephedrine."},
            "cat": {"s": "caution", "d": "Cetirizine 1 mg/kg (about 5 mg/cat) PO q24h", "n": "Plain product only."},
            "rabbit": {"s": "caution", "n": "Limited data."},
            "horse": {"s": "caution", "n": "Cetirizine is used in horses by veterinarians; oral human tablets are impractical at horse doses."}} | F(),
        owner="Plain Zyrtec or Claritin can be used in dogs and cats with vet guidance. NEVER the '-D' versions (Zyrtec-D, Claritin-D, Allegra-D): the decongestant can kill a pet.",
        dvm="Preferred over diphenhydramine when dry eye or glaucoma has not been excluded. Pseudoephedrine ingestion: agitation, tachycardia, hyperthermia, seizures.",
        rf="Any '-D' product swallowed; restlessness, racing heart, or tremors — poison control now.",
        cond=["conjunctivitis"])
