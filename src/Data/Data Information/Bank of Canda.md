# Bank of Canada – Data Collection and Preprocessing

## 1. Overview

As part of the Canadian Stock Market Analytics project, historical financial and economic indicators were collected from the Bank of Canada through its Valet API.

The purpose of this data collection was to obtain macroeconomic and financial variables that could provide additional context for analyzing Canadian stock market movements and developing machine learning models to predict future stock returns.

Three indicators were selected based on their relevance to monetary policy, bond markets, and foreign exchange movements.

## 2. Data Sources and Selected Indicators

The following indicators were retrieved:

| Indicator                     | Series Code        | Frequency      | Unit        |
| ----------------------------- | ------------------ | -------------- | ----------- |
| Policy Rate                   | V39079             | Business Daily | Percent     |
| 10-Year Government Bond Yield | BD.CDN.10YR.DQ.YLD | Business Daily | Percent     |
| USD/CAD Exchange Rate         | FXUSDCAD           | Daily          | CAD per USD |

### 2.1 Policy Rate

The target for the overnight interest rate represents the Bank of Canada's monetary policy rate.

It provides information about the central bank's monetary policy stance and can help capture changes in borrowing costs and broader financial conditions.

- Series Code: V39079
- Observations: 4,564
- Start Date: April 21, 2009
- End Date: November 5, 2026
- Mean: 1.503%
- Minimum: 0.25%
- Maximum: 5.00%

### 2.2 10-Year Government Bond Yield

This indicator represents the benchmark yield on Government of Canada 10-year bonds.

It provides information about long-term interest rate conditions and government bond market movements.

- Series Code: BD.CDN.10YR.DQ.YLD
- Observations: 6,463
- Start Date: January 2, 2001
- End Date: November 5, 2026
- Mean: 3.027%
- Minimum: 0.43%
- Maximum: 5.99%

### 2.3 USD/CAD Exchange Rate

This indicator represents the daily average exchange rate of the US dollar expressed in Canadian dollars.

It provides information about exchange rate movements and the relative value of the Canadian dollar against the US dollar.

A higher USD/CAD value generally indicates a stronger US dollar relative to the Canadian dollar.

- Series Code: FXUSDCAD
- Observations: 2,457
- Start Date: January 3, 2017
- End Date: November 6, 2026
- Mean: 1.3315
- Minimum: 1.204
- Maximum: 1.4603

## 3. Data Extraction

Historical observations were retrieved using the Bank of Canada's Valet API.

The extraction process included:

- Sending HTTP GET requests to the API.
- Retrieving historical observations for each selected series.
- Extracting observation dates and corresponding values.
- Converting dates into Pandas datetime format.
- Converting indicator values into numeric data types.
- Removing observations with unavailable values within the individual API responses.
- Creating separate DataFrames for each indicator.

The extraction process was completed successfully without requiring an API key.

## 4. Data Integration

The three individual datasets were combined using an outer join on the Date column.

An outer join was selected to preserve all available observations across the three indicators, even when their historical coverage periods differed.

The resulting dataset contains:

| Attribute       | Result                                     |
| --------------- | ------------------------------------------ |
| Total Rows      | 6,650                                      |
| Total Columns   | 4                                          |
| Columns         | Date, Policy_Rate, Bond_Yield_10Y, USD_CAD |
| Start Date      | 2001-01-02                                 |
| End Date        | 2026-11-06                                 |
| Duplicate Dates | 0                                          |
| Memory Usage    | Approximately 207.9 KB                     |

The final dataset contains 13,484 individual observations across the three source series before integration.

## 5. Missing Value Analysis

Missing values were examined at two levels:

1. Missing values across the complete combined dataset.
2. Missing values within each indicator's actual historical coverage period.

### 5.1 Overall Missing Values

| Column         | Missing Values | Missing Percentage |
| -------------- | -------------- | ------------------ |
| Policy_Rate    | 2,086          | 31.37%             |
| Bond_Yield_10Y | 187            | 2.81%              |
| USD_CAD        | 4,193          | 63.05%             |

The relatively high overall missing percentages for Policy Rate and USD/CAD are largely explained by their later historical starting dates.

### 5.2 Missing Values Within Historical Coverage

| Indicator      | Missing Observations Within Coverage |
| -------------- | ------------------------------------ |
| Policy_Rate    | 2                                    |
| Bond_Yield_10Y | 186                                  |
| USD_CAD        | 100                                  |

Several missing dates correspond to Canadian public holidays and financial market closures, particularly in the bond yield and exchange rate series.

However, not every missing observation was independently verified, so further investigation may be necessary if these dates become relevant during data integration.

## 6. Data Quality Checks

Several validation procedures were performed:

- Confirmed that the Date column contains valid datetime values.
- Confirmed that the three indicators contain numeric values.
- Checked the overall date range.
- Verified that there are no duplicate dates.
- Examined the number of available observations for each indicator.
- Calculated descriptive statistics.
- Investigated missing dates within each indicator's historical coverage.

The dataset was retained without applying global missing-value removal or imputation.

This decision preserves the original observations and avoids introducing assumptions before the stock market data is integrated.

## 7. Data Preparation Considerations

The three indicators have different historical coverage periods.

The common historical period across all three indicators begins on January 3, 2017, and extends through November 5, 2026.

Future integration with Canadian stock market data will require:

- Aligning observations with actual stock trading dates.
- Considering differences between business-day and trading-day calendars.
- Evaluating forward filling for suitable indicators.
- Avoiding backward filling and other forms of future-information leakage.
- Accounting for the actual publication dates of economic indicators when incorporating them into predictive models.

These considerations are important to ensure that the machine learning models only use information that would have been available at the time of prediction.

## 8. Output Dataset

The final integrated dataset was prepared for export as:

canada_bank_of_canada_daily.csv

It contains the date column and the three selected financial and economic indicators.

## 9. Conclusion

The Bank of Canada data collection and initial preprocessing stage was successfully completed.

Three relevant financial and economic indicators were retrieved, validated, and integrated into a single daily dataset containing 6,650 unique dates.

The resulting dataset provides historical monetary policy, long-term bond yield, and foreign exchange information that can later be integrated with Canadian stock market data.

No final missing-value imputation or stock-market integration has been performed at this stage.

### Bank of Canada – Data Collection Summary

Collected historical financial and economic data from the Bank of Canada's Valet API for the Canadian Stock Market Analytics project.

Three indicators were selected:

- **Policy Rate (V39079):** 4,564 observations, covering April 2009 to November 2026.
- **10-Year Government Bond Yield (BD.CDN.10YR.DQ.YLD):** 6,463 observations, covering January 2001 to November 2026.
- **USD/CAD Exchange Rate (FXUSDCAD):** 2,457 observations, covering January 2017 to November 2026.

The three datasets were integrated using an outer join on the date column, producing a unified dataset containing 6,650 rows and four columns.

Data preprocessing included date conversion, numeric type conversion, sorting, duplicate checks, missing-value analysis, and descriptive statistical analysis.

No duplicate dates were found. Missing values were retained to preserve the original observations, with most gaps associated with different historical coverage periods and non-trading days.

**Output:** canada_bank_of_canada_daily.csv

**Status:** Data collection, integration, and initial quality assessment completed. The dataset is ready for subsequent alignment with Canadian stock market data.