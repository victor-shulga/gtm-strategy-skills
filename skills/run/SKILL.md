---
name: run
description: Orchestrate the full B2B Global GTM strategy flow for an IT agency from a website URL (cold audit). Use when the user wants a complete go-to-market strategy, a GTM audit, an agency-stage diagnosis followed by ICP, value prop, offers, competitor and buyer-journey work, or a 30-90-180 action plan from just a site. Ukrainian triggers include зроби GTM стратегію для url, GTM аудит агенції, побудуй go-to-market, стратегія з сайту, 30-90-180 план. Runs stage-adaptively, stops at 3 checkpoints, and writes every artifact to Notion in Ukrainian.
argument-hint: "<agency-website-url>"
disable-model-invocation: false
---

# GTM Strategy — Orchestrator (`run`)

Ти ведеш повний GTM-флоу B2B Global для **IT-агенції** методом **cold audit**: на вході лише URL,
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
   - **GATE 1** — після `02-stage-diagnostic` (стадія + SMF + 3 discovery-питання).
   - **GATE 2** — після `03-icp` (ICP / Tier A).
   - **GATE 2.5** — після `06-positioning` (легкий): вісь + анкер + ворог, statement + 3 benefits,
     maturity зараз→ціль. Питання «цей кут правильний? від якої роботи готовий відмовлятись?». Бо
     позиціонування — батько VP/offers/материалів: помилка тут множиться вниз по флоу.
   - **GATE 3** — після `13-action-plan` (фінальний 30-90-180).
   На гейті: коротко покажи результат, познач ключові **припущення cold-audit**, і запитай
   «Підтверджуєш / що поправити?». Не йди далі без відповіді.
3. **Reuse.** Кожен крок-скіл сам викликає наявні скіли Viktor'а де доречно. Не дублюй їхню логіку.
4. **Notion як джерело правди.** Кожен крок створює/оновлює свою під-сторінку. Контекст між кроками
   передавай через короткий summary + посилання на Notion-сторінку клієнта.

---

## Послідовність

| Крок | Скіл | Гейт |
|------|------|------|
| 1 | `gtm-strategy:01-intake` | — |
| 2 | `gtm-strategy:02-stage-diagnostic` | **GATE 1** |
| 3 | `gtm-strategy:03-market-icp-persona` (Ринки → Тіри → Персони) | **GATE 2** |
| 4 | `gtm-strategy:04-market-sizing` (TAM-SAM-SOM, по тірах) | — |
| 5 | `gtm-strategy:05-competitor-gap` (whitespace → живить positioning) | — |
| 6 | `gtm-strategy:06-positioning` (вісь+анкер+ворог, stage-gated) | **GATE 2.5** |
| 7 | `gtm-strategy:07-value-prop` (споживає positioning) | — |
| 8 | `gtm-strategy:08-offers` | — |
| 9 | `gtm-strategy:09-buyer-journey` | — |
| 10 | `gtm-strategy:10-materials-plan` | — |
| 11 | `gtm-strategy:11-channels-plan` | — |
| 12 | `gtm-strategy:12-docs-plan` | — |
| 13 | `gtm-strategy:13-action-plan` | **GATE 3** |

> **v0.3.0:** усі кроки `01`–`13` реалізовані (positioning виокремлено в крок 06); оркестратор веде
> повний флоу з 4 чекпоінтами (GATE 1 / 2 / 2.5 / 3).
> Якщо проміжного скіла ще нема — виконай його роль inline за тим самим стандартом (input → process →
> Notion-вихід), спираючись на довідник, і явно познач у звіті «(inline, скіл ще не винесено)».

---

## Алгоритм

1. **Setup.** Визнач робочу Notion-локацію: `notion-search` на «GTM Strategy». Якщо база є — використай;
   якщо ні — створи базу за схемою з `notion-schema.md` (спершу спитай користувача, де її розмістити —
   parent page/teamspace). Створи/знайди сторінку клієнта за URL.
2. **Крок 1** — виклич `01-intake` з URL. Отримай Company Snapshot.
3. **Крок 2** — виклич `02-stage-diagnostic`. → **GATE 1**: покажи стадію (з рівнем впевненості),
   SMF-діру і 3 discovery-питання. Чекай підтвердження/правок стадії.
4. Після підтвердження стадії — **зафіксуй стадію** у властивостях сторінки клієнта і далі веди всі кроки
   **адаптивно під цю стадію**.
5. **Кроки 3–12** — по черзі. Після `03-market-icp-persona` → **GATE 2** (персони вже всередині цього
   кроку — окремого `04-personas` немає). Після `06-positioning` → **GATE 2.5** (підтвердь анкер/ворог/
   statement перед VP/offers). Пропускай/спрощуй кроки за правилами стадії.
6. **Крок 13** — виклич `13-action-plan`. → **GATE 3**: покажи 30-90-180. Чекай фінального підтвердження.
7. **Фініш.** Онови Status сторінки клієнта = «Plan ready». Дай користувачу: лінк на Notion-сторінку,
   стадію, SMF-діру, AGA-фокус і топ-3 дії на 30 днів.

## Definition of Done (флоу)

- Сторінка клієнта в Notion створена, властивості заповнені (Stage, SMF gap, AGA focus, Status).
- Усі релевантні стадії під-сторінки існують; нерелевантні явно позначені «передчасно».
- 4 чекпоінти (GATE 1 / 2 / 2.5 / 3) пройдені з підтвердженням користувача.
- Фінальний Action Plan містить 30/90/180 горизонти з owner/effort/KPI і блоком overshoot/undershoot.
