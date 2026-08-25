# 03 — Operations

## Market selection

**Decided: EU, operating from Bulgaria.** The reasoning is below; it is not close.

| Market | Import situation | Verdict |
|---|---|---|
| **EU** | €150 relief abolished 1 Jul 2026, replaced by a **flat €3/item** transitional duty until the Customs Data Hub goes live mid-2028; €2 handling fee from 1 Nov 2026. | ✅ **Chosen** |
| **US** | De minimis suspended indefinitely (Jun 2026), statutory repeal Jul 2027. Full ad valorem duty on every parcel. | ❌ Worse maths, no home advantage |
| **UK** | £135 threshold, VAT at point of sale above it. | ➖ Viable, smaller, post-Brexit customs friction from the EU |
| **Brazil** | Remessa Conforme; ~20% import tax + 17% ICMS. | ❌ No connection to it |

### Why the EU wins for us

1. **The flat duty is a structural gift.** The US charges full ad valorem duty per parcel.
   The EU currently charges **€3 flat per item**, whatever the value. On an €89 order that
   is 3.4%. This is the single biggest reason the EU maths closes where the US maths does
   not — and it is explicitly transitional, so it is an advantage with a clock on it
   (standard tariff rates return when the Data Hub lands mid-2028).
2. **Bulgaria is in the customs union.** Import once, clear once, then ship anywhere in
   the EU with no further customs. A US-facing business from Bulgaria pays duty on every
   single parcel and has no way around it.
3. **10% flat corporate tax.** Among the lowest in the EU. Personal income tax also 10%,
   dividend tax 5%.
4. **The euro removes FX friction.** Bulgaria adopted it on 1 Jan 2026 at 1.95583 BGN.
   You now price, buy, and bank in the same currency as most of your market.
5. **Home-market operations.** Same timezone as customers, local accountant, local bank,
   no US sales-tax nexus regime to track across 50 states.

### The VAT decision that is worth real money

Since 1 Jan 2026 the **EU SME scheme** lets a business under **€100,000** total annual EU
turnover sell cross-border **without charging VAT at all**. Bulgaria's own registration
threshold is €51,130, now assessed on a calendar-year basis.

Run both ways on the same product:

```bash
python3 tools/unit_economics.py --scenario eu-sme   # EUR 42.56 contribution (48%)
python3 tools/unit_economics.py --scenario eu-vat   # EUR 32.73 contribution (37%)
```

**Staying under the threshold is worth ~€9.83 per order.** Under the SME scheme you keep
the full €89 and eat unrecoverable import VAT on COGS; VAT-registered, you hand €14.83 of
every €89 to the state and only reclaim input VAT on a €22 cost base.

Two consequences:
- During validation, **stay under €100k deliberately.** It is not a milestone to rush.
- Crossing it is a real step-down in margin. Plan the price increase or the move to held
  inventory (which cuts COGS) to land at the same time, not after.

Confirm all of this with a Bulgarian accountant before registering anything. The rules
above are current as of Aug 2026 and the customs side is explicitly transitional.

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
