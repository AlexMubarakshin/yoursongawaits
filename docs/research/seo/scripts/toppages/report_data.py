import json,sys
r=json.load(open(sys.argv[1]+'/results.json'))
def f(x): return f"{x:,.0f}"
for d,o in r.items():
    print(f"\n######## {d}  pages={o['n']} withtraffic={o['withtraffic']} cur={f(o['cur'])} prev={f(o['prev'])} chg={(o['cur']/o['prev']-1)*100 if o['prev'] else 0:.0f}% val={f(o['val'])} pval={f(o['pval'])} vchg={(o['val']/o['pval']-1)*100 if o['pval'] else 0:.0f}% home={f(o['home'])} homeval={f(o['homeval'])} status={o['status']}")
    print('BUCKETS', {k:[v[0],round(v[1]),round(v[2]),round(v[3]),round(v[4])] for k,v in o['buckets'].items()})
    print('PATTERNS'); [print(f"  {k:45} n={v[0]} cur={v[1]:.0f} prev={v[2]:.0f} val={v[3]:.0f} pagesWithTraffic={v[4]}") for k,v in o['patterns'][:25]]
    print('LANG',sorted(o['lang'],key=lambda x:-x[1]))
    for key in ['top_t','top_v']:
        print(key)
        for x in o[key]: print(f"  {x['url']} | {x['b']} | cur {x['cur']:.0f} val {x['val']:.0f} | {x['kw']} p{x['pos']:.0f} v{x['vol']:.0f} {x['c']}")
    print('GAIN'); [print(f"  {x['url']} {x['st']} {x['prev']:.0f}->{x['cur']:.0f} | {x['kw']} p{x['pos']:.0f} {x['c']}") for x in o['gain']]
    print('LOSS'); [print(f"  {x['url']} {x['st']} {x['prev']:.0f}->{x['cur']:.0f} | {x['kw']} p{x['pos']:.0f} {x['c']}") for x in o['loss']]
    print('NEW',o['new'],'LOST',o['lost'])
    print('AI',o['ai'],'pages',o['ai_pages'])
    for x in o['ai_top']: print(f"  {x['url']} all={x['All platforms']:.0f} AIO={x['AI Overviews']:.0f} AIM={x['AI Mode']:.0f} GPT={x['ChatGPT']:.0f} Gem={x['Gemini']:.0f} Ppx={x['Perplexity']:.0f} Cop={x['Copilot']:.0f} | {x['kw']}")
    print('COUNTRY',[(c,v[0],round(v[1]),round(v[2])) for c,v in o['country'][:8]])
    print('COMP'); [print(f"  {x['url']} cur={x['cur']:.0f} prev={x['prev']:.0f} | {x['kw']} p{x['pos']:.0f} v{x['vol']:.0f}") for x in o['comp']]
