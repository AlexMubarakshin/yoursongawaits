from kit import *
import re
P = PROJ + '/'
SLIDES = ['sofa', 'family', 'candles', 'r09', 'r05', 'r01']
def dots(n=6, cur=2):
    return '<div aria-label="Photo %d of %d" style="display:flex;justify-content:center;gap:6px">%s</div>' % (cur + 1, n, ''.join('<span style="width:%dpx;height:6px;border-radius:3px;background:%s"></span>' % (18 if i == cur else 6, '#111' if i == cur else '#DADADA') for i in range(n)))
def stage(h, key='candles', r=24):
    return col(img(key, 'Photo from Max, part of the slideshow playing with the song', h, '50% 45%', r=r), dots(), gap=10)
LYR = [('Morning comes and the kettle sings', 0), ('%s, you still ride that yellow bike' % nm(), 1), ('Down the hill with the whole flat behind', 0), ('Thirty looks good on you tonight', 0)]
def lyrics(big=False):
    return col(*['<p class="un%s" style="margin:0;font-size:%dpx;font-weight:500;line-height:1.3;letter-spacing:-.01em">%s</p>' % ('' if on else ' mut', (30 if on else 22) if big else (21 if on else 17), l) for l, on in LYR], gap=12 if big else 10)
def note_card(big=False):
    tape = '<span aria-hidden="true" style="position:absolute;top:-10px;left:50%;transform:translateX(-50%) rotate(2deg);width:72px;height:20px;background:#FFD84D;border-radius:2px"></span>'
    return ('<article style="position:relative;background:#fff;border:1px solid #DADADA;border-radius:6px;box-shadow:0 8px 20px rgba(17,17,17,.10);padding:28px 22px 20px;transform:rotate(-1deg);display:flex;flex-direction:column;gap:14px">%s'
            '<span class="mut" style="font-size:13px">A note from Max</span><p style="margin:0;font-size:%dpx;line-height:1.45">“Thirty and still the first one dancing. Love you, the whole flat”</p></article>') % (tape, 24 if big else 18)
REC = re.search(r'<button style="height:44px;display:flex;align-items:center;gap:8px;[\s\S]*?Stop</span></button>', open(P + 'p-d-04-song-playing.dc.html').read()).group(0)
CTRL = re.search(r'<div style="display:flex;flex-direction:column;gap:8px">\s*<input type="range"[\s\S]*?Forward 10 seconds"[\s\S]*?</button>\s*</div>', open(P + 'p-d-04-song-playing.dc.html').read()).group(0)
FOOT = '<p class="mut" style="margin:0;font-size:13px;line-height:1.5;text-align:center">Your reaction is recording on this phone only. Nothing is sent yet</p>'
TITLE = col('<strong class="un" style="font-size:18px;font-weight:500">Anna, happy 30th</strong>', '<span class="mut" style="font-size:14px">From Max and the whole flat</span>', gap=2)

def m_play(middle, title, name, h=900):
    body = ('<header style="display:flex;align-items:center;justify-content:space-between;padding:16px 20px;height:76px"><span class="mut" style="font-size:14px">Your song</span>%s</header>'
            '<section style="padding:0 20px 24px;display:flex;flex-direction:column;gap:20px">%s%s%s%s%s</section>') % (REC, stage(300), TITLE, middle, CTRL, FOOT)
    write(name, doc(title, 390, h, body))
def d_play(middle, title, name):
    right = col('<div style="display:flex;justify-content:space-between;align-items:center">%s%s</div>' % (TITLE, REC), middle, CTRL, FOOT.replace('phone', 'device'), gap=32, extra='justify-content:center;min-height:640px')
    body = '<main style="display:grid;grid-template-columns:1fr 1fr;gap:96px;padding:40px 96px 0;align-items:center">%s%s</main>' % (stage(640, r=28), right)
    write(name, doc(title, 1440, 800, body))

