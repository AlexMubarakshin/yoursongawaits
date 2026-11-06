# Ahrefs Top pages: анализ конкурентов (персональная песня в подарок)

> **Детальный отчёт (приложение).** Канонические цифры и решения — в `docs/research/facts.md` и `docs/research/05-decisions.md`; при расхождении верны они. Последняя сверка: 2026-11-05.

Дата выгрузок: 2026-11-05. Источник: `docs/research/seo/top-pages/*.csv` (Ahrefs Site Explorer → Top pages, subdomains: all, режим сравнения previous/current). Скрипты и конвертированные файлы лежат в `docs/research/seo/scripts/toppages/`: `load.py`, `analyze.py`, `gen_md.py`, `results.json` (+ вспомогательные скрипты; UTF-8-копии CSV — в `toppages/csv/`; перенесены из эфемерного scratchpad сессии, см. `seo/scripts/README.md`).

## 0. Оговорки по методике

- **Трафик и traffic value здесь оценки Ahrefs, а не реальные данные.** Ahrefs берёт позиции × объём × CTR-модель и суммирует по всем странам. Погрешность на малых сайтах доходит до нескольких раз. Сравнивать стоит порядки величин и тренды, не точные цифры.
- **Выгрузки неполные.** В них только страницы, которые Ahrefs видит в органике (плюс New/Lost за период). Страницы без ключей в выгрузку не попали, поэтому реальная архитектура сайтов больше. Например, у pesinka.ru в выгрузке нет главной.
- **Классификация по интенту сделана правилами** по URL и *top keyword* страницы. Top keyword — только один из ключей страницы: главная Songfinch собирает 119 ключей, а в бакет «бренд» уходит целиком. Поэтому доля бренда немного завышена, а коммерческие небрендовые запросы на главных занижены.
- **Страна top keyword используется как прокси географии трафика.** Это не точная разбивка трафика по странам.
- Traffic value в выгрузке указан в долларах: у Songfinch $10.1k на 4.0k визитов главной, ≈ $2.5 за визит.
- Бакеты:
  - **brand**: top keyword содержит бренд, включая опечатки вроде songfitch или songglorious;
  - **gift**: custom/personalized song, страницы /occasions/ /relation/ /gifts/ /pricing /create /landing-pages /products, LP-поддомены, RU /podarok/ /povod/ /komu/;
  - **tool_song**: AI song / music / lyrics generator, а также страницы по брендам конкурентов-генераторов (suno, «alternatives»);
  - **tool_audio**: аудио-утилиты (vocal remover, конвертеры, autotune, AI covers, remix/mashup, voice changer);
  - **info**: списки песен, поздравления, цитаты, блог;
  - **ugc_nav**: профили артистов, публичные страницы песен, support, login;
  - **offtopic**: video/image/NSFW/deepfake/celebrity voice.

---

## 1. Сводка по доменам

| Домен | Стр. (с трафиком) | Трафик prev → cur | Δ | Value prev → cur, $ | Δ value | Главная, % трафика | Бренд, % трафика / % value | Gift-коммерция: трафик / $ | Гео (top kw), EN-4 / RU |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| songfinch.com | 371 (132) | 6 423 → 5 516 | −14% | 14 263 → 11 873 | −17% | 72% | 81% / 94% | 242 / $606 | US 98% |
| giftsong.ai | 77 (55) | 2 010 → 1 846 | −8% | 2 561 → 2 132 | −17% | 49% | 0% / 0% | 1 225 / $1 976 (без главной 312 / $472) | US 77%, PH 12%, GB 9% |
| songlorious.com | 26 (19) | 595 → 1 337 | +125% | 1 438 → 3 049 | +112% | 88% | 96% / 97% | 34 / $81 | US 99% |
| sendfame.com | 107 (70) | 6 788 → 3 932 | −42% | 4 099 → 2 683 | −35% | 24% | 27% / 78% | 10 / $2 | US 52%, HU 25%, PK 7% |
| wondera.ai | 1 423 (526) | 4 927 → 4 026 | −18% | 549 → 705 | +28% | 2% | 3% / 6% | 0 | US 34%, IT 10%, ES 9%, RU 8% |
| musicmake.ai | 238 (122) | 3 441 → 3 552 | +3% | 245 → 373 | +52% | 7% | 0% / 0% | 0 | IL 34%, AE 15%, US 6% |
| pesinka.ru | 9 (8) | 225 → 148 | −34% | 0 → 0 | — | нет в выгрузке | 0% | 146 / $0 | RU 100% |
| everyonesing.ru | 1 (1) | 20 → 16 | −20% | 0 → 0 | — | 100% | 0% | 16 / $0 | RU 100% |

Вывод по сводке. Ниша маленькая, органики у всех мало: суммарно ≈ 20k визитов/мес на шесть англоязычных доменов. Коммерческого небрендового gift-трафика из этого ≈ 1.5k (7.5%), а без спорной главной giftsong ≈ 0.6k (3%). Деньги в органике (traffic value) почти целиком брендовые: у Songfinch 94% value приходится на бренд. Wondera и MusicMake по трафику крупные, но это генераторы и аудио-утилиты с value $0.1–0.2 за визит, к подаркам они отношения не имеют.

---

## 2. songfinch.com: лидер категории, держится на бренде

### 2.1 Итоги
**Итоги:** страниц в выгрузке 371 (с текущим трафиком 132); статусы: Unchanged 204, New 89, Lost 78

| Метрика | Previous | Current | Δ |
|---|---:|---:|---:|
| Органический трафик, визитов/мес | 6 423 | 5 516 | -14% |
| Traffic value, $ | 14 263 | 11 873 | -17% |
| Главная: трафик (доля) | | 3 997 (72%) | |
| Бренд (top keyword = бренд): трафик / value | 5 330 / $13 849 | 4 460 (81%) / $11 158 (94%) | -16% |
| Небрендовый трафик / value | 1 093 / $414 | 1 056 / $715 | -3% |

### 2.2 Трафик по интентам
| Бакет | Стр. | Трафик prev → cur | Δ | Value prev → cur, $ | Доля трафика | $/визит |
|---|---:|---:|---:|---:|---:|---:|
| Бренд | 79 | 5 330 → 4 460 | -16% | 13 849 → 11 158 | 81% | 2.50 |
| Инфо-контент (списки песен, поздравления, цитаты, блог) | 33 | 575 → 515 | -10% | 49 → 63 | 9% | 0.12 |
| UGC/навигация (артисты, страницы песен, support, login) | 250 | 394 → 299 | -24% | 25 → 46 | 5% | 0.15 |
| Gift-коммерция | 8 | 124 → 242 | +95% | 340 → 606 | 4% | 2.50 |
| Прочее | 1 | 0 → 0 | — | 0 → 0 | 0% | 0.00 |

Gift-коммерция здесь: `/how-it-works` (custom songs, 155 визитов), `get.songfinch.com/custom-songs-from-real-artists/` (custom song gift, GB, 70), а также `/products/song-streaming`, `/products/song-remix` и sheet music. Ещё часть коммерческих страниц попала в «бренд», потому что их top keyword брендовый: `/store` (songfinch cost), `/products/personalized-song` (how much does songfinch cost; в прошлом периоде top keyword был write a song for me, 600/мес, поз. 2), `/song-builder`, `/reviews`.

### 2.3 Архитектура и SEO-плейбук
| URL-паттерн | Стр. | Стр. с трафиком | Трафик prev → cur | Value cur, $ |
|---|---:|---:|---:|---:|
| `/` | 3 | 2 | 4 696 → 3 997 | 10 080 |
| `/playlists/*` | 35 | 21 | 575 → 515 | 64 |
| `/artists/*` | 243 | 86 | 388 → 263 | 22 |
| `/how-it-works` | 1 | 1 | 111 → 155 | 420 |
| `/playlists` | 1 | 1 | 132 → 135 | 291 |
| `/store` | 1 | 1 | 97 → 71 | 91 |
| `get./custom-songs-from-real-artists` | 2 | 1 | 12 → 70 | 183 |
| `/artists` | 1 | 1 | 78 → 56 | 179 |
| `/products/*` | 12 | 4 | 21 → 53 | 78 |
| `/song-builder` | 1 | 1 | 1 → 49 | 146 |
| `/reviews` | 1 | 1 | 45 → 45 | 121 |
| `/apply` | 1 | 1 | 68 → 43 | 132 |
| `/stories/*` | 24 | 4 | 5 → 37 | 27 |
| `support./hc/*` | 15 | 3 | 21 → 13 | 14 |
| `/lp` | 1 | 1 | 73 → 6 | 7 |

- **`/artists/{name}`, 243 URL.** Профили исполнителей маркетплейса. Дают 263 визита (≈1 визит на страницу), запросы — имена артистов. Это побочный эффект модели с живыми музыкантами, для нашего AI-продукта неприменимо.
- **`/playlists/songs-for-{relation}`, 35 URL, 515 визитов.** Единственный небрендовый контентный кластер: sister, siblings, son, grandma, grandpa, wife, husband, daughter, boyfriend, expecting parents, graduation, retirement, vow renewal, apology, co-worker appreciation. Позиции слабые (8–12) при объёмах 250–1 300 (sister songs 1.1k, daughter songs 1.3k, songs about having a baby 900). Кластер по связке «отношения + песни» есть, но не дожат.
- **`/stories/{uuid}`, 24 URL.** Публичные страницы песен клиентов. Новые начали ранжироваться (custom rock, 150/мес, поз. 2, 34 визита). Это аналог нашей «gift page»: публичная страница подарка индексируется и собирает long-tail.
- **`/u/{user}`, 10 URL.** Пользовательские профили, трафика нет.
- **Поддомены.** `get.songfinch.com` — платные LP, в том числе с utm, которые утекли в индекс. `support.songfinch.com` — help center, его статьи о цене и сроках цитируют AI-ассистенты. `pages.`, `wow.` — служебные.
- **Нет** /occasions/, /vs/, /alternatives/, языковых папок и блога. Songfinch не занимается программатическим SEO, он живёт на бренде, ссылках (1 258 RD на главную) и платном трафике.

### 2.4 Топ-15 по трафику
| # | URL | Бакет | Трафик | Value, $ | Top keyword | Поз. | Объём | Страна |
|---:|---|---|---:|---:|---|---:|---:|---|
| 1 | `/` | brand | 3 996 | 10 079 | songfinch | 1 | 3 100 | US |
| 2 | `/how-it-works` | gift | 155 | 420 | custom songs | 2 | 450 | US |
| 3 | `/playlists` | brand | 135 | 291 | songfinch | 1 | 3 100 | US |
| 4 | `/playlists/songs-for-sister` | info | 119 | 7 | sister songs | 8 | 1 100 | US |
| 5 | `/playlists/songs-for-siblings` | info | 105 | 5 | songs about siblings | 9 | 400 | US |
| 6 | `/store` | brand | 71 | 91 | songfinch cost | 2 | 90 | US |
| 7 | `get.songfinch.com/custom-songs-from-real-artists/` | gift | 70 | 183 | custom song gift | 2 | 150 | GB |
| 8 | `/artists` | brand | 56 | 179 | songfinch | 1 | 3 100 | US |
| 9 | `/song-builder` | brand | 49 | 146 | songfinch | 1 | 3 100 | US |
| 10 | `/playlists/songs-for-expecting-parents` | info | 48 | 11 | songs about having a baby | 8 | 900 | US |
| 11 | `/reviews` | brand | 45 | 121 | songfinch reviews | 2 | 100 | US |
| 12 | `/apply` | brand | 43 | 132 | songfinch | 1 | 3 100 | US |
| 13 | `/playlists/songs-for-son` | info | 41 | 1 | songs for your son | 8 | 250 | US |
| 14 | `/playlists/songs-for-grandma` | info | 38 | 3 | songs about grandmas | 8 | 250 | US |
| 15 | `/products/personalized-song` | brand | 37 | 75 | how much does songfinch cost | 1 | 50 | US |

