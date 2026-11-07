# Shared component kit for OpenYourSong Cut Paper screens (mobile + desktop)
import os, re

PROJ = "/private/tmp/claude-501/-Users-alexdev-projects-personal-congrats/bd37b841-e6fb-40ab-b6f4-ae825644ffa1/scratchpad/artifact-files/b4a8099c-b52e-41d0-ad8e-182f529e1959/project"

HELMET = """<helmet>
<link href="https://fonts.googleapis.com/css2?family=Unbounded:wght@500;800&amp;family=Inter:wght@400;500&amp;display=swap" rel="stylesheet">
<style>
body{margin:0}
strong{font-weight:500}
a{color:#111}a:hover{color:#FF7A00}
.cp{font-family:Inter,system-ui,sans-serif;color:#111;background:#fff}
.cp *{box-sizing:border-box}
.un{font-family:Unbounded,Inter,sans-serif}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:8px;height:56px;padding:0 28px;border-radius:12px;font-weight:500;font-size:17px;text-decoration:none;font-family:inherit;cursor:pointer;border:none;white-space:nowrap}
.btn.sm{height:44px;padding:0 20px;font-size:15px}
.bk{background:#111;color:#fff}
.bk:hover{background:#333;color:#fff}
.bo{background:#fff;color:#111;border:2px solid #111}
.by{background:#FFD84D;color:#111}
.bw{background:#fff;color:#111}
.dis{background:#F2F2F2;color:#8A8A8A;cursor:not-allowed}
.ph{overflow:hidden;border-radius:24px;background:#F2F2F2}
.ph img{width:100%;height:100%;object-fit:cover;display:block}
.play{width:44px;height:44px;border-radius:50%;background:#111;border:none;display:flex;align-items:center;justify-content:center;flex-shrink:0;cursor:pointer}
.mut{color:#4A4A4A}
.h1m{margin:0;font-size:30px;font-weight:500;letter-spacing:-.02em;line-height:1.1}
.h1d{margin:0;font-size:48px;font-weight:500;letter-spacing:-.02em;line-height:1.05}
.h3{margin:0;font-size:20px;font-weight:500;line-height:1.2}
.lab{font-size:14px;font-weight:500;display:block;margin-bottom:8px}
.inp{width:100%;height:52px;border:2px solid #111;border-radius:12px;padding:0 16px;font:500 17px Inter,system-ui,sans-serif;color:#111;background:#fff}
.ta{width:100%;border:2px solid #111;border-radius:12px;padding:16px;font:400 16px/1.5 Inter,system-ui,sans-serif;color:#111;background:#fff;resize:none}
.chip{display:inline-flex;align-items:center;height:44px;padding:0 16px;border-radius:12px;border:1px solid #DADADA;background:#fff;font:500 15px Inter,system-ui,sans-serif;color:#111;cursor:pointer;gap:8px}
.chip.on{background:#111;color:#fff;border-color:#111}
.chips{display:flex;flex-wrap:wrap;gap:8px}
.card{border-radius:24px;background:#F2F2F2;padding:24px}
.frame{border:1px solid #DADADA;border-radius:24px;background:#fff}
.hr{border-top:1px solid #DADADA}
.tn{font-variant-numeric:tabular-nums}
.nm{background:#FFD84D;padding:0 8px;border-radius:4px}
.nmw{background:#fff;padding:0 8px;border-radius:4px}
.li{display:flex;align-items:center;gap:12px;padding:12px 0;border-bottom:1px solid #DADADA}
.fl{display:flex;align-items:center;min-height:44px;text-decoration:none}
.chk{width:22px;height:22px;margin:0;accent-color:#111;flex-shrink:0}
</style>
</helmet>"""

IMG = {
 'box':'2892b385f1c5f1e8dedf7df3815e506f','bed':'e354aac9a424c73c0156013efdeaf1bd','r01':'2744d11a0bc2b86bbfb658477ac52617',
 'r09':'7f51b06f9dac967318218abfed7fecc2','r05':'2e424d0b737f69811f2caaeee23c5d93','r08':'569a369cbde8dfb0c60e52425af4b96c',
 'candles':'84d89a78197fb53d36fc38f060588b8c','family':'753681caffaf93a756329748141b4104','max':'d013d6e315836c683e8ad903fab40d3f',
 'cal':'2a17c1433c28b630a8a2c681eb0bba92','sofa':'5c825ead91ccef82ac575d6be71a2319','office':'ca7740159a99c62c8060e76efe18a779',
 'mum':'b84a9519552c7276a7f67d913a01ed45','dad':'f2f411ec00795b0ea6ea67c498d9ebd2','wed':'622571a5efec9dcfab9862a7f3332a70',
 'r06':'e0bf68270375990a6c155c753ae64c80','head':'8dc0a0f37bdd55b766f2a195b5837c3e',
}

