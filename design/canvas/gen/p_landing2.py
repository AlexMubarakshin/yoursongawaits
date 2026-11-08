import re, sys
sys.path.insert(0, 'gen')
from landing_parts import *
P = 'artifact-files/b4a8099c-b52e-41d0-ad8e-182f529e1959/project/'
def swap(s, marker, new):
    k = s.index(marker); i = s.rindex('<section', 0, k); j = s.index('</section>', k) + 10
    return s[:i] + new + s[j:]
HOW_D = '''<div class="frame" style="margin-top:20px;padding:40px;display:grid;grid-template-columns:400px 1fr;gap:64px;align-items:center">
      <div style="display:flex;flex-direction:column;gap:16px"><span class="mut" style="font-size:15px">Step 2, before you pay</span><h3 class="un" style="margin:0;font-size:40px;font-weight:500;line-height:1.1">You hear the name first</h3><p style="margin:0;font-size:16px;line-height:1.5;color:#4A4A4A">Up to two takes with their name sung. If it sounds off, you fix the spelling and we sing it again</p></div>
      <div style="border-top:1px solid #DADADA">%s</div>
    </div>'''
def take(n, sub):
    return '<div style="display:flex;align-items:center;gap:16px;padding:16px 0;border-bottom:1px solid #DADADA"><button class="play" aria-label="Play take %d" style="width:48px;height:48px">%s</button><div style="display:flex;flex-direction:column;gap:4px;flex:1"><strong style="font-size:17px">Take %d</strong><span class="mut" style="font-size:14px">%s</span></div><span class="mut" style="font-size:14px;font-variant-numeric:tabular-nums">0:40</span></div>' % (n, PLAY, n, sub)
for f, mob in [('03-cut-paper-landing.dc.html', False), ('03-cut-paper-landing-mobile.dc.html', True), ('03-cut-paper-landing-mobile-2.dc.html', True)]:
    s = open(P + f).read()
    if 'Listen to a few first' in s: s = swap(s, 'Listen to a few first', feed(mob))
    if 'What Anna sees, and what comes back' in s: s = swap(s, 'What Anna sees, and what comes back', sees(mob))
    if 'What people said after' in s: s = swap(s, 'What people said after', reviews(mob))
    # how-it-works: listen-only demo, no form on a landing
    m = re.search(r'<div class="frame" style="margin-top:20px;padding:40px;display:grid[\s\S]*?Sounds right</button>\s*</div>\s*</div>', s)
    if m: s = s[:m.start()] + HOW_D % (take(1, 'Pop, bright') + take(2, 'Pop, slower')) + s[m.end():]
    # final banner: ink button on butter, and room before the footer
    k = s.find('Their name, their story, their song')
    if k > 0:
        i = s.rindex('<section', 0, k); j = s.index('</section>', k)
        seg = s[i:j].replace('class="btn bk"', 'class="btn bi"')
        seg = seg.replace('<section style="margin:0 64px;', '<section style="margin:0 64px 96px;').replace('<section style="margin:0 20px;', '<section style="margin:0 20px 48px;')
        s = s[:i] + seg + s[j:]
    open(P + f, 'w').write(s)
    print(f, 'Example songs, made' in s, s.count('Spell it by sound'), s.count('phon'))
