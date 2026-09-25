# Data dictionary

All tables are synthetic and intended for Microsoft Fabric demos.

## Bronze

| File | Grain | Description |
| --- | --- | --- |
| `customer_profiles.csv` | One row per customer | Synthetic demographic, segment, region, and engagement attributes. |
| `sales_transactions.csv` | One row per application or funded sale | Product, channel, amount, stage, and estimated revenue facts. |
| `campaign_touches.csv` | One row per marketing touch | Campaign, channel, offer variant, conversion flag, and attributed revenue. |
| `web_events.csv` | One row per digital event | Product-level web and mobile engagement events. |

## Silver

| File | Grain | Description |
| --- | --- | --- |
| `dim_customer.csv` | One row per customer | Clean customer dimension. |
| `dim_product.csv` | One row per product | Product family and revenue assumptions. |
| `dim_channel.csv` | One row per channel | Channel names and groups. |
| `dim_date.csv` | One row per day | Calendar attributes from 2025-01-01 through 2026-09-30. |
| `fact_sales.csv` | One row per application or funded sale | Conformed sales fact table. |
| `fact_campaign_touch.csv` | One row per campaign touch | Conformed campaign interaction fact table. |
| `fact_web_event.csv` | One row per digital event | Conformed digital engagement fact table. |

## Gold

| File | Grain | Description |
| --- | --- | --- |
| `monthly_sales_summary.csv` | Month, region, segment, product, channel | Sales KPI aggregate for executive dashboards. |
| `campaign_roi_summary.csv` | Month, campaign, channel | Campaign conversion and ROI aggregate. |
| `customer_360.csv` | One row per customer | Customer value and engagement profile. |
| `executive_kpi_snapshot.csv` | One row per reporting period | Executive landing-page KPI snapshot. |
| `product_performance.csv` | Product | Product-level application, funded sales, revenue, conversion, and new-customer mix. |
| `channel_performance.csv` | Month, channel | Channel-level sales trend and conversion performance. |
| `region_segment_scorecard.csv` | Region, segment | Customer, engagement, conversion, revenue, and revenue-per-customer scorecard. |

## Ontology

| File | Grain | Description |
| --- | --- | --- |
| `entities.csv` | One row per business entity | Entity-to-table mapping for the Fabric model. |
| `relationships.csv` | One row per semantic relationship | Entity relationship definitions and cardinality. |
| `metrics.csv` | One row per metric | Business metric definitions and formulas. |
| `business_terms.csv` | One row per term | Demo glossary for business users and Fabric Data Agent prompts. |

## Recommended Power BI measures

```DAX
Funded Sales = SUM(gold_monthly_sales_summary[funded_sales])
Sales Amount = SUM(gold_monthly_sales_summary[sales_amount])
Estimated Revenue = SUM(gold_monthly_sales_summary[estimated_revenue])
Conversion Rate = DIVIDE(SUM(gold_monthly_sales_summary[funded_sales]), SUM(gold_monthly_sales_summary[applications]))
New Customer Sales = SUM(gold_monthly_sales_summary[new_customer_sales])
Campaign ROI Index = DIVIDE(SUM(gold_campaign_roi_summary[attributed_revenue]), SUM(gold_campaign_roi_summary[touches]) * 7.5)
```
