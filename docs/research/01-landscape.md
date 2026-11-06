# 01. Карта рынка и разбор ohappy.ru

Дата: 2026-11-05. Объединяет два ранних документа (первый проход по рынку). Цены и факты сверены с [facts.md](facts.md) и [appendix/competitors-teardown.md](appendix/competitors-teardown.md).

## 1. Референс: ohappy.ru

Сервис персональных песен-поздравлений по короткой истории. Собран автором поста за 17 минут в Claude.

**Флоу.** Форма из 5 шагов (на лендинге подана как 3):
1. Кому и зачем: имя, роль (12 вариантов: мама, подруга, коллега, партнёр и др.), повод.
2. История: пара тёплых деталей (как познакомились, что любит человек, любимая фраза).
3. Звук: 12 жанров (от поп и баллады до рэпа, шансона и диско 80-х), настроение, голос м/ж, язык RU или EN.
4. Текст генерируется за 10–20 с, его можно отредактировать.
5. Запись 1–3 мин. На выходе 2 версии песни и страница-подарок (обложка, плеер, текст) со ссылкой для мессенджеров.

**Поводы:** день рождения, юбилей, годовщина, свадьба, признание, благодарность, Новый год, извинение, «просто так».

**Монетизация:**

| Тариф | Цена | Что даёт |
|---|---|---|
| Послушать | 0 ₽ | текст, 2 версии, страница-подарок, ссылка |
| Стандарт | 290 ₽ | MP3 |
| Супер-качество | 590 ₽ | «новейшая модель Suno», MP3 320 kbps |

**Доверие и прочее:**
- Без регистрации и подписок. Заявлено «1 800+ песен».
- Отзывы дословно совпадают с pesinka.ru, хотя продавцы разные.
- ИП в Санкт-Петербурге, оферты нет, почта на yandex.com.
- Кросс-сейл: песня от Деда Мороза, офлайн-мастерская, Дед Мороз на дом.
- В планах: стихи и поздравления от персонажей.

**Что забрать:**
- Ценность до оплаты: человек слышит песню с именем.
- Страница с песней как формат вручения и вирусный канал (у нас — страница вручения, D16).
- Редактируемый текст и 2 версии.
- Анкета через отношения и повод: дарителю не нужно уметь писать промпт.

**Чего не повторять:**
- Пустой пейвол: главную ценность отдают бесплатно.
- Генерация через Suno: юридический риск, см. [facts.md §4](facts.md).
- Цена $3–7: в англоязычном AI-сегменте нормальная цена $20–40.

Наши решения по этим пунктам — в [05-decisions.md](05-decisions.md) (D3, D8).

## 2. Сегменты мирового рынка

### A. Живые артисты (премиум, $179–395)
- Songfinch, Songlorious, Songs With You, Custom Song Gift ($99, гибрид), Unique Song.
- Нишевые: PrayerSong и HosannaSong (религия).
- Фрилансеры: Fiverr, Comeup (FR), Kmong (KR), CherishX (IN), $5–200.

### B. AI-песня как подарок (прямые конкуренты, $2–79)
- GiftSong.ai, CustomSong, BeatJar, GiftYourSong, MakeCustomSongs, Hitou, Birthdai.
- Демпинг: Gift A Song, Songive, Gift Your Melody.
- Ниши: Pet Anthemz (питомцы).
- Длинный хвост: Tuneliq, SongReels, Porizo, SongLoom, TuneTribute, WrapASong, Songline.gift, LoveTunesAI, Magic AI Song, Birthday Beats (iOS), Luvtune, Tetatune, Song Oven.

Цены и метрики — в [facts.md §2](facts.md), разбор — в [03-competitors.md](03-competitors.md).

### C. Универсальные AI-генераторы с SEO-страницами «birthday song»
Suno, Wondera, Freebeat, MusicCreator, Somio, MusicMake, Musicful, Neume, Insmelo, ImagineArt, Soundverse.

Бесплатно или по подписке. Делают программатик-SEO на 10+ языках и забирают трафик вида «birthday song with name», но подарочной упаковки у них нет.

