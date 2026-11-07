from kit import *
OUT = []

NAV = ('How it works', 'Examples', 'Pricing', 'Ideas')

def head_d(active=None):
    nav = ''.join('<a href="#" style="text-decoration:none;%s">%s</a>' % ('box-shadow:inset 0 -2px 0 #111;padding-bottom:4px' if x == active else '', x) for x in NAV)
    return '<header style="height:88px;display:flex;align-items:center;justify-content:space-between;padding:0 64px;border-bottom:1px solid #DADADA">%s<nav style="display:flex;gap:32px;font-size:15px;font-weight:500">%s</nav><div style="display:flex;gap:24px;align-items:center"><a href="#" class="mut" style="font-size:15px;text-decoration:none">Log in</a>%s</div></header>' % (WM % 22, nav, btn('Make a song', sm=True))

FOOT_COLS = [('Occasions', ['Birthday', 'Anniversary', 'Mother’s Day', 'Father’s Day', 'Wedding', 'Valentine’s Day']),
             ('For', ['Mum', 'Dad', 'Wife', 'Husband', 'Sister', 'Best friend']),
             ('Compare', ['vs Songfinch', 'Songfinch alternatives', 'Best custom song service', 'Custom song vs AI song']),
             ('Guides', ['How much a custom song costs', 'How to make a song gift', 'Birthday song with a name', 'Free love song generator'])]

def foot_d():
    cols = ''.join('<div style="display:flex;flex-direction:column;gap:10px"><strong style="font-size:14px">%s</strong>%s</div>' % (h, ''.join('<a href="#" class="mut" style="font-size:14px;text-decoration:none">%s</a>' % l for l in ls)) for h, ls in FOOT_COLS)
    return ('<footer style="border-top:1px solid #DADADA;padding:48px 64px;display:grid;grid-template-columns:320px repeat(4,1fr);gap:32px">'
            '<div style="display:flex;flex-direction:column;gap:12px">%s<span class="mut" style="font-size:14px;line-height:1.5">Personal songs made with AI from your story</span><span class="mut" style="font-size:13px">Privacy · Terms · Refunds · Contact</span></div>%s</footer>') % (WM % 20, cols)

def foot_m():
    cols = ''.join('<details style="border-top:1px solid #DADADA"><summary style="min-height:52px;display:flex;align-items:center;justify-content:space-between;font-size:15px;font-weight:500;cursor:pointer;list-style:none">%s%s</summary></details>' % (h, ico('plus', '#111', 16)) for h, _ in FOOT_COLS)
    return '<footer style="padding:24px 20px 32px;display:flex;flex-direction:column;gap:0">%s<div style="border-top:1px solid #DADADA;padding-top:16px;display:flex;flex-direction:column;gap:8px">%s<span class="mut" style="font-size:13px">Privacy · Terms · Refunds · Contact</span></div></footer>' % (cols, WM % 18)

def crumbs(*items):
    return '<nav aria-label="Breadcrumb" class="mut" style="font-size:14px;display:flex;gap:8px;flex-wrap:wrap">%s</nav>' % ' <span>/</span> '.join('<a href="#" class="mut" style="text-decoration:none">%s</a>' % i for i in items)

def meta(updated='Updated 7 Nov 2026', read='4 min read'):
    return small('%s · %s · by the openyoursong team' % (updated, read), extra='font-size:14px')

def answer(html, label='Short answer'):
    return '<div style="background:#FFD84D;border-radius:24px;padding:28px;display:flex;flex-direction:column;gap:10px"><strong style="font-size:15px">%s</strong><div style="font-size:19px;line-height:1.5">%s</div></div>' % (label, html)

