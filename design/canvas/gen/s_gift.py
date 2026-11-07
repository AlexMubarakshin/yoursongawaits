from kit import *
OUT = []

def gift_d(name, title, photo, right, h=900, pos=None, banner=''):
    ph = h - 72 - 48 - (48 if banner else 0)
    left = '<div style="height:%dpx">%s</div>' % (ph, img(photo[0], photo[1], ph, pos, r=28))
    R = '<div style="display:flex;flex-direction:column;justify-content:center;min-height:%dpx;max-width:520px">%s</div>' % (ph, right)
    OUT.append(write(name, desktop(title, banner + d_head('gift'), left, R, h=h, split='1fr 1fr', pad='0 48px 48px 48px', gap=96, align='center')))

def gm(name, title, main, bar=None, h=844, banner=''):
    OUT.append(write(name, mobile(title, banner + m_head('gift'), main, bar, h)))

COVER = ('box', 'Gift cover: a tangerine gift box with a blue ribbon and paper confetti')

# d01 waiting
gift_d('p-d-01-waiting-d.dc.html', 'Gift: waiting screen, desktop', ('bed', 'A wrapped gift by a bedside clock in a sunny bedroom'),
       col(small('A gift for Anna from Max', extra='font-size:15px'), un('Something from Max is wrapped and waiting', 48, tag='h1'),
           card(countdown(56) + strong('Opens Sunday 14 March at 9:00 AM, London time', 16), bg='#FFD84D', pad=32, r=28, gap=20),
           rowx(btn('Add to calendar', 'bo', icon='cal'), gap=12), small('The song stays wrapped until then, even with the link'), gap=24))

# d02 first screen
gift_d('p-d-02-gift-first-screen-d.dc.html', 'Gift: first screen, desktop', COVER,
       col(un('Max made you something', 64, tag='h1', extra='font-weight:800'), t('From Max and the whole flat, for your 30th', 20, True),
           rowx(btn('Open', icon='play', extra='height:64px;padding:0 40px;font-size:19px'), small('Turn the sound on'), gap=20),
           small('Made with AI + Max’s story · <a href="#">How it’s made</a>'), gap=28))

# d03 consent 1
gift_d('p-d-03-reaction-consent-d.dc.html', 'Gift: reaction consent, desktop', ('r09', 'Anna laughing as she looks at her phone'),
       col(un('Max would love to see you open it', 48, tag='h1'), t('Record a short video of your reaction? Only Max will see it', 18, True),
           col(rowx(ico('clock'), t('Up to 90 seconds, stop any time', 16)), rowx(ico('lock'), t('Stays on this device until you choose send or delete', 16)), rowx(ico('eye'), t('Private by default, never public', 16)), gap=12),
           check('I’m 16 or older, or my parent is with me', False, 'age'),
           rowx(btn('Record and open', icon='cam'), btn('Just open it', 'bo'), gap=12), gap=24))

# d04 playing + recording
rec = '<div style="display:flex;align-items:center;gap:10px;background:#fff;border:1px solid #DADADA;border-radius:12px;padding:6px 6px 6px 14px"><span style="width:10px;height:10px;border-radius:50%;background:#FF7A00"></span><span class="tn" style="font-size:14px;font-weight:500">Recording 0:42</span>' + btn('Stop', 'bk', sm=True, tag='button', extra='height:36px;padding:0 14px') + '</div>'
lyr = ''.join('<p style="margin:0;font-size:%dpx;line-height:1.4;%s">%s</p>' % s for s in (
    (20, 'color:#8A8A8A', 'Kettle on at six, the flat still asleep'),
    (32, 'font-family:Unbounded,Inter,sans-serif;font-weight:500', '%s, you still ride that yellow bike' % nm()),
    (20, 'color:#8A8A8A', 'down Elm Street like it’s summer every night')))
gift_d('p-d-04-song-playing-d.dc.html', 'Gift: song playing, desktop', ('r05', 'Anna on her bed, moved, listening to the song'),
       col(rowx(small('Your song from Max'), '<span style="flex:1"></span>', rec), col(lyr, gap=16), player('1:02', '2:48', 37, 'Pause'), small('Your reaction is recording on this device only. Nothing is sent yet'), gap=32))

# d05 review reaction
gift_d('p-d-05-review-reaction-d.dc.html', 'Gift: review reaction, desktop', ('r01', 'Your reaction video: Anna laughing with happy tears'),
       col(un('Here’s your reaction', 48, tag='h1'), t('It’s still only on this device. Send it to Max, or delete it', 18, True), rowx(play('Play your reaction', 48), small('1:24 · recorded just now')),
           rowx(btn('Send to Max'), btn('Delete it', 'bo', icon='trash'), gap=12), gap=24), pos='50% 22%')

