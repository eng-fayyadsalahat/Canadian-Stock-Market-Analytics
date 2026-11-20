# Canadian Market-Aware Machine Learning Trading Strategy

## Project Overview

This project develops an end-to-end machine learning-based trading framework for the Canadian stock market.

It combines historical Canadian stock market data, technical indicators, macroeconomic indicators, and market regime analysis to generate stock selection signals and simulate systematic trading strategies.

The main objective is to investigate whether combining stock-level machine learning predictions with broader market conditions can improve trading decisions compared with strategies based exclusively on individual stock predictions.

The project covers the complete workflow, including data collection, data integration, preprocessing, feature engineering, exploratory data analysis, model development, trading strategy construction, portfolio simulation, risk evaluation, benchmark comparison, and workflow automation.

The S&P/TSX Composite Index is used as the primary market benchmark.

---

## Project Objectives

- Collect and integrate Canadian stock market and economic data.
- Build a unified daily dataset for machine learning.
- Engineer technical, economic, and calendar-based features.
- Predict the relative future performance of individual stocks.
- Classify future market conditions into different regimes.
- Develop stock-based and market-aware trading strategies.
- Simulate portfolio execution under defined trading assumptions.
- Evaluate profitability, portfolio risk, and strategy behavior.
- Compare trading strategies against the S&P/TSX Composite Index.
- Build an automated and reusable execution pipeline.

---

## Project Architecture

The project is divided into interconnected components.

### Data Collection

Collecting historical Canadian stock market information and economic indicators from different sources.

### Data Integration

Combining stock market and economic datasets while maintaining date alignment and information availability.

### Feature Engineering

Creating technical indicators, macroeconomic variables, and cyclical calendar features.

### Stock Prediction

Training machine learning models to estimate the probability that a stock will outperform the cross-sectional median future return of the selected stocks.

### Market Regime Classification

Developing a separate model to classify expected market conditions as Bullish, Bearish, or Sideways.

### Trading Strategies

Using stock prediction probabilities and market regime signals to construct portfolios and generate trading decisions.

### Simulation and Risk Evaluation

Simulating trades, tracking portfolio equity, accounting for transaction costs, and evaluating financial performance and risk.

### Benchmark Comparison

Comparing the developed strategies against the S&P/TSX Composite Index.

### Workflow Automation

Connecting the project components through reusable Python functions and a central execution pipeline.

---

## Data Sources

The project integrates financial market information and Canadian economic indicators from multiple sources.

### Stock Market Data

Historical stock market data includes:

- Open, High, Low, and Close prices.
- Adjusted closing prices.
- Trading volume.
- Dividends.
- Stock splits.

The selected Canadian stocks are represented using their respective market ticker symbols.

### Canadian Economic Data

The project incorporates macroeconomic indicators to provide additional context about the Canadian economy.

These indicators include:

- Bank of Canada policy rate.
- Government bond yields.
- USD/CAD exchange rate.
- Consumer Price Index.
- Inflation indicators.
- Real Gross Domestic Product.
- GDP growth indicators.
- Employment statistics.
- Labour force statistics.
- Participation rate.
- Unemployment rate.
- Bank of Canada Commodity Price Index.
- Commodity sector indicators.
- Yield spread.
- Economic growth and change indicators.

### Market Benchmark

The S&P/TSX Composite Index is used as the market benchmark to evaluate the trading strategies against the broader Canadian equity market.

### Data Availability

Economic observations are not necessarily available on their reference dates.

The project therefore maintains availability-related date information to help ensure that historical trading decisions rely on information that would have been available at the time.

---

## Data Processing and Feature Engineering

The project uses a structured data preparation workflow.

The process includes:

- Loading and validating raw datasets.
- Converting date columns into datetime formats.
- Sorting stock observations chronologically.
- Integrating datasets with different frequencies.
- Handling economic information availability.
- Creating technical indicators.
- Generating macroeconomic features.
- Constructing cyclical calendar variables.
- Preparing stock and market regime targets.
- Preparing datasets for model training and simulation.

### Technical Features

Technical indicators are derived from historical stock prices and trading volume.

They include:

- Daily returns.
- Lagged returns.
- Rolling volatility.
- Moving average ratios.
- Price momentum.
- Relative Strength Index (RSI).
- Moving Average Convergence Divergence (MACD).
- MACD signal.
- MACD histogram.

### Economic Features

Economic variables provide information about the broader Canadian economy, including interest rates, bond yields, exchange rates, inflation, GDP, employment, and commodity prices.