def songcard(title='Sixty miles of Leo', sub='For Dad, 60th · country · made with openyoursong', key='dad', alt='A man of sixty with a guitar by an old truck'):
    return frame('<div style="display:flex;gap:16px;align-items:center">%s<div style="flex:1;display:flex;flex-direction:column;gap:4px"><strong class="un" style="font-size:18px;font-weight:500">%s</strong><span class="mut" style="font-size:14px">%s</span></div>%s</div>' % (img(key, alt, 80, r=16, w='80px'), title, sub, play('Play ' + title, 48)), pad=16)

def cta_band(h1='Make theirs with their name in it', sub='Free 30–45 s preview, $29 if you love it'):
    return '<div style="background:#111;color:#fff;border-radius:28px;padding:40px;display:flex;justify-content:space-between;align-items:center;gap:32px"><div style="display:flex;flex-direction:column;gap:8px"><p class="un" style="margin:0;font-size:32px;font-weight:500;line-height:1.1">%s</p><span style="font-size:16px;color:#DADADA">%s</span></div>%s</div>' % (h1, sub, btn('Start free, hear it first', 'by'))

def cta_m(h1='Make theirs with their name in it', sub='Free preview, $29 if you love it'):
    return '<div style="background:#111;color:#fff;border-radius:24px;padding:24px;display:flex;flex-direction:column;gap:12px"><p class="un" style="margin:0;font-size:24px;font-weight:500;line-height:1.15">%s</p><span style="font-size:15px;color:#DADADA">%s</span>%s</div>' % (h1, sub, btn('Start free, hear it first', 'by', full=True))

def aside_d():
    return col(card(img('box', 'A tangerine gift box with a blue ribbon and paper confetti', 180, r=16) + strong('A song with their name in it', 18) + small('Tell us about them in three minutes. Hear a free preview before you pay', mut=False) + btn('Start free, hear it first', full=True), pad=24, r=28, gap=14),
               small('From $29 · two free remakes · refund within 14 days while unopened'), gap=12, extra='position:sticky;top:24px')

def faq(items, open_first=True):
    return '<div>%s</div>' % ''.join('<details%s style="border-top:1px solid #DADADA;padding:20px 0"><summary style="cursor:pointer;font-size:18px;font-weight:500;list-style:none;display:flex;justify-content:space-between;gap:16px">%s%s</summary><p class="mut" style="margin:12px 0 0;font-size:16px;line-height:1.6">%s</p></details>' % (' open' if (open_first and i == 0) else '', q, ico('plus', '#111', 18), a) for i, (q, a) in enumerate(items))

def table(head, rows, hl=1):
    th = ''.join('<th style="text-align:left;font-size:14px;font-weight:500;padding:14px 16px;%s">%s</th>' % ('background:#FFD84D;' if i == hl else '', h) for i, h in enumerate(head))
    tr = ''.join('<tr>%s</tr>' % ''.join('<td style="padding:14px 16px;font-size:15px;line-height:1.4;border-top:1px solid #DADADA;vertical-align:top;%s">%s</td>' % ('font-weight:500;' if i == hl else ('color:#4A4A4A;' if i == 0 else ''), c) for i, c in enumerate(r)) for r in rows)
    return '<div style="border:1px solid #DADADA;border-radius:20px;overflow:hidden"><table style="width:100%%;border-collapse:collapse"><thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>' % (th, tr)

def mtable(rows, a='openyoursong', b='Songfinch'):
    # mobile: stacked rows
    return '<div style="border:1px solid #DADADA;border-radius:20px;overflow:hidden">%s</div>' % ''.join(
        '<div style="padding:14px 16px;%s"><span class="mut" style="font-size:13px">%s</span><div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:6px;font-size:14px;line-height:1.4"><span style="font-weight:500;padding:6px 8px">%s</span><span style="padding:6px 8px">%s</span></div></div>' % ('' if i == 0 else 'border-top:1px solid #DADADA;', r[0], r[1], r[2]) for i, r in enumerate(rows))

def H(t, size=32, tag='h2'):
    return un(t, size, tag=tag, extra='margin-top:16px')

def P(t, size=17):
    return '<p style="margin:0;font-size:%dpx;line-height:1.65">%s</p>' % (size, t)

