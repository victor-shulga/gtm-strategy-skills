---
name: 10-channels-plan
description: Step 10 of the GTM flow. Recommend which lead-gen channels to go into, driven by the stage, the SMF gap (usually L), where the ICP/persona actually hangs out (from 03), and the buyer journey (08). Picks a primary channel plus 1-2 tests for early stages, with per-channel role, fit rationale, data source / how to reach, effort/cost, first action and KPI, plus what NOT to turn on yet. Recommendations only, stage-adaptive. Use when the user asks канали, lead gen channels, де брати ліди, distribution, outreach channels, where to find prospects. Writes to Notion in Ukrainian.
argument-hint: "(reads stage + SMF gap + persona + journey from steps 2-8 in Notion)"
---

# 10 · Channels Plan

Десятий крок. У які канали лідгену йти — **під стадію + SMF-діру (зазвичай L) + де реально буває ICP +
buyer journey**. Recommendations only (не запускаємо канали тут). Без гейту.

Вхід — 02 (стадія + SMF), 03 (персона: preferred channels / де тусуються), 08 (шлях клієнта: який канал на
яку стадію), 09 (чи готові матеріали під канал). Прочитай `${CLAUDE_PLUGIN_ROOT}/reference/agency-stages.md`
§1 (канали за стадіями), §3 (порядок Стадії 1: **Distribution — ОСТАННЄ**).
**Voje enrichment** (`${CLAUDE_PLUGIN_ROOT}/reference/gtm-strategist-voje.md` §6): **7 GTM-motions**
(Inbound/Paid/Outbound/ABM/Community/Partners/PLG) · **Bullseye** (2-3 канали) · demand-capture vs
demand-generation · **CAC = ⅓ LTV** · ABM account-math · **Growth Loops** (5 архетипів).

## Реюз
`niche-data-finder` (джерела даних під нішу) · `list-builder` / `company-finder` / `people-finder`
(як зібрати список) · `WebSearch` (знайти РЕАЛЬНІ спільноти/групи/асоціації/директорії, де є саме цей ICP).

## Принципи (важливо)
- **Distribution — останнє.** Спершу Offer (07) + Proofs (09). Не масштабуй канал, поки нема валідного
  оферу й проофів — інакше «спалиш базу».
- **Стадія диктує к-сть каналів:** 0 → 1 канал (досить для перших 3-5 угод) · 1 → 2-3 тестуються
  паралельно · 2 → 1-2 стабільних + inbound стартує · 3 → 3 (out+in+partnerships) · 4 → 4+.
- **Канал має співпадати з тим, де реально буває ICP** (з 03), а не «де модно». (Напр. blue-collar
  owner'и відповідають на телефон/SMS; LinkedIn для них слабкий.)
- **Адаптуй канали під КОНКРЕТНИЙ ICP — називай реальні майданчики, не абстрактні категорії.** Замість
  «FB-групи» — конкретні групи/subreddit'и/асоціації/директорії/спільноти ПЗ/події/подкасти, де густо є
  саме ця персона (з 03 persona «де тусуються» + 08 journey + `WebSearch`). **Якщо ICP реально там —
  додай цю спільноту окремим каналом у список.** Без конкретики канал неактивовний.
- Завжди спирайся на попередні кроки: персона (03), шлях клієнта (08), готовність матеріалів (09).
- Канал годує **awareness/business-trigger** стадії шлях клієнта (08); пізні стадії — sales/контент.

## Що зібрати

**1 · Channel shortlist (scored).** Оціни канали-кандидати (cold call/SMS · cold email · LinkedIn ·
нішеві спільноти/FB-групи · Upwork/маркетплейси · partnerships/ecosystem · local events/asоціації ·
SEO/контент · paid) за: **ICP-fit** (де буває персона) · **journey-fit** · **SMF-L impact** ·
**швидкість до перших угод** · **вартість/зусилля під стадію**. → Обери **1 primary + 1-2 test** (для 0-1).

**1b · ICP watering holes (КОНКРЕТНО).** Дослідь (03 + `WebSearch`) і **назви реальні майданчики**, де
густо є персона: конкретні FB-групи, subreddit'и, асоціації/чаптери, директорії, спільноти ПЗ (екосистеми
CRM), best-practice мережі, події, подкасти. Кожен майданчик із високою щільністю ICP → кандидат-канал.

**2 · Per-channel картка** (на обрані): *Роль* (яка стадія шлях клієнта) · *Чому fit* · *Data source / як
дістатись* (звідки список — реюз niche-data-finder) · *Effort/cost* · *First action* · *KPI*.

**3 · Sequencing.** Стадія 0 → запустити 1 primary до перших 3-5 угод; тоді тестувати 2-3 гіпотези
(звʼязок із 06-hypothesis-builder), вбивати програшні.

**4 · Що НЕ вмикати зараз** (overshoot guard): передчасні канали для стадії (напр. SEO/paid/events на
Стадії 0 — довгий payback, нема проофів).

## Вихід (Notion)
Під-сторінка **«10 · Channels Plan»**: scored shortlist · per-channel картки (з data sources) ·
sequencing · «не вмикати зараз» · блок «Джерела / припущення». Українською.

## Definition of Done
- Channel shortlist оцінено; обрано **1 primary + 1-2 test** (для Стадії 0-1) під SMF-L.
- Кожен обраний канал: роль(шлях клієнта) + чому-fit + **data source** + effort + first action + KPI.
- **Названо конкретні майданчики під цей ICP** (реальні групи/спільноти/асоціації), не абстрактні категорії.
- Sequencing + явний список «не вмикати зараз» (overshoot).
- Узгоджено з принципом «Distribution — останнє» (офер+проофи спершу). Notion-сторінка створена.
