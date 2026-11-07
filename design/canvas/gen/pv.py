import re, pathlib, json, sys
S = pathlib.Path("/private/tmp/claude-501/-Users-alexdev-projects-personal-congrats/bd37b841-e6fb-40ab-b6f4-ae825644ffa1/scratchpad")
src = S / "artifact-files/b4a8099c-b52e-41d0-ad8e-182f529e1959/project"
out = S / "gen/pv"; out.mkdir(exist_ok=True)
H = json.load(open(S / "blobmap.json"))
files = sorted(src.glob("p-*.dc.html"))
names = []
for f in files:
    s = f.read_text()
    helmet = re.search(r"<helmet>([\s\S]*?)</helmet>", s).group(1)
    body = re.search(r"<x-dc>([\s\S]*?)</x-dc>", s).group(1)
    body = re.sub(r"<helmet>[\s\S]*?</helmet>", "", body)
    o = "<!doctype html><html><head><meta charset='utf-8'>%s</head><body>%s</body></html>" % (helmet, body)
    for k, v in H.items(): o = o.replace("/_blob/" + k, "../../img/" + v + ".jpg")
    n = f.name.replace(".dc.html", ".html"); (out / n).write_text(o); names.append(n)
json.dump(names, open(out / "list.json", "w"))
print(len(names))
