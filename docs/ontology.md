# Gold sales ontology

The ontology gives the demo a Gold-layer business vocabulary that can be used for Microsoft Fabric Data Agent, semantic model design, documentation, and governance conversations. Silver facts and dimensions are intentionally excluded from the ontology.

## Core entities

| Entity | Table | Key | Meaning |
| --- | --- | --- | --- |
| ExecutiveSnapshot | `executive_kpi_snapshot` | `snapshot_date` | Single-row executive scorecard for the reporting period. |
| SalesKPI | `monthly_sales_summary` | `sales_month,region,segment,product_id,channel_id` | Monthly sales KPI aggregate. |
| CustomerValue | `customer_360` | `customer_id` | Customer-level value and engagement profile. |
| CampaignROI | `campaign_roi_summary` | `campaign_month,campaign_id,channel` | Campaign conversion and ROI aggregate. |
| ProductPerformance | `product_performance` | `product_id` | Product-level sales, revenue, conversion, and new-customer mix. |
| ChannelPerformance | `channel_performance` | `sales_month,channel_id` | Monthly channel performance. |
| RegionSegmentScorecard | `region_segment_scorecard` | `region,segment` | Region and segment scorecard. |

## Relationships

| Relationship | Cardinality | Description |
| --- | --- | --- |
| ExecutiveSnapshot -> SalesKPI | one-to-many-summary | Executive scorecard rolls up monthly sales KPIs. |
| ExecutiveSnapshot -> CampaignROI | one-to-many-summary | Executive scorecard rolls up campaign ROI. |
| ExecutiveSnapshot -> ProductPerformance | one-to-many-summary | Executive scorecard summarizes product performance. |
| ExecutiveSnapshot -> ChannelPerformance | one-to-many-summary | Executive scorecard summarizes channel performance. |
| ExecutiveSnapshot -> RegionSegmentScorecard | one-to-many-summary | Executive scorecard summarizes regional segment performance. |
| SalesKPI -> ProductPerformance | many-to-one-summary | Monthly sales KPIs align to product-level performance. |
| SalesKPI -> ChannelPerformance | many-to-one-summary | Monthly sales KPIs align to channel-level performance. |
| SalesKPI -> RegionSegmentScorecard | many-to-one-summary | Monthly sales KPIs align to region and segment scorecards. |
| CustomerValue -> RegionSegmentScorecard | many-to-one-summary | Customer 360 records roll up to region and segment scorecards. |

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

- `ontology\sales_ontology.json` is the machine-readable Gold-only ontology.
- `ontology\sales_ontology_graph.mmd` is a Mermaid graph that can be rendered in Markdown-compatible tools.
- `ontology\sales_ontology_graph.dot` is a Graphviz DOT graph for lineage and architecture docs.
- `ontology\sales_ontology_graph.excalidraw` is an editable visual diagram.
- `data\ontology\entities.csv`, `relationships.csv`, `metrics.csv`, and `business_terms.csv` are Fabric-loadable ontology tables.
- `data\ontology\graph_nodes.csv` and `graph_edges.csv` are graph-shaped node/edge tables for Fabric notebooks, KQL graph demos, or custom visualization.
