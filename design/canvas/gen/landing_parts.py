# Shared landing parts (desktop + mobile) for v62
B = {'e1':'f2f411ec00795b0ea6ea67c498d9ebd2','e2':'622571a5efec9dcfab9862a7f3332a70','e3':'b84a9519552c7276a7f67d913a01ed45','e4':'ca7740159a99c62c8060e76efe18a779',
     'r01':'2744d11a0bc2b86bbfb658477ac52617','bed':'e354aac9a424c73c0156013efdeaf1bd','mum':'b84a9519552c7276a7f67d913a01ed45','f1':'753681caffaf93a756329748141b4104',
     'r06':'e0bf68270375990a6c155c753ae64c80','o1':'84d89a78197fb53d36fc38f060588b8c','box':'2892b385f1c5f1e8dedf7df3815e506f',
     'n1':'14e5fc82d8e091b7c2c5e95a5d6fb907','n2':'1b8a12e55b48d782ad0aed8eb47242db','n3':'3015cceae11db6c90f56093d73001aff','n4':'f5a721339c23682eaaeb28b20b3d3277','p1':'a3f42c6f3111ab5d35fc884beb5eaeac','p2':'8818f91654a75b17e7baedc093c10a73','p3':'581229994cf2e1b007e71612e725066d'}
PLAY = '<svg aria-hidden="true" width="16" height="16" viewBox="0 0 24 24"><path d="M7 4.5l10 7.5-10 7.5z" fill="none" stroke="#fff" stroke-width="2" stroke-linejoin="round"></path></svg>'
CHECK = '<svg aria-hidden="true" width="14" height="14" viewBox="0 0 24 24"><path d="M5 12.5l4.5 4.5L19 7.5" fill="none" stroke="#111" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"></path></svg>'
SONGS = [('n1', 'A man in his sixties laughing at his song on his birthday, cake and family around him', 'Sixty miles of Walt', 'For Dad, 60th · country', 'Walt', ', sixty miles and still the open road', '0:42'),
         ('n2', 'A woman with flowers smiling at the song on her phone on Mother’s Day', 'Sunday pancakes for Rosa', 'For Mum, Mother’s Day · acoustic', 'Rosa', ', pancakes on a Sunday, flipped too high', '0:38'),
         ('n3', 'Newlyweds laughing on the steps, sharing one phone', 'Sam and Jo, row 42', 'For the newlyweds · indie pop', 'Sam and Jo', ', row forty-two', '0:40'),
         ('n4', 'A woman laughing at her retirement song, colleagues with balloons and a cake around her', 'Twenty years, Bev', 'For a colleague, retirement · swing', 'Bev', ', twenty years and the kettle’s still on', '0:44')]

def song_card(k, alt, title, sub, name, line, dur, w=None, ph=240):
    ws = 'width:%dpx;flex-shrink:0;' % w if w else ''
    return ('<article style="%sdisplay:flex;flex-direction:column;gap:14px">'
            '<div class="ph" style="height:%dpx;border-radius:20px"><img src="/_blob/%s" alt="%s"></div>'
            '<div style="display:flex;flex-direction:column;gap:4px"><strong class="un" style="font-size:20px;font-weight:500;line-height:1.2">%s</strong><span class="mut" style="font-size:14px">%s</span></div>'
            '<p style="margin:0;font-size:16px;line-height:1.45"><span style="background:#FFD84D;padding:0 4px;border-radius:3px;font-weight:500">%s</span>%s</p>'
            '<div style="display:flex;align-items:center;gap:12px"><button class="play" aria-label="Play %s" style="width:44px;height:44px">%s</button><span class="mut" style="font-size:14px;font-variant-numeric:tabular-nums">%s</span></div></article>') % (ws, ph, B[k], alt, title, sub, name, line, title, PLAY, dur)

def feed(mobile=False):
    head = '<h2 class="un h2" style="margin-bottom:%dpx;%s">Listen to a few first</h2>' % (20 if mobile else 36, 'font-size:30px' if mobile else '')
    if mobile:
        row = '<div style="display:flex;gap:16px;overflow-x:auto;margin:0 -20px;padding:0 20px 4px;scrollbar-width:none">%s</div>' % ''.join(song_card(*s, w=260, ph=220) for s in SONGS)
        return '<section id="examples" style="padding:0 20px 48px">%s%s</section>' % (head, row)
    row = '<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:24px">%s</div>' % ''.join(song_card(*s) for s in SONGS)
    return '<section id="examples" style="padding:16px 64px 96px">%s%s</section>' % (head, row)

QUOTES = [('I played it in the car on her birthday. She made me play it four more times, then sent it to her whole team', 'Priya', 'for her sister, 30th', 'p1'),
          ('Dad doesn’t cry. Dad cried. He knows every word now and sings the bit about the truck', 'Tom', 'for his dad, 60th', 'p2'),
          ('Twelve of us each wrote a line for Bev. She said it was the best leaving present in twenty years', 'Hannah', 'for a colleague, retirement', 'p3')]
