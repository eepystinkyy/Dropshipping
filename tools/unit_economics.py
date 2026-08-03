#!/usr/bin/env python3
"""Contribution margin and breakeven-CAC calculator for product ideas.

If an idea doesn't clear the gates in docs/01-unit-economics.md, nothing
downstream matters. Run this before sourcing samples, not after.

    python3 tools/unit_economics.py --scenario viable
    python3 tools/unit_economics.py --price 89 --cogs 22 --duty-pct 25 --ship 8
"""

import argparse
from dataclasses import dataclass, field

# 2026 benchmarks. Sources in README.md.
BENCH_CPM = 10.42          # Meta, ecommerce vertical
BENCH_CTR = 0.010          # 1.0%
BENCH_CVR = 0.016          # Shopify median 1.4-1.8%
STRIPE_PCT = 0.029
STRIPE_FLAT = 0.30

# Gates from docs/01-unit-economics.md.
GATE_CM_ABS = 40.00
GATE_CM_PCT = 0.45
GATE_AOV = 60.00
GATE_ORDERS = 2.0
GATE_LTV_CAC = 3.0


@dataclass
class Scenario:
    name: str
    note: str
    price: float
    cogs: float
    duty_pct: float          # % of COGS, the landed-cost adder
    ship: float
    refund_rate: float
    channel_pct: float = 0.0  # TikTok Shop commission etc.
    orders_per_customer: float = 1.0
    actual_cac: float | None = None   # None => derive from benchmarks
    cac_label: str = "cold paid (benchmark)"

    # --- derived ---
    @property
    def duty(self) -> float:
        return self.cogs * self.duty_pct / 100

    @property
    def processing(self) -> float:
        return self.price * STRIPE_PCT + STRIPE_FLAT

    @property
    def channel_fee(self) -> float:
        return self.price * self.channel_pct

    @property
    def refund_cost(self) -> float:
        return self.price * self.refund_rate

    @property
    def contribution(self) -> float:
        return (self.price - self.cogs - self.duty - self.ship
                - self.processing - self.channel_fee - self.refund_cost)

    @property
    def contribution_pct(self) -> float:
        return self.contribution / self.price if self.price else 0.0

    @property
    def breakeven_cac(self) -> float:
        return self.contribution

    @property
    def cac(self) -> float:
        if self.actual_cac is not None:
            return self.actual_cac
        return benchmark_cac()

    @property
    def ltv(self) -> float:
        return self.contribution * self.orders_per_customer

    @property
    def ltv_cac(self) -> float:
        return self.ltv / self.cac if self.cac else float("inf")


def benchmark_cac(cpm=BENCH_CPM, ctr=BENCH_CTR, cvr=BENCH_CVR) -> float:
    """CAC implied by ad benchmarks: CPM / 1000 / CTR / CVR."""
    return cpm / 1000 / ctr / cvr


SCENARIOS = {
    "classic": Scenario(
        name="A — classic (the dead model)",
        note="AliExpress gadget, 3x markup, cold Meta traffic. Do not build this.",
        price=39.99, cogs=8.00, duty_pct=25.0, ship=6.00,
        refund_rate=0.05, orders_per_customer=1.0,
    ),
    "viable": Scenario(
        name="B — viable (validation target)",
        note="Bundle AOV, organic-first acquisition, repeat-purchase category.",
        price=89.00, cogs=22.00, duty_pct=25.0, ship=8.00,
        refund_rate=0.04, orders_per_customer=2.2,
    ),
    "scaled": Scenario(
        name="C — scaled (post-validation, held inventory)",
        note="Bulk-imported to a 3PL. Duty amortised, domestic shipping, warm brand.",
        price=89.00, cogs=16.00, duty_pct=20.0, ship=5.50,
        refund_rate=0.03, orders_per_customer=2.8,
        actual_cac=45.00, cac_label="paid, warm brand",
    ),
}


def money(x: float) -> str:
    return f"${x:>8,.2f}"


