# Sales ontology

The ontology gives the demo a business vocabulary that can be used for Microsoft Fabric Data Agent, semantic model design, documentation, and governance conversations.

## Core entities

| Entity | Table | Key | Meaning |
| --- | --- | --- | --- |
| Customer | `dim_customer` | `customer_id` | Person or household prospect/customer. |
| Product | `dim_product` | `product_id` | Financial product such as savings, CD, loan, invest, or card. |
| Channel | `dim_channel` | `channel_id` | Sales or acquisition channel. |
| Sale | `fact_sales` | `transaction_id` | Application or funded sale event. |
| CampaignTouch | `fact_campaign_touch` | `touch_id` | Marketing touch with optional sales attribution. |
| WebEvent | `fact_web_event` | `event_id` | Digital interaction tied to a customer and product. |

## Relationships

| Relationship | Cardinality | Description |
| --- | --- | --- |
| Sale -> Customer | many-to-one | Every sale/application belongs to one customer. |
| Sale -> Product | many-to-one | Every sale/application is for one product. |
| Sale -> Channel | many-to-one | Every sale/application originates in one channel. |
| CampaignTouch -> Customer | many-to-one | Every campaign touch targets one customer. |
| CampaignTouch -> Sale | many-to-zero-or-one | Converted touches can attribute revenue to a funded sale. |
| WebEvent -> Customer | many-to-one | Digital events are performed by customers. |
| WebEvent -> Product | many-to-one | Digital events can reference a product. |

## Gold datasets

| Dataset | Grain | Primary use |
| --- | --- | --- |
| `executive_kpi_snapshot.csv` | One row per reporting period | Landing-page KPIs and demo overview. |
| `monthly_sales_summary.csv` | Month, region, segment, product, channel | Sales performance dashboard. |
| `product_performance.csv` | Product | Product family and product-level KPI comparison. |
| `channel_performance.csv` | Month, channel | Channel trend analysis. |
| `region_segment_scorecard.csv` | Region, segment | Coverage, conversion, and customer value analysis. |
| `campaign_roi_summary.csv` | Month, campaign, channel | Campaign conversion and ROI analysis. |
| `customer_360.csv` | Customer | Customer value, engagement, and segmentation. |

## Files

- `ontology\sales_ontology.json` is the machine-readable ontology.
- `data\ontology\entities.csv`, `relationships.csv`, `metrics.csv`, and `business_terms.csv` are Fabric-loadable ontology tables.
