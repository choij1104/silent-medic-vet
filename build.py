import json,gzip,base64,hashlib,datetime,kb,cond,kb_human
# Tier 7 (human medicines at home) is appended here so kb.py stays unchanged; ids of tiers 1-6 are preserved.
kb_human.extend(kb.add,kb.FOOD)
for _e in kb.KB:
    for _s in kb.FOOD:
        _c=_e['sp'].get(_s)
        assert _c is None or _c.get('s')=='no' or _c.get('w'), (_e['n'],_s)
for _i,_e in enumerate(kb.KB,1): _e['i']=_i
VERSION='v0.2.0'; BUILD=datetime.date.today().isoformat()
ids={c['id'] for c in cond.COND}
names=[e['n'] for e in kb.KB]
for e in kb.KB:
    for cid in e.get('cond',[]): assert cid in ids, (e['n'],cid)
for c in cond.COND:
    for s in c.get('see',[]): assert s in ids,(c['id'],s)
    for h in c.get('hum',[])+c.get('rx',[]): assert any(n.lower().startswith(h.lower()) for n in names),(c['id'],h)
text=json.dumps({'kb':kb.KB,'cond':cond.COND},separators=(',',':'),ensure_ascii=False)
sha=hashlib.sha256(text.encode('utf-8')).hexdigest()
b64=base64.b64encode(gzip.compress(text.encode('utf-8'),9)).decode()
t=open('template.html').read()
t=t.replace('__KBDATA__',b64).replace('__KBSHA__',sha).replace('__VERSION__',VERSION).replace('__BUILD__',BUILD).replace('__KBCOUNT__',str(len(kb.KB))).replace('__CONDCOUNT__',str(len(cond.COND)))
open('index.html','w').write(t)
sw=open('sw.js').read()
import re as _re
sw=_re.sub(r"const CACHE = '[^']*';","const CACHE = 'silent-medic-vet-"+VERSION+"';",sw)
open('sw.js','w').write(sw)
print(VERSION,BUILD,len(kb.KB),'entries,',len(cond.COND),'conditions, sha',sha[:16],'html bytes',len(t))
