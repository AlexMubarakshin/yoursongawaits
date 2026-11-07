from kit import *
OUT = []

def gift_d(name, title, photo, right, h=900, pos=None):
    ph = h - 72 - 48
    left = '<div style="height:%dpx">%s</div>' % (ph, img(photo[0], photo[1], ph, pos, r=28))
    R = '<div style="display:flex;flex-direction:column;justify-content:center;min-height:%dpx;max-width:540px">%s</div>' % (ph, right)
    OUT.append(write(name, desktop(title, d_head('gift'), left, R, h=h, split='1fr 1fr', pad='0 48px 48px 48px', gap=96, align='center')))

def two(a, b):
    return '<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px">%s%s</div>' % (a, b)

MAKE_M = card(strong('Make one like this for someone you love', 16) + small('A song with their name in it, $29 · free preview first', mut=False) + btn('Make a song', sm=True, extra='align-self:flex-start'), pad=20, gap=8)

# ---------- d06 song ended (recipient), mobile + desktop ----------
thanks = card(un('Happy 30th, %s' % nm(white=True), 26) + t('“Thirty and still the first one dancing. Love you, the whole flat”', 15) + small('Reaction sent to Max', mut=False), bg='#FFD84D', pad=24, r=24, gap=10)
m = col(thanks,
        two(btn('Download MP3', icon='down', full=True, tag='button', extra='padding:0 12px'), btn('Thank Max', 'bo', full=True, tag='button', extra='padding:0 12px')),
        col(strong('Share your song', 16), share_m(('TikTok', 'WhatsApp', 'More')), gap=10),
        MAKE_M, gap=16, extra='padding-bottom:24px')
OUT.append(write('p-d-06-song-ended.dc.html', mobile('Gift: song ended', m_head('gift'), m, h=1000)))
gift_d('p-d-06-song-ended-d.dc.html', 'Gift: song ended, desktop', ('candles', 'Candles on a 30th birthday cake'),
       col(thanks.replace('font-size:26px', 'font-size:32px'),
           two(btn('Download MP3', icon='down', full=True, tag='button'), btn('Thank Max', 'bo', full=True, tag='button')),
           col(strong('Share your song', 17), share_d(), gap=12),
           card(rowx('<div style="flex:1;display:flex;flex-direction:column;gap:4px">' + strong('Make one like this for someone you love', 16) + small('A song with their name in it, $29 · free preview first', mut=False) + '</div>', btn('Make a song', sm=True)), pad=20, gap=8),
           small('Made with AI + Max’s story · <a href="#">Remove my video</a> · <a href="#">Report</a>'), gap=16), h=1040)

# ---------- d15 post your reaction (recipient, after send) ----------
CAP_R = 'Max made me a song for my 30th. This was me hearing it the first time · made with @openyoursong'
m = col(un('Post your reaction', 30, tag='h1'), t('It’s on its way to Max. Want to share it yourself too?', 15, True),
        img('r01', 'Your reaction: Anna laughing with happy tears', 280, '50% 22%'),
        share_m(('TikTok', 'X', 'Save video'), CAP_R), gap=14, extra='padding-bottom:24px')
OUT.append(write('p-d-15-post-reaction.dc.html', mobile('Gift: post your reaction', m_head('gift'), m, btn('Not now, back to my song', 'bo', full=True), h=1000)))
gift_d('p-d-15-post-reaction-d.dc.html', 'Gift: post your reaction, desktop', ('r01', 'Your reaction: Anna laughing with happy tears'),
       col(un('Post your reaction', 48, tag='h1'), t('It’s on its way to Max. Want to share it yourself too? We made a Stories version with your song playing under it', 17, True),
           share_d(CAP_R),
           btn('Not now, back to my song', 'bo', extra='align-self:flex-start'), gap=16), h=980, pos='50% 22%')

# ---------- Story assets (1080x1920 shown at 540x960) ----------
def story(name, title, photo, pos, top, big, foot):
    body = ('%s<div style="height:400px;background:#FFD84D;padding:28px;display:flex;flex-direction:column;justify-content:space-between;gap:12px">'
            '<div style="display:flex;flex-direction:column;gap:12px">%s%s</div>'
            '<div style="display:flex;align-items:center;justify-content:space-between"><span class="un" style="font-size:18px;font-weight:500">@openyoursong</span><span style="font-size:14px;font-weight:500">%s</span></div></div>') % (
        img(photo, title, 560, pos, r=0), top, big.replace('background:#FFD84D', 'background:#fff'), foot)
    OUT.append(write(name, doc(title, 540, 960, body)))
story('p-d-16-story-song.dc.html', 'Story card: the song, 1080×1920', 'box', None,
      '<span style="font-size:14px" class="mut">Now playing</span><p class="un" style="margin:0;font-size:24px;font-weight:500;line-height:1.2">Max made me a song for my 30th</p>',
      lyric(26), 'Link sticker: hear it')