### Calendar Features

Cyclical transformations are applied to calendar variables using sine and cosine functions.

The project includes:

- Day-of-week features.
- Month-of-year features.

### Categorical Features

Stock ticker symbols are treated as categorical variables and encoded using one-hot encoding.

---

## Target Variables

### Stock-Level Target

The stock prediction task is formulated as a binary classification problem.

A stock is classified as an outperformer when its future return exceeds the cross-sectional median future return of the selected stocks on the same date.

The model estimates the probability of relative stock outperformance, which is subsequently used to rank stocks and select potential trading candidates.

### Market Regime Target

The market regime model classifies future market conditions into three categories:

- **Bullish:** Expected positive market conditions.
- **Bearish:** Expected negative market conditions.
- **Sideways:** Market conditions within the defined neutral return range.

The target is constructed using future returns of the TSX market benchmark.

The stock prediction and market regime models are trained separately.

---

## Machine Learning Models

The project evaluates several classification algorithms.

### Stock Prediction Models

The evaluated algorithms include:

- Decision Tree Classifier.
- Random Forest Classifier.
- XGBoost Classifier.

The models are evaluated using classification metrics and ranking-oriented evaluation methods.

Since the main objective is stock selection, the evaluation also considers cross-sectional ranking performance rather than relying exclusively on classification accuracy.

The selected model generates stock outperformance probabilities for the trading strategies.

### Market Regime Models

The market regime task evaluates:

- Decision Tree Classifier.
- Random Forest Classifier.
- XGBoost Classifier.
- Dummy Classifier as a baseline.

The evaluation considers class imbalance and the ability to distinguish between different market conditions.

Balanced accuracy and macro F1-score are considered important metrics alongside ordinary accuracy.

The selected model generates predicted probabilities for the market regimes.

---

## Trading Strategies

The project develops multiple trading approaches to investigate the value of combining stock-level predictions with market information.

### Strategy One: Stock-Based Top-Ranked Strategy

This strategy relies exclusively on the stock prediction model.

The trading process:

- Generates stock outperformance probabilities.
- Ranks available stocks by predicted probability.
- Uses momentum as a secondary ranking criterion.
- Selects the highest-ranked stocks.
- Allocates predefined capital to each selected stock.
- Holds positions for the predefined trading period.
- Accounts for transaction costs.

This strategy serves as the baseline for evaluating stock-level machine learning predictions without market regime information.

### Strategy Two: Market Regime Strategy

This component uses the predicted market regime probabilities to construct market signals.

It identifies the expected market condition and prepares the corresponding signals for integration with stock-level predictions.

The model's predicted probabilities are used rather than actual future market conditions.

### Strategy Three: Market-Aware Stock Selection Strategy

This strategy combines stock-level predictions with predicted market conditions.

The trading process:

- Generates stock outperformance probabilities.
- Predicts market regime probabilities.
- Merges stock and market predictions by trading date.
- Determines portfolio exposure according to the predicted market regime.
- Selects stocks based on their predicted probabilities.
- Adjusts capital allocation according to market conditions.
- Avoids opening new positions under unfavorable predicted conditions.
- Accounts for transaction costs and holding periods.

The separation between predicted and actual future market information is important to prevent future information leakage.

---

## Trading Simulation

The project implements vectorized and exact portfolio simulations.

### Vectorized Simulation

The vectorized simulation evaluates trading signals across the historical dataset.

It calculates:

- Entry and exit dates.
- Selected stocks.
- Position allocations.
- Gross returns.
- Transaction costs.
- Net returns.
- Trade-level performance.
- Portfolio-level results.

### Exact Portfolio Simulation

The exact simulation provides a more detailed representation of portfolio execution.

It tracks:

- Initial capital.
- Available cash.
- Open positions.
- Position sizes.
- Entry and exit prices.
- Holding periods.
- Realized profits and losses.
- Transaction fees.
- Portfolio equity.
- Maximum concurrent positions.

The simulation also supports capital constraints and position management.

---

## Risk Management and Performance Evaluation

The project evaluates trading strategies using financial performance and risk metrics.

### Performance Metrics

- Initial capital.
- Final portfolio equity.
- Net profit or loss.
- Total return.
- Compound Annual Growth Rate (CAGR).
- Number of trades.
- Win rate.
- Average trade return.

### Risk Metrics

- Sharpe Ratio.
- Maximum Drawdown.
- Annualized Volatility.
- Rolling Returns.
- Portfolio equity fluctuations.