def article_d(name, title, active, main, h, aside=True):
    body = '<main style="display:grid;grid-template-columns:%s;gap:80px;padding:48px 120px 64px;align-items:start">%s%s</main>' % ('1fr 360px' if aside else '1fr', main, aside_d() if aside else '')
    OUT.append(write(name, doc(title, 1440, h, head_d(active) + body + foot_d())))

def article_m(name, title, main, h):
    body = m_head('site') + '<main style="padding:8px 20px 32px;display:flex;flex-direction:column;gap:20px">%s</main>' % main + foot_m()
    bar = '<div style="position:absolute;left:0;right:0;bottom:0;background:#fff;border-top:1px solid #DADADA;padding:12px 20px 20px">%s</div>' % btn('Make yours, free preview', full=True)
    OUT.append(write(name, doc(title, 390, h, body + bar)))

# ================= 1. /vs/songfinch =================
ROWS = [('Price', '$29 song, $55 bundle', 'Original from $179–199.99, set by the artist. Instant $29.99'),
        ('Hear it before paying', 'Free 30–45 s preview of the same song', 'Original: no. Instant: you can play variants before choosing'),
        ('How it’s made', 'AI writes and sings it from your story. You can edit every line', 'Original: a real artist. Instant: pre-recorded artist clips put together'),
        ('Name check', 'You hear the name sung and can fix it by sound', 'Not offered as a step. Name issues show up in reviews'),
        ('Delivery', 'Gift page on the date and time you pick, in their time zone', 'Original: about 7 days, rush in 24 h. Instant: about 5 min'),
        ('Reaction video', 'They can record one for you, with consent', 'No'),
        ('Group gift', 'Up to 20 people add a memory, one person pays', 'No')]
SRC = small('Songfinch details from songfinch.com and get.songfinch.com, checked 5 Nov 2026. Prices change, check their site before you buy')
FAQ_VS = [('Is Songfinch better than openyoursong', 'If you want a real musician to write and record the song and you have $180–200 and a week, Songfinch Original is the better fit. If you want to hear the song with their name before paying and send it on a set day for $29, we are'),
          ('Does openyoursong use AI', 'Yes. The lyrics and music are made with AI from your story, and the gift page says so. You can edit every line before the music is made'),
          ('Can I hear it before I pay', 'Yes. You hear a free 30–45 second preview of the same song you’ll get, with their name in it')]
main = col(crumbs('Ideas', 'Compare', 'openyoursong vs Songfinch'), un('openyoursong vs Songfinch: which custom song gift to pick', 56, tag='h1'), meta(),
           answer('Pick <strong>Songfinch Original</strong> if you want a real artist and can wait about a week for around $180–200. Pick <strong>openyoursong</strong> if you want to hear the song with their name for free first, pay $29 and send it on a set day'),
           H('Side by side'), table(['', 'openyoursong', 'Songfinch'], ROWS), SRC,
           H('Where Songfinch is the better choice'), P('A person writes and sings your song, and some people want exactly that. Songfinch has years of reviews and options like vinyl. If budget and time aren’t an issue, it’s a solid gift'),
           H('Where openyoursong is the better choice'), P('You hear the start of the actual song with their name before paying, you check how the name is sung, and the gift opens on the day you choose. Friends can add memories to one song, and the person who gets it can send back a video of their reaction'),
           songcard(), H('Questions'), faq(FAQ_VS), gap=20)
article_d('p-h-02-vs-songfinch-d.dc.html', 'Compare: openyoursong vs Songfinch, desktop', 'Ideas', main, 2560)
m = col(crumbs('Compare', 'vs Songfinch'), un('openyoursong vs Songfinch: which custom song gift to pick', 30, tag='h1'), meta(),
        answer('Songfinch Original if you want a real artist and can wait a week for ~$180–200. openyoursong if you want to hear it free first, pay $29 and send it on a set day').replace('font-size:19px', 'font-size:16px').replace('padding:28px', 'padding:20px'),
        H('Side by side', 24), mtable(ROWS), SRC, songcard(), H('Questions', 24), faq(FAQ_VS), cta_m(), gap=16)
