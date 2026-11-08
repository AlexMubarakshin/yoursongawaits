from kit import *
# v62: one primary per screen (butter), shared "Tag us" block, clear order: the gift -> keep it -> share -> what next
def gift_d(name, title, photo, right, h=900, pos=None):
    ph = h - 72 - 48
    left = '<div style="height:%dpx">%s</div>' % (ph, img(photo[0], photo[1], ph, pos, r=28))
    R = '<div style="display:flex;flex-direction:column;justify-content:center;min-height:%dpx;max-width:540px">%s</div>' % (ph, right)
    write(name, desktop(title, d_head('gift'), left, R, h=h, split='1fr 1fr', pad='0 48px 48px 48px', gap=96, align='center'))

def two(a, b):
    return '<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px">%s%s</div>' % (a, b)

def make_card(title='Make one like this for someone you love', d=False):
    b = btn('Make a song', 'bo', sm=True)
    if d:
        return card(rowx('<div style="flex:1;display:flex;flex-direction:column;gap:4px">%s%s</div>' % (strong(title, 16), small('A song with their name in it, $29 · free preview first', mut=False)), b), pad=20)
    return card(strong(title, 16) + small('A song with their name in it, $29 · free preview first', mut=False) + b.replace('style="', 'style="align-self:flex-start;', 1), pad=20, gap=8)

# ---------- d06 song ended (recipient) ----------
CAP_S = 'Max and the whole flat made me a song for my 30th · made with @openyoursong'
thanks = lambda sz: card(un('Happy 30th, %s' % nm(white=True), sz) + t('“Thirty and still the first one dancing. Love you, the whole flat”', 15) + small('Your reaction is on its way to Max', mut=False), bg='#FFD84D', pad=24, r=24, gap=10)
keep = two(btn('Download MP3', 'bo', icon='down', full=True, tag='button', extra='padding:0 12px'), btn('Thank Max', 'bo', full=True, tag='button', extra='padding:0 12px'))
m = col(thanks(26), keep, col(strong('Share your song', 17), social_m(CAP_S, ('TikTok', 'WhatsApp', 'More')), gap=10), make_card(), gap=20, extra='padding-bottom:24px')
write('p-d-06-song-ended.dc.html', mobile('Gift: song ended', m_head('gift'), m, h=1240))
gift_d('p-d-06-song-ended-d.dc.html', 'Gift: song ended, desktop', ('candles', 'Candles on a 30th birthday cake'),
       col(thanks(32), keep, col(strong('Share your song', 18), social_d(CAP_S), gap=12), make_card(d=True),
           small('Made with AI + Max’s story · <a href="#">Remove my video</a> · <a href="#">Report</a>'), gap=20), h=1180)

# ---------- d15 post your reaction ----------
CAP_R = 'Max made me a song for my 30th. This was me hearing it the first time · made with @openyoursong'
m = col(un('Post your reaction', 30, tag='h1'), t('It’s on its way to Max. Want to share it yourself too?', 15, True),
        img('r01', 'Your reaction: Anna laughing with happy tears', 280, '50% 22%'),
        social_m(CAP_R, ('TikTok', 'X', 'Save video')), gap=16, extra='padding-bottom:24px')
write('p-d-15-post-reaction.dc.html', mobile('Gift: post your reaction', m_head('gift'), m, btn('Not now, back to my song', 'bo', full=True), h=1160))
gift_d('p-d-15-post-reaction-d.dc.html', 'Gift: post your reaction, desktop', ('r01', 'Your reaction: Anna laughing with happy tears'),
       col(un('Post your reaction', 48, tag='h1'), t('It’s on its way to Max. Want to share it yourself too? We made a Stories version with your song playing under it', 17, True),
           social_d(CAP_R), btn('Not now, back to my song', 'bo', extra='align-self:flex-start'), gap=20), h=1000, pos='50% 22%')

# ---------- e09 participant page later ----------
CAP_P = 'We made Mum a song for her 60th, 7 of us wrote it together · made with @openyoursong'
m = col(small('Mum’s 60th · from the family'), un('Mum opened it', 30, tag='h1'), small('Sun 14 March at 10:15'),
        img('r06', 'Mum smiling with a happy tear over a lemon cake', 240, '50% 22%'),
        two(btn('Her reaction', 'bo', icon='play', full=True, tag='button', extra='padding:0 12px'), btn('The song', 'bo', icon='play', full=True, tag='button', extra='padding:0 12px')),
        col(strong('Share the moment', 17), social_m(CAP_P, ('TikTok', 'WhatsApp', 'More')), gap=10),
        make_card(), gap=16, extra='padding-bottom:24px')
write('p-e-09-participant-later.dc.html', mobile('Group: participant page after opening', m_head('gift'), m, h=1300))
write('p-e-09-participant-later-d.dc.html', desktop('Group: participant page after opening, desktop', d_head('gift'),
    col(small('Mum’s 60th · from the family'), un('Mum opened it', 48, tag='h1'), t('Sun 14 March at 10:15. She recorded her reaction for all of you', 18, True),
        two(btn('Play her reaction', 'bo', icon='play', full=True), btn('Listen to the song', 'bo', icon='play', full=True)),
        col(strong('Share the moment', 18), social_d(CAP_P), gap=12), make_card('Make one like this for someone of yours', d=True), gap=24),
    img('r06', 'Mum smiling with a happy tear over a lemon cake', 900, '50% 22%', r=28), h=1060, split='1fr 1fr', pad='48px 96px 0 96px', gap=96))

