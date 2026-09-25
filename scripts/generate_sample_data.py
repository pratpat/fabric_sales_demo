from __future__ import annotations

import csv
import random
from dataclasses import dataclass
from datetime import date, timedelta
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
RANDOM_SEED = 42


@dataclass(frozen=True)
class Product:
    product_id: str
    product_name: str
    product_family: str
    base_amount: int
    revenue_rate: float


PRODUCTS = [
    Product("P001", "Marcus High Yield Savings", "Deposits", 18000, 0.006),
    Product("P002", "Marcus Certificate of Deposit", "Deposits", 27000, 0.004),
    Product("P003", "Marcus Personal Loan", "Lending", 14500, 0.032),
    Product("P004", "Marcus Invest Account", "Wealth", 22000, 0.008),
    Product("P005", "Marcus Credit Card", "Cards", 3200, 0.041),
]

CHANNELS = [
    ("C001", "Web", "Digital"),
    ("C002", "Mobile App", "Digital"),
    ("C003", "Email", "Digital Marketing"),
    ("C004", "Contact Center", "Assisted"),
    ("C005", "Branch Partner", "Partner"),
]

REGIONS = ["Northeast", "Southeast", "Midwest", "Southwest", "West"]
SEGMENTS = ["Mass Affluent", "Emerging Affluent", "Digital Native", "Rate Shopper", "Borrower"]
CAMPAIGNS = [
    ("CMP001", "Savings Rate Booster", "Deposits"),
    ("CMP002", "Debt Consolidation Loan", "Lending"),
    ("CMP003", "Invest Starter", "Wealth"),
    ("CMP004", "Card Rewards Upgrade", "Cards"),
    ("CMP005", "CD Maturity Winback", "Deposits"),
]
FIRST_NAMES = [
    "Alex", "Avery", "Blake", "Casey", "Devon", "Emerson", "Harper", "Jamie",
    "Jordan", "Kendall", "Morgan", "Parker", "Quinn", "Reese", "Riley", "Taylor",
]
LAST_NAMES = [
    "Adams", "Baker", "Chen", "Diaz", "Evans", "Garcia", "Hill", "Johnson",
    "Kim", "Lopez", "Miller", "Patel", "Rivera", "Singh", "Smith", "Wilson",
]


