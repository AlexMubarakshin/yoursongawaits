from kit import *
OUT = []

def split(name, title, head, left, right, h=900, sp='640px 1fr', pad='56px 120px 0 120px', gap=96):
    OUT.append(write(name, desktop(title, head, left, right, h=h, split=sp, pad=pad, gap=gap)))

def contrib(who, txt, st='Added'):
    return '<div class="li" style="align-items:flex-start"><span style="width:40px;height:40px;border-radius:50%%;background:#F2F2F2;display:flex;align-items:center;justify-content:center;font-weight:500;flex-shrink:0">%s</span><div style="flex:1;display:flex;flex-direction:column;gap:2px"><strong style="font-size:15px">%s</strong><span class="mut" style="font-size:14px;line-height:1.4">%s</span></div><span class="mut" style="font-size:13px">%s</span></div>' % (who[0], who, txt, st)

GROUPCARD = card(img('candles', 'Birthday candles on a cake', 200) + '<p class="un" style="margin:0;font-size:24px;font-weight:500;line-height:1.2">A song for %s’s 60th</p>' % nm('Mum') + small('From the family · organised by Kate'), pad=28, r=28, gap=16)

# ===== Group =====
# g00 organizer setup NEW
m = col(un('Invite people to add a memory', 28, tag='h1'), t('You’ve written yours. Pick when collecting ends, then share the link', 15, True),
        chips(['1 day', '3 days', '1 week', 'Pick a date'], ['3 days'], 'Collect until'), small('Ends Wed 11 March at 20:00 · up to 30 days'),
        card(strong('Invite link', 16) + linkbox('openyoursong.com/join/k4m9') + sendrow(('WhatsApp', 'SMS', 'Telegram', 'Share')), bg='#FFD84D', pad=20, gap=12),
        notice('It’s a surprise. The link says not to forward it to Mum'), gap=16)
OUT.append(write('p-e-00-group-setup.dc.html', mobile('Group: set deadline and invite', m_head('wizard', 2), m, btn('Go to my group page', full=True))))
L = col(un('Invite people to add a memory', 48, tag='h1'), t('You’ve written yours. Pick when collecting ends, then share the link. Up to 20 people, no sign-up for them', 18, True),
        chips(['1 day', '3 days', '1 week', 'Pick a date'], ['3 days'], 'Collect until'), small('Ends Wed 11 March at 20:00 · up to 30 days'),
        card(strong('Invite link', 16) + linkbox('openyoursong.com/join/k4m9') + sendrow(('WhatsApp', 'SMS', 'Telegram', 'Share', 'Email')), bg='#FFD84D', pad=28, gap=16),
        notice('It’s a surprise. The invite page tells people not to forward it to Mum'), btn('Go to my group page'), gap=24)
split('p-e-00-group-setup-d.dc.html', 'Group: set deadline and invite, desktop', d_head('wizard', 2), L, GROUPCARD, h=980)

# e01 organizer desktop
L = col(small('Group gift for Mum'), un('5 of 7 have written', 48, tag='h1'),
        '<div style="display:flex;gap:4px">%s</div>' % ''.join('<span style="flex:1;height:8px;border-radius:4px;background:%s"></span>' % ('#111' if i < 5 else '#DADADA') for i in range(7)),
        card(rowx(strong('Collecting until 11 March · 2 days left', 16)) + linkbox('openyoursong.com/join/k4m9') + rowx(btn('Remind the 2 who haven’t', 'bo', sm=True), small('We write the message, without spoilers'), gap=12), bg='#FFD84D', pad=24, gap=12),
        col(contrib('Kate (you)', 'The Sunday lunches, the garden, how she hums while cooking'), contrib('Dad', 'Forty years and she still laughs at my jokes'), contrib('Tom', 'Teaching me to ride a bike on Elm Street'), contrib('Lena', 'Mia calls her the best granny in the world'), contrib('Sam', 'Her lemon cake, every single birthday'), gap=0),
        rowx(btn('Build the song'), small('You can build it now or wait for the deadline'), gap=20), gap=20)
split('p-e-01-organizer-d.dc.html', 'Group: organizer page, desktop', d_head('order'), L, GROUPCARD, h=1100)

