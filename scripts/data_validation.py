import os
import pandas as pd

INPUT_FILE = "data/processed/orders_clean.csv"
REPORT_FILE = "data/processed/validation_report.txt"


def main():
    if not os.path.exists(INPUT_FILE):
        raise FileNotFoundError(f"File not found: {INPUT_FILE}")

    df = pd.read_csv(INPUT_FILE)

    lines = []
    lines.append("DATA VALIDATION REPORT")
    lines.append("=" * 50)
    lines.append(f"Total rows: {len(df)}")
    lines.append(f"Total columns: {len(df.columns)}")
    lines.append("")

    lines.append("COLUMN NAMES")
    lines.append("-" * 50)
    for col in df.columns:
        lines.append(col)
    lines.append("")

    lines.append("NULL COUNTS")
    lines.append("-" * 50)
    null_counts = df.isnull().sum()
    for col, value in null_counts.items():
        lines.append(f"{col}: {value}")
    lines.append("")

    lines.append("DUPLICATE ROWS")
    lines.append("-" * 50)
    lines.append(f"Duplicate rows: {df.duplicated().sum()}")
    lines.append("")

    lines.append("SALES CHECKS")
    lines.append("-" * 50)
    lines.append(f"Negative sales rows: {(df['sales'] < 0).sum()}")
    lines.append(f"Zero sales rows: {(df['sales'] == 0).sum()}")
    lines.append("")

    lines.append("QUANTITY CHECKS")
    lines.append("-" * 50)
    lines.append(f"Negative quantity rows: {(df['quantity'] < 0).sum()}")
    lines.append(f"Zero quantity rows: {(df['quantity'] == 0).sum()}")
    lines.append("")

    lines.append("ORDER ID CHECKS")
    lines.append("-" * 50)
    lines.append(f"Distinct order IDs: {df['order_id'].nunique()}")
    lines.append("")

    lines.append("CUSTOMER ID CHECKS")
    lines.append("-" * 50)
    lines.append(f"Distinct customer IDs: {df['customer_id'].nunique()}")
    lines.append("")

    lines.append("DATA TYPES")
    lines.append("-" * 50)
    for col, dtype in df.dtypes.items():
        lines.append(f"{col}: {dtype}")

    report_text = "\n".join(lines)

    with open(REPORT_FILE, "w", encoding="utf-8") as f:
        f.write(report_text)

    print(report_text)
    print(f"\nValidation report saved to: {REPORT_FILE}")


if __name__ == "__main__":
    main()