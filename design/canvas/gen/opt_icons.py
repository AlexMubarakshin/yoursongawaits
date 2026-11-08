# Quiet option icons for the questionnaire (18px, 1.6 stroke, muted). Helpers, never the first thing you see
OPT = {
 'Pop': '<path d="M12 3a3 3 0 00-3 3v6a3 3 0 006 0V6a3 3 0 00-3-3z"/><path d="M19 10v2a7 7 0 01-14 0v-2M12 19v3"/>',
 'Acoustic': '<path d="M9 18V5l12-2v13"/><circle cx="6" cy="18" r="3"/><circle cx="18" cy="16" r="3"/>',
 'Ballad': '<path d="M12 3a6 6 0 009 9 9 9 0 11-9-9z"/>',
 'Country': '<path d="M3 15c2 2 16 2 18 0M6 14l1.5-7c.3-1.3 2-1.5 3-.7L12 7l1.5-.7c1-.8 2.7-.6 3 .7L18 14"/>',
 'R&amp;B': '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="2.5"/>',
 'Rock': '<path d="M13 2L4 14h7l-1 8 9-12h-7z"/>',
 'Hip-hop': '<path d="M3 18v-6a9 9 0 0118 0v6"/><path d="M21 19a2 2 0 01-2 2h-1v-6h3zM3 19a2 2 0 002 2h1v-6H3z"/>',
 'Jazz': '<path d="M4 10h9l7-5v14l-7-5H4z"/><path d="M7 14v5"/>',
 'Kids': '<path d="M12 15c-3.3 0-6-2.8-6-6.2S8.7 3 12 3s6 2.4 6 5.8-2.7 6.2-6 6.2zM11 15h2l-1 2zM12 17c0 2-2 2-2 4"/>',
 'Upbeat': '<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/>',
 'Warm': '<path d="M4 9h13v5a5 5 0 01-5 5H9a5 5 0 01-5-5zM17 10h1.5a2.5 2.5 0 010 5H17M8 3v3M12 3v3"/>',
 'Funny': '<circle cx="12" cy="12" r="9"/><path d="M8 14s1.5 2 4 2 4-2 4-2M9 9h.01M15 9h.01"/>',
 'Tender': '<path d="M12 20l-7-7a4.5 4.5 0 016.4-6.4l.6.6.6-.6A4.5 4.5 0 0119 13z"/>',
 'Female voice': '<circle cx="12" cy="9" r="5"/><path d="M12 14v7M9 18h6"/>',
 'Male voice': '<circle cx="10" cy="14" r="5"/><path d="M14 10l6-6M15 4h5v5"/>',
}
OPT['Female'] = OPT['Female voice']; OPT['Male'] = OPT['Male voice']
def opt_ico(name, c='#4A4A4A'):
    return '<svg aria-hidden="true" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="%s" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink:0">%s</svg>' % (c, OPT[name])
