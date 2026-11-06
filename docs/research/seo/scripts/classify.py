"""Keyword classifier for the global Ahrefs export (shared taxonomy with US analysis).

Taxonomy: GIFT_CORE, BIRTHDAY_NAME, OCCASION_<x>, RECIPIENT, AI_GENERATOR, BRAND_COMPETITOR,
NAMES_PROGRAMMATIC, OTHER_RELEVANT, NOISE.

Rule order (first match wins):
 1. NOISE  - famous songs/artists/franchises, celebrity AI voice, tool queries unrelated to gifting
             (cover, voice clone, remix, mashup, video, apk, song-name generator), physical merch
             (plaque/wall art/music box/canvas), and "listening" queries (mp3/download/status/lyrics/
             capcut/karaoke/ringtone/for kids/church...) that have NO personalization marker.
 2. BRAND_COMPETITOR - gift-song brands (Songfinch, Songlorious, ForeverSongs, GiftSong, RU clones...)
 3. Occasion detected (multilingual):
      birthday + specific person name  -> NAMES_PROGRAMMATIC
      birthday + (name|custom|ai|create...) -> BIRTHDAY_NAME
      birthday without personalization -> NOISE (generic happy-birthday listening)
      other occasion -> OCCASION_<x>  (flag `explicit` if personalization marker present)
 4. GIFT_CORE - custom/personalized song, song gift, song on order (multilingual)
 5. RECIPIENT - song for wife/husband/mom/... (no occasion)
 6. AI_GENERATOR - generic AI song/music generators (incl. Suno/Udio brand queries, RU "нейросеть")
 7. OTHER_RELEVANT - anything else mentioning song/music creation; otherwise NOISE.
"""
import re

def has(text, pats):
    return any(re.search(p, text) for p in pats)

