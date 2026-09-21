# SILENT MEDIC VET — knowledge base v0.2.0-a
# ev: A strong controlled data in target species | B some controlled data / label-approved | C extrapolated or anecdotal | D traditional, no controlled data | X evidence of harm
# rx: otc | rx | unapproved | supp | proc
# sp status s: ok | caution | no ; d = dose (DVM mode only) ; w = withdrawal ; n = note
FOOD=["cattle","sheep","goat","deer","pig","chicken","duck","turkey","peafowl"]
KB=[]
def add(**e): KB.append(e)

# ───────── TIER 1 · OTC PHARMACEUTICAL ─────────
add(n="Fenbendazole",a=["Panacur","Safe-Guard"],tier=1,cls="Benzimidazole anthelmintic",rx="otc",
 ind=["deworming","roundworm","hookworm","whipworm","Giardia","lungworm","tapeworm Taenia","E. cuniculi"],ev="A",
 evn="Label-approved in dogs, horses, cattle, goats, swine, chickens (AquaSol). Wide safety margin.",
 sp={"dog":{"s":"ok","d":"50 mg/kg PO q24h x3 d (Giardia: 5 d)","n":"Approved."},
     "cat":{"s":"ok","d":"50 mg/kg PO q24h x3-5 d","n":"Extra-label, widely used."},
     "rabbit":{"s":"ok","d":"20 mg/kg PO q24h x5-28 d (E. cuniculi)","n":"Extra-label."},
     "horse":{"s":"ok","d":"5 mg/kg PO once; 10 mg/kg x5 d for encysted small strongyles","n":"Approved. Resistance common in cyathostomins."},
     "cattle":{"s":"ok","d":"5 mg/kg PO","w":"Meat 8 d (Safe-Guard); milk 0 d","n":"Approved; check product label."},
     "sheep":{"s":"caution","d":"5 mg/kg PO","w":"Extra-label; FARAD","n":"No US label for sheep; resistance common."},
     "goat":{"s":"ok","d":"5 mg/kg PO (10 mg/kg often used extra-label)","w":"Meat 6 d; milk 0 d at label dose","n":"Approved at 5 mg/kg; higher doses are extra-label."},
     "deer":{"s":"caution","d":"5-10 mg/kg PO","w":"Extra-label; FARAD","n":"Farmed deer are food animals."},
     "pig":{"s":"ok","d":"5 mg/kg PO (or 3 mg/kg/d x3 d in feed)","w":"Per label (0 d for Safe-Guard swine)","n":"Approved."},
     "chicken":{"s":"ok","d":"1 mg/kg/d in water x5 d (Safe-Guard AquaSol)","w":"0 d eggs, 0 d meat (AquaSol label)","n":"Approved for laying hens — one of few OTC dewormers with a defined egg withdrawal."},
     "duck":{"s":"caution","d":"Extrapolated from chicken","w":"Undefined; FARAD","n":"Extra-label."},
     "turkey":{"s":"ok","d":"Per label (AquaSol turkeys)","w":"Per label","n":"Approved."},
     "peafowl":{"s":"caution","d":"Extrapolated","w":"Undefined","n":"Extra-label."}},
 owner="Broad-spectrum dewormer sold at feed stores. Safe in most species. Fecal test first when possible — blind deworming drives resistance.",
 dvm="Prohibited: none. Extra-label use in food animals requires VCPR and FARAD withdrawal. Do not combine with bromsalans in cattle.",
 rf="Bloody diarrhea, weight loss, pale gums, or no improvement after treatment.")

add(n="Ivermectin",a=["Ivomec","Heartgard (Rx)","Eqvalan"],tier=1,cls="Macrocyclic lactone",rx="otc",
 ind=["deworming","mites","lice","ear mites","heartworm prevention","bots","strongyles","mange"],ev="A",
 evn="Label-approved in horses, cattle, sheep, swine. Injectable/pour-on OTC; canine heartworm preventives are Rx.",
 sp={"dog":{"s":"caution","d":"6 mcg/kg PO monthly (HW prevention, Rx products); extra-label mange 300-600 mcg/kg","n":"MDR1 (ABCB1) mutant breeds — Collie, Aussie, Sheltie, LH Whippet — can die at mange doses. Test before extra-label dosing."},
     "cat":{"s":"caution","d":"24 mcg/kg PO monthly (HW); 200-300 mcg/kg SC for ear mites (extra-label)","n":"Neurotoxicity reported; kittens more sensitive."},
     "rabbit":{"s":"ok","d":"400 mcg/kg SC q14d x2-3 (ear mites)","n":"Extra-label; well tolerated."},
     "horse":{"s":"ok","d":"200 mcg/kg PO paste","n":"Approved. Ineffective vs tapeworms (add praziquantel)."},
     "cattle":{"s":"ok","d":"200 mcg/kg SC or 500 mcg/kg pour-on","w":"Injectable meat 35 d; pour-on 48 d; not for lactating dairy","n":"Approved. Check label."},
     "sheep":{"s":"ok","d":"200 mcg/kg PO drench","w":"Meat 11 d","n":"Approved drench; resistance common."},
     "goat":{"s":"caution","d":"400 mcg/kg PO (extra-label)","w":"FARAD","n":"No US label; goats metabolize faster."},
     "deer":{"s":"caution","d":"200 mcg/kg SC","w":"FARAD","n":"Extra-label."},
     "pig":{"s":"ok","d":"300 mcg/kg SC","w":"Meat 18 d","n":"Approved."},
     "chicken":{"s":"caution","d":"200-400 mcg/kg PO/topical (extra-label)","w":"UNDEFINED — no egg withdrawal data","n":"Not approved in poultry. Egg residue risk; do not use in layers without veterinary guidance."},
     "duck":{"s":"caution","d":"Extra-label","w":"Undefined","n":"Not approved."},
     "turkey":{"s":"caution","d":"Extra-label","w":"Undefined","n":"Not approved."},
     "peafowl":{"s":"caution","d":"Extra-label","w":"Undefined","n":"Not approved."}},
 owner="Feed-store ivermectin is approved for horses, cattle, sheep, pigs. Do NOT dose dogs from livestock products unless your vet has ruled out MDR1 — some herding breeds die from it. Not approved in poultry.",
 dvm="Livestock formulations are not labeled for companion animals. Extra-label use in layers has no established egg withdrawal.",
 rf="Ataxia, tremors, blindness, dilated pupils, drooling within hours of dosing — ivermectin toxicosis, emergency.")

add(n="Pyrantel pamoate",a=["Strongid","Nemex"],tier=1,cls="Tetrahydropyrimidine anthelmintic",rx="otc",
 ind=["deworming","roundworm","hookworm","pinworm","puppies","kittens"],ev="A",evn="Label-approved dogs, horses; safe in young animals.",
 sp={"dog":{"s":"ok","d":"5 mg/kg PO, repeat 2-3 wk","n":"Approved. Safe from 2 wk of age."},
     "cat":{"s":"ok","d":"20 mg/kg PO, repeat 2-3 wk","n":"Extra-label; safe."},
     "rabbit":{"s":"caution","d":"5-10 mg/kg PO","n":"Extra-label; rarely indicated (pinworms)."},
     "horse":{"s":"ok","d":"6.6 mg/kg PO paste (13.2 mg/kg for tapeworms)","n":"Approved."},
     "cattle":{"s":"no","n":"Not used."},"sheep":{"s":"no","n":"Not used."},"goat":{"s":"no","n":"Not used."},"deer":{"s":"no","n":"Not used."},
     "pig":{"s":"ok","d":"Per feed label (Banminth)","w":"Meat 1 d","n":"Approved in feed."},
     "chicken":{"s":"caution","d":"Extra-label","w":"Undefined","n":"Not approved."},"duck":{"s":"caution","n":"Not approved."},"turkey":{"s":"caution","n":"Not approved."},"peafowl":{"s":"caution","n":"Not approved."}},
 owner="Gentle dewormer for roundworms and hookworms; the standard puppy/kitten dewormer. Does not treat tapeworms or whipworms.",
 dvm="Narrow spectrum. Pair with praziquantel for tapeworms.",rf="Persistent vomiting, pot belly with poor growth, or worms in vomit.")

add(n="Praziquantel",a=["Droncit","tapeworm tablets"],tier=1,cls="Isoquinoline cestocide",rx="otc",
 ind=["tapeworm","Dipylidium","Taenia","Anoplocephala"],ev="A",evn="Label-approved dogs, cats, horses (combination pastes).",
 sp={"dog":{"s":"ok","d":"5 mg/kg PO once","n":"OTC tablets available."},"cat":{"s":"ok","d":"5 mg/kg PO once","n":"OTC tablets available. Treat fleas or tapeworms return."},
     "rabbit":{"s":"caution","d":"5-10 mg/kg PO","n":"Rarely indicated."},"horse":{"s":"ok","d":"1-1.5 mg/kg PO (in combination pastes)","n":"Approved."},
     "cattle":{"s":"caution","d":"Extra-label","w":"FARAD","n":"No US label."},"sheep":{"s":"caution","d":"Extra-label","w":"FARAD"},"goat":{"s":"caution","d":"Extra-label","w":"FARAD"},"deer":{"s":"caution","w":"FARAD"},
     "pig":{"s":"caution","d":"Extra-label"},"chicken":{"s":"caution","d":"10 mg/kg PO extra-label","w":"Undefined"},"duck":{"s":"caution"},"turkey":{"s":"caution"},"peafowl":{"s":"caution"}},
 owner="Tapeworm-only dewormer. In dogs and cats tapeworms come from fleas — control fleas or they come back.",dvm="Single dose; repeat only if reinfection.",rf="Rice-grain segments persisting after two treatments.")

add(n="Amprolium",a=["Corid"],tier=1,cls="Thiamine-analog coccidiostat",rx="otc",
 ind=["coccidiosis","bloody droppings chicks","calves scours coccidia"],ev="A",evn="Label-approved chickens, turkeys, calves. Zero egg/meat withdrawal at label dose.",
 sp={"dog":{"s":"caution","d":"Extra-label (rarely used; sulfa preferred)","n":"Off-label."},"cat":{"s":"caution","n":"Rarely used."},"rabbit":{"s":"caution","d":"Extra-label","n":"Some use for hepatic coccidiosis."},
     "horse":{"s":"no","n":"Not used."},
     "cattle":{"s":"ok","d":"10 mg/kg/d PO x5 d (treatment); 5 mg/kg x21 d (prevention)","w":"Meat 24 h (label)","n":"Approved calves."},
     "sheep":{"s":"caution","d":"Extra-label","w":"FARAD","n":"Extra-label."},"goat":{"s":"caution","d":"Extra-label","w":"FARAD","n":"Extra-label; polioencephalomalacia risk with prolonged use (thiamine antagonism)."},"deer":{"s":"caution","w":"FARAD"},
     "pig":{"s":"caution","n":"Not typically indicated."},
     "chicken":{"s":"ok","d":"0.012% (moderate) to 0.024% (severe) in drinking water x3-5 d, then half strength 1-2 wk","w":"0 d","n":"Approved; only water source."},
     "duck":{"s":"caution","d":"Extrapolated from chicken","w":"Undefined","n":"Extra-label."},"turkey":{"s":"ok","d":"Per label","w":"0 d","n":"Approved."},"peafowl":{"s":"caution","d":"Extrapolated","n":"Extra-label; peafowl are highly coccidia-susceptible."}},
 owner="First-line for bloody droppings in chicks. Mix in the only water available; do not add vitamins with thiamine during treatment.",
 dvm="Thiamine antagonist — prolonged or high-dose use in ruminants risks PEM. Not effective once clinical disease is advanced in calves; consider sulfas.",
 rf="Chicks that are hunched, cold, not drinking, or dying despite treatment.")

add(n="Permethrin (poultry dust / spray)",a=["Prozap","Y-Tex"],tier=1,cls="Pyrethroid ectoparasiticide",rx="otc",
 ind=["mites","lice","northern fowl mite","red mite","flies","ticks"],ev="B",evn="EPA-registered for poultry, cattle, horses, dogs. Resistance in poultry mites documented.",
 sp={"dog":{"s":"ok","d":"Per product label","n":"Approved dog products exist."},"cat":{"s":"no","n":"TOXIC — cats lack glucuronidation; permethrin spot-ons cause tremors, seizures, death."},
     "rabbit":{"s":"caution","n":"Some products labeled; avoid high concentration."},"horse":{"s":"ok","d":"Per label","n":"Approved."},
     "cattle":{"s":"ok","d":"Per label","w":"0 d most labels","n":"Approved."},"sheep":{"s":"ok","d":"Per label","w":"Per label"},"goat":{"s":"caution","d":"Extra-label","w":"FARAD"},"deer":{"s":"caution"},
     "pig":{"s":"ok","d":"Per label","w":"Per label"},
     "chicken":{"s":"ok","d":"Per label (dust birds + coop; repeat 7-10 d)","w":"0 d (label)","n":"Approved; treat housing or reinfestation is certain."},"duck":{"s":"ok","d":"Per label","w":"Per label"},"turkey":{"s":"ok","d":"Per label"},"peafowl":{"s":"ok","d":"Per label"}},
 owner="Feed-store mite dust. Never on cats — even contact with a treated dog can poison a cat. Treat the coop, roosts, and nest boxes, not just the birds.",
 dvm="Cats: permethrin toxicosis is a leading feline poisoning. Environmental treatment essential for Dermanyssus (red mite lives off-host).",
 rf="Cat with tremors, twitching, or seizures after exposure — emergency.")

add(n="Chlorhexidine (dilute)",a=["Nolvasan","Hibiclens"],tier=1,cls="Topical antiseptic",rx="otc",
 ind=["wound cleaning","hot spot","bumblefoot","skin infection","umbilical"],ev="A",evn="Broad antiseptic with residual activity; superior to povidone-iodine for skin.",
 sp={k:{"s":"ok","d":"0.05% (wound lavage) to 2-4% (skin scrub)","n":"Dilute — concentrate is irritant."} for k in ["dog","cat","rabbit","horse","cattle","sheep","goat","deer","pig","chicken","duck","turkey","peafowl"]},
 owner="Dilute to the color of weak tea for wounds. Keep out of eyes and ears. Do not use full strength.",
 dvm="Avoid in ear if tympanum ruptured (ototoxic). 0.05% for lavage; use saline for joints and body cavities.",
 rf="Deep, puncture, or gaping wounds; wounds over joints; bites — need veterinary closure and antibiotics.")

add(n="Saline wound lavage",a=["0.9% NaCl","sterile saline"],tier=1,cls="Isotonic irrigant",rx="otc",
 ind=["wound cleaning","eye flush","debridement","hoof abscess"],ev="A",evn="Standard of care. Pressure lavage (35 mL syringe + 18-19 g needle ≈ 8 psi) reduces bacterial load.",
 sp={k:{"s":"ok","d":"Copious; 35 mL syringe with 18-19 g catheter for pressure","n":""} for k in ["dog","cat","rabbit","horse","cattle","sheep","goat","deer","pig","chicken","duck","turkey","peafowl"]},
 owner="The safest first step for any wound or eye irritation. Tap water is acceptable if saline is unavailable. Flush a lot, not a little.",
 dvm="Solution to pollution is dilution. Avoid hydrogen peroxide and full-strength antiseptics in wound beds.",rf="Eye that stays closed, cloudy, or painful after flushing.")

add(n="Oral electrolytes / rehydration",a=["Pedialyte","Resorb","Bounce Back","poultry electrolytes"],tier=1,cls="Oral rehydration solution",rx="otc",
 ind=["dehydration","diarrhea","heat stress","scours","transport stress","pasty butt"],ev="A",evn="Calf scours ORS trials; poultry heat stress data; unflavored pediatric ORS acceptable in dogs/cats.",
 sp={"dog":{"s":"ok","d":"Free choice or 5-10 mL/kg/h if not vomiting","n":"Unflavored, no xylitol."},"cat":{"s":"ok","d":"Small volumes; cats often refuse","n":""},"rabbit":{"s":"ok","d":"Free choice","n":"Rabbits must keep eating — anorexia >12 h is an emergency."},
     "horse":{"s":"ok","d":"Provide plain water alongside electrolyte water","n":""},"cattle":{"s":"ok","d":"Calves 2 L q6-8h between milk feedings","w":"0 d","n":"Do not replace milk entirely >24 h."},
     "sheep":{"s":"ok","d":"50-100 mL/kg/d divided","w":"0 d"},"goat":{"s":"ok","d":"50-100 mL/kg/d divided","w":"0 d"},"deer":{"s":"ok","w":"0 d"},"pig":{"s":"ok","d":"Free choice","w":"0 d"},
     "chicken":{"s":"ok","d":"Per label 1-3 d, then plain water","w":"0 d","n":"Do not exceed 3 consecutive days."},"duck":{"s":"ok","w":"0 d"},"turkey":{"s":"ok","w":"0 d"},"peafowl":{"s":"ok","w":"0 d"}},
 owner="Best OTC support for diarrhea or heat stress. Always offer plain water too. An animal that cannot keep fluids down needs a vet.",
 dvm="Oral route fails with ileus or >8% dehydration — IV/SC fluids indicated.",rf="Sunken eyes, skin tent >2 s, no urination, collapse.")

