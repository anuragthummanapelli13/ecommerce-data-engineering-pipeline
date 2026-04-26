import os
import pandas as pd
from sqlalchemy import create_engine

DB_FILE = "ecommerce_pipeline.db"

FILES = {
    "orders_clean": "data/processed/orders_clean.csv",
    "sales_by_region": "data/processed/sales_by_region.csv",
    "monthly_sales": "data/processed/monthly_sales.csv",
    "customer_summary": "data/processed/customer_summary.csv",
    "product_summary": "data/processed/product_summary.csv"
}


def main():
    engine = create_engine(f"sqlite:///{DB_FILE}")

    for table_name, path in FILES.items():
        if os.path.exists(path):
            df = pd.read_csv(path, low_memory=False)
            df.to_sql(table_name, engine, if_exists="replace", index=False)
            print(f"Loaded {table_name}")
        else:
            print(f"Skipped {table_name} because file not found")

    print(f"Database created: {DB_FILE}")


if __name__ == "__main__":
    main()