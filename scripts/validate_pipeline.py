def validate_data(df):

    print("Running validation checks...")

    print("\nNull values:")
    print(df.isnull().sum())

    print("\nDuplicate rows:")
    print(df.duplicated().sum())

    print("\nNegative sales rows:")
    print(len(df[df["sales"] < 0]))

    print("\nValidation completed.")