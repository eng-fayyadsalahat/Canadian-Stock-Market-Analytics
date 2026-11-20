
from Data import *
from Strategy1_Stock_Trade import portfolio_s1
from Market_Aware_Stock_Strategy import portfolio_s2

def simulate_tsx(tsx_data, strategy, initial_capital=1500):

    # ------------------------------------------
    # 1. Prepare TSX benchmark data
    # ------------------------------------------

    benchmark = (
        tsx_data[
            ["Date", "TSX_Adj_Close"]
        ]
        .copy()
    )

    benchmark["Date"] = pd.to_datetime(benchmark["Date"])

    benchmark = (
        benchmark
        .dropna(subset=["TSX_Adj_Close"])
        .drop_duplicates(subset="Date", keep="last")
        .sort_values("Date")
        .reset_index(drop=True)
    )

    # ------------------------------------------
    # 2. Determine strategy testing period
    # ------------------------------------------

    strategy = strategy.copy()

    strategy["Entry_Date"] = pd.to_datetime(strategy["Entry_Date"])
    strategy["Exit_Date"] = pd.to_datetime(strategy["Exit_Date"])

    start_date = strategy["Entry_Date"].min()
    end_date = strategy["Exit_Date"].max()

    # ------------------------------------------
    # 3. Select common benchmark period
    # ------------------------------------------

    benchmark_period = benchmark[
        (benchmark["Date"] >= start_date) &
        (benchmark["Date"] <= end_date)
    ].copy()

    if len(benchmark_period) < 2:
        raise ValueError(
            "Insufficient TSX data for the strategy testing period."
        )

    benchmark_start = benchmark_period.iloc[0]
    benchmark_end = benchmark_period.iloc[-1]

    # ------------------------------------------
    # 4. Calculate benchmark performance
    # ------------------------------------------

    start_price = benchmark_start["TSX_Adj_Close"]
    end_price = benchmark_end["TSX_Adj_Close"]

    benchmark_return = (
        (end_price / start_price) - 1
    ) * 100

    benchmark_profit = (
        initial_capital * benchmark_return / 100
    )

    benchmark_final_equity = (
        initial_capital + benchmark_profit
    )

    # ------------------------------------------
    # 5. Calculate CAGR
    # ------------------------------------------

    testing_days = (
        benchmark_end["Date"] - benchmark_start["Date"]
    ).days

    testing_years = testing_days / 365.25

    benchmark_cagr = (
        (
            benchmark_final_equity / initial_capital
        ) ** (1 / testing_years) - 1
    ) * 100 if testing_years > 0 else np.nan

    # ------------------------------------------
    # 6. Return results
    # ------------------------------------------

    return {
        "Benchmark": "S&P/TSX Composite",
        "Start_Date": benchmark_start["Date"],
        "End_Date": benchmark_end["Date"],
        "Initial_Capital": initial_capital,
        "Final_Equity": round(benchmark_final_equity, 2),
        "Net_Profit": round(benchmark_profit, 2),
        "Total_Return": round(benchmark_return, 2),
        "Testing_Period_Years": round(testing_years, 2),
        "CAGR": round(benchmark_cagr, 2)
    }

INITIAL_CAPITAL = 1500
TRADING_DAYS = 252



# Performance metrics
def calculate_performance_metrics(equity, returns, initial_capital=1500):

    final_equity = equity.iloc[-1]

    total_return = (
        (final_equity / initial_capital) - 1
    ) * 100

    years = len(equity) / TRADING_DAYS

    cagr = (
        (final_equity / initial_capital) ** (1 / years) - 1
    ) * 100

    volatility = returns.std() * np.sqrt(TRADING_DAYS) * 100

    sharpe = (
        returns.mean() / returns.std() * np.sqrt(TRADING_DAYS)
        if returns.std() != 0 else np.nan
    )

    rolling_max = equity.cummax()

    drawdown = (
        equity / rolling_max - 1
    ) * 100

    max_drawdown = drawdown.min()

    return {
        "Initial Capital": initial_capital,
        "Final Equity": final_equity,
        "Net Profit": final_equity - initial_capital,
        "Total Return (%)": total_return,
        "CAGR (%)": cagr,
        "Annualized Volatility (%)": volatility,
        "Sharpe Ratio": sharpe,
        "Maximum Drawdown (%)": max_drawdown
    }

