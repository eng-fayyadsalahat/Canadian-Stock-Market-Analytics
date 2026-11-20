from pathlib import Path

import pandas as pd
import requests


url = "https://www150.statcan.gc.ca/t1/wds/rest/getFullTableDownloadCSV/14100287/en"

response = requests.get(url)
response.raise_for_status()

download_url = response.json()["object"]

print(download_url)




folder = "data/14100287-eng/"

files = [
    "14100287.csv",
    "14100287_MetaData.csv"
]


for filename in files:
    path = Path(folder + filename)
    print(path)
    print(f"\nFile: {filename}")
    print(f"Size: {path.stat().st_size / (1024**2):.2f} MB")








metadata = pd.read_csv(folder + "14100287_MetaData.csv")

print(metadata.shape)
print(metadata.columns.tolist())
print(metadata.head(20))


for i, row in metadata.iterrows():
    if row.iloc[0] == "Dimension ID":
        print("\n", row.tolist())

    elif pd.notna(row.iloc[0]) and str(row.iloc[0]).isdigit():
        if int(row.iloc[0]) in [2, 5]:
            print(row.tolist())


pd.set_option("display.max_rows", 100)
pd.set_option("display.max_columns", None)

print(metadata)


folder = "data/14100287-eng/"

file_path = "14100287.csv"

file_path = folder + "14100287.csv"

usecols = [
    'REF_DATE',
    'GEO',
    'Labour force characteristics',
    'Gender',
    'Age group',
    'Statistics',
    'Data type',
    'UOM',
    'SCALAR_FACTOR',
    'VALUE'
]

indicators = [
    'Employment',
    'Unemployment rate',
    'Labour force',
    'Participation rate'
]

filtered_chunks = []

for chunk in pd.read_csv(
    file_path,
    usecols=usecols,
    chunksize=200_000
):

    filtered = chunk[
        (chunk['GEO'] == 'Canada') &
        (chunk['Gender'] == 'Total - Gender') &
        (chunk['Age group'] == '15 years and over') &
        (chunk['Statistics'] == 'Estimate') &
        (chunk['Data type'] == 'Seasonally adjusted') &
        (chunk['Labour force characteristics'].isin(indicators))
    ]

    filtered_chunks.append(filtered)

    print(f"Processed chunk: {len(chunk):,} rows")

# Combine filtered data
labour_data = pd.concat(filtered_chunks, ignore_index=True)

print("Filtered shape:", labour_data.shape)

print(labour_data.head())

labour_monthly = labour_data.pivot_table(
    index='REF_DATE',
    columns='Labour force characteristics',
    values='VALUE',
    aggfunc='first'
).reset_index()

labour_monthly.columns.name = None

labour_monthly = labour_monthly.rename(columns={
    'REF_DATE': 'Date'
})

labour_monthly['Date'] = pd.to_datetime(
    labour_monthly['Date'] + '-01'
)

labour_monthly = labour_monthly.sort_values('Date')

print(labour_monthly.head())


print(labour_monthly.info())

print("\nMissing values:")
print(labour_monthly.isna().sum())

print("\nDate range:")
print(labour_monthly['Date'].min())
print(labour_monthly['Date'].max())

print("\nDuplicate dates:")
print(labour_monthly['Date'].duplicated().sum())





# Descriptive statistics
print(labour_monthly.describe().T)

# Check value ranges
print("Minimum values:")
print(labour_monthly.min(numeric_only=True))

print("\nMaximum values:")
print(labour_monthly.max(numeric_only=True))

# Check chronological order
print(
    "Chronologically sorted:",
    labour_monthly['Date'].is_monotonic_increasing
)




labour_monthly.to_csv(
    'canada_labour_market_monthly.csv',
    index=False
)