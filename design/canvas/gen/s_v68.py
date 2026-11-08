from kit import *
import re
P = PROJ + '/'
PH = ['sofa', 'family', 'candles', 'r09', 'r05', 'r01']
for f in ['p-c-07-ready.dc.html', 'p-c-07-ready-d.dc.html']:
    s = open(P + f).read(); s = s.replace('Anna gets it with her gift', 'Anna gets it with the gift'); open(P + f, 'w').write(s)

# ---- 2.1.3b ready to send, song only: the photos are already here, so the upgrade sells itself
for f, g in [('p-c-07-ready.dc.html', 'p-c-07b-ready-song-only.dc.html'), ('p-c-07-ready-d.dc.html', 'p-c-07b-ready-song-only-d.dc.html')]:
    s = open(P + f).read()
    s = s.replace('Your slideshow is ready', 'Your 6 photos can play with the song')
    s = s.replace('Made from the 6 photos you added and the song. Anna gets it with the gift', 'Add the slideshow and Anna sees them while the song plays. Plus a second version and the lyrics, ready to frame')
    s = re.sub(r'<span style="position:absolute;left:50%;top:50%;transform:translate\(-50%,-50%\)"><button class="play" aria-label="Watch a slideshow example"[\s\S]*?</button></span>', '', s)
    s = s.replace('>Watch the slideshow</a>', '>Add the slideshow</a>')
    s = re.sub(r'<div class="(?:li|row)"[^>]*>(?:(?!<div class="(?:li|row)").)*?Take 2[\s\S]*?2:51</span></div>', '', s, count=1, flags=re.S)
    s = s.replace('Bundle · take 1 · paid 1 March', 'Song · paid 1 March')
    s = re.sub(r'<title>([^<]*)</title>', lambda m: '<title>%s, song only</title>' % m.group(1), s)
    open(P + g, 'w').write(s)

# ---- 2.1.6 upgrade to the bundle (pay the difference)
grid = lambda c, h: '<div style="display:grid;grid-template-columns:repeat(%d,1fr);gap:6px">%s</div>' % (c, ''.join('<span class="ph" style="height:%dpx;border-radius:12px;display:block"><img src="/_blob/%s" alt="Your photo"></span>' % (h, IMG[k]) for k in PH))
ADDS = ['Your 6 photos play while Anna hears the song, and as a video to keep', 'A second version of the song, in full quality', 'The lyrics as a poster, A4 and US Letter']
CK = '<span style="width:22px;height:22px;border-radius:50%%;background:#FFD84D;display:flex;align-items:center;justify-content:center;flex-shrink:0">%s</span>' % ico('check', '#111', 14)
adds = col(*['<div style="display:flex;gap:12px;align-items:flex-start;font-size:15px;line-height:1.45">%s<span>%s</span></div>' % (CK, a) for a in ADDS], gap=10)
total = '<div style="display:flex;justify-content:space-between;align-items:baseline;border-top:1px solid #DADADA;padding-top:16px"><span style="font-size:15px">You pay the difference</span><span class="un tn" style="font-size:28px;font-weight:500">$26</span></div>'
when = small('Ready in about 10 minutes, well before Anna opens it on 14 March. Change the photos any time before then', extra='font-size:14px')
m = col(col(un('Add the slideshow for %s' % nm(), 28, tag='h1'), t('Same song, same gift link. These go on top', 15, True), gap=8), grid(3, 104), adds, total, when, gap=20, extra='padding-bottom:24px')
write('p-c-14-upgrade.dc.html', mobile('Order: upgrade to the bundle', m_head('order'), m, btn('Pay $26', full=True, tag='button') + '<a href="#" style="font-size:14px;text-align:center">Not now</a>', h=1000))
left = col(un('Add the slideshow for %s' % nm(), 48, tag='h1'), t('Same song, same gift link. These go on top', 18, True), adds, total, when, rowx(btn('Pay $26'), '<a href="#" style="font-size:15px">Not now</a>', gap=24), gap=24)
write('p-c-14-upgrade-d.dc.html', desktop('Order: upgrade to the bundle, desktop', d_head('order'), left, col(grid(3, 150), small('Your photos from the questionnaire. Add or swap them on the next screen'), gap=12), h=820, split='640px 1fr', pad='56px 120px 0 120px', gap=96))

# ---- 1.3.8 buy 3 more tries
info = col(*['<div style="display:flex;gap:12px;align-items:flex-start;font-size:15px;line-height:1.45">%s<span>%s</span></div>' % (CK, a) for a in ['3 new tries, each with two takes, ready in minutes', 'We take the $3 off the song when you pay', 'Your story, photos and lyrics stay as they are. Edit them before the next try if you like']], gap=10)
tot = '<div style="display:flex;justify-content:space-between;align-items:baseline;border-top:1px solid #DADADA;padding-top:16px"><span style="font-size:15px">3 more tries</span><span class="un tn" style="font-size:28px;font-weight:500">$3</span></div>'
m = col(col(un('3 more tries for %s’s song' % nm(), 28, tag='h1'), t('For when you need the song today', 15, True), gap=8), info, tot, gap=24)
write('p-c-09b-more-tries.dc.html', mobile('Pay: 3 more tries', m_head('wizard'), m, btn('Pay $3', full=True, tag='button') + '<a href="#" style="font-size:14px;text-align:center">Edit the lyrics first</a>', h=844))
left = col(un('3 more tries for %s’s song' % nm(), 48, tag='h1'), t('For when you need the song today', 18, True), info, tot, rowx(btn('Pay $3'), '<a href="#" style="font-size:15px">Edit the lyrics first</a>', gap=24), gap=24)
write('p-c-09b-more-tries-d.dc.html', desktop('Pay: 3 more tries, desktop', d_head('wizard'), left, card(img('sofa', 'Your photo of Anna and the flat', 220, '50% 45%') + lyric(24), pad=32, r=28, gap=20), h=760, split='640px 1fr', pad='56px 120px 0 120px', gap=96))
