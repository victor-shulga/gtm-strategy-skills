---
name: gtm-stage-diagnostic
description: Step 2 of the GTM flow and CHECKPOINT 1. Diagnose an IT agency growth stage 0-5 from the Company Snapshot using the agency-path model, plus the Sales-Market-Fit lens (L, Cr, $, # — which profit driver is leaking), and output the 3 discovery questions to confirm the stage with the client. Use when the user asks яка стадія агенції, діагностуй стадію, stage diagnosis, or right after intake. Stage drives the depth of every later step. Writes to Notion in Ukrainian.
argument-hint: "(reads the Company Snapshot from the client's Notion page)"
---

# 02 · Stage Diagnostic — стадія + SMF (GATE 1)

Другий крок і **перший чекпоінт**. Визнач стадію агенції 0–5 і де в економіці клієнта діра.
Стадія керує глибиною всіх наступних кроків («чим раніше стадія — тим менше всього»).

Прочитай `${CLAUDE_PLUGIN_ROOT}/reference/agency-stages.md` (розділи 1–5). Вхід — Company Snapshot
з кроку 1 (з Notion або з контексту).

## Процес

1. **Стадія (cold-audit гіпотеза).** Зістав проксі-сигнали зі Snapshot з таблицею стадій і
   cold-audit сигналами (розділ 1 довідника). Визнач **найімовірнішу стадію 0–5** і дай
   **рівень впевненості: low / med / high** з 2–4 причинами «чому саме ця стадія».
   - Якщо сигнали суперечливі — назви дві сусідні стадії й що їх розрізнить.
   - ARR прямо не видно → не вигадуй цифру; працюй із проксі (presence, кейси, команда, канали, офери).
   - **Склад команди з LinkedIn (секція 11 Snapshot) — головний проксі стадії:** 0 видимих
     Sales/Marketing/SDR/AM = founder-led → Стадія 0-1; поява окремих біздев-ролей → 2; керівники
     функцій (Head of Sales/Marketing/CS) → 3-4; C-level з розділеними функціями (CRO/CMO/CCO) + лідери практик → 5. Це перевершує claim'и сайту: якщо сайт каже «20+
     років / 200+ проєктів», а в LinkedIn 1-2 особи й сутність нова — стадія за **реальною командою**,
     а claim познач як «особистий досвід founder'а / інша юрособа».
   - **Headcount як проксі (весь штат, не тільки BizDev):** до 5 → 0 · 5–15 → 1 · 15–45 → 2 ·
     45–140 → 3 · 140–400 → 4 · 400+ → 5. Перевірка через ревеню: **headcount × $70K ≈ ARR**
     (коридор $60–90K на людину для EE IT-сервісу). Якщо названий ARR і headcount дають різні
     стадії — бери нижчу і назви розбіжність у припущеннях: сильно вище $90K/людину = US/UK rates
     або продуктова частка, сильно нижче $60K = бенч / субпідряд / дешевий аутстаф.
     ⚠️ Тисячі людей — це Стадія 5 (портфель практик), а не «поза моделлю». Але спершу перевір,
     чи правильна LinkedIn-сутність (той самий бренд/slug) — глобальні групи роздувають headcount.
   - **Тренд росту (6м/1р/2р) = momentum:** hiring spike → активне масштабування (можна вмикати більше
     каналів); flat/decline → обережність із інвестиціями. **Median tenure** = стабільність команди
     (низький tenure + швидкий ріст = молода орг; високий tenure = зрілість).
   - **Tie-breaker Стадія 0 ↔ 1 (часта помилка):** presence-артефакти (лендінг, лого) **НЕ** підвищують
     стадію — лендінг буває й на 0. **6+ розмитих послуг = «все для всіх» (0)**, а не свідомі 2-4 тест-офери
     з метриками (1). Вирішують **traction + команда**: Стадія 1 = 1-2 стабільні платні клієнти + 2-3
     активні канали + ARR >$300K. Інакше (0 біздев · делівері = 1-2 інженери · 0 кейсів · «все для всіх»)
     → **Стадія 0**. Не плутай «новий бренд із лендінгом» зі Стадією 1.
2. **SMF-лінза.** За розділом 2 визнач найімовірнішу **діру (L / Cr / $ / #)** для цієї стадії і
   аргументуй з ознак сайту (напр.: нема кейсів з $ → ймовірна діра Cr/$; порожня company page + лише
   Upwork → діра L). Признач **найдешевшу діру для закриття першою**.
3. **AGA-фокус.** За розділом 4 признач рекомендовані модулі (M1 / M2–M3 / M4 / M5) під стадію.
   На Стадії 4–5 AGA не пропонуємо: заходимо як Fractional CRO, GTM-аудит або RevOps під одну
   практику/вертикаль, і покупець — CRO/CMO або лідер практики, а не CEO.
4. **Overshoot/undershoot (швидкий).** З огляду на Snapshot познач 1–2 явні overshoot (матеріал/актив
   випереджає стадію) і 1–2 undershoot (відстає) — повний аудит буде на кроках 9–11.
5. **3 discovery-питання.** Виведи 3 питання з розділу 1 довідника для підтвердження стадії з клієнтом.

## GATE 1 — чекпоінт
Поверни оркестратору стислий блок: **Стадія X (впевненість)** · **SMF-діра** · **AGA-фокус** ·
**3 питання** · ключові **припущення cold-audit**. Оркестратор покаже це користувачу і чекатиме
підтвердження/правок, перш ніж іти далі. Не починай ICP, доки стадію не підтверджено.

## Terms and plain-language output

<!-- glossary:start terms=agency-stage,smf-gap,aga-focus,overshoot-undershoot,checkpoint,hypothesis-confidence,founder-led,headcount-tenure,arr,discovery-call,cold-audit -->
Rules for every document a client or their team will read (review, roast, canvas, offer cards, instruction):

1. **Open with «Словник цього документа»**: only the terms that actually appear in it, at most 10, each as «термін: що це простими словами». Like the definitions section of a contract.
2. **No internal codes or letter scales in the text** (A/B/C, D L T E, BLEND numbers without words, Own/Shared/Generic, Z1.4, GATE 2.5, T1–T6). Write the meaning instead: «є цифра з клієнтом», not «A».
3. **Use the plain form from the table below.** English stays only for tool names and for copy that ships in English (promises, hooks, subject lines). If the document is in another language, translate the plain form, never the internal term.
4. **Do not score what cannot exist yet.** A block that depends on work not done (signal catalog, case studies, a previous step) gets «пропущено: спершу потрібно <що саме>», not a score.
5. **Every section of a review opens with one concrete action** («до наступного дзвінка: …»), then at most five lines of why. No paragraph that only restates the framework.


| Internal term (this skill) | Write for the reader | What it means |
|---|---|---|
| Stage 0–5, стадія агенції | стадія розвитку компанії (0–5) | шість щаблів від «CEO робить усе» до «портфель напрямів»; від стадії залежить, що доречно робити зараз. |
| SMF gap, Sales-Market Fit, L / Cr / $ / # | де губляться гроші: ліди · конверсія · чек · повторні продажі | одне з чотирьох місць, де прибуток протікає; закривати починаємо з найдешевшого. |
| AGA focus, M1 / M2–M3 / M4 / M5 | напрям робіт: стратегія · LinkedIn і розсилки · продажі · робота з клієнтами | блок робіт, який вмикаємо першим під вашу стадію; кодів модулів у документі не пишемо. |
| overshoot / undershoot | передчасне · запізніле для вашої стадії | матеріал чи документ, зроблений раніше, ніж він окупиться, або той, без якого стадія вже гальмує. |
| GATE 2.5, checkpoint | точка погодження з вами | місце, де зупиняємося і питаємо «підтверджуєте чи міняємо?»; код у документ не пишемо |
| propose-by-default, hypothesis · confidence low/med/high | наш варіант з рівнем упевненості | там, де ви ще не назвали відповідь, пропонуємо свою і пишемо, наскільки впевнені і на чому вона базується |
| founder-led, founder bottleneck | продажі тримаються на засновнику | угоди закриває лише засновник, тому ріст упирається в його час. |
| headcount, growth trend, median tenure | кількість людей · як змінюється · скільки в середньому працюють у компанії | показує розмір команди, чи вона росте і наскільки стабільна. |
| ARR | річна виручка | скільки компанія заробляє за рік. |
| discovery, discovery call | перший дзвінок з розбором потреби | розмова, де з'ясовуємо задачу, бюджет і хто вирішує, до будь-якої пропозиції. |
| cold audit | огляд ззовні за публічними даними | оцінка лише з того, що бачить сторонній: сайт, LinkedIn, відгуки; внутрішніх даних ще немає. |
<!-- glossary:end -->

## Вихід (Notion)
Під-сторінка **«02 · Stage Diagnostic»**: гіпотеза стадії + причини + впевненість; SMF-діра з
аргументацією (the leak named in words: leads, conversion, deal size or repeat business, never the letters L/Cr/$/#); the recommended work focus in plain words, never AGA or M1–M5 codes; a quick list of what is premature and what is lagging for the stage; 3 discovery-питання; блок «Джерела/припущення».
Онови властивості сторінки клієнта: `Stage`, `Stage confidence`, `SMF gap`, `AGA focus`,
`Status = Diagnosed`.

## Definition of Done
- Стадія 0–5 з рівнем впевненості та обґрунтуванням (ARR-брекет + headcount узгоджені).
- SMF-діра визначена + «закрити першою».
- AGA-фокус + по 1–2 overshoot/undershoot.
- 3 discovery-питання виведені для GATE 1.
- Notion оновлено (під-сторінка + властивості).
