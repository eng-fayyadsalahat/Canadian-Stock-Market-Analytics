## Feature Inventory & Missing Values Audit

An initial feature inventory and missing values audit was conducted on the integrated Canadian stock market dataset to assess its structure, identify available variables, and evaluate data completeness before proceeding with feature engineering.

The dataset contained **63,574 records and 39 columns**, covering 10 Canadian stocks over the period from January 4, 2000, to November 6, 2026.

The available variables were organized into the following categories:

- **Stock Market Data:** Open, High, Low, Close, Adjusted Close, Volume, Dividends, and Stock Splits.
- **Daily Economic Indicators:** Bank of Canada Policy Rate, 10-Year Bond Yield, and USD/CAD Exchange Rate.
- **Macroeconomic Indicators:** CPI, Inflation, GDP, Employment, Labour Force, Participation Rate, Unemployment Rate, and commodity price indices.
- **Calendar Features:** Day of Week, Month, Quarter, and their cyclical sine/cosine transformations.

The missing values audit identified the following:

| Feature                | Missing Values | Missing Percentage |
| ---------------------- | -------------- | ------------------ |
| USD_CAD                | 38,984         | 61.32%             |
| Policy_Rate            | 21,090         | 33.17%             |
| Bond_Yield_10Y         | 2,473          | 3.89%              |
| Bank_Availability_Date | 2,259          | 3.55%              |

Most missing values were associated with differences in historical coverage and observation frequency among the economic indicators, rather than errors in the stock market records.

The structural integrity checks also confirmed:

- No duplicate Date-Ticker combinations.
- No completely duplicated records.
- No missing values in the calendar features.
- Consistent date ordering within each ticker.

The audit established a baseline for subsequent feature engineering and highlighted the need to handle missing economic observations carefully without introducing artificial values or future information.

No missing values were removed or arbitrarily replaced at this stage.

## Feature Inventory & Missing Values Audit

The integrated dataset contained **63,574 records and 39 columns**, covering stock prices, daily economic indicators, monthly macroeconomic data, and calendar features. The missing values audit identified higher missingness in USD/CAD (61.32%) and the Policy Rate (33.17%), mainly due to differences in historical data coverage. No duplicate records or Date-Ticker combinations were found, and no missing values were detected in the calendar features. The dataset was preserved without arbitrary imputation or deletion.