# ---------- e06 reaction received (giver) ----------
CAP_G = 'Made Anna a song for her 30th. Her face when she heard her name · made with @openyoursong'
def consent(d=False):
    thumb = '<div class="ph" style="width:56px;height:56px;border-radius:50%%;flex-shrink:0"><img src="/_blob/%s" alt="" style="object-position:50%% 22%%"></div>' % IMG['r01']
    head = '<div style="display:flex;gap:14px;align-items:center">%s%s</div>' % (thumb, col(strong('Anna said yes to sharing her video', 17), '<span style="font-size:14px;line-height:1.45">Can we show it with her song too? Moments like hers help other people find the words. We never show your email</span>', gap=4))
    acts = '<div style="display:flex;gap:8px">%s%s</div>' % (btn('Yes, show it', 'bi', sm=True, tag='button', extra='flex:1' if not d else ''), btn('Not this one', 'bw', sm=True, tag='button', extra=('flex:1;' if not d else '') + 'border:2px solid #111'))
    return card(head + acts, bg='#FFD84D', pad=20, gap=16)
def nexts_m():
    tile = lambda obj, title, sub: '<a href="#" style="text-decoration:none;color:#111;border-radius:20px;background:#F2F2F2;padding:16px;display:flex;flex-direction:column;gap:12px">%s<div style="display:flex;flex-direction:column;gap:2px"><strong style="font-size:15px;line-height:1.3">%s</strong><span class="mut" style="font-size:13px;line-height:1.4">%s</span></div></a>' % (obj, title, sub)
    plus = '<div aria-hidden="true" style="width:44px;height:52px;border-radius:12px;background:#fff;border:2px solid #111;display:flex;align-items:center;justify-content:center">%s</div>' % ico('play', '#111', 18)
    return '<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px">%s%s</div>' % (tile(datetile('MAR', '14', 44), 'Add her birthday to your calendar', 'Never miss it next year'), tile(plus, 'Make another song', 'For Mum, a friend, the team'))
def nexts(d=False):
    cal = calendar_card(title='Never miss her birthday again', sub='Add 14 March to your calendar, with a link back here for next year’s song', mobile=not d, quiet=True, link='Or email me before')
    mk = card('<div style="display:flex;gap:16px;align-items:flex-start">%s%s</div>' % (pdfthumb(44) if False else '<div aria-hidden="true" style="width:56px;height:56px;flex-shrink:0;border-radius:12px;background:#fff;border:2px solid #111;display:flex;align-items:center;justify-content:center">%s</div>' % ico('play', '#111', 22),
              col(strong('Make a song for someone else', 17), '<span style="font-size:14px;line-height:1.45">Mum, a friend, the team. Free preview first, same as Anna’s</span>', gap=4)) + btn('Make another song', 'bo', sm=True, tag='a', extra='' if d else 'width:100%'), bg='#F2F2F2', pad=20, gap=16)
    return col(strong('Next', 18), ('<div style="display:grid;grid-template-columns:1fr 1fr;gap:16px">%s%s</div>' if d else '%s%s') % (cal, mk), gap=12)

m = col(col(un('%s sent you her reaction' % nm(), 28, tag='h1'), small('Opened Sun 14 March, 09:02 · only you can see it', extra='font-size:14px'), gap=8),
        img('r01', 'Anna laughing with happy tears in her kitchen', 280, '50% 22%'),
        two(btn('Play', 'bo', icon='play', full=True, tag='button'), btn('Download', 'bo', icon='down', full=True, tag='button')),
        nexts_m(),
        consent(),
        col(strong('Share it', 17), small('It’s Anna’s face, so check she’s happy for you to post it', extra='font-size:14px'), social_m(CAP_G, ('TikTok', 'X', 'More')), gap=10), gap=24, extra='padding-bottom:24px')
write('p-e-06-reaction.dc.html', mobile('Account: reaction received', m_head('account', right='Orders'), m, h=1900, pad_top=24))
right = col(col(un('%s sent you her reaction' % nm(), 48, tag='h1'), t('She opened your song on Sun 14 March at 09:02. Only you can see this video', 18, True), gap=12),
            rowx(btn('Play her reaction', 'bo', icon='play'), btn('Download', 'bo', icon='down'), gap=8),
            nexts(True),
            consent(True),
            col(strong('Share it', 18), small('It’s Anna’s face, so check she’s happy for you to post it', extra='font-size:14px'), social_d(CAP_G), gap=12), gap=28)
body = '<main style="display:grid;grid-template-columns:480px 1fr;gap:80px;padding:56px 120px 0;align-items:start">%s%s</main>' % (img('r01', 'Anna laughing with happy tears in her kitchen', 640, '50% 22%', r=28), right)
write('p-e-06-reaction-d.dc.html', doc('Account: reaction received, desktop', 1440, 1400, d_head('account', right='Orders') + body))
