# v73: flow review sections B, C, D (docs/research/appendix/flow-review-2026-11-09.md).
# Standalone patch script: edits the boards in ../project in place. Run once on a v72 snapshot.
import json, os, re

P = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'project') + '/'
CJ = json.load(open(P + 'canvas.json'))
B, N = CJ['boards'], CJ['notes']
touched, removed = set(), set()


def rd(f):
    return open(P + f).read()


def wr(f, s):
    open(P + f, 'w').write(s)
    touched.add(f)


def rep(f, old, new, count=1):
    s = rd(f)
    n = s.count(old)
    assert n >= 1 and (count == 0 or n == count), '%s: %r found %d times' % (f, old[:70], n)
    wr(f, s.replace(old, new))


def sub(f, pat, new, count=1):
    s2, n = re.subn(pat, new, rd(f), flags=re.S)
    assert (n >= 1 if count == 0 else n == count), '%s: /%s/ matched %d times' % (f, pat[:70], n)
    wr(f, s2)


def grab(f, pat):
    m = re.search(pat, rd(f), flags=re.S)
    assert m, '%s: /%s/ not found' % (f, pat[:70])
    return m.group(0)


def grow(f, dh):
    h, w = B[f]['h'], B[f]['w']
    rep(f, 'width:%dpx;height:%dpx' % (w, h), 'width:%dpx;height:%dpx' % (w, h + dh))
    rep(f, '"height":%d}' % h, '"height":%d}' % (h + dh))
    B[f]['h'] = h + dh


def remove(stem):
    for f in (stem + '.dc.html', stem + '-d.dc.html'):
        os.remove(P + f)
        del B[f]
        CJ['order'].remove(f)
        removed.add(f)


def place(stem, num, x, name=None):
    for f in (stem + '.dc.html', stem + '-d.dc.html'):
        t = re.sub(r'^[\d.]+', num, B[f]['title'])
        if name:
            t = '%s  %s · %s' % (num, name, 'desktop' if f.endswith('-d.dc.html') else 'mobile')
        B[f]['title'], B[f]['x'] = t, x


def clone(src, dst, title, edits):
    s = rd(src)
    for old, new in edits:
        assert s.count(old) == 1, '%s: %r found %d times' % (src, old[:70], s.count(old))
        s = s.replace(old, new)
    s = re.sub(r'<title>[^<]*</title>', '<title>%s</title>' % title, s, count=1)
    wr(dst, s)


LAB = 'font-size:14px;font-weight:500;display:block;margin-bottom:8px'
INP = 'width:100%;box-sizing:border-box;height:52px;border:2px solid #111;border-radius:12px;padding:0 16px;font:500 17px Inter,system-ui,sans-serif;color:#111;background:#fff'
CHK = 'width:22px;height:22px;margin:0;accent-color:#111;flex-shrink:0'
LNK = 'display:flex;align-items:center;min-height:44px;font-size:15px'
HINT = 'display:block;margin-top:6px;font-size:13px'

# =====================================================================
# 1. Questionnaire: fewer screens before the first sound
# =====================================================================
WHO, WHO_D, OCC, OCC_D = 'p-b-02-who-is-it-for.dc.html', 'p-b-02-who-is-it-for-d.dc.html', 'p-b-02b-occasion.dc.html', 'p-b-02b-occasion-d.dc.html'
SOUNDS = 'Said differently than it’s spelled? Add how it sounds'

# 1.1 "Who" and "Occasion" become one screen. The spelling-by-sound field is optional and lives here (group 5)
occ = grab(OCC, r'<div><span class="lab">What is the occasion</span><div class="chips">.*?</div></div>')
date = grab(OCC, r'<div><label class="lab" for="od">.*?</div>')
rep(WHO, 'maxlength="40"></div>', 'maxlength="40"><a href="#" style="%s;font-size:14px">%s</a></div>' % (LNK, SOUNDS))
sub(WHO, r'(<span class="lab">They are your</span><div class="chips">.*?</div></div>)', lambda m: m.group(1) + '\n    ' + occ + '\n    ' + date)
grow(WHO, 136)
occ = grab(OCC_D, r'<div><span class="lab">Occasion</span><div class="chips">.*?</div></div>')
date = grab(OCC_D, r'<div><label class="lab" for="od">.*?</div>')
rep(WHO_D, 'Up to 40 characters</span>', 'Up to 40 characters · <a href="#">%s</a></span>' % SOUNDS)
sub(WHO_D, r'(<span class="lab">They are your</span><div class="chips">.*?</div></div>)', lambda m: m.group(1) + occ + date)
grow(WHO_D, 80)

