import sys;sys.path.insert(0,sys.argv[1])
from load import *
D=load()
for d in sys.argv[2:]:
    rows=sorted(D[d],key=lambda r:-(r['Current traffic#']+r['Previous traffic#']))
    for r in rows:
        u=re.sub(r'https?://(www\.)?'+re.escape(d),'',r['URL'])
        print(f"{u[:90]:90} {r['Status'][:1]:1} {int(r['Previous traffic#']):5}>{int(r['Current traffic#']):5} ${int(r['Current traffic value#']):5} ai{int(r['AI responses: All platforms#'])} | {(r['Current top keyword'] or r['Previous top keyword'])[:45]} [{(r['Current top keyword: Country'] or r['Previous top keyword: Country'])[:3]}] v{int(r['Current top keyword: Volume#'] or r['Previous top keyword: Volume#'])} p{int(r['Current top keyword: Position#'] or r['Previous top keyword: Position#'])}")
