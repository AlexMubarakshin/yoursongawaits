from kit import *
OUT = []

def summary(extra=''):
    rows = [('Song for', 'Anna, 30th birthday'), ('From', 'Max and the whole flat'), ('Style', 'Pop, upbeat, female voice')]
    rh = ''.join('<div style="display:flex;justify-content:space-between;gap:16px;padding:12px 0;border-top:1px solid #DADADA;font-size:15px"><span class="mut">%s</span><span style="font-weight:500;text-align:right">%s</span></div>' % r for r in rows)
    return card(img('box', 'A tangerine gift box with a blue ribbon and paper confetti', 200) + lyric(24) + '<div>%s</div>' % rh + extra, pad=32, r=28, gap=20)

def split_d(name, title, left, right, h=900, head=None):
    OUT.append(write(name, desktop(title, head or d_head('wizard', None), left, right, h=h, split='640px 1fr', pad='56px 120px 0 120px', gap=96)))

# c01 generating
L = col(small('Attempt 1 of 3', extra='font-size:14px'), un('Writing the music for %s' % nm(), 48, tag='h1'),
        t('Usually 2–3 minutes. You can close this tab, we’ll email the preview link to max.r@mail.com', 18, True),
        card('<div style="display:flex;justify-content:space-between;align-items:baseline"><strong style="font-size:17px">Recording take 1</strong><span class="un tn" style="font-size:32px;font-weight:500">62%</span></div><div style="height:8px;border-radius:4px;background:#fff;position:relative"><span style="position:absolute;left:0;top:0;height:8px;width:62%;border-radius:4px;background:#111"></span></div>' + small('Running for 1:48', mut=False), bg='#FFD84D', pad=28),
        steps(['Lyrics approved', 'Name checked', 'Recording take 1', 'Preview ready'], 2), gap=28)
split_d('p-c-01-generating-d.dc.html', 'Generate: making the music, desktop', L, summary())

# c02 name check
L = col(un('Is %s sung right' % nm(), 48, tag='h1'), t('Listen to how the voice sings the name. Fix it now, before the full song', 18, True),
        card(player('0:04', '0:10', 40, 'Play the name clip') + rowx(btn('Sounds right', tag='button'), btn('Fix it', 'bo', tag='button'), gap=12), pad=28, gap=20),
        frame(strong('Spell it by sound') + t('Write it the way it should be sung. Examples: AH-nah, AN-uh', 15, True) + rowx('<div style="flex:1">%s</div>' % inp('ph', 'Sounds like', 'AH-nah'), btn('Sing it again', 'bo', tag='button', icon='redo'), align='flex-end') + small('Written “Anna” on the gift page, sung “AH-nah” · a name fix gives one extra try'), pad=28, gap=16), gap=28)
split_d('p-c-02-name-check-d.dc.html', 'Generate: name check, desktop', L, summary())

# c03 preview
L = col(un('Your free preview', 48, tag='h1'), lyric(28),
        card(player('0:12', '0:40', 30, 'Play the preview') + small('The start of the same song you’ll get. It fades out at 0:40, full quality after payment'), pad=28, gap=16),
        col(strong('Two takes'), track('Take 1', 'Pop, bright', on=True), track('Take 2', 'Pop, slower'), gap=8),
        rowx('<a href="#" style="font-size:15px">Name sounds off?</a>', '<a href="#" style="font-size:15px">Edit lyrics, try again</a>', small('2 tries left'), gap=24),
        rowx(btn('Continue with take 1'), gap=12), gap=24)
split_d('p-c-03-preview-d.dc.html', 'Generate: preview, desktop', L, summary(), h=960)

# c04 choose
def price(name, amt, items, on=False, bg='#F2F2F2'):
    li = ''.join('<li style="display:flex;gap:10px;align-items:flex-start;font-size:15px;line-height:1.4">%s<span>%s</span></li>' % (ico('check', '#111', 18), i) for i in items)
    return '<label style="display:flex;flex-direction:column;gap:20px;padding:28px;border-radius:28px;background:%s;border:2px solid %s;cursor:pointer"><span style="display:flex;justify-content:space-between;align-items:center"><strong style="font-size:18px">%s</strong><input type="radio" name="plan" class="chk"%s></span><span class="un" style="font-size:56px;font-weight:500;line-height:1">%s</span><ul style="margin:0;padding:0;list-style:none;display:flex;flex-direction:column;gap:10px">%s</ul></label>' % (bg, '#111' if on else bg, name, ' checked' if on else '', amt, li)
