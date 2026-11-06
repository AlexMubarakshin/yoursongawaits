"""US Ahrefs matching-terms analysis for personalized-song-gift product.
Run: python3 -I us_analysis.py   (reads ../raw/us.tsv, never modifies it)
"""
import csv, re, statistics, collections, os, sys

S = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(S, '..', 'raw', 'us.tsv')  # was data/us.tsv in session scratchpad
TREND = 'SV trend (11-2024 - 10-2026)'
MONTHS = [f'{m}' for m in ['2024-11', '2024-12'] + [f'2025-{i:02d}' for i in range(1, 13)] + [f'2026-{i:02d}' for i in range(1, 11)]]

rows = list(csv.DictReader(open(SRC, encoding='utf-8'), delimiter='\t'))


def num(s, f=float):
    s = (s or '').strip()
    try:
        return f(s)
    except ValueError:
        return None


for x in rows:
    x['kw'] = x['Keyword'].strip().lower()
    x['vol'] = num(x['Volume'], int) or 0
    x['kd'] = num(x['Difficulty'], int)
    x['cpc'] = num(x['CPC'])
    x['tp'] = num(x['Traffic potential'], int) or 0
    tr = [num(v, int) or 0 for v in x[TREND].split(',')] if x[TREND].strip() else [0] * 24
    x['trend'] = (tr + [0] * 24)[:24]

# ---------------------------------------------------------------- rules
def rx(words):
    return re.compile(r'\b(?:' + '|'.join(words) + r')\b')

# NOISE (hard): games/mods, famous songs/artists/franchise anniversaries
NOISE_ENTITY = rx([r'beat saber', 'fnf', r'friday night funkin', 'roblox', r'guitar hero', 'rocksmith', 'osu', r'clone hero',
    'paradiddle', 'sao', r'sword art', r'dead as disco', 'brawl', 'genshin', 'pokemon', r'hannah montana', 'elmo\'?s?',
    r'sesame street', r'song of (?:the )?achilles', r'achilles', r'song of the south', r'song of solomon', 'flintstones?', 'flinstones',
    r'al jolson', r'eva cassidy', r'cowboy junkies', r'mariah carey', r'charlie wilson', 'giveon', r'heartbreak anniversary',
    r'tony toni', 'babyface', r'duran duran', r'little river band', r'pinhead gunpowder', r'straight no chaser', 'cma',
    'seventeen', 'smg4', r'bc clark', 'fender', 'washburn', r'disneyland', r'saujana', r'taiwan campus', r'it\'?s our anniversary',
    r'singer 1916', r'who wrote', r'spotdl', r'mobcup', r'naa songs', r'first name,? vol', r'game of thrones', 'caseoh', 'spongebob',
    'bluey', 'kpop', r'morgan wallen', r'boyz? (?:to|ii) men', r'steel panther', r'willow smith', 'dior', r'mod apk', r'high resolution images', r'sheet music', r'work anniversary', r'company anniversary',
    r'death anniversary', 'bts', 'taylor swift', 'beatles', r'hotel lobby'])
# Listening / media-consumption markers -> NOISE always
LISTEN = rx(['lyrics?', 'karaoke', 'chords?', 'ringtone', 'instrumental', 'piano', 'tabs', 'meaning',
    'hindi', 'punjabi', 'tamil', 'telugu', 'kannada', 'malayalam', 'marathi', 'bengali', 'gujarati', 'urdu', 'bollywood',
    'arabic', 'myanmar', 'nepali', 'bhojpuri', 'odia', 'ke', 'ka', 'wale', 'mummy papa', 'serbian', 'korean', 'japanese', 'spanish',
    'lds', 'church', 'worship', 'gospel', 'preschool', r'walk up', 'baseball', 'cake cutting', 'dance', 'dj', 'remix'])
# lyrics words that ARE product-relevant (song from lyrics, custom lyrics)
LYRICS_OK = re.compile(r'custom song lyrics$|lyrics?.*gift|lyrics? to song|from (?:my |your )?lyrics|with (?:my |your |custom )?lyrics|custom lyrics|lyrics? (?:into|in) (?:a )?song|lyrics?\s*(?:->|to)\s*music')
# media / download markers -> NOISE unless personalization signal
MEDIA = rx(['mp3', 'mp4', 'download', r'video song', 'youtube', 'reels?', 'reals', 'status', 'whatsapp', 'capcut', 'template',
    'gif', 'instagram', r'insta', 'tiktok', 'images?', 'photo', 'post', 'story', 'latest', 'new', 'trending', 'album', 'audio',
    r'(?:19|20)\d\d', 'real', 'official', 'old', 'version', 'singer', 'artist', 'music box'])
PERSONAL = re.compile(r'with (?:the |a |my |your |our |custom |child\'?s |person\'?s |persons |indian )?name|custom|personali[sz]|my name|your name|name inserted|enter name')
# AI tool off-target: covers / voice cloning / lyrics-only / titles / video / parody
AI_OFF = re.compile(r'\bcovers?\b|voice|clon|celebrity|parody|mashup|vocaloid|(?:lyrics?|lyric) (?:generator|maker|writer)|'
                    r'song (?:name|title) generator|title generator|video generator|music video|song to video|video maker|'
                    r'prompt generator|song structure|structure tags|interface|screen\b|maximum song length|song length|format lyrics|'
                    r'how to (?:format|structure|use)')