# ---------- language detection ----------
SCRIPT_RANGES = [
    ('ru', r'[Ѐ-ӿ]'), ('ja', r'[぀-ヿ]'), ('ko', r'[가-힯]'),
    ('zh', r'[一-鿿]'), ('ar', r'[؀-ۿ]'), ('hi', r'[ऀ-ॿ]'),
    ('th', r'[฀-๿]'), ('he', r'[֐-׿]'), ('el', r'[Ͱ-Ͽ]'),
    ('bn', r'[ঀ-৿]'), ('ta', r'[஀-௿]'),
]
LATIN_WORDS = {
    'es': ['canción', 'cancion', 'canciones', 'cumpleaños', 'cumpleanos', 'feliz', 'para', 'personalizada', 'personalizado',
           'regalo', 'mamá', 'madre', 'padre', 'esposa', 'esposo', 'boda', 'aniversario', 'navidad', 'crear', 'hacer',
           'con nombre', 'del', 'día', 'dia de la', 'novia', 'novio', 'generador de', 'canciones'],
    'pt': ['música', 'musica', 'aniversário', 'parabéns', 'parabens', 'presente', 'mãe', 'mae', 'pai', 'namorada',
           'namorado', 'casamento', 'personalizada', 'criar', 'fazer', 'com nome', 'dia das', 'dia dos', 'gerador de'],
    'de': ['lied', 'geburtstag', 'geburtstagslied', 'personalisiert', 'personalisiertes', 'geschenk', 'mama', 'hochzeit',
           'muttertag', 'vatertag', 'kostenlos', 'erstellen', 'mit namen', 'für', 'liedgenerator', 'jahrestag', 'ki '],
    'fr': ['chanson', 'anniversaire', 'joyeux', 'personnalisée', 'personnalisee', 'cadeau', 'fête', 'mariage', 'gratuit',
           'créer', 'avec prénom', 'générateur', 'pour'],
    'it': ['canzone', 'compleanno', 'buon', 'personalizzata', 'regalo', 'festa della', 'matrimonio', 'gratis',
           'generatore'],
    'nl': ['liedje', 'verjaardag', 'gefeliciteerd', 'cadeau', 'gratis', 'maken', 'met naam'],
    'pl': ['piosenka', 'urodziny', 'urodzin', 'sto lat', 'prezent', 'personalizowana', 'darmowy'],
    'tr': ['şarkı', 'sarki', 'doğum', 'dogum', 'günü', 'gunu', 'kişiye', 'özel', 'hediye', 'yapay zeka', 'anneler'],
    'id': ['lagu', 'ulang tahun', 'selamat', 'untuk', 'kado', 'hadiah', 'buat', 'membuat', 'gratis'],
    'tl': ['maligayang', 'kaarawan', 'kanta', 'para sa'],
    'vi': ['bài hát', 'sinh nhật', 'chúc mừng', 'tặng'],
    'hi-latn': ['janamdin', 'janmdin', 'janmadin', 'ke liye', 'ka song', 'ki song', 'wala', 'wali', 'gana', 'gaana',
                'mubarak', 'mummy papa', 'bhaiya', 'bhabhi', 'didi', 'dost', 'shaadi', 'saalgirah'],
    'da': ['dansk', 'sang', 'fødselsdag', 'gratis'],
    'sv': ['låt', 'födelsedag', 'gratis'],
}
# Ambiguous tokens resolved by country language
AMBIG = {'gratis', 'cadeau', 'regalo', 'para', 'mama', 'pour'}
COUNTRY_LANG = {
    'es': 'es', 'mx': 'es', 'ar': 'es', 'co': 'es', 'cl': 'es', 'pe': 'es', 'ec': 'es', 've': 'es', 'uy': 'es',
    'py': 'es', 'bo': 'es', 'cr': 'es', 'pa': 'es', 'do': 'es', 'gt': 'es', 'hn': 'es', 'sv': 'es', 'ni': 'es',
    'pr': 'es', 'cu': 'es', 'br': 'pt', 'pt': 'pt', 'ao': 'pt', 'mz': 'pt', 'de': 'de', 'at': 'de', 'ch': 'de',
    'fr': 'fr', 'be': 'fr', 'it': 'it', 'nl': 'nl', 'pl': 'pl', 'tr': 'tr', 'id': 'id', 'ph': 'tl', 'vn': 'vi',
    'dk': 'da', 'se': 'sv', 'no': 'no', 'fi': 'fi', 'ru': 'ru', 'by': 'ru', 'kz': 'ru', 'ua': 'uk',
}
LANG_NAMES = ['hindi', 'tamil', 'telugu', 'kannada', 'malayalam', 'marathi', 'bengali', 'bangla', 'punjabi', 'gujarati',
              'odia', 'assamese', 'urdu', 'nepali', 'sinhala', 'bhojpuri', 'pashto', 'tagalog', 'bisaya', 'spanish',
              'french', 'german', 'italian', 'portuguese', 'arabic', 'korean', 'japanese', 'chinese', 'afrikaans',
              'swahili', 'zulu', 'malay', 'indonesian', 'vietnamese', 'thai', 'russian', 'turkish', 'dansk',
              'bollywood', 'kpop', 'k-pop']


def detect_language(kw, country):
    for lang, rx in SCRIPT_RANGES:
        if re.search(rx, kw):
            if lang == 'ru' and re.search(r'[іїєґ]', kw):
                return 'uk'
            return lang
    padded = f' {kw} '
    scores = {}
    for lang, words in LATIN_WORDS.items():
        for w in words:
            if w in AMBIG:
                continue
            if re.search(r'(?<![a-zà-ÿ])' + re.escape(w.strip()) + r'(?![a-zà-ÿ])', padded):
                scores[lang] = scores.get(lang, 0) + 1
    if scores:
        return max(scores, key=scores.get)
    toks = set(re.findall(r"[a-zà-ÿ]+", kw))
    if toks & AMBIG:
        cl = COUNTRY_LANG.get(country)
        if cl and cl not in ('en',):
            return cl
        return 'xx-latin'
    return 'en'


