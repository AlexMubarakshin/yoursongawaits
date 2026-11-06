# seo/scripts

Скрипты анализа Ahrefs, перенесены из эфемерного scratchpad сессии 2026-11-05 (аудит D30/E17). Не перезапускались после переноса.

- Сырые данные — `../raw/`: `us.tsv` и `global.tsv` — UTF-8-версии выгрузок Ahrefs «Matching terms» (`google_us_…matching-terms_2026-11-05…csv`, `google_global_…matching-terms_2026-11-05…csv`, исходники UTF-16 лежат там же); `*search-volume-history_2026-11-05*.csv` — история объёмов (US и Global).
- US: `python3 -I us_analysis.py` → читает `../raw/us.tsv`, пишет `us_report.md`, `us_clusters.csv`, `us_keywords_classified.csv` рядом со скриптом (в `seo/` лежат копии результата).
- Global: `classify.py` (правила классификации) → `python3 -I analyze.py` (читает `../raw/global.tsv`, пишет `agg.json`, `rows.pkl`, `global_countries.csv` рядом со скриптом) → `python3 -I report.py` (пишет `report_body.md`, тело `../global_report.md`).
- Top pages: `toppages/` — `load.py` читает `toppages/csv/*.csv` (UTF-8-копии выгрузок из `../top-pages/`); остальные скрипты запускаются с путём к папке аргументом, например `python3 -I toppages/analyze.py toppages` → `toppages/results.json`; `gen_md.py` собирает части `../top-pages-report.md`.
- Черновой расчёт COGS перенесён в `../../models/cogs.py` (справочный, до решений 05; канонический расчёт — `models/unit_economics.py`).
