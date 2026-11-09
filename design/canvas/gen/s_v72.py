# v72: flow review fixes A1-A11 (docs/research/appendix/flow-review-2026-11-09.md).
# Standalone patch script: edits the boards in ../project in place. Run once on a v70 snapshot.
import json, os, re

P = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'project') + '/'
CJ = json.load(open(P + 'canvas.json'))
B = CJ['boards']
touched = set()


def rep(f, old, new, count=1):
    s = open(P + f).read()
    n = s.count(old)
    assert n >= 1 and (count == 0 or n == count), '%s: %r found %d times' % (f, old[:60], n)
    open(P + f, 'w').write(s.replace(old, new))
    touched.add(f)


def sub(f, pat, new, count=1):
    s = open(P + f).read()
    s2, n = re.subn(pat, new, s, flags=re.S)
    assert n == count, '%s: /%s/ matched %d times' % (f, pat[:60], n)
    open(P + f, 'w').write(s2)
    touched.add(f)


def grow(f, dh):
    """Make a board taller: root element, $preview and the canvas frame."""
    h = B[f]['h']
    w = B[f]['w']
    rep(f, 'width:%dpx;height:%dpx' % (w, h), 'width:%dpx;height:%dpx' % (w, h + dh))
    rep(f, '"height":%d}' % h, '"height":%d}' % (h + dh))
    B[f]['h'] = h + dh


LAB = 'font-size:14px;font-weight:500;display:block;margin-bottom:8px'
TA = 'width:100%;box-sizing:border-box;border:2px solid #111;border-radius:12px;padding:16px;font:400 16px/1.5 Inter,system-ui,sans-serif;color:#111;background:#fff;resize:none;display:block'
CHK = 'width:22px;height:22px;margin:0;accent-color:#111;flex-shrink:0'
PLAY = '<svg aria-hidden="true" width="18" height="18" viewBox="0 0 24 24"><path d="M7 4.5l10 7.5-10 7.5z" fill="none" stroke="#fff" stroke-width="2" stroke-linejoin="round"></path></svg>'
DOWN = '<svg aria-hidden="true" width="18" height="18" viewBox="0 0 24 24"><path d="M12 4v11m0 0l-4-4m4 4l4-4M5 19h14" fill="none" stroke="#111" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path></svg>'

# ---- A1. The giver writes the note on "What Anna gets", before paying
NOTE = 'Thirty and still the first one dancing. Love you, the whole flat'
field = ('<div><label for="note" style="%s">Your note to Anna, shown after the song</label>'
         '<textarea id="note" rows="3" maxlength="300" style="%s">%s</textarea>'
         '<span class="mut tn" style="display:block;margin-top:6px;font-size:13px">%d / 300</span></div>') % (LAB, TA, NOTE, len(NOTE))
f = 'p-c-03b-gift-peek.dc.html'
rep(f, '<div style="display:flex;flex-direction:column;align-items:center;gap:12px"><button class="btn bk" style="width:100%;">Continue</button>',
    field + '<div style="display:flex;flex-direction:column;align-items:center;gap:12px"><button class="btn bk" style="width:100%;">Continue</button>')
grow(f, 156)
f = 'p-c-03b-gift-peek-d.dc.html'
rep(f, 'Anna can record a reaction for you</p>', 'Anna can record a reaction for you</p>' + field)
grow(f, 160)

# ---- A2. Ask for the date of the occasion (optional alone, required together)
date = lambda i, gap: ('<div><label class="lab" for="%s">When is it</label><input class="inp" id="%s" type="text" value="14 March" style="height:52px">'
                       '<span class="mut" style="display:block;margin-top:%dpx;font-size:13px">Optional. We plan the delivery around it and remind you in time</span></div>') % (i, i, gap)
rep('p-b-02b-occasion.dc.html', '<div><label class="lab" for="gn">', date('od', 6) + '<div><label class="lab" for="gn">')
rep('p-b-02b-occasion-d.dc.html', '<div><label class="lab" for="f">Your name, as it goes on the card', date('od', 8) + '<div><label class="lab" for="f">Your name, as it goes on the card')
for f in sorted(os.listdir(P)):
    if f.startswith('p-b-') and f.endswith('-d.dc.html') and 'Anna’s 30th birthday</span>' in open(P + f).read():
        rep(f, 'Anna’s 30th birthday</span>', 'Anna’s 30th birthday · 14 March</span>', 0)
