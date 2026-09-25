# Fabric notebook starter: load CSV files into Delta tables.
# Run inside a Fabric Lakehouse notebook after uploading the data folder.

from pathlib import Path


TABLES = {
    "bronze_customer_profiles": "Files/data/bronze/customer_profiles.csv",
    "bronze_sales_transactions": "Files/data/bronze/sales_transactions.csv",
    "bronze_campaign_touches": "Files/data/bronze/campaign_touches.csv",
    "bronze_web_events": "Files/data/bronze/web_events.csv",
    "dim_customer": "Files/data/silver/dim_customer.csv",
    "dim_product": "Files/data/silver/dim_product.csv",
    "dim_channel": "Files/data/silver/dim_channel.csv",
    "dim_date": "Files/data/silver/dim_date.csv",
    "fact_sales": "Files/data/silver/fact_sales.csv",
    "fact_campaign_touch": "Files/data/silver/fact_campaign_touch.csv",
    "fact_web_event": "Files/data/silver/fact_web_event.csv",
    "gold_monthly_sales_summary": "Files/data/gold/monthly_sales_summary.csv",
    "gold_campaign_roi_summary": "Files/data/gold/campaign_roi_summary.csv",
    "gold_customer_360": "Files/data/gold/customer_360.csv",
    "gold_executive_kpi_snapshot": "Files/data/gold/executive_kpi_snapshot.csv",
    "gold_product_performance": "Files/data/gold/product_performance.csv",
    "gold_channel_performance": "Files/data/gold/channel_performance.csv",
    "gold_region_segment_scorecard": "Files/data/gold/region_segment_scorecard.csv",
    "ontology_entities": "Files/data/ontology/entities.csv",
    "ontology_relationships": "Files/data/ontology/relationships.csv",
    "ontology_metrics": "Files/data/ontology/metrics.csv",
    "ontology_business_terms": "Files/data/ontology/business_terms.csv",
    "ontology_graph_nodes": "Files/data/ontology/graph_nodes.csv",
    "ontology_graph_edges": "Files/data/ontology/graph_edges.csv",
}


for table_name, path in TABLES.items():
    df = (
        spark.read.format("csv")
        .option("header", "true")
        .option("inferSchema", "true")
        .load(path)
    )
    df.write.mode("overwrite").format("delta").saveAsTable(table_name)
    print(f"Loaded {table_name} from {Path(path).name}")
