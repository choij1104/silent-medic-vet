#!/usr/bin/env python3
"""Builds ios/www, the App Store build of SILENT MEDIC VET, from the web build.

Source: the repository's index.html — the web app as published (v0.2.0). template.html in the
repository is older than index.html (the v0.2 template changes exist only as
tools/template_v020.diff), so the App Store build is derived from the built index.html, not from
template.html. Nothing in the repository root is modified.

The App Store build differs from the web build in four ways:

  1. Tier 3C (unapproved research peptides) is removed from the embedded knowledge base.
     Decision by Jae Hyek Choi, 2026-10-06: App Store Review Guidelines 1.4.1 / 1.4.3 risk;
     several are competition-banned in horses. The web build keeps them.
  2. No weight-based dose computation (Guideline 1.4.2). The weight field is removed and calc()
     returns nothing, so every dose is shown only as its reference source states it.
  3. No "Prototype" or "pilot" wording and no PWA install instructions.
  4. Text that pointed to the Tier 3C cards is reworded.

The knowledge base is re-encoded exactly as build.py does it (gzip + base64, SHA-256 of the JSON
text), so the app's integrity check passes. Every text replacement must match exactly once.
"""
import base64, gzip, hashlib, json, os, re, shutil, sys

IOS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT = os.path.dirname(IOS)
OUT = os.path.join(IOS, "www")

def die(msg):
    sys.exit(f"build-store: {msg}")

def sub1(pattern, repl, s, what, regex=False):
    if regex:
        s2, n = re.subn(pattern, lambda m: repl, s, flags=re.S)
    else:
        n = s.count(pattern)
        s2 = s.replace(pattern, repl)
    if n != 1:
        die(f"{what}: expected 1 match, found {n}")
    return s2

t = open(os.path.join(ROOT, "index.html"), encoding="utf-8").read()

# --- knowledge base -----------------------------------------------------------------
m = re.search(r'(<script id="kbData" type="application/octet-stream">)([^<]+)(</script>)', t)
if not m:
    die("kbData block not found")
text = gzip.decompress(base64.b64decode(m.group(2).strip())).decode("utf-8")
old_sha = hashlib.sha256(text.encode("utf-8")).hexdigest()
if f"KB_EXPECTED_SHA256='{old_sha}'" not in t:
    die("web build's own integrity hash does not match its data — rebuild the web app first")
data = json.loads(text)
kb, cond = data["kb"], data["cond"]
removed = [e["n"] for e in kb if e.get("sub") == "3C"]
if not removed:
    die("no Tier 3C entries found")
kb = [e for e in kb if e.get("sub") != "3C"]
for i, e in enumerate(kb, 1):
    e["i"] = i
names = [e["n"] for e in kb]
ids = {c["id"] for c in cond}
for e in kb:
    for cid in e.get("cond", []):
        assert cid in ids, (e["n"], cid)
for c in cond:
    for h in c.get("hum", []) + c.get("rx", []):
        assert any(n.lower().startswith(h.lower()) for n in names), (c["id"], h, "links to a removed entry")
new_text = json.dumps({"kb": kb, "cond": cond}, separators=(",", ":"), ensure_ascii=False)
new_sha = hashlib.sha256(new_text.encode("utf-8")).hexdigest()
new_b64 = base64.b64encode(gzip.compress(new_text.encode("utf-8"), 9)).decode()
t = t[:m.start(2)] + new_b64 + t[m.end(2):]
t = sub1(f"KB_EXPECTED_SHA256='{old_sha}'", f"KB_EXPECTED_SHA256='{new_sha}'", t, "integrity hash")
n_old = len(data["kb"])
t = sub1(f"knowledge base {n_old} entries", f"knowledge base {len(kb)} entries", t, "entry count")

# --- App Store differences ----------------------------------------------------------
t = sub1(r'<label>Weight <input type="number" id="weight"[^>]*> kg</label>',
         '<input type="hidden" id="weight">', t, "weight field", regex=True)
t = sub1("function calc(d,w){", "function calc(d,w){return '';", t, "calc()")
t = sub1(r'\s*<button type="button" id="installBtn".*?</button>', "", t, "install button", regex=True)
t = sub1(r"\s*<p>Installable app: add to home screen.*?</p>", "", t, "install note", regex=True)
t = sub1(r"\s*<p>Unapproved peptides \(Tier 3C\).*?</p>", "", t, "Tier 3C footer", regex=True)
t = sub1("Prototype — not a substitute", "Not a substitute", t, "footer")
t = sub1("CBD, and all Tier 3C peptides are prohibited or controlled",
         "CBD, and unapproved research peptides are prohibited or controlled", t, "horse note")
t = sub1(r"BPC-157 / TB-500 have no controlled data in any animal and are competition-banned[^']*",
         "Unapproved research peptides have no controlled data in any animal and are competition-banned.",
         t, "peptide note", regex=True)
t = sub1("+' · pilot: eye';", ";", t, "conditions pilot label")
t = sub1('<meta charset="utf-8">', '<meta charset="utf-8">\n<meta name="smv-build" content="store">',
         t, "charset meta")

# --- checks -------------------------------------------------------------------------
for bad in ("Prototype", "Tier 3C", "BPC-157", "TB-500", 'id="installBtn"', 'type="number" id="weight"'):
    if bad in t:
        die(f"'{bad}' still present outside the knowledge base")
if re.search(r'(src|href)="https?://', t):
    die("external resource reference in index.html")
check = json.loads(gzip.decompress(base64.b64decode(new_b64)))
assert hashlib.sha256(json.dumps(check, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest() == new_sha
if any(e.get("sub") == "3C" for e in check["kb"]):
    die("Tier 3C entry in embedded knowledge base")

shutil.rmtree(OUT, ignore_errors=True)
os.makedirs(OUT)
open(os.path.join(OUT, "index.html"), "w", encoding="utf-8").write(t)
for f in ("icon-192.png", "icon-512.png", "manifest.webmanifest"):
    shutil.copy(os.path.join(ROOT, f), os.path.join(OUT, f))
print(f"build-store: {len(kb)} entries (removed {len(removed)} Tier 3C: {', '.join(removed)}) · "
      f"{len(cond)} conditions · sha {new_sha[:16]} · {len(t)} bytes → {OUT}")