def lang_modifier(kw):
    for ln in LANG_NAMES:
        if re.search(r'\b' + re.escape(ln) + r'\b', kw):
            return {'bangla': 'bengali', 'k-pop': 'kpop'}.get(ln, ln)
    return ''

# ---------- classification patterns ----------
PERSONAL = [r'\bwith (my |his |her |their |your )?name', r'\bname\b', r'\bnames\b', r'custom', r'personali[sz]', r'\bai\b',
            r'creat', r'\bmake\b', r'\bmaker\b', r'\bmaking\b', r'generat', r'\bgift', r'\bwrit', r'commission',
            r'\border\b', r'\bfor (my|your) ', r'на заказ', r'заказ', r'именн', r'с именем', r'созда', r'сделать', r'написа',
            r'нейросет', r'в подарок', r'personalizad', r'personalisiert', r'personnalis', r'personalizzat',
            r'kişiye özel', r'nombre', r'\bnome\b', r'namen', r'prénom', r'\bnama\b', r'photo', r'नाम']

NOISE_FAMOUS = [r'flag raising', r'\bhk\b', r'national (day|song)', r'仮面', r'ガッチャマン', r'あんさんぶる', r'あかべぇ',
                r'tony toni', r'al jolson', r'eva cassidy', r'flintstone', r'call of the wild', r'excerpt', r'\bchords?\b',
                r'ukulele', r'guitar', r'piano', r'\btabs?\b', r'перевод', r'meaning', r'abochi', r'beat saber',
                r'moose ?wala', r'michael jackson', r'celebrit', r'walk ?up song', r'heartbreak anniversary',
                r'anniversary song by', r'tuska', r'樋口', r'大泉', r'再放送', r'歌詞', r'コード', r'おすすめ', r'theme song best',
                r"it'?s our anniversary", r'gagna', r'infinity', r'giveon', r'tum hi ho', r'\bmovie\b', r'\bfilm\b',
                r'\bepisode\b', r'\btiktok song\b', r'anniversary song.*(collection|album)', r'\bcadbury\b', r'drake',
                r'taylor swift', r'\bbts\b', r'beyonc', r'ed sheeran', r'\bsonu\b', r'arijit', r'mozart', r'kumar sanu',
                r'lata', r'kishore', r'atif', r'darshan', r'diljit', r'\bsidhu\b', r'\bjohn williamson\b', r'ryan tedder',
                r'thick and thin', r'qualon', r'custom (shop|night|character|paint|plates?|ids?|output|filename|theme)', r'sword art', r'roblox', r'spotdl', r'describes', r'game of thrones', r'wrestlemania', r'fender', r'washburn', r'parmish', r'bluey', r'steel panther', r'boyz', r'sesame', r'thomas rhett', r'willow smith', r'vicky', r'shawna', r'sawyer brown', r'song of solomon', r'dead as disco', r'divine song', r'what i.?ll do', r'@', r'https?:', r'excerpt']
NOISE_TOOL = [r'\bcovers?\b', r'кавер', r'voice ?clon', r'clone', r'\bmy voice\b', r'own voice', r'your voice',
              r'своим голосом', r'со своим голосом', r'\bremix', r'mashup', r'vocal remover', r'\bstems?\b',
              r'\bvideo generator', r'to video', r'video song generator', r'song video generator', r'клип', r'видео',
              r'downloader', r'\bapk\b', r'\bmod\b', r'مهكر', r'(song|title) name generator', r'song title generator',
              r'name generator', r'\bjobs?\b', r'careers?', r'layoffs', r'glassdoor', r'revenue', r'logo\b',
              r'artist application', r'become an artist', r'songfinch artists?\b', r'recording studio', r'login',
              r'sign in', r'contact number', r'company overview', r'\bdeepfake', r'\bstem splitter', r'lip ?sync',
              r'dance generator', r'\bscreen\b', r'interface', r'\bexample\b']
NOISE_MERCH = [r'plaque', r'wall art', r'canvas', r'\bprint', r'\bframe', r'music box', r'necklace', r'keychain',
               r'ornament', r'\bmug\b', r'blanket', r'pillow', r'spotify', r'\bposter', r'vinyl', r'record player',
               r'\bcards?\b', r'jewel', r'bracelet', r'beat saber', r'guitar hero', r'osu\b', r'cake']