# e02 invite landing desktop
L = col(small('Kate invited you'), un('We’re making %s a song for her 60th' % nm('Mum'), 56, tag='h1'), t('Add a memory and a short note. It takes a minute and you don’t need an account', 18, True),
        notice('It’s a surprise. Please don’t forward this link to her', 'warn'), rowx(btn('Add your part'), small('Open until 11 March'), gap=20), gap=24)
split('p-e-02-invite-d.dc.html', 'Group: invite landing, desktop', d_head('gift'), L, img('candles', 'Birthday candles on a cake', 640, r=28), sp='1fr 1fr', pad='64px 96px 0 96px')

# e03 contribute desktop
L = col(un('Your part for %s' % nm('Mum'), 48, tag='h1'), inp('sn', 'Sign as', 'Tom'),
        ta('mem', 'A memory for the song', 'Teaching me to ride a bike on Elm Street, running behind me the whole way', 112, '74 / 500'),
        ta('nt', 'A note to her, shown after the song', 'Happy 60th. Thanks for never letting go too early', 80, '49 / 200'),
        '<div style="display:grid;grid-template-columns:1fr 1fr;gap:16px">%s%s</div>' % (inp('pe', 'Email, optional', ph='For news about this gift only', typ='email'), '<div><span class="lab">A photo of you two, optional</span><button class="btn bo" style="width:100%">' + ico('photo') + 'Add a photo</button><span class="mut" style="display:block;margin-top:8px;font-size:13px;line-height:1.4">It plays in the slideshow while Mum hears her song. Old photos make people cry the most</span></div>'),
        btn('Send my part'), gap=20)
split('p-e-03-contribute-d.dc.html', 'Group: add your part, desktop', d_head('gift'), L, GROUPCARD, h=1000)

# e04 done desktop
L = col(un('Thanks, Tom. You’re in the song', 48, tag='h1'), t('Keep this page. It’s yours: you’ll see when Mum opens the gift and her reaction, if she records one', 18, True),
        card(linkbox('openyoursong.com/p/t7x2') + small('Your page, only for you'), pad=20, gap=8),
        steps(['Your part sent', 'Kate pays and schedules it', 'Mum opens it on 14 March'], 1), '<a href="#" style="font-size:15px">Make a song for someone of yours</a>', gap=24)
split('p-e-04-done-d.dc.html', 'Group: part sent, desktop', d_head('gift'), L, GROUPCARD)

# g05 participant page later NEW
m = col(small('Mum’s 60th · from the family'), un('Mum opened it', 30, tag='h1'), small('Sun 14 March at 10:15'),
        col(img('r06', 'Mum smiling with a happy tear over a lemon cake', 260, '50% 22%'), rowx(play('Play Mum’s reaction'), strong('Her reaction, 1:10', 16)), gap=12),
        small('Shared with everyone who added a part and left an email'), gap=12)
OUT.append(write('p-e-09-participant-later.dc.html', mobile('Group: participant page after opening', m_head('gift'), m, btn('Make a song for someone of yours', 'bo', full=True))))
L = col(small('Mum’s 60th · from the family'), un('Mum opened it', 48, tag='h1'), t('Sun 14 March at 10:15. She recorded her reaction for all of you', 18, True),
        rowx(btn('Play her reaction', icon='play'), btn('Listen to the song', 'bo'), gap=12), small('Shared with everyone who added a part and left an email'),
        card(strong('Make one like this for someone of yours', 16) + btn('Make a song', sm=True), pad=24, gap=10), gap=24)
split('p-e-09-participant-later-d.dc.html', 'Group: participant page after opening, desktop', d_head('gift'), L, img('r06', 'Mum smiling with a happy tear over a lemon cake', 680, '50% 22%', r=28), sp='1fr 1fr', pad='48px 96px 0 96px')

# ===== Account =====
def acc_d(name, title, tab, body, h=900):
    OUT.append(write(name, desktop(title, d_head('account', right=tab), body, None, h=h, pad='48px 120px 0 120px')))

def ordercard(key, alt, who, st, sub, act):
    return '<div style="display:flex;gap:20px;align-items:center;padding:20px 0;border-bottom:1px solid #DADADA">%s<div style="flex:1;display:flex;flex-direction:column;gap:4px"><strong style="font-size:18px">%s</strong><span class="mut" style="font-size:14px">%s</span></div><span style="font-size:14px;font-weight:500;background:%s;border-radius:8px;padding:6px 12px">%s</span>%s</div>' % (img(key, alt, 80, r=16, w='80px'), who, sub, '#FFD84D' if st in ('Scheduled', 'Collecting') else '#F2F2F2', st, btn(act, 'bo', sm=True))
