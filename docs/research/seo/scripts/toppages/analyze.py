import sys,json;sys.path.insert(0,sys.argv[1])
from load import *
from urllib.parse import urlparse, unquote
from collections import defaultdict, Counter
D=load()
ORDER=['songfinch.com','giftsong.ai','songlorious.com','sendfame.com','wondera.ai','musicmake.ai','pesinka.ru','everyonesing.ru']
LANGS=set('en es it ru fr ko pt ja de zh-Hant zh-Hans zh vi ar id tr pl nl hi th x-default uk sv da no fi cs'.split())
BRAND=re.compile(r'songfinch|song ?finch|sonfinch|song ?fitch|giftsong|songl?orious|songglorious|songalicious|send ?fame|wondera|musicmake|pesinka|песинка|everyonesing',re.I)
COMP=re.compile(r'/vs/|-vs-|alternativ|suno|\budio\b|cameo|musichero|soundful|songdo|songr\b|songr-|musenet|songly|musicfx|competitor|best-custom-song-company',re.I)
OFF=re.compile(r'video|image|deepfake|book.?cover|sticker|nsfw|effects|scary|animate|album.?cover|seedance|reelmagic|followers|endorsement|voice.?actor|spongebob|instagram|celebrity|dirty|jumpscare|photo|hulk|belly|jaw|jiggle|arc.?shot|text.?to.?speech|tv.?lovers|deepfake',re.I)
AUDIO=re.compile(r'vocal|voice|remover|convert|bpm|key-detector|master|mp3|wav|m4a|ogg|aac|aiff|flac|midi|cutter|joiner|splitter|tag-editor|autotune|separator|backing|enhancement|muddy|polished|transpose|radio-clean|audio|robot|drake|ariana|cover|remix|mashup|swap|clone|harmon|choir|lyric-swap|ringtone|song-edit|music-elements|piano|phonk|sample|beat|jingle|dance-ai|kids-dancing|hidden-message|meme',re.I)
SONGTOOL=re.compile(r'generator|maker|creator|composer|create|generate|lyrics-to-song|poems-to|ai-music|ai-song|song-builder|music-app|software|api|tools?$|^ai$|alternativ|suno|engine|rap-generator|lyric',re.I)
GIFTURL=re.compile(r'/occasions|/relation|/gifts|/pricing|/create|/landing-pages|/how-to/custom|/products/|/how-it-works|/store|/song-builder|/podarok|/povod|/komu|/happy-birthday-music|/vs/|best-custom-song|custom-songs-cost|/country$|/lp/',re.I)
GIFTKW=re.compile(r'custom (rock|love|country)? ?song|personali[sz]ed (song|music)|song gift|gift a song|на заказ|в подарок|create a song for',re.I)
UGC=re.compile(r'/artists?/|/stories/|/song/info|/song/detail|/music/|/producer|/u/|/careers|/apply|/login|/faq|/dashboard|/terms|/privacy|/featured-artists|/hindi-apply|/about|/reviews|/r$|/event-reminder|/promo|/songlorious-business|/discover$|/info$|/detail$',re.I)
def host(u): return urlparse(u).netloc.replace('www.','')
def kw(r): return r['Current top keyword'] or r['Previous top keyword']
def country(r): return r['Current top keyword: Country'] or r['Previous top keyword: Country']
def segs(u):
    p=urlparse(u); return [unquote(s) for s in p.path.split('/') if s]
def classify(d,r):
    u=r['URL']; k=kw(r); ss=segs(u); path='/'+'/'.join(ss); slug=ss[-1] if ss else ''
    sub=host(u).split('.')[0] if host(u).count('.')>1 else ''
    if BRAND.search(k): return 'brand'
    if ss and all(x in LANGS for x in ss): ss=[]
    if not ss and d in('giftsong.ai','everyonesing.ru','musicmake.ai'):
        return 'gift' if d!='musicmake.ai' else 'tool_song'
    if not ss: return 'brand'
    if OFF.search(path) or OFF.search(k):
        if not GIFTURL.search(path) and '/happy-birthday' not in path: return 'offtopic'
    if sub=='support': return 'ugc_nav'
    if GIFTURL.search(path) or sub=='get' or GIFTKW.search(k): return 'gift'
    if UGC.search(path): return 'ugc_nav'
    if d in('wondera.ai','musicmake.ai','sendfame.com','giftsong.ai'):
        if '/blog' in path or '/article' in path or 'playlist' in path or '/happy-birthday' in path: 
            if SONGTOOL.search(slug) and re.search(r'generator|maker|alternativ|suno|musichero|soundful',slug,re.I) and not OFF.search(slug):
                return 'tool_song'
            return 'info'
        if re.search(r'songs|playlist|song-list|lyrics-about|soundtrack',slug,re.I) and not re.search(r'generator|maker|tool|mashup|remix|cover',slug,re.I): return 'info'
        if slug in ('tools','Tools','AI','Home','Beranda','Alat','Tools/'): slug=k
        if (AUDIO.search(slug) or re.search(r'vocal|voice|remover|bpm|master|autotune|filter',slug,re.I)) and not re.search(r'song-generator|music-generator|lyrics|generate ai music|lagu|muzik|music',slug,re.I): return 'tool_audio'
        if SONGTOOL.search(slug) or re.search(r'(^|-)ai(-|$)|AI-',slug): return 'tool_song'
        return 'info'
    if 'playlist' in path or '/article' in path or '/blog' in path or 'Идеи' in path: return 'info'
    return 'other'
def pattern(u):
    h=host(u); ss=segs(u); pre='' if h.count('.')<2 else h.split('.')[0]+'.'
    out=[]
    for i,s in enumerate(ss):
        if s in LANGS: out.append('{lang}')
        else: out.append(s); break
    if len(ss)>len(out): out.append('*')
    return pre+'/'+'/'.join(out)