add(n="Diphenhydramine",a=["Benadryl"],tier=1,cls="H1 antihistamine",rx="otc",
 ind=["allergic reaction","hives","insect sting","itching","vaccine reaction","motion sickness"],ev="B",evn="Widely used; limited controlled data for pruritus. Plain diphenhydramine only.",
 sp={"dog":{"s":"ok","d":"2-4 mg/kg PO q8-12h","n":"Plain tablets only — no decongestant, no xylitol liquids."},"cat":{"s":"ok","d":"2-4 mg/kg PO q8-12h","n":"May cause excitation."},"rabbit":{"s":"caution","d":"2 mg/kg PO","n":"Limited data."},
     "horse":{"s":"caution","d":"1 mg/kg IV/IM (vet)","n":"Oral bioavailability poor."},"cattle":{"s":"caution","d":"Extra-label","w":"FARAD","n":""},"sheep":{"s":"caution","w":"FARAD"},"goat":{"s":"caution","w":"FARAD"},"deer":{"s":"caution","w":"FARAD"},
     "pig":{"s":"caution","w":"FARAD"},"chicken":{"s":"caution","n":"Rarely indicated."},"duck":{"s":"caution"},"turkey":{"s":"caution"},"peafowl":{"s":"caution"}},
 owner="For mild hives or insect stings in dogs and cats. Check the box: ONLY diphenhydramine. Facial swelling with trouble breathing is an emergency, not a Benadryl case.",
 dvm="Sedation common; anticholinergic effects. Not a substitute for epinephrine in anaphylaxis.",rf="Swelling of face/throat, difficulty breathing, collapse, pale gums.")

add(n="Famotidine",a=["Pepcid AC"],tier=1,cls="H2 receptor antagonist",rx="otc",
 ind=["vomiting","gastric ulcer","reflux","nausea","stress gastritis"],ev="B",evn="Weaker acid suppression than omeprazole; tachyphylaxis with continuous use in dogs.",
 sp={"dog":{"s":"ok","d":"0.5-1 mg/kg PO q12-24h","n":""},"cat":{"s":"ok","d":"0.5-1 mg/kg PO q12-24h","n":"Rapid IV can cause hemolysis — PO only at home."},"rabbit":{"s":"caution","d":"0.5 mg/kg PO","n":""},
     "horse":{"s":"caution","d":"Omeprazole preferred for EGUS","n":"Poor oral bioavailability."},"cattle":{"s":"caution","w":"FARAD"},"sheep":{"s":"caution","w":"FARAD"},"goat":{"s":"caution","w":"FARAD"},"deer":{"s":"caution","w":"FARAD"},"pig":{"s":"caution","w":"FARAD"},
     "chicken":{"s":"caution"},"duck":{"s":"caution"},"turkey":{"s":"caution"},"peafowl":{"s":"caution"}},
 owner="Reasonable for a dog or cat with one-off nausea. Not a fix for repeated vomiting — that needs a diagnosis.",dvm="Limited efficacy for ulcer healing vs PPIs.",rf="Vomiting >24 h, blood in vomit, black stool, abdominal pain, lethargy.")

add(n="Hydrogen peroxide 3% (emesis induction)",a=["H2O2"],tier=1,cls="Emetic",rx="otc",
 ind=["induce vomiting","toxin ingestion","chocolate","grapes","medication ingestion"],ev="B",evn="Effective emetic in dogs but causes gastric erosion; apomorphine or ropinirole (Rx) preferred when available. Never in cats or non-vomiting species.",
 sp={"dog":{"s":"caution","d":"1-2 mL/kg PO, max 45 mL, once; repeat once only if no emesis in 15 min","n":"ONLY with veterinary/poison-control direction. Not if caustic, sharp, petroleum, already vomiting, or obtunded."},
     "cat":{"s":"no","n":"Contraindicated — hemorrhagic gastritis; ineffective."},"rabbit":{"s":"no","n":"Cannot vomit."},"horse":{"s":"no","n":"Cannot vomit."},
     "cattle":{"s":"no","n":"Do not induce."},"sheep":{"s":"no"},"goat":{"s":"no"},"deer":{"s":"no"},"pig":{"s":"no","n":"Not recommended."},
     "chicken":{"s":"no","n":"Not applicable."},"duck":{"s":"no"},"turkey":{"s":"no"},"peafowl":{"s":"no"}},
 owner="Dogs only, and only if a vet or poison control tells you to. Never for cats, rabbits, horses, or livestock. Call ASPCA Poison Control 888-426-4435 first.",
 dvm="Gastric ulceration reported; ropinirole (Clevor) or apomorphine preferred in clinic.",rf="Any toxin ingestion — call before acting.")

add(n="Activated charcoal",a=["ToxiBan"],tier=1,cls="Adsorbent",rx="otc",
 ind=["toxin ingestion","chocolate","rodenticide","medication overdose"],ev="B",evn="Most useful within 1-2 h of ingestion; ineffective for alcohols, xylitol, heavy metals, ethylene glycol.",
 sp={"dog":{"s":"ok","d":"1-4 g/kg PO (with sorbitol first dose only)","n":"Aspiration risk if vomiting/obtunded."},"cat":{"s":"caution","d":"1-4 g/kg PO","n":"Difficult to administer."},"rabbit":{"s":"caution","d":"1 g/kg PO"},
     "horse":{"s":"ok","d":"1-3 g/kg via NG tube (vet)","n":""},"cattle":{"s":"ok","d":"1-3 g/kg PO","w":"0 d","n":"Ruminants: large volumes."},"sheep":{"s":"ok","w":"0 d"},"goat":{"s":"ok","w":"0 d"},"deer":{"s":"ok","w":"0 d"},"pig":{"s":"ok","w":"0 d"},
     "chicken":{"s":"caution","d":"Extra-label"},"duck":{"s":"caution"},"turkey":{"s":"caution"},"peafowl":{"s":"caution"}},
 owner="Binds many poisons in the gut if given early. Does not work for antifreeze, xylitol, or alcohol. Messy — call poison control before using.",
 dvm="Hypernatremia reported with repeated sorbitol doses.",rf="Any suspected poisoning.")

add(n="Aspirin",a=["acetylsalicylic acid"],tier=1,cls="Non-selective NSAID / COX inhibitor",rx="otc",
 ind=["pain","fever","arthritis","antiplatelet"],ev="C",evn="Historic use; high GI ulceration rate in dogs; poor bioavailability in horses. Rx NSAIDs are safer and more effective.",
 sp={"dog":{"s":"caution","d":"10 mg/kg PO q12h with food (short-term only)","n":"Vomiting, GI bleeding common. Never with other NSAIDs or steroids. Do NOT give before surgery."},
     "cat":{"s":"no","d":"(Vet only: 10 mg/kg q48-72h)","n":"Slow clearance; owner dosing not recommended."},"rabbit":{"s":"caution","d":"Vet only"},
     "horse":{"s":"caution","d":"10-20 mg/kg PO q12-24h","n":"Poor absorption; phenylbutazone/flunixin far superior."},
     "cattle":{"s":"caution","d":"100 mg/kg PO q12h (extra-label)","w":"FARAD: meat 1 d, milk 24 h","n":"Extra-label; no approved aspirin in food animals."},
     "sheep":{"s":"caution","w":"FARAD"},"goat":{"s":"caution","w":"FARAD"},"deer":{"s":"caution","w":"FARAD"},"pig":{"s":"caution","w":"FARAD"},
     "chicken":{"s":"caution","d":"Extra-label","w":"Undefined"},"duck":{"s":"caution"},"turkey":{"s":"caution"},"peafowl":{"s":"caution"}},
 owner="Not recommended. Dogs get stomach bleeding; cats can be poisoned. Ibuprofen, naproxen, and acetaminophen are worse — never give them. Ask for a prescription NSAID instead.",
 dvm="Washout ≥7 d before switching to another NSAID. Irreversible platelet inhibition.",rf="Black or bloody stool, vomiting, lethargy after any pain medication.")

add(n="Ibuprofen / naproxen / acetaminophen (DO NOT USE)",a=["Advil","Aleve","Tylenol"],tier=1,cls="Human OTC analgesics",rx="otc",
 ind=["pain","fever","toxicity","poisoning"],ev="X",evn="Leading cause of NSAID poisoning in dogs; acetaminophen is fatal to cats at one tablet.",
 sp={"dog":{"s":"no","n":"Ibuprofen/naproxen: GI ulcers, kidney failure at low doses. Acetaminophen: liver damage."},
     "cat":{"s":"no","n":"Acetaminophen: methemoglobinemia, death from a single 325 mg tablet. NSAIDs: renal failure."},
     "rabbit":{"s":"no"},"horse":{"s":"no","n":"Not indicated; use approved equine NSAIDs."},"cattle":{"s":"no","w":"No withdrawal data"},"sheep":{"s":"no"},"goat":{"s":"no"},"deer":{"s":"no"},"pig":{"s":"no"},
     "chicken":{"s":"no"},"duck":{"s":"no"},"turkey":{"s":"no"},"peafowl":{"s":"no"}},
 owner="Never give human pain relievers to any animal. One Tylenol can kill a cat; one Advil can put a small dog in kidney failure.",
 dvm="Acetaminophen in cats: N-acetylcysteine 140 mg/kg then 70 mg/kg q6h x7; methylene blue caution. NSAID overdose: decontaminate, GI protectants, IV fluids 48-72 h.",
 rf="Brown gums, facial swelling, dark urine, vomiting after exposure.")

# ───────── v0.2 BATCH 1 · RUMINANT / SWINE OTC (labels verified on DailyMed 2026-09-20) ─────────
_NA_C={k:{"s":"no","n":"Not used in this species."} for k in ["cat","rabbit"]}
_NA_B={k:{"s":"no","n":"Not indicated.","w":"n/a"} for k in ["chicken","duck","turkey","peafowl"]}

add(n="Albendazole",a=["Valbazen"],tier=1,cls="Benzimidazole anthelmintic (broad spectrum incl. liver fluke)",rx="otc",
 ind=["deworming","liver fluke","Fasciola","tapeworm","stomach worm","lungworm","Ostertagia inhibited larvae"],ev="A",
 evn="Valbazen label (NADA 110-048): cattle, sheep, goats — liver flukes, tapeworms, stomach worms including inhibited Ostertagia L4, intestinal worms, lungworms. Teratogenic: not in early pregnancy.",
 sp={"dog":{"s":"caution","d":"Extra-label; bone marrow toxicity reported with prolonged courses","n":"Fenbendazole preferred."},
     "horse":{"s":"caution","d":"Extra-label","n":"Fenbendazole/oxibendazole preferred."},
     "cattle":{"s":"ok","d":"10 mg/kg PO once (4.54 mg/lb; 4 mL/100 lb of 113.6 mg/mL)","w":"Meat 27 d; do not use in female dairy cattle of breeding age (no milk withdrawal established)","n":"Do not give in first 45 d of pregnancy or for 45 d after bull removal (label)."},
     "sheep":{"s":"ok","d":"7.5 mg/kg PO once (3.4 mg/lb; 0.75 mL/25 lb)","w":"Meat 7 d; not for lactating ewes","n":"Do not give in first 30 d of pregnancy or 30 d after ram removal (label). Resistance common — FECRT."},
     "goat":{"s":"ok","d":"Label table: 1 mL (113.6 mg) per 25 lb ≈ 10 mg/kg PO once","w":"Meat 7 d; do not use in lactating does","n":"Same 30-d pregnancy restriction as sheep. Goat dose line on label to be confirmed by reviewer (table vs. rate statement)."},
     "deer":{"s":"caution","d":"Extra-label","w":"FARAD","n":"Farmed deer are food animals; same teratogenicity caution."},
     "pig":{"s":"caution","d":"Extra-label; fenbendazole labeled instead","w":"FARAD"}} | _NA_C | _NA_B,
 owner="Feed-store dewormer for cattle, sheep and goats that also kills liver flukes and tapeworms. Never give to a cow in the first 6 weeks of pregnancy or a ewe/doe in the first month — it causes birth defects. Milk from treated goats and dairy cows cannot be used.",
 dvm="Only OTC flukicide labeled for ruminants. Inhibited Ostertagia activity at 10 mg/kg. Teratogenic window per label; record breeding dates before dosing. Extra-label in goats above label dose needs FARAD. Combine with a different class (levamisole or moxidectin) only as part of a resistance-managed program with FECRT.",
 reg="NADA 110-048. OTC. Not affected by GFI #263 (not an antimicrobial).",rf="Bottle jaw, pale gums, or sudden weakness in a treated flock — anaemia from Haemonchus is not fixed by a dewormer alone.")

add(n="Levamisole",a=["Prohibit","LevaMed","Levasole"],tier=1,cls="Imidazothiazole anthelmintic",rx="otc",
 ind=["deworming","Haemonchus","stomach worm","lungworm","benzimidazole resistance"],ev="A",
 evn="Prohibit soluble drench (ANADA 200-225): cattle and sheep — stomach, intestinal and lungworms. Label volume tables correspond to about 8 mg/kg. Narrow safety margin; cholinergic toxicosis with overdose.",
 sp={"dog":{"s":"no","n":"Not used; toxic margin narrow."},
     "horse":{"s":"no","n":"Not used."},
     "cattle":{"s":"ok","d":"≈8 mg/kg PO once (label: 52 g packet in 1 qt water; 1/2 fl oz per 200 lb)","w":"Meat 48 h; do not give to dairy animals of breeding age","n":"Muzzle foam expected and transient. Do not overdose — weigh, do not estimate."},
     "sheep":{"s":"ok","d":"≈8 mg/kg PO once (label: 52 g packet in 1 gal water; 1/2 fl oz per 50 lb)","w":"Meat 72 h; not for dairy sheep of breeding age","n":"Useful against benzimidazole-resistant Haemonchus; resistance to levamisole also documented."},
     "goat":{"s":"caution","d":"Extra-label; goats need a higher mg/kg than sheep but have the narrowest margin — use a published goat chart (ACSRPC) and weigh each animal","w":"FARAD","n":"Toxicosis (salivation, tremor, ataxia, death) reported at modest overdoses."},
     "deer":{"s":"caution","d":"Extra-label","w":"FARAD"},
     "pig":{"s":"caution","d":"Extra-label (older swine labels existed)","w":"FARAD"}} | _NA_C | _NA_B,
 owner="Drench for cattle and sheep that works on worms resistant to the white (benzimidazole) dewormers. Mix exactly as the packet says and dose by actual weight — too much causes drooling, trembling and can kill. Goats need a vet's dose.",
 dvm="Nicotinic agonist: overdose signs are cholinergic (salivation, tremor, hyperaesthesia, collapse); atropine is not an antidote for the nicotinic component — supportive care. No activity against tapeworms or flukes. Short meat withdrawal makes it useful pre-sale. Rotate by class, not by brand.",
 reg="ANADA 200-225 (Prohibit). OTC.",rf="Drooling, trembling, staggering or collapse within hours of drenching — levamisole toxicosis, emergency.")

add(n="Morantel tartrate",a=["Rumatel","Positive Pellet"],tier=1,cls="Tetrahydropyrimidine anthelmintic (feed)",rx="otc",
 ind=["deworming","Haemonchus","goat dewormer","dairy goat","stomach worm"],ev="A",
 evn="Rumatel 88 (NADA 092-444): cattle and goats — adult gastrointestinal nematodes including Haemonchus, Ostertagia/Teladorsagia, Trichostrongylus. No milk discard in dairy cattle or goats.",
 sp={"dog":{"s":"no","n":"Not used."},"horse":{"s":"no","n":"Pyrantel used instead."},
     "cattle":{"s":"ok","d":"0.44 g morantel tartrate per 100 lb (≈9.7 mg/kg) once, top-dressed or mixed in feed","w":"Meat 14 d; milk 0 d","n":"Adult worms only — no larvicidal or fluke activity."},
     "sheep":{"s":"caution","d":"Extra-label (no US sheep label)","w":"FARAD"},
     "goat":{"s":"ok","d":"0.44 g per 100 lb (≈9.7 mg/kg) once in feed","w":"Meat 30 d; milk 0 d","n":"One of two dewormers with a US goat label; the only one with zero milk withdrawal."},
     "deer":{"s":"caution","d":"Extra-label","w":"FARAD"},
     "pig":{"s":"no","n":"Pyrantel labeled for swine instead."}} | _NA_C | _NA_B,
 owner="Feed dewormer approved for goats and cattle with no milk withdrawal — the usual choice for milking goats. Only works on adult worms and every animal must eat its full dose.",
 dvm="Same class as pyrantel; cross-resistance expected. Efficacy depends on intake — individual top-dress in goats. No activity against Moniezia, flukes or larvae. FECRT 10-14 d post-treatment.",
 reg="NADA 092-444. OTC Type A medicated article.",rf="")