body = col(rowx(un('Your songs', 48, tag='h1'), '<span style="flex:1"></span>', small('4 orders')),
           col(ordercard('box', 'Gift cover', 'Anna, 30th birthday', 'Scheduled', 'Opens 14 March 09:00 London · bundle', 'Open order'),
               ordercard('r06', 'Mum with lemon cake', 'Mum, 60th · group of 7', 'Reaction received', 'Opened 14 Feb · 1 reaction', 'Watch'),
               ordercard('dad', 'Dad with a guitar', 'Leo, Father’s Day', 'Opened', 'Opened 16 June 2026', 'Open order'),
               ordercard('office', 'Office team with a cake', 'Dee, retirement · group', 'Collecting', '3 of 9 have written · until 20 March', 'Group page'), gap=0), gap=24)
acc_d('p-e-05-account-orders-d.dc.html', 'Account: orders, desktop', 'Orders', body)

body = col(un('%s sent you her reaction' % nm(), 48, tag='h1'),
           '<div style="display:grid;grid-template-columns:420px 1fr;gap:48px;align-items:start">%s%s</div>' % (
               img('r01', 'Anna laughing with happy tears in her kitchen', 560, '50% 22%', r=28),
               col(t('She opened it on Sun 14 March at 09:02', 18), rowx(btn('Play', icon='play'), btn('Download', 'bo', icon='down'), gap=8),
                   small('Only you can see it. Kept for 12 months, we remind you 14 days before'),
                   card(strong('Anna said we can show her video with the song', 17) + t('Your story and names are in it, so we ask you too. Say no and nothing changes', 15) + rowx(btn('No', 'bo', sm=True), btn('Yes, show it', sm=True), gap=8), bg='#FFD84D', pad=24, gap=10),
                   '<a href="#" style="font-size:15px">Listen to the song</a>', gap=20)), gap=32)
acc_d('p-e-06-reaction-d.dc.html', 'Account: reaction received, desktop', 'Orders', body, h=980)

def occ(who, rel, what, date, sug=False):
    return '<div style="display:grid;grid-template-columns:1fr 200px 160px 140px;gap:24px;align-items:center;padding:16px 0;border-bottom:1px solid #DADADA"><div style="display:flex;flex-direction:column;gap:2px"><strong style="font-size:17px">%s</strong><span class="mut" style="font-size:14px">%s</span></div><span style="font-size:15px">%s</span><span class="tn" style="font-size:15px;font-weight:500">%s</span>%s</div>' % (who, rel, what, date, btn('Add', 'bo', sm=True) if sug else '<a href="#" class="mut" style="font-size:14px">Edit</a>')
body = '<div style="display:grid;grid-template-columns:1fr 400px;gap:64px">%s%s</div>' % (
    col(rowx(un('Dates to remember', 48, tag='h1'), '<span style="flex:1"></span>', btn('Add a date', 'bo', sm=True, icon='plus')), small('We remind you 14 and 3 days before by email, with the form already filled in'),
        col(occ('Mum', 'Mother', 'Birthday', '14 Feb'), occ('Anna', 'Friend', 'Birthday', '14 Mar'), occ('Leo', 'Dad', 'Father’s Day', '21 Jun'), occ('Dee', 'Colleague', 'Work anniversary', '2 Sep', True), gap=0), small('Dee is a suggestion from a past order'), gap=16),
    card(strong('Yearly plan', 18) + '<span class="un tn" style="font-size:48px;font-weight:500">3 credits</span>' + small('Left this year · each credit is one song · credits last 12 months', mut=False) + '<div class="hr"></div>' + small('Extra songs $19 · renews 14 Jan 2027 for $59 · reminder 30 and 7 days before', mut=False) + rowx(btn('Change card', 'bo', sm=True), btn('Cancel renewal', 'bo', sm=True), gap=8), bg='#FFD84D', pad=28, r=28, gap=12))
acc_d('p-e-07-calendar-d.dc.html', 'Account: calendar and plan, desktop', 'Calendar', body)