### Rolling Performance

Rolling returns are used to examine how portfolio performance changes over different investment horizons.

This helps identify periods of stronger and weaker performance rather than relying exclusively on cumulative returns.

### Stop-Loss Evaluation

An additional simulation investigates the impact of stop-loss rules.

The stop-loss simulation is compared with the original strategy to examine its effect on profitability, win rate, Sharpe Ratio, and maximum drawdown.

The results demonstrate that adding a stop-loss rule does not automatically improve a trading strategy.

---

## Benchmark Comparison

The developed strategies are compared against the S&P/TSX Composite Index.

The benchmark comparison uses a common historical evaluation period to make the comparison more meaningful.

The evaluation considers:

- Portfolio equity growth.
- Total return.
- Net profit.
- CAGR.
- Risk-adjusted performance.
- Maximum drawdown.

The market-aware strategy performed better than the stock-only strategy in the evaluated simulation.

However, the TSX benchmark achieved stronger overall returns over the comparison period.

This highlights the importance of evaluating machine learning trading strategies against passive market alternatives rather than considering strategy profitability in isolation.

---

## Key Findings

The project provides several observations:

- Technical and economic information can be integrated into a unified machine learning dataset for the Canadian stock market.
- Stock-level predictions provide a systematic approach to ranking potential investment candidates.
- Market regime classification introduces an additional source of information for portfolio allocation.
- Market-aware trading changes trading frequency and capital exposure.
- The market-aware strategy performed better than the stock-only strategy in the evaluated simulation.
- The TSX benchmark outperformed both developed strategies over the comparison period.
- Stop-loss rules can have different effects on profitability and portfolio risk.
- Historical backtesting results should not be interpreted as guarantees of future performance.

---

## Project Structure

The repository is organized into the following components:

```text
Canadian-Market-Aware-ML-Trading/
│
├── strategies/
│   ├── Strategy1_Stock_Trade.py
│   ├── Market_Rigem_Strategy.py
│   ├── Market_Aware_Stock_Strategy.py
│   ├── Metric.py
│   ├── Benchmark.py
│   └── Data.py
│
├── src/
│   ├── Data/
│   │   ├── code/
│   │   │   ├── Canda-Stock.py
│   │   │   ├── Canda-Labour-Data.py
│   │   │   ├── Canda-GDP-Data.py
│   │   │   ├── Canda-CPI-Data.py
│   │   │   ├── Canda-BankofCandaAPI-data.py
│   │   │   └── Canda-BCPI-Monthly.py
│   │   │
│   │   └── Data Information/
│   │       ├── Canadian Stock Market Data.md
│   │       ├── Canadian Labour Market Data Collection and Preprocessing.md
│   │       ├── Canadian GDP Data.md
│   │       ├── Canadian Consumer Price Index (CPI).md
│   │       ├── Canadian Commodity Price Index (BCPI).md
│   │       └── Bank of Canda.md
│   │
│   ├── documents/
│   │   ├── Feature Engineering.md
│   │   ├── Daily Feature Engineering.md
│   │   ├── Daily Economic Features.md
│   │   ├── Macroeconomic Feature Engineering.md
│   │   ├── Calendar Features.md
│   │   ├── Target Creation.md
│   │   ├── Temporal Leakage Audit.md
│   │   └── OHLC Integrity Audit.md
│   │
│   ├── documents2/
│   │   ├── Stock Classification Model Development.md
│   │   ├── Stock Ranking Evaluation.md
│   │   ├── Market Regime Classification.md
│   │   ├── Market Regime Model Evaluation.md
│   │   ├── Strategy 1_ Top 3 Stocks – 5 Trading Days.md
│   │   ├── Market-Aware Stock Selection Strategy.md
│   │   ├── Trading Simulation & Strategy Evaluation.md
│   │   └── Benchmark Comparison.md
│   │
│   ├── data_prepare.ipynb
│   ├── data_integration.ipynb
│   ├── exploratory_data_analysis.ipynb
│   ├── feature_engineering.ipynb
│   └── model_and_simulation.ipynb
│
├── data/
│   ├── raw/
│   └── processed/
│
├── Main_Workflow.ipynb
├── run_pipeline.py
├── download_data.py
├── requirements.txt
├── Dockerfile
└── corntab.cron
```

The `src` directory contains the original data preparation, integration, exploratory analysis, feature engineering, and modeling notebooks, together with supporting documentation and data collection scripts.