def ico(name, color='#111', size=18):
    p = {
     'play':'<path d="M7 4.5l10 7.5-10 7.5z" fill="none" stroke="%s" stroke-width="2" stroke-linejoin="round"></path>',
     'pause':'<path d="M8 5v14M16 5v14" fill="none" stroke="%s" stroke-width="2.4" stroke-linecap="round"></path>',
     'back':'<path d="M15 5l-7 7 7 7" fill="none" stroke="%s" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path>',
     'check':'<path d="M5 12.5l4.5 4.5L19 7.5" fill="none" stroke="%s" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path>',
     'copy':'<rect x="8" y="8" width="12" height="12" rx="2" fill="none" stroke="%s" stroke-width="1.8"></rect><path d="M16 8V5a1 1 0 00-1-1H5a1 1 0 00-1 1v10a1 1 0 001 1h3" fill="none" stroke="%s" stroke-width="1.8"></path>',
     'cal':'<rect x="4" y="5" width="16" height="15" rx="2" fill="none" stroke="%s" stroke-width="1.8"></rect><path d="M4 10h16M9 3v4M15 3v4" fill="none" stroke="%s" stroke-width="1.8" stroke-linecap="round"></path>',
     'cam':'<rect x="3" y="7" width="13" height="11" rx="2" fill="none" stroke="%s" stroke-width="1.8"></rect><path d="M16 11l5-3v9l-5-3" fill="none" stroke="%s" stroke-width="1.8" stroke-linejoin="round"></path>',
     'down':'<path d="M12 4v11M7 10l5 5 5-5M5 20h14" fill="none" stroke="%s" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"></path>',
     'share':'<path d="M12 15V4M8 8l4-4 4 4M5 13v6a1 1 0 001 1h12a1 1 0 001-1v-6" fill="none" stroke="%s" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"></path>',
     'x':'<path d="M6 6l12 12M18 6L6 18" fill="none" stroke="%s" stroke-width="2" stroke-linecap="round"></path>',
     'menu':'<path d="M4 7h16M4 12h16M4 17h16" fill="none" stroke="%s" stroke-width="2" stroke-linecap="round"></path>',
     'mail':'<rect x="3" y="5" width="18" height="14" rx="2" fill="none" stroke="%s" stroke-width="1.8"></rect><path d="M4 7l8 6 8-6" fill="none" stroke="%s" stroke-width="1.8" stroke-linejoin="round"></path>',
     'lock':'<rect x="5" y="11" width="14" height="9" rx="2" fill="none" stroke="%s" stroke-width="1.8"></rect><path d="M8 11V8a4 4 0 018 0v3" fill="none" stroke="%s" stroke-width="1.8"></path>',
     'photo':'<rect x="3" y="5" width="18" height="14" rx="2" fill="none" stroke="%s" stroke-width="1.8"></rect><circle cx="9" cy="10" r="2" fill="none" stroke="%s" stroke-width="1.8"></circle><path d="M21 16l-5-5-8 8" fill="none" stroke="%s" stroke-width="1.8" stroke-linejoin="round"></path>',
     'plus':'<path d="M12 5v14M5 12h14" fill="none" stroke="%s" stroke-width="2" stroke-linecap="round"></path>',
     'clock':'<circle cx="12" cy="12" r="8" fill="none" stroke="%s" stroke-width="1.8"></circle><path d="M12 8v4l3 2" fill="none" stroke="%s" stroke-width="1.8" stroke-linecap="round"></path>',
     'eye':'<path d="M2 12s4-7 10-7 10 7 10 7-4 7-10 7S2 12 2 12z" fill="none" stroke="%s" stroke-width="1.8"></path><circle cx="12" cy="12" r="3" fill="none" stroke="%s" stroke-width="1.8"></circle>',
     'alert':'<circle cx="12" cy="12" r="9" fill="none" stroke="%s" stroke-width="1.8"></circle><path d="M12 7v6M12 16.5v.5" fill="none" stroke="%s" stroke-width="2" stroke-linecap="round"></path>',
     'trash':'<path d="M4 7h16M9 7V4h6v3M6 7l1 13h10l1-13" fill="none" stroke="%s" stroke-width="1.8" stroke-linejoin="round"></path>',
     'qr':'<rect x="4" y="4" width="6" height="6" fill="none" stroke="%s" stroke-width="1.8"></rect><rect x="14" y="4" width="6" height="6" fill="none" stroke="%s" stroke-width="1.8"></rect><rect x="4" y="14" width="6" height="6" fill="none" stroke="%s" stroke-width="1.8"></rect><path d="M14 14h2v2h-2zM18 18h2v2h-2zM14 18h2M18 14h2" fill="none" stroke="%s" stroke-width="1.8"></path>',
     'msg':'<path d="M4 5h16v11H9l-5 4z" fill="none" stroke="%s" stroke-width="1.8" stroke-linejoin="round"></path>',
     'user':'<circle cx="12" cy="8" r="4" fill="none" stroke="%s" stroke-width="1.8"></circle><path d="M4 20c1.5-4 4.5-6 8-6s6.5 2 8 6" fill="none" stroke="%s" stroke-width="1.8" stroke-linecap="round"></path>',
     'redo':'<path d="M20 11a8 8 0 10-2.3 5.7M20 4v7h-7" fill="none" stroke="%s" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"></path>',
    }[name]
    return '<svg aria-hidden="true" width="%d" height="%d" viewBox="0 0 24 24">%s</svg>' % (size, size, p.replace('%s', color))