# Physical song merch / platform how-tos (adjacent gift intent, different product)
MERCH = re.compile(r'music box|plaque|wall art|canvas|print|poster|frame|acrylic|glass|blanket|necklace|keychain|magnet|vinyl|'
                   r'sound ?wave|\bcards?\b|jewelry box|hoodie|song player|spotify|acrylic sign|ornament|bracelet|pillow|shirt|mug')
SPOTIFY_HOWTO = re.compile(r'(?:add|set|upload|put).*custom song.*(?:spotify|instagram|iphone|alarm|ringtone)|custom song id')

GIFT_BRANDS = {
    'songfinch': r'songfinch|song finch', 'songlorious': r'songlorious', 'giftsong': r'giftsong|gift song ai', 'customsong': r'customsong\b',
    'makecustomsongs': r'make ?custom ?songs\.?com|makecustomsongs', 'birthdai': r'birthdai', 'foreversongs': r'foreversongs|forever songs',
    'custom song central': r'custom song central', 'divine song': r'divine song', 'songs from the heart': r'songs from the heart',
    'unique song': r'unique song custom', 'magic exhalation': r'magic exhalation', 'songer': r'\bsonger\b', 'songsaver': r'songsaver',
}
AI_BRANDS = {
    'suno': r'\bsuno\b|\bsumo ai', 'udio': r'\budio\b', 'wondera': r'wondera', 'freebeat': r'freebeat', 'musicmake': r'musicmake\b',
    'soundverse': r'soundverse', 'mureka': r'mureka|merika', 'musely': r'musely', 'bandlab': r'bandlab', 'singify': r'singify',
    'insmelo': r'insmelo', 'riffusion': r'riffusion', 'boomy': r'boomy', 'vidnoz': r'vidnoz', 'topmediai': r'topmediai',
    'musicful': r'musicful', 'musicfy': r'musicfy', 'voicemod': r'voicemod', 'mozart ai': r'mozart ai', 'jam ai': r'\bjam ai',
    'ace-step': r'ace-step', 'sonauto': r'sonauto', 'loudly': r'loudly', 'makesong': r'makesong', 'muzio': r'muzio', 'brev': r'\bbrev\b',
    'lami': r'\blami\b', 'neume': r'neume', 'soniva': r'soniva', 'melodycraft': r'melody ?craft', 'aimusic.so': r'aimusic\.so',
    'aisongmaker': r'aisongmaker', 'easeus': r'easeus', 'openmusic': r'openmusic', 'perchance': r'perchance', 'song.do': r'song\.do',
    'mubert': r'mubert', 'aiva': r'\baiva\b', 'beatoven': r'beatoven', 'soundraw': r'soundraw', 'musicgpt': r'musicgpt', 'sonu': r'\bsonu ai',
}
BRANDS = {**{k: (re.compile(v), 'gift') for k, v in GIFT_BRANDS.items()}, **{k: (re.compile(v), 'ai_tool') for k, v in AI_BRANDS.items()}}

OCC = [  # order matters
    ('OCCASION_mothers_day', r"mothers?'?s? ?day|mother day|mom'?s day"),
    ('OCCASION_fathers_day', r"fathers?'?s? ?day|father day|dad'?s day"),
    ('OCCASION_valentines', r'valentin'),
    ('OCCASION_christmas', r'christmas|xmas|holiday'),
    ('OCCASION_memorial', r'memorial|funeral|tribute|in heaven|celebration of life|passed away|sympathy|remembrance|in loving memory|rip\b'),
    ('OCCASION_retirement', r'retire'),
    ('OCCASION_graduation', r'graduat'),
    ('OCCASION_wedding', r'wedding(?! anniversary)|first dance|bride|groom|marry me|proposal|engagement(?! anniversary)'),
    ('OCCASION_anniversary', r'anniversary|anniversery|aniversary'),
    ('OCCASION_other', r'baby shower|gender reveal|newborn|new baby|bar mitzvah|bat mitzvah|quincea|sweet 16|sweet sixteen|thanksgiving|'
                       r'easter|hanukkah|get well|congratulat|teacher appreciation|\bnurses? (?:day|week)|baptism|christening|prayer song|custom prayer'),
]
OCC = [(n, re.compile(p)) for n, p in OCC]
RECIP = re.compile(r'\b(?:wife|husband|mom|mother|mum|dad|father|girlfriend|boyfriend|gf|bf|kids?|child(?:ren)?|son|daughter|'
                   r'grandma|grandpa|grandmother|grandfather|grandson|granddaughter|sister|brother|friend|best friend|bestie|'
                   r'fianc[eé]e?|partner|her|him|boss|coworker|teacher|baby|parents?|couple|lover|crush|someone|someone special)\b')
SONG_FOR = re.compile(r'song (?:for|to|about|dedicated to) |songs? (?:for|to) (?:my|your|a) |for (?:my )?(?:wife|husband|mom|dad|girlfriend|boyfriend)')
GIFT_CORE = re.compile(r'custom(?:ized|ised)? (?:made )?(?:love |ai |gift |country |christian |rap |)?songs?|songs? custom|personali[sz]ed (?:music|songs?)|'
                       r'song gift|gift (?:a )?song|gift song|songs? as (?:a )?gift|song for someone|songs? (?:written|made) (?:for|about) (?:you|me|someone)|'
                       r'(?:make|create|write|order|commission|get|buy) (?:a |me a |my own |your own )?(?:custom |personal |personalized |original )?song (?:for|about|made)|'
                       r'write me a song|(?:write|make) a song for me|hire (?:a )?(?:songwriter|musician)|songwriter for hire|custom song|personalized song|'
                       r'song (?:for|about) (?:my|your|someone)|have a song (?:written|made)|song writing service|custom songwriting|'
                       r'how to (?:create|make) a (?:personali[sz]ed|custom) song')
