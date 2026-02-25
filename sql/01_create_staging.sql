CREATE SCHEMA IF NOT EXISTS stg;
DROP TABLE IF EXISTS stg.stg_customers;
DROP TABLE IF EXISTS stg.stg_products;
DROP TABLE IF EXISTS stg.stg_orders;
DROP TABLE IF EXISTS stg.stg_order_revenue;

CREATE TABLE stg.stg_customers (
    customer_id TEXT,
    customer_unique_id TEXT,
    customer_zip_code_prefix INT,
    customer_city TEXT,
    customer_state TEXT
);
CREATE TABLE stg.stg_products (
    product_id TEXT,
    product_category_name TEXT,
    product_name_length INT,
    product_description_length INT,
    product_photos_qty INT,
    product_weight_g INT,
    product_length_cm INT,
    product_height_cm INT,
    product_width_cm INT
);
CREATE TABLE stg.stg_orders (
    order_id TEXT,
    customer_id TEXT,
    order_status TEXT,
    order_purchase_timestamp TIMESTAMP,
    order_approved_at TIMESTAMP,
    order_delivered_carrier_date TIMESTAMP,
    order_delivered_customer_date TIMESTAMP,
    order_estimated_delivery_date TIMESTAMP,
    has_approved BOOLEAN,
    has_carrier_date BOOLEAN,
    has_delivered_date BOOLEAN,
    invalid_timestamps BOOLEAN,
    order_date TIMESTAMP,
    delivery_date TIMESTAMP,
    delivery_days INT,
    is_delayed BOOLEAN
);
CREATE TABLE stg.stg_order_revenue (
    order_id TEXT,
    order_items_revenue NUMERIC(10,2),
    order_freight NUMERIC(10,2),
    order_total NUMERIC(10, 2)
);