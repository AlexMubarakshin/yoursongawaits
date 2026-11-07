from kit import *
yes_m = btn('Yes, show my video', 'by', full=True, tag='button', extra='border:2px solid #111')
no_m = btn('No, keep it private', 'bo', full=True, tag='button')
info = col(rowx(ico('eye'), t('On openyoursong’s site, social posts and ads, next to the song', 15)), rowx(ico('lock'), t('Saying no changes nothing: Max still gets your video', 15)), gap=12)
m = col(un('Can we show your reaction to other people', 26, tag='h1'), t('Your video is already on its way to Max. This is a separate question', 15, True), info,
        check('I’m 18 or older and everyone in the video agrees', False, 'a18'), small('You can take it back any time. We can’t delete copies other people already saved'), gap=20)
write('p-d-10-share-consent.dc.html', mobile('Gift: share consent', m_head('gift'), m, yes_m + no_m))
right = col(un('Can we show your reaction to other people', 40, tag='h1'), t('Your video is already on its way to Max. This is a separate question', 17, True), info,
            check('I’m 18 or older and everyone in the video agrees', False, 'a18d'),
            rowx(btn('Yes, show my video', 'by', tag='button', extra='border:2px solid #111'), btn('No, keep it private', 'bo', tag='button'), gap=12),
            small('You can take it back any time. We can’t delete copies other people already saved or shared'), gap=24)
h=900; ph=h-72-48
left = '<div style="height:%dpx">%s</div>' % (ph, img('r01', 'Your reaction video: Anna laughing with happy tears', ph, '50% 22%', r=28))
R = '<div style="display:flex;flex-direction:column;justify-content:center;min-height:%dpx;max-width:520px">%s</div>' % (ph, right)
write('p-d-10-share-consent-d.dc.html', desktop('Gift: share consent, desktop', d_head('gift'), left, R, h=h, split='1fr 1fr', pad='0 48px 48px 48px', gap=96, align='center'))
