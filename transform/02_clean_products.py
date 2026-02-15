import pandas as pd

df_raw = pd.read_csv("data/raw/olist_products_dataset.csv")
df = df_raw.copy()

df = df.apply(lambda col: col.str.strip() if col.dtype == "object" else col)
df['product_category_name'] = df['product_category_name'].fillna("unknown")
df['product_category_name'] = df['product_category_name'].str.lower().str.replace(" ", "_", regex=False)

df = df.rename(columns={"product_name_lenght": "product_name_length", "product_description_lenght": "product_description_length"})

df.to_csv("data/processed/products_clean.csv", index=False)
