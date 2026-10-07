window.DEMO_SCRIPT=async({sleep,tap,scroll})=>{
  await sleep(2500);
  await tap('#bootBtn',{after:1800});                                   // open after integrity check
  await tap({sel:'.chip',text:/^Dog$/},{after:1500});                   // species
  await tap({sel:'.tier',text:/^7 · Human meds at home/},{after:1800}); // human medicines at home
  await tap({sel:'.head',text:/^Ibuprofen/},{after:2200});              // ok / caution / do not use
  await scroll(500,2200);
  await scroll(-500,1200);
  await tap('#tabCond',{after:2000});                                   // conditions
  await scroll(400,1800);
  await tap('#tabDs',{after:2200});                                     // decision support
  await scroll(400,1800);
  await tap('#modeDvm',{after:1800});                                   // veterinarian mode
  await tap('#tabRef',{after:1500});
  await tap({sel:'.head',text:/^Carprofen/},{after:2200});
  await scroll(500,2200);
  await tap({sel:'.chip',text:/^Horse$/},{after:2000});
  await scroll(400,1800);
};