def play(label='Play', size=44, icon='play'):
    return '<button class="play" aria-label="%s" style="width:%dpx;height:%dpx">%s</button>' % (label, size, size, ico(icon, '#fff', 16 if size < 56 else 22))

def btn(label, kind='bk', full=False, sm=False, icon=None, tag='a', extra=''):
    st = 'width:100%;' if full else ''
    cls = 'btn %s%s' % (kind, ' sm' if sm else '')
    ic = ico(icon, '#fff' if kind == 'bk' else '#111', 18) if icon else ''
    if tag == 'button':
        return '<button class="%s" style="%s%s">%s%s</button>' % (cls, st, extra, ic, label)
    return '<a class="%s" href="#" style="%s%s">%s%s</a>' % (cls, st, extra, ic, label)

def img(key, alt, h, pos=None, r=24, w=None):
    p = ';object-position:%s' % pos if pos else ''
    ws = 'width:%s;' % w if w else ''
    return '<div class="ph" style="%sheight:%dpx;border-radius:%dpx;flex-shrink:0"><img src="/_blob/%s" alt="%s" style="%s"></div>' % (ws, h, r, IMG[key], alt, p.lstrip(';'))

def inp(id, label, val='', ph='', hint='', typ='text', h=52):
    v = ' value="%s"' % val if val else ''
    p = ' placeholder="%s"' % ph if ph else ''
    hn = '<span class="mut" style="display:block;margin-top:8px;font-size:13px">%s</span>' % hint if hint else ''
    return '<div><label class="lab" for="%s">%s</label><input class="inp" id="%s" type="%s"%s%s style="height:%dpx">%s</div>' % (id, label, id, typ, v, p, h, hn)

def ta(id, label, val, h=140, counter=None, ph=''):
    c = '<span class="mut tn" style="display:block;margin-top:8px;font-size:13px;text-align:right">%s</span>' % counter if counter else ''
    p = ' placeholder="%s"' % ph if ph else ''
    return '<div><label class="lab" for="%s">%s</label><textarea class="ta" id="%s"%s style="height:%dpx">%s</textarea>%s</div>' % (id, label, id, p, h, val, c)

def chips(items, on=(), label=None):
    l = '<span class="lab">%s</span>' % label if label else ''
    return '<div>%s<div class="chips">%s</div></div>' % (l, ''.join('<button class="chip%s">%s</button>' % (' on' if i in on else '', i) for i in items))

def card(inner, bg='#F2F2F2', pad=24, r=24, gap=12, extra=''):
    return '<div style="border-radius:%dpx;background:%s;padding:%dpx;display:flex;flex-direction:column;gap:%dpx;%s">%s</div>' % (r, bg, pad, gap, extra, inner)

def frame(inner, pad=24, gap=12, extra=''):
    return '<div class="frame" style="padding:%dpx;display:flex;flex-direction:column;gap:%dpx;%s">%s</div>' % (pad, gap, extra, inner)