body = '<div style="display:grid;grid-template-columns:1fr 1fr;gap:48px">%s%s</div>' % (
    col(un('Not quite right', 48, tag='h1'), t('Song for Anna · paid 1 March · not opened yet', 18, True),
        card(rowx(strong('Free remake', 18), '<span style="flex:1"></span>', small('2 of 2 left', mut=False)) + ta('rm', 'What should change', 'Make the chorus slower and mention the dog, Biscuit', 96) + btn('Remake the song', sm=True), pad=28, r=28, gap=12), gap=20),
    col(frame(strong('Refund', 18) + t('Full refund within 14 days of paying, while the gift is unopened. Yours is open until 15 March', 15, True) + btn('Ask for a refund', 'bo', sm=True), pad=28, gap=12),
        frame(strong('Something else', 18) + t('Email help@openyoursong.com. We reply within 24 hours', 15, True), pad=28, gap=8), gap=16, extra='padding-top:96px'))
acc_d('p-e-08-remake-refund-d.dc.html', 'Account: remake or refund, desktop', 'Orders', body)

# settings NEW
m = col(un('Settings', 30, tag='h1'),
        frame(strong('Email', 16) + small('max.r@mail.com') + check('News and offers', False, 'n1') + check('Reminders for my dates', True, 'n2'), pad=20, gap=10),
        frame(strong('Sign out', 16) + small('You’re signed in on this device for 90 days') + btn('Sign out', 'bo', sm=True), pad=20, gap=8),
        frame(strong('Delete account and data', 16) + small('Orders, dates and videos are deleted. Gift links stop working') + btn('Delete account', 'bo', sm=True, icon='trash'), pad=20, gap=8), gap=16)
OUT.append(write('p-e-10-settings.dc.html', mobile('Account: settings', m_head('account', right='Settings'), m, pad_top=24)))
body = col(un('Settings', 48, tag='h1'), '<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:20px">%s%s%s</div>' % (
    frame(strong('Email', 17) + small('max.r@mail.com') + check('News and offers', False, 'n1d') + check('Reminders for my dates', True, 'n2d'), pad=28, gap=12),
    frame(strong('Sign out', 17) + small('You’re signed in on this device for 90 days. No passwords, we email you a link') + btn('Sign out', 'bo', sm=True), pad=28, gap=12),
    frame(strong('Delete account and data', 17) + small('Orders, dates and videos are deleted. Gift links stop working') + btn('Delete account', 'bo', sm=True, icon='trash'), pad=28, gap=12)), gap=32)
acc_d('p-e-10-settings-d.dc.html', 'Account: settings, desktop', 'Settings', body)

# ===== Entry: sign in, link sent, pricing, occasion =====
m = col(un('Log in', 30, tag='h1'), t('No password. We email you a link that works for 15 minutes', 16, True), inp('le', 'Your email', 'max.r@mail.com', typ='email'),
        btn('Email me a link', full=True, tag='button'), '<a href="#" style="font-size:15px">Lost the link to an order?</a>', gap=20)
OUT.append(write('p-f-01-login.dc.html', mobile('Entry: log in', m_head('site'), m, pad_top=24)))
L = col(un('Log in', 56, tag='h1'), t('No password. We email you a link that works for 15 minutes. Your order links keep working too', 18, True), inp('led', 'Your email', 'max.r@mail.com', typ='email'),
        rowx(btn('Email me a link', tag='button'), '<a href="#" style="font-size:15px">Lost the link to an order?</a>', gap=24), gap=24)
split('p-f-01-login-d.dc.html', 'Entry: log in, desktop', d_head('site'), L, img('max', 'Max smiling at his phone in a café', 640, r=28), sp='1fr 1fr', pad='48px 96px 0 96px')

m = col('<div style="width:56px;height:56px;border-radius:16px;background:#FFD84D;display:flex;align-items:center;justify-content:center">%s</div>' % ico('mail', '#111', 26),
        un('Check your email', 30, tag='h1'), t('We sent a link to max.r@mail.com. It works for 15 minutes on any device', 16, True),
        '<a href="#" style="font-size:15px">Send it again</a>', '<a href="#" class="mut" style="font-size:15px">Use a different email</a>', gap=16)
OUT.append(write('p-f-02-link-sent.dc.html', mobile('Entry: link sent', m_head('site'), m, pad_top=40)))
L = col('<div style="width:64px;height:64px;border-radius:16px;background:#FFD84D;display:flex;align-items:center;justify-content:center">%s</div>' % ico('mail', '#111', 30),
        un('Check your email', 56, tag='h1'), t('We sent a link to max.r@mail.com. It works for 15 minutes on any device', 18, True),
        rowx('<a href="#" style="font-size:15px">Send it again</a>', '<a href="#" class="mut" style="font-size:15px">Use a different email</a>', gap=24), gap=24)
