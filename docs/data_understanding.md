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
  
## 2. Products
+ rows: 32951
+ columns: 9

| Column                       | Data Type | Non-Null Count | Notes |
|------------------------------|-----------|----------------|-------|
| `product_id`                 | str       | 32,951         | Primary key |
| `product_category_name`      | str       | 32,341         | Foreign key to customers table |
| `product_name_lenght`        | float64   | 32,341         | `processing`, `delivered`, `shipped`, `canceled`, etc |
| `product_description_lenght` | float64   | 32,341         | When the order is placed/created/checked out |
| `product_photos_qty`         | float64   | 32,341         | When payment is approved by the seller (could be nullable) |
| `product_weight_g`           | float64   | 32,949         | When order reached shipping carrier |
| `product_length_cm`          | float64   | 32,949         | When customer received the order |
| `product_height_cm`          | float64   | 32,949         | Estimated delivery date provided at purchase |
| `product_width_cm`           | float64   | 32,949         | Estimated delivery date provided at purchase |

- **Primary Key:** `product_id`
- **Relationships:** linked to *olist_order_items_dataset* via `product_id`
- **Data Issues:** `product_category_name` should be normalized
- **Missing Values:** 
    - `product_category_name`     : 610
    - `product_name_lenght`       : 610
    - `product_description_lenght`: 610
    - `product_photos_qty`        : 610
    - `product_weight_g`          : 2
    - `product_length_cm`         : 2
    - `product_height_cm`         : 2
    - `product_width_cm`          : 2 <2 products with no dimensions or weigth>
- **Duplicate Rows:** 
  - *ZERO* duplicate rows
  
## 3. Orders
+ rows: 99441
+ columns: 8

| Column                          | Data Type | Non-Null Count | Notes |
|---------------------------------|-----------|----------------|-------|
| `order_id`                      | str       | 99,441         | Primary key |
| `customer_id`                   | str       | 99,441         | Foreign key to customers table |
| `order_status`                  | str       | 99,441         | `processing`, `delivered`, `shipped`, `canceled`, etc |
| `order_purchase_timestamp`      | str       | 99,441         | When the order is placed/created/checked out |
| `order_approved_at`             | str       | 99,281         | When payment is approved by the seller (could be nullable) |
| `order_delivered_carrier_date`  | str       | 97,658         | When order reached shipping carrier |
| `order_delivered_customer_date` | str       | 96,476         | When customer received the order |
| `order_estimated_delivery_date` | str       | 99,441         | Estimated delivery date provided at purchase |


- **Primary Key:** `order_id`
- **Relationships:**
    - linked to *olist_customers_dataset*      via `customer_id`
    - linked to *olist_order_items_dataset*    via `order_id`
    - linked to *olist_order_payments_dataset* via `order_id`
    - linked to *olist_order_reviews_dataset*  via `order_id`
- **Data Issues:** 
    - Timestamps are stored as strings
    - Some orders have illogical timestamps, like when order_purchase_timestamp > order_approved_at
    - 8 orders are labeled as delivered but have missing delivery/approval timestamps. These records were kept, and delivery metrics were computed only when the required timestamps were available
- **Missing Values:** 
    - `order_approved_at`             :  160 <not approved yet by the seller>
    - `order_delivered_carrier_date`  : 1783 <not delivered yet to the shipping carrier>
    - `order_delivered_customer_date` : 2965 <not delivered yet to the customer>
    > 97% of orders are delivered.
- **Duplicate Rows:** 
    - *ZERO* duplicate rows
- **Order Status:** `delivered`, `shipped`, `canceled`, `unavailable`, `invoiced`, `processing`, `created`, `approved`

