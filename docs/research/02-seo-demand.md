# 02. Спрос и SEO (Ahrefs)

Дата: 2026-11-05. Цифры совпадают с [facts.md §1, §3](facts.md).

**Источники:**
- выгрузки Ahrefs: Matching terms (US и Global) и история объёмов по 5 ключам, сырые данные в [seo/raw/](seo/raw/);
- Site Explorer, Top pages по 8 доменам.

**Подробные отчёты:** [seo/us_report.md](seo/us_report.md), [seo/global_report.md](seo/global_report.md), [seo/top-pages-report.md](seo/top-pages-report.md). Классификация ключей — [seo/us_keywords_classified.csv](seo/us_keywords_classified.csv), страны — [seo/global_countries.csv](seo/global_countries.csv), скрипты — [seo/scripts/](seo/scripts/).

## 1. Главное

1. **Подарочного поискового спроса мало:** в US 14.7k в месяц (без аномального ключа), из них ~10k с явными формулировками custom/personalized/AI. Поиск — дополнительный канал, основной трафик придётся создавать виральностью и соцсетями ([05-decisions.md](05-decisions.md) D11).
2. **Категория растёт, лидер теряет спрос.** Подарочный спрос +23% год к году (LFL), GIFT_CORE +98%. Брендовый спрос Songfinch −17…−30%, органика его сайта −14%.
3. **Деньги в EN high-CPC странах** (US, GB, CA, AU, NZ, IE): 25% подарочного объёма и ~88% его ценности. У Индии самый большой объём, но CPC $0.04.
4. **Контекстная реклама по head-запросам не окупается:** CPC $3–6, CAC ~$104. Окупается только длинный хвост (CAC ~$30). По плану 05 платного поиска нет.
5. **`ai song generator`** (52k US, KD 78) — спрос на инструмент, а не на подарок. Используем максимум как вход в воронку через узкие бесплатные генераторы.

## 2. Кластеры, US (в месяц, KE)

| Кластер | Объём | KD (медиана) | CPC | Комментарий |
|---|---:|---:|---:|---|
| GIFT_CORE (custom/personalized song gift) | 5.9k, **4.2k без аномального ключа** | 52 | $3.03 | В выдаче лидирует Songfinch |
| BIRTHDAY_NAME (song with name) | 2.9k | 1 | $0.42 | Конкуренции нет, спрос ровный |
| Anniversary | 3.6k | ~0 | низкий | В основном ищут готовую песню послушать |
| Mother's Day / Father's Day | 1.7k / 1.25k | ~0 | <$0.10 | Пики в 9–10 раз выше среднего месяца |
| Wedding | 170 | | | |
| Valentine's, Christmas, memorial | ~30 каждый | | | Мало запросов, но это дни покупки подарков |
| AI_GENERATOR | 73k | 73 | $0.79 | Не подарочное намерение |
| Бренды | Songfinch 3.1–3.6k (head) / ~4.6k (все), Songlorious ~1.7k (+20%), Suno 1.9k, Udio 330 (+91%) | | | По GiftSong, CustomSong, MakeCustomSongs, Birthdai, Wondera строк нет |

**Аномалия.** У «how to create a personalized song gift» (1.7k KE / 1.9k SE) объём был нулевым до 02.2026, затем пики 10.5k в мае и 6k в сентябре. Похоже на запросы ботов или AI-ассистентов. Из всех расчётов исключён.

## 3. Динамика по ключам с историей (SVH, последние 12 мес. против предыдущих 12)

| Ключ | US | Global |
|---|---:|---:|
| ai song generator | −21% | −16% |
| songfinch | −30% | −30% |
| songlorious | +38% | — |
| happy birthday song with name | +19% | −12% |
| birthday song with name | — | −20% |
| custom song gift | +53% | — |
| anniversary song | — | −6% |

Рост подарочного спроса в целом: **+23% LFL** (KE SV-trend, только ключи, которые были в базе оба года). Цифра +56% (в global-отчёте +45%) — raw, она завышена появлением новых ключей в базе Ahrefs.

## 4. Сезонность

- **Май–июнь** — главный пик (Mother's Day, Father's Day). UK Mother's Day — в марте, AU Father's Day — в сентябре.
- **Декабрь–февраль** — второй пик (Christmas, Valentine's, годовщины).
- Пик к минимуму 2.9×.
- Ближайшие окна для нас: Valentine's 14.02.2027, UK Mother's Day в марте, US Mother's Day в мае ([05-decisions.md §5](05-decisions.md)).

## 5. Рынки

| Тир | Подарочный объём | Оценка |
|---|---:|---|
| US | 14.7k (KE, без аномального ключа) | №1, 76% ценности |
| GB / CA / AU | 2.5k / 1.5k / 1.2k | Те же EN-страницы. Для GB/AU нужно написание personalised |
| IN / PH / PK / ZA | 48.6k / 2.4k / … | Платёжеспособности почти нет |
| EU, LatAm, JP/KR, TR | — | По этим выгрузкам **оценить нельзя**: seed-ключи были английские (неанглийских подарочных запросов 1.2%). Проверяем местными seed (Q3) |
| RU | ~16k запросов «создать песню нейросеть» (+90%) | Подарочные RU-запросы не выгружались. RU-whitelabel в MVP, проверка спроса — Q11 |

## 6. Органика конкурентов (SE)

- **Вся небрендовая коммерческая органика EN-ниши ~0.6–1.5k визитов в месяц.** Ниша почти пустая, но маленькая.
- Songfinch: 5.5k визитов, 81% из них бренд. Растут коммерческие лендинги: get.songfinch custom song gift ×6, /how-it-works, /song-builder.
- GiftSong: рабочая структура /relation/, /occasions/, /gifts/, /pricing, /vs/.
- Songlorious: узкий лендинг /landing-pages/anniversary на 1-м месте.
- Wondera: массовая программатика на 11 языках, ~3 визита на URL, 274 потерянные страницы. Это модель, которую **не копируем**.
- AI-ассистенты цитируют страницы с фактами: цена, сроки, how-it-works, сравнения, FAQ.

## 7. SEO-плейбук для запуска

Подробно — [seo/top-pages-report.md](seo/top-pages-report.md), раздел плейбука.

1. **Коммерческое ядро:** /pricing, /how-it-works, /create. Явные цены и сроки — это же нужно для цитирования AI-ассистентами.
2. **Матрица повод × получатель.** Варианты personalized (US/CA) и personalised (GB/AU).
3. **Кластер «song with name»** (2.4k, KD 0–12) с настоящим аудиопримером.
4. **Сравнения и цены:** songfinch cost / reviews / alternative, best custom song service (KD 1, CPC $6).
5. **Публичные страницы вручения:** только с согласия (opt-in), по умолчанию noindex.
6. **Узкие бесплатные инструменты:** love song, birthday song.
7. **Не делаем:** NSFW, аудио-утилиты, массовые машинные переводы, блоги со «синонимами happy birthday», профили артистов.

Список из 30 low-KD ключей для первых страниц — в [seo/us_report.md](seo/us_report.md). Выгрузки по местным языкам и по именам — вопросы Q3 и Q7 в [05-decisions.md](05-decisions.md).