add(n="Moxidectin",a=["Cydectin","ProHeart (Rx)","Quest"],tier=1,cls="Macrocyclic lactone (milbemycin)",rx="otc",
 ind=["deworming","Haemonchus","ivermectin resistance","lice","mites","grubs","dairy cattle dewormer"],ev="A",
 evn="Cydectin cattle pour-on (NADA 141-099) 0.5 mg/kg, zero meat and milk withdrawal; cattle injectable (NADA 141-220) 0.2 mg/kg SC, meat 21 d, not for dairy ≥20 mo; sheep oral drench (NADA 141-247) 0.2 mg/kg, meat 7 d. Often retains activity where ivermectin has failed, but resistance is emerging.",
 sp={"dog":{"s":"caution","d":"Rx heartworm products only (ProHeart 6/12 injectable, oral combinations)","n":"MDR1 breeds: livestock-strength moxidectin has killed dogs. Never dose from Cydectin."},
     "cat":{"s":"caution","d":"Rx topical combinations only","n":"Not from livestock products."},
     "horse":{"s":"ok","d":"0.4 mg/kg PO gel (Quest label)","n":"Foals <6 mo: narrow margin — use label age limits. Effective against encysted cyathostomins."},
     "cattle":{"s":"ok","d":"Pour-on 0.5 mg/kg (1 mL/10 kg); injectable 0.2 mg/kg SC","w":"Pour-on: meat 0 d, milk 0 d; injectable: meat 21 d, not for female dairy ≥20 mo; not for veal calves","n":"Pour-on is the only endectocide with zero milk withdrawal in lactating dairy cows. Keep out of waterways — toxic to aquatic life."},
     "sheep":{"s":"ok","d":"0.2 mg/kg PO drench (1 mL/11 lb)","w":"Meat 7 d; not for dairy sheep","n":"Oral only — do not inject the drench. Monitor with FECRT; resistance documented."},
     "goat":{"s":"caution","d":"Extra-label; goats clear macrocyclic lactones faster — published goat charts use a higher mg/kg than the sheep label","w":"FARAD","n":"Sheep drench used orally; pour-on formulations are not reliable orally or topically in goats."},
     "deer":{"s":"caution","d":"Extra-label","w":"FARAD"},
     "pig":{"s":"caution","d":"Extra-label (ivermectin labeled instead)","w":"FARAD"}} | {k:{"s":"no","n":"Not used.","w":"n/a"} for k in ["chicken","duck","turkey","peafowl"]} | {"rabbit":{"s":"caution","n":"Extra-label; ivermectin more commonly used."}},
 owner="Cydectin pour-on is the dewormer dairy farms use because milk needs no withholding. Sheep drench is oral only. Never put livestock moxidectin on a dog — it can be fatal in collie-type breeds.",
 dvm="Longer persistence than ivermectin; side-resistance within macrocyclic lactones is partial, so moxidectin may still work where ivermectin fails, but selection pressure is high — use in a refugia-based program, not as routine. Goats: extra-label, oral drench route; pour-on in goats is unreliable. Environmental: dung-fauna and aquatic toxicity.",
 reg="NADA 141-099 (pour-on), 141-220 (injectable), 141-247 (sheep drench). OTC. Companion-animal products are Rx.",rf="Ataxia, blindness, tremors after exposure (especially dogs) — macrocyclic lactone toxicosis, emergency.")

add(n="Decoquinate",a=["Deccox","Deccox-M"],tier=1,cls="Quinolone coccidiostat (feed)",rx="otc",
 ind=["coccidiosis prevention","calves","lambs","kids","broilers","Eimeria","weaning"],ev="A",
 evn="Deccox (NADA 039-417): ruminating and non-ruminating calves including veal, cattle, young sheep, young goats, broiler chickens — prevention of coccidiosis at 0.5 mg/kg/day for at least 28 days; zero withdrawal.",
 sp={"dog":{"s":"caution","d":"Extra-label; some use for Neospora/Hepatozoon","n":"Off-label."},"cat":{"s":"caution","n":"Off-label."},"rabbit":{"s":"caution","d":"Extra-label","n":"Some use for hepatic coccidiosis."},
     "horse":{"s":"no","n":"Not used."},
     "cattle":{"s":"ok","d":"0.5 mg/kg/day in feed (22.7 mg/100 lb) for ≥28 d during exposure","w":"0 d; do not feed to cows producing milk for human consumption","n":"Prevention only — does not treat clinical coccidiosis (use amprolium or sulfas)."},
     "sheep":{"s":"ok","d":"0.5 mg/kg/day in feed for ≥28 d (young sheep)","w":"0 d; not for lactating ewes producing milk for humans"},
     "goat":{"s":"ok","d":"0.5 mg/kg/day in feed for ≥28 d (young goats)","w":"0 d; not for lactating does producing milk for humans","n":"Labeled for goats — start before the risk period (weaning, transport)."},
     "deer":{"s":"caution","d":"Extra-label","w":"FARAD"},
     "pig":{"s":"no","n":"Not labeled."},
     "chicken":{"s":"ok","d":"Per label in broiler feed (Deccox-M)","w":"0 d; do not feed to laying hens producing eggs for humans","n":"Broilers only."},
     "duck":{"s":"caution","d":"Extra-label","w":"Undefined; FARAD"},"turkey":{"s":"caution","d":"Extra-label","w":"Undefined; FARAD"},"peafowl":{"s":"caution","d":"Extra-label","w":"Undefined; FARAD"}},
 owner="A feed additive that prevents coccidiosis in calves, lambs, kids and meat chickens. It has to be eaten every day for at least 4 weeks and started before the stress period. It will not cure an animal that already has bloody scours — that needs treatment.",
 dvm="Static, not cidal: prevents oocyst output when fed continuously through the exposure window (28 d minimum). Not a treatment. Combine with hygiene and stocking-density control. Not an antimicrobial under GFI #263 — remains OTC.",
 reg="NADA 039-417 (Deccox). OTC Type A medicated article.",rf="Bloody or black diarrhoea, straining, dehydration in young stock despite preventive feed — treat, do not wait.")

# ───────── TIER 2 · Rx SMALL MOLECULE ─────────
add(n="Carprofen",a=["Rimadyl","Novox"],tier=2,cls="COX-2 preferential NSAID",rx="rx",
 ind=["osteoarthritis","pain","post-surgical","lameness"],ev="A",evn="Multiple RCTs in canine OA; label-approved dogs.",
 sp={"dog":{"s":"ok","d":"4.4 mg/kg PO q24h or 2.2 mg/kg q12h","n":"Baseline CBC/chem; recheck labs q3-6 mo on chronic therapy."},"cat":{"s":"caution","d":"Single 4 mg/kg SC (vet, perioperative only)","n":"Not for repeated dosing."},
     "rabbit":{"s":"caution","d":"2-4 mg/kg PO q24h (extra-label)"},"horse":{"s":"caution","d":"0.7 mg/kg IV/PO q24h (extra-label)"},"cattle":{"s":"caution","d":"1.4 mg/kg SC/IV once (extra-label; EU-approved)","w":"FARAD"},
     "sheep":{"s":"caution","w":"FARAD"},"goat":{"s":"caution","w":"FARAD"},"deer":{"s":"caution","w":"FARAD"},"pig":{"s":"caution","w":"FARAD"},"chicken":{"s":"caution","w":"Undefined"},"duck":{"s":"caution"},"turkey":{"s":"caution"},"peafowl":{"s":"caution"}},
 owner="The standard prescription arthritis drug for dogs. Requires bloodwork. Never combine with aspirin, other NSAIDs, or steroids.",dvm="Idiosyncratic hepatotoxicity (Labradors overrepresented historically). Washout ≥5-7 d when switching NSAIDs.",rf="Vomiting, diarrhea, black stool, yellow gums, reduced appetite on therapy — stop and call.")

add(n="Meloxicam",a=["Metacam","Loxicom"],tier=2,cls="COX-2 preferential NSAID",rx="rx",
 ind=["osteoarthritis","pain","post-surgical","lameness"],ev="A",evn="Label-approved dogs (oral), cats (single injection US; chronic use approved elsewhere). Well studied in rabbits.",
 sp={"dog":{"s":"ok","d":"0.2 mg/kg PO day 1, then 0.1 mg/kg q24h","n":""},"cat":{"s":"caution","d":"US label: 0.3 mg/kg SC once. Extra-label chronic: 0.01-0.03 mg/kg PO q24h with renal monitoring","n":"FDA boxed warning: repeated use associated with acute renal failure/death in cats."},
     "rabbit":{"s":"ok","d":"0.3-1 mg/kg PO q24h","n":"Extra-label; well tolerated, higher doses needed."},"horse":{"s":"caution","d":"0.6 mg/kg PO q24h (extra-label; EU-approved)"},
     "cattle":{"s":"caution","d":"0.5 mg/kg SC/PO once (extra-label; approved Canada/EU)","w":"FARAD (commonly cited: meat 21 d, milk 4-5 d — confirm with FARAD)","n":"Used for calf disbudding/castration analgesia."},
     "sheep":{"s":"caution","d":"1 mg/kg PO (extra-label)","w":"FARAD"},"goat":{"s":"caution","d":"0.5-1 mg/kg PO","w":"FARAD"},"deer":{"s":"caution","w":"FARAD"},"pig":{"s":"caution","d":"0.4 mg/kg IM (extra-label; EU-approved)","w":"FARAD"},
     "chicken":{"s":"caution","d":"1-2 mg/kg PO q12-24h (extra-label)","w":"Undefined","n":"Common in backyard flocks; no egg withdrawal data."},"duck":{"s":"caution","w":"Undefined"},"turkey":{"s":"caution","w":"Undefined"},"peafowl":{"s":"caution","w":"Undefined"}},
 owner="Prescription NSAID. In cats, repeated dosing can cause kidney failure — follow your vet's plan exactly.",dvm="Oral suspension is easy to overdose in small patients — dose by syringe volume, verify concentration (0.5 vs 1.5 mg/mL).",rf="Vomiting, anorexia, black stool, reduced urination.")

add(n="Grapiprant",a=["Galliprant"],tier=2,cls="EP4 prostaglandin receptor antagonist (piprant)",rx="rx",
 ind=["osteoarthritis","pain","lameness"],ev="A",evn="RCT-supported for canine OA; non-COX mechanism spares GI/renal prostaglandins.",
 sp={"dog":{"s":"ok","d":"2 mg/kg PO q24h","n":"≥9 mo, ≥3.6 kg."},"cat":{"s":"caution","d":"Extra-label; limited PK data"},"rabbit":{"s":"caution"},"horse":{"s":"caution","d":"Investigational; PK studies only"},"cattle":{"s":"caution","w":"FARAD"},"sheep":{"s":"caution"},"goat":{"s":"caution"},"deer":{"s":"caution"},"pig":{"s":"caution"},"chicken":{"s":"caution"},"duck":{"s":"caution"},"turkey":{"s":"caution"},"peafowl":{"s":"caution"}},
 owner="Prescription arthritis drug for dogs designed to be gentler on the stomach and kidneys than classic NSAIDs.",dvm="Not for acute surgical pain (weaker than COX inhibitors). Still avoid with other NSAIDs/steroids.",rf="Vomiting or diarrhea persisting >48 h.")

add(n="Phenylbutazone",a=["Bute"],tier=2,cls="Non-selective NSAID",rx="rx",
 ind=["lameness","laminitis","arthritis","musculoskeletal pain","colic"],ev="A",evn="Equine standard; label-approved horses and dogs. PROHIBITED in dairy cattle ≥20 mo; not for any food animal.",
 sp={"horse":{"s":"ok","d":"2.2-4.4 mg/kg PO/IV q12-24h; taper to lowest effective","n":"Right dorsal colitis, gastric ulcers, renal papillary necrosis. Never IM/perivascular. FEI/USEF controlled medication."},
     "dog":{"s":"caution","d":"Approved but rarely used (10-22 mg/kg PO q8-12h)","n":"Bone marrow toxicity; safer NSAIDs exist."},"cat":{"s":"no"},"rabbit":{"s":"no"},
     "cattle":{"s":"no","n":"PROHIBITED in female dairy cattle ≥20 months (21 CFR 530.41). Strongly discouraged in all food animals."},"sheep":{"s":"no","n":"Not for food animals."},"goat":{"s":"no"},"deer":{"s":"no"},"pig":{"s":"no"},
     "chicken":{"s":"no"},"duck":{"s":"no"},"turkey":{"s":"no"},"peafowl":{"s":"no"}},
 owner="The horse pain reliever. Prescription only. Never share with dogs, cats, or livestock.",dvm="Combine with omeprazole for chronic use. Do not stack with flunixin (no added analgesia, additive toxicity).",rf="Diarrhea, depression, reduced water intake, oral ulcers in a horse on bute.")

add(n="Flunixin meglumine",a=["Banamine"],tier=2,cls="Non-selective NSAID",rx="rx",
 ind=["colic","endotoxemia","pain","fever","pinkeye","mastitis"],ev="A",evn="Label-approved horses, cattle (IV only), swine.",
 sp={"horse":{"s":"ok","d":"1.1 mg/kg IV/PO q12-24h (colic: 0.25 mg/kg q8h for endotoxemia)","n":"IM injection → clostridial myositis risk; give IV or PO."},
     "cattle":{"s":"ok","d":"1.1-2.2 mg/kg IV q24h (IV ONLY per label); transdermal pour-on approved","w":"IV: meat 4 d, milk 36 h. IM use is extra-label with prolonged residues — avoid.","n":"IM administration in cattle causes violative residues and injection-site lesions."},
     "pig":{"s":"ok","d":"2.2 mg/kg IM once","w":"Meat 12 d","n":"Approved."},"sheep":{"s":"caution","d":"1.1-2.2 mg/kg IV (extra-label)","w":"FARAD"},"goat":{"s":"caution","d":"1.1-2.2 mg/kg IV","w":"FARAD"},"deer":{"s":"caution","w":"FARAD"},
     "dog":{"s":"caution","d":"Extra-label; short-term only","n":"GI toxicity; safer alternatives."},"cat":{"s":"no"},"rabbit":{"s":"caution"},
     "chicken":{"s":"caution","w":"Undefined"},"duck":{"s":"caution"},"turkey":{"s":"caution"},"peafowl":{"s":"caution"}},
 owner="Horse colic and fever drug, prescription only. Can mask colic that needs surgery — call your vet before and after giving it.",dvm="Masks colic progression; reassess at 2 h. Cattle: IV only; extra-label IM requires extended withdrawal.",rf="Colic pain returning within 4-6 h of a dose — likely surgical.")

add(n="Gabapentin",a=["Neurontin"],tier=2,cls="Gabapentinoid",rx="rx",
 ind=["chronic pain","neuropathic pain","osteoarthritis","anxiety","seizures adjunct","pre-visit sedation"],ev="B",evn="Adjunct analgesic; RCT support for feline OA and pre-visit stress. Weak standalone analgesic in dogs.",
 sp={"dog":{"s":"ok","d":"10-20 mg/kg PO q8-12h","n":"Human oral solution often contains xylitol — check."},"cat":{"s":"ok","d":"5-10 mg/kg PO q8-12h; 50-100 mg/cat 2-3 h pre-visit","n":"Reduce in CKD."},"rabbit":{"s":"caution","d":"3-5 mg/kg PO q8-12h"},
     "horse":{"s":"caution","d":"5-20 mg/kg PO q8-12h (laminitis adjunct)","n":"Poor oral bioavailability."},"cattle":{"s":"caution","w":"FARAD"},"sheep":{"s":"caution","w":"FARAD"},"goat":{"s":"caution","w":"FARAD"},"deer":{"s":"caution","w":"FARAD"},"pig":{"s":"caution","w":"FARAD"},
     "chicken":{"s":"caution","d":"Extra-label","w":"Undefined"},"duck":{"s":"caution"},"turkey":{"s":"caution"},"peafowl":{"s":"caution"}},
 owner="Prescription add-on for chronic pain and for calming cats before vet visits. Sedation and wobbliness are the common side effects.",dvm="Taper rather than stop abruptly on chronic use. Schedule V in some states.",rf="Profound sedation or ataxia — dose reduction needed.")

add(n="Amoxicillin / amoxicillin-clavulanate",a=["Clavamox","Amoxi-Tabs"],tier=2,cls="Aminopenicillin ± β-lactamase inhibitor",rx="rx",
 ind=["skin infection","wound infection","urinary tract infection","abscess","bite wound","respiratory infection"],ev="A",evn="Label-approved dogs, cats. Since 2023 (GFI #263) all medically important antimicrobials are prescription-only in all species.",
 sp={"dog":{"s":"ok","d":"Amox 10-20 mg/kg PO q8-12h; Clavamox 12.5-25 mg/kg PO q12h","n":""},"cat":{"s":"ok","d":"Clavamox 62.5 mg/cat PO q12h","n":""},
     "rabbit":{"s":"no","n":"Oral penicillins cause fatal dysbiosis/enterotoxemia in rabbits. Also avoid in guinea pigs, hamsters."},
     "horse":{"s":"caution","d":"Oral amoxicillin poor bioavailability; not recommended","n":"Colitis risk with oral β-lactams."},
     "cattle":{"s":"caution","d":"Amoxicillin trihydrate inj 6.6-11 mg/kg IM q24h (approved)","w":"Meat 25 d (inj label); milk 96 h","n":"Rx (post-GFI #263)."},"sheep":{"s":"caution","w":"FARAD"},"goat":{"s":"caution","w":"FARAD"},"deer":{"s":"caution","w":"FARAD"},"pig":{"s":"caution","w":"FARAD"},
     "chicken":{"s":"caution","d":"Extra-label; Rx only","w":"FARAD","n":"Egg withdrawal required."},"duck":{"s":"caution","w":"FARAD"},"turkey":{"s":"caution","w":"FARAD"},"peafowl":{"s":"caution","w":"FARAD"}},
 owner="Prescription only — feed-store antibiotics ended in 2023. Never give penicillins to rabbits.",dvm="Culture where possible; ISCAID guidelines for UTI/pyoderma durations.",rf="Fever with lethargy, spreading redness, pus, or a wound that smells.")

