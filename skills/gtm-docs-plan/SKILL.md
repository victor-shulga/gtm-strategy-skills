---
name: gtm-docs-plan
description: Step 12 of the GTM flow. Recommend which INTERNAL documents/playbooks to formalize, from the 47-docs-by-5-stages matrix (Doc 2), as a scored inventory (status, quality score 0/1/2, readiness percentage) with how-to-create and AGA mapping. Key insight - several strategy docs are already produced by this GTM flow (ICP=03, competitive=05, positioning=06, value prop=07, buyer journey=09), so mark them as covered. Recommendations only, stage-adaptive (stage 0 = near-zero, do not formalize prematurely). Use when the user asks внутрішні документи, playbooks, SOP, documentation, what docs to write, sales playbook, onboarding docs. Writes to Notion in Ukrainian.
argument-hint: "(reads stage + prior GTM artifacts from steps 2-11 in Notion)"
---

# 12 · Internal Docs Plan (scored)

Дванадцятий крок. Які **внутрішні документи/плейбуки** формалізувати — за матрицею **47×7** (Doc 2),
як scored inventory + gap + пріоритет. Recommendations only. Без гейту.

Вхід — 02 (стадія + AGA), усі попередні артефакти (03/05/06/07/08/09 — частина доків уже з них). Прочитай
`${CLAUDE_PLUGIN_ROOT}/reference/agency-stages.md` §7 (47 доків за стадіями), §8 (overshoot/undershoot).

## Принципи (Doc 2)
- **3 правила доку:** (1) документує процес, що ВЖЕ працює; (2) має owner'а; (3) слугує ролі, що ВЖЕ найнята.
- **Стадія диктує к-сть:** 0 → ~0 (усе в голові CEO; формалізація = передчасні витрати) · 1 → ~16 ·
  2 → ~32 · 3 → ~46 · 4 → 47.
- **Багато стратегічних доків уже виробляє ЦЕЙ флоу** — не дублюй: ICP card / persona = 03 ·
  competitive landscape = 05 · positioning doc = 06 · value prop framework = 07 · buyer journey map = 09 ·
  buying signals = 03(тригери). Познач їх «covered by GTM flow».

## Категорії (Doc 2 §7)
1. Стратегія / ICP / шлях клієнта · 2. Demand gen · 3. Sales toolkit · 4. CRM / Process ·
5. AM / CS playbooks · 6. HR / Onboarding · 7. Knowledge / Leadership.

## Що зібрати
**1 · Stage relevance.** Скільки доків доречно на стадії (Стадія 0 → ~0: попередь про overshoot;
але якщо клієнт виходить в outbound — мінімальний стартовий набір під перші кампанії/угоди).
**2 · Scored inventory** (тільки stage-relevant): таблиця — *Doc · Категорія (№ + назва) · Status (To-Do/
In progress/Done) · Quality Score (0/1/2) · Priority · How-to-create / covered-by (крок флоу або хто пише)*.
+ **Readiness % = Σ score / (2×N)**. Категорії: **1 Стратегія/ICP/шлях клієнта · 2 Demand gen ·
3 Sales toolkit · 4 CRM/Process · 5 AM/CS · 6 HR/Onboarding · 7 Knowledge/Leadership**.
> **AGA-модуль — внутрішній маркер консультанта**, у клієнтський артефакт НЕ виносимо.
**3 · Gap + дії:** що **вбити/відкласти** (передчасні доки — AM/CS, OKR, leadership на ранній стадії) ·
що **написати першим** (критичні під outbound + перші угоди) · owner/дедлайн.

## Stage-adaptive глибина
- **Стадія 0:** ~0 обов'язкових; познач, що Категорія 1 (стратегія) **покрита цим аудитом**; перші НОВІ
  доки під outbound: hypothesis matrix, outbound playbook, email templates, discovery script, BANT.