story('p-d-17-story-reaction.dc.html', 'Story card: the reaction, 1080×1920', 'r01', '50% 22%',
      '<p class="un" style="margin:0;font-size:22px;font-weight:500;line-height:1.2">Me hearing the song Max made me</p>',
      lyric(22), 'Make one for yours')

# ---------- e06 reaction received (giver) ----------
CAP_G = 'Made Anna a song for her 30th. Her face when she heard her name · made with @openyoursong'
m = col(un('%s sent you her reaction' % nm(), 28, tag='h1'), small('She opened it on Sun 14 March at 09:02'),
        img('r01', 'Anna laughing with happy tears in her kitchen', 260, '50% 22%'),
        two(btn('Play', icon='play', full=True, tag='button'), btn('Download', 'bo', icon='down', full=True, tag='button')),
        col(strong('Share it', 16), notice('It’s Anna’s face. Check she’s happy for you to post it'), share_m(('TikTok', 'X', 'More')), gap=10),
        card(strong('Anna said we can show it with the song', 16) + small('Your story and names are in it, so we ask you too. Saying no changes nothing', mut=False) + two(btn('No', 'bo', sm=True, full=True, tag='button'), btn('Yes, show it', sm=True, full=True, tag='button')), bg='#F2F2F2', pad=20, gap=10),
        card(strong('Her birthday comes back every year', 16) + small('One free reminder next year, or every date on a plan', mut=False) + btn('Remind me next year', sm=True, extra='align-self:flex-start'), pad=20, gap=8),
        gap=16, extra='padding-bottom:24px')
OUT.append(write('p-e-06-reaction.dc.html', mobile('Account: reaction received', m_head('account', right='Orders'), m, h=1460, pad_top=24)))
body = col(un('%s sent you her reaction' % nm(), 48, tag='h1'),
           '<div style="display:grid;grid-template-columns:420px 1fr;gap:48px;align-items:start">%s%s</div>' % (
               col(img('r01', 'Anna laughing with happy tears in her kitchen', 520, '50% 22%', r=28), two(btn('Play', icon='play', full=True, tag='button'), btn('Download', 'bo', icon='down', full=True, tag='button')), gap=12),
               col(t('She opened it on Sun 14 March at 09:02. Only you can see it until you share it', 17),
                   col(strong('Share it', 18), notice('It’s Anna’s face. Check she’s happy for you to post it'), share_d(CAP_G), gap=12),
                   card(strong('Anna said we can show her video with the song', 17) + t('Your story and names are in it, so we ask you too. Saying no changes nothing', 15) + rowx(btn('Yes, show it', sm=True), btn('No', 'bo', sm=True), gap=8), bg='#F2F2F2', pad=24, gap=10),
                   card(rowx('<div style="flex:1;display:flex;flex-direction:column;gap:4px">' + strong('Her birthday comes back every year', 16) + small('One free reminder next year, or every date on a plan with cheaper songs', mut=False) + '</div>', btn('Remind me', sm=True), btn('Make another song', 'bo', sm=True), gap=12), pad=24, gap=8), gap=20)), gap=32)
OUT.append(write('p-e-06-reaction-d.dc.html', desktop('Account: reaction received, desktop', d_head('account', right='Orders'), body, None, h=1240, pad='48px 120px 0 120px')))

# ---------- e09 participant page later ----------
CAP_P = 'We made Mum a song for her 60th, 7 of us wrote it together · made with @openyoursong'
m = col(small('Mum’s 60th · from the family'), un('Mum opened it', 30, tag='h1'), small('Sun 14 March at 10:15'),
        img('r06', 'Mum smiling with a happy tear over a lemon cake', 240, '50% 22%'), rowx(play('Play Mum’s reaction'), strong('Her reaction, 1:10', 16)),
        col(strong('Share the moment', 16), share_m(('TikTok', 'WhatsApp', 'More')), gap=10),
        MAKE_M, gap=14, extra='padding-bottom:24px')
OUT.append(write('p-e-09-participant-later.dc.html', mobile('Group: participant page after opening', m_head('gift'), m, h=1180)))
OUT.append(write('p-e-09-participant-later-d.dc.html', desktop('Group: participant page after opening, desktop', d_head('gift'),
    col(small('Mum’s 60th · from the family'), un('Mum opened it', 48, tag='h1'), t('Sun 14 March at 10:15. She recorded her reaction for all of you', 18, True),
        two(btn('Play her reaction', icon='play', full=True), btn('Listen to the song', 'bo', full=True)),
        col(strong('Share the moment', 17), share_d(CAP_P), gap=12),
        card(rowx('<div style="flex:1">' + strong('Make one like this for someone of yours', 16) + '</div>', btn('Make a song', sm=True)), pad=20), gap=20),
    img('r06', 'Mum smiling with a happy tear over a lemon cake', 840, '50% 22%', r=28), h=1000, split='1fr 1fr', pad='48px 96px 0 96px', gap=96)))

