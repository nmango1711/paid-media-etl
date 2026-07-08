import pandas as pd
from analysis import (
    total_spend_by_platform,
    top_campings_by_spend,
    spend_trend_by_account,
    average_daily_spend_by_platform,
    campaigns_using_usd
)


df = pd.read_parquet("./data/cleaned_data/paid_media_output.parquet")


def run_analysis():

    print("""
    -------------------
    Data Analysis

    1. Total spend by platform
    2. Top 5 campaigns by spend
    3. Spend trend over time for one account
    4. Average daily spend by platform
    5. Total spend of the campaigns using USD currency

    """)

    choice = input("Select analysis number: ")

    if choice == "1":
        total_spend_by_platform(df)
        return

    elif choice == "2":
        top_campings_by_spend(df)
        return
    
    elif choice == "3":
        spend_trend_by_account(df)
        return
    
    elif choice == "4":
        average_daily_spend_by_platform(df)
        return
    
    elif choice == "5":
        campaigns_using_usd(df)
        return

    else:
        print("Invalid option")
        return


run_analysis()