LISTEN = [r'\bmp3\b', r'\bmp4\b', r'download', r'скачать', r'\bstatus\b', r'capcut', r'template', r'lyric', r'karaoke',
          r'ringtone', r'\baudio\b', r'\bvideo\b', r'female version', r'male version', r'bollywood', r'\bold\b',
          r'latest', r'\bnew\b', r'\blist\b', r'\bdj\b', r'instrumental', r'whatsapp', r'instagram', r'\breels?\b',
          r'\bkids?\b', r'kindergarten', r'preschool', r'toddler', r'nursery', r'church', r'\blds\b', r'worship',
          r'christian', r'hymn', r'gospel', r'prayer', r'\bsing\b', r'\bsung\b', r'\bplay\b', r'\bfree download',
          r'\bsong(s)? (list|ideas)\b', r'\bbest\b', r'\bgood\b', r'\btop\b', r'romantic', r'\bfunny\b', r'\b\d+(st|nd|rd|th)? anniversary song\b',
          r'\btraditional\b', r'\boriginal\b', r'\bversion\b', r'\bremix\b', r'\bmusic video\b', r'\bspotify\b',
          r'\bsong \d', r'^\d+ ', r'^(one|1|2|two) ', r'\bcom song']

BRANDS = {
    'songfinch': r'songfinch', 'songlorious': r'songlorious', 'foreversongs': r'forever ?songs', 'giftsong': r'gift ?song\.?ai|giftsong',
    'songfox': r'song ?fox', 'bunny': r'\bsongbunny', 'songwish': r'songwish', 'songsforgifts': r'songs ?for ?gifts',
    'personal song co': r'personal ?song ?(co|company)', 'ohappy': r'ohappy|о ?хэппи', 'everyonesing': r'everyone ?sing',
    'pesinka': r'pesinka|песинка', 'lyricgift': r'lyric ?gift', 'heartsong': r'heart ?song', 'songwriters for hire': r'songwriter.?s? for hire',
    'tune my love': r'tune ?my ?love', 'songcards': r'song ?cards?\b(?!.*birthday)', 'custom song gift co': r'\bsongcraft\b',
    'mysongtoyou': r'my ?song ?to ?you', 'sing a gram': r'sing.?a.?gram',
}
AI_BRANDS = r'suno|udio|mureka|soundverse|musely|insmelo|singify|topmediai|clipfly|musicful|voicemod|easeus|bandlab|' \
            r'makesong|jam ai|melody craft|brev ai|poppop|gemini|google ai|wondera|freebeat|musicmake|riffusion|' \
            r'boomy|soundraw|aiva|mubert|musicgpt|musichero|loudly|beatoven|tunee|songer|donna|lalals|vocal ?ai|' \
            r'covers\.ai|music ?ai|kits\.ai|elevenlabs|chatgpt|canva|meta ai|grok|copilot|stable audio'