# 1.2 The first screen is no longer "Alone or together"; the separate name check is gone (group 5)
remove('p-b-01-solo-or-together')
remove('p-b-02b-occasion')
remove('p-c-02-name-check')

# 1.3 Story screen: the giver's first name (asked once) and the way into a group gift
STORY, STORY_D = 'p-b-03-their-story.dc.html', 'p-b-03-their-story-d.dc.html'
me = lambda gap: ('<div><label class="lab" for="yn">Your first name</label><input class="inp" id="yn" type="text" value="Max" autocomplete="given-name" style="height:52px">'
                  '<span class="mut" style="display:block;margin-top:%dpx;font-size:13px">Anna sees it on her gift: “Max made you something”</span></div>'
                  '<a href="#" style="%s">Giving it together? Invite friends to add memories</a>') % (gap, LNK)
rep(STORY, '211 / 1500</span></div></div>\n  </main>', '211 / 1500</span></div></div>\n    ' + me(6) + '\n  </main>')
grow(STORY, 196)
rep(STORY_D, 'text-align:right">211 / 1500</span></div>', 'text-align:right">211 / 1500</span></div>' + me(8))
grow(STORY_D, 120)

# 1.4 Email screen: only the email; no step number after the questionnaire; next step is the music
EM, EM_D = 'p-b-06-email.dc.html', 'p-b-06-email-d.dc.html'
sub(EM, r'<div><label class="lab" for="fn">Your first name</label>.*?</span></div>', '')
rep(EM, 'font-variant-numeric:tabular-nums">4/4</span>', 'font-variant-numeric:tabular-nums"></span>')
rep(EM, 'aria-label="Step 4 of 4"', 'aria-label="Questionnaire done"')
rep(EM, 'Check how the name sounds', 'We record the music')
rep(EM, '<span style="font-size:15px">Hear your free preview</span>', '<span style="font-size:15px">Hear the preview, check the name</span>')
grow(EM, -40)
sub(EM_D, r'<div><label class="lab" for="fnd">Your first name</label>.*?</span></div>', '')
rep(EM_D, '<span class="mut tn" style="font-size:14px">Step 4 of 4</span>', '')
rep(EM_D, 'aria-label="Step 4 of 4"', 'aria-label="Questionnaire done"')
rep(EM_D, 'Check how the name sounds', 'We record the music')
rep(EM_D, '<span>Free preview</span>', '<span>Hear the preview, check the name</span>')

# 1.5 The signature is set where the giver sees it: on "What Anna gets", next to the note
sign = ('<div><label for="sg" style="%s">From, as Anna sees it</label><input id="sg" type="text" value="Max and the whole flat" style="%s">'
        '<span class="mut" style="%s">On the first screen of the gift and on the printed card. Add others if it’s from more of you</span></div>') % (LAB, INP, HINT)
for f, dh in [('p-c-03b-gift-peek.dc.html', 132), ('p-c-03b-gift-peek-d.dc.html', 128)]:
    rep(f, ' / 300</span></div>', ' / 300</span></div>' + sign)
    grow(f, dh)

# 1.6 Desktop summary panel: rows follow the new order of the questions
ROW = '<div style="display:grid;grid-template-columns:120px 1fr;gap:16px;padding:12px 0;border-top:1px solid #DADADA;font-size:15px"><span class="mut">%s</span>%s</div>'
NOW = '<span style="display:flex;align-items:center;gap:8px;font-weight:500"><span style="width:8px;height:8px;border-radius:50%;background:#FFD84D;border:1.5px solid #111"></span>Filling in now</span>'
LATER = '<span aria-label="Comes later" style="display:flex;align-items:center"><span style="display:block;width:%dpx;height:10px;border-radius:5px;background:#F2F2F2"></span></span>'
ORDER = [('For', 120), ('Occasion', 160), ('Photos', 96), ('Story', 160), ('From', 72), ('Sound', 120), ('Lyrics', 140)]
story_val = re.search(r'<span class="mut">Story</span><span style="font-weight:500">(.*?)</span>', rd('p-b-04-genre-and-voice-d.dc.html')).group(1)
VAL = {'For': 'Anna, a friend', 'Occasion': 'Anna’s 30th birthday · 14 March', 'Photos': '6 photos', 'Story': story_val, 'From': 'Max',
       'Sound': 'Pop, upbeat, female voice', 'Lyrics': 'Ready, 3 lines edited'}