### 2.5 Топ-15 по traffic value
| # | URL | Бакет | Трафик | Value, $ | Top keyword | Поз. | Объём | Страна |
|---:|---|---|---:|---:|---|---:|---:|---|
| 1 | `/` | brand | 3 996 | 10 079 | songfinch | 1 | 3 100 | US |
| 2 | `/how-it-works` | gift | 155 | 420 | custom songs | 2 | 450 | US |
| 3 | `/playlists` | brand | 135 | 291 | songfinch | 1 | 3 100 | US |
| 4 | `get.songfinch.com/custom-songs-from-real-artists/` | gift | 70 | 183 | custom song gift | 2 | 150 | GB |
| 5 | `/artists` | brand | 56 | 179 | songfinch | 1 | 3 100 | US |
| 6 | `/song-builder` | brand | 49 | 146 | songfinch | 1 | 3 100 | US |
| 7 | `/apply` | brand | 43 | 132 | songfinch | 1 | 3 100 | US |
| 8 | `/reviews` | brand | 45 | 121 | songfinch reviews | 2 | 100 | US |
| 9 | `/store` | brand | 71 | 91 | songfinch cost | 2 | 90 | US |
| 10 | `/products/personalized-song` | brand | 37 | 75 | how much does songfinch cost | 1 | 50 | US |
| 11 | `/stories/ff8c9864-28aa-4a6b-bb27-1c091cf49249` | ugc_nav | 34 | 26 | custom rock | 2 | 150 | US |
| 12 | `/playlists/songs-for-husband` | info | 30 | 23 | songs for husband | 8 | 70 | US |
| 13 | `/playlists/songs-for-expecting-parents` | info | 48 | 11 | songs about having a baby | 8 | 900 | US |
| 14 | `/playlists/songs-for-wife` | info | 36 | 10 | song for wife | 2 | 40 | US |
| 15 | `get.songfinch.com/thoughtful-gifts/` | brand | 5 | 8 | songfinch cost | 9 | 90 | US |

### 2.6 Winners / losers
| URL | Статус | Трафик prev → cur | Top keyword (поз., страна) |
|---|---|---:|---|
| `get.songfinch.com/custom-songs-from-real-artists/` | — | 12 → 70 | custom song gift (2, GB) |
| `/song-builder` | — | 1 → 49 | songfinch (1, US) |
| `/how-it-works` | — | 111 → 155 | custom songs (2, US) |
| `/stories/ff8c9864-28aa-4a6b-bb27-1c091cf49249` | New | 0 → 34 | custom rock (2, US) |
| `/playlists/songs-for-expecting-parents` | — | 31 → 48 | songs about having a baby (8, US) |
| `/products/personalized-song` | — | 20 → 37 | how much does songfinch cost (1, US) |
| `/playlists/songs-for-wife` | — | 23 → 36 | song for wife (2, US) |
| **Потери** | | | |
| `/` | — | 4 695 → 3 996 | songfinch (1, US) |
| `/dashboard` | — | 71 → 2 | song finch (1, US) |
| `/lp/` | — | 73 → 6 | song finch reviews (5, US) |
| `/artists/alyssa-newton` | — | 35 → 5 | alyssa newton (4, US) |
| `/store` | — | 97 → 71 | songfinch cost (2, US) |
| `/apply` | — | 68 → 43 | songfinch (1, US) |
| `/artists` | — | 78 → 56 | songfinch (1, US) |

New-страниц: 89 (текущий трафик 93, $39); Lost-страниц: 78 (потерянный трафик 83, $5).

Главная потеряла 699 визитов (−15%) по запросу songfinch: 3 400 → 3 100/мес. Это согласуется с падением брендового спроса из прошлого исследования (−17–30% YoY). При этом растут коммерческие LP: `get.` custom song gift в 6 раз, `/how-it-works`, `/song-builder`, `/products/personalized-song`.

### 2.7 AI-видимость
Всего упоминаний в AI-ответах: **115** на 20 страницах (AI Overviews 13, AI Mode 30, ChatGPT 28, Gemini 14, Perplexity 20, Copilot 10, Grok 0).

| URL | Всего | AIO | AI Mode | ChatGPT | Gemini | Perplexity | Copilot | Top keyword |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| `/` | 31 | 3 | 16 | 3 | 4 | 4 | 1 | songfinch |
| `get.songfinch.com/custom-songs/` | 11 | 1 | 2 | 2 | 1 | 0 | 5 | songfinch how long does it take |
| `/products/personalized-song` | 9 | 0 | 0 | 7 | 1 | 0 | 1 | how much does songfinch cost |
| `/how-it-works` | 7 | 2 | 1 | 0 | 0 | 3 | 1 | custom songs |
| `support.songfinch.com/hc/en-us/articles/17016466252571-Pricing-Payment-O…` | 7 | 0 | 2 | 4 | 1 | 0 | 0 | songfinch promo codes |
| `get.songfinch.com/thoughtful-gifts/` | 7 | 3 | 1 | 0 | 3 | 0 | 0 | songfinch cost |
| `support.songfinch.com/hc/en-us/articles/17015838098971-What-is-Songfinch…` | 7 | 0 | 0 | 0 | 0 | 7 | 0 | song finch code |
| `/store` | 6 | 2 | 4 | 0 | 0 | 0 | 0 | songfinch cost |

Цитируются в основном страницы с фактами: цена (`/products/personalized-song` — ChatGPT 7), сроки (`get./custom-songs` — Copilot 5), а также статьи support о ценах и о том, как это работает. AI-ассистенты отвечают на вопросы «сколько стоит» и «как работает» и берут ответ с той страницы, где он сформулирован явно.

### 2.8 География
Страна top keyword → доля текущего трафика: US 98% (5 408), GB 1% (79), IN 0% (17), CA 0% (5), DE 0% (3), AU 0% (3), IL 0% (1)

---

## 3. giftsong.ai: ближайший аналог (AI, подарок, gift page)

### 3.1 Итоги
**Итоги:** страниц в выгрузке 77 (с текущим трафиком 55); статусы: Unchanged 50, New 17, Lost 10

| Метрика | Previous | Current | Δ |
|---|---:|---:|---:|
| Органический трафик, визитов/мес | 2 010 | 1 846 | -8% |
| Traffic value, $ | 2 561 | 2 132 | -17% |
| Главная: трафик (доля) | | 913 (49%) | |
| Бренд (top keyword = бренд): трафик / value | 10 / $15 | 0 (0%) / $0 (0%) | -100% |
| Небрендовый трафик / value | 2 000 / $2 547 | 1 846 / $2 132 | -8% |

### 3.2 Трафик по интентам
| Бакет | Стр. | Трафик prev → cur | Δ | Value prev → cur, $ | Доля трафика | $/визит |
|---|---:|---:|---:|---:|---:|---:|
| Gift-коммерция | 22 | 1 465 → 1 225 | -16% | 2 401 → 1 976 | 66% | 1.61 |
| Инфо-контент (списки песен, поздравления, цитаты, блог) | 41 | 407 → 459 | +13% | 16 → 22 | 25% | 0.05 |
| Off-topic (video/image/NSFW/celebrity voice) | 4 | 86 → 85 | -1% | 116 → 114 | 5% | 1.35 |
| Инструмент: song/lyrics/music generator | 6 | 42 → 77 | +83% | 14 → 19 | 4% | 0.25 |
| Бренд | 4 | 10 → 0 | -100% | 15 → 0 | 0% | 0.00 |

