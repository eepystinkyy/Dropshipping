# 03 — Operations

## Market selection

**This is the open decision blocking execution.** Everything below forks on it, so decide
first.

| Market | Import situation | Notes |
|---|---|---|
| **US** | De minimis suspended indefinitely (Jun 2026), full repeal Jul 2027. All parcels dutiable. | Biggest market, best organic reach, worst import maths, highest chargeback rates |
| **EU** | No de minimis for VAT since 2021; IOSS registration required. Customs duty relief under €150. | VAT complexity, but €150 duty threshold still helps under-€150 goods |
| **UK** | £135 threshold; VAT collected at point of sale above it. | Simpler than EU, smaller market |
| **Brazil** | Remessa Conforme; ~20% import tax under $50 + 17% ICMS, higher above. | Relevant if operating locally; different platform mix (Shopee/ML dominant) |

The plan as written assumes **US** in its worked examples. If we're selling elsewhere,
the unit economics inputs change (duty rates, VAT treatment, shipping) but the *structure*
of the plan doesn't — swap the numbers in `tools/unit_economics.py` and re-run the gates.

Note that where you *live* and where you *sell* are separate questions. You can operate a
US-facing store from anywhere; it mainly changes payment-processor onboarding and tax
registration, not the product strategy.

## Stack

Keep it minimal. Every app is a monthly fee against a margin that isn't proven yet.

| Need | Choice | Cost |
|---|---|---|
| Storefront | Shopify Basic | ~$39/mo |
| Payments | Shopify Payments (fallback: Stripe + PayPal) | 2.9% + $0.30 |
| Fulfillment (phase 1) | Sourcing agent w/ DDP | per-order |
| Fulfillment (phase 2) | Regional 3PL | ~$3–5/order pick & pack |
| Email/SMS | Klaviyo free tier → paid at 250 contacts | $0 → ~$45/mo |
| Reviews | Judge.me free | $0 |
| Analytics | GA4 + Shopify native | $0 |

**Do not buy:** page builders, upsell apps, "AI" product finders, bundle apps, or a
premium theme. Not in the first 90 days. A default Shopify theme with good photography
converts fine; a $300 theme with bad photography does not.

Total fixed burn should be **under $100/month** until the product is validated.

## Channel strategy

Run both, for different jobs:

- **TikTok Shop** — discovery and validation. Organic reach still exists there
  (~$20B GMV in 2025, +150% YoY). Fastest way to find out if anyone wants this.
  Budget for total take of **13–29%** per sale: platform commission 2–8%, transaction fee
  ~1%, and creator/affiliate commission 10–20%. That is a large bite — model it in the
  `--channel-pct` flag, don't ignore it.
- **Shopify store** — owns the customer, the email list, and the higher-AOV bundles.
  ~72% of top TikTok Shop sellers also run their own store, which tells you the pattern.

Validate on TikTok, scale on Shopify, own the email list either way. The list is the only
asset here that appreciates and that no platform can take from you.

## Fulfillment SLAs

Non-negotiable, because these are what generate refunds:

- Order → shipped: **≤48h**
- Shipped → delivered: **≤7 days** phase 1, **≤3 days** phase 2
- Tracking pushed to the customer automatically, no exceptions
- Every order gets a real tracking number. "Processing" for 10 days is a chargeback.

## Returns & chargebacks

Budget 4–6% and treat it as a cost line, not an exception:

- Publish a clear 30-day return policy. Absent policies cause disputes, not prevent them.
- For low-value items, **refund without requesting return shipping** — return freight
  usually exceeds COGS.
- Respond to every dispute with tracking + delivery confirmation.
- Watch the chargeback rate: **above 1% risks losing payment processing entirely.** This
  is the fastest way for the whole business to stop existing overnight.

## Legal & tax

Not optional, and cheap to get right early:

- **Entity.** LLC (US) or local equivalent. Separates personal liability from the
  business. A few hundred dollars.
- **Sales tax / VAT.** US: economic nexus thresholds per state — register where you cross
  them. EU: IOSS. Automate with Shopify Tax or Avalara.
- **Import duty.** Confirm the HTS code per SKU. Get DDP quotes in writing.
- **Product liability insurance.** Before scaling, especially anything touching skin or
  carrying weight.
- **Store policies.** Privacy, terms, returns, shipping. Required by payment processors.
- **Ad platform compliance.** No health, income, or medical claims. Policy violations get
  ad accounts banned, and bans are frequently permanent.

## Customer service

You do this yourself for the first 6 months. It is not overhead — it is the highest-value
research available to you. Every ticket tells you what the listing failed to explain, and
the fix usually improves conversion more than any A/B test you could run.

Target: respond within 12h, resolve within 48h.
