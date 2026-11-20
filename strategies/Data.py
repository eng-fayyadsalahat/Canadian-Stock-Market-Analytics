import pandas as pd
import numpy as np


from pathlib import Path

pd.set_option("display.max_rows", None)




DATA_DIR = "data/processed/"
daily_data = pd.read_csv(
    DATA_DIR + "canada_integrated_daily_macro_features_final.csv",
    parse_dates=[
        "Date",
        "Bank_Availability_Date",
        "Macro_Reference_Date",
        "Macro_Availability_Date"
    ]
)

daily_data = daily_data.sort_values(
    ["Ticker", "Date"]
).reset_index(drop=True)


RAW = [
    "Open", "High", "Low", "Close",
    "Adj Close", "Volume",
    "Dividends", "Stock Splits"
]


META = [
    "Date",
    "Ticker",
    "Bank_Availability_Date",
    "Macro_Reference_Date",
    "Macro_Availability_Date",
    "Macro_Feature_Availability_Date"
]


# Economic indicators
ECONOMIC = [
    "Policy_Rate",
    "Bond_Yield_10Y",
    "USD_CAD",
    "CPI",
    "Inflation_YoY",
    "GDP_Real_Millions_CAD",
    "GDP_MoM",
    "GDP_YoY",
    "Employment",
    "Labour_Force",
    "Participation_Rate",
    "Unemployment_Rate",
    "BCPI_Total",
    "BCPI_NonEnergy",
    "BCPI_Energy",
    "BCPI_Metals",
    "BCPI_Forestry",
    "BCPI_Agriculture",
    "BCPI_Fish",
    "BCPI_Change_12M",
    "BCPI_Energy_Change_12M",
    "BCPI_Metals_Change_12M",
    "Unemployment_Change_12M",
    "Employment_Growth_12M",
    "Yield_Spread",
    "Policy_Rate_Change_21D",
    "USD_CAD_Change_21D"
]


# Cyclical calendar features
CALENDAR = [
    "DayOfWeek_Sin",
    "DayOfWeek_Cos",
    "Month_Sin",
    "Month_Cos"
]


# Technical indicators
TECHNICAL = [
    "Close_Daily_Return",
    "Close_Return_Lag_1",
    "Close_Return_Lag_5",
    "Close_Return_Lag_10",
    "Close_Return_Lag_20",
    "Close_Volatility_5D",
    "Close_Volatility_10D",
    "Close_Volatility_20D",
    "Close_MA_Ratio_5",
    "Close_MA_Ratio_10",
    "Close_MA_Ratio_20",
    "Close_MA_Ratio_50",
    "Close_Momentum_5D",
    "Close_Momentum_10D",
    "Close_Momentum_20D",
    "Close_RSI_14",
    "MACD_Pct",
    "MACD_Signal_Pct",
    "MACD_Histogram_Pct"
]


# Categorical features to be one-hot encoded
DUMMIES = [
    "Ticker"
]


BANK = [
    "Policy_Rate",
    "Bond_Yield_10Y",
    "USD_CAD",
    "Yield_Spread",
    "Policy_Rate_Change_21D",
    "USD_CAD_Change_21D"
]



TO_PREDICT = "Future_Return_5D"


# Modeling Features
NUMERIC = TECHNICAL + ECONOMIC + CALENDAR
FEATURES = NUMERIC + DUMMIES

daily_data["Future_Outperformance_5D"] = (
    daily_data["Future_Return_5D"]
    >
    daily_data.groupby("Date")["Future_Return_5D"]
    .transform("median")
).astype("float")

daily_data.loc[
    daily_data["Future_Return_5D"].isna(),
    "Future_Outperformance_5D"
] = float("nan")



market_dataset = pd.read_csv(
    "data/processed/canada_market_regime_dataset.csv",
    parse_dates=["Date"]
)

tsx_data = pd.read_csv(
    "data/raw/canada_tsx_composite.csv",
    parse_dates=["Date"]
)


