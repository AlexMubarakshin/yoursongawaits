import sys;sys.path.insert(0,sys.argv[1])
from load import *
from urllib.parse import urlparse
from collections import defaultdict
D=load()
for d in sys.argv[2:]:
    hosts=defaultdict(lambda:[0,0]); pats=defaultdict(lambda:[0,0,0,0])
    for r in D[d]:
        p=urlparse(r['URL']); hosts[p.netloc][0]+=1; hosts[p.netloc][1]+=r['Current traffic#']
        segs=[s for s in p.path.split('/') if s]
        k='/'.join(segs[:2]) if len(segs)>1 else (segs[0] if segs else '')
        pats[k][0]+=1;pats[k][1]+=r['Current traffic#'];pats[k][2]+=r['Previous traffic#'];pats[k][3]+=r['Current traffic value#']
    print(d,dict(hosts))
    for k,v in sorted(pats.items(),key=lambda x:-x[1][1])[:45]: print(f'  {k:50} n={v[0]:4} cur={v[1]:6.0f} prev={v[2]:6.0f} ${v[3]:.0f}')
