# 02 — Product & Niche Selection

Product selection is where this is won or lost. Not the store design, not the ad copy.

## Pick the audience before the product

The mistake is starting from "what product can I sell?" That leads to spy tools, which
lead to the same products everyone else found, which leads to competing on ad spend —
the one axis where you have no advantage.

Start instead from **an audience you can credibly make content for every day for six
months**. You need a specific group whose problems you understand well enough to talk
about on camera without research. That constraint is doing real work: it's what makes
the organic phase possible, and the organic phase is what makes the economics close.

Write down 3–5 candidate audiences you have genuine proximity to — a hobby, a job, a
condition, a subculture, a sport. Then find the product inside one of them.

## Hard filters

A candidate product must clear **all** of these. Any single ✗ is a rejection.

| # | Filter | Why |
|---|---|---|
| 1 | Sells at **$60+** (bundled if needed) | Contribution dollars must cover a real CAC |
| 2 | **≥45%** contribution margin after landed cost | See `01-unit-economics.md` |
| 3 | **Repeat purchase** or natural bundle/refill | LTV is what makes CAC survivable |
| 4 | **Light & small** (<2kg, fits a small box) | Shipping and duty scale with weight/value |
| 5 | **Not fragile** | Breakage is refunds, refunds are margin |
| 6 | **Visually demonstrable in <10s** | If it doesn't work on video, organic won't work |
| 7 | **Solves a specific problem** | Generic aesthetic products can't be differentiated |
| 8 | **Not** electronics, batteries, cosmetics, supplements, kids' items, or medical claims | Certification, liability, ad-policy, and customs risk |
| 9 | Not dominated by Amazon at a lower price | You cannot win a price comparison |
| 10 | Sourceable from **≥3 suppliers** | Single-supplier dependency is fatal |

Filter 8 deserves emphasis. Those categories aren't merely harder — they carry
regulatory and liability exposure that a first-time operator is not equipped to absorb.
Supplements and anything with a health claim in particular can generate consequences
well beyond losing your money.

## Research process

1. **Demand exists?** Google Trends (stable or rising over 24 months — avoid spikes),
   search volume, subreddit and Facebook group size. You want steady, not viral.
2. **Are people already paying?** Existing sellers is a *good* sign — it proves demand.
   Zero competitors usually means zero market.
3. **Is the incumbent beatable?** Look at the top 3 sellers' reviews. The 2- and 3-star
   reviews are your product brief: they tell you exactly what's wrong with what people
   currently buy.
4. **Does the content angle exist?** Search the niche on TikTok. Are there accounts under
   50k followers getting 100k+ views? That means organic reach is live in this niche. If
   every video in the niche is dead, that channel is closed and the economics don't work.
5. **Run the numbers.** `python3 tools/unit_economics.py --price X --cogs Y ...` before
   ordering samples.

## Sourcing

Given the de minimis repeal (see [`00-reality-check.md`](00-reality-check.md)), sourcing
strategy is now a two-phase thing:

**Phase 1 — validation (dropshipped):**
- Agent-based sourcing beats marketplace browsing. A sourcing agent (CJ, Zendrop, or a
  private agent found via referral) gets better unit costs and handles customs paperwork.
- Accept the bad landed cost. You are buying *information*, not margin, in this phase.
- Demand **DDP (Delivered Duty Paid)** quotes so tariffs are priced in, not a surprise
  passed to your customer at the door. A customer receiving a duty bill is a chargeback.

**Phase 2 — scale (held inventory):**
- Alibaba for bulk, with a verified supplier, third-party inspection, and a sample order
  before any large PO.
- Import to a **3PL** in your target market. This is what amortises duty and drops
  delivery to 2–3 days.
- Trigger: ~50–100 orders/month of a validated SKU. Not before.

**Always:**
- Order samples yourself. Every single time. You cannot sell what you haven't held.
- Get 3 quotes minimum.
- Never pay a large deposit to an unverified supplier. Use trade assurance/escrow.
- Confirm the **HTS code and duty rate** before committing — that number goes straight
  into the unit economics and it is not optional any more.

## Deliverable from this phase

A one-page brief per candidate containing: audience, product, 3 supplier quotes with
landed cost, unit economics output, 3 competitor teardowns from their bad reviews, and 5
content angles you could film next week.

Do this for **3 candidates**. Pick 1. Kill 2 without sentiment.