add(n="Enrofloxacin",a=["Baytril"],tier=2,cls="Fluoroquinolone",rx="rx",
 ind=["urinary tract infection","skin infection","respiratory infection","Pseudomonas","otitis"],ev="A",evn="Label-approved dogs, cats, cattle, swine. Extra-label use PROHIBITED in poultry and all food animals (21 CFR 530.41).",
 sp={"dog":{"s":"ok","d":"5-20 mg/kg PO q24h","n":"Cartilage damage in growing dogs (avoid <12-18 mo large breeds)."},"cat":{"s":"caution","d":"5 mg/kg PO q24h MAX","n":">5 mg/kg → acute retinal degeneration/blindness."},
     "rabbit":{"s":"ok","d":"5-20 mg/kg PO q12-24h","n":"Safe for rabbit GI flora."},"horse":{"s":"caution","d":"5-7.5 mg/kg PO q24h (extra-label)","n":"Cartilage risk in foals."},
     "cattle":{"s":"caution","d":"Per label (BRD) ONLY","w":"Meat 28 d; not in dairy ≥20 mo, not calves for veal","n":"Extra-label use in food animals is federally prohibited — label indication only."},
     "sheep":{"s":"no","n":"Prohibited extra-label."},"goat":{"s":"no","n":"Prohibited extra-label."},"deer":{"s":"no","n":"Prohibited."},"pig":{"s":"caution","d":"Per label only","w":"Per label"},
     "chicken":{"s":"no","n":"PROHIBITED — fluoroquinolones banned in poultry (FDA 2005)."},"duck":{"s":"no","n":"Prohibited."},"turkey":{"s":"no","n":"Prohibited."},"peafowl":{"s":"no","n":"Prohibited."}},
 owner="Prescription antibiotic. Illegal to use in chickens or other poultry in the US.",dvm="Reserve as second-line per antimicrobial stewardship. Cats: never exceed 5 mg/kg.",rf="Sudden blindness in a cat on enrofloxacin.")

add(n="Metronidazole",a=["Flagyl"],tier=2,cls="Nitroimidazole",rx="rx",
 ind=["Giardia","diarrhea","anaerobic infection","Clostridium"],ev="B",evn="PROHIBITED in all food animals (21 CFR 530.41). Companion animal use common; neurotoxicity at high dose.",
 sp={"dog":{"s":"ok","d":"10-15 mg/kg PO q12h (Giardia 25 mg/kg q12h x5-7 d)","n":"Vestibular signs >60 mg/kg/d."},"cat":{"s":"ok","d":"10-15 mg/kg PO q12h","n":"Bitter; use compounded caps."},"rabbit":{"s":"ok","d":"20 mg/kg PO q12h"},
     "horse":{"s":"ok","d":"15-25 mg/kg PO q6-8h","n":"Anorexia common."},
     "cattle":{"s":"no","n":"FEDERALLY PROHIBITED in food animals."},"sheep":{"s":"no","n":"Prohibited."},"goat":{"s":"no","n":"Prohibited."},"deer":{"s":"no","n":"Prohibited."},"pig":{"s":"no","n":"Prohibited."},
     "chicken":{"s":"no","n":"PROHIBITED — nitroimidazoles banned in food animals."},"duck":{"s":"no"},"turkey":{"s":"no"},"peafowl":{"s":"no"}},
 owner="Common prescription for Giardia and diarrhea in dogs and cats. Illegal in any food animal — including backyard chickens.",dvm="Fenbendazole is a legal alternative for Giardia in food species.",rf="Head tilt, nystagmus, stumbling on metronidazole — stop immediately.")

add(n="Omeprazole",a=["GastroGard","UlcerGard (OTC equine)","Prilosec"],tier=2,cls="Proton pump inhibitor",rx="rx",
 ind=["gastric ulcer","EGUS","reflux","NSAID gastroprotection"],ev="A",evn="RCTs in equine squamous gastric disease; label-approved horses (UlcerGard is OTC for prevention). Dogs/cats extra-label but well supported.",
 sp={"horse":{"s":"ok","d":"Treatment 4 mg/kg PO q24h x28 d; prevention 1 mg/kg (UlcerGard, OTC)","n":"Glandular disease responds less; add sucralfate/misoprostol."},
     "dog":{"s":"ok","d":"0.7-1 mg/kg PO q12-24h","n":"Human OTC capsules acceptable with vet guidance."},"cat":{"s":"ok","d":"0.7-1 mg/kg PO q12-24h"},"rabbit":{"s":"caution"},
     "cattle":{"s":"caution","d":"Extra-label; poor efficacy in ruminants","w":"FARAD"},"sheep":{"s":"caution","w":"FARAD"},"goat":{"s":"caution","w":"FARAD"},"deer":{"s":"caution","w":"FARAD"},"pig":{"s":"caution","w":"FARAD"},
     "chicken":{"s":"caution"},"duck":{"s":"caution"},"turkey":{"s":"caution"},"peafowl":{"s":"caution"}},
 owner="For horses, UlcerGard (the prevention dose) is sold over the counter; the treatment dose is prescription. For dogs and cats, ask before using human Prilosec.",dvm="Buffered/enteric formulations required for horses; compounded pastes unreliable.",rf="Horse: grinding teeth, girthiness, poor appetite, recurrent mild colic.")

# ───────── TIER 3 · PEPTIDE / BIOLOGIC ─────────
add(n="Bedinvetmab",a=["Librela"],tier=3,sub="3A",cls="Canine anti-NGF monoclonal antibody",rx="rx",
 ind=["osteoarthritis","chronic pain","lameness","senior dog"],ev="A",evn="FDA-approved 2023 (dogs). Two RCTs vs placebo; ~1 in 2 dogs improve at day 28. Post-marketing: rare neurologic/ataxia and polyarthritis reports under FDA review.",
 sp={"dog":{"s":"ok","d":"0.5-1 mg/kg SC q28d (weight-band vials)","n":"Not <12 mo, not breeding/pregnant. Avoid combining with NSAIDs long-term only for cost reasons — no pharmacologic conflict."},
     "cat":{"s":"no","n":"Use frunevetmab (Solensia)."},"rabbit":{"s":"no"},"horse":{"s":"no","n":"Not species-appropriate (immunogenic)."},"cattle":{"s":"no"},"sheep":{"s":"no"},"goat":{"s":"no"},"deer":{"s":"no"},"pig":{"s":"no"},"chicken":{"s":"no"},"duck":{"s":"no"},"turkey":{"s":"no"},"peafowl":{"s":"no"}},
 owner="A monthly injection for dog arthritis that blocks the pain signal (NGF) rather than inflammation. No liver/kidney bloodwork burden like NSAIDs. Prescription; given at the clinic.",
 dvm="Species-specific mAb — no cross-species use. Monitor for ataxia/neurologic signs; report adverse events to Zoetis/FDA.",comp="Not applicable (companion).",
 rf="New weakness, stumbling, or inability to rise after injection.")

add(n="Frunevetmab",a=["Solensia"],tier=3,sub="3A",cls="Feline anti-NGF monoclonal antibody",rx="rx",
 ind=["osteoarthritis","chronic pain","senior cat","degenerative joint disease"],ev="A",evn="FDA-approved 2022 (cats). RCT: owner-assessed improvement at day 28 and 56.",
 sp={"cat":{"s":"ok","d":"1-2.8 mg/kg SC q28d (7 mg/mL, 1 vial ≥2.5 kg; 2 vials >7 kg)","n":"Skin reactions/pruritus reported; not <12 mo."},
     "dog":{"s":"no","n":"Use bedinvetmab."},"rabbit":{"s":"no"},"horse":{"s":"no"},"cattle":{"s":"no"},"sheep":{"s":"no"},"goat":{"s":"no"},"deer":{"s":"no"},"pig":{"s":"no"},"chicken":{"s":"no"},"duck":{"s":"no"},"turkey":{"s":"no"},"peafowl":{"s":"no"}},
 owner="Monthly arthritis injection for cats — important because cats tolerate NSAIDs poorly. Look for: jumping again, grooming again, using the litter box normally.",dvm="Feline OA is underdiagnosed; screen cats >10 y with mobility questionnaires.",rf="Vomiting, facial swelling, or skin lesions after injection.")

add(n="Lokivetmab",a=["Cytopoint"],tier=3,sub="3A",cls="Canine anti-IL-31 monoclonal antibody",rx="rx",
 ind=["atopic dermatitis","itching","allergic skin disease","pruritus"],ev="A",evn="Conditionally licensed 2016, full approval; RCTs vs placebo and vs oclacitinib.",
 sp={"dog":{"s":"ok","d":"2 mg/kg SC q4-8 wk","n":"Safe with most comorbidities; no lab monitoring required."},"cat":{"s":"no","n":"Not effective — canine-specific."},
     "rabbit":{"s":"no"},"horse":{"s":"no"},"cattle":{"s":"no"},"sheep":{"s":"no"},"goat":{"s":"no"},"deer":{"s":"no"},"pig":{"s":"no"},"chicken":{"s":"no"},"duck":{"s":"no"},"turkey":{"s":"no"},"peafowl":{"s":"no"}},
 owner="Injection that stops the itch signal in allergic dogs for 4-8 weeks. Does not fix infections or fleas — those still need treating.",dvm="Onset within 24 h; does not treat secondary pyoderma/Malassezia.",rf="Itch not controlled within 3 days — reassess for infection or food allergy.")

add(n="Insulin (veterinary)",a=["Vetsulin","ProZinc","Lantus (glargine, extra-label)"],tier=3,sub="3A",cls="Peptide hormone",rx="rx",
 ind=["diabetes mellitus","hyperglycemia","ketoacidosis"],ev="A",evn="Approved dogs (Vetsulin) and cats (ProZinc, Bexacat SGLT2 alt). Glargine extra-label but standard in cats.",
 sp={"dog":{"s":"ok","d":"Vetsulin 0.5 U/kg SC q12h start; titrate by curves","n":"Feed before dosing; never dose a dog that will not eat without calling."},
     "cat":{"s":"ok","d":"ProZinc/glargine 1-2 U/cat SC q12h start","n":"Remission possible with low-carb diet + early tight control."},
     "rabbit":{"s":"caution","n":"Rare."},"horse":{"s":"caution","n":"Equine metabolic syndrome is insulin RESISTANCE — insulin is not the treatment."},
     "cattle":{"s":"caution","w":"FARAD"},"sheep":{"s":"caution","w":"FARAD"},"goat":{"s":"caution","w":"FARAD"},"deer":{"s":"caution"},"pig":{"s":"caution"},"chicken":{"s":"caution"},"duck":{"s":"caution"},"turkey":{"s":"caution"},"peafowl":{"s":"caution"}},
 owner="The original peptide drug. Prescription; requires home monitoring. Signs of low blood sugar (weakness, wobbling, seizures) — give honey or syrup on the gums and call.",
 dvm="U-40 vs U-100 syringe mismatch is the most common dosing error.",rf="Weakness, collapse, seizures (hypoglycemia); vomiting/ketone breath (DKA).")

add(n="Deslorelin",a=["SucroMate Equine","Suprelorin (ferret/dog implant)"],tier=3,sub="3A",cls="GnRH agonist peptide",rx="rx",
 ind=["ovulation induction","estrus control","adrenal disease ferret","chemical castration"],ev="A",evn="Approved: SucroMate (mares, ovulation induction); Suprelorin F (ferret adrenal disease). Dog implant approved in EU/Australia, not US.",
 sp={"horse":{"s":"ok","d":"1.8 mg IM once when follicle ≥30-35 mm","n":"Approved (mares)."},"dog":{"s":"caution","d":"4.7 mg/9.4 mg implant (not US-approved; import/compounding issues)","n":"Extra-label."},
     "cat":{"s":"caution","d":"Extra-label implant","n":"Induces initial flare."},"rabbit":{"s":"caution","d":"Extra-label; used for adrenal/reproductive tumors"},
     "cattle":{"s":"caution","w":"FARAD"},"sheep":{"s":"caution","w":"FARAD"},"goat":{"s":"caution","w":"FARAD"},"deer":{"s":"caution","w":"FARAD"},"pig":{"s":"caution","w":"FARAD"},"chicken":{"s":"caution","n":"Used extra-label for egg-laying suppression in pet hens/parrots.","w":"Undefined"},"duck":{"s":"caution"},"turkey":{"s":"caution"},"peafowl":{"s":"caution"}},
 owner="A reproductive-hormone peptide: used to time ovulation in mares and, off-label, to stop chronic egg-laying in pet hens. Prescription.",dvm="Initial stimulation phase 1-2 wk before suppression.",rf="")

add(n="Oxytocin",a=["Pitocin"],tier=3,sub="3A",cls="Nonapeptide hormone",rx="rx",
 ind=["dystocia","retained placenta","milk letdown","uterine involution","egg binding"],ev="A",evn="Approved cattle, horses, sheep, swine, dogs, cats. Only useful once the cervix is open and obstruction is ruled out.",
 sp={"dog":{"s":"ok","d":"0.5-2 IU/dog IM (low dose); repeat once","n":"Never with obstructive dystocia — uterine rupture."},"cat":{"s":"ok","d":"0.5-1 IU IM","n":""},"rabbit":{"s":"caution","d":"1-2 IU IM"},
     "horse":{"s":"ok","d":"10-20 IU IM/IV (retained placenta: 10-20 IU q1-2h or drip)","n":"High doses cause colic."},"cattle":{"s":"ok","d":"20-40 IU IM","w":"0 d","n":"Approved."},"sheep":{"s":"ok","d":"5-10 IU IM","w":"0 d"},"goat":{"s":"ok","d":"5-10 IU IM","w":"0 d"},"deer":{"s":"caution","w":"FARAD"},"pig":{"s":"ok","d":"5-20 IU IM","w":"0 d","n":"Approved; overuse causes uterine spasm and stillbirths."},
     "chicken":{"s":"caution","d":"Extra-label; calcium first, then 0.5-1 IU/kg IM (vet)","n":"Egg binding — only if egg is in the shell gland and cloaca is not obstructed."},"duck":{"s":"caution"},"turkey":{"s":"caution"},"peafowl":{"s":"caution"}},
 owner="A labor hormone. Owners should not use it — given with a blocked birth canal it can rupture the uterus. Egg-bound hen: warm humid box, calcium, then vet.",
 dvm="Confirm cervical dilation and fetal position; two doses maximum before C-section decision.",rf="Straining >30 min without progress; >2 h between puppies/kittens; hen straining, tail-pumping, or off legs.")

add(n="rbST (recombinant bovine somatotropin)",a=["Posilac"],tier=3,sub="3A",cls="Recombinant protein hormone",rx="otc",
 ind=["milk production","dairy management"],ev="A",evn="FDA-approved 1993 (lactating dairy cows). Sold without prescription. Not for other species.",
 sp={"cattle":{"s":"ok","d":"500 mg SC q14d from ~57 d post-calving","w":"0 d milk/meat","n":"Approved; market acceptance varies (many processors rbST-free)."},
     "goat":{"s":"caution","d":"Extra-label","w":"FARAD"},"sheep":{"s":"caution","w":"FARAD"},"dog":{"s":"no"},"cat":{"s":"no"},"rabbit":{"s":"no"},"horse":{"s":"no"},"deer":{"s":"no"},"pig":{"s":"no"},"chicken":{"s":"no"},"duck":{"s":"no"},"turkey":{"s":"no"},"peafowl":{"s":"no"}},
 owner="A rare case: an approved protein hormone for dairy cows that does not need a prescription. Check your milk buyer's policy first.",dvm="Increases mastitis and lameness incidence modestly; management-dependent.",rf="")

add(n="Improvest (GnRF conjugate)",a=["Improvac"],tier=3,sub="3A",cls="Immunological castration (peptide-protein conjugate)",rx="rx",
 ind=["boar taint","castration alternative","swine"],ev="A",evn="Approved for male swine; two doses induce anti-GnRF antibodies.",
 sp={"pig":{"s":"ok","d":"2 mL SC x2, ≥4 wk apart; 2nd dose 3-10 wk pre-slaughter","w":"0 d","n":"Accidental human self-injection causes GnRF suppression — safety-needle device required."},
     "dog":{"s":"no"},"cat":{"s":"no"},"rabbit":{"s":"no"},"horse":{"s":"no"},"cattle":{"s":"caution","d":"Bopriva (not US)","w":"FARAD"},"sheep":{"s":"no"},"goat":{"s":"no"},"deer":{"s":"no"},"chicken":{"s":"no"},"duck":{"s":"no"},"turkey":{"s":"no"},"peafowl":{"s":"no"}},
 owner="A vaccine-like peptide that replaces surgical castration in market pigs. Prescription; handled by the vet.",dvm="Human self-injection = medical emergency (effects on fertility).",rf="")

add(n="Semaglutide / GLP-1 agonists",a=["Ozempic","Wegovy","exenatide (OKV-119 implant, investigational)"],tier=3,sub="3B",cls="GLP-1 receptor agonist peptide (human-approved)",rx="rx",
 ind=["feline diabetes","obesity","weight loss","diabetic remission"],ev="B",evn="Human-approved only. Feline pilot studies (exenatide, 2015-2023) show improved glycemic control and higher remission rates with insulin; a long-acting feline exenatide implant is in development. No approved veterinary product; no canine efficacy data.",
 sp={"cat":{"s":"caution","d":"Extra-label/investigational; exenatide ER 200 mcg/kg SC weekly reported in trials","n":"Extra-label under AMDUCA with VCPR. GI upset, hypoglycemia with insulin."},
     "dog":{"s":"caution","d":"No established dosing; case reports only","n":"Dogs are insulin-deficient (type 1-like) — GLP-1 agonists have limited rationale."},"rabbit":{"s":"no"},"horse":{"s":"caution","n":"Theoretical interest for EMS; no data."},
     "cattle":{"s":"no","w":"No withdrawal data — prohibited in practice"},"sheep":{"s":"no"},"goat":{"s":"no"},"deer":{"s":"no"},"pig":{"s":"no"},"chicken":{"s":"no"},"duck":{"s":"no"},"turkey":{"s":"no"},"peafowl":{"s":"no"}},
 owner="The human weight-loss peptides. In cats with diabetes, studies suggest they may help alongside insulin — but no approved pet product exists. Do not use human pens on pets without a vet.",
 dvm="Extra-label human drug use is permitted under AMDUCA in companion animals with VCPR. Compounded 'semaglutide' products for animals have quality concerns.",
 reg="Human-approved; no veterinary approval. Not for food animals.",rf="Anorexia >24 h, vomiting, weakness (hypoglycemia) in a cat on combined therapy.")

