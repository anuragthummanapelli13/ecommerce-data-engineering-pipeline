from extract_pipeline import extract_data
from transform_pipeline import transform_data
from validate_pipeline import validate_data
from load_postgres_pipeline import load_to_postgres

def main():

    df = extract_data()

    df = transform_data(df)

    validate_data(df)

    load_to_postgres(df)

    print("\nETL Pipeline completed successfully!")

if __name__ == "__main__":
    main()