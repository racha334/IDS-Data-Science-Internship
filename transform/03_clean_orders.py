import pandas as pd

df_raw = pd.read_csv("data/raw/olist_orders_dataset.csv")
df = df_raw.copy()

df = df.apply(lambda col: col.str.strip() if col.dtype == "object" else col)

date_cols = [
    'order_purchase_timestamp',
    'order_approved_at',
    'order_delivered_carrier_date',
    'order_delivered_customer_date',
    'order_estimated_delivery_date'
]

for col in date_cols:
    df[col] = pd.to_datetime(df[col])

df = df[df['order_status'] == 'delivered'].copy()

df['order_date'] = df['order_purchase_timestamp'].dt.date
df['delivery_date'] = df['order_delivered_customer_date'].dt.date

df['delivery_days'] = (df['order_delivered_customer_date'] - df['order_purchase_timestamp']).dt.days

df["is_delayed"] = (
    df["order_delivered_customer_date"].notna()
    & (df["order_delivered_customer_date"] > df["order_estimated_delivery_date"])
)

df["has_approved"] = df["order_approved_at"].notna()
df["has_carrier_date"] = df["order_delivered_carrier_date"].notna()
df["has_delivered_date"] = df["order_delivered_customer_date"].notna()

df.to_csv("data/processed/orders_clean.csv", index=False)