article_m('p-h-02-vs-songfinch.dc.html', 'Compare: openyoursong vs Songfinch', m, 2916)

# ================= 2. guide: how much does a custom song cost =================
PR = [('openyoursong', '$29, bundle $55', 'Free preview before paying', 'AI from your story'), ('Songfinch Original', 'from $179–199.99', 'No preview', 'Real artist, about 7 days'),
      ('Songfinch Instant', '$29.99', 'Play variants before choosing', 'Pre-recorded clips'), ('GiftYourSong', '$39.99', 'Free preview', 'AI')]
FAQ_P = [('Why do some custom songs cost $200', 'A real musician writes and records each one, which takes days. AI songs cost less because the music is generated from your story in minutes'),
         ('Are there extra costs', 'With us, no. The $29 includes the full song, the gift page, delivery on your date and the PDF card. The $55 bundle adds a second version, a photo slideshow and a lyrics poster'),
         ('Can I get my money back', 'You get two free remakes. If it still isn’t right, you get a full refund within 14 days of paying, as long as the gift hasn’t been opened')]
main = col(crumbs('Ideas', 'Guides', 'Custom song cost'), un('How much does a custom song cost', 56, tag='h1'), meta(),
           answer('An AI-made custom song costs <strong>$29–40</strong>. A song written and recorded by a real artist costs <strong>$180–200</strong> or more. At openyoursong it’s $29, or $55 with a slideshow and a second version, and you hear a free preview first'),
           H('Prices compared'), table(['Service', 'Price', 'Before you pay', 'How it’s made'], PR, hl=0).replace('background:#FFD84D;', 'background:#F2F2F2;'), small('Prices from each service’s site, checked 5 Nov 2026'),
           H('What changes the price'), P('Who makes it is the biggest factor: a person or AI. Then come extras like rush delivery, more verses, a video or vinyl. The cheapest way to avoid paying for something you don’t like is a service that lets you hear the song before you pay'),
           songcard(), H('Questions'), faq(FAQ_P), gap=20)
article_d('p-h-03-guide-cost-d.dc.html', 'Guide: how much does a custom song cost, desktop', 'Ideas', main, 1952)
m = col(crumbs('Guides', 'Custom song cost'), un('How much does a custom song cost', 30, tag='h1'), meta(),
        answer('AI-made: $29–40. By a real artist: $180–200 or more. openyoursong: $29, or $55 with a slideshow, after a free preview').replace('font-size:19px', 'font-size:16px').replace('padding:28px', 'padding:20px'),
        H('Prices compared', 24), mtable([(r[0], r[1], r[2]) for r in PR], 'Price', 'Before you pay'), H('What changes the price', 24), P('Who makes it is the biggest factor: a person or AI. Then come extras like rush delivery, more verses or vinyl', 16),
        songcard(), H('Questions', 24), faq(FAQ_P), cta_m(), gap=16)
article_m('p-h-03-guide-cost.dc.html', 'Guide: how much does a custom song cost', m, 2284)

# ================= 3. songs for sister (listicle) =================
def song_item(n, t, a, why):
    return '<div style="display:grid;grid-template-columns:56px 1fr;gap:16px;padding:20px 0;border-top:1px solid #DADADA"><span class="un tn" style="font-size:32px;font-weight:500">%02d</span><div style="display:flex;flex-direction:column;gap:6px"><strong style="font-size:19px">%s</strong><span class="mut" style="font-size:15px">%s</span><p style="margin:4px 0 0;font-size:16px;line-height:1.6">%s</p></div></div>' % (n, t, a, why)
