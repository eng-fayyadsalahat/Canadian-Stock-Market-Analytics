## Target Variable Creation

A target variable named Future_Return_5D was created to represent the percentage return of each stock over the next five trading observations. The objective is to provide the machine learning models with a measurable future outcome that can be predicted using historical stock and economic information.

The target was calculated separately for each ticker using the adjusted closing price (Adj Close).

**Formula:**

Future_Return_5D = ((Adj Close(t+5) / Adj Close(t)) - 1) × 100

The calculation uses groupby("Ticker") to ensure that future prices are taken from the same stock rather than from another ticker.

Adjusted closing prices were selected because they account for historical dividends and stock splits, making them suitable for measuring historical total-return performance.

### Target Statistics

| Statistic                 | Value      |
| ------------------------- | ---------- |
| Total observations        | 63,574     |
| Valid target observations | 63,524     |
| Missing target values     | 50         |
| Mean                      | 0.3621%    |
| Standard deviation        | 4.2383%    |
| Minimum                   | \-47.0135% |
| 25th Percentile           | \-1.6666%  |
| Median                    | 0.3736%    |
| 75th Percentile           | 2.3148%    |
| Maximum                   | 43.2821%   |

### Missing Values

The target contains 50 missing values, corresponding to the final five observations of each of the ten stocks.

These values are expected because there are no subsequent five trading observations available to calculate future returns.

They should not be filled with zero because doing so would incorrectly imply that the stock experienced no price change.

### Mathematical Validation

To verify the target calculation, the future date and future adjusted closing price were independently generated using a separate five-observation shift.

The resulting forward returns were compared with the original Future_Return_5D values.

The maximum absolute difference between both calculations was **0.0**, confirming that the target was calculated correctly.

### Extreme Target Values

The target includes substantial positive and negative returns, particularly during periods of market volatility.

For example:

- The highest observed five-day return was approximately +43.28% for SU.TO in November 2008.
- The lowest observed five-day return was approximately -47.01% for CNQ.TO in March 2020.

These observations were investigated as part of the outlier analysis. They were retained because there was not sufficient evidence to classify them as data errors.

### Important Modeling Considerations

Future_Return_5D is the target variable and must not be included among the model input features.

The final five observations per ticker should be excluded from supervised model training because their target values are unavailable.

Additionally, chronological data splitting and an appropriate five-observation purge or embargo should be considered to reduce information leakage between training, validation, and test periods.

**Conclusion:**

The Future_Return_5D target was successfully created and mathematically validated. It provides a consistent measure of five-observation forward stock returns and establishes the prediction objective for the subsequent machine learning stage.

## Target Creation – Summary

A target variable named Future_Return_5D was created to measure each stock's percentage return over the next five trading observations.

The target was calculated using adjusted closing prices and grouped by ticker to prevent mixing observations between different stocks.

**Key Results:**

- Total observations: 63,574.
- Valid target values: 63,524.
- Missing values: 50, corresponding to the final five observations of each stock.
- Mean return: 0.3621%.
- Standard deviation: 4.2383%.
- Minimum return: -47.0135%.
- Maximum return: +43.2821%.

The calculation was independently validated, producing a maximum absolute difference of **0.0**.

The missing target values were retained because future observations are unavailable. Extreme returns were also retained following the initial outlier investigation.

**Final Outcome:** The five-observation forward return target was successfully created and validated for subsequent machine learning modeling.