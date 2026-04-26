import os
import pandas as pd

RAW_XLSX = "data/raw/orders.xlsx"
OUTPUT_FILE = "data/processed/orders_clean.csv"


def load_raw_data():
    if os.path.exists(RAW_XLSX):
        print("Loading Excel file...")
        return pd.read_excel(RAW_XLSX)
    else:
        raise FileNotFoundError(
            "File not found. Make sure orders.xlsx is inside data/raw/"
        )


def standardize_columns(df):
    df.columns = (
        df.columns.str.strip()
        .str.lower()
        .str.replace(" ", "_", regex=False)
        .str.replace("-", "_", regex=False)
    )
    return df


def rename_columns(df):
    rename_map = {
        "invoiceno": "order_id",
        "stockcode": "product_id",
        "description": "product_name",
        "quantity": "quantity",
        "invoicedate": "order_date",
        "unitprice": "unit_price",
        "customerid": "customer_id",
        "country": "region"
    }
    df = df.rename(columns=rename_map)
    return df


def clean_data(df):
    df = standardize_columns(df)
    df = rename_columns(df)

    print("Columns after renaming:")
    print(df.columns.tolist())

    df = df.drop_duplicates()

    df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")
    df["unit_price"] = pd.to_numeric(df["unit_price"], errors="coerce")
    df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")

    df["order_id"] = df["order_id"].fillna("Unknown").astype(str).str.strip()
    df["product_id"] = df["product_id"].fillna("Unknown").astype(str).str.strip()
    df["product_name"] = df["product_name"].fillna("Unknown").astype(str).str.strip()
    df["customer_id"] = df["customer_id"].fillna("Unknown").astype(str).str.strip()
    df["region"] = df["region"].fillna("Unknown").astype(str).str.strip()

    df = df.dropna(subset=["order_date"])

    df = df[df["quantity"] > 0]
    df = df[df["unit_price"] >= 0]

    df["sales"] = df["quantity"] * df["unit_price"]
    df = df[df["sales"] >= 0]

    df["order_year"] = df["order_date"].dt.year
    df["order_month"] = df["order_date"].dt.month
    df["order_day"] = df["order_date"].dt.day

    return df


def main():
    os.makedirs("data/processed", exist_ok=True)

    df = load_raw_data()
    print(f"Raw row count: {len(df)}")

    df_clean = clean_data(df)
    print(f"Clean row count: {len(df_clean)}")

    df_clean.to_csv(OUTPUT_FILE, index=False)
    print(f"Cleaned data saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()