def report(s: Scenario) -> None:
    print(f"\n\033[1m{s.name}\033[0m")
    print(f"  {s.note}\n")

    rows = [
        ("Price", s.price),
        ("COGS", -s.cogs),
        (f"Duty/tariff ({s.duty_pct:.0f}% of COGS)", -s.duty),
        ("Shipping to customer", -s.ship),
        (f"Payment processing ({STRIPE_PCT:.1%} + ${STRIPE_FLAT:.2f})", -s.processing),
    ]
    if s.channel_pct:
        rows.append((f"Channel fee ({s.channel_pct:.1%})", -s.channel_fee))
    rows.append((f"Refunds/chargebacks ({s.refund_rate:.0%})", -s.refund_cost))

    width = max(len(label) for label, _ in rows) + 2
    for label, amount in rows:
        print(f"  {label:<{width}}{money(amount)}")
    print(f"  {'-' * (width + 10)}")
    print(f"  {'Contribution margin':<{width}}{money(s.contribution)}"
          f"   ({s.contribution_pct:.0%})")

    print(f"\n  {'Breakeven CAC':<{width}}{money(s.breakeven_cac)}")
    print(f"  {'Actual CAC — ' + s.cac_label:<{width}}{money(s.cac)}")
    print(f"  {'Orders per customer':<{width}}{s.orders_per_customer:>9.1f}")
    print(f"  {'LTV (contribution basis)':<{width}}{money(s.ltv)}")

    ratio = s.ltv_cac
    flag = "\033[32mOK\033[0m" if ratio >= GATE_LTV_CAC else (
        "\033[33mTHIN\033[0m" if ratio >= 1.0 else "\033[31mLOSS\033[0m")
    print(f"  {'LTV:CAC':<{width}}{ratio:>9.2f}   {flag}")

    per_order = s.contribution - s.cac
    if per_order < 0:
        print(f"\n  \033[31mFirst-order result: {money(per_order)} — "
              f"loses money on every acquisition.\033[0m")

    gates(s)


def gates(s: Scenario) -> None:
    checks = [
        ("Contribution ≥ $40/order", s.contribution >= GATE_CM_ABS),
        ("Contribution ≥ 45% of price", s.contribution_pct >= GATE_CM_PCT),
        ("AOV ≥ $60", s.price >= GATE_AOV),
        ("≥2 orders per customer", s.orders_per_customer >= GATE_ORDERS),
        ("LTV:CAC ≥ 3:1", s.ltv_cac >= GATE_LTV_CAC),
    ]
    print("\n  Gates:")
    for label, ok in checks:
        mark = "\033[32m✓\033[0m" if ok else "\033[31m✗\033[0m"
        print(f"    {mark} {label}")
    passed = sum(ok for _, ok in checks)
    print(f"\n  {passed}/{len(checks)} gates passed.")
    if passed < len(checks):
        print("  \033[33mNot ready to commit capital.\033[0m")


def main() -> None:
    p = argparse.ArgumentParser(
        description="Contribution margin / breakeven CAC calculator.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="Scenarios: " + ", ".join(SCENARIOS))
    p.add_argument("--scenario", choices=SCENARIOS, help="run a worked scenario")
    p.add_argument("--all", action="store_true", help="run every scenario")
    p.add_argument("--price", type=float, help="selling price / AOV")
    p.add_argument("--cogs", type=float, help="supplier unit cost")
    p.add_argument("--duty-pct", type=float, default=25.0, help="duty as %% of COGS")
    p.add_argument("--ship", type=float, default=8.0, help="outbound shipping")
    p.add_argument("--refund-rate", type=float, default=0.04, help="e.g. 0.04 = 4%%")
    p.add_argument("--channel-pct", type=float, default=0.0,
                   help="marketplace commission, e.g. 0.08 for TikTok Shop")
    p.add_argument("--orders", type=float, default=1.0, help="orders per customer")
    p.add_argument("--cac", type=float, help="actual CAC (default: benchmark-derived)")
    args = p.parse_args()

    if args.all:
        for s in SCENARIOS.values():
            report(s)
        return
    if args.scenario:
        report(SCENARIOS[args.scenario])
        return
    if args.price and args.cogs is not None:
        report(Scenario(
            name="Custom", note="Ad-hoc product idea.",
            price=args.price, cogs=args.cogs, duty_pct=args.duty_pct,
            ship=args.ship, refund_rate=args.refund_rate,
            channel_pct=args.channel_pct, orders_per_customer=args.orders,
            actual_cac=args.cac,
            cac_label="user-supplied" if args.cac else "cold paid (benchmark)"))
        return

    print(f"Benchmark cold-paid CAC: ${benchmark_cac():.2f} "
          f"(CPM ${BENCH_CPM}, CTR {BENCH_CTR:.1%}, CVR {BENCH_CVR:.1%})\n")
    p.print_help()


if __name__ == "__main__":
    main()
