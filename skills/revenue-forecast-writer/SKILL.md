---
name: revenue-forecast-writer
description: >-
  Builds and writes the revenue forecast for a B2B service company. Counts it twice (top-down
  from the target, bottom-up from real capacity), names the gap between the two counts, finds
  the bottleneck that creates it, and lists 3-5 levers to close it, plus a plan-vs-actual
  table that becomes the reporting spine. Organised on a metrics pyramid (north-star metric,
  then revenue, sales, channel and supporting metrics). Use when the user says "revenue
  forecast", "can we hit the target", "how many touches do we need to make $X", "reverse
  math", "KPI tree", "plan vs actual on revenue", "split the annual target by quarter",
  "прогноз виручки", "порахуй план на квартал", "скільки доторків треба щоб зробити $X",
  "план/факт по виручці", "чи витягнемо ціль", "розбий річну ціль по кварталах", or hands over
  a revenue target and asks what it takes. Not pipeline hygiene on existing deals (use
  pipeline-analysis), not pricing design, not the weekly channel report (use
  weekly-outreach-report).
---

# Revenue Forecast Writer

A forecast counted once is a wish. This skill counts it from both ends and reports the distance
between the two counts. That distance is the agenda for the planning meeting.

Answer in the user's language. Section labels below are given in English with the Ukrainian
equivalent in brackets; use the language the audience reads.

## What it produces

1. **Assumptions** (Припущення): every conversion rate, average deal size and cycle length, with
   its source.
2. **Top-down forecast** (Прогноз зверху вниз): target → the volume it requires, stage by stage.
3. **Bottom-up forecast** (Прогноз знизу вгору): real capacity × real conversions → what is
   actually reachable.
4. **Gap** (Розрив): the difference, in money and in the stage that causes it.
5. **Bottlenecks** (Вузькі місця): at most 3, ranked.
6. **Levers** (Важелі): 3-5 ways to close the gap, each with its expected effect and its cost.
7. **Plan vs actual spine** (План/факт): the same table structure the monthly and quarterly reports
   will fill.

## The metrics pyramid

Organise every number on five levels so each metric has a parent and the forecast reads as one
tree. This is the author's own planning template:

| Level | What sits here | Example |
| :-- | :-- | :-- |
| North-star metric | the one number the company steers by | new recurring revenue per quarter |
| L1 Revenue | revenue by service line, new vs existing clients | new-logo revenue, renewals, upsell |
| L2 Sales | deals, win rate, average deal size, cycle length | SQLs, proposals sent, deals won |
| L3 Channel | volume and conversion per channel | touches, replies, meetings per channel |
| L4 Supporting | inputs that feed the channels | contacts with a signal, content published, team capacity |

---

## The two counts

### Top-down (reverse math)
`Target $ ÷ average deal = deals` → `÷ win rate = qualified leads (SQL)` →
`÷ meeting-to-SQL rate = meetings` → `÷ reply-to-meeting rate = replies` →
`÷ reply rate = touches`.

Add the sales cycle: revenue landing in Q3 comes from touches made in Q1-Q2. A forecast that ignores
cycle length reports next year's work as this quarter's shortfall.

### Bottom-up (capacity)
`People × touches each person really makes per month × measured conversions = reachable revenue`.

Capacity is the ceiling nobody counts. An SDR who sustains 500 touches a month cannot deliver a
1,000-touch plan by trying harder. Delivery capacity is a ceiling too: `billable hours × rate`
caps revenue whatever the funnel produces.

### The gap
State it in money and in the stage that produces it. Never split the difference between the two
counts, never average them, never quietly adopt the more optimistic one.

---

## Assumptions: the honesty gate

Tag every rate by source:

| Tag | Meaning |
| :-- | :-- |
| `measured` (факт) | measured on this company's own data, period named |
| `benchmark` (бенчмарк) | external benchmark, source named |
| `assumption` (припущення) | an agreed guess, marked as such in every report until it is replaced by a measured rate |