for f in ['p-e-00-group-setup.dc.html', 'p-e-00-group-setup-d.dc.html']:
    rep(f, 'Ends Wed 11 March at 20:00 · up to 30 days', 'Ends Wed 11 March at 20:00, 3 days before the birthday · up to 30 days')

# ---- A3. "I'll send it myself" with a date: the link shows the countdown, same as "We'll send it"
rep('p-c-11-send-myself.dc.html', 'The link works now. We’ll remind you 10 minutes before 09:00 on 14 March',
    'The link shows a countdown until 09:00 on 14 March, then the song. We’ll remind you 10 minutes before')
rep('p-c-11-send-myself-d.dc.html', 'The link works now. We’ll remind you 10 minutes before 09:00 on 14 March and again at 09:00',
    'The link shows a countdown until 09:00 on 14 March, then the song. We’ll remind you 10 minutes before and again at 09:00')

# ---- A4. Name check comes before the music is generated: renumber and reorder the row
ROW = [('p-c-02-name-check', '1.3.1', 0), ('p-c-02b-name-fix', '1.3.2', 1520), ('p-c-01-generating', '1.3.3', 3040), ('p-c-08-delayed', '1.3.4', 4560)]
for stem, num, x in ROW:
    for f in (stem + '.dc.html', stem + '-d.dc.html'):
        B[f]['title'] = re.sub(r'^[\d.]+', num, B[f]['title'])
        B[f]['x'] = x
N = CJ['notes']
N['v66peek']['text'] = N['v66peek']['text'].replace('(1.3.1)', '(1.3.3)')
assert '(1.3.3)' in N['v66peek']['text']

# ---- A5. The recording never interrupts the song
N['v67play']['text'] += ('. The reaction recording stops quietly at 90 s, the red dot just goes out. '
                         '“Here’s your reaction” (3.2.1) comes only after the song ends or when Anna taps Stop')

# ---- A6. Anna's video is for watching. The giver and the group share the song card unless Anna allows more
allow = ('<label style="display:flex;gap:12px;align-items:flex-start;font-size:15px;line-height:1.4;cursor:pointer">'
         '<input type="checkbox" style="%s"><span>Max can post it too'
         '<span class="mut" style="display:block;font-size:13px;margin-top:2px">Leave it off and Max can only watch it</span></span></label>') % CHK
f = 'p-d-05-review-reaction.dc.html'
rep(f, '<div class="ph" style="height:400px;border-radius:28px">', '<div class="ph" style="height:330px;border-radius:28px">')
rep(f, '  <div style="display:flex;flex-direction:column;gap:12px">\n    <button class="btn bk"', '  ' + allow + '\n  <div style="display:flex;flex-direction:column;gap:12px">\n    <button class="btn bk"')
rep('p-d-05-review-reaction-d.dc.html', '<div style="display:flex;align-items:center;gap:12px;"><a class="btn bk" href="#" style="">Send to Max</a>',
    allow + '<div style="display:flex;align-items:center;gap:12px;"><a class="btn bk" href="#" style="">Send to Max</a>')
for f in ['p-e-06-reaction.dc.html', 'p-e-06-reaction-d.dc.html']:
    rep(f, '>Share it</strong>', '>Share the song</strong>')
    rep(f, 'It’s Anna’s face, so check she’s happy for you to post it', 'Anna’s video stays between you two. This shares the song card, without her video')
    rep(f, 'Made Anna a song for her 30th. Her face when she heard her name · made with @openyoursong', 'Made Anna a song for her 30th, with her name in it · made with @openyoursong')
for f, size in [('p-e-09-participant-later.dc.html', 17), ('p-e-09-participant-later-d.dc.html', 18)]:
    rep(f, '<strong style="font-size:%dpx;line-height:1.3">Share the moment</strong>' % size,
        '<strong style="font-size:%dpx;line-height:1.3">Share the song</strong><span class="mut" style="font-size:14px;line-height:1.4">Mum’s video is for the 7 of you. This shares the song card, without her video</span>' % size)
    grow(f, 48)
for f in ['p-e-06-reaction-d.dc.html', 'p-e-09-participant-later-d.dc.html']:
    rep(f, 'Save the video</button>', 'Save the card</button>')
sub('p-c-12-after-opened.dc.html', r'(<button class="btn bo" style="width:100%;padding:0 12px">)<svg.*?</svg>Share it</button>', lambda m: m.group(1) + DOWN + 'Download</button>')