GIFT_INTENT = re.compile(r'custom|personali[sz]|gift|\bmake\b|\bcreate\b|\bwrite\b|written|generator|\bai\b|maker|creator|service|order|'
                         r'commission|\bhire\b|company|website|cost|price|how much|cheap|\bget a\b|made for|with name|send')
AI_GEN = re.compile(r'(?:song|music|songs|lyrics?\s+to\s+song|text\s+to\s+song)\s*(?:generator|maker|creator|writer|ai)|'
                    r'ai (?:song|music)|song ai|text to song|lyrics to song|make (?:a )?songs? with ai|create (?:a )?songs? with ai|'
                    r'generate (?:a )?song|song generat|songwriting ai|ai songwriter|song creator')
NAME_STOP = set('''song songs to you with custom customized personalized mp3 audio video wishes wish card cake images image gif day
birthday anniversary dear the a for my your our hindi tamil telugu love happy funny traditional slow dj epic rock turbo one two 1 2 3 123
music free download name names ji ki ke ka wale real new latest mummy papa mom dad mother father son daughter sister brother friend wife husband
grandson granddaughter grandma grandpa baby boss uncle aunt in on and or celebration day's bday wishing jesus god videomp3 ai make com make making create edit play send generator maker app online custom grandson granddaughter twins girl boy kids kid'''.split())
NAME_PAT = re.compile(r'happy (?:birthday|bday) ([a-z]+) (?:song|to)')


def classify(k):
    """returns (cluster, reason, brand, brand_type, gift_intent)"""
    brand, btype = None, None
    for b, (p, t) in BRANDS.items():
        if p.search(k):
            brand, btype = b, t
            break
    gift = bool(GIFT_INTENT.search(k))
    # --- NOISE rules (explicit, in order)
    if NOISE_ENTITY.search(k):
        return 'NOISE', 'N1 famous song/artist/game/franchise/non-personal anniversary', brand, btype, gift
    if SPOTIFY_HOWTO.search(k):
        return 'NOISE', 'N2 platform how-to (add custom song to Spotify/IG/alarm, game song ids)', brand, btype, gift
    if MERCH.search(k) and not brand and re.search(r'custom|personali|gift|song art|lyric', k):
        return 'OTHER_RELEVANT', 'merch: physical song keepsake (music box/plaque/art/card)', brand, btype, gift
    if LISTEN.search(k) and not LYRICS_OK.search(k):
        return 'NOISE', 'N3 listening/lyrics/regional-language/church/dance intent', brand, btype, gift
    if MEDIA.search(k) and not PERSONAL.search(k) and not brand and not AI_GEN.search(k) and not MERCH.search(k):
        return 'NOISE', 'N4 media/download/reels/"latest" consumption without personalization', brand, btype, gift
    if 'generator' in k or ' ai' in f' {k}' or 'maker' in k:
        if AI_OFF.search(k) and not re.search(r'birthday|anniversary|wedding|mother|father|valentin|christmas|custom|personal', k):
            return 'NOISE', 'N5 AI tool off-target (cover/voice clone/lyrics-only/title/video/parody/how-to)', brand, btype, gift
    # --- relevant clusters (precedence order)
    if brand:
        return 'BRAND_COMPETITOR', 'brand:' + brand, brand, btype, gift
    m = NAME_PAT.search(k)
    if m and m.group(1) not in NAME_STOP and not m.group(1).isdigit() and not re.match(r'\d', m.group(1)) \
            and not re.match(r'(?:\d+(?:st|nd|rd|th))$', m.group(1)):
        return 'NAMES_PROGRAMMATIC', 'name:' + m.group(1), brand, btype, gift
    if MERCH.search(k):
        return 'OTHER_RELEVANT', 'merch: physical song keepsake (music box/plaque/art/card)', brand, btype, gift
    if re.search(r'birthday|bday', k):
        return 'BIRTHDAY_NAME', 'birthday', brand, btype, gift
    for n, p in OCC:
        if p.search(k):
            return n, 'occasion', brand, btype, gift
    if RECIP.search(k) and (SONG_FOR.search(k) or GIFT_CORE.search(k) or 'love song' in k):
        return 'RECIPIENT', 'recipient', brand, btype, gift
    if GIFT_CORE.search(k):
        return 'GIFT_CORE', 'gift_core', brand, btype, gift
    if AI_GEN.search(k) or re.search(r'\bai\b.*\bsongs?\b|\bsongs?\b.*\bai\b', k):
        return 'AI_GENERATOR', 'ai_generator', brand, btype, gift
    if re.search(r'generator|maker|creator', k):
        return 'AI_GENERATOR', 'generator (non-AI wording)', brand, btype, gift
    if RECIP.search(k):
        return 'RECIPIENT', 'recipient (weak)', brand, btype, gift
    return 'NOISE', 'N6 unmatched / no gift, occasion, recipient or creation signal', brand, btype, gift


