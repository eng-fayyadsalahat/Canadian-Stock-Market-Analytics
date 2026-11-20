
import pandas as pd
import numpy as np


import yfinance as yf


import time
from datetime import date

tickers = [
    "RY.TO",    # Banking
    "TD.TO",    # Banking
    "SHOP.TO",  # Technology
    "ENB.TO",   # Energy / Pipeline
    "CNR.TO",   # Transportation
    "BMO.TO",   # Banking
    "CNQ.TO",   # Energy
    "SU.TO",    # Energy
    "BN.TO",    # Financial Services
    "ABX.TO"    # Mining
]

all_stocks = []

for ticker in tickers:

    print(f"Downloading {ticker}...")

    df = yf.download(
        ticker,
        start="2000-01-01",
        interval="1d",
        auto_adjust=False,
        actions=True,
        progress=False
    )

    if df.empty:
        print(f"No data found for {ticker}")
        continue

    # Handle MultiIndex columns if returned
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    df = df.reset_index()
    df["Ticker"] = ticker

    all_stocks.append(df)

# Combine all stocks
stocks = pd.concat(all_stocks, ignore_index=True)

# Organize columns
stocks = stocks[
    [
        "Date",
        "Ticker",
        "Open",
        "High",
        "Low",
        "Close",
        "Adj Close",
        "Volume",
        "Dividends",
        "Stock Splits"
    ]
]

stocks = stocks.sort_values(
    ["Ticker", "Date"]
).reset_index(drop=True)

print("Shape:", stocks.shape)
print(stocks.head())

stocks.to_csv("canada_stocks_daily.csv", index=False)




