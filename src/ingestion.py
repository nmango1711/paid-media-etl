import pandas as pd
from pathlib import Path
from transformation import transform_data

input_file = Path("./data/raw_data/paid_media_export.csv")
output_dir = Path("./data/processed_data")

output_dir.mkdir(parents=True, exist_ok=True)

for i, chunk in enumerate(pd.read_csv(input_file, chunksize = 100000)):

    print(f"Processing chunk {i + 1}")
    df = transform_data(chunk)
    # 1. CLEANING
    # chunk = clean_data(chunk)

    # 2. TRANSFORMATION
    # chunk = transform_data(chunk)

    # 3. AGGREGATION INSIDE CHUNK
    # chunk = aggregate_data(chunk)

    # 4. WRITE CHUNK RESULT TO DISK
    print(f"Null dates: {chunk['date'].isna().sum()}")
    # chunk = chunk.dropna(subset=["date"])
    output_file = output_dir / f"chunk_{i + 1}.parquet"
    df.to_parquet(output_file, engine="pyarrow", index=False)

    print(f"Saved {output_file}")

print("All chunks processed")
