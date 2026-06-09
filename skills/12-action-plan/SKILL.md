---
name: 12-action-plan
description: Final step of the GTM flow and CHECKPOINT 3. Synthesize all prior artifacts into a 30-90-180 day action plan for an IT agency, derived from the diagnosed stage plus the cheapest Sales-Market-Fit gap (L, Cr, $, #) plus the AGA module mapping M1-M5. Produces stage-appropriate task cards with owner, effort, KPI, plus an overshoot kill and undershoot build list. Use when the user asks for екшн-план, 30-90-180, що робити далі, roadmap, or at the end of the GTM flow. Writes to Notion in Ukrainian.
argument-hint: "(reads stage, SMF gap, ICP and other artifacts from the client's Notion page)"
---

# 12 · Action Plan — 30-90-180 (GATE 3)

Фінальний крок і **третій чекпоінт**. Звести все у пріоритизований **екшн-план на 30 / 90 / 180 днів**.
Основа плану: **Стадія + найдешевша SMF-діра + AGA-мапінг** (рішення зафіксоване в архітектурі флоу).

Прочитай `${CLAUDE_PLUGIN_ROOT}/reference/agency-stages.md` (розділи 2, 4, 5, 8). **GTM enrichment** (`${CLAUDE_PLUGIN_ROOT}/reference/gtm-frameworks.md` §0,§7,§8):
proof-мілстоуни (Problem-Solution → PMF → GTM-fit → Scaling; Sean Ellis ≥40%) · NSM + OKR (огляд щомісяця) ·
**Experimentation Loop** + **Impact × Ease** пріоритизація · 90-day plan. Підтягни з Notion-
сторінки клієнта: Stage, SMF gap, AGA focus + **усі артефакти кроків 03-11** (03 ринок/ICP/тіри/персона ·
04 market-sizing · 05 competitor+whitespace · 06 VP · 07 offers · 08 шлях клієнта · 09 materials ·
10 channels · 11 docs). Чого ще нема — врахуй як «залежність». KPI бери leading; де доречно — бенчмарки
Z1 (Appendix A).

## Логіка пріоритизації
1. **Стадія** задає стелю амбіцій (що доречно зараз, що передчасно).
2. **SMF-діра** задає, ЩО лагодимо першим (закривай найдешевшу діру: L → Cr → $ → #).
3. **AGA-фокус** задає, ЯКИЙ блок робіт активуємо (M1 / M2–M3 / M4 / M5).
4. **Overshoot/undershoot** (з кроків 9–11) → конкретні «вбити» та «збудувати».

## Структура плану

**Горизонти:**
- **0–30 днів — Quick Wins:** 5–7 дій, що дають видимий рух і закривають найдешевшу діру. Для Стадії 0–1
  — фокус, не масштаб (1 ICP, 1 офер, 1 канал).
- **31–90 днів — Foundation:** збудувати фундаментні артефакти/процеси під стадію (ICP refresh,
  offer A/B, базові доки за матрицею).
- **91–180 днів — Traction/Scale:** масштабувати те, що спрацювало; додати наступний AGA-модуль.

**Формат кожної дії (task-картка):**
- Назва · Навіщо (яку діру/мету закриває) · Owner (роль за стадією) · Effort (S/M/L) ·
  KPI (leading-метрика) · Залежності.

**Окремі блоки:**
- **Вбити / заморозити (overshoot)** — 1–3 пункти.
- **Збудувати (undershoot, критичні gaps)** — 1–3 пункти.
- **Чого НЕ робимо зараз (передчасно для стадії)** — щоб уникнути paralysis і overshoot.

## Реюз
Перед фіналізацією прожени план через **`gtm-action-thinker`** (стрес-тест: сліпі плями, ризики,
чи реалістичний обсяг під команду стадії). Врахуй зауваження.

## GATE 3 — чекпоінт
Покажи користувачу стислий 30-90-180 + блоки kill/build. Чекай підтвердження/правок. Після — онови
`Status = Plan ready`.

## Вихід (Notion)
Під-сторінка **«12 · Action Plan 30-90-180»**: 3 горизонти з task-картками (таблиця або тогли),
блоки overshoot/undershoot/«не робимо», і резюме зверху (Стадія · SMF-діра · AGA-фокус · топ-3 дії).
Українською. Блок «Джерела/припущення».

## Definition of Done
- 3 горизонти заповнені; кожна дія має owner + effort + KPI.
- План явно прив'язаний до Стадії + SMF-діри + AGA-фокусу.
- Є блоки «вбити», «збудувати», «не робимо зараз».
- Пройдено `gtm-action-thinker`-стрес-тест.
- Notion оновлено; `Status = Plan ready`.