def col(*items, gap=16, extra=''):
    return '<div style="display:flex;flex-direction:column;gap:%dpx;%s">%s</div>' % (gap, extra, ''.join(items))

def rowx(*items, gap=12, align='center', extra=''):
    return '<div style="display:flex;align-items:%s;gap:%dpx;%s">%s</div>' % (align, gap, extra, ''.join(items))

def t(text, size=16, mut=False, w=400, extra=''):
    c = ' class="mut"' if mut else ''
    return '<p%s style="margin:0;font-size:%dpx;line-height:1.5;font-weight:%d;%s">%s</p>' % (c, size, w, extra, text)

def un(text, size=24, extra='', tag='h2'):
    return '<%s class="un" style="margin:0;font-size:%dpx;font-weight:500;line-height:1.15;letter-spacing:%s;%s">%s</%s>' % (tag, size, '-.02em' if size >= 28 else '0', extra, text, tag)

def small(text, mut=True, extra=''):
    return '<span%s style="font-size:13px;line-height:1.4;%s">%s</span>' % (' class="mut"' if mut else '', extra, text)

def strong(text, size=17):
    return '<strong style="font-size:%dpx;line-height:1.3">%s</strong>' % (size, text)

def nm(name='Anna', white=False):
    return '<span class="%s">%s</span>' % ('nmw' if white else 'nm', name)

def track(label, sub, dur='0:40', size=44, on=False):
    bg = 'background:#FFD84D;border-radius:16px;padding:12px;border:none;' if on else ''
    return '<div class="li" style="%s">%s<div style="flex:1;display:flex;flex-direction:column;gap:2px;min-width:0"><strong style="font-size:16px">%s</strong><span class="mut" style="font-size:14px">%s</span></div><span class="mut tn" style="font-size:14px">%s</span></div>' % (bg, play('Play ' + label, size), label, sub, dur)

def player(cur='0:12', total='0:40', pct=30, label='Play'):
    return ('<div style="display:flex;align-items:center;gap:12px">%s<div style="flex:1;display:flex;flex-direction:column;gap:6px">'
            '<div style="height:4px;border-radius:2px;background:#DADADA;position:relative"><span style="position:absolute;left:0;top:0;height:4px;border-radius:2px;background:#111;width:%d%%"></span></div>'
            '<div class="mut tn" style="display:flex;justify-content:space-between;font-size:13px"><span>%s</span><span>%s</span></div></div></div>') % (play(label, 48), pct, cur, total)

def steps(items, cur):
    # items: list of labels; cur index (0-based) of current; earlier are done
    out = []
    for i, s in enumerate(items):
        if i < cur:
            dot = '<span style="width:24px;height:24px;border-radius:50%%;background:#111;display:flex;align-items:center;justify-content:center;flex-shrink:0">%s</span>' % ico('check', '#fff', 14)
            st = ''
        elif i == cur:
            dot = '<span style="width:24px;height:24px;border-radius:50%;background:#FFD84D;border:2px solid #111;flex-shrink:0"></span>'
            st = 'font-weight:500;'
        else:
            dot = '<span style="width:24px;height:24px;border-radius:50%;border:2px solid #DADADA;flex-shrink:0"></span>'
            st = 'color:#4A4A4A;'
        out.append('<div style="display:flex;align-items:center;gap:12px;font-size:15px;%s">%s<span>%s</span></div>' % (st, dot, s))
    return '<div style="display:flex;flex-direction:column;gap:12px">%s</div>' % ''.join(out)

def check(label, on=False, id='c'):
    return '<label style="display:flex;gap:12px;align-items:flex-start;font-size:15px;line-height:1.45;cursor:pointer"><input type="checkbox" class="chk" id="%s"%s style="margin-top:1px"><span>%s</span></label>' % (id, ' checked' if on else '', label)

def radio(title, sub, on=False, name='r', bg_on='#FFD84D'):
    bg = bg_on if on else '#F2F2F2'
    bd = '#111' if on else '#F2F2F2'
    return '<label style="display:flex;gap:16px;align-items:flex-start;padding:20px;border-radius:20px;cursor:pointer;background:%s;border:2px solid %s"><input type="radio" name="%s" class="chk"%s style="margin-top:2px"><span style="display:flex;flex-direction:column;gap:4px"><strong style="font-size:17px">%s</strong><span style="font-size:14px;line-height:1.45;color:#4A4A4A">%s</span></span></label>' % (bg, bd, name, ' checked' if on else '', title, sub)

