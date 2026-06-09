---
name: 01-intake
description: Step 1 of the GTM flow. Scrape an IT agency website (cold audit) and produce a structured Company Snapshot — services, claims, positioning, proof and case studies, pricing signals, team-size hints, tech, target hints, and the agency own customer language. Use when starting a GTM strategy from a URL, or when the user asks to scan or scrape the agency site, intake the company, or make a company snapshot. Writes the snapshot to the client Notion page in Ukrainian.
argument-hint: "<agency-website-url>"
---

# 01 · Intake — Company Snapshot

Перший крок GTM-флоу. Зібрати з **публічного сайту** агенції структурований знімок, на якому
будуються всі наступні кроки. Це **cold audit** — жодних даних клієнта, тільки те, що видно ззовні.

**Вхід:** URL сайту (`$ARGUMENTS`).

## Реюз
- Спершу виклич скіл **`website-scraper`** для збору сторінок (home, services, cases, about, pricing,
  blog, careers, contact).
- Потім виклич **`deep-company-analyser`** для витягання pain points, customer language, proof і
  positioning-сигналів.
- Якщо цих скілів нема — зроби те саме через `WebFetch`/`WebSearch` по ключових сторінках сайту.
- **SPA-фолбек:** якщо сайт клієнт-рендериться (WebFetch/rag-web-browser віддають лише `<title>`),
  візьми Apify `apify/website-content-crawler` (`crawlerType: playwright`, `dynamicContentWaitSecs`).
- **LinkedIn-команда (Apify):** для секції 11 знайди company-LinkedIn (web search `"<назва>" site:linkedin.com`),
  тоді: `scrapemint/linkedin-company-employees-scraper` (безкоштовний огляд: headcount + розподіл ролей +
  featured) і `harvestapi/linkedin-company-employees` (ростер; фільтр `functionIds` 25=Sales, 15=Marketing,
  4=Business Development). Founder — web search `"<назва>" founder/CEO` + LinkedIn.

## Що зібрати (Company Snapshot)

1. **Ідентифікація:** назва, домен, рік/«since», гео-сигнали, мови сайту.
2. **Послуги:** перелік сервісів як їх називає сайт (verbatim) + чи є фокус, чи «все для всіх».
3. **Позиціонування (як є):** хедлайн/hero, кому адресовано, заявлена унікальність, tagline.
4. **Цільові натяки:** індустрії/розмір клієнтів/типи проєктів, які згадуються.
5. **Proof:** кейси (скільки, чи з $-результатами, named/анонімні), лого клієнтів, відгуки, нагороди,
   Clutch/рейтинги.
6. **Цінові сигнали:** є pricing/тіри/«from $», «contact us», productized vs bespoke.
7. **Команда:** розмір (із about/careers/LinkedIn-натяків), видимі ролі (founder, sales, marketing, AM),
   вакансії BizDev-ролей.
8. **Канали presence:** company LinkedIn (активна/порожня), особистий LinkedIn founder'а, блог/SEO,
   lead magnets, Upwork/Clutch профілі.
9. **Технологічні сигнали:** стек (Wappalyzer-стиль, якщо доступно), якість сайту (лендінг / повний /
   сервісні сторінки / ROI-калькулятори).
10. **Мова клієнта (verbatim):** 5–15 фраз із сайту, якими агенція описує проблеми/вигоди — сировина
    для VP і copy на наступних кроках.
11. **LinkedIn: команда та біздев (Apify).** Окрема секція — реальний склад команди, не з сайту:
    - **Headcount (поточний) + тренд росту 6м/1р/2р + median tenure** — головні сигнали динаміки.
      Джерела за пріоритетом: (1) **li_at cookie-актор** (LinkedIn-сесія з `userConfig.linkedin_li_at`):
      тягне повний ростер + staffCount, а Sales-Navigator-aware актор — і тренд 6м/1р/2р + median tenure;
      (2) фолбек — **LinkedIn Premium** «Total employee count», вставлений консультантом (скрін/число);
      (3) анонімні актори часто впираються в login wall (`name: "Join LinkedIn"` / null) → тренд
      недоступний, познач «потрібен li_at / Premium».
    - **Розподіл ролей** (scrapemint) + **ростер** (harvestapi).
    - **Біздев-функції:** скільки Sales / Marketing / SDR / BDM / AM (функції 25/15/4). **0 видимих
      біздев-ролей = founder-led, без двигуна** (сильний проксі Стадії 0-1).
    - **Founder(и):** ім'я, бекграунд, чи збігається з claim'ами сайту (напр. «20+ років» = особистий
      досвід founder'а чи команда entity?).
    - **Вік сутності:** найраніші tenure/«since» у профілях → наскільки бренд новий.
    - **Тех-сигнали з профілів:** стек у описах ролей (часто точніший за сайт — звужує ICP/офер).
    - ⚠️ Публічний LinkedIn недораховує неприв'язані профілі — це **підлога headcount**, не точне число.

## Стадійні проксі-сигнали
Окремим блоком познач, які зі знайдених ознак вказують на стадію 0/1/2/3/4
(див. `${CLAUDE_PLUGIN_ROOT}/reference/agency-stages.md`, розділ 1 — cold-audit проксі-сигнали).
Це **сировина для `02-stage-diagnostic`**, тут стадію ще не оголошуй.

## Вихід (Notion)
Створи/онови під-сторінку **«01 · Company Snapshot»** на сторінці клієнта (див.
`${CLAUDE_PLUGIN_ROOT}/reference/notion-schema.md`). Структура: розділи 1–11 вище + блок
**«Стадійні проксі-сигнали»** + блок **«Джерела / припущення»** (які сторінки прочитані, де гіпотеза).
Українською; назви сервісів і verbatim-фрази — мовою оригіналу.

## Definition of Done
- Усі 11 секцій заповнені (де даних нема — явно «не знайдено», не вигадуй).
- ≥ 5 verbatim-фраз мови клієнта зібрано.
- Секція 11: company-LinkedIn перевірено (знайдено/нема); підраховано біздев-ролі; founder ідентифіковано
  або явно «публічно не знайдено».
- Блок стадійних проксі-сигналів готовий для кроку 2 (з урахуванням складу команди).
- Під-сторінка в Notion створена; повернено короткий summary оркестратору.