def add_tsx_benchmark(
    tsx_data,
    equity_comparison,
    initial_capital=1500
):

    equity_comparison = equity_comparison.copy()

    # 1. Prepare TSX Data
    tsx = tsx_data.copy()

    tsx["Date"] = pd.to_datetime(tsx["Date"])

    tsx = (
        tsx.sort_values("Date")
        .drop_duplicates(subset="Date")
        .set_index("Date")
    )

    # 2. Determine Common Period
    equity_comparison.index = pd.to_datetime(
        equity_comparison.index
    )

    start_date = equity_comparison.index.min()
    end_date = equity_comparison.index.max()

    # 3. Align TSX with Portfolio Trading Dates
    tsx_common = tsx.loc[
        start_date:end_date
    ].copy()

    tsx_common = tsx_common.reindex(
        equity_comparison.index
    )

    tsx_common["TSX_Adj_Close"] = (
        tsx_common["TSX_Adj_Close"].ffill()
    )

    # 4. Calculate Benchmark Equity
    tsx_initial_price = tsx_common["TSX_Adj_Close"].iloc[0]
    tsx_final_price = tsx_common["TSX_Adj_Close"].iloc[-1]

    if pd.isna(tsx_initial_price) or tsx_initial_price <= 0:
        raise ValueError("Invalid TSX initial price.")

    tsx_final_equity = (
        initial_capital
        * tsx_final_price
        / tsx_initial_price
    )

    tsx_total_return = (
        (tsx_final_equity / initial_capital) - 1
    ) * 100

    years = (
        (end_date - start_date).days / 365.25
    )

    tsx_cagr = (
        (tsx_final_equity / initial_capital) ** (1 / years) - 1
    ) * 100 if years > 0 else np.nan

    # 5. Add Benchmark to Equity Comparison
    equity_comparison["TSX_Benchmark"] = (
        initial_capital
        * tsx_common["TSX_Adj_Close"]
        / tsx_initial_price
    )

    # 6. Display Results
    print("TSX Benchmark Results")
    print("--------------------")
    print(f"Initial Capital: ${initial_capital:.2f}")
    print(f"Final Equity: ${tsx_final_equity:.2f}")
    print(f"Net Profit: ${tsx_final_equity - initial_capital:.2f}")
    print(f"Total Return: {tsx_total_return:.2f}%")
    print(f"CAGR: {tsx_cagr:.2f}%")

    return equity_comparison



portfolio_s1.index = pd.to_datetime(portfolio_s1.index)
portfolio_s2.index = pd.to_datetime(portfolio_s2.index)

common_dates = portfolio_s1.index.intersection(
    portfolio_s2.index
).sort_values()

portfolio_s1_common = portfolio_s1.loc[common_dates].copy()
portfolio_s2_common = portfolio_s2.loc[common_dates].copy()

portfolio_s1["Date"] = pd.to_datetime(portfolio_s1["Date"])
portfolio_s2["Date"] = pd.to_datetime(portfolio_s2["Date"])

portfolio_s1 = portfolio_s1.sort_values("Date").reset_index(drop=True)
portfolio_s2 = portfolio_s2.sort_values("Date").reset_index(drop=True)


start_date = max(
    portfolio_s1["Date"].min(),
    portfolio_s2["Date"].min()
)

end_date = min(
    portfolio_s1["Date"].max(),
    portfolio_s2["Date"].max()
)


portfolio_s1_common = portfolio_s1[
    portfolio_s1["Date"].between(start_date, end_date)
].copy()

portfolio_s2_common = portfolio_s2[
    portfolio_s2["Date"].between(start_date, end_date)
].copy()

# Unified trading calendar
trading_calendar = portfolio_s1_common["Date"].sort_values().unique()

# Set Date as index
s1 = portfolio_s1_common.set_index("Date").sort_index()
s2 = portfolio_s2_common.set_index("Date").sort_index()

# Align both portfolios to the same trading calendar
equity_comparison = pd.DataFrame(index=trading_calendar)

equity_comparison["Strategy_1_Equity"] = (
    s1["Equity"].reindex(trading_calendar).ffill()
)

equity_comparison["Strategy_2_Equity"] = (
    s2["Equity"].reindex(trading_calendar).ffill()
)

# Restore initial equity if any leading values are missing
equity_comparison = equity_comparison.fillna(1500)

equity_comparison.index = pd.to_datetime(equity_comparison.index)
equity_comparison.index.name = "Date"

# Daily returns based on portfolio equity
daily_returns = equity_comparison.pct_change().fillna(0)

# Calculate metrics for both strategies
s1_metrics = calculate_performance_metrics(
    equity_comparison["Strategy_1_Equity"],
    daily_returns["Strategy_1_Equity"],
    INITIAL_CAPITAL
)

s2_metrics = calculate_performance_metrics(
    equity_comparison["Strategy_2_Equity"],
    daily_returns["Strategy_2_Equity"],
    INITIAL_CAPITAL
)

comparison = pd.DataFrame({
    "Strategy 1: Top 3 Stocks": s1_metrics,
    "Strategy 2: Market-Aware": s2_metrics
})

rolling_comparison = pd.DataFrame(index=equity_comparison.index)


equity_comparison = add_tsx_benchmark(
    tsx_data=tsx_data,
    equity_comparison=equity_comparison,
    initial_capital=1500
)

for strategy in equity_comparison.columns:

    for window in [63, 126, 252]:

        rolling_return = (
            equity_comparison[strategy]
            / equity_comparison[strategy].shift(window)
            - 1
        ) * 100

        rolling_comparison[
            f"{strategy}_{window}D"
        ] = rolling_return

rolling_summary = pd.DataFrame({
    "Best Return": rolling_comparison.max(),
    "Worst Return": rolling_comparison.min()
})
benchmark_comparison = pd.DataFrame({
    "Strategy 1: Top 3": [
        equity_comparison["Strategy_1_Equity"].iloc[-1]
    ],
    "Strategy 2: Market-Aware": [
        equity_comparison["Strategy_2_Equity"].iloc[-1]
    ],
    "TSX Benchmark": [
        equity_comparison["TSX_Benchmark"].iloc[-1]
    ]
}, index=["Final Equity"]).T

benchmark_comparison["Net Profit"] = (
    benchmark_comparison["Final Equity"] - INITIAL_CAPITAL
)

benchmark_comparison["Total Return (%)"] = (
    benchmark_comparison["Net Profit"] / INITIAL_CAPITAL * 100
)



def run():
    print("Running TSX Benchmark...")

    # TSX Benchmark

    return {
        "benchmark_comparison": benchmark_comparison.round(4)
    }