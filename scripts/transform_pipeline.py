def transform_data(df):
    print("Transforming data...")

    df.columns = [
        "order_id",
        "product_id",
        "product_name",
        "quantity",
        "order_date",
        "unit_price",
        "customer_id",
        "region"
    ]

    df = df.drop_duplicates()
    df = df.dropna()

    df = df[df["quantity"] > 0]
    df = df[df["unit_price"] >= 0]

    df["sales"] = df["quantity"] * df["unit_price"]

    df["order_date"] = df["order_date"].astype(str)

    print("Transformation completed.")
    return df