def summary(f, done, now):
    rows = ''
    for label, w in ORDER:
        cell = ('<span style="font-weight:500">%s</span>' % VAL[label]) if label in done else NOW if label == now else LATER % w
        rows += ROW % (label, cell)
    s = rd(f)
    i = s.index(ROW.split('%s')[0] + 'For</span>')
    j = s.index('</div>', s.index('<span class="mut">Lyrics</span>', i)) + len('</div>')
    wr(f, s[:i] + rows + s[j:])


summary(WHO_D, [], 'For')
summary('p-b-02c-photos-d.dc.html', ['For', 'Occasion'], 'Photos')
summary(STORY_D, ['For', 'Occasion', 'Photos'], 'Story')
summary('p-b-07-moderation-d.dc.html', ['For', 'Occasion', 'Photos'], 'Story')
summary('p-b-04-genre-and-voice-d.dc.html', ['For', 'Occasion', 'Photos', 'Story', 'From'], 'Sound')
summary('p-b-05-lyrics-ready-d.dc.html', ['For', 'Occasion', 'Photos', 'Story', 'From', 'Sound'], 'Lyrics')
summary(EM_D, ['For', 'Occasion', 'Photos', 'Story', 'From', 'Sound', 'Lyrics'], None)
# before "What Anna gets" the song is from "Max"; the longer signature comes later
for f in ['p-c-01-generating-d.dc.html', 'p-c-03-preview-d.dc.html', 'p-c-08-delayed-d.dc.html', 'p-c-02b-name-fix-d.dc.html', 'p-c-09-tries-used-d.dc.html']:
    rep(f, '>Max and the whole flat<', '>Max<', 0)

for f in ['p-e-01-organizer.dc.html', 'p-e-01-organizer-d.dc.html']:
    if 'from Max and the whole flat' in rd(f):
        rep(f, 'from Max and the whole flat', 'organised by Max', 0)

# 1.7 Generating: there is no "name checked" step any more
sub('p-c-01-generating.dc.html', r'<li style="display:flex;align-items:center;gap:12px;min-height:44px">(?:(?!<li ).)*?Name checked: AH-nah</span></li>', '')
for f in ['p-c-01-generating-d.dc.html', 'p-c-08-delayed.dc.html', 'p-c-08-delayed-d.dc.html']:
    sub(f, r'<div style="display:flex;align-items:center;gap:12px;font-size:15px;">(?:(?!<div ).)*?<span>Name checked</span></div>', '')

# 1.8 New numbers and places in the rows
place('p-b-02-who-is-it-for', '1.2.1', 0, 'Who and what for')
place('p-b-02c-photos', '1.2.2', 1520)
place('p-b-03-their-story', '1.2.3', 3040)
place('p-b-07-moderation', '1.2.4', 4560)
place('p-b-04-genre-and-voice', '1.2.5', 6080)
place('p-b-05-lyrics-ready', '1.2.6', 7600)
place('p-b-06-email', '1.2.7', 9120)
place('p-c-01-generating', '1.3.1', 0)
place('p-c-08-delayed', '1.3.2', 1520)
place('p-c-03-preview', '1.3.3', 3040)
place('p-c-02b-name-fix', '1.3.4', 4560)
place('p-c-03b-gift-peek', '1.3.5', 6080)
place('p-c-09-tries-used', '1.3.6', 7600)
place('p-c-09b-more-tries', '1.3.7', 9120)
place('p-c-04-choose', '1.3.8', 10640)
place('p-c-10-pay-with-credit', '1.3.9', 12160)
place('p-c-05-checkout', '1.3.10', 13680)
N['v64photos']['x'] = 1520
N['v64photos']['text'] = N['v64photos']['text'].replace('(2.1.4)', '(2.1.6)')
N['v66peek']['x'] = 6080
N['v66peek']['text'] = N['v66peek']['text'].replace('(1.3.3)', '(1.3.1)')
N['v68tries']['x'] = 7600
N['v62proof']['x'] = 10640 + 430
N['v73name'] = {'fill': 'yellow', 'page': 'landing', 'size': 20, 'w': 380, 'x': 4560, 'y': N['v66peek']['y'],
                'text': 'The name is checked on the preview itself. “Name sounds off?” on the preview (1.3.3) opens this screen; a fix gives one extra try. '
                        'People who know the name is tricky can add how it sounds on the first screen (1.2.1)'}