# ---- A7. Say what the photos do in the Song and in the Bundle
for f in ['p-b-02c-photos.dc.html', 'p-b-02c-photos-d.dc.html']:
    rep(f, 'They go on Anna’s gift page next to the song, and we can set them to the music as a slideshow',
        'The first one becomes the cover of Anna’s gift. With the Bundle, all of them play while the song does')

# ---- A10. Order page starts with the whole song and a way to remake it
listen = ('<div style="border:1px solid #DADADA;border-radius:24px;padding:16px 20px;display:flex;flex-direction:column;gap:10px">'
          '<div style="display:flex;align-items:center;gap:12px"><button class="play" aria-label="Play the whole song" style="width:44px;height:44px">%s</button>'
          '<div style="display:flex;flex-direction:column;gap:2px;flex:1"><strong style="font-size:16px">Listen to the whole song first</strong>'
          '<span class="mut tn" style="font-size:14px;line-height:1.4">You’ve heard 40 s of 2:48</span></div></div>'
          '<a href="#" style="font-size:14px;min-height:28px;display:flex;align-items:center">Not quite right? Remake it, 2 free before Anna opens it</a></div>') % PLAY
for f in ['p-c-07-ready.dc.html', 'p-c-07b-ready-song-only.dc.html']:
    rep(f, '  <div class="tile" style="background:#FFD84D;padding:20px;gap:16px">', '  ' + listen + '\n  <div class="tile" style="background:#FFD84D;padding:20px;gap:16px">')
    grow(f, 140)
# the taller mobile boards need room: move the desktop row of the order page down
for b in B.values():
    if b.get('page') == 'landing' and b['y'] == 22448:
        b['y'] += 140
for f in ['p-c-07-ready-d.dc.html', 'p-c-07b-ready-song-only-d.dc.html']:
    a = '<div style="border-radius:24px;background:#FFD84D;padding:28px;display:flex;flex-direction:column;gap:16px;"><strong style="font-size:17px;line-height:1.3">Gift link</strong>'
    rep(f, a, listen + a)
    grow(f, 140)

# ---- A9. "Thank Max": a short text reply for people who don't record a video
MSG = 'Max, I cried at the yellow bike. Best birthday present I’ve ever had'
thank_field = ('<div><label for="th" style="%s">Your message</label><textarea id="th" rows="4" maxlength="300" style="%s">%s</textarea>'
               '<span class="mut tn" style="display:block;margin-top:6px;font-size:13px">%d / 300</span></div>') % (LAB, TA, MSG, len(MSG))


def clone(src, dst, title, body):
    s = open(P + src).read()
    i, j = s.index('</helmet>') + len('</helmet>'), s.index('</x-dc>')
    s = s[:i] + '\n' + body + '\n' + s[j:]
    s = re.sub(r'<title>[^<]*</title>', '<title>%s</title>' % title, s, count=1)
    open(P + dst, 'w').write(s)
    touched.add(dst)


H1M = 'margin:0;font-size:30px;font-weight:500;line-height:1.15;letter-spacing:-.02em;'
H1D = 'margin:0;font-size:48px;font-weight:500;line-height:1.15;letter-spacing:-.02em;'
clone('p-d-13-my-video.dc.html', 'p-d-18-thank.dc.html', 'Gift page: thank the giver',
      '<div class="cp" style="width:390px;height:844px;box-sizing:border-box;overflow:hidden;position:relative">\n'
      '<header style="display:flex;align-items:center;justify-content:center;height:76px;padding:0 20px"><a href="#" class="un fl" style="font-weight:500;font-size:18px;color:#111">openyoursong</a></header>\n'
      '<main style="padding:0px 20px 0;display:flex;flex-direction:column;gap:24px"><div style="display:flex;flex-direction:column;gap:16px;">'
      '<h1 class="un" style="%s">Say thanks to Max</h1>'
      '<p class="mut" style="margin:0;font-size:16px;line-height:1.5;font-weight:400;">A few words are enough. Max gets them by email and on the order page</p>%s</div></main>\n'
      '<div style="position:absolute;left:0;right:0;bottom:0;background:#fff;border-top:1px solid #DADADA;padding:16px 20px 24px;display:flex;flex-direction:column;align-items:center;gap:8px">'
      '<button class="btn bk" style="width:100%%">Send to Max</button><a href="#" style="font-size:14px;min-height:44px;display:flex;align-items:center">Not now, back to my song</a></div>\n</div>' % (H1M, thank_field))
