CREATE OR ALTER VIEW dbo.vw_sales_kpi AS
SELECT
    sales_month,
    region,
    segment,
    product_id,
    channel_id,
    SUM(applications) AS applications,
    SUM(funded_sales) AS funded_sales,
    SUM(sales_amount) AS sales_amount,
    SUM(estimated_revenue) AS estimated_revenue,
    CAST(SUM(funded_sales) AS FLOAT) / NULLIF(SUM(applications), 0) AS conversion_rate
FROM gold_monthly_sales_summary
GROUP BY sales_month, region, segment, product_id, channel_id;

CREATE OR ALTER VIEW dbo.vw_campaign_roi AS
SELECT
    campaign_month,
    campaign_id,
    campaign_name,
    channel,
    SUM(touches) AS touches,
    SUM(conversions) AS conversions,
    SUM(attributed_revenue) AS attributed_revenue,
    CAST(SUM(conversions) AS FLOAT) / NULLIF(SUM(touches), 0) AS conversion_rate,
    SUM(attributed_revenue) / NULLIF(SUM(touches) * 7.5, 0) AS roi_index
FROM gold_campaign_roi_summary
GROUP BY campaign_month, campaign_id, campaign_name, channel;

CREATE OR ALTER VIEW dbo.vw_customer_value AS
SELECT
    region,
    segment,
    credit_tier,
    COUNT(*) AS customers,
    SUM(web_events) AS web_events,
    SUM(funded_sales) AS funded_sales,
    SUM(lifetime_sales_amount) AS lifetime_sales_amount,
    SUM(lifetime_estimated_revenue) AS lifetime_estimated_revenue
FROM gold_customer_360
GROUP BY region, segment, credit_tier;
