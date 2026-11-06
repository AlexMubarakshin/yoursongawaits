import sys, csv, collections, statistics, json, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from classify import classify, detect_language, lang_modifier

SP = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(SP, '..', 'raw', 'global.tsv')  # was data/global.tsv in session scratchpad
TREND_COL = 'SV trend (11-2024 - 10-2026)'
MONTHS = [f'{y}-{m:02d}' for y, m in [(2024, 11), (2024, 12)] + [(2025, i) for i in range(1, 13)] + [(2026, i) for i in range(1, 11)]]

TIERS = {
    'EN_HIGH_CPC': 'us gb ca au nz ie',
    'EN_LOW_CPC': 'in ph pk ng za lk bd np ke gh ug tz zm zw et jm tt pg fj mw rw cm sl lr bw na mu gy bb bs bz mv',
    'EU_NON_EN': 'de fr es it nl pl se dk no fi be at ch pt gr cz ro hu sk bg hr si rs lt lv ee lu cy mt is ba mk al me',
    'LATAM_BR': 'br mx ar co cl pe ec ve uy py bo cr pa do gt hn sv ni pr cu',
    'RU_CIS': 'ru ua by kz uz kg tj tm am az ge md',
    'ASIA': 'jp kr id vn th my sg hk tw cn kh mm la mn mo bn',
    'MENA': 'ae sa qa kw om bh eg ma dz tn jo lb il iq ly ps ye sy tr',
}
C2T = {c: t for t, cs in TIERS.items() for c in cs.split()}
GIFT = lambda c: c in ('GIFT_CORE', 'BIRTHDAY_NAME', 'RECIPIENT') or c.startswith('OCCASION_')


def num(x, f=float):
    try:
        return f(x) if x not in ('', None) else None
    except ValueError:
        return None


cache = {}
rows = []
with open(DATA, encoding='utf-8') as fh:
    for r in csv.DictReader(fh, delimiter='\t'):
        kw = r['Keyword']; cc = r['Country']
        if kw not in cache:
            kl = kw.lower()
            cache[kw] = classify(kw) + (detect_language(kl, 'xx'), lang_modifier(kl))
        cl, reason, explicit, lang0, mod0 = cache[kw]
        lang = detect_language(kw.lower(), cc) if lang0 == 'xx-latin' else lang0
        tr = [num(x.strip()) or 0 for x in r[TREND_COL].split(',')] if r[TREND_COL].strip() else None
        if tr and len(tr) != 24:
            tr = None
        rows.append(dict(kw=kw, cc=cc, vol=int(num(r['Volume']) or 0), kd=num(r['Difficulty']), cpc=num(r['CPC']),
                         cl=cl, reason=reason, explicit=explicit, lang=lang,
                         mod=mod0, trend=tr, tier=C2T.get(cc, 'OTHER'),
                         intents=r['Intents'], parent=r['Parent Keyword']))

out = []
P = out.append
tot = sum(r['vol'] for r in rows)

# ---------- cluster totals ----------
cl_vol = collections.Counter(); cl_kw = collections.defaultdict(set)
for r in rows:
    cl_vol[r['cl']] += r['vol']; cl_kw[r['cl']].add(r['kw'])
noise_reason = collections.Counter(r['reason'] for r in rows if r['cl'] == 'NOISE' for _ in [0])
noise_rv = collections.Counter()
for r in rows:
    if r['cl'] == 'NOISE':
        noise_rv[r['reason']] += r['vol']

# ---------- language shares ----------
def lang_share(filt):
    c = collections.Counter(); kws = collections.defaultdict(set)
    for r in rows:
        if filt(r):
            c[r['lang']] += r['vol']; kws[r['lang']].add(r['kw'])
    return c, kws

lang_all, lk_all = lang_share(lambda r: True)
lang_rel, lk_rel = lang_share(lambda r: r['cl'] != 'NOISE')
lang_gift, lk_gift = lang_share(lambda r: GIFT(r['cl']))
mod_c = collections.Counter(); mod_g = collections.Counter()
for r in rows:
    if r['lang'] == 'en' and r['mod'] and r['cl'] != 'NOISE':
        mod_c[r['mod']] += r['vol']
        if GIFT(r['cl']):
            mod_g[r['mod']] += r['vol']