add(n="Desmopressin (DDAVP)",a=["Nocdurna"],tier=3,sub="3B",cls="Vasopressin analog peptide (human-approved)",rx="rx",
 ind=["diabetes insipidus","von Willebrand disease","polyuria polydipsia"],ev="A",evn="Standard extra-label therapy for canine central DI and pre-surgical vWD.",
 sp={"dog":{"s":"ok","d":"DI: 1-4 drops (0.1 mg/mL) conjunctival q12-24h or 0.1-0.2 mg PO q8-12h; vWD: 1 mcg/kg SC 30 min pre-op","n":"Water intoxication if free water unrestricted after dosing."},
     "cat":{"s":"ok","d":"1-2 drops conjunctival q12-24h (DI)"},"rabbit":{"s":"caution"},"horse":{"s":"caution","d":"Case reports (DI)"},"cattle":{"s":"no","w":"No data"},"sheep":{"s":"no"},"goat":{"s":"no"},"deer":{"s":"no"},"pig":{"s":"no"},"chicken":{"s":"no"},"duck":{"s":"no"},"turkey":{"s":"no"},"peafowl":{"s":"no"}},
 owner="A prescription peptide for rare hormone deficiency (constant drinking/urinating) and a bleeding disorder in some breeds (Dobermans).",dvm="Confirm central DI with modified water deprivation/DDAVP trial after excluding renal, hepatic, endocrine causes.",rf="")

add(n="Octreotide",a=["Sandostatin"],tier=3,sub="3B",cls="Somatostatin analog peptide (human-approved)",rx="rx",
 ind=["insulinoma","hypoglycemia","gastrinoma","chylothorax"],ev="C",evn="Case series in dogs with insulinoma; variable response.",
 sp={"dog":{"s":"caution","d":"10-40 mcg/kg SC q8-12h","n":"Adjunct to surgery/diet/prednisone."},"cat":{"s":"caution","d":"Case reports"},"rabbit":{"s":"no"},"horse":{"s":"no"},"cattle":{"s":"no"},"sheep":{"s":"no"},"goat":{"s":"no"},"deer":{"s":"no"},"pig":{"s":"no"},"chicken":{"s":"no"},"duck":{"s":"no"},"turkey":{"s":"no"},"peafowl":{"s":"no"}},
 owner="Specialist prescription peptide for a rare pancreatic tumor in dogs.",dvm="Expensive; consider diazoxide first.",rf="")

add(n="Leuprolide",a=["Lupron Depot"],tier=3,sub="3B",cls="GnRH agonist peptide (human-approved)",rx="rx",
 ind=["ferret adrenal disease","estrus suppression","egg-laying suppression birds"],ev="B",evn="Widely used extra-label in ferrets and pet birds; deslorelin implant now preferred.",
 sp={"rabbit":{"s":"caution","d":"Extra-label","n":"Rarely indicated."},"dog":{"s":"caution","d":"Extra-label"},"cat":{"s":"caution"},"horse":{"s":"caution","n":"Studied for stallion behavior."},
     "chicken":{"s":"caution","d":"Extra-label (pet hens with chronic laying); vet","w":"Undefined","n":"Not for production birds."},"duck":{"s":"caution"},"turkey":{"s":"caution"},"peafowl":{"s":"caution"},
     "cattle":{"s":"no"},"sheep":{"s":"no"},"goat":{"s":"no"},"deer":{"s":"no"},"pig":{"s":"no"}},
 owner="A prescription peptide sometimes used to stop dangerous chronic egg-laying in pet hens. Not for birds whose eggs you eat.",dvm="Deslorelin implant is more practical.",rf="")

# ─── 3C UNAPPROVED / RESEARCH-GRADE ───
C3_REG="Not FDA-approved for any species. Sold online as 'research chemical' (human-marketed). Import of unapproved drugs is subject to FDA detention. Not on FDA GFI #256 bulk-substance list for animal compounding; FDA placed it in Category 2 (safety concern) for human compounding (2023)."
def c3(n,a,cls,ind,evn,mech,hyp,comp,extra=""):
    sp={"dog":{"s":"no","n":"No approved use; no controlled canine data."},"cat":{"s":"no","n":"No data."},"rabbit":{"s":"no","n":"No data."},
        "horse":{"s":"no","n":"No controlled equine data. Competition-prohibited."},
        "cattle":{"s":"no","w":"PROHIBITED — no withdrawal data","n":"Food animal."},"sheep":{"s":"no","w":"PROHIBITED"},"goat":{"s":"no","w":"PROHIBITED"},"deer":{"s":"no","w":"PROHIBITED"},"pig":{"s":"no","w":"PROHIBITED"},
        "chicken":{"s":"no","w":"PROHIBITED"},"duck":{"s":"no","w":"PROHIBITED"},"turkey":{"s":"no","w":"PROHIBITED"},"peafowl":{"s":"no","w":"PROHIBITED"}}
    add(n=n,a=a,tier=3,sub="3C",cls=cls,rx="unapproved",ind=ind,ev="D",evn=evn,sp=sp,
        owner="NOT APPROVED. This tool does not recommend it. The section below is a summary of what has been proposed — reference only. Do not self-administer to any animal. Discuss with your veterinarian.",
        dvm="Extra-label use of an unapproved substance is not covered by AMDUCA. Purchasing, importing, or administering carries regulatory and liability exposure. "+extra,
        reg=C3_REG,comp=comp,mech=mech,hyp=hyp,rf="Any adverse event after administration of an unapproved substance — document and report to FDA CVM.")

c3("BPC-157",["Body Protection Compound-157","pentadecapeptide"],"Synthetic gastric-derived pentadecapeptide",
   ["tendon injury","ligament injury","gastric ulcer","wound healing","cruciate","SDFT"],
   "Rodent studies only (tendon, ligament, GI mucosa), largely from one research group; limited independent replication. No controlled trials in dogs, cats, or horses. Human data: anecdotal.",
   "Proposed: angiogenesis via VEGFR2, nitric-oxide pathway modulation, growth-factor (EGR-1, FAK-paxillin) upregulation, gut-brain axis effects.",
   ["Tendon/ligament injury — equine superficial digital flexor tendonitis, canine cranial cruciate disease (hypothesized from rat tendon-to-bone models)","Gastric ulceration — mechanistic overlap with equine squamous gastric disease","Post-surgical soft-tissue recovery","Human off-label use reported oral and subcutaneous; no validated veterinary dosing exists"],
   "Prohibited: FEI, HISA, ARCI (racing), USEF. Detection windows unknown.")
c3("TB-500 (thymosin β4 fragment)",["Tβ4","thymosin beta-4"],"Synthetic peptide fragment of thymosin β4",
   ["tissue repair","tendon injury","muscle recovery","cardiac","wound healing"],
   "Thymosin β4 has legitimate wound-healing research (mouse, human trials for epidermolysis bullosa). TB-500 as sold is a synthetic fragment with no controlled veterinary trials. Long history of illicit use in racing horses and greyhounds.",
   "Proposed: actin sequestration → cell migration, angiogenesis, anti-inflammatory, reduced fibrosis.",
   ["Soft-tissue injury recovery in performance horses (hypothesized; illicit use is the main 'evidence')","Muscle recovery in working/racing dogs","Cardiac remodeling (rodent)"],
   "PROHIBITED: FEI, HISA, ARCI, greyhound racing commissions. Detectable in plasma/urine; positives have led to suspensions.")
c3("GHK-Cu (copper tripeptide)",["copper peptide","glycyl-L-histidyl-L-lysine"],"Copper-binding tripeptide",
   ["wound healing","skin","hair regrowth","dermatitis","topical"],
   "Some in-vitro and small animal-model wound data; a few small canine/equine topical wound reports of low quality. Widely used in human cosmetics (legal as a cosmetic). No controlled veterinary trials.",
   "Proposed: collagen/elastin synthesis, MMP modulation, antioxidant, angiogenesis via copper delivery.",
   ["Topical wound and dermatitis support (most plausible route — low systemic exposure)","Post-clipping hair regrowth","Pressure sores in recumbent large animals"],
   "Not specifically listed by FEI; systemic use would fall under prohibited 'non-approved substances'. Topical cosmetic route is the only regulatory-tolerated pathway.",
   extra="Topical formulations marketed as grooming products are regulated as cosmetics if no drug claims are made.")
c3("CJC-1295 / ipamorelin",["GHRH analog","ghrelin mimetic","GHRP"],"Growth-hormone secretagogue peptides",
   ["muscle mass","recovery","body condition","geriatric"],
   "Human phase I/II PK data (CJC-1295); no veterinary efficacy data. Growth-hormone axis stimulation carries theoretical risk of insulin resistance and laminitis in equids.",
   "Proposed: pulsatile GH release → IGF-1 → lean mass and repair.",
   ["Sarcopenia in geriatric dogs (hypothesized)","Recovery in performance animals","Body-condition support"],
   "PROHIBITED: FEI, HISA, ARCI (growth-hormone releasing factors).",extra="Equids: GH/IGF-1 axis stimulation is a laminitis risk (insulin dysregulation).")
c3("MOTS-c / epitalon / other 'longevity' peptides",["mitochondrial-derived peptide","epithalon"],"Marketed research peptides",
   ["aging","longevity","metabolic","mitochondrial"],
   "MOTS-c: rodent metabolic studies; epitalon: largely Russian-language literature, poor quality. No veterinary data of any kind.",
   "Proposed: AMPK activation (MOTS-c); telomerase activation (epitalon, unverified).",
   ["Marketing claims only — no defensible veterinary hypothesis"],
   "Prohibited as non-approved substances in equine competition.")

# ───────── TIER 4 · NUTRACEUTICAL ─────────
add(n="Omega-3 fatty acids (EPA/DHA)",a=["fish oil","Welactin","EFA"],tier=4,cls="Long-chain n-3 PUFA",rx="supp",
 ind=["osteoarthritis","itching","atopic dermatitis","kidney disease","heart disease","joint pain","senior dog","lameness"],ev="B",
 evn="Dogs: RCTs show reduced OA lameness and NSAID dose-sparing at high dose (Roush 2010; Fritsch 2010). Horses: reduced inflammatory markers in OA; modest clinical data. Cats: dermatology support.",
 sp={"dog":{"s":"ok","d":"~50-100 mg/kg/d combined EPA+DHA (OA); up to ~300 mg/kg^0.75","n":"Triglyceride-form fish oil; not flaxseed (poor conversion). Add vitamin E."},
     "cat":{"s":"ok","d":"~50 mg/kg/d EPA+DHA","n":"Fish flavor aids acceptance."},"rabbit":{"s":"caution","n":"Limited data."},
     "horse":{"s":"ok","d":"Fish oil 30-60 mL/d or marine-source EPA+DHA ≈ 10-20 g/d (450-500 kg)","n":"Palatability; introduce slowly."},
     "cattle":{"s":"ok","w":"0 d","n":"Rumen biohydrogenation limits effect unless protected."},"sheep":{"s":"ok","w":"0 d"},"goat":{"s":"ok","w":"0 d"},"deer":{"s":"ok","w":"0 d"},"pig":{"s":"ok","w":"0 d"},
     "chicken":{"s":"ok","w":"0 d","n":"Flaxseed diets enrich egg omega-3 (marketed)."},"duck":{"s":"ok","w":"0 d"},"turkey":{"s":"ok","w":"0 d"},"peafowl":{"s":"ok","w":"0 d"}},
 owner="The one joint supplement with real trial support in dogs. Doses that work are much higher than pet-store labels — ask your vet for the target. Takes 4-8 weeks.",
 dvm="Dose by EPA+DHA content, not oil volume. GI upset and platelet effects at very high dose; pancreatitis caution in predisposed breeds.",
 refs=["Roush JK et al. J Am Vet Med Assoc. 2010;236(1):59-66. PMID 20043800","Fritsch DA et al. J Am Vet Med Assoc. 2010;236(5):535-539. PMID 20187817"],rf="")

add(n="Glucosamine / chondroitin sulfate",a=["Cosequin","Dasuquin"],tier=4,cls="Glycosaminoglycan precursors",rx="supp",
 ind=["osteoarthritis","joint pain","cartilage","lameness"],ev="C",evn="Systematic reviews (dog, horse) find weak or inconsistent evidence; product quality varies widely. Low harm.",
 sp={"dog":{"s":"ok","d":"Glucosamine 20-30 mg/kg + chondroitin 15-20 mg/kg PO q24h (loading x4-6 wk)","n":"Choose brands with NASC seal / published content."},"cat":{"s":"ok","d":"Per label"},"rabbit":{"s":"caution"},
     "horse":{"s":"ok","d":"Glucosamine 10 g + chondroitin 2-5 g/d (500 kg)","n":"Oral bioavailability of chondroitin is poor."},
     "cattle":{"s":"ok","w":"0 d"},"sheep":{"s":"ok","w":"0 d"},"goat":{"s":"ok","w":"0 d"},"deer":{"s":"ok","w":"0 d"},"pig":{"s":"ok","w":"0 d"},"chicken":{"s":"ok","w":"0 d"},"duck":{"s":"ok"},"turkey":{"s":"ok"},"peafowl":{"s":"ok"}},
 owner="Popular, safe, and the evidence is weak. If you use it, give it 6-8 weeks and judge honestly. Weight loss and omega-3 do more.",dvm="Not a substitute for analgesia; reasonable adjunct.",rf="")

add(n="Green-lipped mussel (Perna canaliculus)",a=["GLM","Antinol"],tier=4,cls="Marine lipid/GAG extract",rx="supp",
 ind=["osteoarthritis","joint pain","lameness"],ev="B",evn="Several small controlled canine trials with modest improvement in OA scores.",
 sp={"dog":{"s":"ok","d":"Per product; typically 20-50 mg/kg/d whole-mussel powder","n":"Shellfish allergy rare."},"cat":{"s":"ok","d":"Per label"},"rabbit":{"s":"caution"},"horse":{"s":"ok","d":"Per label; limited data"},
     "cattle":{"s":"ok","w":"0 d"},"sheep":{"s":"ok"},"goat":{"s":"ok"},"deer":{"s":"ok"},"pig":{"s":"ok"},"chicken":{"s":"ok"},"duck":{"s":"ok"},"turkey":{"s":"ok"},"peafowl":{"s":"ok"}},
 owner="A joint supplement with some real dog trials behind it — a reasonable step above glucosamine.",dvm="Freeze-dried, stabilized products retain lipid fraction.",rf="")

add(n="Undenatured type II collagen (UC-II)",a=["Flexadin Advanced"],tier=4,cls="Oral tolerance collagen",rx="supp",
 ind=["osteoarthritis","joint pain","lameness"],ev="B",evn="Two small canine RCTs (Gupta et al.) showing improved mobility vs placebo and vs glucosamine/chondroitin.",
 sp={"dog":{"s":"ok","d":"40 mg/d UC-II (≈10 mg undenatured collagen) regardless of size","n":"Mechanism is immune tolerance, not dose-per-kg."},"cat":{"s":"ok","d":"Per label"},"rabbit":{"s":"caution"},"horse":{"s":"ok","d":"Per label; 1-2 g/d in some studies"},
     "cattle":{"s":"ok","w":"0 d"},"sheep":{"s":"ok"},"goat":{"s":"ok"},"deer":{"s":"ok"},"pig":{"s":"ok"},"chicken":{"s":"ok"},"duck":{"s":"ok"},"turkey":{"s":"ok"},"peafowl":{"s":"ok"}},
 owner="Small trials suggest it helps stiff dogs; tiny dose, low risk.",dvm="Hydrolyzed collagen is a different product with different (weaker) rationale.",rf="")

add(n="Cannabidiol (CBD)",a=["hemp extract","ElleVet"],tier=4,cls="Phytocannabinoid",rx="supp",
 ind=["osteoarthritis","pain","anxiety","seizures adjunct","lameness"],ev="B",evn="Dogs: placebo-controlled crossover (Gamble 2018) and later trials show reduced OA pain scores at ~2 mg/kg q12h; ALP elevation common. Cats/horses: PK and small studies only. Regulatory gray zone.",
 sp={"dog":{"s":"caution","d":"2 mg/kg PO q12h (studied); products vary","n":"Monitor ALP; CYP interactions (phenobarbital, NSAIDs). THC-free product."},"cat":{"s":"caution","d":"PK data; ~2 mg/kg","n":"Limited efficacy data."},"rabbit":{"s":"caution"},
     "horse":{"s":"caution","d":"PK studies 0.5-3 mg/kg PO; efficacy data limited","n":"Prohibited FEI/USEF (all cannabinoids)."},
     "cattle":{"s":"no","w":"No withdrawal data; not approved as feed additive","n":"AAFCO/FDA: not an approved animal food ingredient."},"sheep":{"s":"no"},"goat":{"s":"no"},"deer":{"s":"no"},"pig":{"s":"no"},"chicken":{"s":"no","n":"Not approved for laying hens — egg residue undefined."},"duck":{"s":"no"},"turkey":{"s":"no"},"peafowl":{"s":"no"}},
 owner="Real dog studies exist for arthritis pain. Buy products with a certificate of analysis. Not for animals you eat and not for competition horses.",
 dvm="Not legally an approved animal drug or feed ingredient; FDA has issued warning letters for veterinary CBD claims. Advise, do not sell, in most states.",
 refs=["Gamble LJ et al. Front Vet Sci. 2018;5:165. PMID 30083539"],comp="Prohibited FEI/USEF/AQHA.",rf="Sedation, ataxia, vomiting.")

