import pandas as pd

import requests

url = "https://www.bankofcanada.ca/valet/observations/group/BCPI_MONTHLY/csv?start_date=1972-01-01"

response = requests.get(url)
response.raise_for_status()


with open("BCPI_MONTHLY-sd-1972-01-01.csv", "wb") as file:
    file.write(response.content)





folder = "data/"
path = folder + "BCPI_MONTHLY-sd-1972-01-01.csv"

with open(path, encoding="utf-8-sig") as f:
    lines = f.readlines()

# ابحث عن سطر "OBSERVATIONS"
obs_idx = next(i for i, l in enumerate(lines) if l.strip().strip('"') == "OBSERVATIONS")

# الـ header هو السطر اللي بعد OBSERVATIONS مباشرة
header_idx = obs_idx + 1

bcpi_data = pd.read_csv(
    path,
    skiprows=header_idx,
    encoding="utf-8-sig",
    parse_dates=["date"],
)

print(f"Header line = {header_idx + 1}")     # لازم يطلع 21
print(bcpi_data.shape)
print(bcpi_data.columns.tolist())
print(bcpi_data.head())
print(bcpi_data.dtypes)

bcpi_data.to_csv("bcpi_monthly.csv")
