

from Data import *
from Market_Rigem_Strategy import  * 
from Metric import  *
trade_features = daily_data[
    [
        "Date",
        "Ticker",
        "Future_Return_5D",
        "Close_Momentum_5D"
    ]
].copy()

market_strategy = market_strategy.merge(
    trade_features,
    on=["Date", "Ticker"],
    how="inner",
    validate="one_to_one"
)

INITIAL_INVESTMENT = 100
TOP_N = 3
HOLDING_DAYS = 5
ROUND_TRIP_FEE = 0.002

REGIME_ALLOCATION = {
    "Bullish": 1.0,
    "Sideways": 0.5,
    "Bearish": 0.0
}

def simulate_market_aware_strategy(
    data,
    investment_per_stock=100,
    top_n=3,
    holding_days=5,
    round_trip_fee=0.002,
    regime_allocation=None
):

    if regime_allocation is None:
        regime_allocation = {
            "Bullish": 1.0,
            "Sideways": 0.5,
            "Bearish": 0.0
        }

    required_columns = [
        "Date",
        "Ticker",
        "Stock_Outperformance_Prob",
        "Predicted_Market_Regime",
        "Future_Return_5D",
        "Close_Momentum_5D"
    ]

    missing = set(required_columns) - set(data.columns)

    if missing:
        raise ValueError(f"Missing columns: {missing}")

    trading_dates = sorted(data["Date"].unique())

    exit_dates = {
        date: trading_dates[i + holding_days]
        for i, date in enumerate(trading_dates)
        if i + holding_days < len(trading_dates)
    }

    trades = []

    for date, daily_group in data.groupby("Date", sort=True):

        if date not in exit_dates:
            continue

        regime = daily_group["Predicted_Market_Regime"].iloc[0]

        allocation = regime_allocation.get(regime, 0)

        if allocation <= 0:
            continue

        selected = (
            daily_group
            .sort_values(
                ["Stock_Outperformance_Prob", "Close_Momentum_5D"],
                ascending=[False, False]
            )
            .head(top_n)
            .copy()
        )

        selected["Investment"] = (
            investment_per_stock * allocation
        )

        selected["Gross_Profit"] = (
            selected["Investment"]
            * selected["Future_Return_5D"] / 100
        )

        selected["Fees"] = (
            selected["Investment"] * round_trip_fee
        )

        selected["Net_Profit"] = (
            selected["Gross_Profit"] - selected["Fees"]
        )
        selected["Date"] = date
        selected["Entry_Date"] = date
        selected["Exit_Date"] = exit_dates[date]

        trades.append(selected)

    if not trades:
        return pd.DataFrame(), {}

    trades_df = pd.concat(trades, ignore_index=True)

    total_trades = len(trades_df)
    
    total_profit = trades_df["Net_Profit"].sum()

    win_rate = (
        trades_df["Net_Profit"].gt(0).mean() * 100
    )

    average_profit = trades_df["Net_Profit"].mean()

    total_invested = trades_df["Investment"].sum()

    summary = {
        "Total Trades": total_trades,
        "Total Investment Across Trades ($)": round(total_invested, 2),
        "Total Gross Profit ($)": round(
            trades_df["Gross_Profit"].sum(), 2
        ),
        "Total Fees ($)": round(trades_df["Fees"].sum(), 2),
        "Total Net Profit ($)": round(total_profit, 2),
        "Win Rate (%)": round(win_rate, 2),
        "Average Net Profit per Trade ($)": round(
            average_profit, 4
        )
    }

    return trades_df, summary