song_items = ['Full song as MP3, 256 kbps', 'Lyrics and a gift page for Anna', 'Delivery on the day you pick', 'Printable PDF card with QR', 'Her reaction video, if she records one']
bundle_items = ['Everything in the song', 'Take 2 in full quality', 'Photo slideshow, 5–20 photos', 'Lyrics poster, A4 and US Letter']
body = col(un('Pick what Anna gets', 48, tag='h1'), t('Pay once. Two free remakes, then a full refund within 14 days if she hasn’t opened it', 18, True),
           '<div style="display:grid;grid-template-columns:1fr 1fr;gap:20px">%s%s</div>' % (price('Song', '$29', song_items), price('Bundle', '$55', bundle_items, True, '#FF7A00')),
           rowx(btn('Continue, $55'), '<a href="#" style="font-size:15px">Have a credit? Pay with credit</a>', small('Subscribers pay less per song · <a href="#">See plans</a>'), gap=24), gap=32)
OUT.append(write('p-c-04-choose-d.dc.html', desktop('Pay: song or bundle, desktop', d_head('wizard', None), body, None, pad='56px 120px 0 120px')))

# c05 checkout
L = col(un('Checkout', 48, tag='h1'), inp('em', 'Receipt to', 'max.r@mail.com', typ='email'),
        col('<span class="lab" style="margin:0">Card</span>', '<input class="inp" aria-label="Card number" placeholder="Card number">', '<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px"><input class="inp" aria-label="Expiry date" placeholder="MM / YY"><input class="inp" aria-label="Security code" placeholder="CVC"></div>', gap=12),
        '<details><summary style="cursor:pointer;font-size:15px;font-weight:500">Have a promo code</summary></details>',
        btn('Pay $55', icon='lock'), small('Payments by Polar. Two free remakes, then a full refund within 14 days while the gift is unopened'), gap=20)
R = card(strong('Your order', 18) + '<div style="display:flex;justify-content:space-between;font-size:15px;padding-top:12px;border-top:1px solid #DADADA"><span>Bundle: song for Anna</span><span class="tn">$55.00</span></div><div style="display:flex;justify-content:space-between;font-size:15px"><span class="mut">Tax</span><span class="mut tn">$0.00</span></div><div style="display:flex;justify-content:space-between;font-size:18px;font-weight:500;padding-top:12px;border-top:1px solid #DADADA"><span>Total</span><span class="tn">$55.00</span></div>' + lyric(20), pad=32, r=28, gap=16)
split_d('p-c-05-checkout-d.dc.html', 'Pay: checkout, desktop', L, R)

# ----- order page -----
def order_aside(cur=2, extra=''):
    return col(card(strong('Status', 18) + steps(['Paid', 'Song ready', 'Delivery scheduled', 'Sent', 'Opened'], cur), pad=28, r=28, gap=20),
               card(img('box', 'Gift cover', 160, r=16) + strong('For Anna, from Max and the whole flat', 16) + small('Bundle · take 1 · paid 1 March'), pad=20, r=28, gap=12) + extra, gap=20)

def order_d(name, title, main, cur=2, h=900, aside_extra=''):
    OUT.append(write(name, desktop(title, d_head('order'), main, order_aside(cur, aside_extra), h=h, split='1fr 400px', pad='48px 120px 0 120px', gap=80)))

# c06 delivery (we send)
main = col(small('Order for Anna'), un('When and how should Anna get it', 48, tag='h1'), t('You can change this until the day', 18, True),
           '<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px">%s%s</div>' % (radio('I’ll send it myself', 'Get the link now, send it any way you like', False, 'how'), radio('We’ll send it', 'An email from “Max via openyoursong” that doesn’t give the song away', True, 'how')),
           '<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:16px">%s%s%s</div>' % (inp('dd', 'Date', '14 March 2027'), inp('tt', 'Time', '09:00'), inp('tz', 'Anna’s time zone', 'London, UK (GMT)')),
           inp('ae', 'Anna’s email', 'anna.k@mail.com', typ='email', hint='We send between 08:00 and 21:00 her time and delete her address 30 days after'),
           rowx(btn('Save delivery'), small('Sun 14 March, 09:00 London · 10:00 your time'), gap=20), gap=24)
