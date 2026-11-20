from pathlib import Path

import pandas as pd


import requests

url = "https://www150.statcan.gc.ca/t1/wds/rest/getFullTableDownloadCSV/36100434/en"

response = requests.get(url)
response.raise_for_status()

download_url = response.json()["object"]

print(download_url)




folder = "data/36100434-eng"

files = [
    "36100434_MetaData.csv",
    "36100434.csv"
]


for filename in files:
    path = Path(folder + filename)
    print(path)
    print(f"\nFile: {filename}")
    print(f"Size: {path.stat().st_size / (1024**2):.2f} MB")


metadata = pd.read_csv(folder + "36100434_MetaData.csv")

print(metadata.shape)
print(metadata.columns.tolist())
print(metadata.head(20))



gdp = pd.read_csv(folder + "36100434.csv",
    encoding="utf-8-sig",
    low_memory=False,)

gdp_canada = gdp[
    (gdp["GEO"] == "Canada") &
    (gdp["Seasonal adjustment"] == "Seasonally adjusted at annual rates") &
    (gdp["Prices"] == "Chained (2017) dollars") &
    (gdp["North American Industry Classification System (NAICS)"] == "All industries [T001]")
].copy()

gdp_canada = gdp_canada[
    ["REF_DATE", "VALUE"]
].copy()

gdp_canada = gdp_canada.rename(columns={
    "REF_DATE": "Date",
    "VALUE": "GDP_Real_Millions_CAD"
})

gdp_canada["Date"] = pd.to_datetime(gdp_canada["Date"])

gdp_canada = gdp_canada.sort_values("Date").reset_index(drop=True)


print("Shape:", gdp_canada.shape)

print("\nDate range:")
print(gdp_canada["Date"].min(), gdp_canada["Date"].max())

print("\nMissing values:")
print(gdp_canada.isnull().sum())

print("\nDuplicate dates:")
print(gdp_canada["Date"].duplicated().sum())

print("\nDescriptive statistics:")
print(gdp_canada.describe())

print("\nFirst rows:")
print(gdp_canada.head())

print("\nLast rows:")
print(gdp_canada.tail())

gdp_canada["GDP_MoM"] = (
    gdp_canada["GDP_Real_Millions_CAD"].pct_change() * 100
)

gdp_canada["GDP_YoY"] = (
    gdp_canada["GDP_Real_Millions_CAD"].pct_change(12) * 100
)

gdp_canada.to_csv(
    "canada_gdp_monthly.csv",
    index=False
)