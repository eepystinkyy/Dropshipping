# Dropshipping Project

An honest, executable plan for building a product business — written against 2026 market
conditions, not 2019 YouTube-guru conditions.

## The short answer

**Yes, this can work. No, not the way you're currently picturing it.**

The version of dropshipping most people have in their head — find a cheap product on
AliExpress, put a 3x markup on a Shopify store, run Facebook ads to cold traffic, ship
directly from China — is not "saturated." It is **structurally broken**. Two independent
things killed it:

1. **The de minimis exemption is gone.** Since 29 Aug 2025 the US $800 duty-free
   threshold was suspended worldwide; CBP made the suspension indefinite by regulation
   effective 24 Jun 2026, with statutory repeal following 1 Jul 2027. Every parcel from
   every country is now subject to duty regardless of value. A $25 product from China
   now lands at $40–60. The China/HK suspension alone dropped daily low-value parcel
   volume from ~4M to ~600K — an 85% collapse. Ship-direct-from-supplier arbitrage was
   built entirely on that exemption.
2. **Paid acquisition costs more than the margin.** Meta CPMs are up ~89% since 2020 and
   rose ~20% YoY to $14.19 all-industry ($10.42 ecommerce). A store on 25% margins needs
   ~4:1 ROAS just to break even, against a global average of ~2.19:1.

Run those together and the classic model has negative contribution margin on the first
order. That is not a hustle problem or an effort problem. It's arithmetic.

## What actually still works

The winning shape in 2026 is **not** arbitrage. It's a narrow product business that
happens to use supplier-fulfilled logistics early on:

- **Organic-first acquisition.** Content (TikTok/Reels/Shorts) carries the first cohort
  so CAC starts near zero. Paid comes later, funded by proven LTV — not before it.
- **AOV of $60+**, via bundles and higher-consideration products. At $30 AOV the maths
  cannot close against a $14 CPM.
- **Repeat-purchase categories**, so LTV covers CAC over 2–3 orders rather than one.
- **Migration to held inventory** at a 3PL once a product is validated — bulk import
  amortises duty and cuts per-unit shipping. Dropshipping is the *validation* phase, not
  the destination.

The honest failure mode isn't that this is impossible. It's that it's a real business
with a 6–12 month ramp, and most people quit at month 3 because they were sold a 6-week
timeline.

## Read in this order

| Doc | What it answers |
|---|---|
| [`docs/00-reality-check.md`](docs/00-reality-check.md) | What changed, what's dead, what survives, and who wins now |
| [`docs/01-unit-economics.md`](docs/01-unit-economics.md) | The maths that decides everything — run this before anything else |
| [`docs/02-product-selection.md`](docs/02-product-selection.md) | Hard filters for what to sell, and sourcing |
| [`docs/03-operations.md`](docs/03-operations.md) | Suppliers, fulfillment, legal, tax, payments, returns |
| [`docs/04-90-day-plan.md`](docs/04-90-day-plan.md) | Week-by-week execution with go/no-go kill gates |
| [`docs/05-risks.md`](docs/05-risks.md) | What kills this, ranked, with mitigations |

## Tools

```bash
python3 tools/unit_economics.py --help
```

A contribution-margin and breakeven-CAC calculator. **If a product idea doesn't clear
this, nothing downstream matters.** Ships with the three worked scenarios from
`docs/01-unit-economics.md`:

```bash
python3 tools/unit_economics.py --scenario classic     # the dead model
python3 tools/unit_economics.py --scenario viable      # what to aim for
python3 tools/unit_economics.py --scenario scaled      # post-validation, held inventory
```

## Status

Planning phase. No capital committed, no supplier contacted, no store built.

**Open decision blocking execution: which market are we selling into?** The entire
sourcing and logistics chain forks on this — the de minimis repeal above is US-specific,
and the EU/UK/BR each have their own thresholds and VAT regimes. See
[`docs/03-operations.md`](docs/03-operations.md#market-selection).

## Sources

- [US Ends $800 De Minimis Tariff Exemption](https://taxcloud.com/sales-tax-radar/us-de-minimis-exemption-ends-2025/)
- [Federal Register: Indefinite Suspension of the De Minimis Exemption](https://www.federalregister.gov/documents/2026/06/24/2026-12670/indefinite-suspension-of-the-de-minimis-exemption-for-merchandise-arriving-through-all-modes-other)
- [Ecommerce after De Minimis Tariff Exemption](https://www.practicalecommerce.com/ecommerce-after-de-minimis-tariff-exemption)
- [Meta Ad Benchmarks by Industry 2026](https://adlibrary.com/posts/meta-ad-benchmarks-by-industry-2026)
- [Is Dropshipping Still Profitable in 2026?](https://branvas.com/blogs/news/is-dropshipping-profitable)
- [Shopify Conversion Rate Benchmarks 2026](https://easyappsecom.com/guides/shopify-conversion-rate-benchmarks)
- [Shopify vs TikTok Shop (2026)](https://easyappsecom.com/guides/shopify-vs-tiktok-shop-2026)
