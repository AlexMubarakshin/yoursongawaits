import json,sys,re
S=sys.argv[1]; r=json.load(open(S+'/results.json'))
BN={'brand':'Бренд','gift':'Gift-коммерция','tool_song':'Инструмент: song/lyrics/music generator','tool_audio':'Инструмент: аудио-утилиты (vocal remover, converter, autotune, covers, remix)','info':'Инфо-контент (списки песен, поздравления, цитаты, блог)','ugc_nav':'UGC/навигация (артисты, страницы песен, support, login)','offtopic':'Off-topic (video/image/NSFW/celebrity voice)','other':'Прочее'}
def n(x): return f"{x:,.0f}".replace(',',' ')
def pct(a,b): return f"{(a/b-1)*100:+.0f}%" if b else ('new' if a else '—')
def short(u,d):
    u=re.sub(r'^https?://(www\.)?','',u); u=re.sub('^'+re.escape(d),'',u)
    if len(u)>75: u=u[:72]+'…'
    return u or '/'
def cc(c): return {'United States':'US','United Kingdom':'GB','Canada':'CA','Australia':'AU','Russian Federation':'RU','Philippines':'PH','India':'IN','Nigeria':'NG','Pakistan':'PK','Hungary':'HU','South Africa':'ZA','Italy':'IT','Spain':'ES','France':'FR','Mexico':'MX','South Korea':'KR','Israel':'IL','United Arab Emirates':'AE','Indonesia':'ID','Vietnam':'VN','Kazakhstan':'KZ','Taiwan':'TW','Belgium':'BE','Japan':'JP','Germany':'DE','Brazil':'BR','Poland':'PL','Turkey':'TR','Oman':'OM','Senegal':'SN'}.get(c,c)
def esc(s): return str(s).replace('|','\\|')
out={}
for d,o in r.items():
    L=[]
    L.append(f"**Итоги:** страниц в выгрузке {o['n']} (с текущим трафиком {o['withtraffic']}); статусы: " + ', '.join(f"{k} {v}" for k,v in o['status'].items()))
    L.append('')
    L.append('| Метрика | Previous | Current | Δ |'); L.append('|---|---:|---:|---:|')
    L.append(f"| Органический трафик, визитов/мес | {n(o['prev'])} | {n(o['cur'])} | {pct(o['cur'],o['prev'])} |")
    L.append(f"| Traffic value, $ | {n(o['pval'])} | {n(o['val'])} | {pct(o['val'],o['pval'])} |")
    b=o['buckets']; br=b.get('brand',[0,0,0,0,0])
    L.append(f"| Главная: трафик (доля) | | {n(o['home'])} ({o['home']/o['cur']*100 if o['cur'] else 0:.0f}%) | |")
    L.append(f"| Бренд (top keyword = бренд): трафик / value | {n(br[2])} / ${n(br[4])} | {n(br[1])} ({br[1]/o['cur']*100 if o['cur'] else 0:.0f}%) / ${n(br[3])} ({br[3]/o['val']*100 if o['val'] else 0:.0f}%) | {pct(br[1],br[2])} |")
    L.append(f"| Небрендовый трафик / value | {n(o['prev']-br[2])} / ${n(o['pval']-br[4])} | {n(o['cur']-br[1])} / ${n(o['val']-br[3])} | {pct(o['cur']-br[1],o['prev']-br[2])} |")
    out[d+'_totals']='\n'.join(L)
    L=['| Бакет | Стр. | Трафик prev → cur | Δ | Value prev → cur, $ | Доля трафика | $/визит |','|---|---:|---:|---:|---:|---:|---:|']
    for k,v in sorted(b.items(),key=lambda x:-x[1][1]):
        L.append(f"| {BN[k]} | {v[0]} | {n(v[2])} → {n(v[1])} | {pct(v[1],v[2])} | {n(v[4])} → {n(v[3])} | {v[1]/o['cur']*100 if o['cur'] else 0:.0f}% | {v[3]/v[1] if v[1] else 0:.2f} |")
    out[d+'_buckets']='\n'.join(L)
    L=['| URL-паттерн | Стр. | Стр. с трафиком | Трафик prev → cur | Value cur, $ |','|---|---:|---:|---:|---:|']
    for k,v in o['patterns'][:int(sys.argv[2]) if len(sys.argv)>2 else 15]:
        L.append(f"| `{k}` | {v[0]} | {v[4]} | {n(v[2])} → {n(v[1])} | {n(v[3])} |")
    out[d+'_patterns']='\n'.join(L)
    for key,title in (('top_t','traffic'),('top_v','value')):
        L=['| # | URL | Бакет | Трафик | Value, $ | Top keyword | Поз. | Объём | Страна |','|---:|---|---|---:|---:|---|---:|---:|---|']
        for i,x in enumerate([x for x in o[key] if (x['cur'] if key=='top_t' else x['val'])>0],1):
            L.append(f"| {i} | `{short(x['url'],d)}` | {x['b']} | {n(x['cur'])} | {n(x['val'])} | {esc(x['kw'])} | {x['pos']:.0f} | {n(x['vol'])} | {cc(x['c'])} |")
        out[d+'_'+key]='\n'.join(L)
    L=['| URL | Статус | Трафик prev → cur | Top keyword (поз., страна) |','|---|---|---:|---|']
    for x in o['gain'][:7]: L.append(f"| `{short(x['url'],d)}` | {x['st'] or '—'} | {n(x['prev'])} → {n(x['cur'])} | {esc(x['kw'])} ({x['pos']:.0f}, {cc(x['c'])}) |")
    L.append('| **Потери** | | | |')
    for x in o['loss'][:7]: L.append(f"| `{short(x['url'],d)}` | {x['st'] or '—'} | {n(x['prev'])} → {n(x['cur'])} | {esc(x['kw'])} ({x['pos']:.0f}, {cc(x['c'])}) |")
    L.append(''); L.append(f"New-страниц: {o['new'][0]} (текущий трафик {n(o['new'][1])}, ${n(o['new'][2])}); Lost-страниц: {o['lost'][0]} (потерянный трафик {n(o['lost'][1])}, ${n(o['lost'][2])}).")
    out[d+'_winlose']='\n'.join(L)
    a=o['ai']
    L=[f"Всего упоминаний в AI-ответах: **{a['All platforms']:.0f}** на {o['ai_pages']} страницах (AI Overviews {a['AI Overviews']:.0f}, AI Mode {a['AI Mode']:.0f}, ChatGPT {a['ChatGPT']:.0f}, Gemini {a['Gemini']:.0f}, Perplexity {a['Perplexity']:.0f}, Copilot {a['Copilot']:.0f}, Grok {a['Grok']:.0f})."]
    if o['ai_top']:
        L+=['','| URL | Всего | AIO | AI Mode | ChatGPT | Gemini | Perplexity | Copilot | Top keyword |','|---|---:|---:|---:|---:|---:|---:|---:|---|']
        for x in o['ai_top'][:8]: L.append(f"| `{short(x['url'],d)}` | {x['All platforms']:.0f} | {x['AI Overviews']:.0f} | {x['AI Mode']:.0f} | {x['ChatGPT']:.0f} | {x['Gemini']:.0f} | {x['Perplexity']:.0f} | {x['Copilot']:.0f} | {esc(x['kw'])} |")
    out[d+'_ai']='\n'.join(L)
    tot=o['cur'] or 1
    out[d+'_country']='Страна top keyword → доля текущего трафика: ' + ', '.join(f"{cc(c)} {v[1]/tot*100:.0f}% ({n(v[1])})" for c,v in o['country'][:7] if v[1]>0)
json.dump(out,open(S+'/md_parts.json','w'),ensure_ascii=False,indent=0)
print(len(out))