# 3.1.9 song playing: photos change with the music, lyrics follow
m_play(lyrics(), 'Gift: song playing', 'p-d-04-song-playing.dc.html')
d_play(lyrics(True), 'Gift: song playing, desktop', 'p-d-04-song-playing-d.dc.html')
# new: during the instrumental break the note appears with its photo
mid_m = col(note_card(), '<span class="mut" style="font-size:13px;text-align:center;display:block">Instrumental · the lyrics come back at 1:58</span>', gap=12)
m_play(mid_m, 'Gift: note during the song', 'p-d-04b-note-moment.dc.html', h=900)
d_play(col(note_card(True), '<span class="mut" style="font-size:14px">Instrumental · the lyrics come back at 1:58</span>', gap=16), 'Gift: note during the song, desktop', 'p-d-04b-note-moment-d.dc.html')

# 3.2.4 song ended -> the gift page from now on: play again, photos, lyrics, notes, then keep and share
def gift_d(name, title, photo, right, h=900, pos=None):
    ph = h - 72 - 48
    left = '<div style="height:%dpx">%s</div>' % (ph, img(photo[0], photo[1], ph, pos, r=28))
    R = '<div style="display:flex;flex-direction:column;justify-content:center;min-height:%dpx;max-width:540px">%s</div>' % (ph, right)
    write(name, desktop(title, d_head('gift'), left, R, h=h, split='1fr 1fr', pad='0 48px 48px 48px', gap=96, align='center'))
CAP_S = 'Max and the whole flat made me a song for my 30th · made with @openyoursong'
thanks = lambda sz: card(un('Happy 30th, %s' % nm(white=True), sz) + t('“Thirty and still the first one dancing. Love you, the whole flat”', 15) + small('Your reaction is on its way to Max', mut=False), bg='#FFD84D', pad=24, r=24, gap=10)
again = '<div style="display:flex;align-items:center;gap:14px">%s<div style="flex:1;display:flex;flex-direction:column;gap:2px"><strong style="font-size:16px">Play it again</strong><span class="mut" style="font-size:14px">With the photos and the lyrics · 2:48</span></div><a href="#" style="font-size:14px">Lyrics</a></div>' % play('Play the song again', 48)
def photos(cols, size):
    cells = ''.join('<span class="ph" style="height:%dpx;border-radius:12px;display:block"><img src="/_blob/%s" alt="Photo from Max"></span>' % (size, IMG[k]) for k in SLIDES)
    return col('<div style="display:flex;justify-content:space-between;align-items:baseline"><strong style="font-size:17px">Your photos from Max</strong><span class="mut" style="font-size:14px">6 photos</span></div>',
               '<div style="display:grid;grid-template-columns:repeat(%d,1fr);gap:6px">%s</div>' % (cols, cells), btn('Watch the slideshow', 'bo', sm=True, icon='play', extra='align-self:flex-start'), gap=12)
keep = '<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px">%s%s</div>' % (btn('Download MP3', 'bo', icon='down', full=True, tag='button', extra='padding:0 12px'), btn('Thank Max', 'bo', full=True, tag='button', extra='padding:0 12px'))
def make_card(d=False):
    b = btn('Make a song', 'bo', sm=True)
    if d: return card(rowx('<div style="flex:1;display:flex;flex-direction:column;gap:4px">%s%s</div>' % (strong('Make one like this for someone you love', 16), small('A song with their name in it, $29 · free preview first', mut=False)), b), pad=20)
    return card(strong('Make one like this for someone you love', 16) + small('A song with their name in it, $29 · free preview first', mut=False) + b.replace('style="', 'style="align-self:flex-start;', 1), pad=20, gap=8)
m = col(thanks(26), again, '<div class="hr"></div>', photos(3, 104), '<div class="hr"></div>', keep, col(strong('Share your song', 17), social_m(CAP_S, ('TikTok', 'WhatsApp', 'More')), gap=10), make_card(), gap=20, extra='padding-bottom:24px')
write('p-d-06-song-ended.dc.html', mobile('Gift: song ended, the gift page', m_head('gift'), m, h=1640))
gift_d('p-d-06-song-ended-d.dc.html', 'Gift: song ended, the gift page, desktop', ('candles', 'Candles on a 30th birthday cake'),
       col(thanks(32), again, '<div class="hr"></div>', photos(6, 76), '<div class="hr"></div>', keep, col(strong('Share your song', 18), social_d(CAP_S), gap=12), make_card(True),
           small('Made with AI + Max’s story · <a href="#">Remove my video</a> · <a href="#">Report</a>'), gap=20), h=1500)
