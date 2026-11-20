import pandas as pd

import requests

url = "https://www150.statcan.gc.ca/t1/wds/rest/getFullTableDownloadCSV/18100004/en"

response = requests.get(url)
response.raise_for_status()

download_url = response.json()["object"]

print(download_url)


folder = "data/18100004-eng/"

cpi_data = pd.read_csv(
    folder + "18100004.csv",
    usecols=[
        "REF_DATE",
        "GEO",
        "Products and product groups",
        "VALUE"
    ]
)

cpi_canada = cpi_data[
    (cpi_data["GEO"] == "Canada") &
    (cpi_data["Products and product groups"] == "All-items")
].copy()

cpi_canada = cpi_canada[
    ["REF_DATE", "VALUE"]
]

cpi_canada = cpi_canada.rename(columns={
    "REF_DATE": "Date",
    "VALUE": "CPI"
})

cpi_canada["Date"] = pd.to_datetime(
    cpi_canada["Date"],
    format="%Y-%m"
)

cpi_canada = cpi_canada.sort_values("Date").reset_index(drop=True)

cpi_canada["Inflation_YoY"] = (
    cpi_canada["CPI"].pct_change(periods=12) * 100
)

print(cpi_canada.shape)

print(cpi_canada.head(15))

print(cpi_canada.tail(15))

print(cpi_canada.isnull().sum())

print("Duplicates:", cpi_canada["Date"].duplicated().sum())

print(cpi_canada.describe())


cpi_canada.to_csv(
    "canada_cpi_monthly.csv",
    index=False
)