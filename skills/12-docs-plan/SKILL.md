---
name: 12-docs-plan
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

## Вихід (Notion)
Під-сторінка **«12 · Docs Plan»**: stage relevance · scored inventory (+Readiness %) · gap/actions +
що покрито флоу · «Джерела / припущення». Українською.

## Definition of Done
- Stage relevance + overshoot-попередження (для ранньої стадії).
- Scored inventory stage-relevant доків: Категорія (№ + назва) + Status + Quality Score + **Readiness %** (AGA — внутрішній, не в клієнтській таблиці).
- Явно позначено доки, **покриті цим GTM-флоу** (не дублювати).
- Gap: що написати першим (під outbound) з owner/дедлайн. Notion-сторінка створена.
