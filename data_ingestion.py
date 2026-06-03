import pandas as pd
import os

data_path = "data/raw"

files = os.listdir(data_path)

print("=" * 50)
print("DATASET ANALYSIS")
print("=" * 50)

for file in files:
    if file.endswith(".csv"):
        print(f"\n{'='*60}")
        print(file)
        print(f"{'='*60}")

        df = pd.read_csv(os.path.join(data_path, file))

        print("\nShape:")
        print(df.shape)

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())