for x in rows:
    x['cluster'], x['reason'], x['brand'], x['brand_type'], x['gift'] = classify(x['kw'])

# --------------------------------------------------------------- metrics
CL_ORDER = ['GIFT_CORE', 'BIRTHDAY_NAME'] + [n for n, _ in OCC] + ['RECIPIENT', 'AI_GENERATOR', 'BRAND_COMPETITOR',
            'NAMES_PROGRAMMATIC', 'OTHER_RELEVANT', 'NOISE']


def growth(rs):
    a = sum(sum(r['trend'][:12]) for r in rs)
    b = sum(sum(r['trend'][12:]) for r in rs)
    return (b / a - 1) * 100 if a else None, a, b


def growth_lfl(rs):
    rs = [r for r in rs if sum(r['trend'][:12]) > 0]
    return growth(rs)[0]


ANOMALY = 'how to create a personalized song gift'


def tp_dedup(rs):
    best = {}
    for r in rs:
        key = (r['Parent Keyword'].strip().lower() or r['kw'])
        best[key] = max(best.get(key, 0), r['tp'])
    return sum(best.values()), len(best)


def wcpc(rs):
    w = [(r['cpc'], r['vol']) for r in rs if r['cpc'] is not None and r['vol']]
    s = sum(v for _, v in w)
    return sum(c * v for c, v in w) / s if s else None


def mkd(rs, weighted=False):
    k = [r['kd'] for r in rs if r['kd'] is not None]
    return statistics.median(k) if k else None


def f(v, d=1, pct=False):
    if v is None:
        return 'n/a'
    if pct:
        return f'{v:+.0f}%'
    if isinstance(v, float):
        return f'{v:.{d}f}'
    return f'{v:,}'


by = collections.defaultdict(list)
for x in rows:
    by[x['cluster']].append(x)

out = []
P = out.append
csvrows = []
P('# US keyword demand — AI personalized song gifts (Ahrefs Matching terms, US)\n')
P(f'Source: `seo/raw/us.tsv`, {len(rows):,} rows, all country=us. SV trend window Nov-2024 → Oct-2026. Generated by `us_analysis.py`.\n')
tot_vol = sum(x['vol'] for x in rows)
nz = sum(1 for x in rows if x['vol'])
P('## Key conclusions (US)\n')
P('- **Gift-intent demand is small but growing fast.** GIFT_CORE+BIRTHDAY_NAME+OCCASION_*+RECIPIENT ≈ 16.4k/mo (14.7k excl. one anomalous query); explicitly custom/personalized/AI wording ≈ 10k/mo. Like-for-like 12-mo growth +23%; GIFT_CORE alone +98% LFL (custom song gift +71%, personalized song gift +89%, custom song +50%).')
P('- **The money terms are hard; the birthday/occasion tail is easy.** GIFT_CORE median KD 52 (custom song gift KD 68, CPC $3.50; personalized song gift KD 64, $4.50) — Songfinch owns the SERP. BIRTHDAY_NAME and OCCASION_* have median KD 0–1 but CPC <$1 (mostly free/listen intent).')
P('- **AI_GENERATOR is 73k/mo (72% of relevant volume) but is a tool market, KD 73, CPC $0.79, declining −10%.** Not gift demand; only the low-KD "best (free) ai song generator" listicle terms are attackable.')
P('- **Branded: Songfinch ~4.6k/mo (−17% YoY), Songlorious ~1.7k/mo (+20%), Udio/Mozart/Mureka small but growing; GiftSong, CustomSong, MakeCustomSongs, Birthdai, Wondera have no US rows.** Songfinch decline + rising generic custom-song queries suggests demand is shifting from the incumbent brand to generic/AI-priced alternatives.')
P('- **Seasonality:** Mother\'s Day (May) and Father\'s Day (June) are ~9–10× their monthly average; anniversary/wedding/recipient peak Dec–Feb (Valentine window); BIRTHDAY_NAME is flat (peak/trough 1.6×) — the evergreen base.')
P('- **Programmatic names:** this export has essentially no `happy birthday <name> song` rows (seed artifact); the "… song with name" template is ~2.4k/mo at KD 0–12. Needs a dedicated name-seeded export to size.\n')
P('## 0. Data notes & caveats\n')
P(f'- Total Ahrefs volume across all {len(rows):,} rows: **{tot_vol:,}/mo**. Only **{nz:,} rows ({nz/len(rows):.0%}) have a non-empty volume**; the rest are long-tail (<10/mo, blank in export) and are counted as 0 in volume sums but their SV-trend arrays are still used for growth/seasonality.')
P('- One head term dominates: `ai song generator` (52,000) is ~45% of all volume — always read AI_GENERATOR separately from gift-intent clusters.')
nokd = sum(1 for x in rows if x['vol'] and x['kd'] is None)
P(f'- {nokd} of {nz} rows with volume have **no KD** (Ahrefs has not computed it); they are excluded from KD medians and from the "low-KD" list (listed separately).')
P('- Ahrefs volumes are rounded modelled estimates (buckets 10/20/…/100/150/…); sums of many long-tail rows overstate precision. Growth figures use the SV-trend arrays (sum of last 12 months vs prior 12), which differ from Ahrefs\' own "Growth (12mo)" column.')
P('- Traffic potential (TP) is a *parent-topic* metric: many keywords share one parent and repeat the same TP. TP is therefore **deduplicated by Parent Keyword within each cluster** (max TP per parent; rows without a parent use their own TP). Parents often point outside the niche (e.g. `songfinch` → parent "how to create a personalized song gift"; `custom song gift` → parent `songfinch`), so TP is a ceiling of what the best page could capture, not additive demand.\n')

