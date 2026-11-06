# План ресерча: AI-песни-подарки

Цель — три артефакта: ресерч конкурентов, ресерч экономики, PRD. Рынок: EN первым, с мультиязычным ядром; Россия — whitelabel на том же ядре, входит в MVP ([05-decisions.md](05-decisions.md) D7).

| # | Этап | Результат | Статус |
|---|---|---|---|
| 1 | Карта рынка и разбор ohappy.ru | [01-landscape.md](01-landscape.md) | ✅ |
| 2 | Спрос и SEO (Ahrefs) | [02-seo-demand.md](02-seo-demand.md), детали в [seo/](seo/) | ✅ EN; местные языки — вопрос Q3 |
| 3 | Конкуренты вглубь | [03-competitors.md](03-competitors.md), детали в [appendix/competitors-teardown.md](appendix/competitors-teardown.md) и [seo/top-pages-report.md](seo/top-pages-report.md) | ✅ |
| 4 | Экономика | [04-economics.md](04-economics.md), модель [models/unit_economics.py](models/unit_economics.py), детали в [appendix/](appendix/) | ✅ |
| 4b | Каналы: Telegram-бот и доставка поздравлений | [appendix/telegram-bot.md](appendix/telegram-bot.md), [appendix/delivery-channels.md](appendix/delivery-channels.md) → решения D14, D15 | ✅ |
| 5 | Решения и гипотеза (go, стратегия, открытые вопросы) | [05-decisions.md](05-decisions.md) | ✅ |
| 6 | PRD | [06-prd.md](06-prd.md) | 🟡 черновик v0.4, ждёт утверждения (Q15) |

## Правила ведения документов

1. **Цифры** живут в [facts.md](facts.md). Остальные документы ссылаются на них или повторяют их без изменений.
2. **Термины** — в [glossary.md](glossary.md): в основных документах и PRD используем только их.
3. **Решения** живут в [05-decisions.md](05-decisions.md). Если сводка или приложение противоречит решению, верно решение.
4. **Открытые вопросы** ведутся одним списком в [05-decisions.md §6](05-decisions.md). В других документах отдельных списков нет.
5. **Приложения** (`appendix/`, `seo/*report.md`) — подробные отчёты сабагентов с источниками. У каждого вверху стоит баннер о приоритете facts и 05.
6. **Сырые данные и скрипты** лежат в репозитории: [seo/raw/](seo/raw/), [seo/scripts/](seo/scripts/), [models/](models/).

## Как делать новые выгрузки Ahrefs

- **Keywords Explorer → Matching terms**, по seed-ключам, база нужной страны. Экспорт всех колонок (Volume, KD, CPC, Traffic potential, Parent keyword, SV trend).
- **Site Explorer → Top pages / Organic keywords** по домену.
- Местные seed-ключи для DE, PL, ES/MX, BR/PT, FR, IT, TR, ID, RU — в [seo/global_report.md](seo/global_report.md).
- Черновик EN-seed (не использовался) — [appendix/keywords-ahrefs.txt](appendix/keywords-ahrefs.txt).
