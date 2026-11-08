from kit import *
# d12: notes as cut-paper letters, one per person, taped down. Personal, not a wall of text
NOTES = [('Kate', 'your daughter', 'Sixty and still beating us all at cards. I hope I get your nerve, and your luck'),
         ('Dad', 'your husband', 'Forty years and you still laugh at my jokes. Even the old ones. Especially the old ones'),
         ('Tom', 'your son', 'Thank you for every Sunday lunch, and for pretending not to see me take the last potato'),
         ('Lena', 'your daughter-in-law', 'Best granny in the world, says Mia. I agree with her'),
         ('Sam', 'your grandson', 'Your lemon cake, every single birthday. Please teach me before I leave for uni'),
         ('Ivy', 'your niece', 'You taught me to drive and never once shouted. I still check my mirrors because of you'),
         ('Max', 'the lodger', 'Happy 60th from the lodger who never left. Thank you for making it home')]
ROT = (-1.2, 0.8, -0.6, 1.1, -0.9, 0.6, -0.4)

def letter(i, who, rel, txt, big=False, d=False):
    tape = '<span aria-hidden="true" style="position:absolute;top:-10px;left:50%%;transform:translateX(-50%%) rotate(%.1fdeg);width:72px;height:20px;background:#FFD84D;opacity:.9;border-radius:2px"></span>' % (-ROT[i] * 2)
    av = '<span aria-hidden="true" class="un" style="width:36px;height:36px;border-radius:50%%;background:#111;color:#fff;display:flex;align-items:center;justify-content:center;font-size:15px;font-weight:500;flex-shrink:0">%s</span>' % who[0]
    sig = '<div style="display:flex;align-items:center;gap:10px">%s<div style="display:flex;flex-direction:column"><strong style="font-size:15px">%s</strong><span class="mut" style="font-size:13px">%s</span></div></div>' % (av, who, rel)
    q = '<p style="margin:0;font-size:%dpx;line-height:1.45">%s</p>' % ((26 if big else 21) if d else (20 if big else 17), txt)
    return ('<article style="position:relative;background:#fff;border:1px solid #DADADA;border-radius:6px;box-shadow:0 6px 16px rgba(17,17,17,.08);padding:28px 22px 20px;'
            'display:flex;flex-direction:column;gap:16px;transform:rotate(%.1fdeg)">%s%s%s</article>') % (ROT[i], tape, q, sig)

intro = lambda sz: col(small('For your 60th, from the family', extra='font-size:14px'), un('Notes from all 7 of us', sz, tag='h1'),
                       t('Everyone wrote one before the song was made. Some of their words are in it', 15 if sz < 40 else 17, True), gap=8)
paper = 'background:#F2F2F2;'
m = col(img('family', 'The family gathered around a phone at the table', 200, '50% 40%'), intro(30),
        col(*[letter(i, *n, big=(i == 0)) for i, n in enumerate(NOTES)], gap=28, extra='padding:32px 16px 24px;margin:0 -20px;background:#F2F2F2'),
        btn('Play the song again', 'bo', icon='play', full=True, tag='button'), gap=20, extra='padding-bottom:24px')
write('p-d-12-group-notes.dc.html', mobile('Gift: notes from everyone', m_head('gift'), m, btn('Make a song for someone', 'bo', full=True), h=1880))

cols = ['', '', '']
for i, n in enumerate(NOTES):
    cols[i % 3] += letter(i, *n, big=(i == 0), d=True)
grid = '<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:40px;align-items:start;background:#F2F2F2;border-radius:28px;padding:56px 48px">%s</div>' % ''.join('<div style="display:flex;flex-direction:column;gap:40px;padding-top:%dpx">%s</div>' % (k * 24, c) for k, c in enumerate(cols))
top = '<div style="display:grid;grid-template-columns:1fr 420px;gap:64px;align-items:center">%s%s</div>' % (col(intro(48), rowx(btn('Play the song again', 'bo', icon='play'), btn('Make a song for someone', 'bo'), gap=8), gap=24), img('family', 'The family gathered around a phone at the table', 240, '50% 40%', r=28))
write('p-d-12-group-notes-d.dc.html', doc('Gift: notes from everyone, desktop', 1440, 1200, d_head('gift') + '<main style="padding:48px 120px 64px;display:flex;flex-direction:column;gap:56px">%s%s</main>' % (top, grid)))