def reviews(mobile=False):
    def q(txt, who, what, ph):
        return ('<figure style="margin:0;border-radius:24px;background:#F2F2F2;padding:%s;display:flex;flex-direction:column;justify-content:space-between;gap:24px">'
                '<blockquote style="margin:0;font-size:%dpx;line-height:1.45">“%s”</blockquote>'
                '<figcaption style="display:flex;align-items:center;gap:12px"><span class="ph" style="width:48px;height:48px;border-radius:50%%;flex-shrink:0;display:block"><img src="/_blob/%s" alt=""></span><span style="display:flex;flex-direction:column"><strong style="font-size:15px">%s</strong><span class="mut" style="font-size:14px">%s</span></span></figcaption></figure>') % ('24px' if mobile else '32px', 17 if mobile else 20, txt, B[ph], who, what)
    h = '<h2 class="un h2" style="margin-bottom:%dpx;%s">What people said after</h2>' % (20 if mobile else 36, 'font-size:30px' if mobile else '')
    if mobile:
        return '<section style="padding:0 20px 48px">%s<div style="display:flex;flex-direction:column;gap:12px">%s</div></section>' % (h, ''.join(q(*x) for x in QUOTES))
    return '<section style="padding:0 64px 96px">%s<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:20px">%s</div></section>' % (h, ''.join(q(*x) for x in QUOTES))

def perks(items, mobile=False):
    li = ''.join('<li style="display:flex;gap:12px;align-items:flex-start;padding:12px 0;border-top:1px solid rgba(17,17,17,.12)"><span style="width:22px;height:22px;border-radius:50%%;background:#fff;display:flex;align-items:center;justify-content:center;flex-shrink:0;margin-top:1px">%s</span><span style="line-height:1.45">%s</span></li>' % (CHECK, x) for x in items)
    return '<ul style="margin:0;padding:0;list-style:none;display:flex;flex-direction:column;font-size:%dpx">%s</ul>' % (16 if mobile else 17, li)

def sees(mobile=False):
    H = 280 if mobile else 360
    def step(n, title, sub, key, alt, pos, row):
        head = '<div style="display:flex;gap:12px;align-items:flex-start"><span class="un" style="width:32px;height:32px;border-radius:50%%;background:#FFD84D;display:flex;align-items:center;justify-content:center;font-size:15px;font-weight:500;flex-shrink:0">%d</span><div style="display:flex;flex-direction:column;gap:4px"><strong style="font-size:18px">%s</strong><span class="mut" style="font-size:15px;line-height:1.45">%s</span></div></div>' % (n, title, sub)
        pic = '<div class="ph" style="height:%dpx;border-radius:24px"><img src="/_blob/%s" alt="%s" style="object-position:%s"></div>' % (H, B[key], alt, pos)
        return '<div style="display:flex;flex-direction:column;gap:16px">%s%s<div style="height:56px;display:flex;align-items:center;gap:12px;padding:0 4px">%s</div></div>' % (head, pic, row)
    play = '<span style="width:44px;height:44px;border-radius:50%%;background:#111;display:flex;align-items:center;justify-content:center;flex-shrink:0">%s</span>' % PLAY
    s = [step(1, 'Until the day, a countdown', 'Any day up to a year ahead, in her time zone', 'bed', 'A wrapped gift by a bedside clock in a sunny bedroom', '50% 50%',
              '<span class="mut" style="font-size:15px">Opens in</span><span class="un" style="font-size:28px;font-weight:500;line-height:1;font-variant-numeric:tabular-nums">2 days 14 h</span>'),
         step(2, 'At 09:00 she opens her gift', 'The song, the lyrics and a note from Max', 'box', 'The gift: a tangerine box with a blue ribbon and paper confetti', '50% 50%',
              play + '<span class="un" style="font-size:22px;font-weight:500">Hey <span style="background:#FFD84D;padding:0 6px;border-radius:3px">Anna</span></span>'),
         step(3, 'Her reaction comes back to you', 'If she says yes. Only you see it', 'r01', 'Anna in her kitchen with happy tears', '50% 22%',
              play + '<span style="display:flex;flex-direction:column"><strong style="font-size:16px">Her reaction</strong><span class="mut" style="font-size:14px;font-variant-numeric:tabular-nums">1:24 · only you see it</span></span>')]
    h = '<h2 class="un h2" style="margin-bottom:%dpx;max-width:820px;%s">What Anna sees, and what comes back to you</h2>' % (24 if mobile else 40, 'font-size:30px' if mobile else '')
    if mobile:
        return '<section style="padding:48px 20px">%s<div style="display:flex;flex-direction:column;gap:32px">%s</div></section>' % (h, ''.join(s))
    return '<section style="padding:96px 64px">%s<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:24px">%s</div></section>' % (h, ''.join(s))
