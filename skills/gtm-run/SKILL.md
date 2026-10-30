---
name: gtm-run
description: Orchestrate the full GTM strategy flow for an IT agency from a website URL (cold audit). Use when the user wants a complete go-to-market strategy, a GTM audit, an agency-stage diagnosis followed by ICP, value prop, offers, competitor and buyer-journey work, or a 30-90-180 action plan from just a site. Ukrainian triggers include зроби GTM стратегію для url, GTM аудит агенції, побудуй go-to-market, стратегія з сайту, 30-90-180 план. Runs stage-adaptively, stops at 3 checkpoints, and writes every artifact to Notion in Ukrainian.
argument-hint: "<agency-website-url>"
disable-model-invocation: false
---

# GTM Strategy — Orchestrator (`gtm-run`)

Ти ведеш повний GTM-флоу для **IT-агенції** методом **cold audit**: на вході лише URL,
усе інше виводиться з публічного вебу + логіки стадій. Вихід — у **Notion, українською**.

**Вхід:** `$ARGUMENTS` = URL сайту агенції. Якщо URL не передано — спитай його (одне питання) і стоп.

Прочитай перед стартом: `${CLAUDE_PLUGIN_ROOT}/reference/agency-stages.md` та
`${CLAUDE_PLUGIN_ROOT}/reference/notion-schema.md`. Кроки 03-13 також спираються на
`${CLAUDE_PLUGIN_ROOT}/reference/gtm-frameworks.md` (GTM-фреймворки: ECP/beachhead,
value-prop canvas, 4 pricing inputs, 7 GTM-motions, proof-мілстоуни, experimentation loop).

---

## Принципи виконання

1. **Stage-adaptive.** Після GATE 1 глибина кроків залежить від стадії (див. довідник): для Стадії 0–1
   пропускай/спрощуй важкі кроки (TAM, deep competitor, category, частину матеріалів/доків).
2. **Checkpointed.** Зупиняйся на **4 чекпоінтах** (3 повних гейти + легкий GATE 2.5) і чекай
   підтвердження користувача, перш ніж іти далі:
   - **GATE 1** — після `gtm-stage-diagnostic` (стадія + SMF + 3 discovery-питання).
   - **GATE 2** — після `gtm-market-icp-persona` (ICP / Tier A).
   - **GATE 2.5** — після `gtm-positioning` (легкий): вісь + анкер + ворог, statement + 3 benefits,
     maturity зараз→ціль. Питання «цей кут правильний? від якої роботи готовий відмовлятись?». Бо
     позиціонування — батько VP/offers/материалів: помилка тут множиться вниз по флоу.
   - **GATE 3** — після `gtm-action-plan` (фінальний 30-90-180).
   На гейті: коротко покажи результат, познач ключові **припущення cold-audit**, і запитай
   «Підтверджуєш / що поправити?». Не йди далі без відповіді.
3. **Reuse.** Кожен крок-скіл сам викликає наявні скіли Viktor'а де доречно. Не дублюй їхню логіку.
4. **Notion як джерело правди.** Кожен крок створює/оновлює свою під-сторінку. Контекст між кроками
   передавай через короткий summary + посилання на Notion-сторінку клієнта.

---

## Послідовність

| Крок | Скіл | Гейт |
|------|------|------|
| 1 | `gtm-strategy:gtm-intake` | — |
| 2 | `gtm-strategy:gtm-stage-diagnostic` | **GATE 1** |
| 3 | `gtm-strategy:gtm-market-icp-persona` (Ринки → Тіри → Персони) | **GATE 2** |
| 4 | `gtm-strategy:gtm-market-sizing` (TAM-SAM-SOM, по тірах) | — |
| 5 | `gtm-strategy:gtm-competitor-gap` (whitespace → живить positioning) | — |
| 6 | `gtm-strategy:gtm-positioning` (вісь+анкер+ворог, stage-gated) | **GATE 2.5** |
| 7 | `gtm-strategy:gtm-value-prop` (споживає positioning) | — |
| 8 | `gtm-strategy:gtm-offers` | — |
| 9 | `gtm-strategy:gtm-buyer-journey` | — |
| 10 | `gtm-strategy:gtm-materials-plan` | — |
| 11 | `gtm-strategy:gtm-channels-plan` | — |
| 12 | `gtm-strategy:gtm-docs-plan` | — |
| 13 | `gtm-strategy:gtm-action-plan` | **GATE 3** |

