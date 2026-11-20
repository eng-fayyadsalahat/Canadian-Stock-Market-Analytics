import requests
import pandas as pd

BASE_URL = "https://www.bankofcanada.ca/valet/observations/"

series = {
    "Policy_Rate": "V39079",
    "Bond_Yield_10Y": "BD.CDN.10YR.DQ.YLD",
    "USD_CAD": "FXUSDCAD"
}

start_date = "1970-01-01"
end_date = "2026-11-07"

dataframes = []

for column_name, series_code in series.items():

    url = (
        f"{BASE_URL}{series_code}/json"
        f"?start_date={start_date}"
        f"&end_date={end_date}"
    )

    response = requests.get(url, timeout=60)
    response.raise_for_status()

    observations = response.json()["observations"]

    df = pd.DataFrame([
        {
            "Date": item["d"],
            column_name: item[series_code]["v"]
        }
        for item in observations
        if item[series_code].get("v") is not None
    ])

    df["Date"] = pd.to_datetime(df["Date"])
    df[column_name] = pd.to_numeric(
        df[column_name],
        errors="coerce"
    )

    df = df.dropna(subset=[column_name])

    dataframes.append(df)

    print(f"\n{column_name}")
    print("Series Code:", series_code)
    print("Observations:", len(df))
    print("Start:", df["Date"].min())
    print("End:", df["Date"].max())

# Merge the three series by date
bank_canada = dataframes[0]

for df in dataframes[1:]:
    bank_canada = bank_canada.merge(
        df,
        on="Date",
        how="outer"
    )

bank_canada = bank_canada.sort_values("Date").reset_index(drop=True)

print("\nFinal Dataset:")
print(bank_canada.info())

print(bank_canada.head())
print(bank_canada.tail())

print("Shape:", bank_canada.shape)

print("\nMissing Values:")
print(bank_canada.isna().sum())

print("\nDuplicate Dates:")
print(bank_canada["Date"].duplicated().sum())

print("\nDate Range:")
print(bank_canada["Date"].min())
print(bank_canada["Date"].max())

print("\nDescriptive Statistics:")
print(bank_canada.describe().T)



for column in ["Policy_Rate", "Bond_Yield_10Y", "USD_CAD"]:

    first_date = bank_canada.loc[
        bank_canada[column].notna(), "Date"
    ].min()

    last_date = bank_canada.loc[
        bank_canada[column].notna(), "Date"
    ].max()

    period_data = bank_canada.loc[
        bank_canada["Date"].between(first_date, last_date)
    ]

    print(f"\n{column}")
    print("First available:", first_date)
    print("Last available:", last_date)
    print("Missing within coverage:", period_data[column].isna().sum())
    print("Available observations:", period_data[column].notna().sum())



# bank_canada.to_csv("canada_bank_of_canada_daily.csv",index=False)

for column in ["Policy_Rate", "Bond_Yield_10Y", "USD_CAD"]:

    missing_dates = bank_canada.loc[
        bank_canada[column].isna()
        & bank_canada["Date"].between(
            bank_canada.loc[bank_canada[column].notna(), "Date"].min(),
            bank_canada.loc[bank_canada[column].notna(), "Date"].max()
        ),
        "Date"
    ]

    print(f"\n{column}")
    print("Missing dates:", len(missing_dates))
    print(missing_dates.to_list()[:20])

bank_canada.to_csv(
    "canada_bank_of_canada_daily.csv",
    index=False
)