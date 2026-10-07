---
name: persona-insights-analysis
description: >-
  Turns discovery and sales call transcripts of a B2B service company (agency, dev or IT
  outsourcing, AEC/BIM outsourcing, consultancy) into a persona report built only on what
  buyers said: goals, pains, triggers, current setup, objections, decision process, buying
  signals and red flags, with exact quotes and a count of calls per theme. Adds a language
  bank for copy and recommendations for messaging, ICP and offer. Accepts pasted text, CSV,
  DOCX, PDF or a connected call-recording tool. Under 5 calls = directional. Use for
  "analyse my calls", "what are buyers saying", "build a persona from transcripts",
  "розбери транскрипти", "аналіз дзвінків", "що кажуть клієнти на дзвінках",
  "мова клієнта". Feeds 03-market-icp-persona, 06-positioning,
  persona-builder and sequence-writer.
  NOT for prep before one booked call (meeting-prep), NOT for outbound reply batches
  (reply-audit), NOT for personas without call data (persona-builder).
---

# Persona insights analysis

Positioning and copy in service companies are usually written from the seller's memory of calls. Memory keeps the dramatic quote and loses the boring one that came up in eight calls out of ten. This skill reads the transcripts, codes every buyer statement, counts it, and only then draws conclusions.

Answer in the user's language. Quotes stay in the language they were spoken in.

## Inputs (ask once, only what is missing)

1. **Transcripts:** pasted text, a CSV export, DOCX or PDF files, or a call-recording connector if one is connected in this environment (for example Fireflies, Fathom, Gong, tl;dv, Claap). Ask for a date range or tag if pulling from a connector.
2. **Which decision this should inform:** messaging, ICP, offer, or all three.
3. **Known personas** to group by, or permission to infer them from the data.
4. **Anonymisation:** may company names appear in the report? Default: no, use role and company type.
5. **Format:** markdown report (default), Notion page if a Notion connector is available, or a DOCX via the docx skill if available.

Call metadata, if the user has it, makes the analysis much stronger: call stage, outcome (won, lost, open, no decision), lead source (outbound, referral, inbound).

## Step 1. Normalise every call into one record

```
call_id · date · stage (discovery / scoping / proposal review) · outcome · lead source
buyer role(s) · company type · company size · geo · source format (full transcript / summary)
```

Summaries and AI notes count, but every finding drawn only from them is tagged `summary-based`. A CSV column holding a link to a transcript gets fetched if the link is reachable.

## Step 2. Keep only buyer speech as evidence

Mark who is the seller and who is the buyer in each call (introductions, who asks about pricing, who describes the service). When several buyer-side people are present, note each role. Seller statements are context: they show what was pitched, but they never count as evidence of what the buyer thinks.

## Step 3. Code each call with a fixed codebook

Go call by call. Every coded item records `call_id`, approximate timestamp if available, and the exact quote.

| Code | What qualifies |
|---|---|
| GOAL | What the buyer wants to achieve, including how their own boss or client measures them |
| PAIN | What is broken today and what it costs (time, money, reputation, stress) |
| TRIGGER | Why they took the call now: lost a key person, won a big project, a client demand, a failed vendor |
| SETUP | How they do it today: in-house team, current vendor, freelancers, nothing |
| OBJECTION | Doubts raised: price, trust in remote teams, IP and security, time zone, quality, switching effort |
| PROCESS | Who else decides, approvals, procurement steps, budget timing, trial or pilot expectations |
| SIGNAL | Intent shown: asks about start dates, team names, contract terms, a pilot scope |
| RED FLAG | Weak fit: no budget owner, "just exploring", use case outside your service |
| WORDS | Distinctive phrases for the problem, the outcome, and for vendors like you |

For OBJECTION also note how the seller answered and whether the buyer accepted it (`resolved`, `parked`, `ignored`).

## Step 4. Count across calls

Frequency is the number of calls in which a theme appears, not the number of times it was said. Merge near-identical themes before counting, and keep the merge list in the appendix.