def notice(text, kind='info'):
    bg = {'info': '#F2F2F2', 'warn': '#FFD84D', 'ok': '#F2F2F2'}[kind]
    ic = {'info': 'alert', 'warn': 'alert', 'ok': 'check'}[kind]
    return '<div style="display:flex;gap:12px;align-items:flex-start;background:%s;border-radius:16px;padding:16px;font-size:14px;line-height:1.45">%s<span>%s</span></div>' % (bg, ico(ic, '#111', 18), text)

def sendrow(items=('WhatsApp', 'Messages', 'Telegram', 'More', 'QR code')):
    m = {'SMS': 'Messages', 'Share': 'More', 'QR': 'QR code', 'Copy': 'Copy link'}
    items = [m.get(i, i) for i in items]
    return sharegrid(items, cols=min(len(items), 5), h=72)

def linkbox(url='openyoursong.com/anna-7kq2'):
    return '<div style="display:flex;align-items:center;gap:8px;background:#fff;border-radius:12px;padding:6px 6px 6px 16px"><span class="tn" style="flex:1;font-size:16px;font-weight:500;overflow:hidden;text-overflow:ellipsis;white-space:nowrap">%s</span>%s</div>' % (url, btn('Copy', 'bk', sm=True, icon='copy', tag='button'))

def lyric(size=24, pad=8):
    return '<p class="un" style="margin:0;font-size:%dpx;font-weight:500;line-height:1.25;letter-spacing:-.01em"><span style="background:#FFD84D;padding:0 %dpx;border-radius:4px">Anna</span>, you still ride that yellow bike</p>' % (size, pad)

def countdown(size=40):
    def u(n, l):
        return '<div style="display:flex;flex-direction:column;gap:4px"><span class="un tn" style="font-size:%dpx;font-weight:500;line-height:1">%s</span><span style="font-size:13px">%s</span></div>' % (size, n, l)
    return '<div style="display:flex;gap:24px">%s%s%s</div>' % (u('02', 'days'), u('14', 'hours'), u('37', 'min'))

# ---------- shells ----------
WM = '<a href="#" class="un fl" style="font-weight:500;font-size:%dpx;color:#111">openyoursong</a>'

def doc(title, w, h, body):
    return ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<title>%s</title>\n<script src="./support.js"></script>\n</head>\n<body>\n<x-dc>\n%s\n'
            '<div class="cp" style="width:%dpx;height:%dpx;box-sizing:border-box;overflow:hidden;position:relative">\n%s\n</div>\n</x-dc>\n'
            '<script type="text/x-dc" data-dc-script data-props=\'{"$preview":{"width":%d,"height":%d}}\'>\nclass Component extends DCLogic {\n  renderVals() { return {}; }\n}\n</script>\n</body>\n</html>\n') % (title, HELMET, w, h, body, w, h)

def m_head(kind='wizard', step=None, back=True, right=None):
    b = '<button aria-label="Back" style="width:44px;height:44px;border:none;background:none;display:flex;align-items:center;justify-content:flex-start;cursor:pointer;padding:0">%s</button>' % ico('back', '#111', 22) if back else '<span style="width:44px"></span>'
    if kind == 'wizard':
        r = '<span class="mut tn" style="width:44px;text-align:right;font-size:14px">%s</span>' % (('%d/4' % step) if step else '')
        h = '<header style="display:flex;align-items:center;justify-content:space-between;padding:16px 20px 8px">%s%s%s</header>' % (b, WM % 18, r)
        if step:
            segs = ''.join('<span style="flex:1;height:4px;border-radius:2px;background:%s"></span>' % ('#111' if i < step else '#DADADA') for i in range(4))
            h += '<div role="progressbar" aria-label="Step %d of 4" style="display:flex;gap:4px;padding:0 20px 20px">%s</div>' % (step, segs)
        else:
            h += '<div style="height:12px"></div>'
        return h
    if kind == 'site':
        return '<header style="display:flex;align-items:center;justify-content:space-between;padding:16px 20px">%s<button aria-label="Open menu" style="width:44px;height:44px;border-radius:12px;border:1px solid #DADADA;background:#fff;display:flex;align-items:center;justify-content:center;cursor:pointer">%s</button></header>' % (WM % 20, ico('menu', '#111', 20))
    if kind == 'gift':
        return '<header style="display:flex;align-items:center;justify-content:center;height:76px;padding:0 20px">%s</header>' % (WM % 18)
    if kind == 'account':
        tabs = ''.join('<a href="#" class="fl" style="height:44px;padding:0 4px;font-size:15px;font-weight:500;%s">%s</a>' % ('border-bottom:2px solid #111;' if right == x else 'color:#4A4A4A;', x) for x in ('Orders', 'Calendar', 'Plan', 'Settings'))
        return '<header style="display:flex;align-items:center;justify-content:space-between;padding:16px 20px 4px">%s<span style="width:36px;height:36px;border-radius:50%%;background:#F2F2F2;display:flex;align-items:center;justify-content:center">%s</span></header><nav style="display:flex;gap:20px;padding:0 20px;border-bottom:1px solid #DADADA">%s</nav>' % (WM % 18, ico('user', '#111', 18), tabs)
    if kind == 'order':
        return '<header style="display:flex;align-items:center;justify-content:space-between;padding:16px 20px 8px">%s<a href="#" class="fl mut" style="font-size:14px">Account</a></header>' % (WM % 18)
    return ''

