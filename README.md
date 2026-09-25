# Fabric Sales Demo

Synthetic Goldman Marcus-style sales dataset for Microsoft Fabric demos.

This repository contains a deterministic sample dataset and Fabric-oriented assets for a medallion architecture demo:

- **Bronze**: raw customer, sales, campaign, and web event extracts.
- **Silver**: cleaned dimensional model tables.
- **Gold**: business-ready sales, customer, campaign, product, channel, and executive aggregates.
- **Ontology**: entities, relationships, business terms, and metric definitions for semantic modeling.

All data is synthetic and generated locally. It is not sourced from Goldman Sachs, Marcus, or any real customer system.

## Quick start

```powershell
python scripts\generate_sample_data.py
```

The script writes CSV files into `data\bronze`, `data\silver`, `data\gold`, and `data\ontology`.

## Suggested Fabric demo flow

1. Create a Fabric Lakehouse named `fabric_sales_demo`.
2. Upload the CSV files under `data\bronze`, `data\silver`, and `data\gold`.
3. Use `fabric\notebooks\01_load_to_lakehouse.py` as starter PySpark code to create Delta tables.
4. Use `sql\gold_views.sql` as a SQL analytics endpoint example for Power BI semantic modeling.
5. Use `ontology\sales_ontology.json` and `data\ontology\*.csv` as business ontology inputs for documentation, governance, or a Fabric Data Agent demo.

## Dataset themes

The sample models a consumer banking sales motion for products like savings, CDs, personal loans, investment accounts, and credit cards. It includes:

- Sales transactions and funded volume.
- Customer segmentation and digital engagement.
- Marketing campaign touches and attributed revenue.
- Gold-level KPIs by month, segment, channel, region, product, campaign, and executive snapshot.

See `docs\data_dictionary.md` for table details and `docs\ontology.md` for the business ontology.
