import json,gzip,base64,hashlib,datetime,kb
VERSION='v0.1.8'; BUILD=datetime.date.today().isoformat()
text=json.dumps(kb.KB,separators=(',',':'),ensure_ascii=False)
sha=hashlib.sha256(text.encode('utf-8')).hexdigest()
b64=base64.b64encode(gzip.compress(text.encode('utf-8'),9)).decode()
t=open('template.html').read()
t=t.replace('__KBDATA__',b64).replace('__KBSHA__',sha).replace('__VERSION__',VERSION).replace('__BUILD__',BUILD).replace('__KBCOUNT__',str(len(kb.KB)))
open('index.html','w').write(t)
sw=open('sw.js').read()
import re as _re
sw=_re.sub(r"const CACHE = '[^']*';","const CACHE = 'silent-medic-vet-"+VERSION+"';",sw)
open('sw.js','w').write(sw)
print(VERSION,BUILD,len(kb.KB),'entries, sha',sha[:16],'html bytes',len(t))
