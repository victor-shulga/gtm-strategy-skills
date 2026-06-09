# Довідник: структура Notion-виходу

Усі артефакти GTM-флоу складаються в Notion українською. Цей файл описує цільову структуру.
Скіли звертаються до Notion через Notion MCP (`notion-search`, `notion-create-database`,
`notion-create-pages`, `notion-fetch`, `notion-update-page`).

---

## Ієрархія

```
[Notion teamspace/parent] (узгоджується на старті — за замовч. шукаємо «GTM Strategy»)
└── DB «GTM Strategy» (база даних проєктів)
    └── Сторінка клієнта = назва агенції (+ URL, дата, стадія, SMF-діра, статус)
        ├── 01 · Company Snapshot
        ├── 02 · Stage Diagnostic        ← GATE 1
        ├── 03 · ICP / Tier A            ← GATE 2
        ├── 04 · Personas + JTBD
        ├── 05 · Value Proposition
        ├── 06 · Offers + Use Cases
        ├── 07 · Competitor + Gap
        ├── 08 · Buyer's Journey
        ├── 09 · Materials Plan
        ├── 10 · Channels Plan
        ├── 11 · Docs Plan
        └── 12 · Action Plan 30-90-180   ← GATE 3
```

## Поля бази «GTM Strategy» (properties сторінки клієнта)

| Поле | Тип | Значення |
|------|-----|----------|
| Name | title | Назва агенції |
| URL | url | Сайт |
| Stage | select | 0 / 1 / 2 / 3 / 4 |
| Stage confidence | select | low / med / high |
| SMF gap | multi-select | L / Cr / $ / # |
| AGA focus | multi-select | M1 / M2-M3 / M4 / M5 |
| Status | select | Intake / Diagnosed / In progress / Plan ready |
| Date | date | дата аудиту |

## Правила запису

1. **Одна сторінка клієнта** = один URL. Перед створенням `notion-search` → якщо є, оновлюємо
   (`notion-update-page`), не дублюємо.
2. Кожен крок створює/оновлює **свою під-сторінку** з префіксом `NN · Назва`.
3. Мова контенту — **українська**. Терміни-якорі (ICP, JTBD, MEDDIC, win-rate) лишаємо як є.
4. Кожна під-сторінка завершується блоком **«Джерела / припущення»** (що взято з сайту, що —
   гіпотеза cold-audit), бо це аудит без даних клієнта.
5. Стадійно-нерелевантні секції **не створюємо** (adaptive), а в Action Plan позначаємо як «передчасно».

## Якщо Notion недоступний

Fallback: писати ті самі артефакти у локальні markdown-файли
`./gtm-output/<agency-slug>/NN-*.md` і повідомити користувача.
