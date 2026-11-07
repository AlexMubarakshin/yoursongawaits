from kit import *

OUT = []

def songcard(level):
    # level: how much of the order is filled in (0..5)
    rows = [
        ('For', 'Anna, a friend' if level >= 1 else '—'),
        ('Occasion', 'Her 30th birthday' if level >= 1 else '—'),
        ('From', 'Max and the whole flat' if level >= 1 else '—'),
        ('Story', 'Yellow bike, kettle at six, bad car singing' if level >= 2 else '—'),
        ('Sound', 'Pop, upbeat, female voice' if level >= 3 else '—'),
        ('Lyrics', 'Ready, 3 lines edited' if level >= 4 else '—'),
    ]
    rh = ''.join('<div style="display:grid;grid-template-columns:120px 1fr;gap:16px;padding:12px 0;border-top:1px solid #DADADA;font-size:15px"><span class="mut">%s</span><span style="font-weight:500%s">%s</span></div>' % (k, ';color:#8A8A8A' if v == '—' else '', v) for k, v in rows)
    title = '<p class="un" style="margin:0;font-size:28px;font-weight:500;line-height:1.2">A song for %s</p>' % (nm() if level >= 1 else 'someone')
    return card(img('box', 'A tangerine gift box with a blue ribbon and paper confetti', 240) + title + '<div>%s</div>' % rh
                + small('Free 30–45 s preview before you pay · $29 if you love it'), pad=32, r=28, gap=20)

def wiz_d(name, title, step, left, level, bar_label, note=''):
    L = col(left, rowx(btn('Back', 'bo', icon='back'), btn(bar_label), small(note) if note else '', gap=12), gap=40)
    OUT.append(write(name, desktop(title, d_head('wizard', step), L, songcard(level), split='640px 1fr', pad='56px 120px 0 120px', gap=96)))

# b01 solo or together
left = col(col(un('Are you giving it alone or together', 48, tag='h1'), t('No sign-up needed. What you type is saved as you go', 18, True), gap=16),
           col(radio('Just me', 'You tell the story, you get the song. Takes about three minutes', True, 'm'),
               radio('Together', 'Invite up to 20 people to add a memory. One person pays, same price', False, 'm'), gap=12), gap=32)
wiz_d('p-b-01-solo-or-together-d.dc.html', 'Create 1: alone or together, desktop', 1, left, 0, 'Continue', 'Free 30–45 s preview')

# b02 who
left = col(un('Who is it for', 48, tag='h1'),
           '<div style="display:grid;grid-template-columns:1fr 1fr;gap:16px">%s%s</div>' % (inp('n', 'Their name', 'Anna', hint='Up to 40 characters'), inp('f', 'Sign it from', 'Max and the whole flat', hint='Shown on the gift page')),
           chips(['Partner', 'Friend', 'Mum', 'Dad', 'Sister', 'Brother', 'Colleague', 'Grandma', 'More'], ['Friend'], 'They are your'),
           chips(['Birthday', 'Anniversary', "Valentine's", "Mother's Day", 'Wedding', 'Retirement', 'Just because', 'More'], ['Birthday'], 'Occasion'), gap=28)
wiz_d('p-b-02-who-is-it-for-d.dc.html', 'Create 2: who is it for, desktop', 1, left, 1, 'Continue')

# b03 story
left = col(un('Tell us about %s' % nm(), 48, tag='h1'),
           t('The small details make the song. Nicknames, places, a joke only you two get', 18, True),
           chips(['How you met', 'What she loves', 'Your inside joke', 'Her favourite phrase', 'What you are proud of'], [], 'Ideas'),
           ta('s', 'Her story', 'We met in the flat on Elm Street. She still rides the yellow bike everywhere, puts the kettle on at six for everyone and sings badly in the car. Turning 30 and still the first to dance', 168, '211 / 1500'), gap=24)
wiz_d('p-b-03-their-story-d.dc.html', 'Create 3: their story, desktop', 2, left, 1, 'Continue', 'At least 50 characters')

# b04 sound
genres = ['Pop', 'Acoustic', 'Ballad', 'Country', 'R&amp;B', 'Rock', 'Hip-hop', 'Jazz', 'Kids']
g = '<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:12px">%s</div>' % ''.join(
    '<div style="display:flex;align-items:center;gap:12px;padding:12px;border-radius:16px;%s">%s<strong style="font-size:16px">%s</strong></div>' % ('background:#FFD84D;border:2px solid #111' if x == 'Pop' else 'background:#F2F2F2;border:2px solid #F2F2F2', play('Play a 10 second %s sample' % x, 40), x) for x in genres)
left = col(un('How should it sound', 48, tag='h1'), col('<span class="lab" style="margin:0">Style, tap to hear 10 s</span>', g, gap=8),
           '<div style="display:grid;grid-template-columns:1fr 1fr;gap:24px">%s%s</div>' % (chips(['Upbeat', 'Warm', 'Funny', 'Tender'], ['Upbeat'], 'Mood'), chips(['Female', 'Male'], ['Female'], 'Voice')), gap=28)
