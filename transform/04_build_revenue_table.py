import pandas as pd
orders = pd.read_csv("data/raw/olist_orders_dataset.csv")
order_items = pd.read_csv("data/raw/olist_order_items_dataset.csv")

orders = orders.apply(lambda col: col.str.strip() if col.dtype == "object" else col)
order_items = order_items.apply(lambda col: col.str.strip() if col.dtype == "object" else col)

joined = order_items.merge(orders, on="order_id", how="left")
## Compute item-level revenue
joined["total_per_item"] = joined["price"] + joined["freight_value"]

## Aggregate to order level
orders_level = (joined.groupby("order_id")
    .agg(order_items_revenue=("price", "sum"),
         order_freight=("freight_value", "sum"),
         order_total=("total_per_item", "sum"))
    .reset_index())

orders_level["order_items_revenue"] = orders_level["order_items_revenue"].round(2)
orders_level["order_total"] = orders_level["order_total"].round(2)
 
## orders_revenue_enriched.csv
orders_level.to_csv("data/processed/orders_revenue_enriched.csv", index=False)