# OpenYourSong design canvas (Cut Paper)

Snapshot of the design canvas: https://claude.ai/artifact/PJsrpVDQ8xjsg7SSAkhj1a

## What's here

- `project/`: the canvas source, a copy of what the artifact serves.
  - `canvas.json` is the board layout.
  - Each `*.dc.html` file is one artboard.
  - Image `src` values point to `/_blob/<id>`, which only resolves inside the artifact. `blobmap.json` maps each blob id to a file in `img/`.
- `img/`: the photos the boards use.
- `gen/`: the Python generator for the product screens.
  - `kit.py` holds the shared components.
  - The `s_*.py` files hold the flows.
  - Paths inside point to the session scratchpad, so update `PROJ` in `kit.py` before you run them.
  - `s_v72.py` and `s_v73.py` are standalone patch scripts: they edit the boards in `project/` in place and run once, on the snapshot of the version before.

## Page "Actual flows", top to bottom

0. Overview: landing (desktop 1440, mobile 390 split into two boards because of the 8000 px canvas limit), brand language, UI kit, growth loop and SEO notes.
1. Create and pay: entry pages, questionnaire, generation, preview and payment.
2. Order and delivery.
3. Recipient and sharing: opening the gift, the reaction video and posting it.
4. Group gift.
5. Account and emails.
6. Content and SEO: ideas hub, comparisons, guides and free tools.

In every flow the mobile screen sits directly above its desktop version. Board names start with page.flow.step.

The "[RESEARCH] Flows" page holds the original Cut Paper exploration.

## File prefixes

| Prefix | What it is |
|---|---|
| `p-a` | Brand and UI kit |
| `p-b` | Questionnaire |
| `p-c` | Generation, payment and order |
| `p-d` | Recipient |
| `p-e` | Group, account and emails |
| `p-f` | Entry pages |
| `p-g` | Growth loop |
| `p-h` | Content |

A `-d` suffix marks the desktop version.

## Button rule

One primary per screen: butter with a 2 px ink edge (`.bk`). On a butter surface the primary is ink (`.bi`). Secondary is white with an ink edge (`.bo`).