> **v0.3.0:** усі кроки `01`–`13` реалізовані (positioning виокремлено в крок 06); оркестратор веде
> повний флоу з 4 чекпоінтами (GATE 1 / 2 / 2.5 / 3).
> Якщо проміжного скіла ще нема — виконай його роль inline за тим самим стандартом (input → process →
> Notion-вихід), спираючись на довідник, і явно познач у звіті «(inline, скіл ще не винесено)».

---

## Алгоритм

1. **Setup.** Визнач робочу Notion-локацію: `notion-search` на «GTM Strategy». Якщо база є — використай;
   якщо ні — створи базу за схемою з `notion-schema.md` (спершу спитай користувача, де її розмістити —
   parent page/teamspace). Створи/знайди сторінку клієнта за URL.
2. **Крок 1** — виклич `gtm-intake` з URL. Отримай Company Snapshot.
3. **Крок 2** — виклич `gtm-stage-diagnostic`. → **GATE 1**: покажи стадію (з рівнем впевненості),
   SMF-діру і 3 discovery-питання. Чекай підтвердження/правок стадії.
4. Після підтвердження стадії — **зафіксуй стадію** у властивостях сторінки клієнта і далі веди всі кроки
   **адаптивно під цю стадію**.
5. **Кроки 3–12** — по черзі. Після `gtm-market-icp-persona` → **GATE 2** (персони вже всередині цього
   кроку — окремого кроку для персон немає). Після `gtm-positioning` → **GATE 2.5** (підтвердь анкер/ворог/
   statement перед VP/offers). Пропускай/спрощуй кроки за правилами стадії.
6. **Крок 13** — виклич `gtm-action-plan`. → **GATE 3**: покажи 30-90-180. Чекай фінального підтвердження.
7. **Фініш.** Онови Status сторінки клієнта = «Plan ready». Дай користувачу: лінк на Notion-сторінку,
   the stage in words, where money leaks in words (leads, conversion, deal size or repeat business, never L/Cr/$/#), the work focus in plain words (never AGA or M1–M5 codes) and the top-3 actions for 30 days.

## Definition of Done (флоу)

- Сторінка клієнта в Notion створена, властивості заповнені (Stage, SMF gap, AGA focus, Status).
- Усі релевантні стадії під-сторінки існують; нерелевантні явно позначені «передчасно».
- 4 чекпоінти (GATE 1 / 2 / 2.5 / 3) пройдені з підтвердженням користувача.
- Фінальний Action Plan містить 30/90/180 горизонти з owner/effort/KPI і блоком overshoot/undershoot.

## Terms and plain-language output

<!-- glossary:start terms=agency-stage,smf-gap,aga-focus,checkpoint,cold-audit,plan-horizons,hypothesis-confidence -->
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
| GATE 2.5, checkpoint | точка погодження з вами | місце, де зупиняємося і питаємо «підтверджуєте чи міняємо?»; код у документ не пишемо |
| cold audit | огляд ззовні за публічними даними | оцінка лише з того, що бачить сторонній: сайт, LinkedIn, відгуки; внутрішніх даних ще немає. |
| Quick Wins / Foundation / Traction-Scale (0–30 / 31–90 / 91–180) | швидкі кроки · фундамент · масштабування | три відрізки плану на 30, 90 і 180 днів. |
| propose-by-default, hypothesis · confidence low/med/high | наш варіант з рівнем упевненості | там, де ви ще не назвали відповідь, пропонуємо свою і пишемо, наскільки впевнені і на чому вона базується |
<!-- glossary:end -->
