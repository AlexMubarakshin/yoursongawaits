from kit import *
# Reaction received (giver): one clear story, top to bottom
# 1. what happened  2. watch it  3. share it (one lead action)  4. one small question  5. quiet next steps

def share_row_d():
    lead = '<button class="btn bk" style="gap:10px">%sSave the video</button>' % soc('Save video', 20).replace('#111', '#fff')
    return '<div style="display:flex;align-items:center;gap:8px">%s%s</div>' % (lead, ''.join(iconbtn(r) for r in ('X', 'Facebook', 'Copy link')))

ask = lambda pad: frame(
    '<div style="display:flex;align-items:center;gap:16px;flex-wrap:wrap"><span style="flex:1;min-width:220px;font-size:15px;line-height:1.45">Anna is happy for us to show her video with the song. Are you?</span>%s</div>' % rowx(btn('No', 'bo', sm=True, tag='button'), btn('Yes', sm=True, tag='button'), gap=8),
    pad=pad, gap=0)
nexts = '<div style="display:flex;gap:24px;font-size:15px"><a href="#">Remind me before her next birthday</a><a href="#">Make another song</a></div>'

# desktop
right = col(
    col(un('%s sent you her reaction' % nm(), 48, tag='h1'), t('She opened your song on Sun 14 March at 09:02. Only you can see this video', 18, True), gap=12),
    rowx(btn('Play her reaction', icon='play'), btn('Download', 'bo', icon='down'), gap=8),
    '<div class="hr"></div>',
    col(strong('Share it', 18), small('It’s Anna’s face, so check she’s happy for you to post it', extra='font-size:14px'), share_row_d(), tagline(), gap=12),
    ask(20), nexts, gap=28)
body = '<main style="display:grid;grid-template-columns:480px 1fr;gap:80px;padding:56px 120px 0;align-items:start">%s%s</main>' % (img('r01', 'Anna laughing with happy tears in her kitchen', 640, '50% 22%', r=28), right)
write('p-e-06-reaction-d.dc.html', doc('Account: reaction received, desktop', 1440, 800, d_head('account', right='Orders') + body))

# mobile
m = col(col(un('%s sent you her reaction' % nm(), 28, tag='h1'), small('Opened Sun 14 March, 09:02 · only you can see it', extra='font-size:14px'), gap=8),
        img('r01', 'Anna laughing with happy tears in her kitchen', 300, '50% 22%'),
        '<div style="display:grid;grid-template-columns:1fr 1fr;gap:8px">%s%s</div>' % (btn('Play', icon='play', full=True, tag='button'), btn('Download', 'bo', icon='down', full=True, tag='button')),
        '<div class="hr"></div>',
        col(strong('Share it', 17), small('It’s Anna’s face, so check she’s happy for you to post it', extra='font-size:14px'), share_m(('TikTok', 'X', 'More')), gap=10),
        ask(16), col('<a href="#" style="font-size:15px">Remind me before her next birthday</a>', '<a href="#" style="font-size:15px">Make another song</a>', gap=12), gap=20, extra='padding-bottom:24px')
write('p-e-06-reaction.dc.html', mobile('Account: reaction received', m_head('account', right='Orders'), m, h=1240, pad_top=24))
