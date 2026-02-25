import pandas as pd

df = pd.read_csv("data/raw/olist_order_items_dataset.csv")

df = df.apply(lambda col: col.str.strip() if col.dtype == "object" else col)
df["shipping_limit_date"] = pd.to_datetime(df["shipping_limit_date"], errors="coerce")
df.to_csv("data/processed/order_items_clean.csv", index=False)
print(df.dtypes)