N['v73start'] = {'fill': 'yellow', 'page': 'landing', 'size': 20, 'w': 380, 'x': 0, 'y': N['v64photos']['y'],
                 'text': 'The questionnaire starts here. Alone is the default. A group gift starts from “Giving it together?” on the story screen (1.2.3) '
                         'or from the group-gift page, and continues at 4.1.1. Six screens up to the email, eight to the first sound (was eleven)'}

# =====================================================================
# 2. After the song: one screen, then the gift page
# =====================================================================
card = ('<div style="border:1px solid #DADADA;border-radius:24px;padding:16px 20px 8px;display:flex;flex-direction:column;gap:4px">'
        '<strong style="font-size:16px;line-height:1.3">Your reaction video</strong>'
        '<span class="mut" style="font-size:14px;line-height:1.45">Only Max can watch it. The rest is up to you, any time</span>'
        '<div style="display:flex;flex-direction:column">'
        '<a href="#" style="%s;border-top:1px solid #DADADA;margin-top:8px">Post it yourself</a>'
        '<a href="#" style="%s;border-top:1px solid #DADADA">Let openyoursong show it to others</a>'
        '<a href="#" style="%s;border-top:1px solid #DADADA">Remove my video</a></div></div>') % (LNK, LNK, LNK)
for f in ['p-d-06-song-ended.dc.html', 'p-d-06-song-ended-d.dc.html']:
    a = '<div style="display:flex;align-items:center;gap:14px"><button class="play" aria-label="Play the song again"'
    rep(f, a, card + a)
grow('p-d-06-song-ended.dc.html', 232)  # on desktop the card fits beside the photo
place('p-d-05-review-reaction', '3.2.1', 0)
place('p-d-06-song-ended', '3.2.2', 1520)
place('p-d-10-share-consent', '3.2.3', 3040)
place('p-d-15-post-reaction', '3.2.4', 4560)
N['v71thank']['text'] = N['v71thank']['text'].replace('(3.2.4)', '(3.2.2)')
assert '(3.2.2)' in N['v71thank']['text']
ended = B['p-d-06-song-ended.dc.html']
N['v73after'] = {'fill': 'yellow', 'page': 'landing', 'size': 20, 'w': 380, 'x': ended['x'] + 430, 'y': ended['y'],
                 'text': 'After the song there is one question: send the video to Max or delete it (3.2.1). Then Anna is on her gift page. '
                         '“Let openyoursong show it” (3.2.3) and “Post it yourself” (3.2.4) open from the card on this page, only if she taps them'}

# =====================================================================
# 3. Emails and delivery
# =====================================================================
clone('p-e-mail-03-preview-ready.dc.html', 'p-e-mail-15-preview-waiting.dc.html', 'Email: preview is waiting', [
    ('Subject: Your preview for Anna is ready', 'Subject: 3 days to Anna’s birthday. Her song is ready to hear'),
    ('Your preview for <span class="nm">Anna</span> is ready', '<span class="nm">Anna</span>’s song is still waiting'),
    ('Two takes are waiting. Your lyrics and 6 photos are saved with them. Listen, check the name, then decide. No payment until you love it',
     'Anna’s birthday is on 14 March, in 3 days. Your two takes, lyrics and 6 photos are saved. Listen again and send it on the day. No payment until you love it'),
    ('Unpaid previews are deleted after 30 days', 'Unpaid previews are deleted after 30 days · <a href="#">Stop reminders about this song</a>'),
    ('You get this because of your order', 'You get this because you started a song'),
])
B['p-e-mail-15-preview-waiting.dc.html'] = {'x': 9520, 'y': 42384, 'w': 600, 'h': 760, 'page': 'landing', 'title': '5.2.15  Preview is waiting · email'}
clone('p-e-mail-06-time-to-send.dc.html', 'p-e-mail-16-not-opened.dc.html', 'Email: gift not opened yet', [
    ('Subject: It’s time to send Anna her song', 'Subject: Anna hasn’t opened her song yet'),
    ('It’s 09:00 in London. Time to send it', 'Anna hasn’t opened it yet'),
    ('Anna’s song is ready to open. Send the link the way you planned', 'We emailed Anna yesterday at 09:00 and the gift is still closed. Emails get lost, so send her the link yourself'),
    ('We remind you again in 2 hours if it’s not marked as sent', 'This is the only reminder about it'),
])
B['p-e-mail-16-not-opened.dc.html'] = {'x': 10200, 'y': 42384, 'w': 600, 'h': 792, 'page': 'landing', 'title': '5.2.16  Not opened yet · email'}
CJ['order'] += ['p-e-mail-15-preview-waiting.dc.html', 'p-e-mail-16-not-opened.dc.html']

