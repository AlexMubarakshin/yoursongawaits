import re, pathlib
P = pathlib.Path("artifact-files/b4a8099c-b52e-41d0-ad8e-182f529e1959/project")
files = list(P.glob("p-*.dc.html")) + [P/"03-cut-paper-landing.dc.html", P/"03-cut-paper-landing-mobile.dc.html"]
BTN = re.compile(r'<(a|button) class="btn bk([^"]*)"([\s\S]*?)</\1>')
def fixicons(m): return m.group(0).replace('#fff', '#111')
# second actions on a screen become outline buttons (label-based, applied per file)
DEMOTE = {
 'p-b-05-lyrics-ready': ['Save lines'], 'p-b-05-lyrics-ready-d': ['Save lines'],
 'p-c-06-delivery': ['Pick a date'],
 'p-d-09-no-camera': ['Copy'], 'p-e-00-group-setup': ['Copy'], 'p-e-00-group-setup-d': ['Copy'],
 'p-e-01-organizer': ['Copy'], 'p-e-01-organizer-d': ['Copy'], 'p-e-mail-06-time-to-send': ['Copy'],
 'p-h-01-ideas-hub': ['Read the guide'], 'p-h-01-ideas-hub-d': ['Read the guide'],
 'p-h-04-songs-for-sister-d': ['Make her song'], 'p-h-04-songs-for-sister': ['Make her song'],
 'p-h-05-birthday-song-name': ['Hear how it sounds'], 'p-h-05-birthday-song-name-d': ['Hear how it sounds'],
 'p-h-06-love-song-tool': ['Write my love song'], 'p-h-06-love-song-tool-d': ['Write my love song'],
}
n = 0
for f in files:
    s = f.read_text(); o = s
    s = s.replace('.bk{background:#111;color:#fff}', '.bk{background:#FFD84D;color:#111;border:2px solid #111}')
    s = s.replace('.bk:hover{background:#333;color:#fff}', '.bk:hover{background:#FFE27A;color:#111}')
    if '.bk:hover' not in s: s = s.replace('.bk{background:#FFD84D;color:#111;border:2px solid #111}', '.bk{background:#FFD84D;color:#111;border:2px solid #111}\n.bk:hover{background:#FFE27A;color:#111}')
    s = BTN.sub(fixicons, s)
    key = f.name.replace('.dc.html', '')
    for lab in DEMOTE.get(key, []):
        s = re.sub(r'class="btn bk( sm)?"([^>]*>(?:<svg[\s\S]*?</svg>)?%s<)' % re.escape(lab), r'class="btn bo\1"\2', s)
    # account header "New song" is navigation, the screen keeps its own primary
    s = re.sub(r'class="btn bk sm"([^>]*>(?:<svg[\s\S]*?</svg>)?New song<)', r'class="btn bo sm"\1', s)
    if s != o: f.write_text(s); n += 1
print(n)