**Важно.** 913 из 1 225 визитов gift-бакета (и $1 504 из $1 976) приходятся на главную с top keyword «how to create a personalized song gift» (1.9k/мес, поз. 3). В прошлом исследовании этот запрос помечен как аномальный / бот-подобный. Вероятно, gift-трафик giftsong сильно завышен. Без главной остаётся ≈ 312 визитов / $472: /pricing, /gifts/*, /relation/*, /create, /how-to/*.

### 3.3 Архитектура и SEO-плейбук
| URL-паттерн | Стр. | Стр. с трафиком | Трафик prev → cur | Value cur, $ |
|---|---:|---:|---:|---:|
| `/` | 1 | 1 | 1 023 → 913 | 1 504 |
| `/article/*` | 44 | 35 | 464 → 540 | 192 |
| `/gifts/*` | 4 | 4 | 341 → 97 | 63 |
| `/pricing` | 1 | 1 | 5 → 76 | 116 |
| `/ai/*` | 3 | 3 | 27 → 68 | 16 |
| `/relation/*` | 5 | 4 | 78 → 54 | 121 |
| `/create` | 1 | 1 | 7 → 27 | 51 |
| `/article` | 1 | 1 | 29 → 19 | 0 |
| `/occasions/*` | 2 | 1 | 9 → 17 | 4 |
| `/how-to/*` | 2 | 1 | 1 → 16 | 50 |
| `/love-song-maker` | 1 | 1 | 15 → 9 | 4 |
| `/gifts` | 1 | 1 | 0 → 7 | 11 |
| `/{lang}/occasions/*` | 1 | 1 | 0 → 3 | 0 |
| `/vs/*` | 2 | 0 | 0 → 0 | 0 |
| `/login` | 1 | 0 | 5 → 0 | 0 |

- **`/occasions/{occasion}`** (birthday, anniversary) и `/de/occasions/birthday/`. Страница birthday ранжируется по birthday song with name (250/мес, поз. 7).
- **`/relation/{who}`** (husband, wife, songs-for-son, loved-one, friend) и `/de/relation/wife`. Ключи: personalized songs for husband (90, поз. 4), song for my wife (60, поз. 5), create a song for a loved one (40, поз. 2). Value на визит самый высокий на сайте, $2–3.
- **`/gifts/{type}`**: music-personalised-gifts (personalised music gifts, GB, **поз. 1**), gift-a-song (personalised song gift 250, поз. 6), song-message, gift-my-music.
- **`/ai/{tool}`**: love-song-maker, lyrics-generator, song-generator, плюс `/es/ai/music-generator`. Это «инструментальные» входы под генераторные запросы, которые потом ведут в подарочную воронку.
- **`/how-to/{x}`**: custom-song-maker (custom songs 450, поз. 6), how-to-make-a-song.
- **`/vs/{competitor}`**: songfinch, songly. Плюс `/songly` — страница под бренд конкурента Songly (songlygift, 500/мес, поз. 4–5). Трафика пока нет.
- **`/article/*`, 44 URL.** Блог широкой тематики: синонимы happy birthday, цитаты для тренеров, поздравления, списки песен, идеи подарков. Даёт 540 визитов, но value $0.05 за визит, и заметная часть трафика идёт из PH и NG. Среди статей есть коммерческие: `best-custom-song-company` (best custom song service 150, поз. 8, New) и `how-much-do-custom-songs-cost` (AI-цитирований 8, максимум на сайте).
- **Языковые папки /de/ и /es/.** Пять URL, 3 визита. Локализация только начата, эффекта нет.

### 3.4 Топ-15 по трафику
| # | URL | Бакет | Трафик | Value, $ | Top keyword | Поз. | Объём | Страна |
|---:|---|---|---:|---:|---|---:|---:|---|
| 1 | `/` | gift | 913 | 1 504 | how to create a personalized song gift | 3 | 1 900 | US |
| 2 | `/article/synonyms-of-happy-birthday` | info | 188 | 4 | happy birthday other term | 6 | 600 | PH |
| 3 | `/article/ai-music-video-generator` | offtopic | 78 | 109 | make ai music video | 2 | 350 | US |
| 4 | `/pricing` | gift | 76 | 116 | song gift | 2 | 150 | US |
| 5 | `/gifts/music-personalised-gifts` | gift | 72 | 38 | personalised music gifts | 1 | 150 | GB |
| 6 | `/ai/love-song-maker` | tool_song | 44 | 14 | ai love song generator | 5 | 150 | US |
| 7 | `/article/thank-you-coach-quotes` | info | 43 | 2 | thank you message from coach to players | 2 | 30 | US |
| 8 | `/article/70-year-birthday-gifts` | info | 30 | 5 | meaningful 70th birthday gifts | 2 | 150 | US |
| 9 | `/create` | gift | 27 | 51 | custom song gift | 3 | 150 | GB |
| 10 | `/ai/lyrics-generator` | tool_song | 22 | 1 | ai song lyrics generator | 9 | 200 | PH |
| 11 | `/article/songs-in-spanish-about-family` | info | 20 | 0 | spanish songs about family love | 2 | 40 | US |
| 12 | `/article/songs-for-reuniting` | info | 19 | 1 | long distance songs | 4 | 200 | US |
| 13 | `/article` | info | 19 | 0 | happy birthday other words | 8 | 150 | PH |
| 14 | `/article/funny-marriage-anniversary-quotes` | info | 18 | 1 | funny wedding anniversary quotes | 5 | 150 | GB |
| 15 | `/article/anniversary-celebration-ideas-at-home` | info | 18 | 2 | at home anniversary ideas | 7 | 150 | US |

### 3.5 Топ-15 по traffic value
| # | URL | Бакет | Трафик | Value, $ | Top keyword | Поз. | Объём | Страна |
|---:|---|---|---:|---:|---|---:|---:|---|
| 1 | `/` | gift | 913 | 1 504 | how to create a personalized song gift | 3 | 1 900 | US |
| 2 | `/pricing` | gift | 76 | 116 | song gift | 2 | 150 | US |
| 3 | `/article/ai-music-video-generator` | offtopic | 78 | 109 | make ai music video | 2 | 350 | US |
| 4 | `/relation/husband` | gift | 16 | 54 | personalized songs for husband | 4 | 90 | US |
| 5 | `/article/best-custom-song-company` | gift | 10 | 53 | best custom song service | 8 | 150 | US |
| 6 | `/create` | gift | 27 | 51 | custom song gift | 3 | 150 | GB |
| 7 | `/how-to/custom-song-maker` | gift | 16 | 50 | custom songs | 6 | 450 | US |
| 8 | `/gifts/music-personalised-gifts` | gift | 72 | 38 | personalised music gifts | 1 | 150 | GB |
| 9 | `/relation/wife` | gift | 16 | 37 | song for my wife | 5 | 60 | US |
| 10 | `/relation/loved-one` | gift | 10 | 29 | create a song for a loved one | 2 | 40 | US |
| 11 | `/gifts/gift-a-song` | gift | 17 | 15 | personalised song gift | 6 | 250 | GB |
| 12 | `/ai/love-song-maker` | tool_song | 44 | 14 | ai love song generator | 5 | 150 | US |
| 13 | `/gifts` | gift | 7 | 11 | song gift | 7 | 150 | US |
| 14 | `/gifts/gift-my-music` | gift | 3 | 8 | gift my music | 4 | 40 | US |
| 15 | `/article/video-tribute-maker` | offtopic | 3 | 5 | group video maker | 10 | 70 | US |

### 3.6 Winners / losers
| URL | Статус | Трафик prev → cur | Top keyword (поз., страна) |
|---|---|---:|---|
| `/article/synonyms-of-happy-birthday` | — | 76 → 188 | happy birthday other term (6, PH) |
| `/pricing` | — | 5 → 76 | song gift (2, US) |
| `/article/70-year-birthday-gifts` | New | 0 → 30 | meaningful 70th birthday gifts (2, US) |
| `/ai/lyrics-generator` | — | 1 → 22 | ai song lyrics generator (9, PH) |
| `/create` | — | 7 → 27 | custom song gift (3, GB) |
| `/ai/love-song-maker` | — | 26 → 44 | ai love song generator (5, US) |
| `/how-to/custom-song-maker` | — | 1 → 16 | custom songs (6, US) |
| **Потери** | | | |
| `/gifts/song-message` | — | 246 → 5 | sending songs to someone (10, US) |
| `/` | — | 1 023 → 913 | how to create a personalized song gift (3, US) |
| `/article/thinking-about-you-text-messages` | — | 69 → 7 | thinking of you text for her (3, US) |
| `/article/anniversary-songs-r-b` | — | 55 → 10 | anniversary songs r&b (9, US) |
| `/relation/songs-for-son` | — | 31 → 12 | songs for your son (4, GB) |
| `/article/thank-you-coach-quotes` | — | 57 → 43 | thank you message from coach to players (2, US) |
| `/relation/husband` | — | 30 → 16 | personalized songs for husband (4, US) |

New-страниц: 17 (текущий трафик 55, $70); Lost-страниц: 10 (потерянный трафик 15, $18).

Растут коммерческие страницы: `/pricing` 5 → 76 (song gift, поз. 2), `/create` 7 → 27 (custom song gift), `/how-to/custom-song-maker` 1 → 16 (custom songs), новая `best-custom-song-company`. Обвалилась `/gifts/song-message` (246 → 5), часть «вирусных» статей тоже падает. Из инфо-контента устойчивы только статьи вокруг подарков и праздников.

### 3.7 AI-видимость
Всего упоминаний в AI-ответах: **35** на 15 страницах (AI Overviews 6, AI Mode 3, ChatGPT 1, Gemini 6, Perplexity 16, Copilot 3, Grok 0).

| URL | Всего | AIO | AI Mode | ChatGPT | Gemini | Perplexity | Copilot | Top keyword |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| `/article/how-much-do-custom-songs-cost` | 8 | 1 | 1 | 0 | 2 | 1 | 3 | how much does a custom song cost |
| `/article/thank-you-coach-quotes` | 4 | 1 | 0 | 0 | 0 | 3 | 0 | thank you message from coach to players |
| `/article/anniversary-celebration-ideas-at-home` | 4 | 0 | 0 | 0 | 0 | 4 | 0 | at home anniversary ideas |
| `/article/virtual-birthday-gift` | 4 | 0 | 0 | 0 | 2 | 2 | 0 | virtual birthday gift ideas |
| `/article/best-custom-song-company` | 3 | 1 | 1 | 0 | 0 | 1 | 0 | best custom song service |
| `/article/synonyms-of-happy-birthday` | 2 | 0 | 0 | 1 | 0 | 1 | 0 | happy birthday other term |
| `/article/video-tribute-maker` | 2 | 1 | 0 | 0 | 1 | 0 | 0 | group video maker |
| `/` | 1 | 0 | 1 | 0 | 0 | 0 | 0 | how to create a personalized song gift |

### 3.8 География
Страна top keyword → доля текущего трафика: US 77% (1 416), PH 12% (229), GB 9% (164), NG 1% (12), AU 1% (10), IN 0% (5), Ghana 0% (4)

---

## 4. songlorious.com: человеческие песни, рост на бренде

### 4.1 Итоги
**Итоги:** страниц в выгрузке 26 (с текущим трафиком 19); статусы: Unchanged 18, New 5, Lost 3

| Метрика | Previous | Current | Δ |
|---|---:|---:|---:|
| Органический трафик, визитов/мес | 595 | 1 337 | +125% |
| Traffic value, $ | 1 438 | 3 049 | +112% |
| Главная: трафик (доля) | | 1 178 (88%) | |
| Бренд (top keyword = бренд): трафик / value | 564 / $1 411 | 1 278 (96%) / $2 967 (97%) | +127% |
| Небрендовый трафик / value | 31 / $27 | 59 / $82 | +90% |

### 4.2 Трафик по интентам
| Бакет | Стр. | Трафик prev → cur | Δ | Value prev → cur, $ | Доля трафика | $/визит |
|---|---:|---:|---:|---:|---:|---:|
| Бренд | 10 | 564 → 1 278 | +127% | 1 411 → 2 967 | 96% | 2.32 |
| Gift-коммерция | 4 | 12 → 34 | +183% | 27 → 81 | 3% | 2.39 |
| UGC/навигация (артисты, страницы песен, support, login) | 12 | 19 → 25 | +32% | 0 → 0 | 2% | 0.01 |

### 4.3 Архитектура
| URL-паттерн | Стр. | Стр. с трафиком | Трафик prev → cur | Value cur, $ |
|---|---:|---:|---:|---:|
| `/` | 1 | 1 | 465 → 1 178 | 2 677 |
| `/about` | 1 | 1 | 55 → 35 | 157 |
| `/artist/*` | 11 | 6 | 17 → 25 | 0 |
| `/landing-pages/*` | 3 | 3 | 1 → 24 | 56 |
| `/reviews` | 1 | 1 | 36 → 18 | 36 |
| `/create-my-song` | 1 | 1 | 3 → 15 | 30 |
| `/faq` | 1 | 1 | 3 → 15 | 30 |
| `/featured-artists` | 1 | 1 | 2 → 14 | 30 |
| `/landing-pages` | 1 | 1 | 10 → 10 | 23 |
| `/promo-code` | 1 | 1 | 0 → 1 | 5 |
| `/songlorious-business` | 1 | 1 | 0 → 1 | 1 |
| `/country` | 1 | 1 | 1 → 1 | 3 |
| `/hindi-apply` | 1 | 0 | 2 → 0 | 0 |
| `/apply` | 1 | 0 | 0 → 0 | 0 |

- **`/landing-pages/{occasion|genre}`**: anniversary, country, custom-songs-vs-ai-music. `/landing-pages/anniversary` вышла на **поз. 1** по custom song for anniversary (30/мес), трафик 1 → 21. Это доказательство, что узкие occasion-LP с точным коммерческим ключом быстро выходят в топ.
- **`/artist/{name}`, 11 URL.** Профили артистов, как у Songfinch.
- `/landing-pages/custom-songs-vs-ai-music` — позиционирование «человек против AI». Страница цитируется AI-ассистентами (3).
- `/songlorious-business` — B2B-страница, 5 AI-цитирований.
- Нет блога, программатики и языков.

### 4.4 Топ страниц по трафику / value
| # | URL | Бакет | Трафик | Value, $ | Top keyword | Поз. | Объём | Страна |
|---:|---|---|---:|---:|---|---:|---:|---|
| 1 | `/` | brand | 1 178 | 2 677 | songlorious | 1 | 700 | US |
| 2 | `/about` | brand | 35 | 157 | songlorious | 1 | 700 | US |
| 3 | `/landing-pages/anniversary` | gift | 21 | 50 | custom song for anniversary | 1 | 30 | US |
| 4 | `/reviews` | brand | 18 | 36 | songlorious | 1 | 700 | US |
| 5 | `/create-my-song` | brand | 15 | 30 | songlorious | 1 | 700 | US |
| 6 | `/artist/mads` | ugc_nav | 15 | 0 | mads | 1 | 50 | BE |
| 7 | `/faq` | brand | 15 | 30 | songlorious | 1 | 700 | US |
| 8 | `/featured-artists` | brand | 14 | 30 | songlorious | 1 | 700 | US |
| 9 | `/landing-pages` | gift | 10 | 23 | custom song for anniversary | 2 | 30 | US |
| 10 | `/artist/savannah-reid` | ugc_nav | 5 | 0 | savannah reid | 7 | 100 | US |
| 11 | `/landing-pages/country` | gift | 2 | 4 | custom country song | 2 | 10 | US |
| 12 | `/artist/chelsea-chase` | ugc_nav | 2 | 0 | chelsea chase | 1 | 100 | US |
| 13 | `/artist/taylor-hayes` | ugc_nav | 1 | 0 | taylor m hayes | 4 | 10 | US |
| 14 | `/artist/ryan-newton` | ugc_nav | 1 | 0 | ryan newton | 7 | 40 | US |
| 15 | `/promo-code` | brand | 1 | 5 | songlorious promo code | 1 | 0 | US |

| # | URL | Бакет | Трафик | Value, $ | Top keyword | Поз. | Объём | Страна |
|---:|---|---|---:|---:|---|---:|---:|---|
| 1 | `/` | brand | 1 178 | 2 677 | songlorious | 1 | 700 | US |
| 2 | `/about` | brand | 35 | 157 | songlorious | 1 | 700 | US |
| 3 | `/landing-pages/anniversary` | gift | 21 | 50 | custom song for anniversary | 1 | 30 | US |
| 4 | `/reviews` | brand | 18 | 36 | songlorious | 1 | 700 | US |
| 5 | `/faq` | brand | 15 | 30 | songlorious | 1 | 700 | US |
| 6 | `/create-my-song` | brand | 15 | 30 | songlorious | 1 | 700 | US |
| 7 | `/featured-artists` | brand | 14 | 30 | songlorious | 1 | 700 | US |
| 8 | `/landing-pages` | gift | 10 | 23 | custom song for anniversary | 2 | 30 | US |
| 9 | `/promo-code` | brand | 1 | 5 | songlorious promo code | 1 | 0 | US |
| 10 | `/landing-pages/country` | gift | 2 | 4 | custom country song | 2 | 10 | US |
| 11 | `/country` | gift | 1 | 3 | custom country song | 4 | 10 | US |
| 12 | `/songlorious-business` | brand | 1 | 1 | songalicious | 1 | 0 | US |
| 13 | `/landing-pages/custom-songs-vs-ai-music` | brand | 1 | 1 | songglorious | 1 | 10 | US |
| 14 | `/artist/ryan-newton` | ugc_nav | 1 | 0 | ryan newton | 7 | 40 | US |
| 15 | `/artist/chelsea-chase` | ugc_nav | 2 | 0 | chelsea chase | 1 | 100 | US |

### 4.5 Winners / losers
| URL | Статус | Трафик prev → cur | Top keyword (поз., страна) |
|---|---|---:|---|
| `/` | — | 465 → 1 178 | songlorious (1, US) |
| `/landing-pages/anniversary` | — | 1 → 21 | custom song for anniversary (1, US) |
| `/artist/mads` | New | 0 → 15 | mads (1, BE) |
| `/create-my-song` | — | 3 → 15 | songlorious (1, US) |
| `/faq` | — | 3 → 15 | songlorious (1, US) |
| `/featured-artists` | — | 2 → 14 | songlorious (1, US) |
| `/landing-pages/country` | New | 0 → 2 | custom country song (2, US) |
| **Потери** | | | |
| `/about` | — | 55 → 35 | songlorious (1, US) |
| `/reviews` | — | 36 → 18 | songlorious (1, US) |
| `/artist/savannah-reid` | — | 12 → 5 | savannah reid (7, US) |
| `/hindi-apply` | Lost | 2 → 0 | hindi lyrics writer (3, IN) |
| `/artist/vanessa-jordan` | Lost | 1 → 0 | vanessa jordan (5, US) |

New-страниц: 5 (текущий трафик 19, $6); Lost-страниц: 3 (потерянный трафик 3, $0).

Рост +125% почти целиком брендовый: главная 465 → 1 178 по запросу songlorious (700/мес). Скорее всего, это работа PR, рекламы или соцсетей, а не SEO.

### 4.6 AI-видимость
Всего упоминаний в AI-ответах: **47** на 8 страницах (AI Overviews 4, AI Mode 9, ChatGPT 15, Gemini 3, Perplexity 10, Copilot 6, Grok 0).

| URL | Всего | AIO | AI Mode | ChatGPT | Gemini | Perplexity | Copilot | Top keyword |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| `/` | 23 | 3 | 8 | 4 | 1 | 5 | 2 | songlorious |
| `/about` | 10 | 1 | 0 | 4 | 1 | 3 | 1 | songlorious |
| `/songlorious-business` | 5 | 0 | 0 | 3 | 0 | 1 | 1 | songalicious |
| `/faq` | 3 | 0 | 0 | 1 | 1 | 1 | 0 | songlorious |
| `/landing-pages/custom-songs-vs-ai-music` | 3 | 0 | 1 | 1 | 0 | 0 | 1 | songglorious |
| `/artist/ryan-newton` | 1 | 0 | 0 | 1 | 0 | 0 | 0 | ryan newton |
| `/country` | 1 | 0 | 0 | 0 | 0 | 0 | 1 | custom country song |
| `/artist/jason-carter` | 1 | 0 | 0 | 1 | 0 | 0 | 0 | who is jason carter |

На размер сайта у Songlorious лучшая AI-видимость: 47 упоминаний на 26 URL. Цитируются /about, /faq, B2B-страница и «vs AI» — страницы, где о компании написано фактами.

### 4.7 География
Страна top keyword → доля текущего трафика: US 99% (1 322), BE 1% (15)

---

## 5. sendfame.com: подарочный продукт, который ушёл в общие AI-генераторы

### 5.1 Итоги
**Итоги:** страниц в выгрузке 107 (с текущим трафиком 70); статусы: Unchanged 73, New 19, Lost 15

| Метрика | Previous | Current | Δ |
|---|---:|---:|---:|
| Органический трафик, визитов/мес | 6 788 | 3 932 | -42% |
| Traffic value, $ | 4 099 | 2 683 | -35% |
| Главная: трафик (доля) | | 948 (24%) | |
| Бренд (top keyword = бренд): трафик / value | 1 560 / $3 211 | 1 054 (27%) / $2 091 (78%) | -32% |
| Небрендовый трафик / value | 5 228 / $887 | 2 878 / $593 | -45% |

### 5.2 Трафик по интентам
| Бакет | Стр. | Трафик prev → cur | Δ | Value prev → cur, $ | Доля трафика | $/визит |
|---|---:|---:|---:|---:|---:|---:|
| Off-topic (video/image/NSFW/celebrity voice) | 40 | 4 051 → 2 004 | -51% | 801 → 522 | 51% | 0.26 |
| Бренд | 9 | 1 560 → 1 054 | -32% | 3 211 → 2 091 | 27% | 1.98 |
| Инфо-контент (списки песен, поздравления, цитаты, блог) | 39 | 1 036 → 674 | -35% | 28 → 15 | 17% | 0.02 |
| Инструмент: song/lyrics/music generator | 12 | 123 → 189 | +54% | 54 → 53 | 5% | 0.28 |
| Gift-коммерция | 1 | 17 → 10 | -41% | 3 → 2 | 0% | 0.24 |
| UGC/навигация (артисты, страницы песен, support, login) | 6 | 1 → 1 | +0% | 0 → 0 | 0% | 0.09 |

Gift-интент у SendFame почти нулевой: `/happy-birthday-music` (happy birthday song custom, 40/мес, поз. 5) — 10 визитов. Половина трафика приходит с off-topic: AI video generator, «image to video nsfw», «dirty ai image generator», deepfake, book cover, celebrity voice.

### 5.3 Архитектура и программатика
| URL-паттерн | Стр. | Стр. с трафиком | Трафик prev → cur | Value cur, $ |
|---|---:|---:|---:|---:|
| `/blog/*` | 37 | 26 | 4 108 → 1 400 | 238 |
| `/` | 1 | 1 | 1 428 → 948 | 1 877 |
| `/happy-birthday/*` | 22 | 17 | 616 → 481 | 9 |
| `/ai-video-generator` | 1 | 1 | 211 → 414 | 138 |
| `/ai-image-generator` | 1 | 1 | 167 → 334 | 135 |
| `/random-song-generator` | 1 | 1 | 63 → 94 | 26 |
| `/ai-book-cover-generator` | 1 | 1 | 0 → 64 | 85 |
| `/discover/*` | 13 | 6 | 49 → 36 | 45 |
| `/freestyle-rap-lyrics` | 1 | 1 | 2 → 36 | 2 |
| `/pricing` | 1 | 1 | 33 → 21 | 43 |
| `/ai-rap-generator` | 1 | 1 | 0 → 20 | 6 |
| `/ai-music-generator` | 1 | 1 | 28 → 15 | 31 |
| `/ai-image-generator/*` | 1 | 1 | 0 → 14 | 31 |
| `/song-name-generator` | 1 | 1 | 14 → 12 | 0 |
| `/scary-ai-images` | 1 | 1 | 10 → 12 | 3 |

- **`/happy-birthday/{name|relation}`, 22 URL, 481 визит.** Программатика по именам (stephanie, linda, kathy, sharon, kim, karen, john, michael, lisa) и по отношениям (aunt, boyfriend, nephew, son-in-law, daughter-in-law, granddaughter, sister). Ключи: birthday wishes for aunt, happy birthday {name} images. Это интент открыток и поздравлений, value ≈ $0.01–0.05 за визит, большая часть трафика из PK, IN, NG. Как шаблон «страница на имя» это интересно, но в таком виде трафик тщеславный.
- **`/ai-*-generator`**: video, image, book cover, music, rap, country, sticker, album cover. Плюс `/random-song-generator`, `/song-name-generator`, `/freestyle-rap-lyrics`, `/diss-track-generator`. Генераторные лендинги.
- **`/discover/effects/*`** — видеоэффекты (hulk, balloon belly, jumpscare).
- **`/blog/*`, 37 URL, 1 400 визитов.** Это 1/3 трафика, на 70% из одной статьи `ai-video-generator-free` (HU, −72%). Есть статьи «X alternatives»: cameo-alternatives, musenet-alternative, kits-ai-alternative.

### 5.4 Топ-15 по трафику
| # | URL | Бакет | Трафик | Value, $ | Top keyword | Поз. | Объём | Страна |
|---:|---|---|---:|---:|---|---:|---:|---|
| 1 | `/blog/ai-video-generator-free` | offtopic | 972 | 120 | ai video generator | 7 | 6 800 | HU |
| 2 | `/` | brand | 948 | 1 877 | sendfame | 1 | 1 100 | US |
| 3 | `/ai-video-generator` | offtopic | 414 | 138 | image to video nsfw | 5 | 3 100 | US |
| 4 | `/ai-image-generator` | offtopic | 334 | 135 | dirty ai image generator | 5 | 1 200 | US |
| 5 | `/happy-birthday/aunt` | info | 288 | 3 | birthday wishes for aunt | 2 | 350 | PK |
| 6 | `/blog/what-is-ai-music` | info | 99 | 2 | ai music | 8 | 3 500 | ZA |
| 7 | `/random-song-generator` | tool_song | 94 | 26 | random song | 7 | 200 | AU |
| 8 | `/blog/heart-touching-husband-bday-wishes` | info | 70 | 2 | heart touching husband bday wishes | 6 | 800 | NG |
| 9 | `/ai-book-cover-generator` | offtopic | 64 | 85 | ai book cover generator | 8 | 1 700 | US |
| 10 | `/happy-birthday/gorgeous` | info | 55 | 3 | happy birthday gorgeous | 7 | 700 | IN |
| 11 | `/happy-birthday/boyfriend` | info | 53 | 1 | birthday message for boyfriend | 8 | 350 | US |
| 12 | `/blog/celebrity-voice-generator-free` | offtopic | 49 | 17 | celebrity voice generator | 2 | 90 | NG |
| 13 | `/blog/best-celebrity-ai-voice-generator` | offtopic | 46 | 8 | celebrity voice generator | 7 | 350 | IN |
| 14 | `/freestyle-rap-lyrics` | tool_song | 36 | 2 | freestyle rap lyrics | 2 | 100 | GB |
| 15 | `/blog/ai-celebrity-voice-generator` | offtopic | 29 | 4 | ai voice generator celebrity | 6 | 90 | GB |

### 5.5 Топ-15 по traffic value
| # | URL | Бакет | Трафик | Value, $ | Top keyword | Поз. | Объём | Страна |
|---:|---|---|---:|---:|---|---:|---:|---|
| 1 | `/` | brand | 948 | 1 877 | sendfame | 1 | 1 100 | US |
| 2 | `/ai-video-generator` | offtopic | 414 | 138 | image to video nsfw | 5 | 3 100 | US |
| 3 | `/ai-image-generator` | offtopic | 334 | 135 | dirty ai image generator | 5 | 1 200 | US |
| 4 | `/blog/ai-video-generator-free` | offtopic | 972 | 120 | ai video generator | 7 | 6 800 | HU |
| 5 | `/ai-book-cover-generator` | offtopic | 64 | 85 | ai book cover generator | 8 | 1 700 | US |
| 6 | `/pricing` | brand | 21 | 43 | sendfame | 1 | 1 100 | US |
| 7 | `/discover/tools` | brand | 21 | 43 | sendfame | 1 | 1 100 | US |
| 8 | `/blog/best-ai-video-creation-tools` | brand | 21 | 43 | sendfame | 1 | 1 100 | US |
| 9 | `/ai-music-generator` | brand | 15 | 31 | sendfame | 1 | 1 100 | US |
| 10 | `/ai-image-generator/editor` | brand | 14 | 31 | sendfame | 1 | 1 100 | US |
| 11 | `/random-song-generator` | tool_song | 94 | 26 | random song | 7 | 200 | AU |
| 12 | `/blog/celebrity-voice-generator-free` | offtopic | 49 | 17 | celebrity voice generator | 2 | 90 | NG |
| 13 | `/blog/cameo-alternatives` | tool_song | 16 | 16 | cameo competitors | 3 | 40 | US |
| 14 | `/blog/ai-video-generator-from-image` | brand | 7 | 11 | send fame | 1 | 800 | US |
| 15 | `/discover` | brand | 7 | 11 | send fame | 1 | 800 | US |

### 5.6 Winners / losers
| URL | Статус | Трафик prev → cur | Top keyword (поз., страна) |
|---|---|---:|---|
| `/ai-video-generator` | — | 211 → 414 | image to video nsfw (5, US) |
| `/ai-image-generator` | — | 167 → 334 | dirty ai image generator (5, US) |
| `/blog/what-is-ai-music` | New | 0 → 99 | ai music (8, ZA) |
| `/ai-book-cover-generator` | New | 0 → 64 | ai book cover generator (8, US) |
| `/happy-birthday/aunt` | — | 227 → 288 | birthday wishes for aunt (2, PK) |
| `/freestyle-rap-lyrics` | — | 2 → 36 | freestyle rap lyrics (2, GB) |
| `/random-song-generator` | — | 63 → 94 | random song (7, AU) |
| **Потери** | | | |
| `/blog/ai-video-generator-free` | — | 3 445 → 972 | ai video generator (7, HU) |
| `/` | — | 1 428 → 948 | sendfame (1, US) |
| `/blog/heart-touching-husband-bday-wishes` | — | 327 → 70 | heart touching husband bday wishes (6, NG) |
| `/happy-birthday/boyfriend` | — | 229 → 53 | birthday message for boyfriend (8, US) |
| `/blog/heart-touching-birthday-wishes-for-special-person` | — | 68 → 3 | special person birthday (8, US) |
| `/blog/best-deepfake-apps` | — | 63 → 23 | ai deepfake app (2, KR) |
| `/happy-birthday/nephew` | Lost | 17 → 0 | happy birthday nephew (5, AU) |

New-страниц: 19 (текущий трафик 203, $142); Lost-страниц: 15 (потерянный трафик 42, $15).

Растут NSFW-генераторы: video ×2, image ×2. Падают бренд (−34%), блог про video и поздравления. Классический сценарий: подарочный продукт не вырос в органике и ушёл ловить общий AI-трафик. Брендовый спрос сокращается.

### 5.7 AI-видимость
Всего упоминаний в AI-ответах: **35** на 10 страницах (AI Overviews 0, AI Mode 4, ChatGPT 7, Gemini 6, Perplexity 18, Copilot 0, Grok 0).

| URL | Всего | AIO | AI Mode | ChatGPT | Gemini | Perplexity | Copilot | Top keyword |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| `/` | 9 | 0 | 2 | 3 | 1 | 3 | 0 | sendfame |
| `/happy-birthday/aunt` | 8 | 0 | 0 | 0 | 0 | 8 | 0 | birthday wishes for aunt |
| `/pricing` | 3 | 0 | 1 | 0 | 1 | 1 | 0 | sendfame |
| `/blog/cameo-alternatives` | 3 | 0 | 0 | 0 | 2 | 1 | 0 | cameo competitors |
| `/ai-video-generator` | 2 | 0 | 0 | 2 | 0 | 0 | 0 | image to video nsfw |
| `/ai-image-generator` | 2 | 0 | 0 | 1 | 0 | 1 | 0 | dirty ai image generator |
| `/blog/celebrity-voice-generator-free` | 2 | 0 | 1 | 0 | 0 | 1 | 0 | celebrity voice generator |
| `/blog/best-ai-video-creation-tools` | 2 | 0 | 0 | 0 | 2 | 0 | 0 | sendfame |

### 5.8 География
Страна top keyword → доля текущего трафика: US 52% (2 050), HU 25% (972), PK 7% (293), IN 3% (127), NG 3% (119), AU 3% (108), ZA 3% (106)

---

## 6. wondera.ai: массовая мультиязычная программатика

### 6.1 Итоги
**Итоги:** страниц в выгрузке 1423 (с текущим трафиком 526); статусы: Unchanged 766, Lost 274, New 383

| Метрика | Previous | Current | Δ |
|---|---:|---:|---:|
| Органический трафик, визитов/мес | 4 927 | 4 026 | -18% |
| Traffic value, $ | 549 | 705 | +28% |
| Главная: трафик (доля) | | 100 (2%) | |
| Бренд (top keyword = бренд): трафик / value | 80 / $27 | 108 (3%) / $40 (6%) | +35% |
| Небрендовый трафик / value | 4 847 / $522 | 3 918 / $665 | -19% |

### 6.2 Трафик по интентам
| Бакет | Стр. | Трафик prev → cur | Δ | Value prev → cur, $ | Доля трафика | $/визит |
|---|---:|---:|---:|---:|---:|---:|
| Инструмент: аудио-утилиты (vocal remover, converter, autotune, covers, remix) | 232 | 2 041 → 2 152 | +5% | 371 → 451 | 53% | 0.21 |
| Инфо-контент (списки песен, поздравления, цитаты, блог) | 855 | 1 654 → 1 004 | -39% | 71 → 50 | 25% | 0.05 |
| Инструмент: song/lyrics/music generator | 131 | 525 → 366 | -30% | 57 → 82 | 9% | 0.22 |
| UGC/навигация (артисты, страницы песен, support, login) | 179 | 616 → 307 | -50% | 12 → 5 | 8% | 0.02 |
| Бренд | 15 | 80 → 108 | +35% | 27 → 40 | 3% | 0.37 |
| Off-topic (video/image/NSFW/celebrity voice) | 11 | 11 → 89 | +709% | 11 → 77 | 2% | 0.87 |

### 6.3 Архитектура и программатика

| URL-паттерн | Стр. | Стр. с трафиком | Трафик prev → cur | Value cur, $ |
|---|---:|---:|---:|---:|
| `/tools/*` | 1219 | 474 | 4 104 → 3 545 | 656 |
| `/song/*` | 163 | 38 | 608 → 295 | 5 |
| `/` | 1 | 1 | 76 → 100 | 37 |
| `/tools` | 1 | 1 | 85 → 40 | 2 |
| `/AI-real-time-AI-autotune-tools` | 1 | 1 | 26 → 20 | 0 |
| `/producer/*` | 14 | 3 | 1 → 6 | 0 |
| `/song-recreation-with-my-voice-tool` | 1 | 1 | 6 → 6 | 3 |
| `/info` | 1 | 1 | 5 → 4 | 0 |
| `/karaoke-love-songs-for-females` | 1 | 1 | 3 → 3 | 0 |
| `/songs-about-complicated-love` | 1 | 1 | 2 → 2 | 1 |
| `/detail` | 1 | 1 | 2 → 2 | 0 |
| `/music` | 1 | 1 | 1 → 1 | 1 |
| `/brand` | 1 | 1 | 1 → 1 | 0 |
| `/home` | 1 | 1 | 1 → 1 | 0 |
| `/tool-for-clean-audio-mixdown` | 1 | 0 | 2 → 0 | 0 |

Почти весь сайт (1 219 из 1 423 URL) построен по шаблону `/tools/{lang}/{slug}`. Языки: en 281, it 212, es 177, fr 114, ru 96, pt 74, de 71, ja 39, ko 20, zh-Hant 17. Под одним префиксом /tools/ смешаны разные типы страниц:

| Тип страниц (Wondera) | URL | Трафик prev → cur |
|---|---:|---:|
| Аудио-инструменты: autotune, AI cover, robot voice, mashup, remix, song editor | 232 | 2 041 → 2 152 |
| Списки песен, прочее: mood, genre, «{artist} love songs», dance, karaoke | 653 | 1 262 → 707 |
| Списки песен под повод или отношения: birthday (91), wedding, mother/daughter, siblings, son… | 201 | 391 → 296 |
| Генераторы песен и музыки | 112 | 496 → 280 |
| UGC `/song/info/{uuid}`, `/song/detail/{id}`, `/producer/*` | 177 | 609 → 301 |
| `the-best-{competitor}-alternatives`: songdo, songr, musicfx, moises, riffusion, boomy, jammable, amper, musicfy, soundraw | 19 | 30 → 87 |

- В среднем ≈ 2.8 визита на URL. Ротация высокая: 383 New / 274 Lost, Lost-страницы унесли 1 055 визитов. Похоже, Google периодически пересматривает индексацию массового шаблонного контента.
- 85 URL встречаются и на `www.`, и без него. Это дубли, канонизация не настроена.
- **UGC-страницы песен ранжируются по запросам «поздравление + имя».** Примеры: «с днем рождения олеся» (RU, 1 100/мес, поз. 4, 118 визитов, затем Lost), «feliz cumpleaños aime» (5 100/мес), «happy birthday julia» (300–450), «happy birthday maurice», «happy birthday mary ann». Спрос на именные поздравительные песни есть во всех языках, и публичная страница песни умеет его собирать, хотя и нестабильно.

### 6.4 Топ-15 по трафику
| # | URL | Бакет | Трафик | Value, $ | Top keyword | Поз. | Объём | Страна |
|---:|---|---|---:|---:|---|---:|---:|---|
| 1 | `/tools/en/ai-robot-voice-filter` | tool_audio | 243 | 44 | robot voice changer | 2 | 600 | US |
| 2 | `/tools/en/AI-cover-generator-tools` | tool_audio | 166 | 40 | ai covers | 7 | 2 000 | US |
| 3 | `/song/info/aba186e2-11ba-4cbb-a0d6-6605ab86212e` | ugc_nav | 158 | 0 | mai doli chadhi chalali lyrics | 7 | 3 000 | IN |
| 4 | `/tools/es/AI-real-time-AI-autotune-tools` | tool_audio | 146 | 12 | autotune online gratis | 3 | 100 | ES |
| 5 | `/tools/en/AI-two-song-mashup-tools` | tool_audio | 125 | 75 | song combiner | 2 | 250 | US |
| 6 | `/tools/fr/AI-real-time-AI-autotune-tools` | tool_audio | 111 | 37 | autotune gratuit | 7 | 1 000 | FR |
| 7 | `/tools/ko/ai-vocal-style-cover-tools` | tool_audio | 104 | 28 | ai 커버 만들기 | 2 | 400 | KR |
| 8 | `/` | brand | 100 | 37 | wondera | 1 | 30 | ES |
| 9 | `/tools/es/AI-real-time-AI-autotune-tools` | tool_audio | 71 | 4 | autoturn online | 2 | 450 | MX |
| 10 | `/tools/en/ai-song-edit-tools` | tool_audio | 69 | 25 | ai song editor | 4 | 300 | US |
| 11 | `/tools/fr/the-best-songdo-alternatives` | tool_song | 65 | 23 | song do | 3 | 500 | FR |
| 12 | `/tools/en/free-ai-music-video-generator` | offtopic | 62 | 73 | free music video maker | 6 | 30 | AU |
| 13 | `/tools/ru/ai-beat-maker` | tool_audio | 59 | 1 | бит | 9 | 2 000 | RU |
| 14 | `/tools/en/AI-real-time-AI-autotune-tools` | tool_audio | 52 | 11 | ai autotune | 8 | 250 | US |
| 15 | `/tools/en/ai-drake-voice-tools` | tool_audio | 52 | 10 | ai drake | 5 | 100 | US |

### 6.5 Топ-15 по traffic value
| # | URL | Бакет | Трафик | Value, $ | Top keyword | Поз. | Объём | Страна |
|---:|---|---|---:|---:|---|---:|---:|---|
| 1 | `/tools/en/AI-two-song-mashup-tools` | tool_audio | 125 | 75 | song combiner | 2 | 250 | US |
| 2 | `/tools/en/free-ai-music-video-generator` | offtopic | 62 | 73 | free music video maker | 6 | 30 | AU |
| 3 | `/tools/en/ai-robot-voice-filter` | tool_audio | 243 | 44 | robot voice changer | 2 | 600 | US |
| 4 | `/tools/en/AI-cover-generator-tools` | tool_audio | 166 | 40 | ai covers | 7 | 2 000 | US |
| 5 | `/tools/fr/AI-real-time-AI-autotune-tools` | tool_audio | 111 | 37 | autotune gratuit | 7 | 1 000 | FR |
| 6 | `/` | brand | 100 | 37 | wondera | 1 | 30 | ES |
| 7 | `/tools/ko/ai-vocal-style-cover-tools` | tool_audio | 104 | 28 | ai 커버 만들기 | 2 | 400 | KR |
| 8 | `/tools/en/ai-song-edit-tools` | tool_audio | 69 | 25 | ai song editor | 4 | 300 | US |
| 9 | `/tools/fr/the-best-songdo-alternatives` | tool_song | 65 | 23 | song do | 3 | 500 | FR |
| 10 | `/tools/ai-song-edit-tools` | tool_audio | 27 | 19 | ai song editor | 4 | 300 | US |
| 11 | `/tools/en/AI-mashup-generator` | tool_audio | 25 | 19 | mashup generator | 6 | 100 | US |
| 12 | `/tools/ja/the-best-ai-music-composer-free` | tool_song | 37 | 16 | 音楽 作成 | 2 | 150 | JP |
| 13 | `/tools/en/professional-audio-editing-tool` | tool_audio | 43 | 16 | ai mixing tools | 1 | 70 | US |
| 14 | `/tools/ko/song-recreation-with-my-voice-tool` | tool_audio | 39 | 13 | 내 목소리 ai 노래 만들기 | 3 | 200 | KR |
| 15 | `/tools/es/AI-real-time-AI-autotune-tools` | tool_audio | 146 | 12 | autotune online gratis | 3 | 100 | ES |

### 6.6 Winners / losers
| URL | Статус | Трафик prev → cur | Top keyword (поз., страна) |
|---|---|---:|---|
| `/tools/en/ai-robot-voice-filter` | — | 0 → 243 | robot voice changer (2, US) |
| `/song/info/aba186e2-11ba-4cbb-a0d6-6605ab86212e` | New | 0 → 158 | mai doli chadhi chalali lyrics (7, IN) |
| `/tools/en/AI-cover-generator-tools` | — | 21 → 166 | ai covers (7, US) |
| `/tools/en/AI-two-song-mashup-tools` | — | 51 → 125 | song combiner (2, US) |
| `/tools/en/free-ai-music-video-generator` | — | 6 → 62 | free music video maker (6, AU) |
| `/tools/fr/the-best-songdo-alternatives` | — | 13 → 65 | song do (3, FR) |
| `/tools/en/ai-song-edit-tools` | — | 20 → 69 | ai song editor (4, US) |
| **Потери** | | | |
| `/tools/en/summer-playlist` | — | 301 → 8 | summer playlist (6, GB) |
| `/tools/ru/use-case/text-to-music-ai-generator` | — | 227 → 30 | генератор песни (4, RU) |
| `/song/info/714283a1-36f8-4696-ade0-8b0314c5c5f3` | Lost | 179 → 0 | siloe todos los besos (4, ES) |
| `/tools/es/AI-real-time-AI-autotune-tools` | — | 230 → 71 | autoturn online (2, MX) |
| `/song/info/54853d2d-bd7e-406f-8878-1c9fd1f1e2de` | Lost | 126 → 0 | mpeg a mp3 (3, ES) |
| `/song/info/d0126e2ce54b449ab4f489a86f894d30` | Lost | 118 → 0 | с днем рождения олеся (4, RU) |
| `/tools/pt/AI-vocal-comp-cover-tools` | — | 98 → 2 | covers ai (3, Portugal) |

New-страниц: 383 (текущий трафик 527, $51); Lost-страниц: 274 (потерянный трафик 1 055, $105).

### 6.7 AI-видимость
Всего упоминаний в AI-ответах: **3** на 3 страницах (AI Overviews 2, AI Mode 1, ChatGPT 0, Gemini 0, Perplexity 0, Copilot 0, Grok 0).

| URL | Всего | AIO | AI Mode | ChatGPT | Gemini | Perplexity | Copilot | Top keyword |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| `/tools/en/AI-real-time-AI-autotune-tools` | 1 | 0 | 1 | 0 | 0 | 0 | 0 | ai autotune |
| `/tools/fr/just-dance-2023-song-list` | 1 | 1 | 0 | 0 | 0 | 0 | 0 | just dance 2023 musique |
| `/tools/fr/ai-robot-voice-filter` | 1 | 1 | 0 | 0 | 0 | 0 | 0 | robot voix |

Массовая программатика в AI-ответах почти не цитируется: 3 упоминания на 1 423 URL.

### 6.8 География
Страна top keyword → доля текущего трафика: US 34% (1 355), IT 10% (418), ES 9% (345), RU 8% (319), FR 6% (256), MX 5% (213), KR 5% (184)

---

## 7. musicmake.ai: аудио-утилиты и паразитирование на бренде Suno

### 7.1 Итоги
**Итоги:** страниц в выгрузке 238 (с текущим трафиком 122); статусы: Unchanged 86, Lost 67, New 85

| Метрика | Previous | Current | Δ |
|---|---:|---:|---:|
| Органический трафик, визитов/мес | 3 441 | 3 552 | +3% |
| Traffic value, $ | 245 | 373 | +52% |
| Главная: трафик (доля) | | 233 (7%) | |
| Бренд (top keyword = бренд): трафик / value | 0 / $0 | 0 (0%) / $0 (0%) | — |
| Небрендовый трафик / value | 3 441 / $245 | 3 552 / $373 | +3% |

### 7.2 Трафик по интентам
| Бакет | Стр. | Трафик prev → cur | Δ | Value prev → cur, $ | Доля трафика | $/визит |
|---|---:|---:|---:|---:|---:|---:|
| Инструмент: аудио-утилиты (vocal remover, converter, autotune, covers, remix) | 138 | 1 981 → 2 727 | +38% | 84 → 219 | 77% | 0.08 |
| Инструмент: song/lyrics/music generator | 59 | 1 330 → 758 | -43% | 141 → 128 | 21% | 0.17 |
| Off-topic (video/image/NSFW/celebrity voice) | 7 | 37 → 49 | +32% | 5 → 25 | 1% | 0.51 |
| Инфо-контент (списки песен, поздравления, цитаты, блог) | 33 | 93 → 18 | -81% | 15 → 2 | 1% | 0.09 |
| Бренд | 1 | 0 → 0 | — | 0 → 0 | 0% | 0.00 |

### 7.3 Архитектура
| URL-паттерн | Стр. | Стр. с трафиком | Трафик prev → cur | Value cur, $ |
|---|---:|---:|---:|---:|
| `/vocal-remover` | 1 | 1 | 608 → 1 208 | 71 |
| `/Tools` | 2 | 1 | 1 → 517 | 21 |
| `/{lang}/audio-converter/*` | 37 | 18 | 96 → 264 | 13 |
| `/{lang}/suno` | 8 | 4 | 448 → 251 | 8 |
| `/` | 1 | 1 | 27 → 233 | 35 |
| `/{lang}/audio-converter` | 6 | 6 | 64 → 192 | 13 |
| `/{lang}/generate` | 1 | 1 | 0 → 85 | 10 |
| `/{lang}` | 7 | 2 | 41 → 67 | 4 |
| `/ai-ringtone-generator` | 1 | 1 | 110 → 64 | 1 |
| `/{lang}/bpm-finder` | 7 | 3 | 31 → 57 | 1 |
| `/ai-mastering` | 1 | 1 | 12 → 53 | 57 |
| `/{lang}/voice-change` | 3 | 2 | 31 → 50 | 2 |
| `/photo-video` | 1 | 1 | 36 → 40 | 24 |
| `/{lang}/ai-mastering` | 3 | 3 | 8 → 37 | 13 |
| `/ai-song-generator` | 1 | 1 | 34 → 30 | 35 |

- **`/{lang}/{tool}` на 17 языках:** es, ru, id, tr, vi, fr, de, nl, th, ja, pt, zh-Hant, ar, pl, hi, ko. Плюс комбинаторная матрица `/{lang}/audio-converter/{a}-to-{b}-converter` (37 URL).
- **`/{lang}/suno`, 8 URL**, и блог про цены и бесплатный план Suno: ловят брендовый трафик конкурента («suno ai» 14k/мес, поз. 14). `blog/suno-ai-pricing-plans-2026` получил 14 AI-цитирований. Это подтверждает, что AI-ответы на вопросы о ценах цитируют сторонние страницы.
- Подарочных и occasion-страниц нет совсем. Трафик ушёл на vocal remover (1 208 + 517 визитов, top kw с гео IL и AE).

### 7.4 Топ-15 по трафику
| # | URL | Бакет | Трафик | Value, $ | Top keyword | Поз. | Объём | Страна |
|---:|---|---|---:|---:|---|---:|---:|---|
| 1 | `/vocal-remover` | tool_audio | 1 208 | 71 | vocal remover | 3 | 3 100 | IL |
| 2 | `/Tools` | tool_audio | 517 | 21 | vocal remover | 4 | 4 300 | AE |
| 3 | `/` | tool_song | 233 | 35 | music maker | 4 | 1 600 | CA |
| 4 | `/ru/suno` | tool_song | 141 | 5 | suno ai | 14 | 14 000 | KZ |
| 5 | `/pl/generate` | tool_song | 85 | 10 | darmowy generator piosenek ai | 7 | 900 | PL |
| 6 | `/es/audio-converter` | tool_audio | 77 | 3 | online audio converter | 1 | 70 | Uruguay |
| 7 | `/vi/audio-converter/mp3-to-wav-converter` | tool_audio | 75 | 1 | chuyển mp3 sang wav | 7 | 800 | VN |
| 8 | `/id/suno` | tool_song | 74 | 1 | suno ai indonesia free | 6 | 1 400 | ID |
| 9 | `/pt/audio-converter` | tool_audio | 72 | 2 | online áudio converter | 3 | 2 200 | BR |
| 10 | `/id` | tool_song | 64 | 1 | ai buat lagu | 10 | 2 900 | ID |
| 11 | `/ai-ringtone-generator` | tool_audio | 64 | 1 | ai ringtone maker | 1 | 200 | IN |
| 12 | `/ai-mastering` | tool_audio | 53 | 57 | free mastering online | 3 | 90 | ZA |
| 13 | `/tr/audio-converter/ogg-to-mp3-converter` | tool_audio | 51 | 1 | ogg to mp3 converter | 1 | 100 | TR |
| 14 | `/zh-Hant/audio-converter/aac-to-mp3-converter` | tool_audio | 42 | 6 | aac轉檔 | 3 | 20 | TW |
| 15 | `/photo-video` | offtopic | 40 | 24 | photo video maker with music online free | 6 | 500 | US |

### 7.5 Топ-15 по traffic value
| # | URL | Бакет | Трафик | Value, $ | Top keyword | Поз. | Объём | Страна |
|---:|---|---|---:|---:|---|---:|---:|---|
| 1 | `/vocal-remover` | tool_audio | 1 208 | 71 | vocal remover | 3 | 3 100 | IL |
| 2 | `/ai-mastering` | tool_audio | 53 | 57 | free mastering online | 3 | 90 | ZA |
| 3 | `/` | tool_song | 233 | 35 | music maker | 4 | 1 600 | CA |
| 4 | `/ai-song-generator` | tool_song | 30 | 35 | best free ai song generator | 4 | 400 | US |
| 5 | `/photo-video` | offtopic | 40 | 24 | photo video maker with music online free | 6 | 500 | US |
| 6 | `/Tools` | tool_audio | 517 | 21 | vocal remover | 4 | 4 300 | AE |
| 7 | `/blog/suno-ai-pricing-plans-2026` | tool_song | 24 | 20 | suno ai pricing | 11 | 250 | US |
| 8 | `/ai-sample-generator` | tool_audio | 19 | 16 | ai sample generator | 9 | 150 | US |
| 9 | `/es/ai-mastering` | tool_audio | 21 | 12 | masterizar audio online gratis | 9 | 350 | MX |
| 10 | `/pl/generate` | tool_song | 85 | 10 | darmowy generator piosenek ai | 7 | 900 | PL |
| 11 | `/ja/audio-converter` | tool_audio | 28 | 8 | オンラインオーディオコンバーター | 4 | 250 | JP |
| 12 | `/use-cases/poem-to-song-generator?prompt=Create%20romantic%20poem%20ball…` | tool_song | 4 | 6 | ballad generator | 5 | 30 | US |
| 13 | `/zh-Hant/audio-converter/aac-to-mp3-converter` | tool_audio | 42 | 6 | aac轉檔 | 3 | 20 | TW |
| 14 | `/ru/suno` | tool_song | 141 | 5 | suno ai | 14 | 14 000 | KZ |
| 15 | `/tools` | tool_song | 18 | 4 | generate ai music | 2 | 30 | CA |

### 7.6 Winners / losers
| URL | Статус | Трафик prev → cur | Top keyword (поз., страна) |
|---|---|---:|---|
| `/vocal-remover` | — | 608 → 1 208 | vocal remover (3, IL) |
| `/Tools` | — | 1 → 517 | vocal remover (4, AE) |
| `/` | — | 27 → 233 | music maker (4, CA) |
| `/pl/generate` | New | 0 → 85 | darmowy generator piosenek ai (7, PL) |
| `/vi/audio-converter/mp3-to-wav-converter` | New | 0 → 75 | chuyển mp3 sang wav (7, VN) |
| `/pt/audio-converter` | — | 3 → 72 | online áudio converter (3, BR) |
| `/es/audio-converter` | — | 19 → 77 | online audio converter (1, Uruguay) |
| **Потери** | | | |
| `/vi/ai-vocal-remover` | — | 455 → 15 | voice remover (4, VN) |
| `/ja/piano-music-maker` | Lost | 324 → 0 | ピアノ 無料 (1, JP) |
| `/ai-vocal-remover` | — | 330 → 17 | vocalremover.or (1, US) |
| `/ar/suno` | — | 226 → 25 | سونو (5, OM) |
| `/tr/ai-lyrics-generator` | Lost | 162 → 0 | şarkı yapan yapay zeka (2, TR) |
| `/id/ai-music-maker` | Lost | 79 → 0 | buat musik ai (11, ID) |
| `/ai-music-generator-with-vocals` | Lost | 74 → 0 | ai music generator free (2, BR) |

New-страниц: 85 (текущий трафик 519, $67); Lost-страниц: 67 (потерянный трафик 983, $96).

### 7.7 AI-видимость
Всего упоминаний в AI-ответах: **18** на 4 страницах (AI Overviews 5, AI Mode 3, ChatGPT 0, Gemini 0, Perplexity 10, Copilot 0, Grok 0).

| URL | Всего | AIO | AI Mode | ChatGPT | Gemini | Perplexity | Copilot | Top keyword |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| `/blog/suno-ai-pricing-plans-2026` | 14 | 3 | 3 | 0 | 0 | 8 | 0 | suno ai pricing |
| `/id/suno` | 2 | 2 | 0 | 0 | 0 | 0 | 0 | suno ai indonesia free |
| `/pt/audio-converter` | 1 | 0 | 0 | 0 | 0 | 1 | 0 | online áudio converter |
| `/nl/mashup` | 1 | 0 | 0 | 0 | 0 | 1 | 0 | mashup maken |

### 7.8 География
Страна top keyword → доля текущего трафика: IL 34% (1 208), AE 15% (517), CA 7% (254), ID 7% (243), US 6% (203), VN 4% (153), KZ 4% (141)

---

## 8. Россия: pesinka.ru и everyonesing.ru

### pesinka.ru
**Итоги:** страниц в выгрузке 9 (с текущим трафиком 8); статусы: Unchanged 7, New 2

| Метрика | Previous | Current | Δ |
|---|---:|---:|---:|
| Органический трафик, визитов/мес | 225 | 148 | -34% |
| Traffic value, $ | 0 | 0 | — |
| Главная: трафик (доля) | | 0 (0%) | |
| Бренд (top keyword = бренд): трафик / value | 0 / $0 | 0 (0%) / $0 (0%) | — |
| Небрендовый трафик / value | 225 / $0 | 148 / $0 | -34% |

| URL-паттерн | Стр. | Стр. с трафиком | Трафик prev → cur | Value cur, $ |
|---|---:|---:|---:|---:|
| `/podarok/*` | 5 | 4 | 174 → 105 | 0 |
| `/povod/*` | 2 | 2 | 47 → 40 | 0 |
| `/Идеи` | 1 | 1 | 4 → 2 | 0 |
| `/komu/*` | 1 | 1 | 0 → 1 | 0 |

| # | URL | Бакет | Трафик | Value, $ | Top keyword | Поз. | Объём | Страна |
|---:|---|---|---:|---:|---|---:|---:|---|
| 1 | `/podarok/muzhu-na-den-rozhdeniya` | gift | 91 | 0 | трогательная песня мужу на день рождения | 5 | 600 | RU |
| 2 | `/povod/godovschina` | gift | 32 | 0 | песня на годовщину свадьбы | 7 | 150 | RU |
| 3 | `/podarok/pape-na-den-rozhdeniya` | gift | 8 | 0 | песня папе на день рождения | 3 | 40 | RU |
| 4 | `/povod/svadba` | gift | 8 | 0 | песня в подарок на свадьбу | 2 | 30 | RU |
| 5 | `/podarok/muzhu-na-godovschinu` | gift | 5 | 0 | песня на годовщину свадьбы мужу | 6 | 80 | RU |
| 6 | `/%D0%98%D0%B4%D0%B5%D0%B8` | info | 2 | 0 | песня папе на день рождения | 4 | 20 | RU |
| 7 | `/komu/muzhu` | gift | 1 | 0 | песня для мужа на день рождения | 1 | 30 | RU |
| 8 | `/podarok/mame-na-den-rozhdeniya` | gift | 1 | 0 | трогательная песня маме на день рождения от сына | 6 | 20 | RU |

| URL | Статус | Трафик prev → cur | Top keyword (поз., страна) |
|---|---|---:|---|
| `/povod/svadba` | — | 2 → 8 | песня в подарок на свадьбу (2, RU) |
| `/podarok/pape-na-den-rozhdeniya` | — | 6 → 8 | песня папе на день рождения (3, RU) |
| `/komu/muzhu` | New | 0 → 1 | песня для мужа на день рождения (1, RU) |
| `/podarok/mame-na-den-rozhdeniya` | New | 0 → 1 | трогательная песня маме на день рождения от сына (6, RU) |
| **Потери** | | | |
| `/podarok/muzhu-na-den-rozhdeniya` | — | 160 → 91 | трогательная песня мужу на день рождения (5, RU) |
| `/povod/godovschina` | — | 45 → 32 | песня на годовщину свадьбы (7, RU) |
| `/podarok/muzhu-na-godovschinu` | — | 8 → 5 | песня на годовщину свадьбы мужу (6, RU) |
| `/%D0%98%D0%B4%D0%B5%D0%B8` | — | 4 → 2 | песня папе на день рождения (4, RU) |

New-страниц: 2 (текущий трафик 2, $0); Lost-страниц: 0 (потерянный трафик 0, $0).

### everyonesing.ru
**Итоги:** страниц в выгрузке 1 (с текущим трафиком 1); статусы: Unchanged 1

| Метрика | Previous | Current | Δ |
|---|---:|---:|---:|
| Органический трафик, визитов/мес | 20 | 16 | -20% |
| Traffic value, $ | 0 | 0 | — |
| Главная: трафик (доля) | | 16 (100%) | |
| Бренд (top keyword = бренд): трафик / value | 0 / $0 | 0 (0%) / $0 (0%) | — |
| Небрендовый трафик / value | 20 / $0 | 16 / $0 | -20% |

| # | URL | Бакет | Трафик | Value, $ | Top keyword | Поз. | Объём | Страна |
|---:|---|---|---:|---:|---|---:|---:|---|
| 1 | `/` | gift | 16 | 0 | написать песню на заказ | 3 | 100 | RU |

**Выводы по РФ:**
- Органика в RU-нише зачаточная: два сайта суммарно ≈ 160 визитов/мес. AI-цитирований ноль. Traffic value = $0, потому что у Ahrefs нет CPC по этим запросам. Конкуренции в SEO почти нет.
- **У pesinka.ru самая чистая подарочная архитектура из всех восьми доменов**, это матрица «кому × повод»:
  - `/podarok/{komu}-na-{povod}`: muzhu-na-den-rozhdeniya, pape-na-den-rozhdeniya, mame-na-den-rozhdeniya, zhene-na-den-rozhdeniya, muzhu-na-godovschinu;
  - `/povod/{povod}`: godovschina, svadba;
  - `/komu/{komu}`: muzhu;
  - страница идей `/Идеи` (кириллический URL — плохая практика).
- 100% трафика сайта — подарочный интент. Ключи: «трогательная песня мужу на день рождения» (600/мес, поз. 5, 91 визит), «песня на годовщину свадьбы» (150, поз. 7), «песня в подарок на свадьбу» (30, поз. 2), «песня для мужа на день рождения» (30, поз. 1), «песня папе на день рождения» (40, поз. 3).
- Трафик pesinka просел на 34%, в основном главная страница кластера «мужу на ДР» (160 → 91). Позиции 5–7 нестабильны, сайт молодой.
- everyonesing.ru — одна главная по «написать песню на заказ» / «песни на заказ» (70–100/мес, поз. 2–3), при этом 569 RD. Ссылки есть, страниц нет.
- Плюс у Wondera UGC-страница «с днем рождения олеся» (1 100/мес) получала 118 визитов. В RU тоже есть спрос на именные поздравительные песни, и он больше, чем на «песню на заказ».
- Вывод: в RU можно занять нишу малыми силами, если сразу построить матрицу «кому × повод» (pesinka показывает рабочий шаблон) и добавить страницы «песня с именем {Имя}». Абсолютные объёмы маленькие, это скорее дешёвый дополнительный канал, чем основной.

---

## 9. Кросс-доменный синтез

### 9.1 Рейтинг по коммерческому (небрендовому gift) трафику и value

| # | Домен | Gift-коммерция: трафик | Value, $ | $/визит | Комментарий |
|---:|---|---:|---:|---:|---|
| 1 | giftsong.ai | 1 225 (312 без главной) | 1 976 (472 без главной) | 1.61 | Главная по аномальному запросу 1.9k; реальное ядро — /pricing, /gifts/, /relation/, /create |
| 2 | songfinch.com | 242 (+ коммерческие страницы с брендовым top kw: /store, /products/personalized-song, /song-builder ≈ 160) | 606 | 2.50 | how-it-works (custom songs), LP get. (custom song gift) |
| 3 | pesinka.ru | 146 | 0 (нет CPC) | — | Вся органика — подарочная матрица RU |
| 4 | songlorious.com | 34 | 81 | 2.38 | /landing-pages/anniversary поз. 1 |
| 5 | everyonesing.ru | 16 | 0 | — | «песня на заказ» |
| 6 | sendfame.com | 10 | 2 | 0.20 | /happy-birthday-music |
| 7–8 | wondera.ai, musicmake.ai | 0 | 0 | — | Подарочного коммерческого трафика нет |

Небрендовый коммерческий gift-трафик всей EN-ниши в органике — ~0.6–1.5k визитов в месяц (facts.md §3). Head-термины (custom song gift, personalized song gift) держит Songfinch, но даже у него небрендовая коммерция — ≈ 400 визитов. **Ниша в органике не занята, её никто системно не окучивает.** Спрос из прошлого исследования (≈ 15k/мес gift-intent в US) распределён по SERP, где ранжируются маркетплейсы (Etsy и подобные), медиа и Songfinch. В этих выгрузках этот спрос почти не виден.

### 9.2 Какой контент приносит gift-трафик, а какой тщеславный

| Тип контента | Где | Трафик | $/визит | Вердикт |
|---|---|---:|---:|---|
| Коммерческие LP: pricing / create / how-it-works / gift-a-song / occasion-LP | songfinch, giftsong, songlorious | ≈ 750 (без главной giftsong) | 1.6–3.0 | **Работает.** Быстро растёт (×2–×15 за период), выходит в топ-3 по точным ключам |
| `/relation/{who}`, `/occasions/{occasion}` (подарочные) | giftsong, pesinka | ≈ 200 | 2–3 (EN) | **Работает**, но слабо дожато (поз. 4–7) |
| Списки песен «songs for {relation}» | songfinch (515), wondera (≈ 300) | ≈ 800 | 0.01–0.15 | Промежуточный интент. Трафик есть, коммерции почти нет. Полезен как вход с CTA «создай свою песню для сестры» |
| Поздравления, цитаты, синонимы, open-ended блог | giftsong /article, sendfame /happy-birthday, blog | ≈ 1 100 | 0.01–0.05 | **Тщеславный трафик** (PH, NG, PK, IN), волатильный |
| Генераторы песен и лирики | giftsong /ai, sendfame, wondera, musicmake | ≈ 1 400 | 0.1–0.3 | Высокая конкуренция с Suno/Udio, низкая конверсия в подарок. Только как вспомогательный вход |
| Аудио-утилиты | wondera, musicmake | ≈ 4 900 | 0.08–0.2 | Не наша аудитория |
| NSFW / video / image | sendfame | ≈ 2 000 | 0.26 | Брендовый риск, не копировать |
| UGC-страницы песен и профили артистов | songfinch, wondera | ≈ 600 | ≈ 0.1 | Профили бесполезны. Публичные страницы песен иногда ловят «custom rock», «happy birthday {name}» |
| Брендовые страницы о компании (/about, /faq, /reviews, /pricing) | все | — | — | Главный источник AI-цитирований |

### 9.3 AI-видимость (кто цитируется)

| Домен | Упоминаний | Страниц | Что цитируется |
|---|---:|---:|---|
| songfinch.com | 115 | 20 | Главная (31; AI Mode 16), get./custom-songs (11), /products/personalized-song (ChatGPT 7), how-it-works, support про цены и сроки |
| songlorious.com | 47 | 8 | Главная (23), /about (10), /songlorious-business (5), custom-songs-vs-ai-music (3) |
| giftsong.ai | 35 | 15 | how-much-do-custom-songs-cost (8), best-custom-song-company (3), статьи-идеи (в основном Perplexity, 16) |
| sendfame.com | 35 | 10 | Главная (9), /happy-birthday/aunt (Perplexity 8), cameo-alternatives |
| musicmake.ai | 18 | 4 | blog/suno-ai-pricing-plans-2026 (14) |
| wondera.ai | 3 | 3 | — |
| pesinka.ru, everyonesing.ru | 0 | 0 | — |

Закономерность: AI-ассистенты цитируют страницы с прямым фактическим ответом. Это цена и что входит, сроки доставки, how it works, сравнения («best custom song service», «custom songs vs AI music», «X alternatives»), страницы «о компании». Массовая программатика и тщеславный блог почти не цитируются.

### 9.4 Плейбук для нового игрока (EN: US/GB/CA/AU)

**Что строить первым, по приоритету:**

1. **Ядро коммерческих страниц, по одной на интент, с явными фактами (цена, срок, что получит получатель, пример gift page):**
   - `/` — custom song gift / personalized song gift (head; там Songfinch, KD 52–68, долгая игра);
   - `/pricing` — song gift, how much does a custom song cost (у giftsong /pricing 5 → 76 и поз. 2 по «song gift»);
   - `/how-it-works` — custom songs (450/мес; у Songfinch поз. 2 и 155 визитов);
   - `/create` — custom song gift, write a song for me (600/мес; у Songfinch поз. 2 на продуктовой странице).
2. **Матрица occasion × relation**, тот же шаблон, что у pesinka и giftsong. Чистые URL: `/occasions/{birthday|anniversary|wedding|mothers-day|fathers-day|valentines-day|graduation|retirement|memorial}`, `/for/{wife|husband|mom|dad|sister|daughter|son|grandma|best-friend|boyfriend|girlfriend}`, затем пересечения `/for/{who}/{occasion}` для пар с явным спросом. Ключи, видимые в выгрузках:
   - personalized songs for husband — 90, поз. 4 у giftsong;
   - song for my wife — 60, поз. 5;
   - create a song for a loved one — 40, поз. 2;
   - custom song for anniversary — 30, у songlorious поз. 1 с узкой LP;
   - custom country song — 10;
   - personalised music gifts (GB) — 150, поз. 1 у giftsong;
   - personalised song gift (GB) — 250, поз. 6.

   Писать в двух вариантах написания: personalised для GB/AU, personalized для US/CA.
3. **Кластер «song with name»** (KD 0–12 из прошлого исследования): `/birthday-song-with-name`, затем программатика `/birthday-song/{name}` по топ-200 именам US/GB. Подтверждение спроса в этих выгрузках:
   - birthday song with name — 250, у giftsong поз. 7, слабая страница;
   - happy birthday song with name (DE);
   - name song maker — 100, sendfame поз. 5;
   - happy birthday song custom — 40;
   - UGC Wondera ранжируется по «happy birthday julia / maurice / mary ann» и «feliz cumpleaños aime» (5.1k).

   Важно: каждая страница должна давать реальный аудио-пример с именем, а не открытку. У SendFame /happy-birthday/{name} собирает «images»-трафик из PK/IN с value ≈ 0.
4. **Публичные gift pages как SEO-актив** (по аналогии с Songfinch `/stories/`, Wondera `/song/info`):
   - индексировать только с явного согласия (opt-in) и только «витринные» примеры: никаких персональных данных, текст переписан как пример;
   - noindex по умолчанию для личных страниц;
   - перелинковка из occasion- и relation-страниц.

   У Songfinch новая story-страница уже собирает «custom rock» на 2-й позиции.
5. **Страницы под AI-ответы и сравнения:**
   - how much does a custom song cost (50, 8 AI-цитирований у giftsong);
   - best custom song service (150; Songfinch /lp был на поз. 2, но LP потерял 73 → 6);
   - custom song vs AI song (у Songlorious цитируется);
   - `/vs/songfinch`, `/songfinch-alternatives` (giftsong сделал /vs/, трафика пока нет, но брендовый спрос на Songfinch 3.1k и падает);
   - /faq, /about с фактами.

   Формат: короткий прямой ответ, таблица цен и сроков, schema FAQ/Product.
6. **Вспомогательные инструменты** — только узкие, со связью с подарком: `/ai-love-song-generator` (ai love song generator 150, make a love song 100, love song generator 60 — у giftsong поз. 3–5), `/ai-birthday-song-generator` (70). Выход каждого инструмента — та же gift page. Общие «AI music generator» не трогать: там Suno, Udio и десятки клонов, а value у них $0.1 за визит.
7. **Контент-хаб «songs for {relation/occasion}»** — второй эшелон, после коммерческих страниц. Позиции Songfinch там 8–12, объёмы 250–1 300 (sister songs 1.1k, daughter songs 1.3k, songs about having a baby 900, songs for sons 700). Каждая статья должна заканчиваться CTA «или создайте песню, которой нет ни в одном плейлисте».

**Что НЕ копировать:**
- NSFW/video/image-генераторы ради трафика (SendFame): бренд-риск, трафик не конвертируется в подарки, и при этом −42% за период.
- Массовую мультиязычную программатику «{lang}/{slug}» на тысячи URL (Wondera): ≈ 3 визита на URL, 274 Lost-страницы за период, нет AI-цитирований, дубли www/non-www.
- Аудио-утилиты и конвертеры (MusicMake): трафик из IL, AE, ID, VN, value около нуля.
- Широкий блог про «синонимы happy birthday», цитаты для тренеров, тексты «thinking of you» (giftsong): трафик из PH и NG, $0.01–0.05 за визит, нестабилен (−90% на отдельных статьях).
- Профили артистов (Songfinch, Songlorious): бессмысленны для AI-продукта.
- Утечку платных LP с utm в индекс (`get.songfinch.com/...?utm_...`) и кириллические URL (`pesinka.ru/Идеи`).
- Ранние языковые папки без контента (giftsong /de/, /es/: 5 URL, 3 визита). Сначала EN-ядро, потом локализация. *Сверка с 05-decisions:* i18n-каркас с первого дня допустим и принят; не публиковать пустые языковые папки — 1–2 доп. языка открывать только с контентом, после выгрузок с местными seed.
- Ставку на одну главную по «how to create a personalized song gift» (giftsong): запрос подозрителен, на нём не строить прогнозы.

### 9.5 Россия: рекомендации (фаза 2: RU — отдельный whitelabel по 05-decisions)
- Конкуренции в органике почти нет: pesinka ≈ 150, everyonesing ≈ 16 визитов в месяц.
- Строить RU-версию по матрице pesinka (`/podarok/{komu}-na-{povod}`, `/povod/*`, `/komu/*`) латиницей. Добавить кластер «песня с именем {Имя}» / «с днём рождения {Имя} песня»: UGC Wondera на одном имени собирала 118 визитов, больше, чем весь pesinka.
- Head-запросы: «песня на заказ» / «написать песню на заказ» (70–100), «песня в подарок на свадьбу», «песня на годовщину свадьбы» (150), «трогательная песня мужу на день рождения» (600).
- Ожидания реалистичные: сотни визитов в месяц, а не тысячи. Проверка спроса через Wordstat — открытый вопрос фазы 2 (до инвестиций в RU-whitelabel), ведётся как Q11 в 05-decisions.md §6.

---

## 10. Ключевые цифры одной строкой
- Органика всей EN-ниши ≈ 20k/мес; подарочной небрендовой коммерции из них ≈ 0.6–1.5k.
- Songfinch: 81% трафика и 94% value — бренд; главная −15%.
- Растут коммерческие LP: Songfinch get. ×6, giftsong /pricing ×15, songlorious /landing-pages/anniversary 1 → 21 (поз. 1).
- AI-цитирования достаются страницам с ценами, how-it-works, сравнениями и about/faq. Лидеры — Songfinch (115) и Songlorious (47); программатика Wondera получила 3.
- RU: pesinka 148 визитов, everyonesing 16; ниша пустая, но маленькая.
