# Canadian Stock Market Data Collection and Quality Assessment

## 1. Data Collection

Historical daily stock market data was collected using the Python yfinance library from Yahoo Finance.

Ten Canadian stocks listed on the Toronto Stock Exchange (TSX) were selected to represent different economic sectors:

| Ticker  | Company / Sector   |
| ------- | ------------------ |
| ABX.TO  | Mining             |
| BMO.TO  | Banking            |
| BN.TO   | Financial Services |
| CNQ.TO  | Energy             |
| CNR.TO  | Transportation     |
| ENB.TO  | Energy / Pipelines |
| RY.TO   | Banking            |
| SHOP.TO | Technology         |
| SU.TO   | Energy             |
| TD.TO   | Banking            |

The data was downloaded using:

- Start date: January 1, 2000.
- Interval: Daily.
- Auto-adjust: False.
- Corporate actions: Included.

The following fields were retained:

Date, Ticker, Open, High, Low, Close, Adj Close, Volume, Dividends, and Stock Splits.

The dataset was converted into a long-format structure, with each row representing one stock on one trading date.

## 2. Dataset Overview

After combining the data for all ten stocks, the resulting dataset contained:

| Metric                           | Result           |
| -------------------------------- | ---------------- |
| Total records                    | 63,575 initially |
| Records after cleaning           | 63,574           |
| Number of stocks                 | 10               |
| Number of columns                | 10               |
| Earliest date                    | January 4, 2000  |
| Latest date                      | November 6, 2026 |
| Missing values                   | 0                |
| Duplicate (Date, Ticker) records | 0                |

Nine stocks have historical data beginning on January 4, 2000.

SHOP.TO has a shorter history, beginning on May 21, 2015, which is consistent with its later market listing.

The original historical coverage was retained rather than removing stocks or restricting the dataset to a common starting date.

## 3. Data Quality Assessment

Several validation checks were performed to assess the reliability and consistency of the downloaded data.

### 3.1 Invalid Prices

The dataset initially contained one record with zero values across all price fields:

- Ticker: ENB.TO
- Date: May 19, 2003
- Open, High, Low, Close, and Adj Close: 0
- Volume: 0

This record was removed because it did not represent a valid trading price.

After removal:

- Invalid price records: 0.
- Total records: 63,574.

### 3.2 OHLC Consistency

The following logical relationships were checked:

- High must be greater than or equal to Low.
- High must be greater than or equal to Open and Close.
- Low must be less than or equal to Open and Close.

Result: Zero invalid OHLC records.

### 3.3 Trading Volume

The volume validation produced the following results:

| Check                               | Result |
| ----------------------------------- | ------ |
| Zero-volume records before cleaning | 5      |
| Zero-volume records after cleaning  | 4      |
| Negative-volume records             | 0      |

The remaining four zero-volume records were retained temporarily rather than automatically removed, since their causes require further investigation.

## 4. Stock-Level Descriptive Analysis

A summary was generated for each stock, including its number of observations, historical coverage, minimum and maximum closing prices, average closing price, average trading volume, and zero-volume records.

Key observations:

- Nine stocks have 6,744 records each.
- SHOP.TO has 2,878 records.
- All stocks have data through November 6, 2026.
- SHOP.TO has the shortest historical coverage.
- CNQ.TO has the highest average trading volume among the selected stocks, at approximately 9.11 million shares.
- CNQ.TO also has one of the higher average closing-price volatility profiles when examined through daily returns.

The closing-price ranges differ substantially across companies, reflecting differences in share prices, corporate histories, and business sectors.

## 5. Daily Return Calculation

Daily percentage returns were calculated separately for each ticker using the adjusted closing price:

Daily Return (%) = (Adj Close\[t\] / Adj Close\[t-1\] - 1) × 100

The calculation was grouped by ticker to prevent returns from being calculated across different stocks.

This produced 6,743 daily-return observations for each stock with a full historical period and 2,877 for SHOP.TO.

The first observation for each stock naturally has no previous trading-day price and therefore produces a missing return.

### 5.1 Daily Return Statistics

| Ticker  | Mean (%) | Std (%) | Minimum (%) | Median (%) | Maximum (%) |
| ------- | -------- | ------- | ----------- | ---------- | ----------- |
| ABX.TO  | 0.049    | 2.525   | \-16.394    | 0.000      | 32.463      |
| BMO.TO  | 0.061    | 1.397   | \-16.413    | 0.072      | 16.975      |
| BN.TO   | 0.079    | 1.751   | \-13.976    | 0.066      | 16.788      |
| CNQ.TO  | 0.090    | 2.391   | \-29.180    | 0.086      | 22.612      |
| CNR.TO  | 0.068    | 1.496   | \-11.116    | 0.083      | 10.544      |
| ENB.TO  | 0.060    | 1.382   | \-16.504    | 0.067      | 20.686      |
| RY.TO   | 0.066    | 1.329   | \-13.450    | 0.079      | 14.896      |
| SHOP.TO | 0.213    | 3.649   | \-19.628    | 0.207      | 24.048      |
| SU.TO   | 0.072    | 2.254   | \-20.656    | 0.060      | 24.673      |
| TD.TO   | 0.057    | 1.372   | \-12.738    | 0.087      | 17.882      |

SHOP.TO recorded the highest mean daily return and standard deviation in this sample. Banking stocks generally exhibited lower daily-return standard deviations than the selected energy and mining stocks.

These are historical descriptive statistics and should not be interpreted as forecasts of future performance.

## 6. Outlier Detection

