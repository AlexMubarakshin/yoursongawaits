import re, kit, glob
P = kit.PROJ + '/'; I = kit.IMG
PH = ['sofa', 'family', 'candles', 'r01', 'r09', 'r05']
PLUS = '<svg aria-hidden="true" width="22" height="22" viewBox="0 0 24 24"><path d="M12 5v14M5 12h14" fill="none" stroke="#111" stroke-width="1.8" stroke-linecap="round"></path></svg>'
X = '<svg aria-hidden="true" width="12" height="12" viewBox="0 0 24 24"><path d="M6 6l12 12M18 6L6 18" fill="none" stroke="#111" stroke-width="2.4" stroke-linecap="round"></path></svg>'
def grid(cols, size, empty):
    cells = ''.join('<div style="position:relative;height:%dpx"><div class="ph" style="height:%dpx;border-radius:14px"><img src="/_blob/%s" alt="Your photo %d"></div><button aria-label="Remove photo %d" style="position:absolute;top:6px;right:6px;width:24px;height:24px;border-radius:50%%;border:none;background:#fff;display:flex;align-items:center;justify-content:center;cursor:pointer">%s</button></div>' % (size, size, I[k], n + 1, n + 1, X) for n, k in enumerate(PH))
    cells += '<button style="height:%dpx;border-radius:14px;border:2px dashed #111;background:#FFD84D;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:6px;cursor:pointer;font:500 14px Inter,system-ui,sans-serif;color:#111">%sAdd photos</button>' % (size, PLUS)
    cells += ''.join('<div style="height:%dpx;border-radius:14px;border:2px dashed #DADADA"></div>' % size for _ in range(empty))
    return '<div style="display:grid;grid-template-columns:repeat(%d,1fr);gap:8px">%s</div>' % (cols, cells)
WHY = 'They go on Anna’s gift page next to the song, and we can set them to the music as a slideshow'
META = '6 of 20 · from your phone or computer · only Anna and you see them'

# ---- 1. giver name, said plainly
for f in ['p-b-02b-occasion.dc.html', 'p-b-02b-occasion-d.dc.html']:
    s = open(P + f).read()
    s = s.replace('>Sign it from</label>', '>Your name, as it goes on the card</label>').replace('>Shown on the gift page</span>', '>Anna sees it on the gift page and the printed card. Add others if it’s from more of you</span>')
    open(P + f, 'w').write(s)

# ---- 2. photos step, mobile (cloned from the occasion screen: same header, progress, bar)
s = open(P + 'p-b-02b-occasion.dc.html').read()
i = s.index('<main'); j = s.index('</main>') + 7
main = ('<main style="padding:0 20px;display:flex;flex-direction:column;gap:20px">'
        '<div style="display:flex;flex-direction:column;gap:12px"><h1 class="un h1">Add photos of you and <span style="background:#FFD84D;padding:0 8px;border-radius:4px">Anna</span></h1><p class="mut" style="margin:0;font-size:16px;line-height:1.5">%s</p></div>'
        '%s<span class="mut" style="font-size:13px;line-height:1.4">%s</span></main>') % (WHY, grid(3, 104, 2), META)
s = s[:i] + main + s[j:]
s = re.sub(r'(<div style="position:absolute;left:0;right:0;bottom:0;[^"]*)(">)<button class="btn bk" style="width:100%">Continue</button>',
           r'\1;align-items:center;gap:12px\2<button class="btn bk" style="width:100%">Continue</button><a href="#" style="font-size:15px">Skip, add photos later</a>', s)
s = s.replace('Create 2b: occasion', 'Create 2c: photos')
open(P + 'p-b-02c-photos.dc.html', 'w').write(s)

# ---- 2. photos step, desktop
s = open(P + 'p-b-02b-occasion-d.dc.html').read()
i = s.index('<h1'); j = s.index('<div style="display:flex;align-items:center;gap:12px;"><a class="btn bo"', i)
left = ('<h1 class="un" style="margin:0;font-size:48px;font-weight:500;line-height:1.15;letter-spacing:-.02em;">Add photos of you and <span class="nm">Anna</span></h1>'
        '<p class="mut" style="margin:0;font-size:18px;line-height:1.5">%s</p>%s<span class="mut" style="font-size:13px;line-height:1.4">%s · or drag them here</span></div>') % (WHY, grid(4, 148, 1), META)
s = s[:i] + left + s[j:]
s = s.replace('<a class="btn bk" href="#" style="">Continue</a>', '<a class="btn bk" href="#" style="">Continue</a><a href="#" style="font-size:15px;margin-left:12px">Skip, add photos later</a>')
s = s.replace('Create 2b: occasion', 'Create 2c: photos')
open(P + 'p-b-02c-photos-d.dc.html', 'w').write(s)

# ---- 3. sidebar gets a Photos row; after the photo step it shows the user's first photo
CUR = '<span style="display:flex;align-items:center;gap:8px;font-weight:500"><span style="width:8px;height:8px;border-radius:50%;background:#FFD84D;border:1.5px solid #111"></span>Filling in now</span>'
SK = '<span aria-label="Comes later" style="display:flex;align-items:center"><span style="display:block;width:96px;height:10px;border-radius:5px;background:#F2F2F2"></span></span>'
ROW = '<div style="display:grid;grid-template-columns:120px 1fr;gap:16px;padding:12px 0;border-top:1px solid #DADADA;font-size:15px"><span class="mut">Photos</span>%s</div>'
state = {'p-b-01-solo-or-together-d': SK, 'p-b-02-who-is-it-for-d': SK, 'p-b-02b-occasion-d': SK, 'p-b-02c-photos-d': CUR}
for f in glob.glob(P + 'p-b-*-d.dc.html'):
    n = f.split('/')[-1][:-8]; s = open(f).read()
    if '<span class="mut">Photos</span>' in s: continue
    v = state.get(n, '<span style="font-weight:500">6 photos</span>')
    s, k = re.subn(r'(<span class="mut">From</span>[\s\S]*?</span></div>)', lambda m: m.group(1) + ROW % v, s, count=1)
    if n not in state:
        s = s.replace('<div class="ph" style="height:240px;border-radius:24px;flex-shrink:0"><img src="/_blob/2892b385f1c5f1e8dedf7df3815e506f" alt="A tangerine gift box with a blue ribbon and paper confetti" style="">',
                      '<div class="ph" style="height:240px;border-radius:24px;flex-shrink:0"><img src="/_blob/%s" alt="Your photo of Anna and the flat on the sofa" style="object-position:50%% 45%%">' % I['sofa'])
    open(f, 'w').write(s); print(n, k)
