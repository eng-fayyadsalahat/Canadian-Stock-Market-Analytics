import pandas as pd
import numpy as np



def vectorized_simulation(
    trades_df,
    initial_capital=1500,
    round_trip_fee=0.002
):
    trades = trades_df.copy()

    trades["Entry_Date"] = pd.to_datetime(trades["Entry_Date"]) 
    trades["Exit_Date"] = pd.to_datetime(trades["Exit_Date"])

    # Convert percentage return to decimal
    returns = trades["Future_Return_5D"] / 100

    trades["Gross_Profit"] = trades["Investment"] * returns
    trades["Fees"] = trades["Investment"] * round_trip_fee
    trades["Net_Profit"] = trades["Gross_Profit"] - trades["Fees"]

    trades["Net_Return"] = (
        trades["Net_Profit"] / trades["Investment"]
    )

    summary = {
        "Total Trades": len(trades),
        "Total Investment": trades["Investment"].sum(),
        "Gross Profit": trades["Gross_Profit"].sum(),
        "Fees": trades["Fees"].sum(),
        "Net Profit": trades["Net_Profit"].sum(),
        "Win Rate (%)": (trades["Net_Profit"] > 0).mean() * 100,
        "Average Net Profit": trades["Net_Profit"].mean(),
        "Initial Capital": initial_capital,
        "Return on Initial Capital (%)": (
            trades["Net_Profit"].sum() / initial_capital * 100
        )
    }

    return trades, pd.Series(summary)