OCCASIONS = [
    ('memorial', [r'death anniversary', r'funeral', r'memorial', r'in memory', r'\brip\b', r'tribute', r'celebration of life',
                  r'passed away', r'condolenc', r'barsi', r'поминк', r'памят', r'en memoria', r'heaven']),
    ('mothers_day', [r"mother'?s'? ?day", r"mom'?s'? day", r'mothersday', r'день матери', r'dia das m[ãa]es', r'd[ií]a de la madre',
                     r'muttertag', r'f[êe]te des m[èe]res', r'festa della mamma', r'anneler g[üu]n[üu]', r'hari ibu', r'moederdag', r'dzień matki']),
    ('fathers_day', [r"father'?s'? ?day", r"dad'?s'? day", r'день отца', r'dia dos pais', r'd[ií]a del padre', r'vatertag',
                     r'f[êe]te des p[èe]res', r'festa del pap[àa]', r'babalar g[üu]n[üu]', r'hari ayah', r'vaderdag']),
    ('valentines', [r'valentin', r'день влюбл', r'san valent', r'dia dos namorados', r'saint.?valentin']),
    ('christmas', [r'christmas', r'xmas', r'рождеств', r'новогод', r'новый год', r'navidad', r'\bnatal\b', r'weihnacht', r'no[ëe]l', r'natale']),
    ('retirement', [r'retire', r'пенси', r'jubilaci', r'ruhestand', r'retraite']),
    ('graduation', [r'graduat', r'выпускн', r'graduaci', r'formatura', r'abschluss', r'\bconvocation']),
    ('wedding', [r'wedding(?! anniversary)', r'свадьб', r'\bboda\b', r'casamento', r'hochzeit(?!stag)', r'\bmariage\b(?!.*anniv)',
                 r'matrimonio', r'bruiloft', r'engagement(?! anniversary)', r'first dance', r'bridal', r'bride', r'groom',
                 r'walk(ing)? down the aisle', r'shaadi', r'nikah', r'reception']),
    ('anniversary', [r'anniversar', r'годовщин', r'aniversario', r'jahrestag', r'hochzeitstag', r'yıldönümü', r'yildonumu',
                     r'anniversario', r'anniversaire de mariage', r'saalgirah', r'ulang tahun pernikahan', r'trouwdag']),
    ('other', [r'baby shower', r'gender reveal', r'teacher', r'proposal', r'propose', r'bachelor', r'bar mitzvah', r'bat mitzvah',
               r'quincea', r'\beid\b', r'diwali', r'raksha', r'rakhi', r'karva', r'thanksgiving', r'easter', r'8 марта',
               r'день учителя', r'new year', r'friendship day', r'women.?s day', r'siblings day', r'grandparents day',
               r'farewell', r'housewarming', r'baptism', r'christening', r'newborn', r'baby', r'get well', r'apology', r'sorry',
               r'promotion', r'congratulat', r'поздравл', r'\bholi\b', r'lohri', r'onam', r'pongal', r'birth of']),
]
BIRTHDAY = [r'birthday', r'\bb-?day\b', r'день рождени', r'днем рождени', r'днём рождени', r'юбиле', r'cumplea[ñn]os',
            r'anivers[áa]rio', r'parab[ée]ns', r'geburtstag', r'(?<!de mariage )anniversaire(?! de mariage)', r'compleanno',
            r'verjaardag', r'urodzin', r'doğum g', r'dogum g', r'ulang tahun(?! pernikahan)', r'janam ?din', r'janm(a)?din',
            r'kaarawan', r'sinh nhật', r'生日', r'誕生日', r'생일', r'عيد ميلاد', r'जन्मदिन', r'बर्थडे', r'fødselsdag', r'födelsedag',
            r'\bhbd\b']

GIFT_CORE = [r'custom (\w+ ){0,2}songs?\b', r'personali[sz]ed (\w+ ){0,2}songs?\b', r'custom(ized|ised)? (made )?songs?', r'personali[sz]ed songs?', r'songs? (as a |as |for a )?gift', r'gift songs?',
             r'personal songs?', r'custom music', r'personali[sz]ed music', r'write a song (for|about)', r'song written (for|about)',
             r'commission(ed)? (a )?song', r'songs? (made|written) (for|about)', r'custom lyrics', r'custom song',
             r'песн[яиюе] на заказ', r'заказать песн', r'песн[яюи] в подарок', r'персональн\w* песн', r'именн\w* песн',
             r'песн[яю] по (истории|вашей)', r'авторск\w* песн', r'canci[óo]n(es)? personalizad', r'canci[óo]n para regalar',
             r'canci[óo]n de regalo', r'm[úu]sica personalizad', r'm[úu]sica para presente', r'm[úu]sica de presente',
             r'personalisierte[s]? (lied|song)', r'(lied|song) als geschenk', r'chanson personnalis', r'chanson cadeau',
             r'canzone personalizzat', r'kişiye özel şarkı', r'lagu (custom|personal|kado|hadiah)', r'song for someone',
             r'song about (my|your|someone)', r'song from (a |your )?story', r'story (in)?to song', r'song for my',
             r'make (a|your own) song for', r'how to make a (custom )?song for']