The `strategies` directory contains the reusable Python modules responsible for data loading, trading strategies, performance metrics, and benchmark comparison.

The root directory contains the central pipeline, main workflow notebook, dependency definitions, data download utility, Docker configuration, and scheduled execution configuration.

---

## Installation and Setup

### Clone the Repository

```bash
git clone <YOUR_REPOSITORY_URL>
cd Canadian-Market-Aware-ML-Trading
```

### Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it:

**Linux / macOS**

```bash
source .venv/bin/activate
```

**Windows**

```bash
.venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Data Access

The project uses prepared datasets stored outside the Git repository and retrieved through Google Drive.

Before running the complete workflow:

- Configure the Google Drive file identifiers in `download_data.py`.
- Ensure the required files are accessible.
- Ensure the destination directories exist.
- Download the prepared datasets.

Run:

```bash
python download_data.py
```

The downloaded files are saved in the project's processed data directory.

The raw data directory is used for the TSX benchmark dataset and other required source data.

---

## Running the Project

After installing dependencies and preparing the required datasets, execute:

```bash
python run_pipeline.py
```

The central pipeline coordinates the project components, including data loading, model execution, prediction generation, trading strategies, portfolio simulation, and benchmark evaluation.

The `Main_Workflow.ipynb` notebook provides an interactive entry point for demonstrating and inspecting the complete workflow.

---

## Docker Support

The project includes a Dockerfile for running the pipeline in a consistent environment.

Build the image:

```bash
docker build -t canadian-trading-ml .
```

Run the pipeline:

```bash
docker run --rm \
  -v "$(pwd)/outputs:/app/outputs" \
  canadian-trading-ml
```

The output directory can be mounted to preserve generated results outside the container.

---

## Workflow Automation

The project includes a cron configuration file named `corntab.cron`.

It can be used to schedule automated execution of the trading pipeline on selected weekdays.

To install the schedule, review the configuration and update its project path and Python executable path to match the local environment.

Then install it using:

```bash
crontab corntab.cron
```

Execution logs can be redirected to a file for monitoring scheduled runs.

Automated execution depends on data availability and successful completion of the required data loading and prediction steps.

---

## Technologies Used

**Programming Language**
- Python

**Data Processing**
- Pandas
- NumPy

**Machine Learning**
- Scikit-learn
- XGBoost

**Financial Data**
- yfinance
- Canadian economic data sources

**Visualization**
- Matplotlib

**Model Persistence**
- Joblib

**Data Download**
- gdown

**Development and Automation**
- Jupyter Notebook
- Python Scripts
- Docker
- Linux Cron

---

## Limitations

This project is an educational and experimental machine learning trading system.

Its main limitations include:

- Financial markets are inherently uncertain.
- Historical relationships may not remain stable.
- Machine learning predictions are subject to errors.
- Market regime models may struggle to identify sudden market transitions.
- Economic data may be revised after publication.
- Backtesting assumptions may differ from real-world execution.
- Transaction costs, liquidity, slippage, and market impact can affect actual trading performance.
- Benchmark results depend on the evaluation period and price methodology.
- Historical performance does not guarantee future profitability.

---

## Future Improvements

Potential future developments include:

- Expanding the Canadian stock universe.
- Integrating additional financial and economic indicators.
- Improving economic data update automation.
- Exploring advanced market regime detection techniques.
- Evaluating alternative portfolio allocation methods.
- Incorporating more realistic execution costs and slippage.
- Testing strategies across different market conditions.
- Implementing paper trading with live market data.
- Improving workflow monitoring and error handling.

---

## Conclusion

This project demonstrates the development of an end-to-end machine learning trading framework for the Canadian stock market.

It integrates financial data engineering, macroeconomic analysis, machine learning, market regime classification, systematic portfolio construction, trading simulation, and risk evaluation into a unified workflow.

Rather than focusing exclusively on predictive accuracy, the project investigates how machine learning predictions translate into portfolio decisions and how those decisions perform relative to a real market benchmark.

The results emphasize that financial machine learning requires more than building predictive models. It also requires careful data handling, realistic simulation assumptions, risk evaluation, and objective comparison against passive investment alternatives.

---

## Disclaimer

This project was developed for educational, research, and portfolio demonstration purposes.

It does not provide financial advice, investment recommendations, or guarantees of future performance.

All trading simulations are based on historical data and assumptions that may not reflect actual market execution.

**Use at your own risk.**