split('p-f-02-link-sent-d.dc.html', 'Entry: link sent, desktop', d_head('site'), L, img('max', 'Max smiling at his phone in a café', 640, r=28), sp='1fr 1fr', pad='48px 96px 0 96px')

# pricing page
def pc(name, amt, sub, items, bg='#F2F2F2', cta='Start free, hear it first'):
    li = ''.join('<li style="display:flex;gap:10px;font-size:15px;line-height:1.4">%s<span>%s</span></li>' % (ico('check', '#111', 18), i) for i in items)
    return card(strong(name, 18) + '<span class="un" style="font-size:56px;font-weight:500;line-height:1">%s</span>' % amt + small(sub, mut=False) + '<ul style="margin:0;padding:0;list-style:none;display:flex;flex-direction:column;gap:10px">%s</ul>' % li + btn(cta, sm=True, extra='align-self:flex-start;margin-top:8px'), bg=bg, pad=32, r=28, gap=16)
P1 = pc('Song', '$29', 'Pay after the free preview', ['Full song with their name, MP3', 'Gift page, delivery on the day', 'PDF card with QR', 'Their reaction video'])
P2 = pc('Bundle', '$55', 'Pay after the free preview', ['Everything in the song', 'A second version', 'Photo slideshow', 'Lyrics poster'], '#FF7A00')
P3 = pc('Yearly plan', '$59', 'a year · 3 songs included', ['Dates calendar with reminders', '3 credits, one song each', 'Extra songs $19', 'Cancel in one click'], '#FFD84D', 'Get the plan')
P4 = pc('Monthly plan', '$7', 'a month · a credit every 3 months', ['Dates calendar with reminders', 'Up to 3 credits saved', 'Extra songs $19', 'Cancel in one click'], '#F2F2F2', 'Get the plan')
body = col(un('How much does a custom song cost', 64, tag='h1'), t('A personalized song with their name, from $29. You hear a free preview before you pay anything', 20, True),
           '<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:20px">%s%s%s%s</div>' % (P1, P2, P3, P4),
           small('Subscription prices are placeholders until approved · two free remakes, then a full refund within 14 days if the gift is unopened'), gap=24)
OUT.append(write('p-f-03-pricing-d.dc.html', desktop('Entry: pricing, desktop', d_head('site'), body, None, h=900, pad='40px 64px 0 64px')))
m = col(un('How much does a custom song cost', 36, tag='h1'), t('A personalized song with their name, from $29. Free preview before you pay', 16, True), P1, P2, P3, P4, gap=16)
OUT.append(write('p-f-03-pricing.dc.html', mobile('Entry: pricing', m_head('site'), m, h=2240, pad_top=8)))

# occasion page (SEO entry, prefilled)
L = col(small('Mother’s Day songs'), un('A Mother’s Day song with Mum’s name in it', 72, tag='h1', extra='font-weight:800'), t('A personalised song gift for Mum, made from your story. Hear a free preview, then send it on Mother’s Day', 20, True),
        rowx(btn('Start her song'), btn('Hear an example', 'bo', icon='play'), gap=12), small('Free 30–45 s preview · $29 if you love it'), gap=28)
split('p-f-04-occasion-d.dc.html', 'Entry: occasion page, desktop', d_head('site'), L, col(img('mum', 'A mother laughing while making pancakes', 520, r=28), rowx(play('Play Mum’s Sunday pancakes'), strong('Mum’s Sunday pancakes · acoustic', 16)), gap=16), sp='1fr 560px', pad='40px 64px 0 64px', gap=80)
m = col(small('Mother’s Day songs'), un('A Mother’s Day song with Mum’s name in it', 40, tag='h1', extra='font-weight:800'), t('A personalised song gift for Mum, made from your story. Hear a free preview, then send it on Mother’s Day', 16, True),
        col(btn('Start her song', full=True), btn('Hear an example', 'bo', full=True, icon='play'), gap=12), img('mum', 'A mother laughing while making pancakes', 240), gap=20)
OUT.append(write('p-f-04-occasion.dc.html', mobile('Entry: occasion page', m_head('site'), m, pad_top=8)))