def load_all_data():

    DATA_DIR = Path("data/processed")
    RAW_DIR = Path("data/raw")

    daily_data = pd.read_csv(
        DATA_DIR / "canada_integrated_daily_macro_features_demo3.csv",
        parse_dates=[
            "Date",
            "Bank_Availability_Date",
            "Macro_Reference_Date",
            "Macro_Availability_Date"
        ]
    )

    daily_data = (
        daily_data
        .sort_values(["Ticker", "Date"])
        .reset_index(drop=True)
    )

    # Feature groups
    RAW = [
        "Open", "High", "Low", "Close",
        "Adj Close", "Volume",
        "Dividends", "Stock Splits"
    ]

    META = [
        "Date",
        "Ticker",
        "Bank_Availability_Date",
        "Macro_Reference_Date",
        "Macro_Availability_Date",
        "Macro_Feature_Availability_Date"
    ]

    ECONOMIC = [
        "Policy_Rate", "Bond_Yield_10Y", "USD_CAD",
        "CPI", "Inflation_YoY", "GDP_Real_Millions_CAD",
        "GDP_MoM", "GDP_YoY", "Employment", "Labour_Force",
        "Participation_Rate", "Unemployment_Rate",
        "BCPI_Total", "BCPI_NonEnergy", "BCPI_Energy",
        "BCPI_Metals", "BCPI_Forestry", "BCPI_Agriculture",
        "BCPI_Fish", "BCPI_Change_12M",
        "BCPI_Energy_Change_12M", "BCPI_Metals_Change_12M",
        "Unemployment_Change_12M", "Employment_Growth_12M",
        "Yield_Spread", "Policy_Rate_Change_21D",
        "USD_CAD_Change_21D"
    ]

    CALENDAR = [
        "DayOfWeek_Sin", "DayOfWeek_Cos",
        "Month_Sin", "Month_Cos"
    ]

    TECHNICAL = [
        "Close_Daily_Return", "Close_Return_Lag_1",
        "Close_Return_Lag_5", "Close_Return_Lag_10",
        "Close_Return_Lag_20", "Close_Volatility_5D",
        "Close_Volatility_10D", "Close_Volatility_20D",
        "Close_MA_Ratio_5", "Close_MA_Ratio_10",
        "Close_MA_Ratio_20", "Close_MA_Ratio_50",
        "Close_Momentum_5D", "Close_Momentum_10D",
        "Close_Momentum_20D", "Close_RSI_14",
        "MACD_Pct", "MACD_Signal_Pct",
        "MACD_Histogram_Pct"
    ]

    DUMMIES = ["Ticker"]

    BANK = [
        "Policy_Rate", "Bond_Yield_10Y", "USD_CAD",
        "Yield_Spread", "Policy_Rate_Change_21D",
        "USD_CAD_Change_21D"
    ]

    NUMERIC = TECHNICAL + ECONOMIC + CALENDAR
    FEATURES = NUMERIC + DUMMIES

    # Stock prediction target
    daily_data["Future_Outperformance_5D"] = (
        daily_data["Future_Return_5D"]
        > daily_data.groupby("Date")["Future_Return_5D"].transform("median")
    ).astype(float)

    daily_data.loc[
        daily_data["Future_Return_5D"].isna(),
        "Future_Outperformance_5D"
    ] = float("nan")

    # Market regime dataset
    market_dataset = pd.read_csv(
        DATA_DIR / "canada_market_regime_dataset.csv",
        parse_dates=["Date"]
    )

    # TSX benchmark data
    tsx_data = pd.read_csv(
        RAW_DIR / "canada_tsx_composite.csv",
        parse_dates=["Date"]
    )

    return {
        "daily_data": daily_data,
        "market_dataset": market_dataset,
        "tsx_data": tsx_data,
        "features": FEATURES,
        "numeric_features": NUMERIC,
        "categorical_features": DUMMIES,
        "economic_features": ECONOMIC,
        "technical_features": TECHNICAL,
        "bank_features": BANK,
        "raw_columns": RAW,
        "meta_columns": META
    }