own = '<div style="background:#FFD84D;border-radius:24px;padding:28px;display:grid;grid-template-columns:1fr auto;gap:24px;align-items:center"><div style="display:flex;flex-direction:column;gap:8px"><p class="un" style="margin:0;font-size:26px;font-weight:500;line-height:1.15">Or the one song no playlist has: with %s in it</p><span style="font-size:16px">Tell us about your sister. Hear a free preview with her name</span></div>%s</div>' % (nm('her name', True), btn('Make her song'))
main = col(crumbs('Ideas', 'Songs for', 'Sister'), un('Songs for your sister, and one with her name in it', 56, tag='h1'), meta(read='6 min read'),
           P('Songs to send your sister on her birthday or just because, from old favourites to ones you can sing together in the car', 19),
           song_item(1, 'We Are Family', 'Sister Sledge, 1979', 'Recorded by four real sisters. The obvious pick, and still the one everyone dances to'),
           song_item(2, 'Sisters', 'Rosemary and Betty Clooney, 1954', 'Written by Irving Berlin for White Christmas. Sweet, a little silly, perfect for a sister who loves old films'),
           own, small('The full article lists 15 songs'), H('Questions'), faq([('Can I make a song about my sister', 'Yes. Tell us her name, your memories and her inside jokes. You hear a free preview with her name before you pay $29'), ('What makes a good song for a sister', 'Specific memories: the room you shared, the fights you laugh about now, what she calls you')]), gap=16)
article_d('p-h-04-songs-for-sister-d.dc.html', 'Songs for: sister, desktop', 'Ideas', main, 1592)
m = col(crumbs('Songs for', 'Sister'), un('Songs for your sister, and one with her name in it', 30, tag='h1'), meta(read='6 min read'),
        song_item(1, 'We Are Family', 'Sister Sledge, 1979', 'Recorded by four real sisters. Still the one everyone dances to'),
        song_item(2, 'Sisters', 'Rosemary and Betty Clooney, 1954', 'Written by Irving Berlin for White Christmas'),
        card('<p class="un" style="margin:0;font-size:22px;font-weight:500;line-height:1.15">Or the one song no playlist has: with %s in it</p>' % nm('her name', True) + btn('Make her song', full=True), bg='#FFD84D', pad=20, gap=12),
        small('The full article lists 15 songs'), gap=12)
article_m('p-h-04-songs-for-sister.dc.html', 'Songs for: sister', m, 1296)

# ================= 4. /birthday-song-with-name =================
NAMES = ['Anna', 'Leo', 'Mia', 'Olivia', 'James', 'Sophie', 'Noah', 'Emma']
namegrid = '<div style="display:flex;flex-wrap:wrap;gap:8px">%s</div>' % ''.join('<button class="chip">%s%s</button>' % (ico('play', '#111', 14), n) for n in NAMES)
hero_l = col(crumbs('Ideas', 'Birthday song with name'), un('A birthday song with their name in it', 64, tag='h1', extra='font-weight:800'),
             t('Not “happy birthday, dear friend”. A song with their name, their jokes and their year, made from your story. Hear a free preview first', 19, True),
             rowx('<div style="flex:1">%s</div>' % inp('bn', 'Their name', 'Anna'), btn('Hear how it sounds', tag='button', icon='play'), align='flex-end'),
             col('<span class="lab" style="margin:0">Or play an example</span>', namegrid, gap=8), gap=24)
body = ('<main style="padding:48px 120px 64px;display:flex;flex-direction:column;gap:64px">'
        '<div style="display:grid;grid-template-columns:1fr 520px;gap:80px;align-items:center">%s%s</div>'
        '<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:20px">%s%s%s</div>%s%s</main>') % (
    hero_l, col(img('candles', 'Candles on a birthday cake', 440, r=28), rowx(play('Play Happy 30th, Anna'), strong('“Happy 30th, Anna” · pop · 0:40', 16)), gap=12),
    card(strong('1. Their name, sung', 17) + small('You hear how the name sounds and fix it by spelling it out', mut=False), pad=24), card(strong('2. Their story', 17) + small('Nicknames, the bike, the bad car singing. About three minutes', mut=False), pad=24, bg='#FFD84D'), card(strong('3. On their birthday', 17) + small('Opens at the time you pick, in their time zone', mut=False), pad=24),
    faq([('Is there a free birthday song with my friend’s name', 'You can hear a free 30–45 second preview with their name. The full song is $29'), ('Which names work', 'Any name. If it’s unusual, you write how it sounds and we sing it that way')]), cta_band('Make their birthday song'))
