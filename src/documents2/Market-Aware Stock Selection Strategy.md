### Strategy 2 – Market-Aware Stock Selection Strategy

This strategy combines stock outperformance predictions with overall Canadian market regime predictions to make market-aware investment decisions.

It integrates the outputs of two independently trained machine learning models:

- **Stock Outperformance Model:** Estimates the probability that each selected Canadian stock will outperform the cross-sectional median return over the next five trading days. These probabilities are used to rank stocks and identify potential investment opportunities.
- **Market Regime Classification Model:** Predicts the overall market condition as Bullish, Bearish, or Sideways using economic and market-related features derived from Canadian market data.

The predictions from both models are merged by date to create a unified dataset. This allows the strategy to consider individual stock opportunities within the context of broader market conditions.

#### Market-Based Allocation Rules

The strategy adjusts its investment allocation according to the predicted market regime:

- **Bullish:** Allocates the full investment amount to each selected stock.
- **Sideways:** Reduces the investment amount for each selected stock.
- **Bearish:** Avoids opening new positions.

For each eligible trading date, stocks are ranked by their predicted outperformance probabilities. The highest-ranked stocks are selected, with five-day closing momentum used as a secondary ranking criterion when probabilities are tied.

#### Trade Execution and Risk Management

Selected stocks are assigned investments based on the predicted market regime. Each position is held for five trading days, and a round-trip transaction fee is applied when calculating net profit.

The simulation records trade-level information, including entry and exit dates, investment allocation, gross profit, transaction fees, and net profit.

It also evaluates the strategy's overall trading activity, profitability, win rate, maximum number of simultaneously open positions, required capital, total return, and compound annual growth rate.

#### Benchmark Comparison

The strategy is evaluated against the S&P/TSX Composite Index (^GSPTSE), which represents the broader Canadian equity market and serves as the benchmark for performance evaluation.

Both the strategy and the benchmark are evaluated over the same testing period using an equivalent initial capital. The benchmark return is calculated using the index's adjusted closing prices, representing a passive buy-and-hold investment approach.

This comparison helps assess whether the proposed market-aware stock selection approach can outperform the broader Canadian market, rather than evaluating its performance in isolation.

By incorporating broader market conditions into stock selection and capital allocation, this strategy aims to adapt investment exposure to changing market environments rather than relying exclusively on individual stock predictions.

### Strategy 2 – Market-Aware Stock Selection Strategy

This strategy combines stock outperformance predictions with Canadian market regime classification to make investment decisions that account for both individual stock opportunities and overall market conditions.

Stocks are ranked according to their predicted outperformance probabilities, while the predicted market regime determines the investment allocation. The strategy maintains full exposure during Bullish conditions, reduces investment during Sideways conditions, and avoids opening new positions during Bearish conditions.

Selected positions are held for five trading days, with transaction fees included in the profit calculations. The simulation evaluates trading performance, capital requirements, and risk-related metrics.

#### Benchmark Comparison

The strategy is compared against the S&P/TSX Composite Index (^GSPTSE) over the same testing period using equivalent initial capital. This benchmark provides a passive market investment reference to evaluate whether the proposed strategy can outperform the broader Canadian equity market.

The objective is to improve stock selection and manage investment exposure by incorporating market conditions into the trading decision process.