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


def save_final_output(df, output_dir):
    output_file = output_dir / f"paid_media_output.parquet"
    df.to_parquet(output_file, index=False)
    print(f"Saved to file: {output_file}")


def generating_output():

    start_time = time.time()

    print("************************")
    print("Generating output file")
    print("************************")

    input_dir = Path("./data/batch_chunks")
    output_dir = Path("./data/cleaned_data")

    if output_dir.exists():
        shutil.rmtree(output_dir)

    output_dir.mkdir(exist_ok=True)

    files = list(input_dir.glob("*.parquet"))

    df = read_parquet_files(files)

    df = aggregate_data(df)

    save_final_output(df, output_dir)
        
    print("Cleaned output file is generated!!!")
    print("------------------------\n")

    return time.time() - start_time