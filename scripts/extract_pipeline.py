import pandas as pd

FILE_PATH = "data/raw/orders.xlsx"

def extract_data():
    print("Extracting raw data...")
    
    df = pd.read_excel(FILE_PATH)

    print(f"Rows extracted: {len(df)}")

    return df