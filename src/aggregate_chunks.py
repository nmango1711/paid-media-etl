from pathlib import Path
import pandas as pd
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
            "video_views": "sum",
        })
    )


def read_parquet_files(files):
    dfs = [pd.read_parquet(file) for file in files]
    return pd.concat(dfs, ignore_index=True)


def save_batch_chunk(df, output_dir, chunk_number):
    output_file = output_dir / f"batch_chunk_{chunk_number}.parquet"
    df.to_parquet(output_file, index=False)
    print(f"Saved to file: {output_file}")


def batch_aggregation():

    start_time = time.time()

    print("***********************")
    print("Batch aggregations")
    print("***********************")

    input_dir = Path("./data/ingestion_chunks")
    output_dir = Path("./data/batch_chunks")

    if output_dir.exists():
        shutil.rmtree(output_dir)

    output_dir.mkdir(exist_ok=True)

    files = list(input_dir.glob("*.parquet"))

    batch_size = 10

    for batch_number, i in enumerate(range(0, len(files), batch_size), start = 1):

        print(f"Processing batch chunk: {batch_number}")

        batch_files = files[i:i + batch_size]

        df = read_parquet_files(batch_files)
        df = aggregate_data(df)

        save_batch_chunk(df, output_dir, batch_number)

        print("-----------------------")
        
    print("All batch chunks are aggregated and saved!!!")

    return time.time() - start_time