# ---------- c12 order after opened: add share ----------
m = col(un('%s opened it' % nm(), 30, tag='h1'), small('Sun 14 March at 09:02'),
        img('r01', 'Anna laughing with happy tears in her kitchen', 220, '50% 22%'),
        two(btn('Play reaction', icon='play', full=True, tag='button', extra='padding:0 12px'), btn('Share it', 'bo', icon='share', full=True, tag='button', extra='padding:0 12px')),
        card(strong('Remind me next year', 16) + small('One free reminder before her birthday', mut=False) + btn('Remind me', 'bk', sm=True, extra='align-self:flex-start'), bg='#FFD84D', pad=20, gap=8), gap=16)
OUT.append(write('p-c-12-after-opened.dc.html', mobile('Order: after Anna opened it', m_head('order'), m, btn('Make another song', 'bo', full=True))))

# ---------- Growth loop board ----------
def node(title, sub, val, gain, bg='#F2F2F2', w=270):
    return ('<div style="width:%dpx;border-radius:20px;background:%s;padding:20px;display:flex;flex-direction:column;gap:10px">'
            '<strong class="un" style="font-size:18px;font-weight:500;line-height:1.2">%s</strong><span class="mut" style="font-size:13px;line-height:1.4">%s</span>'
            '<div style="display:flex;flex-direction:column;gap:6px;padding-top:10px;border-top:1px solid rgba(17,17,17,.12);font-size:13px;line-height:1.4">'
            '<span><strong>User gets</strong> · %s</span><span><strong>We get</strong> · %s</span></div></div>') % (w, bg, title, sub, val, gain)
arrow = '<svg aria-hidden="true" width="48" height="24" viewBox="0 0 48 24" style="flex-shrink:0"><path d="M2 12h40M34 5l8 7-8 7" fill="none" stroke="#111" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path></svg>'
row1 = rowx(node('Found us', 'Landing, occasion page, a friend’s Story, a gift they received', 'An idea for a gift that feels personal', 'A visitor with gift intent', '#FFD84D'), arrow,
            node('Made a song', 'Story, free preview, name check', 'Hears their name sung before paying', 'Email, story, occasion date'), arrow,
            node('Paid and sent', '$29 or $55, the day and time they pick', 'A gift that arrives on time', 'Revenue, recipient email'), arrow,
            node('Recipient opens', 'Gift page, song, notes', 'A song with their name, from people who love them', 'A new person sees the product', '#FFD84D'), gap=12, align='stretch')
row2 = rowx(node('Reaction recorded', 'Two consents, only the giver sees it', 'Their moment saved', 'The strongest proof we have'), arrow,
            node('Shared with a tag', 'Stories, TikTok, X with @openyoursong, from recipient, giver and the group', 'Friends see the moment', 'Free reach and content to repost', '#FFD84D'), arrow,
            node('Shown on our site', 'Only with recipient and giver consent', 'Their story featured, if they want it', 'Ads and landing proof'), arrow,
            node('Next song', '“Make one like this”, remind next year, calendar plan', 'Never miss a date, cheaper songs on a plan', 'Repeat orders and new givers', '#FFD84D'), gap=12, align='stretch')
legend = small('Every end screen has one of three exits: share with a tag, make a song for someone, or remember the next date. Group gifts multiply each step by up to 20 people')
loop = col(un('Growth loop: where the user gets value and where we do', 48, tag='h1'), legend, row1,
           '<div style="display:flex;justify-content:flex-end;padding-right:140px"><svg aria-hidden="true" width="24" height="56" viewBox="0 0 24 56"><path d="M12 2v48M5 42l7 8 7-8" fill="none" stroke="#111" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path></svg></div>',
           row2,
           '<div style="display:flex;align-items:center;gap:12px;padding:16px 20px;border:2px dashed #111;border-radius:20px"><svg aria-hidden="true" width="24" height="24" viewBox="0 0 24 24"><path d="M20 11a8 8 0 10-2.3 5.7M20 4v7h-7" fill="none" stroke="#111" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path></svg><span style="font-size:15px;line-height:1.4"><strong>Back to the start.</strong> A shared Story, a “make one like this” tap or a calendar reminder each lands on a page with the occasion and attribution filled in (FR-2.8, FR-12.2)</span></div>', gap=28)
OUT.append(write('p-g-01-growth-loop.dc.html', doc('Growth loop', 1440, 900, '<main style="padding:64px">%s</main>' % loop)))
