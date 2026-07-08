import pandas as pd
from pathlib import Path
from src.pipeline import transform_data
import time, shutil

def aggregate_data(df):
    return (
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


def save_parquet(df, output_dir, chunk_number):
    output_file = output_dir / f"ingestion_chunk_{chunk_number}.parquet"
    df.to_parquet(output_file, engine="pyarrow", index=False)
    print(f"Saved to file: {output_file}")


def process_ingestion_chunks():

    start_time = time.time()

    print("************************")
    print("Starting pipeline")
    print("************************")
    
    input_file = Path("./data/raw_data/paid_media_export.csv")
    output_dir = Path("./data/ingestion_chunks")

    if output_dir.exists():
        shutil.rmtree(output_dir)
    
    output_dir.mkdir(parents=True, exist_ok=True)

    for i, chunk in enumerate(pd.read_csv(input_file, dtype=str ,chunksize = 150000), start = 1):

        print(f"Processing ingestion chunk: {i}")

        df = transform_data(chunk)
        df = aggregate_data(df)

        save_parquet(df, output_dir, i)

        print("------------------------")

    print("All ingestion chunks are processed and saved!!!")
    print("------------------------\n")

    return time.time() - start_time