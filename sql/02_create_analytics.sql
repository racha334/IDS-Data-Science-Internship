CREATE SCHEMA IF NOT EXISTS dw;
DROP TABLE IF EXISTS dw.fact_orders CASCADE;
DROP TABLE IF EXISTS dw.dim_customers CASCADE;
DROP TABLE IF EXISTS dw.dim_products CASCADE;
DROP TABLE IF EXISTS dw.dim_date CASCADE;

CREATE TABLE dw.dim_customers (
    customer_sk BIGSERIAL PRIMARY KEY,
    customer_id TEXT UNIQUE,
    customer_unique_id TEXT,
    customer_zip_code_prefix INT,
    customer_city TEXT,
    customer_state TEXT
);
CREATE TABLE dw.dim_products (
    product_sk BIGSERIAL PRIMARY KEY,
    product_id TEXT UNIQUE,
    product_category_name TEXT,
    product_name_length INT,
    product_description_length INT,
    product_photos_qty INT,
    product_weight_g INT,
    product_length_cm INT,
    product_height_cm INT,
    product_width_cm INT
);
CREATE TABLE dw.dim_date (
    date_sk BIGSERIAL PRIMARY KEY,
    date DATE UNIQUE,
    day INT,
    month INT,
    year INT,
    weekday TEXT
);
CREATE TABLE dw.fact_orders (
    order_id TEXT PRIMARY KEY,
    customer_sk BIGINT,
    order_date_sk INT,
    order_items_revenue NUMERIC(10,2),
    order_freight_total NUMERIC(107,2),
    delivery_days INT,
    is_delayed BOOLEAN,
    FOREIGN KEY (customer_sk) REFERENCES dw.dim_customers(customer_sk),
    FOREIGN KEY (order_date_sk) REFERENCES dw.dim_date(date_sk)
);

INSERT INTO dw.dim_customers (customer_id, customer_unique_id, customer_zip_code_prefix, customer_city, customer_state)
SELECT DISTINCT customer_id, customer_unique_id, customer_zip_code_prefix, customer_city, customer_state
FROM stg.stg_customers;

INSERT INTO dw.dim_products (product_id, product_category_name, product_name_length, product_description_length, product_photos_qty, product_weight_g, product_length_cm, product_height_cm, product_width_cm)
SELECT DISTINCT product_id, product_category_name, product_name_length, product_description_length, product_photos_qty, product_weight_g, product_length_cm, product_height_cm, product_width_cm
FROM stg.stg_products;

INSERT INTO dw.dim_date (date, day, month, year, weekday)
SELECT DISTINCT DATE(order_purchase_timestamp),
       EXTRACT(DAY FROM order_purchase_timestamp),
       EXTRACT(MONTH FROM order_purchase_timestamp),
       EXTRACT(YEAR FROM order_purchase_timestamp),
       TO_CHAR(order_purchase_timestamp,'Day')
FROM stg.stg_orders;

INSERT INTO dw.fact_orders (order_id, customer_sk, order_date_sk, order_items_revenue, order_freight_total, delivery_days, is_delayed)
SELECT
    o.order_id,
    c.customer_sk,
    d.date_sk,
    r.order_items_revenue,
    r.order_freight,
    EXTRACT(DAY FROM (o.order_delivered_customer_date - o.order_purchase_timestamp)) AS delivery_days,
    (o.order_delivered_customer_date > o.order_estimated_delivery_date) AS is_delayed
FROM stg.stg_orders o
JOIN stg.stg_order_revenue r ON o.order_id = r.order_id
JOIN dw.dim_customers c ON o.customer_id = c.customer_id
JOIN dw.dim_date d ON DATE(o.order_purchase_timestamp) = d.date