mod_noise = collections.Counter()
for r in rows:
    if r['lang'] == 'en' and r['mod'] and r['cl'] == 'NOISE':
        mod_noise[r['mod']] += r['vol']

# ---------- country table ----------
def wavg(pairs):
    s = sum(v for v, c in pairs if c is not None and v > 0)
    return sum(v * c for v, c in pairs if c is not None and v > 0) / s if s else None

def growth(trs):
    trs = [t for t in trs if t]
    if not trs:
        return None
    a = sum(sum(t[:12]) for t in trs); b = sum(sum(t[12:]) for t in trs)
    return (b / a - 1) * 100 if a > 0 else None

by_c = collections.defaultdict(list)
for r in rows:
    by_c[r['cc']].append(r)

table = []
for cc, rs in by_c.items():
    rel = [r for r in rs if r['cl'] not in ('NOISE', 'AI_GENERATOR')]
    ai = [r for r in rs if r['cl'] == 'AI_GENERATOR']
    gift = [r for r in rs if GIFT(r['cl'])]
    strict = [r for r in gift if r['explicit']]
    nz = [r for r in rs if r['cl'] != 'NOISE']
    gv = sum(r['vol'] for r in gift)
    if sum(r['vol'] for r in nz) == 0:
        continue
    kds = [r['kd'] for r in gift if r['vol'] > 0 and r['kd'] is not None]
    kds_rel = [r['kd'] for r in nz if r['vol'] > 0 and r['kd'] is not None]
    gcpc = wavg([(r['vol'], r['cpc']) for r in gift])
    aicpc = wavg([(r['vol'], r['cpc']) for r in ai])
    allcpc = wavg([(r['vol'], r['cpc']) for r in nz])
    langs = collections.Counter()
    for r in nz:
        langs[r['lang']] += r['vol']
    dom = langs.most_common(1)[0]
    nonen = sum(v for l, v in langs.items() if l != 'en')
    cpc_used = gcpc if gcpc is not None else allcpc
    table.append(dict(
        country=cc, tier=C2T.get(cc, 'OTHER'), relevant_vol=sum(r['vol'] for r in rel), gift_vol=gv,
        gift_strict_vol=sum(r['vol'] for r in strict), gift_core_vol=sum(r['vol'] for r in rs if r['cl'] == 'GIFT_CORE'),
        birthday_name_vol=sum(r['vol'] for r in rs if r['cl'] == 'BIRTHDAY_NAME'),
        occasion_vol=sum(r['vol'] for r in rs if r['cl'].startswith('OCCASION_')),
        brand_vol=sum(r['vol'] for r in rs if r['cl'] == 'BRAND_COMPETITOR'),
        ai_generator_vol=sum(r['vol'] for r in ai), noise_vol=sum(r['vol'] for r in rs if r['cl'] == 'NOISE'),
        median_kd_gift=statistics.median(kds) if kds else None, median_kd_all=statistics.median(kds_rel) if kds_rel else None,
        wcpc_gift=gcpc, wcpc_ai=aicpc, wcpc_all=allcpc,
        growth_12mo_gift_pct=growth([r['trend'] for r in gift]), growth_12mo_all_pct=growth([r['trend'] for r in nz]),
        dominant_lang=dom[0], non_en_share_pct=100 * nonen / sum(langs.values()),
        attractiveness=gv * (cpc_used or 0), cpc_fallback=gcpc is None,
    ))
table.sort(key=lambda d: -d['attractiveness'])
for i, d in enumerate(table, 1):
    d['rank_attr'] = i
for i, d in enumerate(sorted(table, key=lambda d: -d['gift_vol']), 1):
    d['rank_giftvol'] = i

fields = ['rank_attr', 'rank_giftvol', 'country', 'tier', 'gift_vol', 'gift_strict_vol', 'relevant_vol', 'gift_core_vol',
          'birthday_name_vol', 'occasion_vol', 'brand_vol', 'ai_generator_vol', 'noise_vol', 'median_kd_gift', 'median_kd_all',
          'wcpc_gift', 'wcpc_ai', 'wcpc_all', 'attractiveness', 'cpc_fallback', 'growth_12mo_gift_pct', 'growth_12mo_all_pct',
          'dominant_lang', 'non_en_share_pct']