def write_csv(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        raise ValueError(f"No rows to write for {path}")
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def daterange(start: date, end: date) -> list[date]:
    days = (end - start).days + 1
    return [start + timedelta(days=offset) for offset in range(days)]


def make_customers(count: int) -> list[dict]:
    customers = []
    start_date = date(2024, 1, 1)
    for index in range(1, count + 1):
        region = random.choice(REGIONS)
        segment = random.choice(SEGMENTS)
        acquired_on = start_date + timedelta(days=random.randint(0, 620))
        customers.append(
            {
                "customer_id": f"CUST{index:05d}",
                "first_name": random.choice(FIRST_NAMES),
                "last_name": random.choice(LAST_NAMES),
                "region": region,
                "segment": segment,
                "age_band": random.choice(["18-29", "30-39", "40-49", "50-64", "65+"]),
                "annual_income_band": random.choice(["<75K", "75K-125K", "125K-250K", "250K+"]),
                "credit_tier": random.choice(["Prime", "Super Prime", "Near Prime"]),
                "digital_engagement_score": random.randint(25, 100),
                "customer_since": acquired_on.isoformat(),
            }
        )
    return customers


def make_transactions(customers: list[dict], count: int) -> list[dict]:
    rows = []
    start_date = date(2025, 1, 1)
    all_dates = daterange(start_date, date(2026, 9, 30))
    for index in range(1, count + 1):
        customer = random.choice(customers)
        product = random.choice(PRODUCTS)
        channel_id, channel_name, _ = random.choice(CHANNELS)
        txn_date = random.choice(all_dates)
        amount = max(250, round(random.gauss(product.base_amount, product.base_amount * 0.35), 2))
        revenue = round(amount * product.revenue_rate, 2)
        rows.append(
            {
                "transaction_id": f"TXN{index:07d}",
                "transaction_date": txn_date.isoformat(),
                "customer_id": customer["customer_id"],
                "product_id": product.product_id,
                "channel_id": channel_id,
                "region": customer["region"],
                "segment": customer["segment"],
                "sales_amount": amount,
                "estimated_revenue": revenue,
                "sales_stage": random.choices(
                    ["Funded", "Approved", "Application Started", "Abandoned"],
                    weights=[70, 12, 10, 8],
                    k=1,
                )[0],
                "is_new_customer_sale": random.choices([True, False], weights=[28, 72], k=1)[0],
                "source_system": random.choice(["marcus_web", "crm", "loan_origination", "campaign_platform"]),
            }
        )
    return rows


def make_campaign_touches(customers: list[dict], transactions: list[dict], count: int) -> list[dict]:
    funded_transactions = [row for row in transactions if row["sales_stage"] == "Funded"]
    rows = []
    for index in range(1, count + 1):
        campaign_id, campaign_name, product_family = random.choice(CAMPAIGNS)
        customer = random.choice(customers)
        touch_date = date(2025, 1, 1) + timedelta(days=random.randint(0, 638))
        converted = random.random() < 0.22
        matched_txn = random.choice(funded_transactions) if converted and funded_transactions else None
        rows.append(
            {
                "touch_id": f"TCH{index:06d}",
                "touch_date": touch_date.isoformat(),
                "customer_id": customer["customer_id"],
                "campaign_id": campaign_id,
                "campaign_name": campaign_name,
                "target_product_family": product_family,
                "channel": random.choice(["Email", "Paid Search", "Display", "In App", "Contact Center"]),
                "offer_variant": random.choice(["Control", "Rate", "Cash Bonus", "Rewards", "Education"]),
                "converted": converted,
                "attributed_transaction_id": matched_txn["transaction_id"] if matched_txn else "",
                "attributed_revenue": matched_txn["estimated_revenue"] if matched_txn else 0,
            }
        )
    return rows


def make_web_events(customers: list[dict], count: int) -> list[dict]:
    rows = []
    event_types = ["page_view", "rate_check", "calculator_use", "application_start", "document_upload"]
    for index in range(1, count + 1):
        customer = random.choice(customers)
        product = random.choice(PRODUCTS)
        event_date = date(2025, 1, 1) + timedelta(days=random.randint(0, 638))
        rows.append(
            {
                "event_id": f"EVT{index:07d}",
                "event_timestamp": f"{event_date.isoformat()}T{random.randint(8, 22):02d}:{random.randint(0, 59):02d}:00",
                "customer_id": customer["customer_id"],
                "product_id": product.product_id,
                "event_type": random.choice(event_types),
                "device_type": random.choice(["Desktop", "Mobile", "Tablet"]),
                "session_minutes": random.randint(1, 36),
                "referrer": random.choice(["Direct", "Search", "Email", "Partner", "Social"]),
            }
        )
    return rows


def make_dim_date() -> list[dict]:
    rows = []
    for day in daterange(date(2025, 1, 1), date(2026, 9, 30)):
        rows.append(
            {
                "date_key": day.strftime("%Y%m%d"),
                "date": day.isoformat(),
                "year": day.year,
                "quarter": f"Q{((day.month - 1) // 3) + 1}",
                "month_number": day.month,
                "month_name": day.strftime("%B"),
                "week_of_year": day.isocalendar().week,
                "is_weekend": day.weekday() >= 5,
            }
        )
    return rows


def summarize_sales(transactions: list[dict]) -> list[dict]:
    grouped: dict[tuple, dict] = {}
    for row in transactions:
        txn_date = date.fromisoformat(row["transaction_date"])
        key = (
            txn_date.strftime("%Y-%m"),
            row["region"],
            row["segment"],
            row["product_id"],
            row["channel_id"],
        )
        target = grouped.setdefault(
            key,
            {
                "sales_month": key[0],
                "region": key[1],
                "segment": key[2],
                "product_id": key[3],
                "channel_id": key[4],
                "applications": 0,
                "funded_sales": 0,
                "sales_amount": 0.0,
                "estimated_revenue": 0.0,
                "new_customer_sales": 0,
            },
        )
        target["applications"] += 1
        if row["sales_stage"] == "Funded":
            target["funded_sales"] += 1
            target["sales_amount"] += float(row["sales_amount"])
            target["estimated_revenue"] += float(row["estimated_revenue"])
            target["new_customer_sales"] += 1 if row["is_new_customer_sale"] else 0
    return [
        {
            **row,
            "sales_amount": round(row["sales_amount"], 2),
            "estimated_revenue": round(row["estimated_revenue"], 2),
            "conversion_rate": round(row["funded_sales"] / row["applications"], 4),
        }
        for row in grouped.values()
    ]


def summarize_campaigns(touches: list[dict]) -> list[dict]:
    grouped: dict[tuple, dict] = {}
    for row in touches:
        month = row["touch_date"][:7]
        key = (month, row["campaign_id"], row["campaign_name"], row["channel"])
        target = grouped.setdefault(
            key,
            {
                "campaign_month": month,
                "campaign_id": row["campaign_id"],
                "campaign_name": row["campaign_name"],
                "channel": row["channel"],
                "touches": 0,
                "conversions": 0,
                "attributed_revenue": 0.0,
            },
        )
        target["touches"] += 1
        target["conversions"] += 1 if row["converted"] else 0
        target["attributed_revenue"] += float(row["attributed_revenue"])
    return [
        {
            **row,
            "attributed_revenue": round(row["attributed_revenue"], 2),
            "conversion_rate": round(row["conversions"] / row["touches"], 4),
            "roi_index": round((row["attributed_revenue"] / max(row["touches"] * 7.5, 1)), 2),
        }
        for row in grouped.values()
    ]


def make_customer_360(customers: list[dict], transactions: list[dict], web_events: list[dict]) -> list[dict]:
    sales_by_customer: dict[str, dict] = {}
    events_by_customer: dict[str, int] = {}
    for row in transactions:
        target = sales_by_customer.setdefault(
            row["customer_id"],
            {"funded_sales": 0, "sales_amount": 0.0, "estimated_revenue": 0.0},
        )
        if row["sales_stage"] == "Funded":
            target["funded_sales"] += 1
            target["sales_amount"] += float(row["sales_amount"])
            target["estimated_revenue"] += float(row["estimated_revenue"])
    for row in web_events:
        events_by_customer[row["customer_id"]] = events_by_customer.get(row["customer_id"], 0) + 1
    rows = []
    for customer in customers:
        sales = sales_by_customer.get(customer["customer_id"], {"funded_sales": 0, "sales_amount": 0.0, "estimated_revenue": 0.0})
        rows.append(
            {
                "customer_id": customer["customer_id"],
                "region": customer["region"],
                "segment": customer["segment"],
                "credit_tier": customer["credit_tier"],
                "digital_engagement_score": customer["digital_engagement_score"],
                "web_events": events_by_customer.get(customer["customer_id"], 0),
                "funded_sales": sales["funded_sales"],
                "lifetime_sales_amount": round(sales["sales_amount"], 2),
                "lifetime_estimated_revenue": round(sales["estimated_revenue"], 2),
            }
        )
    return rows


def main() -> None:
    random.seed(RANDOM_SEED)

    customers = make_customers(500)
    transactions = make_transactions(customers, 2500)
    campaign_touches = make_campaign_touches(customers, transactions, 900)
    web_events = make_web_events(customers, 3000)

    product_rows = [
        {
            "product_id": product.product_id,
            "product_name": product.product_name,
            "product_family": product.product_family,
            "base_amount": product.base_amount,
            "revenue_rate": product.revenue_rate,
        }
        for product in PRODUCTS
    ]
    channel_rows = [
        {"channel_id": channel_id, "channel_name": channel_name, "channel_group": channel_group}
        for channel_id, channel_name, channel_group in CHANNELS
    ]

    write_csv(DATA / "bronze" / "customer_profiles.csv", customers)
    write_csv(DATA / "bronze" / "sales_transactions.csv", transactions)
    write_csv(DATA / "bronze" / "campaign_touches.csv", campaign_touches)
    write_csv(DATA / "bronze" / "web_events.csv", web_events)

    write_csv(DATA / "silver" / "dim_customer.csv", customers)
    write_csv(DATA / "silver" / "dim_product.csv", product_rows)
    write_csv(DATA / "silver" / "dim_channel.csv", channel_rows)
    write_csv(DATA / "silver" / "dim_date.csv", make_dim_date())
    write_csv(DATA / "silver" / "fact_sales.csv", transactions)
    write_csv(DATA / "silver" / "fact_campaign_touch.csv", campaign_touches)
    write_csv(DATA / "silver" / "fact_web_event.csv", web_events)

    write_csv(DATA / "gold" / "monthly_sales_summary.csv", summarize_sales(transactions))
    write_csv(DATA / "gold" / "campaign_roi_summary.csv", summarize_campaigns(campaign_touches))
    write_csv(DATA / "gold" / "customer_360.csv", make_customer_360(customers, transactions, web_events))

    print("Generated synthetic Fabric sales demo data.")
    print(f"Customers: {len(customers)}")
    print(f"Transactions: {len(transactions)}")
    print(f"Campaign touches: {len(campaign_touches)}")
    print(f"Web events: {len(web_events)}")


if __name__ == "__main__":
    main()
