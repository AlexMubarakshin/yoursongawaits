import sys,re;sys.path.insert(0,sys.argv[1])
exec(open(sys.argv[1]+'/analyze.py').read().split('res={}')[0])
from collections import Counter
W=D['wondera.ai']
for r in W: r['bucket']=classify('wondera.ai',r)
def sl(r): return segs(r['URL'])[-1] if segs(r['URL']) else ''
groups={'alternatives (the-best-X-alternatives)':lambda r: 'alternativ' in sl(r).lower(),
 'song lists: occasion/relation':lambda r: r['bucket']=='info' and re.search(r'birthday|wedding|anniversar|mother|father|daughter|(^|-)sons?(-|$)|sister|brother|sibling|grand|wife|husband|valentine|graduat|baby|retire|friend|mom|dad|bridal|first-dance|funeral|memorial|christmas',sl(r),re.I),
 'song lists: artist-based (X-love-songs etc.)':None,
 'song lists: other (mood/genre/dance)':None,
 'UGC /song/*, /producer/*':lambda r: '/song/' in r['URL'] or '/producer/' in r['URL'],
}
res=Counter(); tr=Counter(); pv=Counter()
for r in W:
    g=None
    if '/song/' in r['URL'] or '/producer/' in r['URL']: g='UGC song/producer pages'
    elif 'alternativ' in sl(r).lower(): g='alternatives pages'
    elif r['bucket']=='info':
        if re.search(r'birthday|wedding|anniversar|mother|father|daughter|(^|-)sons?(-|$)|sister|brother|sibling|grand|wife|husband|valentine|graduat|baby|retire|friend|mom|dad|bridal|first-dance|funeral|memorial|christmas|couple',sl(r),re.I): g='song lists: occasion/relation'
        else: g='song lists/other info (mood, genre, artist, dance)'
    elif r['bucket'] in('tool_audio',): g='tool pages: audio/voice/cover/remix'
    elif r['bucket']=='tool_song': g='tool pages: song/music generator'
    else: g=r['bucket']
    res[g]+=1; tr[g]+=r['Current traffic#']; pv[g]+=r['Previous traffic#']
for g in res: print(f'{g:50} n={res[g]} cur={tr[g]:.0f} prev={pv[g]:.0f}')
occ=[r for r in W if r['bucket']=='info' and re.search(r'birthday',sl(r),re.I)]
print('birthday lists',len(occ),sum(r['Current traffic#'] for r in occ))
# en only
for g in ['en']:
    x=[r for r in W if f'/tools/{g}/' in r['URL'] and r['bucket']=='info']; print('en info',len(x),sum(r['Current traffic#'] for r in x))
print(sorted(set(sl(r) for r in W if 'alternativ' in sl(r).lower()))[:40])
print('SF',[(segs(r['URL'])[-1],r['bucket']) for r in D['sendfame.com'] if '/happy-birthday' in r['URL']][:5])
