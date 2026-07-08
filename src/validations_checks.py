import pandas as pd
import json
from data_quality import (
    check_nulls,
    check_duplicates,
    check_schema,
    check_row_count,
    check_date_validity,
    check_numeric_metrics,
    check_platform_validation,
    print_info,
    show_df_sample
)


df = pd.read_parquet("./data/cleaned_data/paid_media_output.parquet")


def print_check_result(result):
    symbol = "✅" if result["status"] == "PASS" else "❌"
    result["status"] = f"{symbol} {result['status']}"

    print(json.dumps(result, indent=4, ensure_ascii=False))


def run_validations():

    print("""
    -------------------
    Data Quality Checks

    1. Null check
    2. Schema check
    3. Duplicate check
    4. Date validity check
    5. Numeric metrics check
    6. Platform check
    7. Row count check
    8. Display cleaned file details
    9. Show cleaned file sample
    """)

    choice = input("Select check number: ")

    if choice == "1":
        result = check_nulls(df)
        print_check_result(result)

    elif choice == "2":
        result = check_schema(df)
        print_check_result(result)

    elif choice == "3":
        result = check_duplicates(df)
        print_check_result(result)

    elif choice == "4":
        result = check_date_validity(df)
        print_check_result(result)

    elif choice == "5":
        result = check_numeric_metrics(df)
        print_check_result(result)

    elif choice == "6":
        result = check_platform_validation(df)
        print_check_result(result)

    elif choice == "7":
        with open("./data/raw_data/paid_media_export.csv", "r") as f:
            raw_rows = sum(1 for _ in f) - 1 
        result = check_row_count(raw_rows,len(df))
        print_check_result(result)

    elif choice == "8":
        print_info(df)
    
    elif choice == "9":
        show_df_sample(df)

    else:
        print("Invalid option")
        return


run_validations()