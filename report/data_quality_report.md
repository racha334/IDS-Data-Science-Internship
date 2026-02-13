# Data Quality Report

**Dataset:** `olist_customers_dataset.csv` --> `customers_clean.csv` 
**Date:** 2026-02-13

## 1. Null Value Checks
- No missing values

## 2. Duplicate Checks
- **Customer IDs:** Unique, primray key
- No duplicate rows

## 3. Whitespace Checks
- All leading and trailing whitespaces have been trimmed

## 4. City Standardization
- All values in `customer_city` have been transformed into Title Case

## 5. State Standardization
- All values in `customer_state` were already in UPPERCASE.