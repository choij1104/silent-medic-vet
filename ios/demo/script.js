window.DEMO_SCRIPT=async({sleep,tap,type,scroll})=>{
  await sleep(2500);                                                     // opening screen fades after the integrity check
  await tap({sel:'.chip',text:/^Dog$/},{after:1200});                    // which animal
  await type('#q','ibuprofen',1200);                                    // human medicine at home
  await tap({sel:'.head',text:/^Ibuprofen/},{after:2000});              // ok / caution / do not use
  await scroll(400,1800);
  await tap('.smvTab[data-tab="cond"]',{after:1800});                    // conditions (bottom bar)
  await tap({sel:'.head',text:/^Glaucoma/},{after:1800});
  await tap('.smvTab[data-tab="ds"]',{after:1500});                      // triage plan builder
  await tap({sel:'#dsSyn .opt',text:/^Eye/},{after:700});
  await tap({sel:'#dsOnset .opt',text:/^Today$/},{after:700});
  await tap('#dsGo',{after:2000});
  await scroll(500,2000);
  await tap('.smvTab[data-tab="pat"]',{after:1500});                     // patients (on-device profiles)
  await tap('#patNew',{after:900});
  await type('#pfName','Bella',600);
  await type('#pfN','Right eye tearing since Monday.',600);
  await tap('#patForm button[type=submit]',{after:1500});
  await tap({sel:'.pat button',text:/^Recheck reminder$/},{after:1200}); // local reminder
  await tap({sel:'.quick button',text:/^Tomorrow 8 AM$/},{after:700});
  await type('.rcWhy','Right eye',500);
  await tap({sel:'.pat button',text:/^Set reminder$/},{after:2200});    // iOS asks for notification permission
  await tap({sel:'.pat button',text:/^Add observation$/},{after:900});
  await type('.obTxt','Squinting less this evening.',500);
  await tap({sel:'.pat button',text:/^Add to log$/},{after:1800});
  await scroll(500,1800);
  await tap('#modeDvm',{after:1200});                                    // veterinarian mode
  await tap('.smvTab[data-tab="ref"]',{after:1200});
  await tap({sel:'.head',text:/^Carprofen/},{after:2200});
  await scroll(400,1800);
};