OUT.append(write('p-h-05-birthday-song-name-d.dc.html', doc('Birthday song with name, desktop', 1440, 1712, head_d('Ideas') + body + foot_d())))
m = col(crumbs('Ideas', 'Birthday song with name'), un('A birthday song with their name in it', 36, tag='h1', extra='font-weight:800'),
        t('A song with their name, their jokes and their year. Hear a free preview first', 16, True), inp('bnm', 'Their name', 'Anna'), btn('Hear how it sounds', full=True, tag='button', icon='play'),
        col('<span class="lab" style="margin:0">Or play an example</span>', namegrid, gap=8), img('candles', 'Candles on a birthday cake', 220),
        faq([('Is there a free birthday song with my friend’s name', 'You can hear a free 30–45 second preview with their name. The full song is $29')]), gap=16)
article_m('p-h-05-birthday-song-name.dc.html', 'Birthday song with name', m, 1536)

# ================= 5. free tool: love song lyrics =================
out_card = card('<span class="mut" style="font-size:13px">Your lyrics, verse 1</span>' + ''.join('<p style="margin:0;font-size:18px;line-height:1.6">%s</p>' % l for l in ['%s, you still steal my side of the bed' % nm('Sam'), 'and every song I hum is something that you said', 'ten years of coffee, cold by the time I drink', 'you’re still the first thing that I think']) + rowx(btn('Hear it sung, free preview', icon='play'), btn('Write another', 'bo', icon='redo'), gap=8), bg='#fff', pad=28, r=28, gap=10, extra='border:2px solid #111')
form = col(inp('ln', 'Their name', 'Sam'), chips(['Partner', 'Wife', 'Husband', 'Crush'], ['Partner'], 'They are your'), ta('lm', 'One thing only they do', 'Steals my side of the bed, hums all day', 72), chips(['Sweet', 'Funny', 'Tender'], ['Sweet'], 'Mood'), btn('Write my love song', tag='button', full=True), small('Free, no sign-up. Lyrics only, the sung version is a free preview'), gap=16)
body = ('<main style="padding:48px 120px 64px;display:flex;flex-direction:column;gap:48px">%s<div style="display:grid;grid-template-columns:440px 1fr;gap:48px;align-items:start">%s%s</div>%s%s</main>') % (
    col(crumbs('Ideas', 'Free tools', 'Love song generator'), un('Free AI love song generator', 64, tag='h1', extra='font-weight:800'), t('Write love song lyrics with their name in seconds. Like them? Hear them sung with a free preview', 19, True), gap=16),
    card(form, pad=28, r=28), out_card,
    faq([('Is the love song generator free', 'Yes, the lyrics are free. Hearing them sung is a free 30–45 second preview, the full song is $29'), ('Can I edit the lyrics', 'Yes. Change any line, or ask for a rewrite with a wish like “funnier”')]), cta_band('Turn the lyrics into a song for them'))
OUT.append(write('p-h-06-love-song-tool-d.dc.html', doc('Tool: love song generator, desktop', 1440, 1624, head_d('Ideas') + body + foot_d())))
m = col(crumbs('Free tools', 'Love song generator'), un('Free AI love song generator', 34, tag='h1', extra='font-weight:800'), t('Love song lyrics with their name in seconds', 16, True), form, out_card.replace('padding:28px', 'padding:20px').replace('<div style="display:flex;align-items:center;gap:8px;">', '<div style="display:flex;flex-direction:column;align-items:stretch;gap:8px;">'), gap=16)
article_m('p-h-06-love-song-tool.dc.html', 'Tool: love song generator', m, 1716)

