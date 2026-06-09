print("Data ingestion script is working!")
import pandas as pd
import os

DATA_PATH = "data/raw"

csv_files = [f for f in os.listdir(DATA_PATH) if f.endswith(".csv")]

print(f"Found {len(csv_files)} CSV files\n")

for file in csv_files:

    print("=" * 50)
    print(f"Dataset: {file}")

    df = pd.read_csv(os.path.join(DATA_PATH, file))

    print("\nShape:")
    print(df.shape)

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Rows:")
    print(df.duplicated().sum())

    print("\n")