add(n="Probiotics",a=["FortiFlora","Proviable","Probios"],tier=4,cls="Live microbial supplement",rx="supp",
 ind=["diarrhea","stress colitis","antibiotic-associated diarrhea","scours","gut health"],ev="C",evn="Modest reduction in diarrhea duration in some canine trials; calf and poultry data for specific strains. Strain- and product-specific.",
 sp={"dog":{"s":"ok","d":"Per label","n":""},"cat":{"s":"ok","d":"Per label"},"rabbit":{"s":"caution","n":"Cecotrophy; limited benefit."},"horse":{"s":"ok","d":"Per label; Saccharomyces boulardii for colitis"},
     "cattle":{"s":"ok","w":"0 d"},"sheep":{"s":"ok","w":"0 d"},"goat":{"s":"ok","w":"0 d"},"deer":{"s":"ok"},"pig":{"s":"ok","w":"0 d"},"chicken":{"s":"ok","w":"0 d","n":"Competitive exclusion products reduce Salmonella colonization in chicks."},"duck":{"s":"ok"},"turkey":{"s":"ok"},"peafowl":{"s":"ok"}},
 owner="Harmless and sometimes helpful for mild diarrhea. Bland diet (boiled chicken and rice for dogs) matters more.",dvm="Separate from antibiotic doses by ≥2 h.",rf="Diarrhea >48 h, blood, or lethargy.")

add(n="Oral hyaluronic acid / resveratrol (equine)",a=["Conquer","Equithrive"],tier=4,cls="Oral joint nutraceuticals",rx="supp",
 ind=["osteoarthritis","joint pain","lameness","hock"],ev="B",evn="Resveratrol: one placebo-controlled equine trial (hindlimb lameness) showed improvement vs placebo. Oral HA: small equine trials with mixed results.",
 sp={"horse":{"s":"ok","d":"Per label (resveratrol ~1 g q12h in trial)","n":""},"dog":{"s":"caution","d":"Limited data"},"cat":{"s":"caution"},"rabbit":{"s":"caution"},
     "cattle":{"s":"ok","w":"0 d"},"sheep":{"s":"ok"},"goat":{"s":"ok"},"deer":{"s":"ok"},"pig":{"s":"ok"},"chicken":{"s":"ok"},"duck":{"s":"ok"},"turkey":{"s":"ok"},"peafowl":{"s":"ok"}},
 owner="Among horse joint supplements, resveratrol has a placebo-controlled trial behind it; most others do not.",dvm="Adjunct to intra-articular therapy and farriery.",rf="")

# ───────── TIER 5 · HERBAL / TCVM ─────────
add(n="Curcumin (turmeric)",a=["Curcuma longa"],tier=5,cls="Polyphenol / TCVM herb",rx="supp",
 ind=["osteoarthritis","inflammation","joint pain"],ev="C",evn="Poor oral bioavailability; canine OA trials small and mixed. Traditional use in TCVM for 'blood stasis'. Low toxicity.",
 sp={"dog":{"s":"ok","d":"Per product; bioavailable formulations","n":"GI upset; possible antiplatelet effect."},"cat":{"s":"caution","n":"Palatability."},"rabbit":{"s":"caution"},"horse":{"s":"ok","d":"Per label","n":"FEI: not listed, but check product for prohibited additives (devil's claw)."},
     "cattle":{"s":"ok","w":"0 d"},"sheep":{"s":"ok"},"goat":{"s":"ok"},"deer":{"s":"ok"},"pig":{"s":"ok"},"chicken":{"s":"ok","w":"0 d","n":"Poultry feed additive studies show modest effects."},"duck":{"s":"ok"},"turkey":{"s":"ok"},"peafowl":{"s":"ok"}},
 owner="Safe, weakly supported. Fine as an add-on; not a replacement for weight loss or real analgesia.",dvm="Traditional use, limited controlled data.",rf="")

add(n="Devil's claw (Harpagophytum)",a=["harpagoside"],tier=5,cls="Iridoid glycoside herb",rx="supp",
 ind=["arthritis","musculoskeletal pain","stiffness"],ev="C",evn="Human OA trials modestly positive; equine data anecdotal. PROHIBITED in FEI/USEF competition (harpagoside).",
 sp={"horse":{"s":"caution","d":"Per label","n":"Competition-prohibited; gastric ulcer caution."},"dog":{"s":"caution","d":"Per label","n":"GI upset."},"cat":{"s":"caution"},"rabbit":{"s":"caution"},
     "cattle":{"s":"caution","w":"Undefined"},"sheep":{"s":"caution"},"goat":{"s":"caution"},"deer":{"s":"caution"},"pig":{"s":"caution"},"chicken":{"s":"caution"},"duck":{"s":"caution"},"turkey":{"s":"caution"},"peafowl":{"s":"caution"}},
 owner="A common herbal 'bute alternative' for horses. Weak evidence, and it will fail a competition drug test.",dvm="Avoid in horses with EGUS.",comp="Prohibited FEI/USEF.",rf="")

add(n="Boswellia serrata",a=["frankincense"],tier=5,cls="Boswellic acid herb",rx="supp",
 ind=["osteoarthritis","inflammation","joint pain"],ev="C",evn="One open-label canine study; human OA trials positive. Low toxicity.",
 sp={"dog":{"s":"ok","d":"Per label (~40 mg/kg/d in one study)","n":""},"cat":{"s":"caution"},"rabbit":{"s":"caution"},"horse":{"s":"ok","d":"Per label"},
     "cattle":{"s":"ok","w":"0 d"},"sheep":{"s":"ok"},"goat":{"s":"ok"},"deer":{"s":"ok"},"pig":{"s":"ok"},"chicken":{"s":"ok"},"duck":{"s":"ok"},"turkey":{"s":"ok"},"peafowl":{"s":"ok"}},
 owner="Safe herbal anti-inflammatory with thin evidence.",dvm="",rf="")

add(n="Yunnan Baiyao",a=["Yunnan Paiyao"],tier=5,cls="Proprietary TCVM hemostatic formula",rx="supp",
 ind=["bleeding","hemangiosarcoma","epistaxis","hemostasis"],ev="C",evn="In-vitro platelet effects; small canine studies inconsistent. Widely used in oncology palliative care. Contents proprietary.",
 sp={"dog":{"s":"caution","d":"Per label (capsules; 'red pill' for acute bleeding)","n":"Hepatotoxicity reported with prolonged use."},"cat":{"s":"caution"},"rabbit":{"s":"caution"},"horse":{"s":"caution","d":"Used for EIPH anecdotally","n":"Competition: proprietary contents — risk."},
     "cattle":{"s":"no","w":"Undefined"},"sheep":{"s":"no"},"goat":{"s":"no"},"deer":{"s":"no"},"pig":{"s":"no"},"chicken":{"s":"no"},"duck":{"s":"no"},"turkey":{"s":"no"},"peafowl":{"s":"no"}},
 owner="A Chinese herbal formula vets sometimes use for bleeding tumors in dogs. Not a substitute for emergency care.",dvm="Traditional use, limited controlled data; monitor liver enzymes.",rf="Pale gums, distended abdomen, weakness — internal bleeding, emergency.")

add(n="Tea tree oil / essential oils (TOXIC)",a=["Melaleuca","eucalyptus","pennyroyal","wintergreen","pine oil"],tier=5,cls="Volatile oils",rx="supp",
 ind=["skin","fleas","toxicity","poisoning"],ev="X",evn="Concentrated tea tree oil causes ataxia, tremors, hepatotoxicity in dogs and cats; pennyroyal is hepatotoxic; wintergreen = methyl salicylate (aspirin toxicity). Birds are extremely sensitive to aerosolized oils.",
 sp={"dog":{"s":"no","n":"Never undiluted; ≥7-8 mL topically has caused death."},"cat":{"s":"no","n":"Cats cannot glucuronidate phenols — even diffusers cause respiratory distress."},"rabbit":{"s":"no"},"horse":{"s":"caution","n":"Diluted topical products exist; avoid ingestion."},
     "cattle":{"s":"caution"},"sheep":{"s":"caution"},"goat":{"s":"caution"},"deer":{"s":"caution"},"pig":{"s":"caution"},"chicken":{"s":"no","n":"Avian respiratory system — no diffusers in coops."},"duck":{"s":"no"},"turkey":{"s":"no"},"peafowl":{"s":"no"}},
 owner="'Natural' is not 'safe.' Tea tree oil poisons dogs and cats; essential-oil diffusers harm cats and birds.",dvm="Decontaminate (bathe), supportive care, hepatic monitoring.",rf="Wobbling, drooling, tremors, or breathing difficulty after oil exposure.")

add(n="Garlic / onion / allium (TOXIC)",a=["Allium","chives","leeks"],tier=5,cls="Organosulfur-containing plants",rx="supp",
 ind=["fleas","deworming","toxicity","poisoning","anemia"],ev="X",evn="Oxidative Heinz-body hemolytic anemia in dogs, cats, horses, cattle. 'Garlic for fleas' has no efficacy data and documented toxicity.",
 sp={"dog":{"s":"no","n":"Toxic ≥15-30 g/kg onion; garlic ~5x more potent. Japanese breeds more sensitive."},"cat":{"s":"no","n":"Highly sensitive."},"rabbit":{"s":"no"},"horse":{"s":"no","n":"Hemolysis with chronic feeding."},
     "cattle":{"s":"no","n":"Onion toxicosis in cattle documented."},"sheep":{"s":"caution","n":"Sheep are relatively tolerant."},"goat":{"s":"caution"},"deer":{"s":"caution"},"pig":{"s":"caution"},"chicken":{"s":"caution","n":"Small amounts tolerated; avoid."},"duck":{"s":"caution"},"turkey":{"s":"caution"},"peafowl":{"s":"caution"}},
 owner="Garlic does not repel fleas and does cause anemia. Do not feed alliums to dogs, cats, or horses.",dvm="Onset 1-5 d post-ingestion; check PCV, Heinz bodies.",rf="Pale gums, red/brown urine, weakness.")

add(n="Calendula / aloe / honey (topical)",a=["Manuka honey","Medihoney","Calendula officinalis"],tier=5,cls="Topical botanicals",rx="supp",
 ind=["wound healing","burns","hot spot","bumblefoot","skin"],ev="B",evn="Medical-grade honey: controlled wound data in horses (distal limb wounds) and dogs. Calendula/aloe: weak data, low harm topically. Aloe latex is a purgative if ingested.",
 sp={"dog":{"s":"ok","d":"Medical-grade honey under bandage; change q24-48h","n":"Prevent licking."},"cat":{"s":"ok","d":"Same","n":"E-collar."},"rabbit":{"s":"ok"},"horse":{"s":"ok","d":"Manuka honey under bandage for distal limb wounds","n":"Evidence for reduced infection and faster healing."},
     "cattle":{"s":"ok","w":"0 d"},"sheep":{"s":"ok"},"goat":{"s":"ok"},"deer":{"s":"ok"},"pig":{"s":"ok"},"chicken":{"s":"ok","w":"0 d","n":"Bumblefoot after debridement."},"duck":{"s":"ok"},"turkey":{"s":"ok"},"peafowl":{"s":"ok"}},
 owner="Medical-grade honey is one of the few 'natural' wound treatments with veterinary trial support. Use sterile medical honey, not the kitchen jar, under a clean dressing.",dvm="Osmotic antibacterial effect; useful in contaminated wounds pending debridement.",rf="Wounds that are deep, over joints, or from bites.")

# ───────── TIER 6 · MANUAL / PHYSICAL ─────────
add(n="Cold therapy (cold hosing, icing, cryotherapy)",a=["cryotherapy","ice boots","cold hosing"],tier=6,cls="Physical modality",rx="proc",
 ind=["lameness","tendon injury","laminitis","swelling","acute injury","sprain","post-exercise"],ev="A",evn="Equine: continuous distal limb cryotherapy reduces laminitis severity in sepsis-associated cases (van Eps studies). Acute soft-tissue inflammation: standard of care across species.",
 sp={"horse":{"s":"ok","d":"Cold hose/ice 15-20 min q4-6h for 48-72 h; laminitis prophylaxis: continuous ice-slurry to mid-cannon","n":"Most effective single non-drug intervention."},
     "dog":{"s":"ok","d":"Ice pack in towel 10-15 min q4-6h x48-72 h post-injury","n":""},"cat":{"s":"caution","n":"Tolerance limited."},"rabbit":{"s":"caution"},
     "cattle":{"s":"ok","w":"0 d"},"sheep":{"s":"ok"},"goat":{"s":"ok"},"deer":{"s":"caution"},"pig":{"s":"ok"},"chicken":{"s":"caution","n":"Cool water foot soak for bumblefoot inflammation."},"duck":{"s":"caution"},"turkey":{"s":"caution"},"peafowl":{"s":"caution"}},
 owner="The most effective thing an owner can do for a fresh leg injury or a horse at laminitis risk — and it costs nothing. 15-20 minutes, several times a day, for the first 2-3 days.",dvm="Switch to heat/controlled exercise after the acute phase (72 h).",rf="Non-weight-bearing lameness, heat + bounding digital pulses, or swelling that spreads.")

add(n="Weight management",a=["caloric restriction","body condition score"],tier=6,cls="Lifestyle intervention",rx="proc",
 ind=["osteoarthritis","lameness","laminitis","equine metabolic syndrome","diabetes","senior dog","joint pain"],ev="A",evn="Dogs: caloric restriction reduced OA lameness and delayed onset (Kealy lifetime study). Horses: obesity drives insulin dysregulation and laminitis. Single most effective intervention for OA.",
 sp={"dog":{"s":"ok","d":"Target BCS 4-5/9; 1-2% body weight loss per week","n":"Therapeutic weight-loss diets preserve lean mass."},"cat":{"s":"ok","d":"0.5-1%/wk (faster → hepatic lipidosis)","n":""},"rabbit":{"s":"ok","d":"Hay-based diet"},
     "horse":{"s":"ok","d":"Target BCS 5/9; hay at 1.5% BW, soaked; grazing muzzle","n":"Never starve — hyperlipemia risk in ponies/donkeys."},"cattle":{"s":"ok"},"sheep":{"s":"ok"},"goat":{"s":"ok"},"deer":{"s":"ok"},"pig":{"s":"ok"},"chicken":{"s":"ok","n":"Obese hens: fatty liver hemorrhagic syndrome."},"duck":{"s":"ok"},"turkey":{"s":"ok"},"peafowl":{"s":"ok"}},
 owner="If your dog or horse is overweight, this beats every supplement on this list. Ask for a body-condition score and a calorie target.",dvm="Kealy RD et al. JAVMA 2000/2002 — lifetime restricted-feeding Labrador study.",refs=["Kealy RD et al. J Am Vet Med Assoc. 2002;220(9):1315-1320. PMID 11991408"],rf="")

add(n="Farriery / hoof balance",a=["corrective shoeing","trimming"],tier=6,cls="Mechanical intervention",rx="proc",
 ind=["lameness","laminitis","navicular","hoof abscess","arthritis","hock"],ev="A",evn="Hoof balance is a primary driver of distal limb loading; therapeutic shoeing is standard of care for laminitis, navicular syndrome, and many OA cases.",
 sp={"horse":{"s":"ok","d":"Trim cycle 4-6 wk; radiograph-guided for laminitis/navicular","n":"Coordinate vet + farrier."},"cattle":{"s":"ok","d":"Hoof trimming 1-2x/yr; blocks for sole ulcers","w":"0 d"},"sheep":{"s":"ok","d":"Trim; footrot management"},"goat":{"s":"ok","d":"Trim q6-8 wk"},"deer":{"s":"caution"},"pig":{"s":"ok"},
     "dog":{"s":"ok","d":"Nail trimming; traction","n":"Overgrown nails alter gait."},"cat":{"s":"ok"},"rabbit":{"s":"ok","d":"Nail trim; soft flooring (pododermatitis)"},"chicken":{"s":"ok","d":"Perch diameter/height; bumblefoot prevention"},"duck":{"s":"ok"},"turkey":{"s":"ok"},"peafowl":{"s":"ok"}},
 owner="For horses, a good farrier is joint care. For chickens, correct perch height prevents bumblefoot.",dvm="",rf="Hoof heat, pulses, reluctance to move — laminitis.")

add(n="Controlled exercise / rehabilitation",a=["physiotherapy","hydrotherapy","underwater treadmill"],tier=6,cls="Physical rehabilitation",rx="proc",
 ind=["osteoarthritis","tendon injury","post-surgical","cruciate","lameness","obesity"],ev="B",evn="Canine: hydrotherapy improves function post-TPLO and in OA; equine: controlled walking programs central to tendon rehab (rest alone worsens outcomes).",
 sp={"dog":{"s":"ok","d":"Short frequent leash walks; swimming/UWTM 2-3x/wk","n":"Avoid ball-chasing/stairs during flare."},"cat":{"s":"ok","d":"Environmental enrichment, ramps, low-sided litter box"},"rabbit":{"s":"ok"},
     "horse":{"s":"ok","d":"Tendon: hand-walk 10-20 min/d increasing weekly per ultrasound; OA: consistent daily turnout/light work","n":"Box rest alone impairs tendon remodeling."},"cattle":{"s":"ok"},"sheep":{"s":"ok"},"goat":{"s":"ok"},"deer":{"s":"caution"},"pig":{"s":"ok"},"chicken":{"s":"ok"},"duck":{"s":"ok"},"turkey":{"s":"ok"},"peafowl":{"s":"ok"}},
 owner="Rest is not the answer for arthritis — short, regular, low-impact movement is. Ramps instead of stairs; non-slip rugs; keep it consistent.",dvm="Certified canine rehab (CCRP/CCRT) referral where available.",rf="Sudden non-weight-bearing lameness.")