# ================= 6. /ideas hub =================
def link_list(title, items):
    return col('<strong class="un" style="font-size:20px;font-weight:500">%s</strong>' % title, '<div>%s</div>' % ''.join('<a href="#" style="display:flex;justify-content:space-between;align-items:center;padding:14px 0;border-top:1px solid #DADADA;text-decoration:none;font-size:16px">%s%s</a>' % (i, ico('back', '#4A4A4A', 16).replace('M15 5l-7 7 7 7', 'M9 5l7 7-7 7')) for i in items), gap=8)
feat = '<div style="display:grid;grid-template-columns:1fr 1fr;gap:0;border-radius:28px;overflow:hidden;background:#FFD84D">%s<div style="padding:40px;display:flex;flex-direction:column;justify-content:center;gap:16px"><span style="font-size:14px;font-weight:500">Guide</span><p class="un" style="margin:0;font-size:36px;font-weight:500;line-height:1.1">How much does a custom song cost</p><span style="font-size:16px;line-height:1.5">$29 to $200 and why. With a price table for the main services</span>%s</div></div>' % (img('candles', 'Candles on a birthday cake', 380, r=0), btn('Read the guide', sm=True, extra='align-self:flex-start'))
lists = '<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:40px">%s%s%s%s</div>' % (
    link_list('Guides', ['How much a custom song costs', 'How to make a song gift', 'What to write in a song for Mum', 'Custom song vs AI song']),
    link_list('Compare', ['openyoursong vs Songfinch', 'Songfinch alternatives', 'Best custom song service']),
    link_list('Songs for', ['Sister', 'Daughter', 'Son', 'Mum', 'Best friend', 'A new baby']),
    link_list('Free tools', ['Love song generator', 'Birthday song generator', 'Birthday song with a name']))
occ = col('<strong class="un" style="font-size:20px;font-weight:500">By occasion</strong>', '<div class="chips">%s</div>' % ''.join('<a href="#" class="chip" style="text-decoration:none">%s</a>' % o for o in ['Birthday', 'Anniversary', 'Valentine’s Day', 'Mother’s Day', 'Father’s Day', 'Wedding', 'Retirement', 'Graduation']), gap=12)
body = '<main style="padding:48px 64px 64px;display:flex;flex-direction:column;gap:56px">%s%s%s%s%s</main>' % (
    col(un('Ideas for a song gift', 64, tag='h1'), t('Guides, comparisons and songs for the people you love. Every page ends with a way to make theirs', 19, True), gap=12), feat, lists, occ, cta_band())
OUT.append(write('p-h-01-ideas-hub-d.dc.html', doc('Ideas hub, desktop', 1440, 1744, head_d('Ideas') + body + foot_d())))
m = col(un('Ideas for a song gift', 34, tag='h1'), t('Guides, comparisons and songs for the people you love', 16, True),
        card(img('candles', 'Candles on a birthday cake', 180, r=16) + '<span style="font-size:13px;font-weight:500">Guide</span><p class="un" style="margin:0;font-size:22px;font-weight:500;line-height:1.15">How much does a custom song cost</p>' + btn('Read the guide', sm=True, extra='align-self:flex-start'), bg='#FFD84D', pad=20, gap=10),
        link_list('Guides', ['How much a custom song costs', 'How to make a song gift', 'Custom song vs AI song']), link_list('Compare', ['openyoursong vs Songfinch', 'Songfinch alternatives']),
        link_list('Songs for', ['Sister', 'Daughter', 'Mum', 'Best friend']), link_list('Free tools', ['Love song generator', 'Birthday song with a name']), occ, gap=24)
article_m('p-h-01-ideas-hub.dc.html', 'Ideas hub', m, 2120)
