# Project context

Read this first. It is the shared brain for Claude Code, Cowork, and chat — whichever is
running, these are the standing facts and conventions.

## What this is

A single-niche product brand, sold into the EU, operated from Bulgaria. Dropshipping is
the **validation logistics for months 1–4**, not the business model. We are not building
a dropshipping store.

## Decisions already made — do not relitigate

| Decision | Value | Where |
|---|---|---|
| Target market | **EU**, operated from Bulgaria | `docs/03` |
| Business model | Single-niche brand, organic-first, dropship→3PL | `docs/00` |
| Acquisition | Organic content first. Paid only after Gate 3. | `docs/04` |
| VAT posture | Stay under €100k EU SME threshold during validation | `docs/03` |
| Niche | **OPEN** — audience-first, see `docs/02` | — |
| Supplier | **OPEN** — GoShipPro is a candidate, needs EU quotes | `docs/02` |

## Standing facts (Aug 2026)

- EU abolished the €150 duty relief on 1 Jul 2026. Flat **€3/item** transitional duty
  until the Customs Data Hub lands mid-2028, plus **€2 handling** from 1 Nov 2026.
- US de minimis suspended indefinitely since Jun 2026, statutory repeal Jul 2027. This is
  why we are not selling into the US.
- Bulgaria: 10% flat corporate tax, euro since 1 Jan 2026 (1.95583 BGN), VAT registration
  threshold €51,130 on a calendar-year basis, EU SME scheme exempt under €100k.
- Meta CPM ~$10.42 ecommerce, +20% YoY. Benchmark cold-paid CAC ≈ **$65**. Assume worse
  for a new store.

## Hard rules

1. **Run the numbers before believing anything.** `python3 tools/unit_economics.py`. Six
   gates in `docs/01`. A product that fails on paper fails in reality.
2. **No fabricated testimonials, invented customer stories, or fake social proof.** Not
   in ads, listings, reviews, or content. FTC 16 CFR 465 and EU consumer law both bite,
   and liability sits with us. Copy is first-person-true or attributed to a real named
   source.
3. **No health, medical, or outcome claims.** Describe the problem, never promise the fix.
4. **Excluded categories:** electronics, batteries, cosmetics, supplements, kids' items,
   anything medical. See `docs/02`.
5. **Fixed burn under €100/month** until Gate 3 passes.
6. **Contribution dollars per order, measured not projected**, is the only metric that
   matters.

## Repo layout

```
docs/00-reality-check.md      market conditions, what's dead, what survives
docs/01-unit-economics.md     the model + three worked scenarios
docs/02-product-selection.md  audience-first method, 10 hard filters, sourcing
docs/03-operations.md         market decision, stack, SLAs, legal/tax
docs/04-90-day-plan.md        phased plan, four kill gates, budget
docs/05-risks.md              ranked risks, pre-mortem, stop-loss
docs/06-workflow.md           how Code and Cowork stay in sync
tools/unit_economics.py       contribution margin / breakeven CAC calculator
research/                     working notes, supplier quotes, candidate briefs
```

## If you are Cowork working in a local folder

This folder is a git clone. **Git is the only bridge between you and Claude Code.** A
file you write here is invisible to Claude Code until it is committed and pushed.

At the **start** of every session, before reading or editing anything:

```bash
git pull
```

At the **end** of every session, or whenever you finish a piece of work:

```bash
git add -A
git commit -m "short description of what you did"
git push
```

If you cannot run shell commands, **say so explicitly** rather than skipping this — the
work will otherwise sit on one machine and quietly diverge. Tell the user to run the
three commands above, or to hand the files to Claude Code.

If `git pull` reports a conflict, stop and ask. Do not force anything.

## Tool ownership — respect this or the two agents will fight

- **Claude Code owns `docs/`, `tools/`, and this file.** Durable decisions, anything
  version-controlled, anything that is code.
- **Cowork owns `research/` and working documents in Google Drive.** Supplier
  comparisons, content calendars, drafts, the objection log.
- **Promotion:** when something in `research/` becomes a decision, it gets written into
  `docs/` and committed. That commit is what makes it real.
- **Always pull before editing.** Both tools write to this repo. See `docs/06`.

## Conventions

- Working branch: `claude/dropshipping-business-plan-60p144`. PR #1.
- Currency: EUR. Prices to EU customers are what the customer pays.
- Cite sources for market claims. Link them. We check numbers, we do not recall them.
- When a fact here goes stale, update this file in the same commit as the change.
