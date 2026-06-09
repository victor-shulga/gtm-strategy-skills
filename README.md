# GTM Strategy — B2B Global

Плагін-набір скілів для Claude Code, що з **одного URL сайту IT-агенції** будує повну GTM-стратегію
методом **cold audit** (без даних клієнта) і складає її у **Notion українською**.

Побудовано на двох внутрішніх документах B2B Global:
- **Z1 Strategy Task Cards** (Master Blueprint Companion) — 27 task-карток, 4 фази, 6 модулів.
- **Шлях ІТ-агенції / Стадії агенції** — діагностика стадії 0–4, SMF-лінза (L/Cr/$/#), матриці
  22 маркетингових матеріалів × 5 стадій і 47 внутрішніх документів × 5 стадій, мапінг на AGA M1–M5.


---

## Принципи

1. **Cold audit** — на вході лише URL. Усе інше виводиться з публічного вебу + логіки стадій.
2. **Stage-adaptive** — «чим раніше стадія, тим менше всього». Глибина кожного кроку залежить від
   діагностованої стадії. Для Стадії 0–1 важкі кроки (TAM, deep competitor, category) пропускаються.
3. **Checkpointed** — оркестратор зупиняється на 4 чекпоінтах (Стадія → ICP → Positioning → Фінальний план) для рев'ю.
4. **Recommend, not generate** — кроки mat/channels/docs дають пріоритизовані списки (inventory + gap +
   overshoot/undershoot), а не самі артефакти.
5. **Reuse** — де можливо, кроки викликають наявні скіли Viktor'а (`website-scraper`,
   `deep-company-analyser`, `08-icp-builder`, `10-persona-builder`, `value-prop-lister`,
   `offer-factory`, `competitor-finder`, `niche-data-finder`, `gtm-action-thinker`).

---

## Флоу (оркестратор + 13 кроків)

| #  | Скіл | Призначення | Гейт |
|----|------|-------------|------|
| 0  | `run` | Оркестратор: веде флоу, тримає Notion-сторінку клієнта, передає контекст | — |
| 1  | `01-intake` | URL → скрейп сайту → Company Snapshot | — |
| 2  | `02-stage-diagnostic` | Стадія 0–4 + SMF-діра + 3 discovery-питання | **GATE 1** |
| 3  | `03-market-icp-persona` | Ринки (топ-3) → Тіри (1/2/3) → Персони + Anti-ICP | **GATE 2** |
| 4  | `04-market-sizing` | TAM/SAM/SOM (top-down + bottom-up), по тірах | — |
| 5  | `05-competitor-gap` | Competitor matrix + GAP + whitespace | — |
| 6  | `06-positioning` | Вісь+анкер+ворог, stage-gated + Z1.4 maturity | **GATE 2.5** |
| 7  | `07-value-prop` | VP canvas (споживає positioning) | — |
| 8  | `08-offers` | Offer ladder + Grand Slam cards | — |
| 9  | `09-buyer-journey` | Карта buyer's journey + touchpoints | — |
| 10 | `10-materials-plan` | Матриця 22×5: inventory + gap (рекомендації) | — |
| 11 | `11-channels-plan` | Канали лідгену під стадію + SMF | — |
| 12 | `12-docs-plan` | Матриця 47×7: inventory + gap (рекомендації) | — |
| 13 | `13-action-plan` | **30-90-180** з (Стадія + SMF + AGA) | **GATE 3** |

> **v0.3.0:** реалізовано **всі кроки `01`–`13` + оркестратор `run`** (positioning виокремлено в крок 06). 

---

## Знання

- `reference/agency-stages.md` — діагностика стадій, SMF, матриці матеріалів/доків, AGA-мапінг.
- `reference/notion-schema.md` — структура Notion-воркспейсу та схема сторінок.
- `reference/gtm-frameworks.md` — перевірені GTM-фреймворки, змаплені на кроки:
  ECP/beachhead, value-prop canvas, 8-step positioning, 4 pricing inputs, 7 GTM-motions, proof-мілстоуни,
  experimentation loop, anti-patterns.

Скіли звертаються до них через `${CLAUDE_PLUGIN_ROOT}/reference/...`.

---

## Встановлення

**Спосіб 1 — через Claude Code marketplace (рекомендовано):**
```
/plugin marketplace add victor-shulga/gtm-strategy-skills
/plugin install gtm-strategy@gtm-strategy-skills
/gtm-strategy:run https://example-agency.com
```
Оновлення: `/plugin marketplace update gtm-strategy-skills`.

**Спосіб 2 — локально через клон:**
```bash
git clone https://github.com/victor-shulga/gtm-strategy-skills.git
claude --plugin-dir ./gtm-strategy-skills
/gtm-strategy:run https://example-agency.com
```
Зміни підхоплюються `/reload-plugins`. Або скопіюй папку в `~/.claude/skills/`.

---

## Залежності

- **Notion MCP** (опційно) — для запису артефактів. Без нього є fallback у локальні `.md`
  (`gtm-output/`, див. `reference/notion-schema.md`).
- Деякі кроки можуть **реюзати** наявні GTM-скіли (icp-builder, offer-factory, competitor-finder,
  niche-data-finder тощо). Якщо їх немає — крок виконує логіку inline.
- Для скрейпу JS-сайтів і LinkedIn-команди — Apify MCP (опційно).

---

## Валідація (для контриб'юторів)

```bash
bash scripts/validate.sh
```

Перевіряє структуру плагіна (чистий `python3`, без залежностей): `name:` фронтматера == ім'я папки ·
номери в H1 / «Step N» / Notion-заголовках збігаються з папкою · послідовність кроків `01..NN` без
дір/дублів · оркестратор `run` посилається на кожен крок · описи YAML-безпечні (без лапок / `: `) ·
JSON валідний і версії `plugin.json` ↔ `marketplace.json` збігаються. Той самий чек ганяє CI
(`.github/workflows/ci.yml`) на кожен push/PR.