Benchmarks must carry their source. Two reference points for cold email, for example:
- A cold-email sending platform's published benchmark across its 2025 sending data puts the average cold email reply
  rate at about 3.4%.
- The skill's author plans 2026 cold outbound for service companies at about 1.5% reply rate, with
  at most a fifth of replies positive (about 0.3% positive), based on his own campaigns. Tag this
  as `assumption` unless the company's own data confirms it.

A forecast built entirely on benchmarks and assumptions is a scenario, not a forecast. Label it so
at the top. **Never present an assumed rate as measured.** That is how a plan turns into a stick
for beating the team.

---

## Bottlenecks: look in these four places, name at most three

1. **Data / base.** Are there enough accounts with a real buying signal to feed the plan? The author's
   rule of thumb: if fewer than 1 in 10 target accounts carries a signal, rebuild the base before
   sending more.
2. **Presales.** Who writes proposals, and how many can they write a month?
3. **Seller.** How many discovery calls can one person run and follow up properly per week?
4. **Delivery ceiling.** `Hours × rate`. Selling past it creates a delivery crisis, not revenue.

## Levers: each with effect and cost

Effect is arithmetic, not adjectives: "+1 SDR = +500 touches a month = +2 SQLs = +$X at the current
win rate". Cost includes money, ramp time, and whose attention it takes. A lever whose effect cannot
be computed from the assumptions table does not go on the list.

---

## Plan vs actual spine

The forecast's output tables ARE the reporting tables. Columns:
`Metric · Plan for period · Actual · % of plan · Comment`.

Deviation shows in the same row, not in a section further down. Metrics that live in a system the
team has no access to are marked "no data", never modelled to fill the table.

Where two plans exist (a board deck and an operating plan, for example), name both, say which one
this audience sees, and flag the divergence in every report. Do not merge them.

---

## Process

1. Get the target, the period, and where the current plan lives. Ask who will read the output.
2. Build the assumptions table first, tagging every rate. Missing rates: ask, or mark as
   `assumption`.
3. Do both counts, top-down and then bottom-up, before looking at the gap.
4. Write the gap, then find the bottleneck that explains it.
5. Build the levers. Recompute the forecast WITH the levers as a second scenario, so the reader sees
   base vs levered, not one hopeful line.
6. Ship the narrative:
   - as a **Notion page**, if a Notion connector is available;
   - otherwise as a **markdown document** (or .docx via the docx skill, if the user prefers).
   Add an **XLSX** (via the xlsx skill, if available) only when the company's team will enter
   numbers into it monthly: an empty skeleton they fill. Do not backfill their actuals for them.
7. Edit the prose for AI tells before delivery; if installed, use `anticopywriting-ai` (pack
   `gtm-skills`). In Ukrainian, prefer plain words: прогноз, припущення, кваліфіковані ліди,
   завантаження команди, продовження.

## Rules

- Never invent a conversion rate to make the arithmetic land on the target.
- The gap is the deliverable. If top-down and bottom-up agree perfectly, one was probably derived
  from the other. Check.
- A quarterly split is not the annual target divided by 4. Weight it by cycle length, seasonality,
  and the ramp of anything new.
- Weekly targets are prorated by working days, not by 4.33 weeks per month.

## Related skills (optional, if installed)

- `pipeline-analysis` (pack `sales-engine-skills`): health of the deals already in the pipeline;
  feeds the measured rates.
- `capacity-plan` (pack `gtm-strategy-skills`): team workload and hiring math behind the bottom-up
  count.
- `growth-planner` (pack `gtm-strategy-skills`): turns the chosen levers into a growth plan.
- `sales-hiring-brief` (pack `gtm-strategy-skills`): when the lever is a new hire.
- `weekly-outreach-report` (pack `outbound-engine-skills`): the weekly channel numbers that fill
  the plan vs actual spine.
- `pricing` (pack `marketing-engine-skills`): when the gap points at deal size, not volume.

## Credits

Built by Victor Shulga; the metrics pyramid is his planning template. The cold email reply-rate
reference comes from a cold-email sending platform's published benchmark report (2025 data).
