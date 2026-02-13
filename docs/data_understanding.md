# Data Understanding

## 1. Customers
+ rows: 99441
+ columns: 5

| Column                     | Data Type | Non-Null Count | Notes |
|----------------------------|-----------|----------------|-------|
| `customer_id`              | str       | 99,441         | Primary key |
| `customer_unique_id`       | str       | 99,441         |  |
| `customer_zip_code_prefix` | int64     | 99,441         | ZIP code prefix |
| `customer_city`            | str       | 99,441         | City name |
| `customer_state`           | str       | 99,441         | State abbreviation |

- **Primary Key:** `customer_id`
- **Relationships:** linked to *olist_orders_dataset* via `customer_id`
- **Data Issues:** `customer_city` are not titles
- **Missing Values:** 
  - *ZERO* missing values
- **Duplicate Rows:** 
  - *ZERO* duplicate rows