def calculate_capital_requirements(trades):

    trades = trades.copy()

    # ------------------------------------------
    # 1. Prepare dates
    # ------------------------------------------

    trades["Entry_Date"] = pd.to_datetime(trades["Entry_Date"])
    trades["Exit_Date"] = pd.to_datetime(trades["Exit_Date"])

    if trades.empty:
        return {
            "Start Date": None,
            "End Date": None,
            "Period (Years)": 0,
            "Total Net Profit ($)": 0,
            "Total Return (%)": 0,
            "CAGR (%)": np.nan,
            "Maximum Open Positions": 0,
            "Required Capital ($)": 0
        }

    # ------------------------------------------
    # 2. Calculate active capital
    # ------------------------------------------

    events = pd.concat([
        trades[["Entry_Date", "Investment"]].rename(
            columns={
                "Entry_Date": "Date",
                "Investment": "Change"
            }
        ),

        trades[["Exit_Date", "Investment"]].rename(
            columns={
                "Exit_Date": "Date",
                "Investment": "Change"
            }
        ).assign(
            Change=lambda x: -x["Change"]
        )
    ])

    daily_events = (
        events.groupby("Date")["Change"]
        .sum()
        .sort_index()
    )

    active_capital = daily_events.cumsum()

    required_capital = active_capital.max()

    # ------------------------------------------
    # 3. Calculate active positions
    # ------------------------------------------

    position_events = pd.concat([
        trades[["Entry_Date"]].rename(
            columns={"Entry_Date": "Date"}
        ).assign(Change=1),

        trades[["Exit_Date"]].rename(
            columns={"Exit_Date": "Date"}
        ).assign(Change=-1)
    ])

    daily_positions = (
        position_events.groupby("Date")["Change"]
        .sum()
        .sort_index()
        .cumsum()
    )

    max_open_positions = daily_positions.max()

    # ------------------------------------------
    # 4. Testing period
    # ------------------------------------------

    start_date = trades["Entry_Date"].min()
    end_date = trades["Exit_Date"].max()

    days = (end_date - start_date).days
    years = days / 365.25

    # ------------------------------------------
    # 5. Performance metrics
    # ------------------------------------------

    total_net_profit = trades["Net_Profit"].sum()

    total_return = (
        (total_net_profit / required_capital) * 100
        if required_capital > 0 else np.nan
    )

    if years > 0 and total_return > -100:
        cagr = (
            (1 + total_return / 100) ** (1 / years) - 1
        ) * 100
    else:
        cagr = np.nan

    # ------------------------------------------
    # 6. Return results
    # ------------------------------------------

    return {
        "Start Date": start_date,
        "End Date": end_date,
        "Period (Years)": round(years, 2),
        "Total Net Profit ($)": round(total_net_profit, 2),
        "Total Return (%)": round(total_return, 2),
        "CAGR (%)": round(cagr, 2),
        "Maximum Open Positions": int(max_open_positions),
        "Required Capital ($)": round(required_capital, 2)
    }



strategy2_trades, strategy2_results = simulate_market_aware_strategy(
    data=market_strategy,
    investment_per_stock=INITIAL_INVESTMENT,
    top_n=TOP_N,
    holding_days=HOLDING_DAYS,
    round_trip_fee=ROUND_TRIP_FEE,
    regime_allocation=REGIME_ALLOCATION
)

vectorized_trades, vectorized_summary = vectorized_simulation(
    strategy2_trades,
    initial_capital=1500
)

trading_dates = dates = sorted(
    daily_data.loc[
        daily_data["Date"].between(
            strategy2_trades["Entry_Date"].min(),
            strategy2_trades["Entry_Date"].max()
        ),
        "Date"
    ].unique()
)


exact_trades, portfolio_s2, exact_summary = exact_simulation(
    strategy2_trades,
    daily_data=daily_data,
    initial_capital=1500,
    max_open_positions=15,
    position_fraction=1 / 15,
    trading_dates=trading_dates
)

portfolio_s2 = portfolio_s2.reset_index()
portfolio_risk_s2, risk_metrics = calculate_risk_metrics(
    portfolio_s2,
    initial_capital=1500
)


stop_loss_trades = apply_stop_loss(
    strategy2_trades,
    daily_data,
    stop_loss_pct=0.03
)

stop_loss_results, stop_loss_portfolio, stop_loss_summary = (
    exact_simulation(
        stop_loss_trades,
        daily_data=daily_data,
        initial_capital=1500,
        max_open_positions=15,
        position_fraction=1 / 15,
        trading_dates=trading_dates
    )
)
stop_loss_portfolio = stop_loss_portfolio.reset_index()
stop_loss_portfolio, stop_loss_risk = calculate_risk_metrics(
    stop_loss_portfolio
)

def run():
    print("Running Market-Aware Strategy...")

    # Merge stock and market predictions
    # Strategy 2
    # Exact simulation
    # Risk metrics

    return {
        "strategy2_results": strategy2_results,
        "strategy2_trades": strategy2_trades,
        "portfolio_s2": portfolio_s2,
        "risk_s2": risk_metrics,
    }