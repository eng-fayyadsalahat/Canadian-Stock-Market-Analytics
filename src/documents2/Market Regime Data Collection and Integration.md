# Market Regime Data Collection and Integration

## 1. Canadian Market Index Data Collection

To develop the Market Regime Prediction model, historical data for the **S&P/TSX Composite Index (^GSPTSE)** was collected using the yfinance Python library.

The index was selected because it represents the Canadian equity market, which is the primary focus of this project. The S&P 500 was not used as the target market benchmark because it represents the US stock market.

Historical data was downloaded starting from January 1, 2000, with automatic price adjustment disabled to preserve the original downloaded price fields.

The following variables were retrieved:

- **TSX_Open:** Opening index value.
- **TSX_High:** Highest index value during the trading session.
- **TSX_Low:** Lowest index value during the trading session.
- **TSX_Close:** Closing index value.
- **TSX_Adj_Close:** Adjusted closing index value.
- **TSX_Volume:** Trading volume.

Additional data preparation steps included handling possible MultiIndex columns, converting dates to timezone-naive datetime values, sorting observations chronologically, and removing duplicate dates.

## 2. Market Target Engineering

The S&P/TSX Composite closing prices were used to calculate the five-trading-day future market return.

The resulting target variables were:

- Future_Market_Return_5D: The percentage return of the index over the next five trading days.
- Market_Regime_5D: The categorical market regime derived from the future return.

Three market regimes were defined:

| Market Regime | Condition                         |
| ------------- | --------------------------------- |
| Bullish       | Future return > +1%               |
| Bearish       | Future return < -1%               |
| Sideways      | Future return between -1% and +1% |

This formulation converts the market prediction task into a three-class classification problem.

## 3. Economic Data Preparation

The economic dataset was extracted from the previously integrated daily stock and macroeconomic dataset.

The MARKET_FEATURES variables were selected alongside the availability dates:

- Bank_Availability_Date
- Macro_Availability_Date

Since the original dataset contains multiple stock records for each trading date, duplicate dates were removed to create one economic observation per date.

The resulting economic_daily dataset contains daily economic features rather than separate observations for each stock ticker.

## 4. Economic and Market Target Integration

The economic features were combined with the market target variables using the Date column as the common key.

An inner join was applied to retain only dates available in both datasets.

The merge operation used validate="one_to_one" to ensure that each date appeared only once in each dataset, preventing unintended duplication during integration.

The resulting market_dataset contains:

- Daily economic indicators.
- Bank and macroeconomic availability dates.
- Five-day future market returns.
- Three-class market regime labels.

This dataset provides the foundation for training and evaluating the Market Regime Prediction model.

## 5. Conclusion

The integration process created a unified daily dataset connecting Canadian macroeconomic conditions with the future performance of the S&P/TSX Composite Index.

Unlike the stock-level prediction model, which evaluates the relative outperformance of individual stocks, the Market Regime Prediction model focuses on forecasting the broader Canadian market environment.

The resulting dataset is therefore used independently for market-level classification and can later provide additional signals to the trading strategies.

### Market Regime Data Collection and Integration

Historical data for the S&P/TSX Composite Index (^GSPTSE) was collected using yfinance, starting from January 2000. This index was selected to represent the Canadian equity market, which is the primary focus of the project.

The five-trading-day future market return (Future_Market_Return_5D) was calculated using the index closing prices and converted into three market regimes: Bullish, Bearish, and Sideways, based on thresholds of +1% and -1%.

The daily economic features were extracted from the integrated dataset using MARKET_FEATURES. Duplicate dates were removed to ensure one economic observation per trading day, while bank and macroeconomic availability dates were retained.

Finally, the economic dataset was merged with the market target variables using an inner join on Date, with one-to-one validation to ensure unique dates.

The resulting market_dataset combines daily economic indicators with future market returns and regime labels, providing the input dataset for the Market Regime Prediction model.