order_d('p-c-06-delivery-d.dc.html', 'Order: delivery, desktop', main, 1, h=960)

# c07 ready
main = col(un('The song for %s is ready' % nm(), 48, tag='h1'), t('We email her on Sun 14 March at 09:00 London time · <a href="#">Change</a>', 18, True),
           card(strong('Gift link', 17) + linkbox() + sendrow(), bg='#FFD84D', pad=28, gap=16),
           '<div style="display:grid;grid-template-columns:1fr 1fr;gap:16px">%s%s</div>' % (
               frame(rowx(ico('qr', '#111', 22), strong('PDF card with QR', 16)) + small('“For Anna, from Max” · A4 and US Letter') + btn('Download PDF', 'bo', sm=True, icon='down'), pad=24, gap=12),
               frame(rowx(ico('eye', '#111', 22), strong('See it as Anna will', 16)) + small('Preview mode, doesn’t count as opening') + btn('Open preview', 'bo', sm=True), pad=24, gap=12)),
           col(strong('Your files'), track('Take 1, full song', 'MP3 · lyrics', '2:48'), track('Take 2, full song', 'Bundle', '2:51'),
               '<div class="li">%s<div style="flex:1;display:flex;flex-direction:column;gap:2px"><strong style="font-size:16px">Slideshow</strong><span class="mut" style="font-size:14px">Add 5–20 photos, ready in about 10 minutes</span></div>%s</div>' % ('<span style="width:44px;height:44px;border-radius:12px;background:#F2F2F2;display:flex;align-items:center;justify-content:center">%s</span>' % ico('photo', '#111', 20), btn('Add photos', 'bo', sm=True)), gap=4), gap=24)
order_d('p-c-07-ready-d.dc.html', 'Order: ready to send, desktop', main, 2, h=1080)

# ===== NEW screens (mobile + desktop) =====
# c08 generation delayed / failed
mm = col('<div style="width:56px;height:56px;border-radius:16px;background:#F2F2F2;display:flex;align-items:center;justify-content:center">%s</div>' % ico('clock', '#111', 26),
         un('This one is taking longer', 30, tag='h1'), t('Nothing for you to do. We’ll email the preview to max.r@mail.com when it’s ready, usually within the hour', 16, True),
         card(steps(['Lyrics approved', 'Name checked', 'Recording take 1', 'Preview ready'], 2), pad=24), notice('This attempt doesn’t count towards your 3 tries'), gap=20)
OUT.append(write('p-c-08-delayed.dc.html', mobile('Generate: taking longer', m_head('wizard'), mm, btn('Close, I’ll wait for the email', 'bo', full=True))))
L = col('<div style="width:64px;height:64px;border-radius:16px;background:#F2F2F2;display:flex;align-items:center;justify-content:center">%s</div>' % ico('clock', '#111', 30), un('This one is taking longer', 48, tag='h1'),
        t('Nothing for you to do. We’ll email the preview to max.r@mail.com when it’s ready, usually within the hour. You can close this tab', 18, True),
        steps(['Lyrics approved', 'Name checked', 'Recording take 1', 'Preview ready'], 2), notice('This attempt doesn’t count towards your 3 tries'), btn('Close, I’ll wait for the email', 'bo'), gap=28)
split_d('p-c-08-delayed-d.dc.html', 'Generate: taking longer, desktop', L, summary())

# c09 tries used up
mm = col(un('You’ve used all 3 free tries', 30, tag='h1'), t('Pick the take you liked most. After payment you get 2 more remakes before Anna opens it', 16, True),
         col(track('Try 3, take 1', 'Pop, bright · today'), track('Try 2, take 2', 'Acoustic · today', on=True), track('Try 1, take 1', 'Pop · yesterday'), gap=8),
         small('New free tries tomorrow if you’d rather start over'), gap=20)
