import json,gzip,base64,hashlib,datetime,kb
VERSION='v0.1.2'; BUILD=datetime.date.today().isoformat()
text=json.dumps(kb.KB,separators=(',',':'),ensure_ascii=False)
sha=hashlib.sha256(text.encode('utf-8')).hexdigest()
b64=base64.b64encode(gzip.compress(text.encode('utf-8'),9)).decode()
t=open('template.html').read()
t=t.replace('__KBDATA__',b64).replace('__KBSHA__',sha).replace('__VERSION__',VERSION).replace('__BUILD__',BUILD).replace('__KBCOUNT__',str(len(kb.KB)))
open('index.html','w').write(t)
print(VERSION,BUILD,len(kb.KB),'entries, sha',sha[:16],'html bytes',len(t))
