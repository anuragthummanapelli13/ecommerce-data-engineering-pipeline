import os
import pandas as pd

INPUT_FILE = "data/processed/orders_clean.csv"
OUTPUT_DIR = "data/processed"


def main():
    if not os.path.exists(INPUT_FILE):
        raise FileNotFoundError(f"File not found: {INPUT_FILE}")

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    df = pd.read_csv(INPUT_FILE)

    # Sales by region
    sales_by_region = (
        df.groupby("region", as_index=False)["sales"]
        .sum()
        .sort_values("sales", ascending=False)
    )
    sales_by_region.to_csv(f"{OUTPUT_DIR}/sales_by_region.csv", index=False)

    # Monthly sales trend
    monthly_sales = (
        df.groupby(["order_year", "order_month"], as_index=False)["sales"]
        .sum()
        .sort_values(["order_year", "order_month"])
    )
    monthly_sales.to_csv(f"{OUTPUT_DIR}/monthly_sales.csv", index=False)

    # Customer summary
    customer_summary = (
        df.groupby("customer_id", as_index=False)
        .agg(
            total_sales=("sales", "sum"),
            total_orders=("order_id", "count")
        )
        .sort_values("total_sales", ascending=False)
    )
    customer_summary.to_csv(f"{OUTPUT_DIR}/customer_summary.csv", index=False)

    # Product summary
    product_summary = (
        df.groupby("product_name", as_index=False)
        .agg(
            total_sales=("sales", "sum"),
            total_quantity=("quantity", "sum")
        )
        .sort_values("total_sales", ascending=False)
    )
    product_summary.to_csv(f"{OUTPUT_DIR}/product_summary.csv", index=False)

    print("Transformation complete.")
    print("Files created:")
    print("data/processed/sales_by_region.csv")
    print("data/processed/monthly_sales.csv")
    print("data/processed/customer_summary.csv")
    print("data/processed/product_summary.csv")


if __name__ == "__main__":
    main()