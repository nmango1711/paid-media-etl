import pandas as pd

def transform_data(df):
    newdf = df.copy()
    newdf["date"] = newdf["date"].str.strip()

    changed_rows = (df["date"] != newdf["date"]) & ~(df["date"].isna() & newdf["date"].isna())

    # Get first changed row index
    if changed_rows.any():
        idx = changed_rows[changed_rows].index[0]

    # Print original and cleaned value
        value = df.loc[idx, "date"]

        print("Before:")
        print(value)
        print("Length:", len(str(value)))

        value2 = newdf.loc[idx, "date"]

        print("\nAfter:")
        print(value2)
        print("Length:", len(str(value2)))

    print("Rows changed:", changed_rows.sum())


    rows_before = len(df)
    rows_after = len(df)
    print(rows_before)
    print(rows_after)
    print(f"Dropped rows: {rows_before - rows_after}")