wiz_d('p-b-04-genre-and-voice-d.dc.html', 'Create 4: sound, desktop', 3, left, 2, 'Write the lyrics', 'In English · about 20 s')

# b05 lyrics
def sec(name, lines, edit=False):
    if edit:
        body = ta('v2', name, '\n'.join(lines), 112) + rowx(btn('Save lines', sm=True, tag='button'), btn('Cancel', 'bo', sm=True, tag='button'), gap=8)
        return frame(body, pad=20, gap=12)
    ls = ''.join('<p style="margin:0;font-size:17px;line-height:1.6">%s</p>' % l for l in lines)
    return '<div style="display:flex;justify-content:space-between;gap:24px;padding:16px 0;border-top:1px solid #DADADA"><div style="display:flex;flex-direction:column;gap:4px"><span class="mut" style="font-size:13px">%s</span>%s</div>%s</div>' % (name, ls, btn('Edit', 'bo', sm=True, tag='button'))
left = col(un('Here are the lyrics', 48, tag='h1'), t('Edit any line, or ask for a rewrite. Music is not made yet', 18, True),
           col(sec('Verse 1', ['%s, you still ride that yellow bike' % nm(), 'down Elm Street like it’s summer every night']),
               sec('Chorus', ['Thirty candles, kettle on at six', 'the whole flat singing, out of tune and quick']),
               sec('Verse 2', ['You sing too loud in the car again', 'and we turn it up, we never complain'], True), gap=0),
           rowx('<div style="flex:1">%s</div>' % inp('w', 'Rewrite with a wish', ph='Funnier, add the dog'), btn('Rewrite', 'bo', tag='button', icon='redo'), align='flex-end'),
           small('9 rewrites left'), gap=20)
OUT.append(write('p-b-05-lyrics-ready-d.dc.html', desktop('Create 5: lyrics, desktop', d_head('wizard', 4), col(left, rowx(btn('Back', 'bo', icon='back'), btn('Lyrics look good'), gap=12), gap=32), songcard(3), split='640px 1fr', pad='48px 120px 0 120px', gap=96, h=1160)))

# b06 email
left = col(un('Where should we send %s’s preview' % nm(), 48, tag='h1'), t('We email you the link in case you close this tab. No payment yet', 18, True),
           inp('e', 'Your email', 'max.r@mail.com', typ='email'), check('Send me occasional news and offers', False, 'mk'),
           card(strong('Next') + steps(['Lyrics checked', 'Check how the name sounds', 'Free 30–45 s preview'], 1), pad=24), gap=24)
wiz_d('p-b-06-email-d.dc.html', 'Create 6: email, desktop', 4, left, 4, 'Make the music', '$29 only if you love it')

# b07 moderation, NEW (mobile + desktop)
mm = col(
    '<div style="width:56px;height:56px;border-radius:16px;background:#FFD84D;display:flex;align-items:center;justify-content:center">%s</div>' % ico('alert', '#111', 26),
    un('We can’t write this one as it is', 30, tag='h1'), t('A line in the story mentions a real singer by name. We don’t write songs in the style of real artists. Change it and we’ll try again', 16, True),
    frame(small('The part we flagged') + '<p style="margin:0;font-size:16px;line-height:1.5">“…she sings like <span style="background:#FFD84D;padding:0 4px;border-radius:4px">Adele</span> in the car…”</p>', pad=20, gap=8),
    ta('fix', 'Edit that part', 'She sings at the top of her voice in the car', 96), gap=20)
OUT.append(write('p-b-07-moderation.dc.html', mobile('Create: story needs a change', m_head('wizard', 2), mm, btn('Try again', full=True, tag='button') + small('Your other answers are kept', extra='text-align:center'))))
dl = col('<div style="width:64px;height:64px;border-radius:16px;background:#FFD84D;display:flex;align-items:center;justify-content:center">%s</div>' % ico('alert', '#111', 30),
         un('We can’t write this one as it is', 48, tag='h1'),
         t('A line in the story mentions a real singer by name. We don’t write songs in the style of real artists, quote other songs or include anything hurtful. Change it and we’ll try again', 18, True),
         frame(small('The part we flagged') + '<p style="margin:0;font-size:17px;line-height:1.5">“…she sings like <span style="background:#FFD84D;padding:0 4px;border-radius:4px">Adele</span> in the car…”</p>', pad=24, gap=8),
         ta('fixd', 'Edit that part', 'She sings at the top of her voice in the car', 96),
         rowx(btn('Back', 'bo', icon='back'), btn('Try again'), small('Your other answers are kept'), gap=12), gap=24)
OUT.append(write('p-b-07-moderation-d.dc.html', desktop('Create: story needs a change, desktop', d_head('wizard', 2), dl, songcard(1), split='640px 1fr', pad='48px 120px 0 120px', gap=96)))