add(n="Acupuncture",a=["dry needling","electroacupuncture","TCVM"],tier=6,cls="Manual therapy (regulated as veterinary medicine in TX)",rx="proc",
 ind=["osteoarthritis","back pain","IVDD","chronic pain","lameness"],ev="B",evn="Dogs: RCTs for IVDD recovery (electroacupuncture) and OA pain with mixed but generally positive results. Horses: back pain studies small. Placebo control difficult.",
 sp={"dog":{"s":"ok","d":"Weekly x4-6, then taper","n":"Texas: must be performed by a licensed veterinarian."},"cat":{"s":"ok"},"rabbit":{"s":"caution"},"horse":{"s":"ok","d":"q1-2 wk","n":"Texas: DVM only. Competition: permitted."},
     "cattle":{"s":"ok","w":"0 d"},"sheep":{"s":"caution"},"goat":{"s":"caution"},"deer":{"s":"caution"},"pig":{"s":"caution"},"chicken":{"s":"caution"},"duck":{"s":"caution"},"turkey":{"s":"caution"},"peafowl":{"s":"caution"}},
 owner="Some real evidence for pain and nerve recovery in dogs. In Texas only a veterinarian may perform it on animals.",dvm="Texas Veterinary Practice Act: acupuncture is the practice of veterinary medicine.",reg="Texas: DVM only (TBVME).",rf="")

add(n="Chiropractic / osteopathic manipulation",a=["animal chiropractic","VOM","osteopathy"],tier=6,cls="Manual therapy (restricted in TX)",rx="proc",
 ind=["back pain","stiffness","performance","lameness"],ev="C",evn="Equine: small studies show transient improvement in spinal mobility/pain thresholds; no evidence for lasting structural change. Canine: minimal controlled data. Low harm with trained practitioner; harm reported with untrained manipulation.",
 sp={"horse":{"s":"caution","d":"Per practitioner","n":"Texas: DVM, or a licensed DC with veterinary referral/supervision (TBVME Rule 573.14)."},"dog":{"s":"caution","d":"Per practitioner","n":"Same TX rule; contraindicated with IVDD, fractures, instability."},"cat":{"s":"caution"},"rabbit":{"s":"no","n":"Fragile spine — do not manipulate."},
     "cattle":{"s":"caution"},"sheep":{"s":"caution"},"goat":{"s":"caution"},"deer":{"s":"no"},"pig":{"s":"caution"},"chicken":{"s":"no"},"duck":{"s":"no"},"turkey":{"s":"no"},"peafowl":{"s":"no"}},
 owner="Popular for horses and working dogs; evidence is thin and Texas law requires a veterinarian's involvement. Never let anyone 'adjust' a rabbit or a dog with a suspected disc problem.",
 dvm="Rule out fracture, neoplasia, IVDD, and instability before referral.",reg="Texas: DVM or DC under veterinary referral (TBVME Rule 573.14).",rf="Neck/back pain with weakness, dragging paws, or incontinence — do not manipulate; emergency.")

add(n="Therapeutic laser / PEMF / shockwave",a=["photobiomodulation","Assisi loop","ESWT"],tier=6,cls="Energy-based modalities",rx="proc",
 ind=["osteoarthritis","tendon injury","wound healing","back pain","lameness"],ev="B",evn="Shockwave (ESWT): controlled equine data for proximal suspensory desmitis and navicular; provides analgesia (FEI/USEF restrict use pre-competition). Laser: small canine OA and wound trials, mixed. PEMF: mostly uncontrolled.",
 sp={"horse":{"s":"ok","d":"ESWT by vet; laser per protocol","n":"ESWT analgesia can mask injury — competition restrictions (USEF: no ESWT within 3 days)."},"dog":{"s":"ok","d":"Laser 2-3x/wk x3-4 wk","n":"Owner PEMF loops are low-risk."},"cat":{"s":"ok"},"rabbit":{"s":"caution"},
     "cattle":{"s":"caution"},"sheep":{"s":"caution"},"goat":{"s":"caution"},"deer":{"s":"caution"},"pig":{"s":"caution"},"chicken":{"s":"caution"},"duck":{"s":"caution"},"turkey":{"s":"caution"},"peafowl":{"s":"caution"}},
 owner="Laser and PEMF devices are low-risk with modest evidence. Shockwave is a vet procedure with real horse data.",dvm="Laser: eye protection; avoid over tumors, pregnant uterus, growth plates.",comp="ESWT restricted pre-competition (USEF/FEI).",rf="")

# ───────── REGULATORY REFERENCE (DVM) ─────────
add(n="Prohibited extra-label drugs in food animals (21 CFR 530.41)",a=["AMDUCA prohibited list","FARAD"],tier=2,cls="Regulatory reference",rx="rx",
 ind=["withdrawal","food animal","prohibited","AMDUCA","chickens","cattle","goats","pigs","residue"],ev="A",evn="Federal regulation. Applies to all food-producing animals including backyard poultry and farmed deer.",
 sp={k:{"s":"no","n":"See DVM note."} for k in FOOD} | {k:{"s":"ok","n":"Companion animals not affected."} for k in ["dog","cat","rabbit","horse"]},
 owner="Some drugs are illegal in any animal that produces food — including your backyard hens. Your vet cannot prescribe them for chickens even if they work in dogs.",
 dvm="PROHIBITED extra-label in food animals: chloramphenicol; clenbuterol; diethylstilbestrol; dimetridazole, ipronidazole, other nitroimidazoles (METRONIDAZOLE); furazolidone, nitrofurazone (topical included); fluoroquinolones (enrofloxacin — label indications only); glycopeptides (vancomycin); sulfonamides in lactating dairy cattle (except approved); phenylbutazone in female dairy cattle ≥20 mo; cephalosporins (extra-label restrictions in cattle, swine, chickens, turkeys); gentian violet; adamantanes and neuraminidase inhibitors (amantadine, oseltamivir) in chickens, turkeys, ducks. Horses: treated as food animals for slaughter export — 'not for food' declaration required on medical records for bute etc.",
 reg="21 CFR 530.41; GFI #263 (2023) moved all medically important antimicrobials to Rx.",rf="")

# ───────── TIER 6 ADDITIONS (v0.1.3) — dog and horse only ─────────
_OUT={k:{"s":"no","n":"Outside the scope of this card (dog and horse only)."} for k in ["cat","rabbit"]} | {k:{"s":"no","n":"Outside the scope of this card (dog and horse only).","w":"n/a — no drug administered"} for k in FOOD}

add(n="Osteopathic manipulative treatment (OMT) — dog and horse",a=["osteopathy","veterinary osteopathy","OMT","equine osteopath","canine osteopath"],tier=6,cls="Manual therapy (restricted in TX)",rx="proc",
 ind=["back pain","stiffness","poor performance","sacroiliac","neck pain","lameness","musculoskeletal pain"],ev="C",
 evn="No controlled trial of osteopathy as a distinct method in dogs or horses. Closest evidence is equine spinal manipulation (HVLA) and mobilisation: short-term increases in trunk flexibility and pressure-pain thresholds in randomised trials, no data on lasting change or on horses with confirmed back pathology. Canine: one blinded owner-assessed trial of combined acupuncture plus manual therapy showed short-term comfort gains; no osteopathy-specific canine trial.",
 sp={"dog":{"s":"caution","d":"Per practitioner; typically 1-3 sessions 1-4 wk apart, reassessed each visit","n":"Texas: DVM, or a non-veterinarian under veterinary supervision with signed owner acknowledgment (TBVME 573.14). Contraindicated with IVDD, fracture, atlantoaxial or lumbosacral instability, neoplasia, discospondylitis."},
     "horse":{"s":"caution","d":"Per practitioner; typically 1-3 sessions 2-4 wk apart with objective reassessment (flexion, pressure algometry, ridden evaluation)","n":"Texas 573.14 as for dog. Rule out fracture, kissing spines with impingement, sacroiliac instability, neurologic disease before manipulation. Sedated manipulation is not standard."}} | _OUT,
 owner="Osteopathy uses hands-on techniques — gentle joint mobilisation, soft-tissue and myofascial work, and sometimes quick low-amplitude thrusts — for back, neck and pelvic stiffness in dogs and horses. Small studies show short-term loosening and less back tenderness in horses; there is no proof it fixes an underlying problem. In Texas it must be done by, or under, a veterinarian, and you sign a form acknowledging it is an alternate therapy. Never let anyone manipulate a dog with a suspected slipped disc or a horse with a suspected fracture.",
 dvm="Diagnosis first: imaging or a neurological examination that excludes IVDD, instability, fracture, neoplasia and infection is the gate to referral. Treat OMT as an adjunct to a rehabilitation plan with measurable outcomes (pressure algometry, ROM, gait analysis, owner questionnaires) and stop when two sessions show no objective change. Texas 573.14: alternate therapy — signed owner acknowledgment in the permanent record; non-veterinarian practitioners only under your direct or general supervision. Evidence grade C: extrapolated from equine spinal manipulation trials; no osteopathy-specific controlled data in either species.",
 reg="22 TAC 573.14 (alternate therapy; signed owner acknowledgment; veterinary supervision of non-veterinarians).",
 comp="Not prohibited by FEI/USEF; competition-day manipulation may be restricted by event rules — check the show's veterinary regulations.",
 refs=["Haussler KK, Hill AE, Puttlitz CM, McIlwraith CW. Am J Vet Res. 2007;68(5):508-516. PMID 17472450",
       "Sullivan KA, Hill AE, Haussler KK. Equine Vet J. 2008;40(1):14-20. PMID 18083655",
       "Haussler KK, Martin CE, Hill AE. Equine Vet J Suppl. 2010;(38):695-702. PMID 21059083",
       "Lane DM, Hill SA. Can Vet J. 2016;57(4):407-414. PMID 27041759"],
 rf="Back or neck pain with weakness, knuckling, dragging limbs, incontinence, or sudden inability to rise — do not manipulate; emergency.")

add(n="Physical therapy / veterinary rehabilitation — dog and horse",a=["physiotherapy","physical rehabilitation","rehab","CCRP","CCRT","hydrotherapy","underwater treadmill","therapeutic exercise"],tier=6,cls="Structured rehabilitation program",rx="proc",
 ind=["post-surgical","cruciate","TPLO","osteoarthritis","tendon injury","suspensory","IVDD recovery","muscle atrophy","obesity","geriatric mobility","back pain","return to work"],ev="B",
 evn="Canine: postoperative rehabilitation after cruciate surgery improves force-plate limb function at 6 months versus exercise restriction (n=51) and early physiotherapy after TPLO restores thigh circumference and stifle range of motion by 6 weeks (n=8); reviews summarise modality evidence, much of it small or extrapolated. Equine: practitioner-level reviews of thermal therapy, therapeutic ultrasound, shockwave, laser, stretching and core-strengthening; few controlled outcome trials, tendon rehabilitation rests on controlled-loading principles.",
 sp={"dog":{"s":"ok","d":"Program set by DVM or certified rehabilitation practitioner (CCRP/CCRT, DACVSMR): passive ROM and stretching 2-3x/d, therapeutic exercise progressing weekly, underwater treadmill or swimming 2-3x/wk, cryotherapy first 72 h post-op then heat before exercise; typical course 6-12 wk","n":"Start within days of surgery when the surgeon agrees. Obesity management is part of every OA program."},
     "horse":{"s":"ok","d":"Program set by DVM (ACVSMR or equine rehabilitation trained): controlled hand-walking increasing per ultrasound, dynamic mobilisation (carrot stretches) 5 reps each direction daily, core-strengthening and pole work, cold therapy 15-20 min after work, therapeutic ultrasound/laser/shockwave per modality protocol; tendon courses 3-9 mo","n":"Box rest alone impairs tendon remodelling. Reassess with ultrasound every 4-8 wk before increasing load."}} | _OUT,
 owner="Physical therapy for dogs and horses is a planned program — stretching, specific exercises, water treadmill or swimming, cold and heat, sometimes laser or shockwave — run by a veterinarian or a certified rehabilitation therapist. It has the best evidence of any Tier 6 option: dogs recover leg function after cruciate surgery measurably better with rehab than with crate rest alone. It is not a substitute for diagnosis or surgery when those are needed, and the exercises must be done at home between visits.",
 dvm="Prescribe rehabilitation like a drug: diagnosis, goal, modality, dose, frequency, duration, reassessment date. Objective outcome measures: force plate or stance analysis, goniometry, thigh circumference, timed walk, validated owner questionnaires (LOAD, CBPI); horses: ultrasound cross-sectional area and fibre pattern, ridden assessment. Credentials to look for: CCRP (Tennessee), CCRT (CRI), DACVSMR. Texas: rehabilitation is veterinary practice; a non-veterinarian therapist works under veterinary supervision and any musculoskeletal manipulation component falls under 573.14. Combine with multimodal analgesia (NSAID, gabapentin as indicated) so the patient can load the limb.",
 reg="22 TAC 573.14 applies to any manipulation component; rehabilitation itself is within the veterinary practice act — supervision of non-veterinarian therapists required.",
 comp="Modalities are not prohibited; check FEI/USEF rules on treatment during competition periods.",
 refs=["Marsolais GS, Dvorak G, Conzemius MG. J Am Vet Med Assoc. 2002;220(9):1325-1330. PMID 11991410",
       "Monk ML, Preston CA, McGowan CM. Am J Vet Res. 2006;67(3):529-536. PMID 16506922",
       "Millis DL, Ciuperca IA. Vet Clin North Am Small Anim Pract. 2015;45(1):1-27. PMID 25432679",
       "Kaneps AJ. Vet Clin North Am Equine Pract. 2016;32(1):167-180. PMID 26898959"],
 rf="Sudden non-weight-bearing lameness, swelling with heat and fever, or neurologic decline during a rehab program — stop and re-examine.")

# ───────── PRESCRIBING & DISPENSING REFERENCE (DVM) — v0.1.2 ─────────
# Regulatory text verified 2026-09-07 against eCFR (21 CFR 530, 558.6, 1306.05), FDA GFI #256 / #263,
# Texas 22 TAC 573 (Subchapter E), Texas HSC 481, and AVMA prescription FAQ. No doses. Federal + Texas;
# other states: substitute the state practice act.
_ALL=["dog","cat","rabbit","horse","cattle","sheep","goat","deer","pig","chicken","duck","turkey","peafowl"]
_SP=lambda note_c,note_f: {k:{"s":"ok","n":note_c} for k in ["dog","cat","rabbit","horse"]} | {k:{"s":"ok","n":note_f,"w":"n/a — reference card"} for k in FOOD}

add(n="VCPR — veterinarian-client-patient relationship",a=["VCPR","valid relationship","telemedicine"],tier=2,cls="Prescribing reference",rx="rx",
 ind=["prescription","VCPR","dispense","refill","telemedicine","online pharmacy","who can prescribe"],ev="A",
 evn="Federal definition 21 CFR 530.3(i); Texas 22 TAC 573.41 makes prescribing, dispensing or ordering any Rx drug without a VCPR unprofessional conduct.",
 sp=_SP("Applies to every Rx, controlled substance, compounded drug and extra-label use.","Also the gate for VFD feed and any extra-label use with withdrawal."),
 owner="Your veterinarian can only prescribe for an animal they actually know: they have examined it (or made timely visits to the farm), take responsibility for its care, and are available for follow-up. This is why a clinic cannot phone in a prescription for an animal it has never seen.",
 dvm="Federal VCPR (21 CFR 530.3(i)) has three elements: (1) the veterinarian assumes responsibility for medical judgments and the client agrees to follow instructions; (2) sufficient knowledge of the animal(s) to initiate at least a general or preliminary diagnosis — by examination or medically appropriate and timely visits to the premises; (3) the veterinarian is readily available for follow-up on adverse reactions or treatment failure. Texas 573.41: no prescribing, administering, dispensing, delivering or ordering delivered any Rx drug without first establishing a VCPR. For VFD feed, 21 CFR 558.6(b)(1) defers to the state VCPR only if it contains the federal elements. Document the exam or premises visit that establishes the VCPR and its date; a VCPR that lapses (commonly treated as 12 months without a visit) does not support refills. Telemedicine: the federal AMDUCA definition requires in-person knowledge; state rules on establishing a VCPR electronically change frequently — check the current TBVME rule before relying on it.",
 reg="21 CFR 530.3(i); 22 TAC 573.41; 21 CFR 558.6(b)(1).",rf="")

add(n="Prescription — required elements and refills",a=["writing a prescription","Rx elements","script"],tier=2,cls="Prescribing reference",rx="rx",
 ind=["prescription","refill","script","how to write","DEA number","quantity","directions","sig"],ev="A",
 evn="Controlled substances: 21 CFR 1306.05(a) and 1306.12/1306.22. Non-controlled: AVMA prescription guidance and state pharmacy law.",
 sp=_SP("Same elements for all species; add species and animal identification.","Add species, number of animals, and the withdrawal time on every food-animal prescription."),
 owner="A valid prescription names the clinic and veterinarian, you and your animal, the drug, its strength and form, how much, how to give it, how many refills, and the date. Pharmacies will not fill one that is missing these.",
 dvm="Every prescription: date issued; client name and address; animal identification and species (herd/flock/lot for groups); drug established name, strength, dosage form; quantity (in words and figures for controlled substances); directions for use (dose, route, frequency, duration); number of refills authorized (write 'no refills' rather than leaving blank); cautionary statements; withdrawal time for any food animal; veterinarian name, address, telephone, license number, DEA number when the drug is controlled; signature. Controlled substances (21 CFR 1306.05): must be dated and signed on the day issued, paper prescriptions manually signed in ink or printed and hand-signed, electronic prescriptions only through a DEA-certified (Part 1311) application. Schedule II: no refills (1306.12); a new prescription each time. Schedules III–IV: maximum 5 refills within 6 months of issue (1306.22). Schedule V: per state law. Texas: veterinarians may issue written (not electronic) controlled-substance prescriptions (HSC 481.0755). Keep a copy of every prescription in the medical record; note phoned-in and refill authorizations with date and who took the call.",
 reg="21 CFR 1306.05, 1306.12, 1306.22; Tex. Health & Safety Code 481.0755; AVMA Prescriptions & Pharmacies FAQ.",rf="")

