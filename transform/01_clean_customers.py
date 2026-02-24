import pandas as pd

df_raw = pd.read_csv("data/raw/olist_customers_dataset.csv")
df = df_raw.copy()

df = df.apply(lambda col: col.str.strip() if col.dtype == "object" else col)
df['customer_city'] = df['customer_city'].str.title()
df['customer_state'] = df['customer_state'].str.upper() #Not necessary, as all values are already in uppercase

df.to_csv("data/processed/customers_clean.csv", index=False)
print(df.dtypes)