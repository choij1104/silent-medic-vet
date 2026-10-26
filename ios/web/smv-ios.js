/* Silent Medic Vet for iPhone: native layer of the App Store build.
   Bottom tab bar, the Patients tab (on-device animal profiles, observation log, recheck reminders),
   Spotlight indexing of the reference, Siri / Shortcuts / Spotlight / reminder routes, and haptics.
   Talks only to the app's own native plugins (FieldRoute, KnowledgeIndex, PatientChart, Recheck,
   FieldHaptics). No network. Nothing here computes a dose; a weight in a profile is a note. */
(function(){
'use strict';
const C=window.Capacitor;
const NATIVE=!!(C&&C.isNativePlatform&&C.isNativePlatform()&&C.registerPlugin);
function plug(n){if(!NATIVE)return null;try{return C.registerPlugin(n)}catch(e){return null}}
const Route=plug('FieldRoute'),Index=plug('KnowledgeIndex'),Chart=plug('PatientChart'),Recheck=plug('Recheck'),Hap=plug('FieldHaptics');
const H={
  sel(){if(Hap)Hap.selection().catch(()=>{})},
  imp(style){if(Hap)Hap.impact({style:style||'medium'}).catch(()=>{})},
  note(type){if(Hap)Hap.notify({type:type||'success'}).catch(()=>{})}
};
const MARK='<svg class="smvMark" viewBox="0 0 64 64" aria-hidden="true"><rect width="64" height="64" rx="16" fill="#f4efe2"/><g fill="#b5622a"><ellipse cx="19" cy="25" rx="5" ry="6.5"/><ellipse cx="28" cy="17" rx="5" ry="6.5"/><ellipse cx="38" cy="17" rx="5" ry="6.5"/><ellipse cx="47" cy="25" rx="5" ry="6.5"/></g><path d="M33 29c-7 0-14 9-14 15 0 5 4 7 8 6 3-.7 4-1.5 6-1.5s3 .8 6 1.5c4 1 8-1 8-6 0-6-7-15-14-15z" fill="#24563f"/><path d="M33 35v10M28 40h10" stroke="#f4efe2" stroke-width="3" stroke-linecap="round"/></svg>';
const ICON={
  ref:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M4 5.5A2.5 2.5 0 0 1 6.5 3H20v15H6.5A2.5 2.5 0 0 0 4 20.5z"/><path d="M4 20.5A2.5 2.5 0 0 0 6.5 23H20v-5"/><path d="M12 7v6M9 10h6"/></svg>',
  cond:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M2 12h4l2.5-6 4 12 2.5-6H22"/></svg>',
  ds:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M9 3h6v4h-6z"/><path d="M7 5H5v16h14V5h-2"/><path d="M9 12l2 2 4-4M9 18h6"/></svg>',
  pat:'<svg viewBox="0 0 24 24" fill="currentColor"><ellipse cx="6" cy="9.5" rx="2" ry="2.6"/><ellipse cx="9.8" cy="5.8" rx="2" ry="2.6"/><ellipse cx="14.2" cy="5.8" rx="2" ry="2.6"/><ellipse cx="18" cy="9.5" rx="2" ry="2.6"/><path d="M12 11c-3 0-6 3.8-6 6.4 0 2.2 1.8 3 3.5 2.6 1.2-.3 1.6-.6 2.5-.6s1.3.3 2.5.6c1.7.4 3.5-.4 3.5-2.6 0-2.6-3-6.4-6-6.4z"/></svg>'
};
const TABS=[['ref','Reference'],['cond','Conditions'],['ds','Triage'],['pat','Patients']];
const LS_P='smv.patients.v1',LS_A='smv.activePatient';
const ui={patients:[],active:null,editing:null,open:null,sheet:null,msg:{},current:'ref',ready:false,queued:[]};
function lsGet(k,d){try{const v=localStorage.getItem(k);return v==null?d:JSON.parse(v)}catch(e){return d}}
function lsSet(k,v){try{localStorage.setItem(k,JSON.stringify(v))}catch(e){}}
const uid=()=>Date.now().toString(36)+Math.random().toString(36).slice(2,8);
const spL=k=>(SPECIES[k]||{l:k}).l;
const fmtDate=ms=>new Date(ms).toLocaleDateString(undefined,{month:'short',day:'numeric',year:'numeric'});
const fmtWhen=ms=>new Date(ms).toLocaleString(undefined,{weekday:'short',month:'short',day:'numeric',hour:'numeric',minute:'2-digit'});
function localInput(d){const p=n=>String(n).padStart(2,'0');return d.getFullYear()+'-'+p(d.getMonth()+1)+'-'+p(d.getDate())+'T'+p(d.getHours())+':'+p(d.getMinutes())}

/* ---------- patient storage: native file on iPhone, browser storage elsewhere ---------- */
const store={
  async list(){if(Chart){const r=await Chart.list();return r.patients||[]}return lsGet(LS_P,[])},
  async save(p){if(Chart){const r=await Chart.save({patient:p});return r.patients||[]}const a=lsGet(LS_P,[]);const i=a.findIndex(x=>x.id===p.id);if(i>=0)a[i]=p;else a.push(p);lsSet(LS_P,a);return a},
  async remove(id){if(Chart){const r=await Chart.remove({id});return r.patients||[]}const a=lsGet(LS_P,[]).filter(x=>x.id!==id);lsSet(LS_P,a);return a}
};

/* ---------- chrome: header, rail heading, bottom bar, patients panel ---------- */
function chrome(){
  const bh=document.querySelector('#boot h1');
  if(bh){bh.insertAdjacentHTML('beforebegin',MARK);bh.firstChild.textContent='Silent Medic Vet'}
  const br=document.querySelector('header .brand');
  if(br)br.innerHTML=MARK+'<span class="smvTitle"><b>Silent Medic Vet</b><span id="smvCtx"></span></span>';
  const rail=document.querySelector('.rail');
  if(rail){rail.insertAdjacentHTML('afterbegin','<div class="smvRailHead"><h2>Which animal?</h2><span>13 species</span></div>');
    rail.insertAdjacentHTML('beforeend','<div class="activeStrip" id="activeStrip" hidden></div>')}
  const ds=$('dsPanel');
  ds.insertAdjacentHTML('afterend','<div class="panel pad" id="patPanel" role="tabpanel" aria-label="Patients"></div>');
  const bar=document.createElement('nav');bar.className='smvBar';bar.setAttribute('role','tablist');bar.setAttribute('aria-label','Sections');
  bar.innerHTML=TABS.map(([k,l])=>'<button type="button" class="smvTab" role="tab" data-tab="'+k+'" aria-selected="'+(k==='ref')+'">'+ICON[k]+'<span>'+l+'</span></button>').join('');
  document.body.appendChild(bar);
  bar.addEventListener('click',e=>{const b=e.target.closest('.smvTab');if(!b)return;H.sel();tab(b.dataset.tab);window.scrollTo(0,0)});
}

/* ---------- wrap the web app's own navigation so every path keeps the bar in sync ---------- */
const baseTab=tab,baseBuildRail=buildRail,baseSetMode=setMode,baseRenderPlan=renderPlan;
tab=function(t){
  const pat=t==='pat';
  if(!pat)baseTab(t);
  else for(const k of ['ref','cond','ds']){$(k+'Panel').classList.remove('active');$('tab'+k[0].toUpperCase()+k.slice(1)).setAttribute('aria-selected','false')}
  const pp=$('patPanel');if(pp)pp.classList.toggle('active',pat);
  ui.current=t;
  document.body.classList.toggle('onPatients',pat);
  document.querySelectorAll('.smvTab').forEach(b=>b.setAttribute('aria-selected',b.dataset.tab===t));
  if(pat)renderPatients();
};
buildRail=function(){
  baseBuildRail();
  if(ui.active){const p=ui.patients.find(x=>x.id===ui.active);if(!p||p.species!==state.species)setActive(null,true)}
  ctx();
};
setMode=function(m){baseSetMode(m);ctx()};
renderPlan=function(){baseRenderPlan();ctx()};
function ctx(){
  const el=$('smvCtx');if(!el)return;
  const p=ui.active&&ui.patients.find(x=>x.id===ui.active);
  el.innerHTML=(p?'<span class="pt">'+esc(p.name)+'</span> · ':'')+esc(spL(state.species))+' · '+(state.mode==='dvm'?'Veterinarian view':'Owner view');
  const s=$('activeStrip');
  if(s){if(p){s.hidden=false;s.innerHTML='Charting <b>'+esc(p.name)+'</b> · '+esc(spL(p.species))+'<button type="button" id="activeClear" aria-label="Stop charting this patient">Clear</button>';$('activeClear').onclick=()=>{H.sel();setActive(null)}}else s.hidden=true}
}
function setActive(id,quiet){
  ui.active=id;lsSet(LS_A,id);
  const p=id&&ui.patients.find(x=>x.id===id);
  if(p&&SPECIES[p.species]&&state.species!==p.species){
    state.species=p.species;
    if(VIEWS[state.view].sp&&!VIEWS[state.view].sp.includes(p.species))setView('all');
    else{baseBuildRail();render();renderCond();baseRenderPlan()}
  }
  if(!quiet)ctx();
  if(ui.current==='pat'&&!quiet)renderPatients();
}

/* ---------- Patients tab ---------- */
function speciesOptions(sel){return Object.entries(SPECIES).map(([k,v])=>'<option value="'+k+'"'+(k===sel?' selected':'')+'>'+esc(v.l)+'</option>').join('')}
function formHTML(p){
  const e=p||{name:'',species:state.species,weightKg:'',weightDate:'',notes:''};
  return '<form class="patForm" id="patForm" autocomplete="off"><h3>'+(p?'Edit '+esc(p.name):'New patient')+'</h3>'
   +'<label class="fld">Name or tag<input id="pfName" maxlength="60" required value="'+esc(e.name)+'" placeholder="e.g. Bella, Ewe 214, Barn cat"></label>'
   +'<label class="fld">Species<select id="pfSp">'+speciesOptions(e.species)+'</select></label>'
   +'<div class="fldRow"><label class="fld">Weight noted (kg)<input id="pfW" type="number" inputmode="decimal" min="0" step="0.1" value="'+esc(e.weightKg??'')+'"></label>'
   +'<label class="fld">Weighed on<input id="pfWd" type="date" value="'+esc(e.weightDate||'')+'"></label></div>'
   +'<p class="fld"><small>Kept as a record for you and your veterinarian. Silent Medic Vet never calculates a dose from it.</small></p>'
   +'<label class="fld">Notes<textarea id="pfN" maxlength="2000" placeholder="Age, history, vaccinations, your veterinarian\'s instructions">'+esc(e.notes||'')+'</textarea></label>'
   +'<div class="btnRow"><button type="submit" class="smvBtn">Save</button><button type="button" class="smvBtn ghost" id="pfCancel">Cancel</button></div></form>';
}
function recheckLine(p){
  if(!p.recheck)return '';
  const past=p.recheck.at<Date.now();
  return '<div class="rc'+(past?' past':'')+'"><strong>'+(past?'Recheck was due ':'Recheck ')+esc(fmtWhen(p.recheck.at))+'</strong>'+(p.recheck.reason?' — '+esc(p.recheck.reason):'')
    +(p.recheck.alert===false?'<br><small>Saved in the profile; no iPhone alert is set.</small>':'')+'</div>';
}
function sheetHTML(p,kind){
  if(kind==='recheck'){
    const d=new Date(Date.now()+24*3600e3);d.setSeconds(0,0);
    return '<div class="sheet"><div class="quick" role="group" aria-label="Quick times">'
      +'<button type="button" data-q="4h">In 4 hours</button><button type="button" data-q="tm8">Tomorrow 8 AM</button><button type="button" data-q="3d">In 3 days</button><button type="button" data-q="7d">In 1 week</button><button type="button" data-q="14d">In 2 weeks</button></div>'
      +'<label class="fld">When<input type="datetime-local" class="rcAt" value="'+localInput(d)+'"></label>'
      +'<label class="fld">What to recheck<input class="rcWhy" maxlength="120" placeholder="e.g. eye, wound dressing, appetite" value="'+esc((p.recheck&&p.recheck.reason)||'')+'"></label>'
      +'<div class="btnRow"><button type="button" class="smvBtn copper" data-act="rcSet">Set reminder</button>'+(p.recheck?'<button type="button" class="smvBtn warn" data-act="rcOff">Remove reminder</button>':'')+'<button type="button" class="smvBtn ghost" data-act="close">Close</button></div></div>';
  }
  return '<div class="sheet"><label class="fld">Observation<textarea class="obTxt" maxlength="500" placeholder="e.g. Ate half her breakfast. Right eye less squinty."></textarea></label>'
    +'<div class="btnRow"><button type="button" class="smvBtn" data-act="obAdd">Add to log</button><button type="button" class="smvBtn ghost" data-act="close">Close</button></div></div>';
}
function patHTML(p){
  const open=ui.open===p.id;const act=ui.active===p.id;
  const log=(p.log||[]).slice().sort((a,b)=>b.t-a.t);
  let h='<article class="pat'+(act?' active':'')+'" data-pid="'+esc(p.id)+'"><div class="ph"><div class="av" aria-hidden="true">'+esc((p.name||'?').trim().slice(0,1).toUpperCase())+'</div>'
    +'<div style="flex:1;min-width:0"><div class="pn">'+esc(p.name)+'</div><div class="ps">'+esc(spL(p.species))+(p.weightKg?' · '+esc(p.weightKg)+' kg noted'+(p.weightDate?' on '+esc(fmtDate(p.weightDate+'T12:00')):''):'')+'</div></div>'
    +(act?'<span class="tag">Active</span>':'')+'</div><div class="pb">';
  if(p.notes)h+='<p style="margin:0 0 6px;white-space:pre-wrap">'+esc(p.notes)+'</p>';
  h+=recheckLine(p);
  h+='<div class="btnRow">'+(act?'':'<button type="button" class="smvBtn" data-act="use">Chart this animal</button>')
    +'<button type="button" class="smvBtn ghost" data-act="recheck">Recheck reminder</button><button type="button" class="smvBtn ghost" data-act="obs">Add observation</button></div>';
  if(ui.sheet&&ui.sheet.id===p.id)h+=sheetHTML(p,ui.sheet.kind);
  if(ui.msg[p.id])h+='<p class="smvMsg'+(ui.msg[p.id].err?' err':'')+'" role="status">'+esc(ui.msg[p.id].t)+'</p>';
  if(log.length)h+='<ul class="log">'+log.slice(0,open?50:3).map(x=>'<li><time>'+esc(fmtWhen(x.t))+'</time>'+esc(x.text)+'</li>').join('')+'</ul>'+(log.length>3&&!open?'<button type="button" class="smvBtn ghost" data-act="more" style="margin-top:8px;width:100%">Show all '+log.length+' observations</button>':'');
  h+='<div class="btnRow" style="margin-top:10px"><button type="button" class="smvBtn ghost" data-act="edit">Edit</button><button type="button" class="smvBtn warn" data-act="del">Delete</button></div>';
  return h+'</div></article>';
}
function renderPatients(){
  const P=$('patPanel');if(!P)return;
  let h='<div class="patTop"><h2>Patients</h2>'+(ui.editing===null?'<button type="button" class="smvBtn" id="patNew">New patient</button>':'')+'</div>'
   +'<p class="patIntro">A profile for each animal you look after: species, a weight you noted, notes, an observation log and recheck reminders. Profiles stay on this iPhone.</p>';
  if(ui.editing!==null)h+=formHTML(ui.editing==='new'?null:ui.patients.find(x=>x.id===ui.editing));
  if(!ui.patients.length&&ui.editing===null)h+='<div class="smvEmpty">'+MARK+'<p>No patients yet. Add one to keep its species ready, log what you see, and get a reminder when it is time to recheck.</p></div>';
  const list=ui.patients.slice().sort((a,b)=>(b.id===ui.active)-(a.id===ui.active)||(a.name||'').localeCompare(b.name||''));
  h+=list.map(patHTML).join('');
  h+='<div class="native"><h3>On this iPhone</h3><ul>'
   +'<li>Ask Siri: “Look up a drug for my dog in Silent Medic Vet”, “Build a triage plan for my horse in Silent Medic Vet”, or “Open my patients in Silent Medic Vet”.</li>'
   +'<li>Search the Home Screen for a drug or condition, such as carprofen or glaucoma, to open its card directly.</li>'
   +'<li>Recheck reminders are local notifications; tap one to come back to that patient.</li></ul></div>';
  P.innerHTML=h;
  const nb=$('patNew');if(nb)nb.onclick=()=>{H.sel();ui.editing='new';renderPatients();const n=$('pfName');if(n)n.focus()};
  const f=$('patForm');if(f){f.onsubmit=onSave;$('pfCancel').onclick=()=>{ui.editing=null;renderPatients()}}
  P.querySelectorAll('.pat').forEach(card=>{
    const id=card.dataset.pid;
    card.querySelectorAll('[data-act]').forEach(b=>b.onclick=()=>act(id,b.dataset.act,card));
    card.querySelectorAll('.quick [data-q]').forEach(b=>b.onclick=()=>{H.sel();const inp=card.querySelector('.rcAt');inp.value=localInput(quick(b.dataset.q))});
  });
}
function quick(q){const d=new Date();d.setSeconds(0,0);
  if(q==='4h')d.setTime(d.getTime()+4*3600e3);
  else if(q==='tm8'){d.setDate(d.getDate()+1);d.setHours(8,0,0,0)}
  else d.setDate(d.getDate()+parseInt(q,10));
  return d}
async function onSave(ev){
  ev.preventDefault();
  const name=$('pfName').value.trim();if(!name){$('pfName').focus();return}
  const w=parseFloat($('pfW').value);
  const old=ui.editing!=='new'&&ui.patients.find(x=>x.id===ui.editing);
  const now=Date.now();
  const p=Object.assign({},old||{id:uid(),created:now,log:[],recheck:null},{name:name.slice(0,60),species:SPECIES[$('pfSp').value]?$('pfSp').value:'dog',
    weightKg:isFinite(w)&&w>0?Math.round(w*100)/100:null,weightDate:$('pfWd').value||'',notes:$('pfN').value.slice(0,2000),updated:now});
  try{ui.patients=await store.save(p);ui.editing=null;H.note('success');if(!old&&!ui.active)setActive(p.id,true);ctx();renderPatients()}
  catch(e){H.note('error');alert('Could not save: '+(e&&e.message||e))}
}
async function act(id,a,card){
  const p=ui.patients.find(x=>x.id===id);if(!p)return;
  delete ui.msg[id];
  if(a==='use'){H.sel();setActive(id);tab('ref');window.scrollTo(0,0);return}
  if(a==='edit'){ui.editing=id;ui.sheet=null;renderPatients();window.scrollTo(0,0);return}
  if(a==='recheck'||a==='obs'){H.sel();ui.sheet={id,kind:a==='obs'?'obs':'recheck'};renderPatients();return}
  if(a==='close'){ui.sheet=null;renderPatients();return}
  if(a==='more'){ui.open=id;renderPatients();return}
  if(a==='del'){
    if(!confirm('Delete '+p.name+' and its observation log from this iPhone?'))return;
    if(p.recheck&&Recheck)try{await Recheck.cancel({id})}catch(e){}
    try{ui.patients=await store.remove(id);H.note('warning');if(ui.active===id)setActive(null,true);ctx();renderPatients()}catch(e){alert('Could not delete: '+(e&&e.message||e))}
    return}
  if(a==='obAdd'){
    const t=card.querySelector('.obTxt').value.trim();if(!t)return;
    const q=Object.assign({},p,{log:(p.log||[]).concat([{t:Date.now(),text:t.slice(0,500)}]).slice(-200),updated:Date.now()});
    try{ui.patients=await store.save(q);ui.sheet=null;H.note('success');renderPatients()}catch(e){ui.msg[id]={t:'Could not save: '+(e&&e.message||e),err:1};renderPatients()}
    return}
  if(a==='rcOff'){
    if(Recheck)try{await Recheck.cancel({id})}catch(e){}
    ui.patients=await store.save(Object.assign({},p,{recheck:null,updated:Date.now()}));ui.sheet=null;ui.msg[id]={t:'Reminder removed.'};renderPatients();return}
  if(a==='rcSet'){
    const at=new Date(card.querySelector('.rcAt').value).getTime();
    const why=card.querySelector('.rcWhy').value.trim().slice(0,120);
    if(!isFinite(at)||at<Date.now()+60e3){ui.msg[id]={t:'Pick a time at least a minute from now.',err:1};H.note('error');renderPatients();return}
    let alertSet=false,note='';
    if(Recheck){
      try{
        let s=(await Recheck.permission()).status;
        if(s==='prompt')s=(await Recheck.request()).granted?'granted':'denied';
        if(s==='granted'){
          await Recheck.schedule({id,at,title:'Recheck: '+p.name+' ('+spL(p.species)+')',body:why||'Time to recheck '+p.name+'.',route:'patient:'+id});
          alertSet=true;
        }else note=' Notifications are off for Silent Medic Vet; turn them on in Settings > Notifications to get an alert.';
      }catch(e){note=' The alert could not be set: '+(e&&e.message||e)}
    }else note=' Alerts need the iPhone app.';
    ui.patients=await store.save(Object.assign({},p,{recheck:{at,reason:why,alert:alertSet},updated:Date.now()}));
    ui.sheet=null;ui.msg[id]={t:(alertSet?'Reminder set for '+fmtWhen(at)+'.':'Recheck saved for '+fmtWhen(at)+'.')+note,err:!alertSet&&!!Recheck};
    H.note(alertSet?'success':'warning');renderPatients();return}
}

/* ---------- Spotlight ---------- */
async function indexSpotlight(){
  if(!Index||!state.kb.length)return;
  const items=state.kb.map(e=>({id:'kb:'+e.i,title:e.n,detail:(TIERS[e.tier]||'')+(e.cls?' · '+e.cls:''),keywords:[...(e.a||[]),...(e.ind||[])].slice(0,20)}))
    .concat(state.cond.map(c=>({id:'cond:'+c.id,title:c.n,detail:c.sys+' · '+c.sp.map(spL).join(', '),keywords:[...(c.a||[]),...(c.signs||[])].slice(0,20)})));
  try{await Index.index({stamp:KB_EXPECTED_SHA256+':'+items.length+':1',items})}catch(e){}
}

/* ---------- routes from Spotlight, Siri / Shortcuts and reminders ---------- */
function dismissBoot(){const b=$('boot');if(b)b.remove()}
function go(route){
  if(!route)return;
  if(!ui.ready){ui.queued.push(route);return}
  dismissBoot();
  const parts=route.split(':');const k=parts[0];
  if(k==='kb'){openKB(parts[1]);ui.current='ref';document.querySelectorAll('.smvTab').forEach(b=>b.setAttribute('aria-selected',b.dataset.tab==='ref'))}
  else if(k==='cond'){openCond(parts.slice(1).join(':'))}
  else if(k==='lookup'||k==='plan'){
    const sp=parts[1];
    if(SPECIES[sp]){state.species=sp;if(VIEWS[state.view].sp&&!VIEWS[state.view].sp.includes(sp))setView('all');else{buildRail();render();renderCond();renderPlan()}}
    if(k==='lookup'){const term=parts.slice(2).join(':').trim();tab('ref');$('q').value=term;state.q=term.toLowerCase();render()}
    else tab('ds');
    window.scrollTo(0,0)}
  else if(k==='patients'){tab('pat');window.scrollTo(0,0)}
  else if(k==='patient'){const id=parts.slice(1).join(':');ui.open=id;tab('pat');const el=document.querySelector('.pat[data-pid="'+CSS.escape(id)+'"]');if(el)el.scrollIntoView({block:'start'})}
}
async function pull(){if(!Route)return;try{const r=await Route.take();if(r&&r.route)go(r.route)}catch(e){}}

/* ---------- haptics on the web app's own controls ---------- */
document.addEventListener('click',e=>{
  const t=e.target.closest('button');if(!t)return;
  if(t.id==='dsGo'){H.imp('medium');return}
  if(t.matches('.chip,.opt,.view,.tier,.modeSwitch button'))H.sel();
},true);

/* ---------- start ---------- */
chrome();
async function whenReady(){
  for(let i=0;i<300;i++){const b=$('bootBtn');if(state.kb.length&&b&&b.style.display==='inline-block')break;await new Promise(r=>setTimeout(r,50))}
  try{ui.patients=await store.list()}catch(e){ui.patients=[]}
  const a=lsGet(LS_A,null);if(a&&ui.patients.some(p=>p.id===a))setActive(a,true);
  ctx();
  ui.ready=true;
  // The integrity result stays on screen if it failed; otherwise the opening screen fades out by itself.
  if(state.kbOk){const b=$('boot');if(b){b.classList.add('smvFade');setTimeout(dismissBoot,320)}}
  const q=ui.queued.splice(0);q.forEach(go);
  await pull();
  if(Route){try{Route.addListener('route',()=>pull())}catch(e){}}
  document.addEventListener('visibilitychange',()=>{if(document.visibilityState==='visible')pull()});
  indexSpotlight();
}
whenReady();
window.SMV_IOS={go,ready:()=>ui.ready,native:NATIVE};
})();
