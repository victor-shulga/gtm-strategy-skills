---
name: growth-planner
description: >-
  Guided growth planning for a service business (agency, consultancy, fractional exec). Interviews
  the owner block by block (goals, current clients, offers, Point A funnel by channel, channels for
  next year, upsells, products sold without a call, team capacity), says where to find each answer
  (P&L, CRM, booking calendar, outreach platforms, waitlist), pre-fills what connected sources can
  answer, then builds an interactive planner page (activity per channel -> intro calls -> clients ->
  revenue vs target, with current-client, upsell, product and new-client revenue streams, capacity
  and client-ceiling checks) and cascades it into quarterly and weekly KPIs per owner plus a channel
  plan for the year. Trigger on "growth plan", "plan next year", "revenue plan by channel", "KPIs
  for the team from the plan", "forward planner", "план росту", "планувальник", "спланувати рік",
  "план по каналах", "план доходу на рік", "KPI команді з плану".
---

# Growth planner

Turns "we want to grow" into a forward plan: activity per channel × Point A conversions = calls, clients
and revenue, held against the target. Then every owner gets a weekly and a quarterly number.

Talk to the owner in their language, in plain words: say "metrics" or "cost to win a client" in the
words a non-marketer uses, and skip jargon and borrowed terms where a plain word exists (in Ukrainian,
for example, «показники» rather than «метрики», «ціна залучення клієнта» rather than «CAC», «оцінка лідів»
rather than «лід-скоринг»). Tool names (Notion, HubSpot, Instantly) stay as they are.

## Files

- `references/interview.md`: the question bank (9 blocks, 31 questions), each with where to look and what to do if the answer is unknown. Read it before starting.
- `assets/planner.html`: the engine, a single HTML file. Everything business-specific sits between `// CFG-START` and `// CFG-END`. The page UI is in Ukrainian; translate the strings in this file if the owner needs another language.
- `scripts/build.py [config.json] <out.html> [--brand brand.json]`: validates a config and writes the page. Without a config it uses `configs/example.json`. `--brand` swaps colour tokens and fonts for the client's own design system.
- `configs/example.json`: a fictional agency ("Агенція А", labelled as an example everywhere). Copy its shape for a real business; keep real configs outside this folder, because they hold client names and revenue.

## Requirements & integrations

| Integration | Used for | Required? | Auth / setup |
|---|---|---|---|
| Python 3.8+ | `scripts/build.py` | yes | none |
| A browser | opening the planner page | yes | none; edits save in the browser (localStorage) |
| P&L (Google Sheets, accounting export) | revenue by month, current clients, LTV, upsells | strongly recommended | the owner's file or connector |
| CRM (any) | deal sources, stages, cycle length | recommended | the owner's connector or export |
| Booking calendar (Calendly, TidyCal and similar) | intro-call counts | recommended | the owner's connector or export |
| Outreach platforms (LinkedIn tools, cold-email tools) | activity per channel | optional | the owner's account stats |
| Claude Artifacts with a shared database | one plan edited by the whole team | optional | the page detects `window.claude` and switches from browser storage to shared storage automatically |
| Headless Chrome | render check before handing the page over | optional | local Chrome |

## Flow

### 1. Pre-fill before asking

Pull everything a connector or file can answer, so the owner only confirms:
- revenue by month, current paying clients, lifetime, upsells: the P&L or a business report
- intro calls: the booking calendar, plus CRM deals at stage "meeting" or later
- channel of each deal: the CRM source field; new clients: the month of first payment in the P&L, not the CRM status
- activity: post counts, outreach platform stats, freelance-marketplace logs
- waitlists: the product's waitlist table

Tell the owner which numbers you already have, and from where, in one short list.

### 2. Interview, one block at a time