RECIP = [r'\b(wife|husband|mom|mum|mommy|mummy|mother|dad|daddy|father|papa|girlfriend|boyfriend|gf|bf|son|daughter|grandma|'
         r'grandpa|grandmother|grandfather|nana|friend|bestie|sister|brother|sis|bro|teacher|boss|partner|fianc[ée]e?|him|her|'
         r'couple|parents|lover|crush|grandson|granddaughter|niece|nephew|aunt|uncle|coworker|colleague)\b',
         r'для (мамы|папы|жены|мужа|подруги|друга|девушки|парня|сестры|брата|бабушки|дедушки|любимо|сына|дочери|учител)',
         r'для мам', r'para (mi )?(mam[áa]|madre|pap[áa]|padre|esposa|esposo|novia|novio|amig)', r'für (mama|papa|frau|mann|freundin)']
AI_GEN = [r'\bai\b', r'\ba\.i\.', r'generat', r'нейросет', r'\bии\b', r'ии ', r'text to (song|music)', r'lyrics to (song|music)',
          r'song maker', r'music maker', r'make (a )?song', r'create (a )?song', r'создать песн', r'сделать песн', r'песню онлайн',
          r'песню по тексту', r'gerador', r'generador', r'générateur', r'generatore', r'generator', r'kostenlos', r'gratis',
          r'song (creator|writer)', r'songwriter', r'yapay zeka', r'pembuat lagu']
SONGISH = [r'\bsongs?\b', r'\bmusic\b', r'песн', r'музык', r'canci', r'm[úu]sica', r'\blied', r'chanson', r'canzone', r'lagu',
           r'şarkı', r'piosenk', r'\bgana\b', r'\bgaana\b', r'\bkanta\b', r'jingle', r'\bsang\b', r'\blåt\b', r'bài hát']

# Name detection for NAMES_PROGRAMMATIC
GENERIC = set('''happy birthday song songs with name names the a an and for to of in on my your our his her their me you
 him she he it its is are was be by from at as this that what how where who which when why can do does make made maker making
 create created creating creator generator generate custom customized customised personalized personalised free online
 download mp3 mp4 audio video wishes wish wishing card cards photo photos picture image images pic pics lyrics lyric english
 hindi marathi kannada telugu tamil malayalam bengali bangla punjabi gujarati odia urdu nepali sinhala spanish korean japanese
 french german arabic chinese italian portuguese tagalog bisaya indian traditional funny cute new latest old best good top
 one two three 1 2 3 dear day bday b-day dj remix version special love romantic sweet kids kid child children baby boy girl
 son daughter mom mother mum mummy dad father papa wife husband sister brother sis bro friend friends bestie grandma grandpa
 grandson granddaughter nephew niece aunt uncle teacher boss lover girlfriend boyfriend gf bf ai app apps maker website
 site sites link links whatsapp facebook instagram status full hd 4k cake candle cut com www ringtone ringtones tune tunes
 music musical song's birthday's party year years old th st nd rd sing singing sung sang singer sang karaoke instrumental
 to-you you're your's u ur mp3s free-download download-free hbd wala wali ka ki ke liye gana gaana janamdin bday's inserted
 insert add adding edit editing editor maker's message messages greeting greetings ecard e-card gif gifs sticker stickers
 voice voices tone tones remake rap rock pop jazz country classical slow fast cover covers own personal personalize
 personalise birthdays happiest wonderful beautiful lovely amazing great very much many most all every each any some
 male female men women man woman lady ladies gentleman 18th 21st 30th 40th 50th 60th 70th 80th 90th 100th 1st 2nd 3rd 16th
 sixteenth eighteenth sweet16 first second third twenty thirty forty fifty sixty seventy eighty hundred
 jesus god christian church gospel worship prayer hymn and/or text texting send sending share sharing tiktok youtube reels
 reel short shorts clip clips style styles type types kind version versions original real official greek latin jewish hebrew
 african nigerian ghanaian kenyan filipino pinoy desi bollywood tollywood kollywood surprise surprised funny-birthday customize customise customized creation play playing find finding get getting epic
 heavy metal today tomorrow month months week simple normal muslim hindu sikh magical https http com org net vol volume specific
 person persons people someone somebody first last full zoom captain turbo tum jab paya tujhe saal hazaro jiyo hindi-english
 song-with-name use using used now without where online-free maker-free app-free songs-with-name famous popular trending viral
 make-a happy-birthday dance dancing party-song celebration celebrate celebrating latest-new mix medley version-with
 telugu-song wishing-song birthdaysong happybirthday names-list list lists number numbers digit generator-free whose only india software pagalworld mr
 own their there here good-morning morning night evening twins twin brothers sisters grandmother grandfather nani dadi
 nana dada amma appa akka anna thambi bhai behen didi bhaiya bhabhi chachu mama mami mausi beta beti bacha
'''.split())


