import sys;sys.path.insert(0,sys.argv[1])
from load import *
D=load()
for d,rows in D.items():
    ct=sum(r['Current traffic#'] for r in rows); pt=sum(r['Previous traffic#'] for r in rows)
    cv=sum(r['Current traffic value#'] for r in rows); pv=sum(r['Previous traffic value#'] for r in rows)
    print(d,len(rows),'cur',ct,'prev',pt,'val',cv/100,pv/100, 'status',{s:sum(1 for r in rows if r['Status']==s) for s in set(r['Status'] for r in rows)}, 'withtraffic',sum(1 for r in rows if r['Current traffic#']>0))
r=D['songfinch.com'][0]; print(r)
