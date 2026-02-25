SELECT
    SUM(r.order_total) AS staging_revenue,
    SUM(f.order_items_revenue + f.order_freight_total) AS fact_revenue
FROM stg.stg_order_revenue r
JOIN dw.fact_orders f ON r.order_id = f.order_id;

SELECT
    (SELECT COUNT(DISTINCT order_id) FROM stg.stg_order_revenue) AS staging_orders,
    (SELECT COUNT(order_id) FROM dw.fact_orders) AS dw_orders;

SELECT order_id, COUNT(*)
FROM dw.fact_orders
GROUP BY order_id
HAVING COUNT(*) > 1;

SELECT f.order_id
FROM dw.fact_orders f
LEFT JOIN dw.dim_customers c
ON f.customer_sk = c.customer_sk
WHERE c.customer_sk IS NULL;