res={}
for d in ORDER:
    rows=D[d]
    for r in rows: r['bucket']=classify(d,r); r['pattern']=pattern(r['URL']); r['comp']=bool(COMP.search(r['URL']) or COMP.search(kw(r)) or (d!='songfinch.com' and 'songfinch' in kw(r).lower()))
    T=lambda f,rs=rows: sum(r[f] for r in rs)
    out={'n':len(rows),'cur':T('Current traffic#'),'prev':T('Previous traffic#'),'val':T('Current traffic value#'),'pval':T('Previous traffic value#'),
         'withtraffic':sum(1 for r in rows if r['Current traffic#']>0),
         'status':Counter(r['Status'] or 'Unchanged' for r in rows)}
    home=[r for r in rows if not segs(r['URL']) and host(r['URL'])==d.replace('www.','')]
    out['home']=sum(r['Current traffic#'] for r in home); out['homeval']=sum(r['Current traffic value#'] for r in home)
    b=defaultdict(lambda:[0,0,0,0,0])
    for r in rows:
        x=b[r['bucket']]; x[0]+=1; x[1]+=r['Current traffic#']; x[2]+=r['Previous traffic#']; x[3]+=r['Current traffic value#']; x[4]+=r['Previous traffic value#']
    out['buckets']={k:v for k,v in b.items()}
    p=defaultdict(lambda:[0,0,0,0,0])
    for r in rows:
        x=p[r['pattern']]; x[0]+=1; x[1]+=r['Current traffic#']; x[2]+=r['Previous traffic#']; x[3]+=r['Current traffic value#']; x[4]+=(r['Current traffic#']>0)
    out['patterns']=sorted(p.items(),key=lambda x:(-x[1][1],-x[1][0]))
    lang=Counter(); langt=Counter()
    for r in rows:
        ls=[s for s in segs(r['URL']) if s in LANGS]
        l=ls[0] if ls else '(none/en)'; lang[l]+=1; langt[l]+=r['Current traffic#']
    out['lang']=[(l,lang[l],langt[l]) for l in lang]
    def row(r): return dict(url=r['URL'],st=r['Status'],prev=r['Previous traffic#'],cur=r['Current traffic#'],val=r['Current traffic value#'],kw=kw(r),c=country(r),vol=r['Current top keyword: Volume#'] or r['Previous top keyword: Volume#'],pos=r['Current top keyword: Position#'] or r['Previous top keyword: Position#'],b=r['bucket'],ai=r['AI responses: All platforms#'],rd=r['Current referring domains#'],nk=r['Current # of keywords#'],chg=r['Traffic change#'])
    out['top_t']=[row(r) for r in sorted(rows,key=lambda r:-r['Current traffic#'])[:15]]
    out['top_v']=[row(r) for r in sorted(rows,key=lambda r:-r['Current traffic value#'])[:15]]
    out['gain']=[row(r) for r in sorted(rows,key=lambda r:-r['Traffic change#'])[:10] if r['Traffic change#']>0]
    out['loss']=[row(r) for r in sorted(rows,key=lambda r:r['Traffic change#'])[:10] if r['Traffic change#']<0]
    out['new']=(sum(1 for r in rows if r['Status']=='New'),sum(r['Current traffic#'] for r in rows if r['Status']=='New'),sum(r['Current traffic value#'] for r in rows if r['Status']=='New'))
    out['lost']=(sum(1 for r in rows if r['Status']=='Lost'),sum(r['Previous traffic#'] for r in rows if r['Status']=='Lost'),sum(r['Previous traffic value#'] for r in rows if r['Status']=='Lost'))
    out['newtop']=[row(r) for r in sorted([r for r in rows if r['Status']=='New'],key=lambda r:-r['Current traffic#'])[:6]]
    out['losttop']=[row(r) for r in sorted([r for r in rows if r['Status']=='Lost'],key=lambda r:-r['Previous traffic#'])[:6]]
    plats=['All platforms','AI Overviews','AI Mode','ChatGPT','Gemini','Perplexity','Copilot','Grok']
    out['ai']={p_:sum(r['AI responses: '+p_+'#'] for r in rows) for p_ in plats}
    out['ai_pages']=sum(1 for r in rows if r['AI responses: All platforms#']>0)
    out['ai_top']=[dict(row(r),**{p_:r['AI responses: '+p_+'#'] for p_ in plats}) for r in sorted(rows,key=lambda r:-r['AI responses: All platforms#'])[:10] if r['AI responses: All platforms#']>0]
    cc=defaultdict(lambda:[0,0,0])
    for r in rows:
        c=country(r) or '(n/a)'; cc[c][0]+=1; cc[c][1]+=r['Current traffic#']; cc[c][2]+=r['Current traffic value#']
    out['country']=sorted(cc.items(),key=lambda x:-x[1][1])
    out['comp']=[row(r) for r in rows if r['comp']]
    out['bucket_top']={bk:[row(r) for r in sorted([r for r in rows if r['bucket']==bk],key=lambda r:-r['Current traffic#'])[:8]] for bk in b}
    res[d]=out
json.dump(res,open(sys.argv[1]+'/results.json','w'),ensure_ascii=False,indent=1,default=list)
for d in ORDER:
    o=res[d]; print('\n#',d,o['n'],'cur',o['cur'],'prev',o['prev'],'val',round(o['val']),round(o['pval']),'home',o['home'],o['status'])
    for k,v in sorted(o['buckets'].items(),key=lambda x:-x[1][1]): print('  ',k,v[0],int(v[1]),int(v[2]),round(v[3]),round(v[4]))