clone('p-d-09-no-camera-d.dc.html', 'p-d-18-thank-d.dc.html', 'Gift page: thank the giver, desktop',
      '<div class="cp" style="width:1440px;height:900px;box-sizing:border-box;overflow:hidden;position:relative">\n'
      '<header style="height:72px;display:flex;align-items:center;justify-content:center"><a href="#" class="un fl" style="font-weight:500;font-size:18px;color:#111">openyoursong</a></header>\n'
      '<main style="display:grid;grid-template-columns:1fr 1fr;gap:96px;padding:0 48px 48px 48px;align-items:center"><div style="height:780px"><div class="ph" style="height:780px;border-radius:28px;flex-shrink:0">'
      '<img src="/_blob/5c825ead91ccef82ac575d6be71a2319" alt="The cover photo of the gift: Anna and the flat on the sofa" style="object-position:50%% 45%%"></div></div>'
      '<div style="display:flex;flex-direction:column;justify-content:center;min-height:780px;max-width:520px"><div style="display:flex;flex-direction:column;gap:24px;">'
      '<h1 class="un" style="%s">Say thanks to Max</h1>'
      '<p class="mut" style="margin:0;font-size:18px;line-height:1.5;font-weight:400;">A few words are enough. Max gets them by email and on the order page</p>%s'
      '<div style="display:flex;align-items:center;gap:24px;"><a class="btn bk" href="#" style="">Send to Max</a><a href="#" style="font-size:15px">Not now, back to my song</a></div></div></div></main>\n</div>' % (H1D, thank_field))
B['p-d-18-thank.dc.html'] = {'x': 12160, 'y': 28256, 'w': 390, 'h': 844, 'page': 'landing', 'title': '3.2.9  Thank Max · mobile'}
B['p-d-18-thank-d.dc.html'] = {'x': 12160, 'y': 31264, 'w': 1440, 'h': 900, 'page': 'landing', 'title': '3.2.9  Thank Max · desktop'}
for f in ['p-d-18-thank.dc.html', 'p-d-18-thank-d.dc.html']:
    if f not in CJ['order']:
        CJ['order'].append(f)

# ---- A11 and new notes
N['v68tries']['text'] = ('Where the buttons go. “Continue with try 2” → What Anna gets (that take) → Song or bundle → payment. '
                         '“Get 2 more tries” → 2 more tries, free, once per song → generating, attempt 4 of 5. After those two, only “Continue” is left')
e06 = B['p-e-06-reaction.dc.html']
N['v71share'] = {'fill': 'yellow', 'page': 'landing', 'size': 20, 'w': 380, 'x': e06['x'], 'y': e06['y'] - 330,
                 'text': 'Who can post Anna’s video. By default nobody: the giver and the group can watch and download it, and “Share” posts the song card (3.2.7). '
                         'If Anna ticks “Max can post it too” on 3.2.1, this block shares the reaction card (3.2.8) instead'}
th = B['p-d-18-thank.dc.html']
N['v71thank'] = {'fill': 'yellow', 'page': 'landing', 'size': 20, 'w': 380, 'x': th['x'] + 430, 'y': th['y'],
                 'text': '“Thank Max” on the gift page (3.2.4) opens this. It is the reply for people who skip the video: '
                         'the giver gets it by email and on the order page, so most gifts get an answer, not only “opened”'}

json.dump(CJ, open(P + 'canvas.json', 'w'), ensure_ascii=False, separators=(',', ':'))

# ---- sanity: no two boards on the page overlap, tags balance
items = [(k, b) for k, b in B.items() if b.get('page') == 'landing']
for i, (k1, a) in enumerate(items):
    for k2, b in items[i + 1:]:
        if a['x'] < b['x'] + b['w'] and b['x'] < a['x'] + a['w'] and a['y'] < b['y'] + b['h'] and b['y'] < a['y'] + a['h']:
            print('OVERLAP', k1, k2)
for f in sorted(touched):
    s = open(P + f).read()
    for tag in ['div', 'span', 'label', 'button', 'a', 'main', 'section', 'p']:
        o, c = len(re.findall(r'<%s[\s>]' % tag, s)), s.count('</%s>' % tag)
        if o != c:
            print('UNBALANCED', f, tag, o, c)
print('changed boards:', len(touched))
print('\n'.join(sorted(touched)))