- **Стадія 1:** ~16 стартових (Strategy + Demand + базовий Sales/CRM + onboarding + comp).
- **Стадія 2:** +Sales playbook, objection handlers, battle cards, client onboarding, lead scoring.
- **Стадія 3-4:** AM/CS playbooks, SLA, OKR, leadership cadence, board update.

## Terms and plain-language output

<!-- glossary:start terms=readiness-score,status-todo,playbook-sop,bant-meddic,qbr,sla,okr,lead-scoring,hypothesis-matrix,overshoot-undershoot,agency-stage -->
Rules for every document a client or their team will read (review, roast, canvas, offer cards, instruction):

1. **Open with «Словник цього документа»**: only the terms that actually appear in it, at most 10, each as «термін: що це простими словами». Like the definitions section of a contract.
2. **No internal codes or letter scales in the text** (A/B/C, D L T E, BLEND numbers without words, Own/Shared/Generic, Z1.4, GATE 2.5, T1–T6). Write the meaning instead: «є цифра з клієнтом», not «A».
3. **Use the plain form from the table below.** English stays only for tool names and for copy that ships in English (promises, hooks, subject lines). If the document is in another language, translate the plain form, never the internal term.
4. **Do not score what cannot exist yet.** A block that depends on work not done (signal catalog, case studies, a previous step) gets «пропущено: спершу потрібно <що саме>», not a score.
5. **Every section of a review opens with one concrete action** («до наступного дзвінка: …»), then at most five lines of why. No paragraph that only restates the framework.


| Internal term (this skill) | Write for the reader | What it means |
|---|---|---|
| Quality Score 0 / 1 / 2, Readiness % | якість: немає · є, але слабке · готово; загальна готовність у відсотках | кожен матеріал чи документ оцінюємо від 0 до 2, відсоток показує, скільки з потрібного вже є. |
| Status To-Do / In progress / Done | не почато · в роботі · готово | стан кожного пункту в списку. |
| playbook, SOP | інструкція з продажів · покрокова інструкція | записаний порядок дій, за яким команда працює без засновника. |
| BANT, MEDDIC | чек-лист кваліфікації угоди | питання, які перевіряють бюджет, того, хто вирішує, потребу і терміни, перш ніж вкладатися в угоду. |
| QBR | квартальна зустріч з клієнтом | раз на квартал разом з клієнтом підсумовуєте результати і плануєте наступні кроки. |
| SLA (marketing ↔ sales) | домовленість між маркетингом і продажами | хто передає ліда, у якому вигляді і за скільки годин на нього реагують. |
| OKR | цілі й ключові результати | ціль словами плюс 3–5 вимірюваних результатів, переглядаємо щомісяця. |
| lead scoring | оцінка лідів | бали, за якими видно, з ким говорити першим. |
| hypothesis matrix | таблиця гіпотез | список варіантів «кому · з чим · через який канал» для перевірки в розсилках. |
| overshoot / undershoot | передчасне · запізніле для вашої стадії | матеріал чи документ, зроблений раніше, ніж він окупиться, або той, без якого стадія вже гальмує. |
| Stage 0–5, стадія агенції | стадія розвитку компанії (0–5) | шість щаблів від «CEO робить усе» до «портфель напрямів»; від стадії залежить, що доречно робити зараз. |
<!-- glossary:end -->

## Вихід (Notion)
Під-сторінка **«12 · Docs Plan»**: stage relevance · scored inventory (+Readiness %) · gap/actions +
що покрито флоу · «Джерела / припущення». Українською.

## Definition of Done
- Stage relevance + overshoot-попередження (для ранньої стадії).
- Scored inventory stage-relevant доків: Категорія (№ + назва) + Status + Quality Score + **Readiness %** (AGA — внутрішній, не в клієнтській таблиці).
- Явно позначено доки, **покриті цим GTM-флоу** (не дублювати).
- Gap: що написати першим (під outbound) з owner/дедлайн. Notion-сторінка створена.