P('## 1. Cleaning rules (NOISE)\n')
P('Applied in order; first match wins. Keywords are lower-cased.\n')
P('| Rule | Definition | Rows | Volume |')
P('|---|---|---:|---:|')
nr = collections.defaultdict(list)
for x in by['NOISE']:
    nr[x['reason']].append(x)
for k in sorted(nr):
    P(f"| {k.split(' ',1)[0]} | {k.split(' ',1)[1]} | {len(nr[k]):,} | {sum(x['vol'] for x in nr[k]):,} |")
P('\nDetails:\n')
P('- **N1** famous songs/artists/franchises/games: Flintstones, Giveon "Heartbreak Anniversary", Al Jolson, Cowboy Junkies, Beat Saber/FNF/Roblox/Guitar Hero custom songs, Song of Achilles, Hannah Montana, Genshin, BTS, etc., plus work/company/death anniversaries.')
P('- **N2** platform how-tos: "add custom song to Spotify/Instagram/alarm", "roblox custom song ids".')
P('- **N3** listening/consumption: lyrics (except "lyrics to song / custom lyrics" which is creation intent), karaoke, chords, ringtone, instrumental, regional-language terms (hindi, tamil, punjabi, kannada, spanish, korean…), church/LDS/worship, walk-up, dance, DJ.')
P('- **N4** media/download/reels/"latest"/"new 2025"/youtube/status/capcut unless a personalization signal is present ("with name", "custom", "personalized"). So `happy birthday song download with name` stays (BIRTHDAY_NAME) but `anniversary song mp3 download` is noise.')
P('- **N5** AI tools that are off-product: covers, voice cloning / "with my voice", celebrity, parody, mashup, vocaloid, lyrics-only generators, song name/title generators, video generators, Suno/Udio UI how-tos — unless an occasion/custom word is present.')
P('- **N6** catch-all: no gift, occasion, recipient, brand or creation signal (e.g. bare `anniversary song`-style variants already caught above, misc).')
P('\nNote: plain `happy anniversary song` / `mothers day song` / `fathers day song` (listening intent but occasion-specific) are **kept** in their OCCASION cluster and flagged by a `gift_intent` column; per-cluster tables below show both all-intent and gift-intent volume.\n')
top_noise = sorted(by['NOISE'], key=lambda x: -x['vol'])[:15]
P('Top noise keywords by volume: ' + ', '.join(f"`{x['kw']}` ({x['vol']}, {x['reason'].split()[0]})" for x in top_noise) + '\n')

P('## 2. Cluster summary\n')
P('| Cluster | Keywords | w/ volume | Volume/mo | Gift-intent vol | TP (dedup by parent) | Parents | Median KD | Wtd CPC $ | 12mo growth (SV trend) | LFL growth* |')
P('|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|')
summary = {}
for c in CL_ORDER:
    rs = by.get(c, [])
    if not rs:
        P(f'| {c} | 0 | 0 | 0 | 0 | 0 | 0 | n/a | n/a | n/a | n/a |')
        summary[c] = dict(n=0, vol=0)
        continue
    g, a, b = growth(rs)
    tp, npar = tp_dedup(rs)
    vol = sum(x['vol'] for x in rs)
    gv = sum(x['vol'] for x in rs if x['gift'])
    summary[c] = dict(lfl=growth_lfl(rs), n=len(rs), nvol=sum(1 for x in rs if x['vol']), vol=vol, giftvol=gv, tp=tp, parents=npar, kd=mkd(rs), cpc=wcpc(rs), growth=g,
                      prior12=a, last12=b)
    s = summary[c]
    P(f"| {c} | {s['n']:,} | {s['nvol']:,} | {vol:,} | {gv:,} | {tp:,} | {npar:,} | {f(s['kd'])} | {f(s['cpc'],2)} | {f(g,pct=True)} | {f(s['lfl'],pct=True)} |")
rel = [c for c in CL_ORDER if c != 'NOISE']
core = ['GIFT_CORE', 'BIRTHDAY_NAME'] + [n for n, _ in OCC] + ['RECIPIENT']
for label, cs in [('All relevant (excl. NOISE)', rel), ('Gift demand core (GIFT_CORE+BIRTHDAY_NAME+OCCASION_*+RECIPIENT)', core)]:
    rs = [x for c in cs for x in by.get(c, [])]
    g, _, _ = growth(rs)
    tp, npar = tp_dedup(rs)
    P(f"| **{label}** | {len(rs):,} | {sum(1 for x in rs if x['vol']):,} | {sum(x['vol'] for x in rs):,} | {sum(x['vol'] for x in rs if x['gift']):,} | {tp:,} | {npar:,} | {f(mkd(rs))} | {f(wcpc(rs),2)} | {f(g,pct=True)} | {f(growth_lfl(rs),pct=True)} |")
