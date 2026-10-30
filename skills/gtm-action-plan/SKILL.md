---
name: gtm-action-plan
description: Final step of the GTM flow and CHECKPOINT 3. Synthesize all prior artifacts into a 30-90-180 day action plan for an IT agency, derived from the diagnosed stage plus the cheapest Sales-Market-Fit gap (L, Cr, $, #) plus the AGA module mapping M1-M5. Produces stage-appropriate task cards with owner, effort, KPI, plus an overshoot kill and undershoot build list. Use when the user asks for екшн-план, 30-90-180, що робити далі, roadmap, or at the end of the GTM flow. Writes to Notion in Ukrainian.
argument-hint: "(reads stage, SMF gap, ICP and other artifacts from the client's Notion page)"
---

# 13 · Action Plan — 30-90-180 (GATE 3)

Фінальний крок і **фінальний чекпоінт (GATE 3)**. Звести все у пріоритизований **екшн-план на 30 / 90 / 180 днів**.
Основа плану: **Стадія + найдешевша SMF-діра + AGA-мапінг** (рішення зафіксоване в архітектурі флоу).

Прочитай `${CLAUDE_PLUGIN_ROOT}/reference/agency-stages.md` (розділи 2, 4, 5, 8). **GTM enrichment** (`${CLAUDE_PLUGIN_ROOT}/reference/gtm-frameworks.md` §0,§7,§8):
proof-мілстоуни (Problem-Solution → PMF → GTM-fit → Scaling; Sean Ellis ≥40%) · NSM + OKR (огляд щомісяця) ·
**Experimentation Loop** + **Impact × Ease** пріоритизація · 90-day plan. Підтягни з Notion-
сторінки клієнта: Stage, SMF gap, AGA focus + **усі артефакти кроків 03-12** (03 ринок/ICP/тіри/персона ·
04 market-sizing · 05 competitor+whitespace · 06 positioning · 07 VP · 08 offers · 09 шлях клієнта ·
10 materials · 11 channels · 12 docs). Чого ще нема — врахуй як «залежність». KPI бери leading; де доречно — бенчмарки
Z1 (Appendix A).

## Логіка пріоритизації
1. **Стадія** задає стелю амбіцій (що доречно зараз, що передчасно).
2. **SMF-діра** задає, ЩО лагодимо першим (закривай найдешевшу діру: L → Cr → $ → #).
3. **AGA-фокус** задає, ЯКИЙ блок робіт активуємо (M1 / M2–M3 / M4 / M5).
4. **Overshoot/undershoot** (з кроків 10–12) → конкретні «вбити» та «збудувати».

## Структура плану

**Горизонти:**
- **0–30 днів — Quick Wins:** 5–7 дій, що дають видимий рух і закривають найдешевшу діру. Для Стадії 0–1
  — фокус, не масштаб (1 ICP, 1 офер, 1 канал).
- **31–90 днів — Foundation:** збудувати фундаментні артефакти/процеси під стадію (ICP refresh,
  offer A/B, базові доки за матрицею).
- **91–180 днів — Traction/Scale:** масштабувати те, що спрацювало; додати наступний AGA-модуль.

**Формат кожної дії (task-картка):**
- Назва · Навіщо (яку діру/мету закриває) · Owner (роль за стадією) · Effort (small / medium / large, written in words) ·
  KPI (leading-метрика) · Залежності.

**Окремі блоки:**
- **Вбити / заморозити (overshoot)** — 1–3 пункти.
- **Збудувати (undershoot, критичні gaps)** — 1–3 пункти.
- **Чого НЕ робимо зараз (передчасно для стадії)** — щоб уникнути paralysis і overshoot.

## Реюз
Перед фіналізацією прожени план через **`gtm-action-thinker`** (цей пак; стрес-тест: сліпі плями, ризики,
чи реалістичний обсяг під команду стадії). Врахуй зауваження.

## GATE 3 — чекпоінт
Покажи користувачу стислий 30-90-180 + блоки kill/build. Чекай підтвердження/правок. Після — онови
`Status = Plan ready`.

## Terms and plain-language output

<!-- glossary:start terms=agency-stage,smf-gap,aga-focus,checkpoint,plan-horizons,effort-sml,leading-lagging,overshoot-undershoot,fit-milestones,north-star-metric,okr,impact-ease -->
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
| Quick Wins / Foundation / Traction-Scale (0–30 / 31–90 / 91–180) | швидкі кроки · фундамент · масштабування | три відрізки плану на 30, 90 і 180 днів. |
| Effort S / M / L | обсяг роботи: малий · середній · великий | грубо, скільки часу забере дія; пишемо словами, без літер. |
| leading / lagging metric, KPI (leading) | випереджальний · підсумковий показник | випереджальний видно за тиждень-два (відповіді, дзвінки), підсумковий приходить пізніше (угоди, гроші). |
| overshoot / undershoot | передчасне · запізніле для вашої стадії | матеріал чи документ, зроблений раніше, ніж він окупиться, або той, без якого стадія вже гальмує. |
| Problem-Solution fit → PMF → GTM-fit → Scaling | етапи доведення: проблему визнають · клієнти тримаються · продажі повторюються · масштабування | чотири перевірки, які показують, що бізнес готовий до наступного кроку. |
| North Star Metric, NSM | головний показник | одна цифра, за якою компанія звіряє курс; вона веде до виручки і показує цінність для клієнта. |
| OKR | цілі й ключові результати | ціль словами плюс 3–5 вимірюваних результатів, переглядаємо щомісяця. |
| Impact × Ease | вплив × легкість | спосіб розставити дії за пріоритетом: спершу те, що дає багато і робиться легко. |
<!-- glossary:end -->

## Вихід (Notion)
Під-сторінка **«13 · Action Plan 30-90-180»**: 3 горизонти з task-картками (таблиця або тогли),
блоки overshoot/undershoot/«не робимо», і резюме зверху (stage named in words; where money leaks in words: leads, conversion, deal size or repeat business, never the letters L/Cr/$/#; the work focus in plain words, never AGA or M1–M5 codes; top-3 actions).
Українською. Блок «Джерела/припущення».

## Definition of Done
- 3 горизонти заповнені; кожна дія має owner + effort + KPI.
- План явно прив'язаний до Стадії + SMF-діри + AGA-фокусу.
- Є блоки «вбити», «збудувати», «не робимо зараз».
- Пройдено `gtm-action-thinker`-стрес-тест.
- Notion оновлено; `Status = Plan ready`.