# d06 ended
gift_d('p-d-06-song-ended-d.dc.html', 'Gift: song ended, desktop', ('candles', 'Candles on a 30th birthday cake'),
       col(card(un('Happy 30th, %s' % nm(white=True), 32) + t('“Thirty and still the first one dancing. Love you, the whole flat”', 16) + small('Reaction sent to Max', mut=False), bg='#FFD84D', pad=28, r=28, gap=12),
           rowx(btn('Download MP3', icon='down'), btn('Share the song', 'bo', icon='share'), gap=12),
           card(strong('Make one like this for someone you love', 17) + small('A song with their name in it, $29 · free preview first', mut=False) + btn('Make a song', sm=True), pad=24, gap=10),
           small('Made with AI + Max’s story · <a href="#">Remove my video</a> · <a href="#">Report</a>'), gap=20))

# ===== NEW recipient screens =====
# d07 link preview card (OG image) 1200x630 + chat bubble demo board
og = ('<div style="display:grid;grid-template-columns:520px 1fr;height:630px">%s<div style="padding:64px;display:flex;flex-direction:column;justify-content:center;gap:24px;background:#FFD84D"><span class="un" style="font-size:22px;font-weight:500">openyoursong</span>'
      '<p class="un" style="margin:0;font-size:64px;font-weight:500;line-height:1.05;letter-spacing:-.02em">A gift for <span class="nmw">Anna</span> from Max</p><span style="font-size:22px">Open it on your phone, sound on</span></div></div>') % img('box', 'Gift cover', 630, r=0)
OUT.append(write('p-d-07-link-preview.dc.html', doc('Gift: link preview image, 1200×630', 1200, 630, og)))

# d08 reveal moment
rv_m = col('<div style="height:360px;display:flex;align-items:center;justify-content:center">%s</div>' % img('box', 'The gift box opening, paper confetti flying', 360, r=28, w='100%'),
           '<p class="un" style="margin:0;text-align:center;font-size:32px;font-weight:500;line-height:1.15">For you, %s</p>' % nm(), small('Your song starts in a second', extra='text-align:center'), gap=24, extra='padding-top:40px')
gm('p-d-08-reveal.dc.html', 'Gift: reveal moment', rv_m)
gift_d('p-d-08-reveal-d.dc.html', 'Gift: reveal moment, desktop', ('box', 'The gift box opening, paper confetti flying'),
       col(un('For you, %s' % nm(), 64, tag='h1'), small('Your song starts in a second', extra='font-size:16px'), gap=20))

# d09 camera unavailable
m = col('<div style="width:56px;height:56px;border-radius:16px;background:#F2F2F2;display:flex;align-items:center;justify-content:center">%s</div>' % ico('cam', '#111', 26),
        un('The camera isn’t available here', 30, tag='h1'), t('This app’s built-in browser can’t record video. Open the link in Safari or Chrome to record your reaction, or just open the gift', 16, True),
        card(linkbox() + small('Copy the link, then paste it in your browser'), pad=20, gap=12), gap=20)
gm('p-d-09-no-camera.dc.html', 'Gift: camera unavailable', m, btn('Open without recording', full=True))
gift_d('p-d-09-no-camera-d.dc.html', 'Gift: camera unavailable, desktop', ('bed', 'A wrapped gift by a bedside clock in a sunny bedroom'),
       col(un('The camera isn’t available here', 48, tag='h1'), t('Your browser didn’t give access to the camera. Allow it in the browser settings to record, or just open the gift', 18, True),
           rowx(btn('Open without recording'), btn('Try again', 'bo', icon='redo'), gap=12), gap=24))

# d10 share consent (P19)
opts = col(radio('No, keep it private', 'Only Max sees it. Nothing changes for your gift', True, 'sh', '#F2F2F2'),
           radio('Yes, on the site and social', 'openyoursong’s own pages and posts', False, 'sh'),
           radio('Yes, and in ads', 'Also in paid ads', False, 'sh'), gap=8)
m = col(un('Can we show your video to other people', 26, tag='h1'), t('Your video is already on its way to Max. This is a separate question', 15, True), opts,
        check('I’m 18 or older and everyone in the video agrees', False, 'a18'), small('You can take it back any time. We can’t delete copies other people already saved'), gap=16)
gm('p-d-10-share-consent.dc.html', 'Gift: share consent', m, btn('Save my answer', full=True))
gift_d('p-d-10-share-consent-d.dc.html', 'Gift: share consent, desktop', ('r01', 'Your reaction video: Anna laughing with happy tears'),
       col(un('Can we show your video to other people', 40, tag='h1'), t('Your video is already on its way to Max. This is a separate question and saying no changes nothing', 17, True), opts,
           check('I’m 18 or older and everyone in the video agrees', False, 'a18d'), btn('Save my answer'), small('You can take it back any time. We can’t delete copies other people already saved or shared'), gap=20), pos='50% 22%')