add(n="Dispensed drug label — required elements",a=["dispensing label","container label","pharmacy label"],tier=2,cls="Prescribing reference",rx="rx",
 ind=["label","dispense","container","labeling","extra-label label","withdrawal on label"],ev="A",
 evn="Texas 22 TAC 573.40 (all dispensed drugs) and 21 CFR 530.12 (extra-label drugs, all states).",
 sp=_SP("573.40 elements on the immediate container.","573.40 plus 530.12: the veterinarian's withdrawal time must be printed on the label."),
 owner="Every bottle a clinic hands you must carry a label with the clinic's name and phone, the date, your name, the animal's species, the drug name, strength and amount, directions, and warnings. If it doesn't, ask for one.",
 dvm="Texas 573.40 — label affixed to the immediate container (or a labeled outer container if the vial is too small): veterinarian's name, address, telephone with area code; date dispensed; patient/client name (client address if controlled); species; drug name, strength, quantity; directions for use; cautionary statements required by law ('not for human consumption', poison, withdrawal periods). Federal 530.12 adds, for any extra-label drug in any species: name and address of the prescribing veterinarian (or pharmacy); established name of each active ingredient; directions including class/species or identification of animal, herd, flock, pen or lot; dosage, frequency, route, duration; cautionary statements; and the veterinarian's specified withdrawal, withholding or discard time for meat, milk, eggs or other food. Food animals: never leave withdrawal blank — write the number of days (from label or FARAD) and the date the animal may be sold.",
 reg="22 TAC 573.40; 21 CFR 530.12.",rf="")

add(n="Extra-label drug use (AMDUCA) — conditions and records",a=["AMDUCA","ELDU","off-label","extra-label"],tier=2,cls="Prescribing reference",rx="rx",
 ind=["extra-label","off-label","AMDUCA","records","food animal","withdrawal","human drug in animals","cascade"],ev="A",
 evn="21 CFR 530.5 (records), 530.20 (food animals), 530.12 (labeling), 530.41 (prohibited). Texas 573.45 requires community standard of humane care.",
 sp=_SP("Extra-label use of approved animal or human drugs is lawful under a VCPR; keep the 530.5 record.","Food animals: 530.20 cascade, substantially extended withdrawal, animal identification, and no prohibited drugs (see 530.41 card)."),
 owner="Most drugs a vet uses in cats, rabbits, goats, chickens and other species were approved for a different animal. That is legal when a veterinarian directs it, but for animals that produce meat, milk or eggs the vet must set a withdrawal time and you must respect it.",
 dvm="Permitted only by or under the supervision of a licensed veterinarian within a VCPR, for therapeutic purposes (not production), with an approved animal or human drug — never a bulk-substance compound in a food animal except as GFI #256 allows. Food animals (530.20): allowed only when no approved animal drug labeled for the use contains the same active ingredient in the required dosage form and concentration, or the approved drug is clinically ineffective; make a careful diagnosis; establish a substantially extended withdrawal supported by data (FARAD); maintain animal identification; assure the withdrawal is met. Human-approved drugs in food animals need an appropriate medical rationale and, if residue safety is unknown, the animal may not enter the food supply. Records (530.5), kept 2 years or longer if state law requires: established name of each active ingredient; condition treated; species; dosage; duration; number of animals; specified withdrawal/withholding/discard time. Label per 530.12. Texas 573.45: veterinarian's discretion, judged against the community standard of humane care.",
 reg="21 CFR 530.5, 530.12, 530.20, 530.41; 22 TAC 573.45; FARAD (farad.org) for withdrawal intervals.",rf="")

add(n="Controlled substances — DEA and Texas duties",a=["DEA","Schedule II","CII","CIII","controlled drugs","PMP","biennial inventory"],tier=2,cls="Prescribing reference",rx="rx",
 ind=["controlled substance","DEA","ketamine","buprenorphine","butorphanol","tramadol","diazepam","phenobarbital","hydrocodone","pentobarbital","euthanasia","PMP","inventory","Form 222"],ev="A",
 evn="21 CFR 1301 (registration), 1304 (records, inventory), 1306 (prescriptions); Texas 22 TAC 573.43, HSC 481.",
 sp=_SP("Same duties for all species.","Same duties; food-animal use adds AMDUCA withdrawal (most CS have none — FARAD)."),
 owner="Some pain, sedation and seizure drugs are federally controlled. Clinics must keep them locked, count them, and record every dose, and they cannot phone in refills for some of them. Return unused controlled drugs to a take-back site, never the trash.",
 dvm="Registration: DEA registration (Form 224) for every location where CS are stored or dispensed; Texas requires DEA registration plus a current Texas veterinary license (the separate DPS controlled-substance registration ended in 2016 — 573.43). Records (21 CFR 1304): initial inventory, then a biennial inventory (1304.11); receipt, dispensing, administration and disposal records kept 2 years and readily retrievable; Schedule II records kept separately from III–V; Schedule II ordered only on DEA Form 222 or CSOS; disposal by reverse distributor with DEA Form 41 documentation. Storage: securely locked, substantially constructed cabinet; theft or significant loss reported to DEA (Form 106) within one business day of discovery. Prescriptions: see the Prescription card — CII no refills, CIII–IV ≤5 refills in 6 months, DEA number on every CS prescription. Texas PMP: veterinarians are exempt from checking the PMP before prescribing and may view only the animal's dispensing history, not the owner's (HSC 481.0764); the next-business-day reporting duty in HSC 481.075 is written for dispensing pharmacists — confirm with TSBP/TBVME whether in-clinic veterinary dispensing must report, and record the answer in the practice SOP. Common veterinary schedules: II hydrocodone, morphine, fentanyl, hydromorphone, methadone, pentobarbital (euthanasia solutions with other agents may be III); III ketamine, buprenorphine, tiletamine-zolazepam, testosterone, anabolic steroids; IV butorphanol, tramadol, diazepam, midazolam, alprazolam, phenobarbital, zolpidem; V pregabalin. Gabapentin and xylazine are not federally scheduled but are scheduled or restricted in several states — check the state list.",
 reg="21 CFR 1301, 1304.04, 1304.11, 1305, 1306.05, 1306.12, 1306.22; 22 TAC 573.43; Tex. Health & Safety Code 481.075, 481.0755, 481.0764.",rf="")

add(n="Compounded drugs — FDA GFI #256",a=["compounding","GFI 256","bulk drug substance","office stock"],tier=2,cls="Prescribing reference",rx="rx",
 ind=["compounding","compounded","flavored","transdermal","bulk substance","office stock","pharmacy"],ev="A",
 evn="FDA GFI #256 (effective April 2022); Texas 22 TAC 573.44 limits veterinary compounding to a specific animal or herd under a VCPR.",
 sp=_SP("Patient-specific compounding from bulk substances is possible when no approved drug can meet the need.","Compounding from bulk substances for food animals is not permitted except antidotes (and sedatives/anesthetics for free-ranging wildlife)."),
 owner="A compounded drug is made by a pharmacy for one animal when no manufactured product fits — a smaller dose, a flavored liquid, a cat-sized transdermal. It is not FDA-approved, its strength is not verified by FDA, and it cannot be used in animals that produce food except in narrow cases.",
 dvm="Compounding from an approved finished drug (crushing, diluting, flavoring) is manipulation of an approved product and falls under extra-label rules. Compounding from bulk drug substances is unapproved; FDA exercises enforcement discretion under GFI #256 when: the drug is for a non-food-producing animal; there is no medically appropriate FDA-approved (animal or human) product that can be used as labeled or extra-label, and an approved product cannot be used as the API source; the compounded product is not a copy of an approved drug; it is prepared on a patient-specific prescription, or as office stock only for substances on FDA's List of Bulk Drug Substances for Compounding Office Stock Drugs for Nonfood-Producing Animals; adverse events are reported to FDA (compounders have no such duty, so the prescribing veterinarian carries it). Food-producing animals: bulk-substance compounding is limited to FDA's antidote list and sedatives/anesthetics for free-ranging wildlife; anything else is not defensible and has no residue data. Texas 573.44: a veterinarian may compound only for a specific animal or herd under a VCPR. Prefer 503A/503B pharmacies with veterinary accreditation; document why an approved product would not work.",
 reg="FDA GFI #256 (2022); FDA List of Bulk Drug Substances for Compounding Office Stock (nonfood) and Antidotes (food); 22 TAC 573.44.",rf="")

add(n="Veterinary Feed Directive (VFD) and Rx-only antimicrobials",a=["VFD","feed directive","GFI 263","medicated feed"],tier=2,cls="Prescribing reference",rx="rx",
 ind=["VFD","feed","medicated feed","antibiotic in feed","chlortetracycline","tylosin","GFI 263","water medication"],ev="A",
 evn="21 CFR 558.6 (VFD); FDA GFI #213 (2017) moved medically important antimicrobials in feed/water to VFD/Rx; GFI #263 (June 2023) moved the remaining OTC injectable, oral and intramammary medically important antimicrobials to Rx.",
 sp=_SP("VFD is a food-animal instrument; companion animals are covered by ordinary Rx rules.","Any medically important antimicrobial in feed needs a VFD; in water, an Rx; injectable products (penicillin, oxytetracycline, sulfas, lincomycin) are Rx since June 2023."),
 owner="Antibiotics in feed or water and the old feed-store injectable antibiotics (penicillin, oxytetracycline) now need a veterinarian's order. Feed stores cannot sell them over the counter. Dewormers, ionophores and coccidiostats like amprolium are not antibiotics and remain OTC.",
 dvm="A VFD is issued by a licensed veterinarian within a VCPR, in the course of professional practice, and only as the VFD drug's approval allows — no extra-label use of VFD feed (558.6(a)(3)). Required content (558.6(b)(3)): veterinarian name, address, phone; client name, address, phone; premises where animals are located; date of issue; expiration date (not beyond 6 months, or as the approval specifies); VFD drug(s); species and production class; approximate number of animals; indication; drug level (g/ton) and duration; withdrawal time, special instructions, cautions; number of reorders (refills) if the approval permits; the extralabel-use-prohibited statement; veterinarian signature. Records: veterinarian keeps the original, client and distributor keep copies, all for 2 years (558.6(a)(4)). Combination VFD drugs must be approved combinations. Water-soluble medically important antimicrobials require a prescription, not a VFD. After GFI #263 the OTC antimicrobial cards in this app that were feed-store products are now Rx — the tier badge follows the current status.",
 reg="21 CFR 558.6; FDA GFI #120, #209, #213, #263.",rf="")

add(n="Prescription portability and online pharmacies",a=["written prescription request","1-800 pharmacy","internet pharmacy",".pharmacy"],tier=2,cls="Prescribing reference",rx="rx",
 ind=["prescription","online pharmacy","fill elsewhere","Chewy","1-800-PetMeds","written prescription","verification","refill request"],ev="B",
 evn="AVMA policy: provide a prescription on request when a VCPR exists; most states codify this. Texas Chapter 573 does not spell out a portability rule — AVMA standard applies.",
 sp=_SP("Standard clinic practice.","Same; add withdrawal and species on the written prescription."),
 owner="If you want to buy a prescribed drug elsewhere, your veterinarian should give you a written prescription instead of selling it to you, as long as they have a relationship with your animal. Use pharmacies accredited by the National Association of Boards of Pharmacy (.pharmacy domain) — counterfeit heartworm and flea products are common online.",
 dvm="Provide a written prescription in lieu of dispensing when the client asks and a VCPR exists; a fee for the exam is reasonable, a fee for writing the prescription is prohibited in some states. Whether a drug is included in the plan is the veterinarian's decision, not the pharmacy's: verify pharmacy refill requests against the record and decline them when the VCPR has lapsed, the drug is inappropriate, or the patient is due for monitoring (e.g., NSAID bloodwork, phenobarbital levels). Do not authorize a refill by fax from a pharmacy you did not choose without confirming the request is genuine. Legitimacy: NABP Pharmacy Verified Websites program (.pharmacy); avoid sites that sell Rx drugs without a prescription. Human pharmacies: warn about xylitol-containing liquids, and pharmacist substitutions (e.g., generic thyroid products, insulin type) that change veterinary dosing — write 'dispense as written' where it matters.",
 reg="AVMA Prescriptions and Pharmacies FAQ; state practice acts vary; NABP .pharmacy program.",rf="")

# ───────── ALTERNATE THERAPY LAW (v0.1.5) ─────────
# Texas 22 TAC 573.16 (acupuncture, holistic medicine, homeopathy — combined March 2026; 573.17 repealed) and 573.14 (musculoskeletal manipulation).
# Verified against TBVME Chapter 573 PDF updated 2026-03-09 and LII text on 2026-09-20.
_ACU_REG=("Texas 22 TAC 573.16 (2026): only a licensed veterinarian may perform acupuncture (needling, moxibustion, thermal or electrical point stimulation); "
          "no delegation to non-veterinarians. Before treatment the veterinarian must inform the client of the conventional treatments available and their probable ability to cure the problem, "
          "and obtain a signed owner statement acknowledging acupuncture is an alternate therapy; the statement is a permanent part of the record. Other states differ — check the state practice act.")
_ACU_REFS=["Hayashi AM, Matera JM, Fonseca Pinto AC. J Am Vet Med Assoc. 2007;231(6):913-918. PMID 17867976",
           "Joaquim JG, Luna SP, Brondani JT, et al. J Am Vet Med Assoc. 2010;236(11):1225-1229. PMID 20513202"]
for _e in KB:
    if _e["n"]=="Acupuncture":
        _e["reg"]=_ACU_REG
        _e["refs"]=(_e.get("refs") or [])+_ACU_REFS
        _e["evn"]=_e["evn"]+" Canine IVDD: randomised trial (n=50) — electroacupuncture plus standard care shortened time to ambulation versus standard care alone; a controlled study (n=40) favoured electroacupuncture over late decompressive surgery in long-standing severe deficits."

add(n="Alternate therapies — Texas law (acupuncture, holistic, homeopathy, manipulation)",a=["573.16","573.14","alternate therapy consent","CAVM","complementary","holistic medicine law","homeopathy law"],tier=2,cls="Prescribing reference",rx="rx",
 ind=["acupuncture","holistic","homeopathy","chiropractic","manipulation","osteopathy","herbal","TCVM","consent form","alternate therapy","who can perform"],ev="A",
 evn="Regulatory text: 22 TAC 573.14 and 573.16 (TBVME Chapter 573, updated 2026-03-09). AVMA policy treats complementary and alternative veterinary medicine as veterinary medicine subject to the same standards of evidence and the practice act.",
 sp={k:{"s":"ok","n":"Reference card — applies to every species."} for k in ["dog","cat","rabbit","horse"]} | {k:{"s":"ok","n":"Reference card — applies to every species; herbal products in food animals still need a withdrawal (FARAD).","w":"n/a — reference card"} for k in FOOD},
 owner="In Texas, acupuncture, holistic medicine and homeopathy on animals may only be done by a licensed veterinarian, who must first tell you what conventional treatments exist and how likely they are to work, and have you sign a form acknowledging the therapy is 'alternate'. Chiropractic and other spinal manipulation may be done by a non-veterinarian only under a veterinarian's supervision, with the same signed form. Anyone offering these without a veterinarian is practising illegally.",
 dvm="573.16 (acupuncture, holistic medicine, homeopathy): veterinarian only, no delegation to staff or contractors; disclose conventional options and their probable ability to cure; signed owner acknowledgment kept permanently in the record. 'Holistic medicine' in the rule covers herbal medicine and homeopathy used alongside conventional care, so Tier 5 herbal/TCVM prescribing in Texas also carries the disclosure-and-acknowledgment duty. 573.14 (chiropractic and musculoskeletal manipulation): veterinarian with a VCPR, or a non-veterinarian employee/independent contractor under direct or general supervision; signed owner acknowledgment that MSM is an alternate therapy. Practical form: one acknowledgment covering the specific therapy, dated, listing the conventional options discussed. Evidence and liability: the alternate-therapy designation does not lower the standard of care — diagnosis, differential list and conventional-option discussion must be in the record. Other states: rules vary from veterinarian-only to layperson-permitted; the app's regulatory text is Texas-specific.",
 reg="22 TAC 573.14; 22 TAC 573.16 (combined acupuncture/holistic/homeopathy rule, 573.17 repealed); AVMA Guidelines for Complementary and Alternative Veterinary Medicine.",rf="")

# ───────── WITHDRAWAL COMPLETENESS RULE (v0.1.1) ─────────
# Every food-animal cell that is not status "no" must carry a withdrawal string.
# Cells that already have one are never overwritten. Rule, in order:
#   procedures / physical therapies (rx="proc")            -> "n/a — no drug administered"
#   topical irrigant / antiseptic (cls contains "irrigant"/"antiseptic") -> "None established (topical); FARAD if systemic exposure"
#   dose text says "per label"                              -> "Per label"
#   everything else (no label withdrawal recorded here)     -> "FARAD"
_TOPICAL=("irrigant","antiseptic")
for e in KB:
    for _s in FOOD:
        c=e["sp"].get(_s)
        if c is None or c.get("s")=="no" or c.get("w"): continue
        if e["rx"]=="proc": c["w"]="n/a — no drug administered"
        elif any(t in e["cls"].lower() for t in _TOPICAL): c["w"]="None established (topical); FARAD if systemic exposure"
        elif "per label" in c.get("d","").lower(): c["w"]="Per label"
        else: c["w"]="FARAD"

for i,e in enumerate(KB,1): e["i"]=i
