import pandas as pd
from pathlib import Path
from transformation import transform_data


def process_chunks():
    
    print("***********************")
    print("Starting pipeline")
    print("***********************")

    input_file = Path("./data/raw_data/paid_media_export.csv")
    output_dir = Path("./data/processed_chunks")
    output_dir.mkdir(parents=True, exist_ok=True)

    for i, chunk in enumerate(pd.read_csv(input_file, dtype=str ,chunksize = 100000)):

        print(f"Processing chunk: {i + 1}")
        df = transform_data(chunk)

        df = (
            df.groupby(
                ["date", "platform", "account_id", "campaign_id"],
                as_index=False
            )
            .agg({
                "campaign_name": "first",
                "impressions": "sum",
                "clicks": "sum",
                "spend": "sum",
                "currency": "first",
                "conversions": "sum",
                "video_views": "sum"
            })
        )

        output_file = output_dir / f"chunk_{i + 1}.parquet"
        df.to_parquet(output_file, engine="pyarrow", index=False)

        print(f"Saved to file: {output_file}")
        print("-----------------------")

process_chunks()
print("All chunks are processed!!!")