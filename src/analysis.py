import pandas as pd

# Total spend by platform
def total_spend_by_platform(df):

    df = (
        df.groupby("platform", as_index=False)
        .agg({
            "spend": "sum"
        })
        .sort_values("spend", ascending=False)
    )

    print("\n***************************")
    print("Total spend by platform")
    print("---------------------------")

    print(f"{'platform':<40} {'spend':>20}")
    print("-" * 61)

    for _, row in df.iterrows():
        print(f"{row['platform']:<40} {row['spend']:>20,.2f}")
    print()


# Top 5 campaigns by spend
def top_campings_by_spend(df):
    df = (
        df.groupby("campaign_name", as_index=False)
        .agg({
            "spend": "sum"
        })
        .sort_values("spend", ascending=False)
        .head(5)
    )

    print("\n***************************")
    print("Top 5 campaigns by spend")
    print("---------------------------")

    print(f"{'campaign_name':<40} {'spend':>20}")
    print("-" * 61)

    for _, row in df.iterrows():
        print(f"{row['campaign_name']:<40} {row['spend']:>20,.2f}")
    print()


# Spend trend over time for one account
def spend_trend_by_account(df):

    account_id = df["account_id"].iloc[0]

    df = (
        df[df["account_id"] == account_id]
        .groupby("date", as_index=False)
        .agg({
            "spend": "sum"
        })
        .sort_values("date")
        .head(12)
    )

    print("\n***************************")
    print(f"Spend trend over time - account {account_id}")
    print("---------------------------")

    print(f"{'date':<40} {'spend':>20}")
    print("-" * 61)

    for _, row in df.iterrows():
        print(f"{row['date']:<40} {row['spend']:>20,.2f}")
    print()


# Average daily spend by platform
def average_daily_spend_by_platform(df):

    df = (
        df.groupby("platform")
        .agg(
            total_spend=("spend", "sum"),
            active_days=("date", "nunique")
        )
        .assign(
            average_daily_spend=lambda x: x["total_spend"] / x["active_days"]
        )
        .sort_values("average_daily_spend", ascending=False)
        .reset_index()
    )

    print("\n***************************")
    print("Average daily spend by platform")
    print("---------------------------")

    print(
        f"{'platform':<20}"
        f"{'total_spend':>20}"
        f"{'active_days':>18}"
        f"{'avg_daily_spend':>22}"
    )
    print("-" * 80)

    for _, row in df.iterrows():
        print(
            f"{row['platform']:<20}"
            f"{row['total_spend']:>20,.2f}"
            f"{row['active_days']:>18}"
            f"{row['average_daily_spend']:>22,.2f}"
        )
    print()


# Campaigns using USD currency
def campaigns_using_usd(df):

    df = (
        df[df["currency"] == "USD"]
        .groupby("campaign_name", as_index=False)
        .agg(
            total_spend=("spend", "sum")
        )
        .sort_values("total_spend", ascending=False)
    )

    print("\n***************************")
    print("Campaigns using USD currency")
    print("---------------------------")

    print(f"{'campaign_name':<40} {'total_spend':>20}")
    print("-" * 61)

    for _, row in df.iterrows():
        print(
            f"{row['campaign_name']:<40}"
            f"{row['total_spend']:>21,.2f}"
        )
    print()