def exact_simulation(
    trades_df,
    daily_data,
    initial_capital=1500,
    max_open_positions=15,
    position_fraction=1 / 15,
    round_trip_fee=0.002,
    trading_dates=None
):
    trades = trades_df.copy()
    prices_data = daily_data.copy()

    # 1. Prepare dates
    trades["Entry_Date"] = pd.to_datetime(trades["Entry_Date"])
    trades["Exit_Date"] = pd.to_datetime(trades["Exit_Date"])

    prices_data["Date"] = pd.to_datetime(prices_data["Date"])

    trades = trades.sort_values(
        ["Entry_Date", "Ticker"]
    ).reset_index(drop=True)

    prices_data = prices_data[
        ["Date", "Ticker", "Adj Close"]
    ].drop_duplicates(
        ["Date", "Ticker"]
    )

    # 2. Build daily price matrix
    prices = prices_data.pivot(
        index="Date",
        columns="Ticker",
        values="Adj Close"
    ).sort_index()

    # 3. Build complete trading calendar
    if trading_dates is not None:
        dates = sorted(
            set(pd.to_datetime(trading_dates))
        )
    else:
        start_date = trades["Entry_Date"].min()
        end_date = trades["Exit_Date"].max()

        dates = sorted(
            prices.index[
                (prices.index >= start_date) &
                (prices.index <= end_date)
            ].tolist()
        )

    dates = sorted(
        set(dates)
        .union(trades["Entry_Date"])
        .union(trades["Exit_Date"])
    )

    # Carry forward the latest available price
    prices = prices.reindex(dates).ffill()

    cash = float(initial_capital)
    active_positions = []
    completed_trades = []
    daily_records = []

    # 4. Run simulation
    for date in dates:

        # Close positions whose exit date has arrived
        remaining_positions = []

        for position in active_positions:

            if position["Exit_Date"] <= date:

                exit_price = prices.at[
                    date, position["Ticker"]
                ]

                if pd.isna(exit_price):
                    raise ValueError(
                        f"Missing exit price: "
                        f"{position['Ticker']} on {date}"
                    )

                gross_profit = (
                    position["Investment"]
                    * (exit_price / position["Entry_Price"] - 1)
                )

                fees = position["Investment"] * round_trip_fee

                net_profit = gross_profit - fees

                cash += position["Investment"] + net_profit

                position["Exit_Price"] = exit_price
                position["Gross_Profit"] = gross_profit
                position["Fees"] = fees
                position["Net_Profit"] = net_profit
                position["Cash_After_Exit"] = cash

                completed_trades.append(position)

            else:
                remaining_positions.append(position)

        active_positions = remaining_positions

        # Open new positions
        todays_trades = trades[
            trades["Entry_Date"] == date
        ]

        for _, trade in todays_trades.iterrows():

            if len(active_positions) >= max_open_positions:
                break

            ticker = trade["Ticker"]

            entry_price = prices.at[date, ticker]

            if pd.isna(entry_price) or entry_price <= 0:
                raise ValueError(
                    f"Missing entry price: {ticker} on {date}"
                )

            investment = cash * position_fraction

            if investment <= 0 or cash < investment:
                continue

            position = {
                "Ticker": ticker,
                "Entry_Date": date,
                "Exit_Date": trade["Exit_Date"],
                "Investment": investment,
                "Entry_Price": entry_price
            }

            cash -= investment
            active_positions.append(position)

        # Calculate daily market value of open positions
        invested_capital = sum(
            p["Investment"] for p in active_positions
        )

        market_value = 0.0

        for position in active_positions:

            current_price = prices.at[
                date, position["Ticker"]
            ]

            if pd.isna(current_price):
                raise ValueError(
                    f"Missing market price: "
                    f"{position['Ticker']} on {date}"
                )

            position_value = (
                position["Investment"]
                * current_price / position["Entry_Price"]
            )

            market_value += position_value

        equity = cash + market_value

        daily_records.append({
            "Date": date,
            "Cash": cash,
            "Invested_Capital": invested_capital,
            "Market_Value": market_value,
            "Equity": equity,
            "Open_Positions": len(active_positions)
        })

    # 5. Create results
    results = pd.DataFrame(completed_trades)

    portfolio = pd.DataFrame(daily_records)

    portfolio = portfolio.set_index("Date").sort_index()

    # 6. Summary
    if not results.empty:
        total_profit = results["Net_Profit"].sum()
        win_rate = (
            results["Net_Profit"] > 0
        ).mean() * 100
    else:
        total_profit = 0
        win_rate = 0

    final_equity = (
        portfolio["Equity"].iloc[-1]
        if not portfolio.empty else initial_capital
    )
    
    if trading_dates is not None:
        dates = sorted(set(pd.to_datetime(trading_dates)))
    else:
        dates = sorted(
        set(trades["Entry_Date"]).union(trades["Exit_Date"]))
    summary = {
        "Initial Capital": initial_capital,
        "Final Cash": cash,
        "Total Trades": len(results),
        "Net Profit": total_profit,
        "Final Equity": final_equity,
        "Total Return (%)": (
            final_equity / initial_capital - 1
        ) * 100,
        "Win Rate (%)": win_rate,
        "Max Open Positions": (
            portfolio["Open_Positions"].max()
            if not portfolio.empty else 0
        ),
        "Trading Dates" : trading_dates,
        "Remaining Open Positions": len(active_positions),
        "First Date": portfolio.index.min() if not portfolio.empty else None,
        "Last Date": portfolio.index.max() if not portfolio.empty else None
    }

    return results, portfolio, pd.Series(summary)