rs = [x for c in core for x in by.get(c, []) if x['kw'] != ANOMALY]
P(f"| Gift demand core **excl. anomaly** `{ANOMALY}` | {len(rs):,} | | {sum(x['vol'] for x in rs):,} | | | | | | {f(growth(rs)[0],pct=True)} | {f(growth_lfl(rs),pct=True)} |")
P('\n*LFL (like-for-like) growth = only keywords that already had SV in the prior 12 months (Nov-24→Oct-25); removes the "new keyword appears in Ahrefs" effect that inflates raw growth (e.g. RECIPIENT, GIFT_CORE).\n')
P(f'**Anomaly:** `{ANOMALY}` (1,700/mo, KD 68, first seen 2026-02-22) has SV 0 until Feb-2026 then spikes to 10,543 in May-2026 and 5,995 in Sep-2026 — looks like a synthetic / AI-assistant-driven or bot query, not organic demand. It alone accounts for most of GIFT_CORE\'s raw growth and May/Sep peaks; it is kept in GIFT_CORE but reported with and without it.\n')
P('\n"Gift-intent vol" = volume of keywords containing custom/personalized/gift/make/create/write/generator/ai/maker/service/cost/price/with name/etc.\n')

P('## 3. Top keywords per cluster\n')
for c in CL_ORDER:
    rs = sorted(by.get(c, []), key=lambda x: (-x['vol'], x['kw']))
    if not rs:
        continue
    P(f'### {c}\n')
    s = summary[c]
    P(f"{s['n']:,} keywords · {s['vol']:,}/mo · TP(dedup) {s['tp']:,} · median KD {f(s['kd'])} · wtd CPC ${f(s['cpc'],2)} · 12mo growth {f(s['growth'],pct=True)} (prior-12 SV sum {s['prior12']:,} → last-12 {s['last12']:,})\n")
    P('| Keyword | Volume | KD | CPC $ | TP | Parent | 12mo growth |')
    P('|---|---:|---:|---:|---:|---|---:|')
    for x in rs[:10]:
        g, _, _ = growth([x])
        P(f"| {x['kw']} | {x['vol']:,} | {f(x['kd'])} | {f(x['cpc'],2)} | {x['tp']:,} | {x['Parent Keyword']} | {f(g,pct=True)} |")
    P('')

# NAMES_PROGRAMMATIC analysis
P('### NAMES_PROGRAMMATIC — programmatic SEO read\n')
nm = by.get('NAMES_PROGRAMMATIC', [])
names = collections.Counter(x['reason'].split(':')[1] for x in nm)
withname = [x for x in rows if PERSONAL.search(x['kw']) and re.search(r'birthday|bday|anniversary', x['kw']) and 'name' in x['kw']]
P(f"- Keywords with a specific first name (\"happy birthday <name> …\"): **{len(nm)}** rows, **{sum(x['vol'] for x in nm):,}/mo** total. Names found: {', '.join(sorted(names)) or 'none'}.")
P(f"- Generic template \"… song with name\" variants (all clusters incl. noise): **{len(withname)}** rows, **{sum(x['vol'] for x in withname):,}/mo**; non-noise: {sum(1 for x in withname if x['cluster']!='NOISE')} rows / {sum(x['vol'] for x in withname if x['cluster']!='NOISE'):,}/mo.")
P('- This export was seeded on "song" matching terms, so it **does not contain** the classic `happy birthday <name>` name long tail (e.g. "happy birthday sarah song") at scale — the near-absence here is an artifact of the seed, not proof of no demand. Sizing programmatic name pages needs a separate export (seed "happy birthday" + name list). The generic "with name" template demand (~1–2k/mo, KD 0–12) is low-competition and is the real evidence of the pattern.\n')

# --------------------------------------------------------------- seasonality
P('## 4. Seasonality (SV trend, Nov-2024 → Oct-2026)\n')
groups = [('Gift core: GIFT_CORE+BIRTHDAY_NAME+OCCASION_*', ['GIFT_CORE', 'BIRTHDAY_NAME'] + [n for n, _ in OCC]),
          ('GIFT_CORE', ['GIFT_CORE']), ('BIRTHDAY_NAME', ['BIRTHDAY_NAME']), ('OCCASION_anniversary', ['OCCASION_anniversary']),
          ('OCCASION_wedding', ['OCCASION_wedding']), ('OCCASION_mothers_day', ['OCCASION_mothers_day']),
          ('OCCASION_fathers_day', ['OCCASION_fathers_day']), ('OCCASION_valentines', ['OCCASION_valentines']),
          ('OCCASION_christmas', ['OCCASION_christmas']), ('RECIPIENT', ['RECIPIENT']), ('AI_GENERATOR', ['AI_GENERATOR']),
          ('BRAND_COMPETITOR', ['BRAND_COMPETITOR'])]
groups.insert(1, ('Gift core excl. anomaly', ['GIFT_CORE', 'BIRTHDAY_NAME'] + [n for n, _ in OCC]))
groups.insert(3, ('GIFT_CORE excl. anomaly', ['GIFT_CORE']))
series = {}
for lab, cs in groups:
    rs = [x for c in cs for x in by.get(c, []) if not ('excl. anomaly' in lab and x['kw'] == ANOMALY)]
    series[lab] = [sum(x['trend'][i] for x in rs) for i in range(24)]