# ===== Emails =====
def mail(name, title, subj, hero, body, cta, h=760, note=''):
    hero_html = img(hero[0], hero[1], 240, hero[2] if len(hero) > 2 else None, r=16) if hero else ''
    inner = ('<div style="padding:16px 40px;border-bottom:1px solid #DADADA;font-size:13px" class="mut">%s</div>'
             '<div style="padding:40px;display:flex;flex-direction:column;gap:20px">%s%s%s%s%s</div>'
             '<div style="padding:24px 40px;border-top:1px solid #DADADA;font-size:12px;line-height:1.5" class="mut">openyoursong · personal songs made with AI from your story<br>You get this because of your order · <a href="#">Email settings</a></div>') % (
        'Subject: ' + subj, WM % 18, hero_html, body, btn(cta, extra='align-self:flex-start'), small(note) if note else '')
    OUT.append(write(name, doc('Email: ' + title, 600, h, inner)))

mail('p-e-mail-03-preview-ready.dc.html', 'preview ready', 'Your preview for Anna is ready', ('box', 'Gift cover'), un('Your preview for %s is ready' % nm(), 28) + t('Two takes are waiting. Listen, check the name, then decide. No payment until you love it', 16, True), 'Listen to the preview', note='Unpaid previews are deleted after 30 days')
mail('p-e-mail-04-paid.dc.html', 'order paid', 'Your song for Anna: order page inside', None, un('Thanks, Max. The song for %s is yours' % nm(), 28) + t('Keep this email. The button opens your order page: pick when to send it, get the gift link and the PDF card', 16, True) + card('<div style="display:flex;justify-content:space-between;font-size:15px"><span>Bundle: song for Anna</span><span class="tn">$55.00</span></div>', pad=20), 'Open my order', h=568)
mail('p-e-mail-05-gift-for-you.dc.html', 'gift for the recipient', 'Max sent you a gift', ('box', 'Gift cover'), un('Max made you something', 28) + t('Open it on your phone with the sound on', 16, True), 'Open your gift', h=728, note='From Max via openyoursong · nothing to sign up for')
mail('p-e-mail-06-time-to-send.dc.html', 'time to send', 'It’s time to send Anna her song', None, un('It’s 09:00 in London. Time to send it', 28) + t('Anna’s song is ready to open. Send the link the way you planned', 16, True) + card(linkbox() + sendrow(('WhatsApp', 'SMS', 'Telegram', 'Copy')), bg='#FFD84D', pad=20, gap=12), 'I’ve sent it', h=672, note='We remind you again in 2 hours if it’s not marked as sent')
mail('p-e-mail-07-calendar.dc.html', 'calendar reminder', 'Mum’s birthday is in 14 days', ('mum', 'Mum laughing while making pancakes'), un('%s’s birthday is in 14 days' % nm('Mum'), 28) + t('Her song form is ready with her name and the occasion filled in. You have 2 credits left', 16, True), 'Start Mum’s song', h=716)
mail('p-e-mail-08-login.dc.html', 'log-in link', 'Your log-in link', None, un('Your log-in link', 28) + t('It works for 15 minutes. If you didn’t ask for it, ignore this email', 16, True), 'Log in to openyoursong', h=440)
mail('p-e-mail-09-video-expiring.dc.html', 'reaction video expiring', 'Download Anna’s reaction before 28 Feb', ('r01', 'Anna’s reaction', '50% 22%'), un('Anna’s reaction will be deleted in 14 days', 28) + t('We keep reaction videos for 12 months. Download it if you want to keep it', 16, True), 'Download the video', h=748)
mail('p-e-mail-10-new-part.dc.html', 'group: new part', 'Tom added his part · 5 of 7', None, un('Tom added his part', 28) + t('5 of 7 have written for Mum’s song. Collecting ends 11 March at 20:00', 16, True) + card(t('“Teaching me to ride a bike on Elm Street, running behind me the whole way”', 15), pad=20), 'Open the group page', h=560)
mail('p-e-mail-11-scheduled.dc.html', 'group: gift scheduled', 'Mum’s song is ready and scheduled', ('candles', 'Birthday candles'), un('Mum’s song is on its way', 28) + t('Kate paid for it. Mum opens it on 14 March at 10:00. We’ll tell you when she does', 16, True), 'See your page', h=716)
