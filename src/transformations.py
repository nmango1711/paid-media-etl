import pandas as pd


# "date" transformations
def transform_date(df):
    df["date"] = df["date"].str.strip()
    df["date"] = df["date"].replace("", pd.NA)
    df["date"] = pd.to_datetime(df["date"], errors="coerce", format="mixed")
    df = df.dropna(subset=["date"])
    df = df[df["date"] <= pd.Timestamp.today().normalize()]
    df["date"] = df["date"].dt.strftime("%Y-%m-%d")
    return df


# "platform" transformations
def transform_platform(df):
    df["platform"] = (
        df["platform"]
        .str.lower()
        .str.strip()
        .str.replace(r"[-_]", " ", regex=True)
        .str.replace(r"\s+", " ", regex=True)
    )
    df["platform"] = df["platform"].replace("", pd.NA)
    df = df.dropna(subset=["platform"])
    mapping = {
        "facebook": "meta",
        "meta": "meta",
        "google ads": "google_ads",
    }
    df["platform"] = df["platform"].map(mapping)
    df = df.dropna(subset=["platform"])
    return df


# "account_id" transformations
def transform_account_id(df):
    df["account_id"] = (
        df["account_id"]
        .str.strip()
        .str.replace(r"\s+", "", regex=True)
    )
    df["account_id"] = df["account_id"].replace("", pd.NA)
    df = df.dropna(subset=["account_id"])
    return df


# "campaign_id" transformations
def transform_campaign_id(df):
    df["campaign_id"] = (
        df["campaign_id"]
        .str.strip()
        .str.replace(r"\s+", "", regex=True)
    )
    df["campaign_id"] = df["campaign_id"].replace("", pd.NA)
    df = df.dropna(subset=["campaign_id"])
    return df


# "campaign_name" transformations
def transform_campaign_name(df):
    df["campaign_name"] = (
        df["campaign_name"]
        .str.lower()
        .str.strip()
        .str.replace(r"\s+", " ", regex=True)
    )
    df["campaign_name"] = df["campaign_name"].replace("", pd.NA)
    df["campaign_name"] = df["campaign_name"].fillna("UNKNOWN")
    return df


# "impressions" transformations
def transform_impressions(df):
    df["impressions"] = (
        df["impressions"]
        .str.replace(",", "", regex=False)
        .str.strip()
    )
    df["impressions"] = df["impressions"].replace("", pd.NA)
    df["impressions"] = pd.to_numeric(df["impressions"], errors="coerce")
    df = df.dropna(subset=["impressions"])
    df = df[df["impressions"] >= 0]
    df = df[df["impressions"].mod(1) == 0]
    df["impressions"] = df["impressions"].astype("int64")
    return df


# "clicks" transformations
def transform_clicks(df):
    df["clicks"] = (
        df["clicks"]
        .str.replace(",", "", regex=False)
        .str.strip()
    )
    df["clicks"] = df["clicks"].replace("", pd.NA)
    df["clicks"] = pd.to_numeric(df["clicks"], errors="coerce")
    df = df.dropna(subset=["clicks"])
    df = df[df["clicks"] >= 0]
    df = df[df["clicks"].mod(1) == 0]
    df["clicks"] = df["clicks"].astype("int64")
    return df


# "spend" transformations
def transform_spend(df):
    df["spend"] = (
        df["spend"]
        .str.replace(",", "", regex=False)
        .str.strip()
    )
    df["spend"] = df["spend"].replace("", pd.NA)
    df["spend"] = pd.to_numeric(df["spend"], errors="coerce")
    df = df.dropna(subset=["spend"])
    df = df[df["spend"] >= 0]
    df["spend"] = df["spend"].round(2)
    return df


# "currency" transformations
def transform_currency(df):
    df["currency"] = (
        df["currency"]
        .str.upper()
        .str.strip()
    )
    df["currency"] = df["currency"].replace("", pd.NA)
    currency_map = {
        "EURO": "EUR",
    }
    df["currency"] = df["currency"].replace(currency_map)
    df["currency"] = df["currency"].fillna("UNKNOWN")
    return df


# "conversions" transformations
def transform_conversions(df):
    df["conversions"] = (
        df["conversions"]
        .str.strip()
    )
    df["conversions"] = df["conversions"].replace("", pd.NA)
    df["conversions"] = pd.to_numeric(df["conversions"], errors="coerce")
    df["conversions"] = df["conversions"].fillna(0)
    df = df[df["conversions"] >= 0]
    return df


# "video_views" transformations
def transform_video_views(df):
    df["video_views"] = (
        df["video_views"]
        .str.strip()
    )
    df["video_views"] = df["video_views"].replace("", pd.NA)
    df["video_views"] = pd.to_numeric(df["video_views"], errors="coerce")
    df["video_views"] = df["video_views"].fillna(0)
    df = df[df["video_views"] >= 0]
    return df