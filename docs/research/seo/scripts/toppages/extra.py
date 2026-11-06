import sys,re;sys.path.insert(0,sys.argv[1])
exec(open(sys.argv[1]+'/analyze.py').read().split('res={}')[0])
from collections import Counter
for d in ORDER:
    for r in D[d]: r['bucket']=classify(d,r)
print('== gift buckets per domain after fix')
for d in ORDER:
    g=[r for r in D[d] if r['bucket']=='gift']; print(d,len(g),sum(r['Current traffic#'] for r in g),round(sum(r['Current traffic value#'] for r in g)))
print('== EN gift/occasion keywords (all domains, kw from cur or prev)')
GR=re.compile(r'song|lyric|birthday|anniversary|wedding|gift|mother|father|wife|husband|valentine|grandma|grandpa|sister|brother|son\b|daughter|boyfriend|girlfriend|personali|custom',re.I)
seen=set(); rows=[]
for d in ORDER:
    for r in D[d]:
        for pre in ('Current','Previous'):
            k=r[pre+' top keyword']; c=r[pre+' top keyword: Country']
            if not k or c not in('United States','United Kingdom','Canada','Australia'): continue
            if not GR.search(k) or BRAND.search(k): continue
            key=(k,d)
            if key in seen: continue
            seen.add(key); rows.append((r[pre+' top keyword: Volume#'],k,c[:3],d,r[pre+' top keyword: Position#'],r['Current traffic#'],r['URL'].split('.ai')[-1].split('.com')[-1][:55],r['bucket']))
for x in sorted(rows,key=lambda x:-x[0])[:150]: print(f"{x[0]:6.0f} | {x[1][:50]:50} | {x[2]} | {x[3][:10]:10} | p{x[4]:.0f} | t{x[5]:.0f} | {x[6]} | {x[7]}")
print('== name-song keywords')
NR=re.compile(r'happy birthday [a-z]+|с днем рождения|feliz cumplea|buon compleanno|joyeux anniv|alles gute|birthday song with name|song with name|name song',re.I)
for d in ORDER:
    m=[r for r in D[d] if NR.search(kw(r))]
    print(d,len(m),sum(r['Current traffic#'] for r in m),sum(r['Previous traffic#'] for r in m))
    for r in sorted(m,key=lambda r:-(r['Current traffic#']+r['Previous traffic#']))[:8]: print('   ',r['URL'][-60:],'|',kw(r),r['Current top keyword: Volume#'] or r['Previous top keyword: Volume#'],int(r['Previous traffic#']),'>',int(r['Current traffic#']))
print('== sendfame happy-birthday slugs'); print([segs(r['URL'])[-1] for r in D['sendfame.com'] if '/happy-birthday/' in r['URL']])
print('== wondera info slugs sample by lang'); 
c=Counter(); 
for r in D['wondera.ai']:
    if r['bucket']=='info':
        ss=segs(r['URL']); l=[x for x in ss if x in LANGS]; c[l[0] if l else '-']+=1
print(c)
occ=Counter()
for r in D['wondera.ai']:
    if r['bucket']=='info':
        sl=segs(r['URL'])[-1].lower()
        for t in ['birthday','wedding','anniversary','mother','father','daughter','son','sister','brother','sibling','love','sad','dance','karaoke','breakup','christmas','graduation','funeral','memorial','valentine','baby','grand','friend','wife','husband','retire']:
            if re.search(r'(^|-)'+t,sl): occ[t]+=1
print(occ)
gt=[r for r in D['wondera.ai'] if r['bucket']=='info' and re.search(r'birthday|wedding|anniversar|mother|father|daughter|(^|-)son|sister|brother|sibling|grand|wife|husband|valentine|graduat|baby|retire|friend',segs(r['URL'])[-1],re.I)]
print('wondera occasion/relation song lists',len(gt),sum(r['Current traffic#'] for r in gt),sum(r['Previous traffic#'] for r in gt))
print('== songfinch playlists'); pl=[r for r in D['songfinch.com'] if '/playlists/' in r['URL']]; print(len(pl),sum(r['Current traffic#'] for r in pl)); print([segs(r['URL'])[-1] for r in pl])
print('== giftsong all urls'); print([r['URL'].split('giftsong.ai')[1] for r in D['giftsong.ai']])
print('== wondera hosts duplicates'); u=Counter(r['URL'].replace('www.','') for r in D['wondera.ai']); print(sum(1 for k,v in u.items() if v>1))
