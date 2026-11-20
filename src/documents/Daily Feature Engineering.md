# Daily Feature Engineering

Daily feature engineering was performed to extract meaningful information from historical stock prices and transform raw market data into useful inputs for machine learning models.

The features were calculated separately for each stock ticker to ensure that historical observations from different companies were not mixed. The dataset contains ten Canadian stocks listed on the Toronto Stock Exchange (TSX).

### 1. Daily Returns

The Daily_Return feature measures the percentage change in a stock's adjusted closing price compared with its previous trading observation.

**Formula:**

Daily_Return = (Adj Close(t) / Adj Close(t-1) - 1) × 100

This feature captures short-term price movements and provides a basic measure of daily stock performance.

**Statistics:**

- Mean: 0.0733%
- Standard deviation: 1.9452%
- Minimum: -29.1804%
- Maximum: 32.4627%

The average daily return was slightly positive, while the relatively high standard deviation reflects variations in daily market movements.

### 2. Return Lag Features

Four lagged return features were created:

- Return_Lag_1
- Return_Lag_5
- Return_Lag_10
- Return_Lag_20

These features represent historical daily returns from 1, 5, 10, and 20 trading observations earlier.

They allow machine learning models to identify potential relationships between previous price movements and subsequent stock performance.

### 3. Rolling Volatility

Three rolling volatility features were calculated:

- Volatility_5D
- Volatility_10D
- Volatility_20D

These features measure the standard deviation of daily returns over the previous 5, 10, and 20 observations.

**Statistics:**

| Feature        | Mean   | Standard Deviation | Minimum | Maximum |
| -------------- | ------ | ------------------ | ------- | ------- |
| Volatility_5D  | 1.5264 | 1.2237             | 0.0426  | 16.5760 |
| Volatility_10D | 1.5928 | 1.1303             | 0.1645  | 14.8759 |
| Volatility_20D | 1.6316 | 1.0685             | 0.2376  | 13.9519 |

The results indicate that longer observation windows generally produced higher average volatility, while short windows captured more immediate fluctuations.

### 4. Moving Averages and Moving Average Ratios

Four moving averages were created:

- MA_5
- MA_10
- MA_20
- MA_50

These features represent the average adjusted closing price over the previous 5, 10, 20, and 50 trading observations.

To make the features more comparable across stocks with different price levels, four additional ratio features were calculated:

- MA_Ratio_5
- MA_Ratio_10
- MA_Ratio_20
- MA_Ratio_50

These ratios measure the percentage difference between the current adjusted closing price and its corresponding moving average.

**Formula:**

MA_Ratio = (Adj Close / MA - 1) × 100

A positive value indicates that the current adjusted closing price is above its moving average, while a negative value indicates that it is below.

The mean ratios were:

- MA_Ratio_5: 0.1155%
- MA_Ratio_10: 0.2667%
- MA_Ratio_20: 0.5686%
- MA_Ratio_50: 1.4724%

These features provide information about short- and medium-term price trends.

### 5. Momentum Features

Three momentum features were created:

- Momentum_5D
- Momentum_10D
- Momentum_20D

They measure the percentage change in adjusted closing prices over the previous 5, 10, and 20 trading observations.

**Formula:**

Momentum = (Adj Close(t) / Adj Close(t-n) - 1) × 100

The average momentum values were:

- Momentum_5D: 0.3621%
- Momentum_10D: 0.7205%
- Momentum_20D: 1.4257%

The positive averages suggest that historical price changes were slightly positive on average over these observation windows.

### 6. Relative Strength Index (RSI)

The RSI_14 feature was calculated using a 14-period Exponential Moving Average-based smoothing method.

RSI measures the strength of recent upward and downward price movements and ranges from 0 to 100.

Common interpretations include:

- Above 70: Potentially overbought conditions.
- Below 30: Potentially oversold conditions.
- Around 50: Relatively balanced momentum.

**Statistics:**

- Mean: 53.3840
- Standard deviation: 11.9792
- Minimum: 7.3858
- Median: 53.5615
- Maximum: 90.9401

The average RSI was slightly above 50, indicating a modest positive momentum tendency across the observations.

### 7. MACD Features

The Moving Average Convergence Divergence (MACD) indicator was calculated using exponential moving averages.

Three features were created:

- MACD: Difference between the 12-period and 26-period exponential moving averages.
- MACD_Signal: 9-period exponential moving average of MACD.
- MACD_Histogram: Difference between MACD and its signal line.

These features capture changes in price momentum and potential trend shifts.

**Statistics:**

| Feature        | Mean   | Standard Deviation | Minimum   | Maximum |
| -------------- | ------ | ------------------ | --------- | ------- |
| MACD           | 0.1533 | 1.1150             | \-16.9124 | 14.2964 |
| MACD_Signal    | 0.1528 | 1.0507             | \-15.0945 | 11.9954 |
| MACD_Histogram | 0.0007 | 0.3341             | \-5.6738  | 4.8655  |

The histogram's mean was close to zero, indicating that MACD and its signal line were relatively balanced on average.

### 8. Calendar Features

Seven calendar-related features were created to capture recurring temporal patterns:

- DayOfWeek
- Month
- Quarter
- DayOfWeek_Sin
- DayOfWeek_Cos
- Month_Sin
- Month_Cos

The sine and cosine transformations encode weekday and monthly cycles as continuous numerical values.

This representation helps models capture cyclical patterns without treating December and January, for example, as distant categories.

The weekday cycle uses five trading days, while the monthly cycle uses twelve months.

### Missing Values

Some missing values were generated naturally during feature engineering:

- Lag features require previous observations.
- Rolling volatility and moving averages require sufficient historical windows.
- RSI and MACD require initial observations to initialize their calculations.
- Daily returns require a previous closing price.

These missing values were expected and were not automatically replaced with zeros.

### Conclusion

The daily feature engineering process generated technical, historical, momentum, volatility, and calendar features from the original stock prices.

Together, these features provide different perspectives on historical market behavior and establish a richer input dataset for subsequent machine learning experiments.

# Daily Feature Engineering – Summary

Daily feature engineering was performed to extract useful information from historical stock prices and create additional variables for machine learning.

The following feature groups were generated:

| Feature Group         | Features Created                            | Purpose                                          |
| --------------------- | ------------------------------------------- | ------------------------------------------------ |
| Daily Returns         | Daily_Return                                | Measure daily stock performance.                 |
| Return Lags           | Return_Lag_1, 5, 10, 20                     | Capture previous price movements.                |
| Rolling Volatility    | Volatility_5D, 10D, 20D                     | Measure historical price fluctuations.           |
| Moving Averages       | MA_5, 10, 20, 50                            | Identify historical price trends.                |
| Moving Average Ratios | MA_Ratio_5, 10, 20, 50                      | Measure price distance from moving averages.     |
| Momentum              | Momentum_5D, 10D, 20D                       | Measure recent price momentum.                   |
| RSI                   | RSI_14                                      | Evaluate the strength of recent price movements. |
| MACD                  | MACD, MACD_Signal, MACD_Histogram           | Capture momentum and trend changes.              |
| Calendar              | DayOfWeek, Month, Quarter, Sin/Cos features | Capture recurring calendar patterns.             |

The generated features provide information about daily performance, historical trends, volatility, momentum, and seasonal behavior.

Missing values were mainly caused by the historical lookback requirements of lagged and rolling calculations. They were retained without arbitrary imputation.

**Final Outcome:** Multiple daily features were successfully engineered, expanding the dataset with historical price indicators and calendar information for the next machine learning stage.