# d11 group first screen
m = col(img('box', 'Gift cover', 300, r=28), un('Kate, Dad, Tom and 4 others made you something', 30, tag='h1', extra='font-weight:800'), t('For your 60th, from the family', 16, True), gap=16)
gm('p-d-11-group-first.dc.html', 'Gift: first screen, group', m, btn('Open', full=True, icon='play') + small('Turn the sound on', extra='text-align:center'))
gift_d('p-d-11-group-first-d.dc.html', 'Gift: first screen, group, desktop', ('family', 'The family gathered around a phone at the table'),
       col(un('Kate, Dad, Tom and 4 others made you something', 56, tag='h1', extra='font-weight:800'), t('For your 60th, from the family', 20, True),
           rowx(btn('Open', icon='play', extra='height:64px;padding:0 40px;font-size:19px'), small('Turn the sound on'), gap=20), gap=28))

# d12 notes from everyone (all shown)
def note(who, txt, bg='#F2F2F2'):
    return card(t('“%s”' % txt, 16) + small('%s' % who, mut=False, extra='font-weight:500'), bg=bg, pad=20, gap=8)
NOTES = [('Kate', 'Sixty and still beating us all at cards', '#F2F2F2'), ('Tom', 'Thank you for every Sunday lunch', '#FFD84D'), ('Dad', 'Forty years and you still laugh at my jokes', '#F2F2F2'),
         ('Lena', 'Best granny in the world, says Mia', '#F2F2F2'), ('Sam', 'Your lemon cake, every single birthday', '#FFD84D'), ('Ivy', 'You taught me to drive and never once shouted', '#F2F2F2'), ('Max', 'Happy 60th from the lodger who never left', '#F2F2F2')]
m = col(un('Notes from all 7 of us', 30, tag='h1'), *[note(w, x, c) for w, x, c in NOTES], gap=12)
gm('p-d-12-group-notes.dc.html', 'Gift: notes from everyone', m, btn('Make a song for someone', 'bo', full=True), h=1240)
gift_d('p-d-12-group-notes-d.dc.html', 'Gift: notes from everyone, desktop', ('family', 'The family gathered around a phone at the table'),
       col(un('Notes from all 7 of us', 48, tag='h1'), '<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px">%s</div>' % ''.join(note(w, x, c) for w, x, c in NOTES), gap=24))

# d13 remove my video
m = col(un('Your video', 30, tag='h1'), t('Sent to Max on 14 March. Shown on the site and social with your permission', 16, True),
        frame(strong('Stop showing it publicly', 16) + small('We take it off our pages and posts and stop ads within 7 days. Max keeps his copy') + btn('Remove from publications', 'bo', sm=True), pad=20, gap=8),
        frame(strong('Delete it completely', 16) + small('Deleted for everyone within 72 hours, including Max’s copy') + btn('Delete my video', 'bo', sm=True, icon='trash'), pad=20, gap=8), gap=16)
gm('p-d-13-my-video.dc.html', 'Gift: remove my video', m)
gift_d('p-d-13-my-video-d.dc.html', 'Gift: remove my video, desktop', ('r01', 'Your reaction video'),
       col(un('Your video', 48, tag='h1'), t('Sent to Max on 14 March. Shown on the site and social with your permission', 18, True),
           frame(strong('Stop showing it publicly', 17) + small('We take it off our pages and posts and stop ads within 7 days. Max keeps his copy') + btn('Remove from publications', 'bo', sm=True), pad=24, gap=8),
           frame(strong('Delete it completely', 17) + small('Deleted for everyone within 72 hours, including Max’s copy') + btn('Delete my video', 'bo', sm=True, icon='trash'), pad=24, gap=8), gap=20), pos='50% 22%')

# d14 preview mode (giver sees as Anna)
ban_m = '<div style="background:#111;color:#fff;padding:12px 20px;font-size:14px;display:flex;gap:8px;align-items:center">%s<span>Preview mode. It doesn’t count as opening or turn on the camera</span></div>' % ico('eye', '#fff', 16)
m = col(img('box', 'Gift cover', 300, r=28), un('Max made you something', 32, tag='h1', extra='font-weight:800'), t('From Max and the whole flat, for your 30th', 16, True), gap=16)
gm('p-d-14-preview-mode.dc.html', 'Gift: preview mode for Max', m, btn('Open', full=True, icon='play') + '<a href="#" style="font-size:14px;text-align:center">Back to your order</a>', banner=ban_m)
ban_d = '<div style="background:#111;color:#fff;height:48px;padding:0 48px;font-size:15px;display:flex;gap:10px;align-items:center;justify-content:center">%s<span>Preview mode. This is what Anna sees. It doesn’t count as opening and won’t turn on the camera</span><a href="#" style="color:#FFD84D;margin-left:16px">Back to your order</a></div>' % ico('eye', '#fff', 16)
gift_d('p-d-14-preview-mode-d.dc.html', 'Gift: preview mode for Max, desktop', COVER,
       col(un('Max made you something', 64, tag='h1', extra='font-weight:800'), t('From Max and the whole flat, for your 30th', 20, True), btn('Open', icon='play', extra='height:64px;padding:0 40px;font-size:19px;align-self:flex-start'), gap=28), banner=ban_d)
