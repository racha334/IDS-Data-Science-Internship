# Data Quality Report

**Dataset:** `olist_customers_dataset.csv` --> `customers_clean.csv` 
**Date:** 2026-02-12

## 1. Null Value Checks
- No missing values

## 2. Duplicate Checks
- **Customer ID:** Unique, primray key
- No duplicate rows

## 3. Whitespace Checks
- All leading and trailing whitespaces have been trimmed

## 4. City Standardization
- All values in `customer_city` have been transformed into Title Case

## 5. State Standardization
- All values in `customer_state` were already in UPPERCASE.


**Dataset:** `olist_products_dataset.csv` --> `products_clean.csv` 
**Date:** 2026-02-13

## 1. Null Value Checks
- product_name_lenght           610
- product_description_lenght    610
- product_photos_qty            610
- product_weight_g                2
- product_length_cm               2
- product_height_cm               2
- product_width_cm                2

## 2. Duplicate Checks
- **Product ID:** Unique, primray key
- No duplicate rows

## 3. Whitespace Checks
- All leading and trailing whitespaces have been trimmed

## 4. Normalization:
- Converted all letters to lowercase in `product_category_name`
- Replaced spaces with underscores `product_category_name`


**Dataset:** `olist_orders_dataset.csv` --> `orders_clean.csv` 
**Date:** 2026-02-13

## 1. Null Value Checks
- No missing values -----<<<>>>

## 2. Duplicate Checks
- **Order ID:** Unique, primray key
- **Customer ID:** Unique, foreign key
- No duplicate rows

## 3. Whitespace Checks
- All leading and trailing whitespaces have been trimmed

## 4. Datatype Checks
- Timestamps were converted from strings to datetime

## 5. Non delivered Orders
- All non delivered orders have been dropped

## 6. Indicators:
Some simple indicators have been added
- order_date
- delivery_date
- delivery_days     : delivery_date - order_date
- is_delayed        : delivery_date > order_estimated_delivery_date
- has_approved      : approval date available
- has_carrier_date  : carrier delivery date available
- has_delivered     : customer delivery date available
- invalid_timestamps: True if one of these inequalities is true: purchase > approval >= carrier >= delivered

## 7. Delivery Consistency
- Purchase date VS Delivery Date
- 13 orders have been delivered in the same day 
- 26380 order have been delivered after more than 14 days
- Delivery Date VS Estimated Delivery Date
- 88649 orders were *early*
- 7827  orders were *delayed*
- 2965  orders were *estimated correctly*

## 8. Invalid Timestamps
- purchase >  approval : 0
- approval >= carrier  : 1359
    - 1350 delivered
    - 9    shipped
- carrier  >= delivered: 32
    - 32 delivered