Daily returns were examined to identify unusually large positive and negative movements.

Examples included:

| Ticker  | Date       | Daily Return (%) |
| ------- | ---------- | ---------------- |
| ABX.TO  | 2008-11-21 | 32.463           |
| CNQ.TO  | 2020-03-09 | \-29.180         |
| CNQ.TO  | 2020-03-16 | \-27.254         |
| CNQ.TO  | 2008-11-20 | \-21.511         |
| SU.TO   | 2020-03-12 | \-20.656         |
| ENB.TO  | 2020-03-13 | 20.686           |
| SHOP.TO | 2015-09-17 | 24.048           |

Several extreme movements occurred during historically volatile periods, including the 2008 financial crisis and the market disruption in March 2020.

These observations were retained because extreme returns can represent genuine market events. No automatic outlier removal or winsorization was applied.

The observations should remain subject to further verification before being used in model training.

## 7. Corporate Actions Assessment

The dataset includes two corporate-action fields:

- Dividends
- Stock Splits

### 7.1 Dividends

Dividend records were inspected, particularly for ABX.TO.

Examples included historical distributions between 2003 and 2008.

The difference between Close and Adj Close reflects historical price adjustments, including dividend adjustments.

### 7.2 Stock Splits

Multiple split events were identified across the selected companies.

Examples include:

- BMO.TO: 2.0
- CNQ.TO: 2.0
- CNR.TO: 2.0
- ENB.TO: 2.0
- RY.TO: 2.0
- SHOP.TO: 10.0
- SU.TO: 2.0
- BN.TO: Several recorded ratios, including 1.5, 1.033, and 1.237.

Price and adjusted-price observations surrounding the recorded events were inspected.

The examined events did not show obvious split-related price discontinuities in the calculated adjusted daily returns.

The original corporate-action records were retained. Unusual recorded ratios, particularly for BN.TO, may require additional verification.

## 8. Data Preparation Decisions

The following decisions were made:

1. Removed the single record containing zero prices.
2. Retained the four remaining zero-volume records for further investigation.
3. Retained all valid OHLC observations.
4. Preserved historical data for all ten stocks.
5. Retained both Close and Adj Close.
6. Retained Dividends and Stock Splits for corporate-action analysis.
7. Calculated daily returns using Adj Close.
8. Retained extreme returns rather than automatically removing them.

## 9. Important Limitations and Future Considerations

Several considerations remain before the dataset can be used in a historical strategy simulation:

- The four remaining zero-volume records need further investigation.
- Extreme daily returns should be checked against historical market and corporate events.
- Historical adjusted prices may be revised retrospectively by the data provider.
- Adjusted prices are suitable for measuring historical total returns, but they are not necessarily executable historical transaction prices.
- Corporate-action records should not automatically be used as predictive features.
- The selected stocks may introduce survivorship bias because the sample consists of currently selected companies with available historical data.
- Different stocks have different historical coverage periods.

For a realistic historical simulation, adjusted returns can be used for return analysis, while execution assumptions should account for actual prices, transaction timing, dividends, splits, and other relevant costs.

## 10. Conclusion

The Canadian stock dataset was successfully collected, combined, and subjected to several data-quality and exploratory checks.

The final dataset contains 63,574 daily observations across ten TSX-listed stocks, covering January 2000 to November 2026, with different historical starting dates.

The initial invalid-price record was removed, OHLC consistency was verified, daily returns were calculated, extreme observations were examined, and corporate-action records were reviewed.

The dataset is now ready for the next preparation stage, subject to resolving the remaining zero-volume records and documenting the limitations described above.

The next major step is to integrate the stock dataset with the collected Canadian macroeconomic indicators while carefully accounting for different data frequencies, publication dates, and historical information availability to prevent look-ahead bias.

# Canadian Stock Market Data – Summary

Historical daily stock data was collected using the yfinance Python library for ten Canadian companies listed on the Toronto Stock Exchange (TSX), representing banking, financial services, energy, mining, transportation, and technology sectors.

The dataset initially contained 63,575 records and 10 columns, covering January 4, 2000, to November 6, 2026. After quality assessment, one invalid record containing zero prices was removed, leaving 63,574 records.

### Data Quality Assessment

- Missing values: 0.
- Duplicate (Date, Ticker) records: 0.
- Invalid prices after cleaning: 0.
- Invalid OHLC records: 0.
- Negative-volume records: 0.
- Remaining zero-volume records: 4.

Nine stocks have historical data beginning in January 2000, while SHOP.TO begins in May 2015.

### Daily Return Analysis

Daily percentage returns were calculated using Adj Close, grouped by ticker. The resulting dataset contains 6,743 return observations for each of the nine longer-history stocks and 2,877 for SHOP.TO.

SHOP.TO recorded the highest average daily return (0.213%) and standard deviation (3.649%) among the selected stocks.

Extreme returns were identified, including large movements during the 2008 financial crisis and March 2020 market disruption. These observations were retained rather than automatically removed.

### Corporate Actions

Dividend and stock-split records were inspected. Price behavior around selected split events was examined, with no obvious split-related discontinuities in the adjusted daily returns.

Both Dividends and Stock Splits were retained for future analysis.

### Final Status

The dataset has passed the main initial quality checks and is suitable for the next preparation stage, subject to further investigation of the four remaining zero-volume records and selected extreme returns.

The next step is to integrate the stock data with Canadian macroeconomic indicators, accounting for publication dates, different data frequencies, and look-ahead bias before developing predictive models and conducting historical strategy simulations.