# 01 — Unit Economics

This is the most important document in the repo. Every other decision is downstream of
these numbers. Run `tools/unit_economics.py` on any product idea *before* you get
attached to it.

## The model

```
Contribution margin = Price
                    − COGS (supplier unit cost)
                    − Duty/tariff (landed cost adder)
                    − Outbound shipping
                    − Payment processing (≈2.9% + $0.30)
                    − Platform/channel fees
                    − Expected refund & chargeback cost
```

**Breakeven CAC = contribution margin.** Spend more than that to acquire a customer and
you lose money on every order. "Make it up on volume" is how people lose money faster.

Then the only question that matters:

```
Actual CAC  <  Breakeven CAC × (expected orders per customer)
```

If that inequality doesn't hold, the business doesn't work — regardless of how good the
product, the site, or the ads are.

## Estimating actual CAC

You cannot know this until you run traffic, but you can bound it:

```
CAC = CPM / 1000 / CTR / conversion_rate
```

With 2026 ecommerce benchmarks — CPM $10.42, CTR ~1.0%, Shopify conversion ~1.4–1.8%
(top decile 4.7%):

```
CAC = 10.42 / 1000 / 0.01 / 0.016 ≈ $65
```

**Treat ~$65 as the default cold-paid CAC on Meta.** A new store with no social proof
runs worse than benchmark, not better. Assume $70–80 for planning. If your plan requires
a $25 CAC on cold paid traffic, the plan is fiction.

## Three scenarios

All runnable via `python3 tools/unit_economics.py --scenario <name>`.

### Scenario A — "classic" (the dead model)

The thing most people build. AliExpress gadget, 3x markup, Meta ads.

| Line | Amount |
|---|---|
| Price | $39.99 |
| COGS | −$8.00 |
| Duty/tariff (~25% of declared) | −$2.00 |
| Shipping to customer | −$6.00 |
| Payment processing | −$1.46 |
| Refunds/chargebacks (5%) | −$2.00 |
| **Contribution margin** | **$20.53 (51%)** |
| **Breakeven CAC** | **$20.53** |
| Actual CAC (cold paid) | ~$65 |
| **Per-order result** | **−$44 🔴** |

51% gross margin *looks* healthy. It's irrelevant. The business loses $44 per order and
scaling ad spend accelerates the loss. **This is the model to not build.**

### Scenario B — "viable" (what we aim for)

Bundle-driven AOV, organic-first acquisition, repeat-purchase category.

| Line | Amount |
|---|---|
| Price (bundle) | $89.00 |
| COGS | −$22.00 |
| Duty/tariff | −$5.50 |
| Shipping to customer | −$8.00 |
| Payment processing | −$2.88 |
| Refunds/chargebacks (4%) | −$3.56 |
| **Contribution margin** | **$47.06 (53%)** |
| **Breakeven CAC (1st order)** | **$47.06** |
| Actual CAC — organic phase | ~$5–15 🟢 |
| Actual CAC — paid phase | ~$65 |
| Expected orders/customer | 2.2 |
| **LTV** | **$103.53** |
| **LTV:CAC at paid CAC** | **1.6:1 🟡** |

Note the gross margin is *the same 53%*. What changed is the absolute dollars: $47 of
contribution instead of $20. That is the entire trick — **margin percentage is vanity,
contribution dollars pay for customers.**

Even so, 1.6:1 on paid is below the 3:1 target. Which tells us something important: **at
these numbers, paid acquisition alone still doesn't clear the bar.** The organic phase
isn't a nice-to-have that precedes the real business — for a while it *is* the business.

### Scenario C — "scaled" (post-validation, held inventory)

Same product, after bulk-importing to a 3PL. Duty amortised over a container, unit cost
down on volume, shipping domestic.

| Line | Amount |
|---|---|
| Price (bundle) | $89.00 |
| COGS (volume pricing) | −$16.00 |
| Duty/tariff (amortised) | −$3.20 |
| Shipping (domestic 3PL) | −$5.50 |
| Payment processing | −$2.88 |
| Refunds/chargebacks (3%) | −$2.67 |
| **Contribution margin** | **$58.75 (66%)** |
| Actual CAC (paid, warm brand) | ~$45 |
| Expected orders/customer | 2.8 |
| **LTV** | **$164.50** |
| **LTV:CAC** | **3.7:1 🟢** |

This is where the business actually makes money. Note it is **not reachable directly** —
you can't bulk-import before you know the product sells. Scenario B is the bridge you
have to survive to get to Scenario C.

## What this tells us

1. **Anything under ~$60 AOV is dead on arrival.** The contribution dollars can't cover a
   real CAC.
2. **Organic content isn't a growth hack, it's the only affordable acquisition during
   validation.** Budget effort there, not ad spend.
3. **The whole plan is a race to Scenario C** before capital or motivation runs out.
4. **One product with repeat purchase beats ten products without it.** Every scenario
   above lives or dies on orders-per-customer.

## Hard gates

Do not proceed past validation unless:

- [ ] Contribution margin ≥ **$40/order** in the dropshipped configuration
- [ ] Contribution margin ≥ **45%** of price
- [ ] AOV ≥ **$60**
- [ ] Credible path to **≥2 orders per customer**
- [ ] Blended CAC in the organic phase ≤ **$20**
- [ ] Refund rate ≤ **6%** across the first 50 orders

Six boxes. If a product idea can't tick all six on paper, it will not tick them in
reality — reality is always worse than the spreadsheet.
