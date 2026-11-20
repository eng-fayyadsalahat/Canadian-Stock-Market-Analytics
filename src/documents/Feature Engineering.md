### Feature Engineering

The feature engineering phase focused on transforming historical stock price data into meaningful technical indicators that could help machine learning models identify patterns in stock price movements and predict future returns.

All price-based features were calculated independently for each stock (Ticker) using historical data, ensuring that information from different stocks was not mixed and that no future observations were used.

The following categories of features were created:

**1\. Daily Returns**

Calculated the daily percentage change in adjusted closing prices to measure the daily performance of each stock.

**2\. Lagged Returns**

Created historical return features over different time lags to capture previous price movements and provide the model with information about recent market behavior.

**3\. Rolling Volatility**

Calculated rolling standard deviations of daily returns over different windows to measure changes in stock price volatility and market risk.

**4\. Moving Averages**

Calculated simple moving averages over multiple periods to identify short-term and long-term price trends.

**5\. Moving Average Ratios**

Measured the percentage difference between the current adjusted closing price and its moving averages. These features help indicate whether a stock is trading above or below its recent average price.

**6\. Momentum Indicators**

Created momentum features over multiple periods to measure the cumulative percentage change in stock prices and capture the strength and direction of recent price movements.

**7\. Relative Strength Index (RSI)**

Added the 14-period RSI using Wilder's smoothing method to measure the strength of recent price movements and identify potentially overbought or oversold conditions.

**8\. MACD Indicators**

Calculated the MACD line, Signal line, and Histogram using standard exponential moving average settings. These indicators help capture changes in price trends and momentum.

Overall, this phase produced a set of technical features representing different aspects of stock market behavior, including returns, trends, volatility, and momentum. These features will be reviewed for missing values, correlation, and redundancy before being used in model training.

### Feature Engineering Summary

Created technical indicators from historical stock prices to capture market trends, returns, volatility, and momentum.

The engineered features include daily and lagged returns, rolling volatility, moving averages, moving average ratios, momentum indicators, RSI, and MACD.

All calculations were performed separately for each stock using historical observations only, providing the foundation for the next stages of feature selection and machine learning model development.