# Trading Simulation & Strategy Evaluation

## 1. Simulation Objective

The objective of this stage was to evaluate the practical performance of the developed machine learning models by translating their predictions into executable trading strategies.

Two strategies were implemented and evaluated against the S&P/TSX Composite Index to determine whether incorporating market conditions improves stock selection and portfolio performance.

## 2. Trading Strategies

### Strategy 1: Top 3 Stock Selection

The baseline strategy relies exclusively on the Stock Outperformance Model.

At each trading date:
- Stocks are ranked according to their predicted outperformance probabilities.
- The three highest-ranked stocks are selected.
- An equal investment amount is allocated to each selected stock.
- Positions are held for five trading days before being closed.

This strategy provides a baseline for evaluating stock-level predictions without considering broader market conditions.

### Strategy 2: Market-Aware Stock Selection

The second strategy combines stock-level predictions with the Market Regime Model.

The portfolio allocation is adjusted according to the predicted market condition:

- **Bullish:** Full allocation to the selected stocks.
- **Sideways:** Reduced allocation to limit market exposure.
- **Bearish:** No new positions are opened.

Within each permitted market condition, the three highest-ranked stocks are selected using their predicted outperformance probabilities.

This approach introduces market awareness into the trading decision process rather than relying exclusively on individual stock predictions.

## 3. Trading Assumptions

Both strategies follow consistent trading assumptions to ensure a meaningful comparison:

- Initial capital: $1,500.
- Maximum of 15 concurrent positions.
- Five-trading-day holding period.
- Equal allocation across selected positions, subject to the available capital and strategy-specific allocation rules.
- A 0.2% round-trip transaction fee.
- Capital is reused after positions are closed.

## 4. Vectorized Simulation

A vectorized simulation was implemented to evaluate the strategies efficiently across the historical test dataset.

The simulation identifies entry and exit dates, calculates investment amounts, estimates gross and net profits, and tracks trading activity.

This approach provides an initial overview of strategy performance, including trade count, win rate, transaction costs, capital utilization, and cumulative returns.

## 5. Exact Simulation with Reinvestment

An additional event-driven simulation was developed to represent portfolio execution more realistically.

Unlike the vectorized approach, this simulation manages available cash and active positions over time.

Its main components include:

- Opening positions subject to available capital and position limits.
- Closing positions when their holding periods end.
- Deducting transaction fees from realized profits.
- Reinvesting available capital in subsequent trades.
- Tracking cash, invested capital, market value, and total portfolio equity.

Portfolio equity is calculated using available cash and the current market value of open positions. This provides a more realistic representation of portfolio performance than simply accumulating individual trade returns.

## 6. Risk Management and Performance Evaluation

Several performance and risk metrics were calculated to assess the strategies beyond total profitability.

The evaluation includes:

- **Total Return:** Measures overall portfolio growth.
- **CAGR:** Estimates the annualized growth rate.
- **Sharpe Ratio:** Evaluates returns relative to portfolio volatility.
- **Maximum Drawdown:** Measures the largest decline from a previous equity peak.
- **Annualized Volatility:** Measures fluctuations in portfolio returns.
- **Rolling Returns:** Examines performance across different investment horizons.
- **Win Rate:** Measures the proportion of profitable trades.

A Stop Loss mechanism was also tested to examine whether limiting individual trade losses improves overall portfolio performance.

The results showed that Stop Loss did not consistently improve the strategies. In particular, it reduced profitability in the Market-Aware strategy without providing a meaningful improvement in maximum drawdown. Therefore, the baseline configuration without Stop Loss was retained for the final comparison.

## 7. Strategy Comparison

Both strategies were evaluated over a common testing period to ensure that their performance was compared across the same market conditions.

The Market-Aware strategy performed better than the baseline Top 3 strategy. It achieved positive returns, a higher Sharpe Ratio, and a lower maximum drawdown.

These findings suggest that incorporating predicted market conditions into stock selection and capital allocation can improve the performance of a stock-level prediction strategy.

However, the improvement does not necessarily indicate that the underlying models can consistently predict market movements or stock outperformance.

## 8. Benchmark Comparison

The S&P/TSX Composite Index was selected as the benchmark to evaluate the strategies against the broader Canadian equity market.

The benchmark was simulated using the same initial capital and common evaluation period, assuming a buy-and-hold investment.

The results showed that the benchmark substantially outperformed both trading strategies.

Although the Market-Aware strategy achieved positive returns and improved upon the baseline strategy, it did not capture the broader market's growth during the testing period.

This comparison highlights an important distinction between building a profitable trading strategy and developing one that outperforms a passive market investment.

## 9. Final Findings

The simulation results provide several important findings:

1. Stock-level predictions alone were insufficient to produce consistently attractive portfolio performance.
2. Incorporating market regime predictions improved stock selection and capital allocation.
3. The Market-Aware strategy demonstrated better profitability and risk-adjusted performance than the baseline strategy.
4. Stop Loss did not improve the overall results under the tested configuration.
5. Both strategies underperformed the S&P/TSX Composite benchmark.

Overall, the simulation demonstrates the value of combining stock-level predictions with market-level information. However, the benchmark comparison indicates that further improvements in predictive accuracy, portfolio allocation, and risk management are necessary before the strategy can be considered competitive with passive market investing.
