import pandas as pd

# Check nulls
def check_nulls(df):
    columns = [
        "date",
        "platform",
        "account_id",
        "campaign_id"
    ]

    results = {}

    for col in columns:
        results[col] = int(df[col].isna().sum())

    passed = all(count == 0 for count in results.values())

    return {
        "check": "Target grain null validation",
        "status": "PASS" if passed else "FAIL",
        "results": results,
        "rows_checked": int(len(df))
    }

# Check schema
def check_schema(df):
    required_columns = [
        "date",
        "platform",
        "account_id",
        "campaign_id",
        "campaign_name",
        "impressions",
        "clicks",
        "spend",
        "currency",
        "conversions",
        "video_views",
    ]

    missing_columns = [
        col for col in required_columns
        if col not in df.columns
    ]

    passed = len(missing_columns) == 0

    return {
        "check": "Schema validation",
        "status": "PASS" if passed else "FAIL",
        "missing_columns": missing_columns,
        "columns_found": len(df.columns),
        "rows_checked": len(df)
    }

# Check duplicates
def check_duplicates(df):
    grain_columns = [
        "date",
        "platform",
        "account_id",
        "campaign_id"
    ]

    duplicate_count = (
        df.duplicated(
            subset=grain_columns,
            keep=False
        )
        .sum()
    )

    passed = duplicate_count == 0

    return {
        "check": "Target grain duplicate validation",
        "status": "PASS" if passed else "FAIL",
        "duplicate_rows": int(duplicate_count),
        "rows_checked": int(len(df))
    }

# Check date validity
def check_date_validity(df):
    df["date"] = pd.to_datetime(df["date"], errors="coerce")

    invalid_dates = df["date"].isna().sum()
    future_dates = (df["date"] > pd.Timestamp.today().normalize()).sum()

    passed = invalid_dates == 0 and future_dates == 0

    return {
        "check": "Date validity validation",
        "status": "PASS" if passed else "FAIL",
        "invalid_dates": int(invalid_dates),
        "future_dates": int(future_dates),
        "rows_checked": int(len(df))
}

# Check numeric metrics
def check_numeric_metrics(df):
    metrics = [
        "impressions",
        "clicks",
        "spend",
        "conversions",
        "video_views"
    ]

    invalid_values = {}

    for col in metrics:
        negative_count = (df[col] < 0).sum()
        invalid_values[col] = int(negative_count)

    failed_columns = {
        col: count
        for col, count in invalid_values.items()
        if count > 0
    }

    passed = len(failed_columns) == 0

    return {
        "check": "Numeric metrics validation",
        "status": "PASS" if passed else "FAIL",
        "negative_values": failed_columns,
        "rows_checked": int(len(df))
}

# Check platform values
def check_platform_validation(df):
    allowed_platforms = {
        "meta",
        "google_ads"
    }

    invalid_platforms = (
        df.loc[
            ~df["platform"].isin(allowed_platforms),
            "platform"
        ]
        .unique()
        .tolist()
    )

    passed = len(invalid_platforms) == 0

    return {
        "check": "Platform validation",
        "status": "PASS" if passed else "FAIL",
        "invalid_platforms": invalid_platforms,
        "rows_checked": int(len(df))
}

# Check row count
def check_row_count(raw_count, cleaned_count):
    
    removed_rows = raw_count - cleaned_count
    removal_percentage = (removed_rows / raw_count) * 100

    return {
        "check": "Row count monitoring",
        "status": "PASS",
        "raw_rows": int(raw_count),
        "cleaned_rows": int(cleaned_count),
        "removed_rows": int(removed_rows),
        "removal_percentage": round(removal_percentage, 2)
}

# Print df info
def print_info(df):
    print(df.info())

# Show df sample
def show_df_sample(df):
    print(df.head(10))