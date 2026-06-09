# GTM Strategy — B2B Global

Плагін-набір скілів для Claude Code, що з **одного URL сайту IT-агенції** будує повну GTM-стратегію
методом **cold audit** (без даних клієнта) і складає її у **Notion українською**.

Побудовано на двох внутрішніх документах B2B Global:
- **Z1 Strategy Task Cards** (Master Blueprint Companion) — 27 task-карток, 4 фази, 6 модулів.
- **Шлях ІТ-агенції / Стадії агенції** — діагностика стадії 0–4, SMF-лінза (L/Cr/$/#), матриці
  22 маркетингових матеріалів × 5 стадій і 47 внутрішніх документів × 5 стадій, мапінг на AGA M1–M5.

Формат натхненний `growthband-outbound-skills`: окремі скіли з єдиним стандартом input → process → output.

---

## Принципи

1. **Cold audit** — на вході лише URL. Усе інше виводиться з публічного вебу + логіки стадій.
2. **Stage-adaptive** — «чим раніше стадія, тим менше всього». Глибина кожного кроку залежить від
   діагностованої стадії. Для Стадії 0–1 важкі кроки (TAM, deep competitor, category) пропускаються.
3. **Checkpointed** — оркестратор зупиняється на 3 гейтах (Стадія → ICP → Фінальний план) для рев'ю.
4. **Recommend, not generate** — кроки mat/channels/docs дають пріоритизовані списки (inventory + gap +
   overshoot/undershoot), а не самі артефакти.
5. **Reuse** — де можливо, кроки викликають наявні скіли Viktor'а (`website-scraper`,
   `deep-company-analyser`, `08-icp-builder`, `10-persona-builder`, `value-prop-lister`,
   `offer-factory`, `competitor-finder`, `niche-data-finder`, `gtm-action-thinker`).

---

## Флоу (оркестратор + 12 кроків)

| #  | Скіл | Призначення | Гейт |
|----|------|-------------|------|
| 0  | `run` | Оркестратор: веде флоу, тримає Notion-сторінку клієнта, передає контекст | — |
| 1  | `01-intake` | URL → скрейп сайту → Company Snapshot | — |
| 2  | `02-stage-diagnostic` | Стадія 0–4 + SMF-діра + 3 discovery-питання | **GATE 1** |
| 3  | `03-market-icp-persona` | Ринки (топ-3) → Тіри (1/2/3) → Персони + Anti-ICP | **GATE 2** |
| 4  | `04-market-sizing` | TAM/SAM/SOM (top-down + bottom-up), по тірах | — |
| 5  | `05-competitor-gap` | Competitor matrix + GAP + whitespace (ДО positioning) | — |
| 6  | `06-value-prop` | VP canvas (market problem → statements → ...) | — |
| 7  | `07-offers` | Offer ladder + Grand Slam cards | — |
| 8  | `08-buyer-journey` | Карта buyer's journey + touchpoints | — |
| 9  | `09-materials-plan` | Матриця 22×5: inventory + gap (рекомендації) | — |
| 10 | `10-channels-plan` | Канали лідгену під стадію + SMF | — |
| 11 | `11-docs-plan` | Матриця 47×7: inventory + gap (рекомендації) | — |
| 12 | `12-action-plan` | **30-90-180** з (Стадія + SMF + AGA) | **GATE 3** |

> **v0.2.0:** реалізовано **всі кроки `01`–`12` + оркестратор `run`**. Прогнано end-to-end на
> демо-кейсі (AI Visionary Labs) → повний 30-90-180 у Notion.

---

## Знання

- `reference/agency-stages.md` — діагностика стадій, SMF, матриці матеріалів/доків, AGA-мапінг.
- `reference/notion-schema.md` — структура Notion-воркспейсу та схема сторінок.

Скіли звертаються до них через `${CLAUDE_PLUGIN_ROOT}/reference/...`.

---

## Встановлення

```bash
git clone https://github.com/<your-username>/gtm-strategy-skills.git
claude --plugin-dir ./gtm-strategy-skills
```

Після старту:

```
/gtm-strategy:run https://example-agency.com
```

Зміни підхоплюються `/reload-plugins` без рестарту. Або скопіюй папку в `~/.claude/skills/`.

---

## Залежності

- **Notion MCP** (опційно) — для запису артефактів. Без нього є fallback у локальні `.md`
  (`gtm-output/`, див. `reference/notion-schema.md`).
- Деякі кроки можуть **реюзати** наявні GTM-скіли (icp-builder, offer-factory, competitor-finder,
  niche-data-finder тощо). Якщо їх немає — крок виконує логіку inline.
- Для скрейпу JS-сайтів і LinkedIn-команди — Apify MCP (опційно).