### D. Заменители
- Suno и Udio напрямую (DIY).
- Cameo (видео от звезды).
- Музыкальные e-card и singing telegrams.
- Генераторы «Happy Birthday + имя».

### E. Локальные рынки
- **RU:** продажи и доставка уходят в мессенджеры. WhatsApp заблокирован, Telegram де-факто работает только через VPN, растёт MAX ([facts §8](facts.md)). Рынок переполнен клонами. ohappy, pesinka (790 ₽), everyonesing, lyricgift (дарк-паттерн с автоподпиской), «Создать песню».рф (7 990 ₽ с видео), студии с живым вокалом (pesnyanazakaz.ru, glavstudio.ru).
- **DE:** personalisierter-song.de — ~$198k за всё время (TrustMRR). Есть работающий локальный бизнес.
- **PL, PT, DE, UK:** сильнейшие рынки Flippa-кейса.
- **FR, KR:** рынок держат фрилансеры (Comeup, Kmong).
- **IN:** CherishX (₹250–1 799, живой вокал + видео); кампания Cadbury #MyBirthdaySong.
- **CN:** iOS-приложение «Happy 生日歌曲 AI». WeChat-мини-программ не нашли.
- **Остальные языки:** выдачу держат машинные переводы сегмента C. Это проверяем выгрузками (Q3 в [05-decisions.md](05-decisions.md)).

## 3. Какие гипотезы первого прохода проверены

| Гипотеза | Итог |
|---|---|
| Спрос на подарочные песни есть | ✅ Подтверждено: +23% год к году в US, Songfinch и Flippa-кейс ([02](02-seo-demand.md), [facts](facts.md)) |
| Ценовой коридор AI-подарка $7–30 | ❌ Уточнено: массовый AI-сегмент $20–40, ниже $7 только демпинг ([facts §2](facts.md)) |
| Отличаться нужно упаковкой подарка, а не генерацией | ✅ Принято как позиционирование C ([05](05-decisions.md) D1) |
| Есть окно в неанглоязычных рынках | ⏳ Вероятно: personalisierter-song.de, Flippa. Проверяем выгрузками (Q3) |
| Спрос сезонный | ✅ Пики в мае–июне и декабре–феврале, 2.9× ([02](02-seo-demand.md)) |
| Главный риск — легальность генерации | ⏳ Частично: D8 задаёт рамку (только pay-per-use модели, Suno — по партнёрскому договору), условия использования выбранной модели проверяем в Q2 |

## Источники
- [ohappy.ru](https://ohappy.ru)
- [Songfinch Instant](https://songfinch.com/lp/instant), [Rolling Stone о выручке Songfinch](https://www.rollingstone.com/pro/news/the-weeknd-songfinch-custom-gift-music-1196163/), [MBW о раунде $17M](https://musicbusinessworldwide.com/the-weeknd-backed-personalized-song-creation-firm-songfinch-raises-17m)
- [Songlorious](https://www.songlorious.com/about), [Tuneliq: сравнение](https://tuneliq.com/learn/best-custom-song-gift-apps), [Hitou: сравнение](https://hitou.site/best-ai-song-generator-for-gifts), [GiftSong](https://www.giftsong.ai)
- [GiftYourSong](https://giftyoursong.com), [Custom Song Gift в Trustpilot](https://ca.trustpilot.com/review/customsonggift.com)
- [TrustMRR: LoveTunesAI](https://trustmrr.com/startup/lovetunesai), [TrustMRR: AI-стартапы](https://trustmrr.com/category/ai)
- [Pesinka](https://pesinka.ru/podarok/pesnya-na-zakaz), [LyricGift](https://lyricgift.ru/), [Everyonesing](https://everyonesing.ru/), [tproger: топ-10 нейросетей для песен-поздравлений](https://tproger.ru/articles/nejroseti-dlya-sozdaniya-pesen-pozdravlenij-top-10-servisov-v-202)
- [CherishX](https://cherishx.com/experience/5579/pune/personalized-birthday-song), [Kmong](https://kmong.com/gig/562062), [Comeup](https://comeup.com/fr/service/524017/creer-votre-chanson-personnalisee-par-ia-pour-tout-evenement)
