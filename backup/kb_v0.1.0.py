# SILENT MEDIC VET — knowledge base seed v0.1.0
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

for i,e in enumerate(KB,1): e["i"]=i