def mobile(title, head, main, bar=None, h=844, pad_top=0):
    barh = ''
    if bar:
        barh = '<div style="position:absolute;left:0;right:0;bottom:0;background:#fff;border-top:1px solid #DADADA;padding:16px 20px 24px;display:flex;flex-direction:column;gap:8px">%s</div>' % bar
    body = '%s\n<main style="padding:%dpx 20px 0;display:flex;flex-direction:column;gap:24px">%s</main>\n%s' % (head, pad_top, main, barh)
    return doc(title, 390, h, body)

def d_head(kind='wizard', step=None, right=None):
    if kind == 'wizard':
        mid = ''
        if step:
            segs = ''.join('<span style="width:56px;height:4px;border-radius:2px;background:%s"></span>' % ('#111' if i < step else '#DADADA') for i in range(4))
            mid = '<div style="display:flex;align-items:center;gap:16px"><div role="progressbar" aria-label="Step %d of 4" style="display:flex;gap:4px">%s</div><span class="mut tn" style="font-size:14px">Step %d of 4</span></div>' % (step, segs, step)
        return '<header style="height:80px;display:flex;align-items:center;justify-content:space-between;padding:0 64px;border-bottom:1px solid #DADADA">%s%s<a href="#" class="fl mut" style="font-size:15px">Save and exit</a></header>' % (WM % 20, mid)
    if kind == 'site':
        nav = ''.join('<a href="#" style="text-decoration:none">%s</a>' % x for x in ('How it works', 'Examples', 'Pricing', 'Ideas'))
        return '<header style="height:88px;display:flex;align-items:center;justify-content:space-between;padding:0 64px">%s<nav style="display:flex;gap:32px;font-size:15px;font-weight:500">%s</nav><div style="display:flex;gap:24px;align-items:center"><a href="#" class="mut" style="font-size:15px;text-decoration:none">Log in</a>%s</div></header>' % (WM % 22, nav, btn('Make a song', sm=True))
    if kind == 'gift':
        return '<header style="height:72px;display:flex;align-items:center;justify-content:center">%s</header>' % (WM % 18)
    if kind == 'account':
        tabs = ''.join('<a href="#" class="fl" style="height:80px;font-size:15px;font-weight:500;%s">%s</a>' % ('box-shadow:inset 0 -2px 0 #111;' if right == x else 'color:#4A4A4A;', x) for x in ('Orders', 'Calendar', 'Plan', 'Settings'))
        return '<header style="height:80px;display:flex;align-items:center;justify-content:space-between;padding:0 64px;border-bottom:1px solid #DADADA"><div style="display:flex;align-items:center;gap:48px">%s<nav style="display:flex;gap:32px">%s</nav></div><div style="display:flex;align-items:center;gap:16px"><span class="mut" style="font-size:14px">max.r@mail.com</span>%s</div></header>' % (WM % 20, tabs, btn('New song', sm=True, icon='plus'))
    if kind == 'order':
        return '<header style="height:80px;display:flex;align-items:center;justify-content:space-between;padding:0 64px;border-bottom:1px solid #DADADA">%s<div style="display:flex;align-items:center;gap:24px"><a href="#" class="mut" style="font-size:15px;text-decoration:none">Help</a><a href="#" style="font-size:15px;text-decoration:none;font-weight:500">Account</a></div></header>' % (WM % 20)
    return ''

