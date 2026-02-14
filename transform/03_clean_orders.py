import pandas as pd
df = pd.read_csv("data/raw/olist_orders_dataset.csv")
df = df.apply(lambda col: col.str.strip() if col.dtype == "object" else col)

date_cols = [
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date"
]

for col in date_cols:
    df[col] = pd.to_datetime(df[col], errors="coerce")

df["has_approved"] = df["order_approved_at"].notna()
df["has_carrier_date"] = df["order_delivered_carrier_date"].notna()
df["has_delivered_date"] = df["order_delivered_customer_date"].notna()

mask = df['order_purchase_timestamp'].notna() & df['order_approved_at'].notna()
invalid = (df.loc[mask, 'order_purchase_timestamp'] > df.loc[mask, 'order_approved_at'])
mask1 = df['order_approved_at'].notna() & df['order_delivered_carrier_date'].notna()
invalid1 = ( df.loc[mask1, 'order_approved_at'] > df.loc[mask1, 'order_delivered_carrier_date'])
mask2 = df['order_delivered_carrier_date'].notna() & df['order_delivered_customer_date'].notna()
invalid2 = (df.loc[mask2, 'order_delivered_carrier_date'] == df.loc[mask2, 'order_delivered_customer_date'])

df['invalid_timestamps'] = False ## Timestamps not chronologically logical
df.loc[mask, 'invalid_timestamps'] = invalid
df.loc[mask1, 'invalid_timestamps'] = invalid1 | df.loc[mask1, 'invalid_timestamps']
df.loc[mask2, 'invalid_timestamps'] = invalid2 | df.loc[mask2, 'invalid_timestamps']

kpi_mask = (
    (df["order_status"] == "delivered") &
    (df["has_delivered_date"]) &
    (~df["invalid_timestamps"])
)

df.loc[kpi_mask, "order_date"] = df.loc[kpi_mask, "order_purchase_timestamp"].dt.date
df.loc[kpi_mask, "delivery_date"] = df.loc[kpi_mask, "order_delivered_customer_date"].dt.date
df.loc[kpi_mask, "delivery_days"] = (df.loc[kpi_mask, "order_delivered_customer_date"] - df.loc[kpi_mask, "order_purchase_timestamp"]).dt.days
df.loc[kpi_mask, "is_delayed"] = (df.loc[kpi_mask, "order_delivered_customer_date"] > df.loc[kpi_mask, "order_estimated_delivery_date"])

print(df.dtypes)
print(df.isna().sum())

df.to_csv("data/processed/orders_clean.csv", index=False)
