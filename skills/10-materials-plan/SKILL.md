---
name: 10-materials-plan
description: Step 10 of the GTM flow. Plan the marketing materials/content as a SCORED inventory mapped to the buyer journey — each asset gets a status (To-Do/In progress/Done), a quality score (0/1/2) and an overall readiness percentage, plus how-to-create (which framework/step produces it) and an interface breakdown (website sections, LinkedIn profile, cold email). Recommendations only (inventory + gap + overshoot/undershoot + 3-5 actions), stage-adaptive via the 22-materials-by-5-stages matrix. Use when the user asks materials, content plan, які матеріали потрібні, content audit, asset inventory, readiness score, что создавать. Writes to Notion in Ukrainian.
argument-hint: "(reads stage + buyer journey + ICP/positioning/VP/offers from steps 2-9 in Notion)"
---

# 10 · Materials / Content Plan (scored)

Десятий крок. Спланувати **матеріали/контент** як **scored inventory, прив'язаний до buyer journey**
(09). НЕ генеруємо самі ассети — даємо inventory + gap + пріоритети (рішення з архітектури). Без гейту.

Вхід — 02 (стадія), 09 (шлях клієнта + контент-на-стадію), 03/05/06/07/08 (для «how to create»). Прочитай
`${CLAUDE_PLUGIN_ROOT}/reference/agency-stages.md` §6 (матриця 22×5 — ЩО релевантно стадії) і §8
(overshoot/undershoot). Формат — за content-plan документом Viktor'а (scored inventory + how-to-create).

## Що зібрати

**1 · Контент × стадія journey.** З 08 — які типи контенту впливають на покупця на кожній стадії
(problem-unaware → business trigger → problem-aware → solution-aware → alternatives → objections →
consideration → decision). 1 рядок на стадію: що тут доречно.

**2 · Materials inventory (scored).** Для кожного **релевантного стадії** матеріалу (фільтр — матриця
22×5 + wedge): таблиця з полями:
- *Material* · *Maps-to-stage* (journey) · *Status* (To-Do / In progress / Done) ·
  **Quality Score (0 / 1 / 2)** · *Priority* · **How-to-create** (фреймворк/крок: ICP(03) · Value
  Prop canvas(07) · Positioning(06) · Buyer journey(09) · Customer interview · Competitor(05) · Offer(08)).
- **Readiness % = Σ score / (2 × N)** — загальна готовність матеріалів (як у документі: напр. 56.9%).

**3 · Interface breakdown.** Ключові поверхні → segment → deliverable → джерело (framework). Бери лише
релевантні стадії. Приклади:
- *Website:* service page → Services (Messaging); Hero → UVP (VP canvas) · Positioning (Messaging) ·
  ICP (ICP framework); Social proof → client logos/testimonials (Customer interview); FAQ → objections.
- *LinkedIn profile:* banner → client logos; tagline → positioning/ICP; About → benefits; projects → cases.
- *Cold email:* opening → buying signal (ICP); problem → Messaging; credibility → case study; offer → Offer framework.

**4 · Gap + дії** (Doc 2 §8): що **вбити/заморозити** (overshoot — передчасне для стадії) · що
**збудувати за 30 днів** (критичний gap, найнижчий score на високому Priority) · що **переробити**.
Кожна дія — owner + дедлайн + бюджет.

## Stage-adaptive глибина
- **Стадія 0-1:** лише stage-relevant (founder LinkedIn, простий лендінг, 3 короткі кейси, 1-pager,
  proposal, hook-аудит). Score їх (часто 0 — це чесно). Без website/service-pages/industry-report.
- **Стадія 2:** + повний сайт, сервісні сторінки, lead magnets, case studies за template, video.
- **Стадія 3-4:** повний inventory + ROI calculator, industry report, partnership kit.

## Принципи
- **Recommendations only** — не пишемо самі матеріали (це окремі скіли/робота).
- Матеріал слугує **каналу, що працює** + **оферу, що продається** + **людині, що найнята** (3 правила Doc 2).
- Score чесно: відсутній = 0. Низький Readiness % на Стадії 0 — це нормально й actionable.

## Вихід (Notion)
Під-сторінка **«10 · Materials Plan»**: (1) контент×стадія · (2) scored inventory + **Readiness %** ·
(3) interface breakdown · (4) gap/overshoot/undershoot + 3-5 дій · «Джерела / припущення». Українською.

## Definition of Done
- Контент змаплено на стадії journey (09).
- Scored inventory зі Status + Quality Score (0/1/2) + **Readiness %** для stage-relevant матеріалів.
- How-to-create (framework/крок) на кожен; interface breakdown для релевантних поверхонь.
- Gap: ≥1 «вбити», ≥1-2 «збудувати за 30 днів», з owner/дедлайн/бюджет. Notion-сторінка створена.
