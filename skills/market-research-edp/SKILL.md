---
name: market-research-edp
description: >-
  Researches a vertical or segment for a B2B service company (agency, dev or IT outsourcing,
  AEC/BIM outsourcing, consultancy) and finds its existential data points: facts about the
  buyer's business that make the problem urgent and the service a must-have, such as
  regulation deadlines, hiring gaps, project backlogs, margin pressure or platform end-of-life.
  Every number is sourced and confidence-rated, unsourced claims are parked as hypotheses,
  and each data point becomes a per-account trigger plus an outbound opener. Use for "research the market for X", "find urgency in this vertical", "why would
  they buy now", "EDP", "pain in [vertical]", "дослідження ринку", "чому їм терміново",
  "тригери терміновості", "біль сегмента", "оціни ринок". Used by 03-market-icp-persona and
  04-market-sizing.
  NOT for TAM/SAM/SOM math (04-market-sizing), NOT for the competitor map
  (competitor-finder), NOT for live signal detection (signal-research).
---

# Market research: existential data points

An existential data point (EDP) is a fact about the buyer that turns "interesting, maybe later" into "we have to sort this out this quarter." For a service company the EDP is almost never about the service itself. It sits in the buyer's world: a compliance date they cannot move, a role they have failed to hire for months, a backlog that delays revenue, a client who now demands a standard they cannot meet.

This skill finds those facts for one vertical or segment, proves them with sources, and turns each into something outbound can use.

Answer in the user's language.

## Boundary with 04-market-sizing

This skill can record numbers that describe the market (number of firms, growth rate) when they appear in sources, but it does not do the sizing math. Pass any such figures with their URLs to `04-market-sizing`, which owns TAM/SAM/SOM.

## Inputs (ask once, in one message)

1. The vertical or segment, with geo and company size (for example: "UK MEP contractors, 50 to 500 staff", "US digital agencies with 20 to 100 people that white-label development").
2. The service being sold to them.
3. A hunch to validate, if any ("we think the pain is the shortage of BIM coordinators").
4. Depth: scan (about 10 sources, 3 to 4 EDPs) or deep (25+ sources, 5 to 7 EDPs, segment split).

## Step 1. Map the buyer's economics

Before searching for pain, write five lines on how the buyer makes money and what limits it:
- revenue model (project fees, billable hours, retainers, product sales)
- the scarce resource (qualified people, project slots, cash, certification)
- who pays them and what that payer increasingly demands
- the cost they watch most closely
- the event that ruins a year for them (losing a framework contract, a failed audit, a key person leaving)

Urgency lives where one of these five is under pressure. Use the list to steer the searches.

## Step 2. Hunt for candidate data points

Search across the six urgency families below. For each family run at least two targeted queries; in deep mode, at least four.

| Family | What it looks like in service-buyer markets | Where to look |
|---|---|---|
| Rule with a date | A regulation, standard or public-procurement requirement with an enforcement or mandate date | Regulator and government sites, official journals, trade association guidance |
| Talent gap | Roles open for months, wage growth above inflation, shrinking graduate pipeline | Job boards (count of open posts, time open), national statistics, association workforce surveys |
| Backlog | Work won but not delivered, delayed projects, capacity-constrained growth | Industry backlog indices, public company filings, trade press |
| Margin squeeze | Fixed-price contracts with rising costs, client pressure on rates | Annual reports, association benchmark surveys, earnings calls |
| Platform shift | End of support, forced migration, new tool mandated by large clients | Vendor lifecycle pages, release notes, client tender documents |
| Payer pressure | The buyer's own clients start requiring a capability or proof | Tender portals, RFP language, procurement frameworks |

Practitioner voice (Reddit, forums, LinkedIn posts, review sites) is useful to confirm that the pain is felt. It does not replace a primary source for the number.

## Step 3. Grade each source

- **A:** primary (regulator, statistics office, association survey with method, audited filing), published in the last 24 months
- **B:** reputable secondary (analyst firm, established trade press) or primary older than 24 months
- **C:** practitioner content, single-company data, vendor research with a stated method
- **D:** vendor marketing without method, AI-generated summaries, unattributed stats

D sources are never used as the basis of an EDP. A number that appears in many articles with no traceable origin gets traced to its origin or dropped.

## Step 4. Filter candidates into EDPs

Score each candidate 0, 1 or 2 on four tests:

1. About the buyer: describes the buyer's business (a market-size figure scores 0)
2. Has a clock: a deadline, or a loss that grows every month it is ignored
3. Visible per account: you can tell from outside which companies are exposed (a job post, a tender win, a filing, a certification list)
4. Your service moves it: the service directly reduces the exposure, without three steps in between

A candidate with 6 or more out of 8 and at least one A or B source becomes an EDP. Others go to the hypotheses list with what is missing.

## Step 5. Convert each EDP into an outbound asset

For every EDP produce:
- **Account trigger:** the observable signal that marks one company as exposed, and where to detect it
- **Opener:** one or two sentences in the buyer's language, referencing the fact, ending in a question. No pitch in the opener
- **Discovery question:** what to ask on a call to confirm the EDP applies to this company
- **Proof needed:** the case or sample the seller must have to be credible on this topic

## Step 6. Split the segment by exposure (deep mode)

Group the segment into 2 to 4 sub-segments that feel different EDPs hardest (by size, sub-vertical, geo or client type). For each: the EDP that hits hardest, the trigger, and a one-line angle. These become candidate hypotheses for outbound.

## Output template

```
# EDP research: [segment] · [service] · [date] · depth: [scan / deep]

## Buyer economics
[five lines from Step 1]

## EDPs (ranked)
### EDP 1: [short name]
Fact: [the number or rule, exact wording] · Source: [URL] · Grade: [A/B] · Date of source: [ ]
Score: buyer [ ] clock [ ] visible [ ] moves [ ] = [ ]/8
Why it is urgent: [two sentences]
Account trigger: [signal + where to detect]
Opener: "[text ending in a question]"
Discovery question: [ ]
Proof needed: [ ]
Confidence: [high / medium / low] because [reason]

## Sub-segments by exposure (deep mode)
| Sub-segment | Hardest EDP | Trigger | Angle |

## Hypotheses to verify
| Candidate | What is missing | How to verify |

## Figures handed to 04-market-sizing
| Figure | Value | Source |

## Sources
[grouped by family, with grade]
```

Confidence rule of thumb: high = A source and visible per-account trigger; medium = B source, or A source with a weak trigger; low = C source only (allowed only in the hypotheses list).

## Quality gate

- [ ] Every number has a URL and a grade; nothing rests on a D source
- [ ] At least one EDP has a clock with a specific date or monthly loss
- [ ] Each EDP has an account trigger someone can actually check
- [ ] Openers end with a question and use buyer words, without a pitch
- [ ] Sizing figures moved to the hand-off table, not interpreted here
- [ ] At least one finding the user did not expect, or an explicit note that the hunch was confirmed with sources

## Hand-offs

- Market choice, ICP tiers and personas: `03-market-icp-persona` (this pack)
- Sizing: `04-market-sizing` (this pack)
- Building detection for the account triggers: if installed, `signal-research` (pack `outbound-engine-skills`)
- Turning EDPs into tested hypotheses and copy: if installed, `hypothesis-builder` and `sequence-writer` (pack `outbound-engine-skills`), or `angle-finder` (same pack)
- Finding data sources for a niche trigger: if installed, `niche-data-finder` (pack `outbound-engine-skills`)

## Credits

Idea adapted from lemlist's public `market-research-edp` skill (github.com/l3mpire/claude-skills); rewritten for B2B service companies.