P('Monthly SV sum (all keywords in group):\n')
P('| Month | ' + ' | '.join(l.split(':')[0] for l, _ in groups) + ' |')
P('|---|' + '---:|' * len(groups))
for i, m in enumerate(MONTHS):
    P(f'| {m} | ' + ' | '.join(f'{series[l][i]:,}' for l, _ in groups) + ' |')
P('\nPeak / trough on the last 12 months (Nov-2025 → Oct-2026):\n')
P('| Group | Peak month | Peak SV | Trough month | Trough SV | Peak/trough | Peak / 12-mo avg | Top-3 months |')
P('|---|---|---:|---|---:|---:|---:|---|')
for lab, _ in groups:
    s = series[lab][12:]
    mo = MONTHS[12:]
    if not sum(s):
        continue
    pi = max(range(12), key=lambda i: s[i]); ti = min(range(12), key=lambda i: s[i])
    top3 = sorted(range(12), key=lambda i: -s[i])[:3]
    P(f"| {lab} | {mo[pi]} | {s[pi]:,} | {mo[ti]} | {s[ti]:,} | {f(s[pi]/s[ti] if s[ti] else None,1)}x | {s[pi]/(sum(s)/12):.2f}x | {', '.join(mo[i] for i in top3)} |")
P('')

# --------------------------------------------------------------- opportunities
P('## 5. Opportunities\n')
REL = set(rel)
BRAND_BUYER = re.compile(r'cost|price|pricing|review|alternative|\\bvs\\b|legit|worth it|competitor|cheaper|sites like|how much')
def COMMERCIAL(x):
    if x['cluster'] == 'BRAND_COMPETITOR' and not BRAND_BUYER.search(x['kw']):
        return False  # navigational brand / shark-tank / net-worth queries are not rankable buyer intent
    return 'Commercial' in x['Intents'] or 'Transactional' in x['Intents'] or bool(x['gift'])
P('### 5a. Low-KD (≤20), volume ≥100, commercial/gift intent\n')
cand = [x for x in rows if x['cluster'] in REL and x['kd'] is not None and x['kd'] <= 20 and x['vol'] >= 100 and COMMERCIAL(x)]
cand.sort(key=lambda x: (-x['vol'], x['kd']))
P(f'Only **{len(cand)}** keywords meet the strict filter (KD≤20, vol≥100, commercial/gift intent, non-noise; brand rows only if comparison/price/review intent — `songfinch`/`songlorious` navigational, shark-tank and net-worth queries excluded). To reach 30, the list is extended with vol 50–90 (marked ‡) and then KD-unknown rows with vol ≥100 (marked †; KD not computed by Ahrefs = usually low competition, verify SERP).\n')
ext = [x for x in rows if x['cluster'] in REL and x['kd'] is not None and x['kd'] <= 20 and 50 <= x['vol'] < 100 and COMMERCIAL(x)]
ext.sort(key=lambda x: (-x['vol'], x['kd']))
unk = [x for x in rows if x['cluster'] in REL and x['kd'] is None and x['vol'] >= 100 and COMMERCIAL(x)]
unk.sort(key=lambda x: -x['vol'])
lst = [(x, '') for x in cand] + [(x, '‡') for x in ext] + [(x, '†') for x in unk]
gift_first = sorted(lst[:], key=lambda t: (t[1] != '', t[0]['cluster'] == 'AI_GENERATOR', -t[0]['vol']))
P('| # | Keyword | Cluster | Volume | KD | CPC $ | TP | 12mo growth | Intents |')
P('|---:|---|---|---:|---:|---:|---:|---:|---|')
for i, (x, m) in enumerate(gift_first[:30], 1):
    g, _, _ = growth([x])
    P(f"| {i} | {x['kw']} {m} | {x['cluster']} | {x['vol']:,} | {f(x['kd'])} | {f(x['cpc'],2)} | {x['tp']:,} | {f(g,pct=True)} | {x['Intents'].replace(',Non-local','').replace('Non-branded','NB')} |")
P('\nOrdering: gift/occasion clusters first, AI_GENERATOR after, then by volume.\n')

P('### 5b. Fastest-growing relevant keywords (volume ≥100, SV-trend last-12 vs prior-12)\n')
gr = []
for x in rows:
    if x['cluster'] in REL and x['vol'] >= 100:
        g, a, b = growth([x])
        if g is not None and a >= 120:
            gr.append((g, x, a, b))
gr.sort(key=lambda t: -t[0])
P('| # | Keyword | Cluster | Volume | KD | CPC $ | Prior-12 SV | Last-12 SV | Growth | Ahrefs Growth(12mo) |')
P('|---:|---|---|---:|---:|---:|---:|---:|---:|---:|')
for i, (g, x, a, b) in enumerate(gr[:20], 1):
    P(f"| {i} | {x['kw']} | {x['cluster']} | {x['vol']:,} | {f(x['kd'])} | {f(x['cpc'],2)} | {a:,} | {b:,} | {f(g,pct=True)} | {x['Growth (12mo)'] or 'n/a'} |")
P('\n(Requires prior-12 SV sum ≥120 to avoid infinite growth from near-zero bases.)\n')

