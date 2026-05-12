import pandas as pd

FILE_PATH = "data/processed/orders_clean.csv"

print("Starting data quality checks...")

df = pd.read_csv(FILE_PATH, low_memory=False)

# -----------------------------
# Null Checks
# -----------------------------
print("\nNULL VALUE CHECKS")
print(df.isnull().sum())

# -----------------------------
# Duplicate Checks
# -----------------------------
duplicates = df.duplicated().sum()

print("\nDUPLICATE CHECKS")
print(f"Duplicate rows: {duplicates}")

# -----------------------------
# Negative Quantity Checks
# -----------------------------
negative_qty = df[df["quantity"] < 0]

print("\nNEGATIVE QUANTITY CHECKS")
print(f"Negative quantity rows: {len(negative_qty)}")

# -----------------------------
# Negative Sales Checks
# -----------------------------
negative_sales = df[df["sales"] < 0]

print("\nNEGATIVE SALES CHECKS")
print(f"Negative sales rows: {len(negative_sales)}")

# -----------------------------
# Invalid Date Checks
# -----------------------------
invalid_dates = df["order_date"].isnull().sum()

print("\nINVALID DATE CHECKS")
print(f"Invalid dates: {invalid_dates}")

print("\nData quality checks completed successfully!")