def name_tokens(kw):
    toks = re.findall(r"[a-z][a-z'\-]+", kw)
    out = []
    for t in toks:
        t2 = t.strip("'-").replace("'s", '')
        if len(t2) < 3 or t2 in GENERIC:
            continue
        if re.match(r'^\d', t2):
            continue
        out.append(t2)
    return out


def classify(kw):
    """Return (cluster, reason, explicit_flag)."""
    k = kw.lower().replace('’', "'").replace('‘', "'").strip()
    personal = has(k, PERSONAL)
    # 1. NOISE
    if has(k, NOISE_FAMOUS):
        return 'NOISE', 'famous/franchise/off-topic', False
    if has(k, NOISE_TOOL) and not re.search(r'songfinch (cost|price|review)', k):
        return 'NOISE', 'unrelated tool (cover/voice/remix/video/jobs)', False
    if has(k, NOISE_MERCH) and not re.search(r'with name', k):
        return 'NOISE', 'physical merch / card', False
    # 2. brand
    for b, rx in BRANDS.items():
        if re.search(rx, k):
            return 'BRAND_COMPETITOR', b, True
    # 3. occasions
    is_bday = has(k, BIRTHDAY)
    occ = None
    for o, pats in OCCASIONS:
        if has(k, pats):
            occ = o
            break
    if is_bday and occ in (None, 'other', 'anniversary'):
        # "birthday anniversary song" -> treat as birthday
        names = name_tokens(k)
        if names and not has(k, AI_GEN):
            return 'NAMES_PROGRAMMATIC', 'name:' + names[0], True
        if personal:
            return 'BIRTHDAY_NAME', 'birthday+personalization', True
        return 'NOISE', 'generic happy-birthday listening', False
    if occ:
        listen = has(k, LISTEN) or bool(lang_modifier(k))
        if listen and not personal:
            return 'NOISE', f'{occ} listening (download/status/lyrics/kids/church)', False
        return 'OCCASION_' + occ, occ, personal
    # 4. gift core
    if has(k, GIFT_CORE):
        return 'GIFT_CORE', 'custom/personalized/gift song', True
    # 5. recipient
    if has(k, RECIP) and has(k, SONGISH):
        if has(k, LISTEN) and not personal:
            return 'NOISE', 'recipient listening', False
        return 'RECIPIENT', 'song for recipient', personal
    # 6. AI generator
    if has(k, AI_GEN) or re.search(AI_BRANDS, k):
        if has(k, SONGISH) or re.search(AI_BRANDS, k) or 'нейросет' in k:
            return 'AI_GENERATOR', 'generic AI song/music tool', False
    # 7. other
    if has(k, SONGISH):
        if has(k, LISTEN) and not personal:
            return 'NOISE', 'generic song listening', False
        return 'OTHER_RELEVANT', 'song-related, unclassified', personal
    return 'NOISE', 'no song term', False