# the giver sees Anna's written thanks (3.2.9) next to her reaction
thanks = ('<div style="border-radius:24px;background:#F2F2F2;padding:16px 20px;display:flex;flex-direction:column;gap:6px">'
          '<span class="mut" style="font-size:13px">Anna wrote back</span>'
          '<p style="margin:0;font-size:16px;line-height:1.5">“Max, I cried at the yellow bike. Best birthday present I’ve ever had”</p></div>')
for f in ['p-c-12-after-opened.dc.html', 'p-c-12-after-opened-d.dc.html']:
    a = '<div style="border-radius:24px;background:#FFD84D;padding:20px;display:flex;flex-direction:column;gap:16px;"><div style="display:flex;gap:16px;align-items:flex-start"><div aria-hidden="true"'
    rep(f, a, thanks + a)
    grow(f, 124)
N['t_p5_mail']['maxW'] = 10800

backup = ('<label style="display:flex;gap:10px;align-items:flex-start;font-size:14px;line-height:1.4;cursor:pointer%s"><input type="checkbox" style="' + CHK + '">'
          '<span>Email Anna if it’s still closed 2 hours after 09:00<span class="mut" style="display:block;font-size:13px;margin-top:2px">Off unless you tick it. We then ask for her email</span></span></label>')
rep('p-c-11-send-myself-d.dc.html', '<span class="mut" style="font-size:13px;line-height:1.4;">If you added her email and she hasn’t opened it 2 hours later, we email her too</span>', backup % ';max-width:360px')
rep('p-c-11-send-myself.dc.html', 'Schedule it with Send Later in iMessage</span></div>', 'Schedule it with Send Later in iMessage</span></div>' + backup % '')
grow('p-c-11-send-myself.dc.html', 80)
ready = B['p-c-07-ready.dc.html']
N['v73slides'] = {'fill': 'yellow', 'page': 'landing', 'size': 20, 'w': 380, 'x': ready['x'] + 430, 'y': ready['y'] + 420,
                  'text': 'Bundle, sent right now. For about 10 minutes after payment the slideshow tile says “Your slideshow will be ready at 12:40”. '
                          'The gift link works meanwhile: if Anna opens it earlier she sees the cover photo, and the slideshow joins the gift page when it’s done'}

# =====================================================================
# 4. Payment rules and small mismatches
# =====================================================================
for f in ['p-c-15-yearly-upgrade.dc.html', 'p-c-15-yearly-upgrade-d.dc.html']:
    rep(f, 'Open for 14 days after your order, until Anna opens the gift. Renews', 'Open for 14 days after your order. Renews')
N['v69year']['text'] = N['v69year']['text'].replace('Open 14 days after the order, until the gift is opened', 'Open 14 days after the order, also after the gift is opened')
assert 'also after the gift is opened' in N['v69year']['text']
rep('p-e-08-remake-refund.dc.html', 'until 14 Mar</span>', 'until 15 Mar</span>')
rep('p-e-08-remake-refund.dc.html', 'as long as Anna hasn’t opened the gift yet. The gift link stops working',
    'as long as Anna hasn’t opened the gift and you haven’t downloaded the MP3. After a download, write to us. The gift link stops working')
rep('p-e-08-remake-refund-d.dc.html', 'Full refund within 14 days of paying, while the gift is unopened. Yours is open until 15 March',
    'After both free remakes, a full refund within 14 days of paying, while the gift is unopened and the MP3 isn’t downloaded. Yours is open until 15 March')
