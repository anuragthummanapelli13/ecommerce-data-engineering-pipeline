from sqlalchemy import create_engine
from urllib.parse import quote_plus

POSTGRES_PASSWORD = "Anurag@1320"
ENCODED_PASSWORD = quote_plus(POSTGRES_PASSWORD)

DATABASE_URL = f"postgresql+psycopg2://postgres:{ENCODED_PASSWORD}@localhost:5432/ecommerce_db"

def load_to_postgres(df):
    print("Loading data into PostgreSQL...")

    engine = create_engine(DATABASE_URL)

    df.to_sql(
        "orders_clean",
        engine,
        if_exists="replace",
        index=False
    )

    print("Data loaded successfully.")