Sample-size rule, stated at the top of the report:
- Under 5 calls: directional. Every finding gets the label `directional, n=[x]`. No percentages; write "3 of 4 calls".
- 5 to 14 calls: patterns. Report counts and percentages; split by persona only if each group has at least 3 calls.
- 15 calls or more: segment cuts are allowed (persona, company size, lead source). Compare won with lost if outcomes are known.

## Step 5. Build the persona cuts

Group buyers by their role in the purchase, then by company type:

- **Economic buyer:** signs and owns budget (founder, CEO, managing director, project director)
- **Champion or day-to-day owner:** feels the pain and manages the vendor (head of delivery, CTO, BIM manager, MEP lead, marketing lead)
- **Evaluator:** checks quality or risk (senior engineer, procurement, legal)

For each persona: the top 3 goals, top 3 pains, main triggers, objections ranked by frequency, the decision steps they described, and 5 to 8 quotes that carry the most information. Where the data has no quote for a field, write `no quote in data`.

## Step 6. Language bank

Collect phrases buyers used, grouped as:
- how they name the problem
- how they describe a good result
- what they call a provider like you (vendor, partner, outsourcing team, white-label, extension of our team)
- words that triggered pushback or that they explicitly disliked

Mark each phrase with the number of calls it appeared in. Copywriters use the high-count phrases verbatim.

## Step 7. Recommendations

Each recommendation points to its evidence (codes and counts). Group them:

- **Messaging:** the pain to lead with per persona, the opener built from a buyer phrase, claims to drop because nobody cared
- **ICP:** criteria to add or remove (for example, companies without an in-house lead to manage vendors stalled every time), with the call count
- **Offer:** packaging, pilot design, pricing form, guarantees that answer the top objections
- **Discovery:** questions to add, because a theme surfaced late or only when the buyer raised it
- **Objection handling:** the top objections with how the best-received answer in the data was phrased

Finish with the gaps: personas missing from the sample, stages not covered, and which 3 to 5 next calls would close them.

## Quote rules

- Copy quotes exactly as transcribed. Keep filler words if cutting them changes the meaning; mark cuts with `[...]`.
- Attribute by role and company type ("CTO, 40-person agency"), never by name unless the user allowed it.
- Never write a quote that is not in the data. Never merge two people's words into one quote.
- Poor transcription gets `[unclear transcript]` next to the quote.

## Output template

```
# Persona insights · [company] · [date]
Calls analysed: [n] ([x] full transcripts, [y] summaries) · Period: [ ] · Confidence: [directional / patterns / segmented]
Decision this informs: [messaging / ICP / offer]

## Top findings
[3 to 5 findings, each with count]

## Themes by frequency
| Theme | Code | Calls | Share | Example quote |

## Personas
### [Persona name]: [role in purchase] · calls: [n]
Goals · Pains · Triggers · Current setup · Objections (with handling result) · Decision process · Signals · Quotes

## Won vs lost (if outcomes known)
| Theme | In won calls | In lost calls |

## Language bank
| Phrase | Group | Calls |

## Recommendations
Messaging · ICP · Offer · Discovery · Objection handling

## Gaps and next calls

## Appendix: call list and merged themes
```

## Quality gate

- [ ] Sample size and confidence label are at the top
- [ ] Every finding shows a call count; under 5 calls has no percentages
- [ ] Every quote is traceable to one call_id and one speaker
- [ ] Seller statements are not counted as buyer evidence
- [ ] Each recommendation cites its evidence
- [ ] Company and person names follow the anonymisation choice

## Hand-offs

- Persona cards for outbound: if installed, `persona-builder` (pack `outbound-engine-skills`)
- ICP tiers and personas in the GTM flow: `03-market-icp-persona` (this pack)
- Positioning built on buyer language: `06-positioning` (this pack)
- Sequences using the language bank: if installed, `sequence-writer` (pack `outbound-engine-skills`)
- Objection replies: if installed, `reply-objection-handler` (pack `outbound-engine-skills`)

## Credits

Idea adapted from lemlist's public `persona-insights-analysis` skill (github.com/l3mpire/claude-skills); rewritten for B2B service companies.