OUT.append(write('p-c-09-tries-used.dc.html', mobile('Generate: free tries used', m_head('wizard'), mm, btn('Continue with try 2', full=True))))
L = col(un('You’ve used all 3 free tries', 48, tag='h1'), t('Pick the take you liked most. After payment you get 2 more remakes before Anna opens it', 18, True),
        col(track('Try 3, take 1', 'Pop, bright · today'), track('Try 2, take 2', 'Acoustic · today', on=True), track('Try 1, take 1', 'Pop · yesterday'), gap=8),
        rowx(btn('Continue with try 2'), small('New free tries tomorrow if you’d rather start over'), gap=20), gap=28)
split_d('p-c-09-tries-used-d.dc.html', 'Generate: free tries used, desktop', L, summary())

# c10 subscriber with credit
mm = col(un('Use a credit for this song', 30, tag='h1'), t('You have 3 credits on your yearly plan', 16, True),
         card(rowx(strong('Song', 18), '<span style="flex:1"></span>', '<span class="un" style="font-size:32px;font-weight:500">1 credit</span>') + small('Full song, gift page, delivery, PDF card, reaction video'), bg='#FFD84D', pad=24),
         card(rowx(strong('Bundle', 18), '<span style="flex:1"></span>', '<span class="un" style="font-size:24px;font-weight:500">1 credit + $26</span>') + small('Adds take 2, photo slideshow and lyrics poster'), pad=24),
         small('Credits last 12 months. 2 left after this one'), gap=16)
OUT.append(write('p-c-10-pay-with-credit.dc.html', mobile('Pay: subscriber with credit', m_head('wizard'), mm, btn('Use 1 credit', full=True))))
body = col(un('Use a credit for this song', 48, tag='h1'), t('You have 3 credits on your yearly plan. Credits last 12 months', 18, True),
           '<div style="display:grid;grid-template-columns:1fr 1fr;gap:20px">%s%s</div>' % (
               card(strong('Song', 18) + '<span class="un" style="font-size:48px;font-weight:500">1 credit</span>' + small('Full song, gift page, delivery, PDF card, reaction video', mut=False), bg='#FFD84D', pad=28, r=28, gap=16, extra='border:2px solid #111'),
               card(strong('Bundle', 18) + '<span class="un" style="font-size:48px;font-weight:500">1 credit + $26</span>' + small('Adds take 2, photo slideshow and lyrics poster', mut=False), pad=28, r=28, gap=16)),
           rowx(btn('Use 1 credit'), small('2 credits left after this one'), gap=20), gap=32)
OUT.append(write('p-c-10-pay-with-credit-d.dc.html', desktop('Pay: subscriber with credit, desktop', d_head('wizard'), body, None, pad='56px 120px 0 120px')))

# c11 I'll send it myself
mm = col(un('Send it when you’re ready', 30, tag='h1'), t('The link works now. We’ll remind you 10 minutes before 09:00 on 14 March', 16, True),
         card(linkbox() + sendrow(), bg='#FFD84D', pad=20, gap=12),
         ta('msg', 'Message, edit if you like', 'Something for your birthday. Turn the sound on', 72),
         notice('Want it at midnight on the dot? Schedule it with Send Later in iMessage'), gap=16)
OUT.append(write('p-c-11-send-myself.dc.html', mobile('Order: I’ll send it myself', m_head('order'), mm, btn('I’ve sent it', 'bo', full=True, icon='check'))))
main = col(un('Send it when you’re ready', 48, tag='h1'), t('The link works now. We’ll remind you 10 minutes before 09:00 on 14 March and again at 09:00', 18, True),
           card(strong('Gift link') + linkbox() + sendrow(('WhatsApp', 'SMS', 'Telegram', 'Share', 'QR', 'Email')), bg='#FFD84D', pad=28, gap=16),
           ta('msgd', 'Message, edit if you like', 'Something for your birthday. Turn the sound on', 72),
           notice('Want it at midnight on the dot? Schedule it with Send Later in iMessage'),
           rowx(btn('I’ve sent it', 'bo', icon='check'), small('If you added her email and she hasn’t opened it 2 hours later, we email her too'), gap=20), gap=24)
