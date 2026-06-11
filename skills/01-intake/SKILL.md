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
   **+ Скоринг позиціонування (cold).** Оцінюй ТІЛЬКИ те, що бачить холодний відвідувач за
   5 секунд на позиційних поверхнях (hero/H1/tagline/above-the-fold головної). Кожен пункт
   0 / 0.5 / 1 + verbatim-доказ або «нема»:
   - **Positioning — X out of 5:** (1) ICP названий; (2) industry/category названі;
     (3) the problem you solve зрозуміла; (4) use case зрозумілий; (5) offer зрозумілий.
   - **Value Proposition — X out of 4** (value equation Hormozi): (1) Dream Outcome аудиторії;
     (2) пруфи (perceived likelihood); (3) Time Delay to get the result; (4) Effort & Sacrifice
     (що треба від клієнта / наскільки безболісно).
   Це cold-скоринг «як є» — сировина для `06-positioning` (там enemy-кут і Z1.4 self-score),
   не фінальний вердикт.
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
12. **Трафік і SEO (Ahrefs MCP + SimilarWeb).** Обов'язкова секція кожного снапшота:
    - **Ahrefs MCP** (основне джерело): DR + backlinks stats, `site-explorer-metrics-history`
      (organic traffic за 24 міс, monthly, `mode=subdomains`), top-pages за трафіком,
      топ organic keywords. Перед першим використанням перевір юніти через
      `subscription-info-limits-and-usage` (безкоштовний) — **Trial-акаунт має 0 API units**,
      тоді познач «Ahrefs недоступний, дозбирати після апгрейду» і не пали виклики.
    - **Semrush MCP** (сервер `semrush`, https://mcp.semrush.com/v1/mcp, user scope, OAuth):
      станом на 2026-06-10 план Viktor'а **не включає MCP-доступ** — тули відповідають
      відмовою про план. Пробувати першим викликом; якщо відмова — познач і йди далі.
    - **SimilarWeb (безкоштовний, основний робочий шлях):**
      (а) lite-endpoint `https://data.similarweb.com/api/v1/data?domain=<домен>` через
      WebFetch — візити/міс (3 міс історії), bounce/pages/duration, гео, ранки;
      (б) Apify-актор `tri_angle/similarweb-scraper` (permissions підтверджено, ~$0.06/домен) —
      додає топ-органік-запити, similarity-конкурентів, зміни гео-часток, technographics.
      Для сайтів <50K/міс цифри приблизні — познач це. `epctex/similarweb-scraper` —
      платна підписка $15/міс, НЕ використовувати.
    - **Інтерпретація обов'язкова:** трафік росте/плоский/падає; конвертується чи ні
      (lead magnets? CTA?); чи збігається гео з цільовим ринком. Це сировина для SMF-діри L
      та `11-channels-plan`.

## Стадійні проксі-сигнали
Окремим блоком познач, які зі знайдених ознак вказують на стадію 0/1/2/3/4
(див. `${CLAUDE_PLUGIN_ROOT}/reference/agency-stages.md`, розділ 1 — cold-audit проксі-сигнали).
Це **сировина для `02-stage-diagnostic`**, тут стадію ще не оголошуй.

## Вихід (Notion)
Створи/онови під-сторінку **«01 · Company Snapshot»** на сторінці клієнта (див.
`${CLAUDE_PLUGIN_ROOT}/reference/notion-schema.md`). Структура: розділи 1–12 вище + блок
**«Стадійні проксі-сигнали»** + блок **«Джерела / припущення»** (які сторінки прочитані, де гіпотеза).
Українською; назви сервісів і verbatim-фрази — мовою оригіналу.

## Definition of Done
- Усі 12 секцій заповнені (де даних нема — явно «не знайдено», не вигадуй).
- Секція 3 містить скоринг: Positioning X/5 + Value Proposition X/4, кожен пункт із
  verbatim-доказом.
- Секція 12: трафік-овервʼю зібрано (Ahrefs або SimilarWeb-фолбек); якщо Ahrefs без юнітів —
  це явно позначено в секції та в «Джерела / припущення».
- ≥ 5 verbatim-фраз мови клієнта зібрано.
- Секція 11: company-LinkedIn перевірено (знайдено/нема); підраховано біздев-ролі; founder ідентифіковано
  або явно «публічно не знайдено».
- Блок стадійних проксі-сигналів готовий для кроку 2 (з урахуванням складу команди).
- Під-сторінка в Notion створена; повернено короткий summary оркестратору.
