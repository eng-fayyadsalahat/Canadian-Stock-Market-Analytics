## Monthly-to-Daily Feature Integration

The engineered monthly macroeconomic features were integrated into the daily stock market dataset to provide additional economic context for each stock observation.

The monthly engineered dataset, canada_macro_monthly_features.csv, contained **1,354 records and 23 columns**, including the original macroeconomic indicators and five newly engineered features:

**Commodity Market Features:**

- BCPI_Change_12M: 12-month percentage change in the total Bank of Canada Commodity Price Index.
- BCPI_Energy_Change_12M: 12-month percentage change in the energy commodity index.
- BCPI_Metals_Change_12M: 12-month percentage change in the metals commodity index.

**Labour Market Features:**

- Unemployment_Change_12M: Change in the unemployment rate over 12 months, measured in percentage points.
- Employment_Growth_12M: 12-month percentage growth in employment.

### Integration Methodology

Since macroeconomic indicators are published monthly while stock prices are recorded daily, a time-aware integration approach was required.

The merge_asof() function was used with:

- direction="backward" to select the latest available observation.
- A separate macro feature availability date.
- A temporary three-month availability lag applied to the monthly reference date.

This approach ensured that each daily stock observation was matched with the latest macroeconomic feature whose assumed availability date was not later than the stock observation date.

The integration was performed using the availability date rather than the original monthly reference date to reduce the risk of look-ahead bias.

### Integration Results

The resulting daily dataset contained:

| Metric                         | Result |
| ------------------------------ | ------ |
| Records                        | 63,574 |
| Total Columns                  | 45     |
| Newly Integrated Features      | 5      |
| Missing Values in New Features | 0      |
| Duplicate Date-Ticker Records  | 0      |
| Availability Date Mismatches   | 0      |

A final availability-date audit confirmed that Macro_Feature_Availability_Date matched the existing Macro_Availability_Date for every record.

The resulting dataset successfully combined daily stock market information with engineered monthly economic features while preserving its original number of observations.

### Methodological Limitation

The three-month availability lag is a temporary modeling assumption rather than a verified publication schedule for each economic indicator. Actual release dates should be investigated before final model evaluation and historical backtesting.

The integrated dataset was preserved separately as canada_integrated_daily_macro_features.csv, keeping the original integrated dataset unchanged.

## Monthly-to-Daily Feature Integration

Five engineered monthly macroeconomic features covering commodity price changes and labour market trends were integrated into the daily stock dataset using merge_asof() with backward matching and a temporary three-month availability lag. The resulting dataset contained **63,574 records and 45 columns**, with no missing values in the newly integrated features and no duplicate Date-Ticker records. An availability-date audit confirmed zero mismatches with the original macroeconomic integration. The three-month lag remains a provisional assumption pending verification of actual publication dates.