Follow `references/interview.md`. Per block: state what is pre-filled ("the report shows X, correct?"),
ask only what is missing, and give the where-to-look line for each open question. Wait for answers before
the next block. An "unknown" becomes an explicit assumption (a dashed cell in the planner, listed in the
page's sources). Never an invented Point A.

Keep a running config file for the business as answers arrive, so a paused interview resumes where it
stopped (the optional `interview` key records finished blocks and the next one).

### 3. Build and publish

1. Fill the config (schema below). Rules:
   - Point A = the whole previous year + the closed quarters of the current one (for example January of last year to September of this year = 7 quarters). Service firms close few deals: half a year gives 3 to 7 wins, and one deal then moves conversion by several points. `pointA.quarters` = number of quarters in the window; pace per quarter = window total ÷ quarters. Put the last 2 quarters in `pointA.recent` so the page shows fresh pace next to the average. Per channel: `A.act` (null if nobody counted), `A.calls`, `A.wins`.
   - If the CRM covers only part of the window, take channel shares from the CRM and spread the calendar total by those shares; say so in `pointA.note`. A channel launched inside the window is not scaled.
   - Wins exclude non-client income (sponsorships, referral payouts) and warm exceptions that came through a personal acquaintance; list them in the note.
   - Channel without countable activity: set `dAct` and `dA2C` so the default plan reproduces the Point A calls (the page must open at Point A pace, not at an optimistic one).
   - Inbound or unattributed calls: a channel with `fixedA2C: 100`, `hu: 0`, `dAct` = Point A calls per quarter, unit "inbound calls".
   - Offer `m` = months a client really pays. Shares must give an average deal value close to the P&L LTV (`ltvFact`); say so if they differ by more than 20%.
2. `python3 scripts/build.py path/to/business.json path/to/output/business-planner.html [--brand brand.json]`. Write the output outside the skill folder.
3. Hand over the page: send the HTML file, host it, or publish it as a Claude Artifact with a shared database so edits are visible to everyone with access.
4. Render check once (headless Chrome `--dump-dom` with `--virtual-time-budget=6000`): read the year cards and the KPI block, confirm there is no `NaN`, then hand over the link.

### 4. Review with the owner (interview block 9)

Walk four questions: gap to target, capacity, client ceiling, single-channel dependence. Record each
decision as an edit in the planner (activity, offer mix, target). The planner is the record.

### 5. Cascade into KPIs and plans

The page already renders:
- **Revenue plan**: current clients / upsells / product / new clients per quarter and for the year, against the target, with monthly recurring revenue and active clients at quarter end.
- **Channel plan for the year**: activity · calls · clients per channel per quarter.
- **Team KPIs**: per owner, weekly activity per channel (leading), calls and clients per quarter (lagging) and sales hours per week; the current-client owner gets retention revenue, upsells and active clients against the ceiling; the product owner gets waitlist per week, buyers, revenue and delivery hours.

Then put the per-owner numbers wherever the team tracks work (a task board, the weekly report's plan
vs fact section). If installed, `weekly-outreach-report` (pack `outbound-engine-skills`) carries a plan
vs fact funnel. Every leading KPI is checked weekly (Friday works well), lagging ones monthly. A KPI
without an owner is not a KPI.

## Config schema (short)

```
client, title, firstMonth "YYYY-10", quarters [5 labels: Q4 this year + 4 quarters next year],
pointA {label, quarters, calls, wins, callsNote?, recent {label, quarters, calls, wins}?, note},
channels [{id, n, u (unit), owner, A {act|null, calls, wins}, hu (hours per unit), tools ($/quarter),
           dAct?, dA2C?, fixedA2C?, what, src}],
offers [{n, p ($/month or one-off), m (months paid), s (% of wins), note}], ltvFact, cacFact?,
base [{n, mrr, end "YYYY-MM"|"", p? (% chance, for unsigned deals)}], baseOwner,
upsell {p, m, perQ [per quarter], note}?,
course {n, owner, tiers [{n, p, s}], wl [waitlist per quarter], extra [buyers outside the waitlist per quarter],
        pointANote?, note}?,
params {cconv, chrs, c2cl, upP, upM, lag, c2p, hcall, hprop, hweek, rate, churn, cap,
        t26 (plan this year), f26 (fact Jan-Sep this year), t27 (target next year)},
known {param: 1 if sourced from data, 0 if assumption},
infoSrc? {info key: "where this number came from"}  (overrides the generic source line in the i panels),
sources "one paragraph: every number and where it came from; what is an assumption",
interview? {done: [...], next: N}
```

`t26`, `f26`, `t27` are fixed key names; the page labels them with the real years from `firstMonth`.

Model rules the page states to the reader (keep them true if you change the engine): forward plan, the
goal is a yardstick; Point A = previous year + closed quarters of this one; one intro-call stage; deal lag
in months, with pre-horizon calls at Point A pace; a channel with fewer than 5 Point A calls uses the
all-channel conversion; revenue by offer mix, billing from the win month; base rows with an end date
stop, the others decay by churn; hours = actions + calls + proposals vs hours/week × 13; cost = hours ×
rate + channel tools.

## Guardrails

- Client pages use the client's brand (`--brand`).
- Real configs contain client names and revenue: never publish or share them outside the owner's account, and never commit them to a public repo.
- Point A comes from money (P&L) and calendars, not from CRM statuses alone: CRMs under-record wins, often by a wide margin. Reconcile the two before trusting either.
- The engine is built for an October start (Q4 of this year + next year). For another start month the model in `assets/planner.html` (`HOR`, the quarter labels and the year split) has to be changed first.

## Credits

Method, interview and planner engine by Victor Shulga (victorshulga.com).
