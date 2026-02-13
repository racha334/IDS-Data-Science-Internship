# Data Quality Report

**Dataset:** `olist_customers_dataset.csv` --> `customers_clean.csv` 
**Date:** 2026-02-13

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
- 
## 5. Non delivered Orders
- All non delivered orders have been dropped

## 6. Indicators:
Some simple indicators have been added
- order_date
- delivery_date
- delivery_days   : delivery_date - order_date
- is_delayed      : delivery_date > order_estimated_delivery_date
- has_approved    : approval date available
- has_carrier_date: carrier delivery date available
- has_delivered   : customer delivery date available