def calculate_risk_metrics(
    portfolio,
    initial_capital=1500,
    risk_free_rate=0.0
):
    df = portfolio.copy()

    df["Date"] = pd.to_datetime(df["Date"])
    df = df.sort_values("Date").reset_index(drop=True)

    # Equity curve
    df["Equity"] = df["Equity"].astype(float)

    # Daily returns
    df["Daily_Return"] = df["Equity"].pct_change()

    # Sharpe Ratio
    daily_rf = risk_free_rate / 252

    excess_returns = df["Daily_Return"].dropna() - daily_rf

    if excess_returns.std() != 0 and len(excess_returns) > 1:
        sharpe = (
            excess_returns.mean()
            / excess_returns.std()
            * np.sqrt(252)
        )
    else:
        sharpe = np.nan

    # Maximum Drawdown
    df["Running_Peak"] = df["Equity"].cummax()

    df["Drawdown"] = (
        df["Equity"] / df["Running_Peak"] - 1
    )

    max_drawdown = df["Drawdown"].min() * 100

    # Rolling Returns
    rolling_periods = {
        "63D": 63,
        "126D": 126,
        "252D": 252
    }

    for name, period in rolling_periods.items():
        df[f"Rolling_Return_{name}"] = (
            df["Equity"] / df["Equity"].shift(period) - 1
        ) * 100

    metrics = {
        "Sharpe Ratio": sharpe,
        "Maximum Drawdown (%)": max_drawdown,
        "Best 63D Rolling Return (%)": df["Rolling_Return_63D"].max(),
        "Worst 63D Rolling Return (%)": df["Rolling_Return_63D"].min(),
        "Best 126D Rolling Return (%)": df["Rolling_Return_126D"].max(),
        "Worst 126D Rolling Return (%)": df["Rolling_Return_126D"].min(),
        "Best 252D Rolling Return (%)": df["Rolling_Return_252D"].max(),
        "Worst 252D Rolling Return (%)": df["Rolling_Return_252D"].min()
    }

    return df, pd.Series(metrics)

def apply_stop_loss(
    trades_df,
    daily_data,
    stop_loss_pct=0.03
):
    trades = trades_df.copy()
    prices = daily_data.copy()

    trades["Entry_Date"] = pd.to_datetime(trades["Entry_Date"])
    trades["Exit_Date"] = pd.to_datetime(trades["Exit_Date"])

    prices["Date"] = pd.to_datetime(prices["Date"])

    prices = prices[
        ["Date", "Ticker", "Adj Close"]
    ].dropna()

    prices = prices.sort_values(["Ticker", "Date"])

    price_groups = {
        ticker: group.set_index("Date")["Adj Close"].sort_index()
        for ticker, group in prices.groupby("Ticker")
    }

    actual_exit_dates = []
    actual_returns = []
    stop_loss_triggered = []

    for _, trade in trades.iterrows():

        ticker = trade["Ticker"]
        entry_date = trade["Entry_Date"]
        scheduled_exit = trade["Exit_Date"]

        ticker_prices = price_groups.get(ticker)

        if ticker_prices is None:
            raise ValueError(f"Missing price data for {ticker}")

        if entry_date not in ticker_prices.index:
            raise ValueError(
                f"Missing entry price for {ticker} on {entry_date}"
            )

        entry_price = ticker_prices.loc[entry_date]

        future_prices = ticker_prices.loc[
            (ticker_prices.index > entry_date)
            & (ticker_prices.index <= scheduled_exit)
        ]

        stop_price = entry_price * (1 - stop_loss_pct)

        hit = future_prices[future_prices <= stop_price]

        if not hit.empty:

            exit_date = hit.index[0]
            exit_price = hit.iloc[0]
            stopped = True

        else:

            if scheduled_exit not in ticker_prices.index:
                raise ValueError(
                    f"Missing scheduled exit price for {ticker} "
                    f"on {scheduled_exit}"
                )

            exit_date = scheduled_exit
            exit_price = ticker_prices.loc[scheduled_exit]
            stopped = False

        realized_return = (
            (exit_price / entry_price) - 1
        ) * 100

        actual_exit_dates.append(exit_date)
        actual_returns.append(realized_return)
        stop_loss_triggered.append(stopped)

    trades["Exit_Date"] = actual_exit_dates
    trades["Realized_Return_Pct"] = actual_returns
    trades["Stop_Loss_Triggered"] = stop_loss_triggered

    # Use the realized return instead of the original 5-day return
    trades["Future_Return_5D"] = trades["Realized_Return_Pct"]

    return trades

