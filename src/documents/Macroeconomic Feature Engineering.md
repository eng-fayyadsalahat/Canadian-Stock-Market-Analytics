# Macroeconomic Feature Engineering

## 1. Overview

In this stage, additional macroeconomic features were engineered from the previously integrated Canadian economic datasets. The objective was to capture changes in commodity prices, labour market conditions, interest rates, and currency exchange rates that may provide useful information for analyzing and predicting Canadian stock market movements.

Feature engineering was performed using the monthly macroeconomic dataset (monthly_data) and the integrated daily dataset (daily_data), depending on the frequency of each indicator.

## 2. Commodity Market Features

Three annual percentage-change features were created using the monthly Bank of Canada Commodity Price Index (BCPI):

- BCPI_Change_12M
- BCPI_Energy_Change_12M
- BCPI_Metals_Change_12M

These features measure the percentage change in the total commodity index, energy index, and metals index compared with the same month of the previous year.

**Key findings:**

- Total BCPI annual change averaged approximately 5.39%.
- Energy BCPI annual change averaged approximately 9.88%.
- Metals BCPI annual change averaged approximately 6.19%.
- In October 2026, the annual changes were approximately 21.39%, 41.09%, and 5.58%, respectively.

These features help represent changes in commodity market conditions, particularly those relevant to Canada's resource-oriented economy.

## 3. Labour Market Features

Two features were engineered from Statistics Canada's monthly Labour Force Survey data:

- Unemployment_Change_12M: Measures the difference in the unemployment rate compared with the same month one year earlier, expressed in percentage points.
- Employment_Growth_12M: Measures the annual percentage growth in employment.

**Key findings:**

- Average unemployment-rate change was approximately -0.01 percentage points.
- Average annual employment growth was approximately 1.59%.
- In October 2026, unemployment was 0.2 percentage points higher than the previous year, while employment growth was approximately 0.08%.

These features capture changes in employment conditions and labour market trends.

## 4. Interest Rate Features

Two features were created using daily Bank of Canada indicators:

- Yield_Spread: Calculated as the 10-year government bond yield minus the policy interest rate.
- Policy_Rate_Change_21D: Measures the change in the policy rate over 21 previous records.

**Key findings:**

- Average yield spread was approximately 0.80 percentage points.
- Average policy-rate change over 21 records was approximately 0.01 percentage points.
- The median policy-rate change was zero, reflecting the fact that policy rates generally remain unchanged between monetary policy decisions.

These features describe the relationship between short-term policy rates and long-term bond yields, as well as changes in monetary policy.

## 5. Currency Exchange Rate Feature

One feature was created using the daily USD/CAD exchange rate:

- USD_CAD_Change_21D: Measures the percentage change in the USD/CAD exchange rate over 21 previous records.

**Key findings:**

- Mean change: approximately 0.07%.
- Standard deviation: approximately 1.82%.
- Minimum: approximately -5.74%.
- Maximum: approximately 9.55%.

A positive value indicates an increase in USD/CAD, meaning the US dollar strengthened relative to the Canadian dollar. A negative value indicates the opposite.

This feature provides information about currency movements that may affect Canadian companies, particularly those exposed to international trade and foreign exchange fluctuations.

## 6. Missing Values and Data Considerations

Missing values were observed across several engineered features due to differences in historical data coverage, unavailable observations, and the lookback periods required for calculating changes.

The missing values were not automatically replaced with zeros or removed. This preserves the original information and avoids introducing artificial observations.

The current macroeconomic availability dates also use assumed publication lags. These are temporary approximations and must be verified against official release dates before final model evaluation to reduce the risk of look-ahead bias.

## 7. Conclusion

This stage produced eight additional macroeconomic features across four categories: commodities, labour market, interest rates, and currency exchange rates.

These features expand the dataset beyond individual stock-price indicators by incorporating broader economic conditions that may influence Canadian equity markets.

The next stage will focus on calendar-based features, followed by a comprehensive feature review, missing-value assessment, and preparation of the final modeling dataset.

# Macroeconomic Feature Engineering – Summary

Engineered eight additional macroeconomic features using monthly Statistics Canada data and daily Bank of Canada indicators.

- **Commodities:** Created 12-month percentage-change features for total BCPI, energy, and metals indices.
- **Labour Market:** Created annual unemployment-rate change and employment-growth features.
- **Interest Rates:** Calculated the 10-year bond yield spread over the policy rate and the 21-record policy-rate change.
- **Currency:** Created a 21-record percentage-change feature for the USD/CAD exchange rate.

These features capture changes in Canada's commodity markets, employment conditions, monetary policy, and currency movements.

Missing values were retained for further assessment rather than automatically filled or removed. Publication-date assumptions and potential look-ahead bias will also be reviewed before model training.

**Outcome:** Eight new macroeconomic features were engineered to complement the existing stock-market technical indicators.