def desktop(title, head, left, right=None, h=900, split='640px 1fr', pad='64px 64px', gap=96, align='start', bar=None):
    if right is None:
        inner = '<main style="padding:%s">%s</main>' % (pad, left)
    else:
        inner = '<main style="display:grid;grid-template-columns:%s;gap:%dpx;padding:%s;align-items:%s">%s%s</main>' % (split, gap, pad, align, left, right)
    return doc(title, 1440, h, head + '\n' + inner + (bar or ''))

def write(name, html):
    open(os.path.join(PROJ, name), 'w').write(html)
    return name

# ---------- social sharing ----------
SOC = {
 'Instagram': '<rect x="3.5" y="3.5" width="17" height="17" rx="5" fill="none" stroke="#111" stroke-width="1.8"></rect><circle cx="12" cy="12" r="4" fill="none" stroke="#111" stroke-width="1.8"></circle><circle cx="17.2" cy="6.8" r="1.1" fill="#111"></circle>',
 'Stories': '<circle cx="12" cy="12" r="8.5" fill="none" stroke="#111" stroke-width="1.8" stroke-dasharray="4 2.2"></circle><path d="M12 8.5v7M8.5 12h7" fill="none" stroke="#111" stroke-width="1.8" stroke-linecap="round"></path>',
 'TikTok': '<path d="M14 4v10.5a3.5 3.5 0 11-3.5-3.5" fill="none" stroke="#111" stroke-width="1.8" stroke-linecap="round"></path><path d="M14 4c.4 2.6 2.2 4.3 5 4.5" fill="none" stroke="#111" stroke-width="1.8" stroke-linecap="round"></path>',
 'X': '<path d="M5 4.5l14 15M19 4.5L5 19.5" fill="none" stroke="#111" stroke-width="1.9" stroke-linecap="round"></path>',
 'WhatsApp': '<path d="M5 19l1.2-3.6A7.5 7.5 0 1112 19.5a7.4 7.4 0 01-3.4-.8z" fill="none" stroke="#111" stroke-width="1.8" stroke-linejoin="round"></path><path d="M9.5 9.5c.3 1.8 2.2 3.8 4.2 4.3" fill="none" stroke="#111" stroke-width="1.6" stroke-linecap="round"></path>',
 'Telegram': '<path d="M3.5 11.5l16-6.5-2.8 14-5-4-2.4 2.6.3-4.2 7-6.4-8.8 5.2z" fill="none" stroke="#111" stroke-width="1.7" stroke-linejoin="round"></path>',
 'Messages': '<path d="M4 6h16v10H10l-4 3.5V16H4z" fill="none" stroke="#111" stroke-width="1.8" stroke-linejoin="round"></path>',
 'Facebook': '<path d="M14.5 20v-7h2.6l.4-3h-3V8.2c0-.9.3-1.5 1.6-1.5h1.5V4.1A20 20 0 0015.4 4C13.2 4 11.6 5.3 11.6 7.8V10H9v3h2.6v7" fill="none" stroke="#111" stroke-width="1.7" stroke-linejoin="round"></path>',
 'Save video': '<path d="M12 4v11M7 10l5 5 5-5M5 20h14" fill="none" stroke="#111" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"></path>',
 'Copy link': '<path d="M10 14a4 4 0 005.7 0l3-3a4 4 0 00-5.7-5.7l-1 1M14 10a4 4 0 00-5.7 0l-3 3a4 4 0 005.7 5.7l1-1" fill="none" stroke="#111" stroke-width="1.8" stroke-linecap="round"></path>',
 'More': '<circle cx="6" cy="12" r="1.6" fill="#111"></circle><circle cx="12" cy="12" r="1.6" fill="#111"></circle><circle cx="18" cy="12" r="1.6" fill="#111"></circle>',
 'QR code': '<rect x="4" y="4" width="6" height="6" fill="none" stroke="#111" stroke-width="1.8"></rect><rect x="14" y="4" width="6" height="6" fill="none" stroke="#111" stroke-width="1.8"></rect><rect x="4" y="14" width="6" height="6" fill="none" stroke="#111" stroke-width="1.8"></rect><path d="M14 14h2v2h-2zM18 18h2v2h-2zM14 18h2M18 14h2" fill="none" stroke="#111" stroke-width="1.8"></path>',
 'Email': '<rect x="3" y="5" width="18" height="14" rx="2" fill="none" stroke="#111" stroke-width="1.8"></rect><path d="M4 7l8 6 8-6" fill="none" stroke="#111" stroke-width="1.8" stroke-linejoin="round"></path>',
}