P('### 5c. CPC as intent / acquisition-cost signal\n')
cp = sorted([x for x in rows if x['cluster'] in REL and x['cpc'] is not None and x['vol'] >= 20], key=lambda x: -x['cpc'])[:15]
P('| Keyword | Cluster | Volume | CPC $ | KD |')
P('|---|---|---:|---:|---:|')
for x in cp:
    P(f"| {x['kw']} | {x['cluster']} | {x['vol']:,} | {f(x['cpc'],2)} | {f(x['kd'])} |")
P('')

# --------------------------------------------------------------- brands
P('## 6. Branded demand\n')
P('All rows matching each brand pattern, **regardless of cluster** (so brand+cover/how-to rows that were classified NOISE are still counted here). Monthly volume = sum of Ahrefs Volume; trend from SV-trend arrays.\n')
P('| Brand | Type | Keywords | Volume/mo | Head term (vol) | Prior-12 SV | Last-12 SV | 12mo growth | Last-3-mo avg vs same 3 mo prior yr | Wtd CPC $ |')
P('|---|---|---:|---:|---|---:|---:|---:|---:|---:|')
bstats = []
for b, (p, t) in BRANDS.items():
    rs = [x for x in rows if p.search(x['kw'])]
    if not rs:
        continue
    g, a, bb = growth(rs)
    l3 = sum(sum(x['trend'][21:24]) for x in rs); p3 = sum(sum(x['trend'][9:12]) for x in rs)
    head = max(rs, key=lambda x: x['vol'])
    bstats.append((sum(x['vol'] for x in rs), b, t, rs, g, a, bb, l3, p3, head))
bstats.sort(key=lambda t: -t[0])
for v, b, t, rs, g, a, bb, l3, p3, head in bstats:
    P(f"| {b} | {t} | {len(rs)} | {v:,} | {head['kw']} ({head['vol']:,}) | {a:,} | {bb:,} | {f(g,pct=True)} | {f((l3/p3-1)*100 if p3 else None,pct=True)} | {f(wcpc(rs),2)} |")
P('\nNot found in this export (0 rows): ' + ', '.join(b for b in BRANDS if b not in {t[1] for t in bstats}) + '.\n')
P('Monthly SV for the main brands:\n')
main = [t for t in bstats if t[1] in ('songfinch', 'songlorious', 'suno', 'udio', 'giftsong', 'customsong', 'birthdai', 'wondera', 'freebeat', 'mureka', 'foreversongs')]
P('| Month | ' + ' | '.join(t[1] for t in main) + ' |')
P('|---|' + '---:|' * len(main))
for i, m in enumerate(MONTHS):
    P(f'| {m} | ' + ' | '.join(f"{sum(x['trend'][i] for x in t[3]):,}" for t in main) + ' |')
P('')
P('Note: Suno brand volume here is only "song"-containing Suno queries (e.g. `suno ai song generator`); the navigational `suno` / `suno ai` head terms are not in this export, so true Suno brand demand is far larger.\n')

open(os.path.join(S, 'us_report.md'), 'w', encoding='utf-8').write('\n'.join(out))

# per-cluster CSV (summary) + keyword-level CSV
with open(os.path.join(S, 'us_clusters.csv'), 'w', newline='', encoding='utf-8') as fh:
    w = csv.writer(fh)
    w.writerow(['market', 'cluster', 'keywords', 'keywords_with_volume', 'volume', 'gift_intent_volume', 'traffic_potential_dedup_by_parent',
                'distinct_parents', 'median_kd', 'weighted_cpc', 'sv_prior12', 'sv_last12', 'growth_12mo_pct', 'growth_12mo_lfl_pct', 'top10_keywords'])
    for c in CL_ORDER:
        s = summary.get(c, {})
        if not s.get('n'):
            w.writerow(['us', c, 0, 0, 0, 0, 0, 0, '', '', 0, 0, '', '', '']); continue
        top = sorted(by[c], key=lambda x: -x['vol'])[:10]
        w.writerow(['us', c, s['n'], s['nvol'], s['vol'], s['giftvol'], s['tp'], s['parents'], s['kd'], round(s['cpc'], 2) if s['cpc'] else '',
                    s['prior12'], s['last12'], round(s['growth'], 1) if s['growth'] is not None else '', round(s['lfl'], 1) if s['lfl'] is not None else '',
                    '; '.join(f"{x['kw']} ({x['vol']}|KD {x['kd'] if x['kd'] is not None else 'na'}|${x['cpc'] if x['cpc'] is not None else 'na'})" for x in top)])
with open(os.path.join(S, 'us_keywords_classified.csv'), 'w', newline='', encoding='utf-8') as fh:
    w = csv.writer(fh)
    w.writerow(['keyword', 'cluster', 'reason', 'brand', 'brand_type', 'gift_intent', 'volume', 'kd', 'cpc', 'traffic_potential', 'parent_keyword',
                'intents', 'sv_prior12', 'sv_last12'])
    for x in sorted(rows, key=lambda x: (x['cluster'], -x['vol'])):
        w.writerow([x['kw'], x['cluster'], x['reason'], x['brand'] or '', x['brand_type'] or '', int(x['gift']), x['vol'], x['kd'] if x['kd'] is not None else '',
                    x['cpc'] if x['cpc'] is not None else '', x['tp'], x['Parent Keyword'], x['Intents'], sum(x['trend'][:12]), sum(x['trend'][12:])])
print('ok')
for c in CL_ORDER:
    s = summary.get(c, {})
    print(c, s.get('n'), s.get('vol'))
