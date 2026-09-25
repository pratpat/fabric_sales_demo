# Fabric Sales Demo

Synthetic Goldman Marcus-style sales dataset for Microsoft Fabric demos.

This repository contains a deterministic sample dataset and Fabric-oriented assets for a medallion architecture demo:

- **Bronze**: raw customer, sales, campaign, and web event extracts.
- **Silver**: cleaned dimensional model tables.
- **Gold**: business-ready sales, customer, and campaign aggregates.

All data is synthetic and generated locally. It is not sourced from Goldman Sachs, Marcus, or any real customer system.

## Quick start

```powershell
python scripts\generate_sample_data.py
```

The script writes CSV files into `data\bronze`, `data\silver`, and `data\gold`.

## Suggested Fabric demo flow

1. Create a Fabric Lakehouse named `fabric_sales_demo`.
2. Upload the CSV files under `data\bronze`, `data\silver`, and `data\gold`.
3. Use `fabric\notebooks\01_load_to_lakehouse.py` as starter PySpark code to create Delta tables.
4. Use `sql\gold_views.sql` as a SQL analytics endpoint example for Power BI semantic modeling.

## Dataset themes

The sample models a consumer banking sales motion for products like savings, CDs, personal loans, investment accounts, and credit cards. It includes:

- Sales transactions and funded volume.
- Customer segmentation and digital engagement.
- Marketing campaign touches and attributed revenue.
- Gold-level KPIs by month, segment, channel, region, and product.

See `docs\data_dictionary.md` for table details.
