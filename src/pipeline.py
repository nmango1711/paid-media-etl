from src.transformations import (
    transform_date,
    transform_platform,
    transform_account_id,
    transform_campaign_id,
    transform_campaign_name,
    transform_impressions,
    transform_clicks,
    transform_spend,
    transform_currency,
    transform_conversions,
    transform_video_views
)

def transform_data(df):
    df = transform_date(df)
    df = transform_platform(df)
    df = transform_account_id(df)
    df = transform_campaign_id(df)
    df = transform_campaign_name(df)
    df = transform_impressions(df)
    df = transform_clicks(df)
    df = transform_spend(df)
    df = transform_currency(df)
    df = transform_conversions(df)
    df = transform_video_views(df)
    return df