WB = 'height:52px;border-radius:12px;background:#111;color:#fff;border:2px solid #111;font:500 17px Inter,system-ui,sans-serif;cursor:pointer;width:100%'
wallets = ('<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px"><button style="%s">Apple Pay</button><button style="%s">Google Pay</button></div>'
           '<div style="display:flex;align-items:center;gap:12px"><span style="flex:1;border-top:1px solid #DADADA"></span><span class="mut" style="font-size:13px">or pay by card</span>'
           '<span style="flex:1;border-top:1px solid #DADADA"></span></div>') % (WB, WB)
rep('p-c-05-checkout.dc.html', '  <div><label for="em" class="lbl">Email for the receipt and order link</label>', '  ' + wallets + '\n  <div><label for="em" class="lbl">Email for the receipt and order link</label>')
grow('p-c-05-checkout.dc.html', 76)
rep('p-c-05-checkout-d.dc.html', '<div><label class="lab" for="em">Receipt to</label>', wallets + '<div><label class="lab" for="em">Receipt to</label>')
grow('p-c-05-checkout-d.dc.html', 76)
# the organizer can hide someone's part, not rewrite a note signed with their name
for f in ['p-e-01-organizer.dc.html', 'p-e-01-organizer-d.dc.html']:
    if 'aria-label="Edit ' in rd(f):
        sub(f, r'<(button|a)\b[^>]*aria-label="Edit [^"]*"[^>]*>.*?</\1>', '', 0)

# the yearly plan upgrade (2.1.8) is reachable from the order page before and after the gift is opened
plan = '<a href="#" style="%s">More dates this year? Make this a yearly plan, +$30</a>' % LNK
for b in B.values():
    if b.get('page') == 'landing' and b['y'] == 22588:
        b['y'] += 80
for f in ['p-c-07-ready.dc.html', 'p-c-07b-ready-song-only.dc.html']:
    rep(f, 'See it as Anna will</a>', 'See it as Anna will</a>\n  ' + plan)
    grow(f, 68)
for f in ['p-c-07-ready-d.dc.html', 'p-c-07b-ready-song-only-d.dc.html']:
    a = '<div style="border-radius:24px;background:#F2F2F2;padding:20px;display:flex;flex-direction:column;gap:16px;"><div style="display:flex;gap:6px'
    rep(f, a, plan + a)
    grow(f, 68)
rep('p-c-12-after-opened.dc.html', 'Or email me 14 days before</a>', 'Or email me 14 days before</a><a href="#" style="font-size:14px">Every date on a plan, songs cost less</a>')
grow('p-c-12-after-opened.dc.html', 32)

# =====================================================================
# 6. One plan: yearly
# =====================================================================
MONTHLY = r'<div style="border-radius:28px;background:#F2F2F2;padding:32px;display:flex;flex-direction:column;gap:16px;"><strong style="font-size:18px;line-height:1.3">Monthly plan</strong>.*?Get the plan</a></div>'
sub('p-f-03-pricing.dc.html', MONTHLY, '')
grow('p-f-03-pricing.dc.html', -400)
sub('p-f-03-pricing-d.dc.html', MONTHLY, '')
rep('p-f-03-pricing-d.dc.html', 'grid-template-columns:repeat(4,1fr);gap:20px', 'grid-template-columns:repeat(3,1fr);gap:20px')

json.dump(CJ, open(P + 'canvas.json', 'w'), ensure_ascii=False, separators=(',', ':'))

# ---- sanity: boards on the page don't overlap, tags balance, every board has a file and the other way round
items = [(k, b) for k, b in B.items() if b.get('page') == 'landing']
for i, (k1, a) in enumerate(items):
    for k2, b in items[i + 1:]:
        if a['x'] < b['x'] + b['w'] and b['x'] < a['x'] + a['w'] and a['y'] < b['y'] + b['h'] and b['y'] < a['y'] + a['h']:
            print('OVERLAP', k1, k2)
files = set(f for f in os.listdir(P) if f.endswith('.dc.html'))
print('boards without file:', sorted(set(B) - files), 'files without board:', sorted(files - set(B)), 'order ok:', sorted(CJ['order']) == sorted(B))
for f in sorted(touched):
    s = rd(f)
    for tag in ['div', 'span', 'label', 'button', 'a', 'main', 'section', 'p', 'li', 'ul', 'ol']:
        o, c = len(re.findall(r'<%s[\s>]' % tag, s)), s.count('</%s>' % tag)
        if o != c:
            print('UNBALANCED', f, tag, o, c)
print(json.dumps({'changed': sorted(touched), 'removed': sorted(removed)}))