def soc(name, size=22):
    return '<svg aria-hidden="true" width="%d" height="%d" viewBox="0 0 24 24">%s</svg>' % (size, size, SOC[name])

def sharegrid(items, cols=4, bg='#fff', h=80):
    cells = ''.join('<button style="height:%dpx;border-radius:16px;border:none;background:%s;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:8px;cursor:pointer;font:500 13px Inter,system-ui,sans-serif;color:#111">%s<span>%s</span></button>' % (h, bg, soc(i), i) for i in items)
    return '<div style="display:grid;grid-template-columns:repeat(%d,1fr);gap:8px">%s</div>' % (cols, cells)

def tagcard(text='Tag @openyoursong so we can find it. We repost our favourites, with your OK', bg='#111'):
    return '<div style="display:flex;gap:12px;align-items:center;background:%s;color:#fff;border-radius:16px;padding:14px 16px"><span class="un" style="font-size:15px;font-weight:500;background:#FFD84D;color:#111;border-radius:8px;padding:6px 10px;white-space:nowrap">@openyoursong</span><span style="font-size:14px;line-height:1.4">%s</span></div>' % (bg, text)

def caption(text):
    return '<div style="display:flex;align-items:center;gap:8px;background:#fff;border:1px solid #DADADA;border-radius:12px;padding:6px 6px 6px 14px"><span style="flex:1;font-size:14px;line-height:1.4">%s</span>%s</div>' % (text, btn('Copy', 'bo', sm=True, tag='button', extra='height:36px;padding:0 12px'))

def phone_only(text='Instagram and TikTok posting works from your phone'):
    return '<div style="display:flex;gap:16px;align-items:center;background:#F2F2F2;border-radius:16px;padding:16px"><div style="width:96px;height:96px;flex-shrink:0;background:#fff;border-radius:12px;display:flex;align-items:center;justify-content:center">%s</div><div style="display:flex;flex-direction:column;gap:4px"><strong style="font-size:15px">Post it from your phone</strong><span class="mut" style="font-size:14px;line-height:1.4">%s. Scan to open this page there</span></div></div>' % (soc('QR code', 64), text)

# ---------- quiet share block (one lead action) ----------
def tagline():
    return '<p class="mut" style="margin:0;font-size:14px;line-height:1.45">Tag <span class="nm" style="color:#111;font-weight:500">@openyoursong</span> so we can find it</p>'

def iconbtn(name):
    return '<button aria-label="%s" style="width:48px;height:48px;border-radius:12px;border:1px solid #DADADA;background:#fff;display:flex;align-items:center;justify-content:center;cursor:pointer">%s</button>' % (name, soc(name, 20))

def share_m(rest=('TikTok', 'X', 'Save video'), cap=None, lead='Share to Stories'):
    leadb = '<button class="btn bk" style="width:100%%;gap:10px">%s%s</button>' % (soc('Stories', 20).replace('#111', '#fff'), lead)
    more = '<div style="display:flex;align-items:center;gap:8px"><span class="mut" style="font-size:14px;flex:1">Or</span>%s</div>' % ''.join(iconbtn(r) for r in rest)
    return col(leadb, more, caption(cap) if cap else '', tagline(), gap=10)

def share_d(cap=None, rest=('X', 'Facebook', 'Copy link')):
    leadb = '<button class="btn bk" style="gap:10px">%s%s</button>' % (soc('Save video', 20).replace('#111', '#fff'), 'Save the video')
    row = '<div style="display:flex;align-items:center;gap:8px">%s%s</div>' % (leadb, ''.join(iconbtn(r) for r in rest))
    qr = '<div style="display:flex;gap:12px;align-items:center">%s<span class="mut" style="font-size:14px;line-height:1.4">Stories and TikTok post from your phone. Scan to open this page there</span></div>' % ('<div style="width:56px;height:56px;flex-shrink:0;border:1px solid #DADADA;border-radius:12px;display:flex;align-items:center;justify-content:center">%s</div>' % soc('QR code', 36))
    return col(row, caption(cap) if cap else '', qr, tagline(), gap=12)