order_d('p-c-11-send-myself-d.dc.html', 'Order: I’ll send it myself, desktop', main, 2, h=980)

# c12 order after opened
mm = col(un('%s opened it' % nm(), 30, tag='h1'), small('Sun 14 March at 09:02'),
         col(img('r01', 'Anna laughing with happy tears in her kitchen', 240, '50% 22%'), rowx(play('Play Anna’s reaction'), '<div style="flex:1">' + strong('Her reaction, 1:24', 16) + small('<br>Only you can see it') + '</div>', '<a class="btn bo sm" href="#" aria-label="Download reaction" style="width:44px;padding:0">%s</a>' % ico('down', '#111', 18)), gap=12),
         card(strong('Remind me next year', 16) + small('One free reminder before her birthday', mut=False) + btn('Remind me', 'bk', sm=True), bg='#FFD84D', pad=20, gap=8),
         gap=16)
OUT.append(write('p-c-12-after-opened.dc.html', mobile('Order: after Anna opened it', m_head('order'), mm, btn('Make another song', 'bo', full=True))))
main = col(un('%s opened it' % nm(), 48, tag='h1'), t('Sun 14 March at 09:02, London time', 18, True),
           '<div style="display:grid;grid-template-columns:320px 1fr;gap:24px;align-items:start">%s%s</div>' % (
               img('r01', 'Anna laughing with happy tears in her kitchen', 400, '50% 22%'),
               col(strong('Her reaction, 1:24', 20), t('Only you can see it. Kept for 12 months, we remind you 14 days before', 15, True), rowx(btn('Play', icon='play'), btn('Download', 'bo', icon='down'), btn('Delete', 'bo', icon='trash'), gap=8),
                   card(strong('Remind me next year', 17) + small('One free reminder before her birthday. Or get every date on a plan, songs cost less', mut=False) + rowx(btn('Remind me', sm=True), '<a href="#" style="font-size:15px">See plans</a>', gap=16), bg='#FFD84D', pad=24, gap=10),
                   frame(rowx(strong('Upgrade to the bundle', 16), '<span style="flex:1"></span>', btn('Pay $26', 'bo', sm=True)) + small('Add take 2, the slideshow and the lyrics poster'), pad=20, gap=6), gap=16)),
           rowx(btn('Make another song', icon='plus'), gap=12), gap=24)
order_d('p-c-12-after-opened-d.dc.html', 'Order: after Anna opened it, desktop', main, 5, h=980)

# c13 slideshow photos
tiles = ''.join(img(k, a, 104, r=16) for k, a in (('r09', 'Anna laughing at her phone'), ('sofa', 'Two friends on a sofa'), ('candles', 'Birthday candles'), ('r05', 'Anna on her bed'), ('head', 'Anna with headphones')))
add = '<button style="height:104px;border-radius:16px;border:2px dashed #111;background:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:4px;font:500 14px Inter,sans-serif;cursor:pointer">%sAdd</button>' % ico('plus', '#111', 20)
mm = col(un('Photos for the slideshow', 30, tag='h1'), t('5–20 photos. We set them to the song in about 10 minutes', 16, True),
         '<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:8px">%s%s</div>' % (tiles, add), small('5 of 20 added · JPG or PNG, up to 10 MB each'), gap=16)
OUT.append(write('p-c-13-slideshow.dc.html', mobile('Order: slideshow photos', m_head('order'), mm, btn('Make the slideshow', full=True))))
main = col(un('Photos for the slideshow', 48, tag='h1'), t('5–20 photos. We set them to the song in about 10 minutes. Without photos by the day, the gift goes out without one', 18, True),
           '<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:12px">%s%s</div>' % (tiles.replace('height:104px', 'height:160px'), add.replace('height:104px', 'height:160px')),
           rowx(btn('Make the slideshow'), small('5 of 20 added · JPG or PNG, up to 10 MB each'), gap=20), gap=28)
order_d('p-c-13-slideshow-d.dc.html', 'Order: slideshow photos, desktop', main, 2)