with open(os.path.join(SP, 'global_countries.csv'), 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=fields)
    w.writeheader()
    for d in table:
        w.writerow({k: (round(v, 2) if isinstance(v, float) else v) for k, v in d.items() if k in fields})

# ---------- tier aggregates ----------
tier_agg = collections.defaultdict(lambda: collections.Counter())
tier_cpc = collections.defaultdict(list); tier_ai_cpc = collections.defaultdict(list)
tier_trend = collections.defaultdict(lambda: [0.0] * 24)
tier_trend_ai = collections.defaultdict(lambda: [0.0] * 24)
for r in rows:
    t = r['tier']
    if GIFT(r['cl']):
        tier_agg[t]['gift'] += r['vol']; tier_cpc[t].append((r['vol'], r['cpc']))
        if r['explicit']:
            tier_agg[t]['strict'] += r['vol']
        if r['trend']:
            tier_trend[t] = [a + b for a, b in zip(tier_trend[t], r['trend'])]
    if r['cl'] == 'AI_GENERATOR':
        tier_agg[t]['ai'] += r['vol']; tier_ai_cpc[t].append((r['vol'], r['cpc']))
        if r['trend']:
            tier_trend_ai[t] = [a + b for a, b in zip(tier_trend_ai[t], r['trend'])]
    if r['cl'] not in ('NOISE', 'AI_GENERATOR'):
        tier_agg[t]['rel'] += r['vol']
    if r['cl'] == 'NOISE':
        tier_agg[t]['noise'] += r['vol']

# ---------- occasion seasonality per country ----------
occ_trend = collections.defaultdict(lambda: [0.0] * 24)
for r in rows:
    if r['trend'] and (r['cl'].startswith('OCCASION_') or r['reason'].endswith('listening (download/status/lyrics/kids/church)')):
        occ = r['cl'][9:] if r['cl'].startswith('OCCASION_') else r['reason'].split(' ')[0]
        occ_trend[(occ, r['cc'])] = [a + b for a, b in zip(occ_trend[(occ, r['cc'])], r['trend'])]
bday_trend = collections.defaultdict(lambda: [0.0] * 24)
for r in rows:
    if r['trend'] and r['cl'] in ('BIRTHDAY_NAME', 'GIFT_CORE', 'BRAND_COMPETITOR', 'RECIPIENT'):
        bday_trend[(r['cl'], r['tier'])] = [a + b for a, b in zip(bday_trend[(r['cl'], r['tier'])], r['trend'])]

json.dump(dict(cl_vol=cl_vol, cl_kw={k: len(v) for k, v in cl_kw.items()}, noise_rv=noise_rv, tot=tot,
               lang_all=lang_all, lang_rel=lang_rel, lang_gift=lang_gift,
               lk_all={k: len(v) for k, v in lk_all.items()}, mod_c=mod_c, mod_g=mod_g, mod_noise=mod_noise,
               tier_agg={t: dict(c) for t, c in tier_agg.items()},
               tier_cpc={t: wavg(v) for t, v in tier_cpc.items()}, tier_ai_cpc={t: wavg(v) for t, v in tier_ai_cpc.items()},
               tier_trend=tier_trend, tier_trend_ai=tier_trend_ai,
               occ_trend={f'{k[0]}|{k[1]}': v for k, v in occ_trend.items()},
               bday_trend={f'{k[0]}|{k[1]}': v for k, v in bday_trend.items()}),
          open(os.path.join(SP, 'agg.json'), 'w'), default=float)

# rows for later sections
import pickle
pickle.dump([{k: v for k, v in r.items() if k != 'trend'} | {'trend': r['trend']} for r in rows],
            open(os.path.join(SP, 'rows.pkl'), 'wb'))
print('rows', len(rows), 'countries', len(table))
for d in table[:30]:
    print({k: (round(v, 2) if isinstance(v, float) else v) for k, v in d.items() if k in ('country', 'gift_vol', 'gift_strict_vol', 'ai_generator_vol', 'wcpc_gift', 'wcpc_ai', 'attractiveness', 'growth_12mo_gift_pct', 'dominant_lang', 'median_kd_gift')})
