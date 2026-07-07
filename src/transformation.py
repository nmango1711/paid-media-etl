import pandas as pd

def transform_data(df):
    
    key_cols = ["date", "platform", "account_id", "campaign_id"]
    df[key_cols] = df[key_cols].apply(lambda x: x.str.strip())
    df[key_cols] = df[key_cols].replace(
        ["", "n/a", "N/A", "null", "NULL",],
        pd.NA
    )

    df = df.dropna(subset=key_cols)
    
    # Date transformations
    df["date"] = pd.to_datetime(df["date"], errors="coerce", format="mixed")
    df = df.dropna(subset=["date"])
    df["date"] = df["date"].dt.strftime("%Y-%m-%d")

    

    return df

    
