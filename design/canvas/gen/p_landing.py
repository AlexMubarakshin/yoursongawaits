import re, sys
sys.path.insert(0, 'gen')
from landing_parts import *
P = 'artifact-files/b4a8099c-b52e-41d0-ad8e-182f529e1959/project/'
SONG = ['The full song with their name, as MP3', 'Lyrics and a gift page made for them', 'Delivery on the date and time you pick', 'A printable PDF card with a QR code', 'Their reaction video, if they record one']
BUND = ['<strong>Everything in the song</strong>', 'A second version of the song', 'A photo slideshow set to it', 'Printable lyrics', 'Upgrade later by paying the difference']
TOG_H = 'A song from the whole group'
TOG_P = 'Share one link. Up to 20 friends add a memory and a note. We build one song from all of them, and one person pays the usual price'

def sec(s, start_marker):
    i = s.index(start_marker); j = s.index('</section>', i) + len('</section>'); return i, j

def apply(f, mobile):
    s = open(P + f).read()
    # 1. feed replaces the single preview line and the old examples list, right under the hero
    if not mobile:
        i, j = sec(s, '<section aria-label="A line from Anna\'s preview"'); s = s[:i] + s[j:]
    i, j = sec(s, '<section id="examples"'); s = s[:i] + s[j:]
    i = s.index('<section id="how"'); s = s[:i] + feed(mobile) + '\n  ' + s[i:]
    # 2. what Anna sees: one left-to-right story
    i, j = sec(s, 'What Anna sees, and what comes back to you'); i = s.rindex('<section', 0, i); s = s[:i] + sees(mobile) + '\n  ' + reviews(mobile) + s[j:]
    # 3. occasions get a picture
    i = s.index('Pick the occasion and we shape the song around it. Or skip it and just tell us why</p>') + len('Pick the occasion and we shape the song around it. Or skip it and just tell us why</p>')
    pic = '<div class="ph" style="height:%dpx;border-radius:24px;margin-top:%dpx"><img src="/_blob/%s" alt="A mother laughing while making pancakes" style="object-position:50%% 35%%"></div>' % (220 if mobile else 340, 8 if mobile else 24, B['r06'])
    s = s[:i] + pic + s[i:]
    # 4. group headline
    s = s.replace('The whole group chat in one song', TOG_H)
    s = re.sub(r'Share one link\. Up to 20 friends add a memory and a note, no sign-up\.[^<]*', TOG_P, s)
    # 5. pricing perks
    s = re.sub(r'<ul style="margin:0;padding:0;list-style:none;display:flex;flex-direction:column;gap:12px;font-size:1\dpx">\s*<li>The full song[\s\S]*?</ul>', lambda m: perks(SONG, mobile), s, count=1)
    s = re.sub(r'<ul style="margin:0;padding:0;list-style:none;display:flex;flex-direction:column;gap:12px;font-size:1\dpx">\s*<li>Everything in the song[\s\S]*?</ul>', lambda m: perks(BUND, mobile), s, count=1)
    open(P + f, 'w').write(s)
    print(f, s.count('Listen to a few first'), s.count('What people said after'), s.count(TOG_H), s.count('rgba(17,17,17,.12)'))

apply('03-cut-paper-landing.dc.html', False)
