from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.tree import DecisionTreeClassifier


from Data import *
from Metric import *


# Original stock features
STOCK_FEATURES = TECHNICAL + ECONOMIC + CALENDAR + ["Ticker"]

STOCK_TARGET = "Future_Outperformance_5D"

stock_data = (
    daily_data
    .dropna(subset=[STOCK_TARGET])
    .sort_values(["Date", "Ticker"])
    .copy()
)

unique_dates = sorted(stock_data["Date"].unique())

n_dates = len(unique_dates)
train_end = int(n_dates * 0.60)
val_end = int(n_dates * 0.80)

train_dates = unique_dates[:train_end - 5]
val_dates = unique_dates[train_end:val_end - 5]
test_dates = unique_dates[val_end:]

train_mask = stock_data["Date"].isin(train_dates)
val_mask = stock_data["Date"].isin(val_dates)
test_mask = stock_data["Date"].isin(test_dates)

X_stock_train = stock_data.loc[train_mask, STOCK_FEATURES]
y_stock_train = stock_data.loc[train_mask, STOCK_TARGET]

X_stock_val = stock_data.loc[val_mask, STOCK_FEATURES]
y_stock_val = stock_data.loc[val_mask, STOCK_TARGET]

X_stock_test = stock_data.loc[test_mask, STOCK_FEATURES]
y_stock_test = stock_data.loc[test_mask, STOCK_TARGET]





def stock_train(X_stock_train, y_stock_train, X_stock_val, y_stock_val, X_stock_test, y_stock_test):
    # Preprocessing
    stock_preprocessor = ColumnTransformer(
        transformers=[
            (
                "num",
                SimpleImputer(
                    strategy="median",
                    add_indicator=True,
                    keep_empty_features=True
                ),
                TECHNICAL + ECONOMIC + CALENDAR
            ),
            (
                "cat",
                OneHotEncoder(handle_unknown="ignore"),
                ["Ticker"]
            )
        ]
    )

    # Best tuned Decision Tree
    stock_model = Pipeline([
        ("preprocessor", stock_preprocessor),
        ("model", DecisionTreeClassifier(
            criterion="gini",
            max_depth=10,
            min_samples_leaf=20,
            min_samples_split=100,
            class_weight="balanced",
            random_state=42
        ))
    ])

    # Train only
    stock_model.fit(X_stock_train, y_stock_train)

    # Probability of outperforming
    positive_class_index = list(
        stock_model.named_steps["model"].classes_
    ).index(1)

    val_probabilities = stock_model.predict_proba(X_stock_val)[:, positive_class_index]
    test_probabilities = stock_model.predict_proba(X_stock_test)[:, positive_class_index]

    # Save predictions with their dates and tickers
    stock_val_predictions = stock_data.loc[
        val_mask, ["Date", "Ticker", STOCK_TARGET]
    ].copy()

    stock_val_predictions["Stock_Outperformance_Prob"] = val_probabilities

    stock_test_predictions = stock_data.loc[
        test_mask, ["Date", "Ticker", STOCK_TARGET]
    ].copy()

    stock_test_predictions["Stock_Outperformance_Prob"] = test_probabilities


    return stock_test_predictions






# ==========================================
# Strategy 1: Top 3 Stocks - 5 Trading Days
# ==========================================

def strategy_stock_trading(
    stock_test_predictions,
    daily_data,
    INITIAL_INVESTMENT = 100,
    TOP_N = 3,
     HOLDING_DAYS = 5,
     ROUND_TRIP_FEE = 0.002
     ):
    
    # ------------------------------------------
    # 1. Prepare future returns and exit dates
    # ------------------------------------------

    exit_data = daily_data[
        ["Date", "Ticker", "Future_Return_5D",
        "Close_Momentum_5D"]
    ].sort_values(["Ticker", "Date"]).copy()

    exit_data["Exit_Date"] = (
        exit_data.groupby("Ticker")["Date"].shift(-HOLDING_DAYS)
    )

    # ------------------------------------------
    # 2. Merge predictions with actual returns
    # ------------------------------------------

    simulation_data = stock_test_predictions.merge(
        exit_data,
        on=["Date", "Ticker"],
        how="inner",
        validate="one_to_one"
    )

    simulation_data = simulation_data.dropna(
        subset=[
            "Stock_Outperformance_Prob",
            "Future_Return_5D",
            "Exit_Date"
        ]
    )

    # ------------------------------------------
    # 3. Select Top 3 stocks per trading day
    # ------------------------------------------

    selected_trades = (
        simulation_data
        .sort_values(
            ["Date", "Stock_Outperformance_Prob", "Close_Momentum_5D"],
            ascending=[True, False, False]
        )
        .groupby("Date")
        .head(TOP_N)
        .copy()
    )

    # ------------------------------------------
    # 4. Calculate financial results
    # ------------------------------------------

    selected_trades["Investment"] = INITIAL_INVESTMENT

    selected_trades["Gross_Profit"] = (
        INITIAL_INVESTMENT *
        selected_trades["Future_Return_5D"] / 100
    )

    selected_trades["Fees"] = (
        INITIAL_INVESTMENT * ROUND_TRIP_FEE
    )

    selected_trades["Net_Profit"] = (
        selected_trades["Gross_Profit"] -
        selected_trades["Fees"]
    )

    # ------------------------------------------
    # 5. Calculate investment statistics
    # ------------------------------------------

    total_trades = len(selected_trades)

    gross_profit = selected_trades["Gross_Profit"].sum()
    total_fees = selected_trades["Fees"].sum()
    net_profit = selected_trades["Net_Profit"].sum()

    average_profit_per_trade = (
        net_profit / total_trades
        if total_trades > 0 else 0
    )

    win_rate = (
        (selected_trades["Net_Profit"] > 0).mean()
        if total_trades > 0 else 0
    )

    # ------------------------------------------
    # 6. Calculate required capital
    # ------------------------------------------

    events = pd.concat([
        selected_trades[["Date"]].rename(
            columns={"Date": "Event_Date"}
        ).assign(Change=1),

        selected_trades[["Exit_Date"]].rename(
            columns={"Exit_Date": "Event_Date"}
        ).assign(Change=-1)
    ])

    daily_positions = (
        events.groupby("Event_Date")["Change"]
        .sum()
        .sort_index()
        .cumsum()
    )

    selected_trades["Entry_Date"] = selected_trades["Date"]

    selected_trades["Entry_Date"] = pd.to_datetime(
        selected_trades["Entry_Date"]
    )
    
    max_open_positions = daily_positions.max()

    required_capital = (
        max_open_positions * INITIAL_INVESTMENT
    )

    # ------------------------------------------
    # 7. Calculate daily portfolio equity
    # ------------------------------------------

    daily_profit = (
        selected_trades.groupby("Exit_Date")["Net_Profit"]
        .sum()
    )

    trading_dates = (
        daily_data.loc[
            (daily_data["Date"] >= selected_trades["Date"].min()) &
            (daily_data["Date"] <= selected_trades["Exit_Date"].max()),
            "Date"
        ]
        .drop_duplicates()
        .sort_values()
    )

    equity = (
        daily_profit
        .reindex(trading_dates, fill_value=0)
        .cumsum()
        + required_capital
    )

    equity = equity.rename("Portfolio_Value")

    # ------------------------------------------
    # 8. Calculate CAGR and Maximum Drawdown
    # ------------------------------------------

    if len(equity) > 1:
        duration_days = (
            equity.index[-1] - equity.index[0]
        ).days

        final_value = equity.iloc[-1]

        if required_capital > 0 and final_value > 0:
            cagr = (
                (final_value / required_capital)
                ** (365.25 / duration_days)
            ) - 1
        else:
            cagr = np.nan

        drawdown = equity / equity.cummax() - 1
        max_drawdown = drawdown.min()

    else:
        final_value = required_capital
        cagr = np.nan
        max_drawdown = np.nan

    start_date = selected_trades["Date"].min()
    end_date = selected_trades["Exit_Date"].max()

    years = (end_date - start_date).days / 365.25

    total_return = (
        net_profit / required_capital * 100
        if required_capital > 0 else np.nan
        )

    cagr = (
        ((1 + total_return / 100) ** (1 / years) - 1) * 100
        if years > 0 and total_return > -100
        else np.nan
        )

    
    # ------------------------------------------
    # 9. Final results
    # ------------------------------------------

    
    strategy_results = pd.DataFrame([{
        "Strategy": "Top 3 Stocks",
        "Total_Trades": total_trades,
        "Gross_Profit": gross_profit,
        "Total_Fees": total_fees,
        "Net_Profit": net_profit,
        "Average_Profit_Per_Trade": average_profit_per_trade,
        "Win_Rate": win_rate,
        "Max_Open_Positions": max_open_positions,
        "Required_Capital": required_capital,
        "Final_Portfolio_Value": final_value,
        "CAGR": cagr,
        "Maximum_Drawdown": max_drawdown,
        "Entry_Date": start_date,
        "Exit_Date": end_date,
        "Testing_Period_Years": years,
        "Total_Return": total_return,
    }])

    # ------------------------------------------
    # 10. Latest Selected Trades
    # ------------------------------------------

    latest_trades = (
        selected_trades[
            selected_trades["Date"].isin(
                simulation_data["Date"]
                .drop_duplicates()
                .sort_values()
                .head(5)
            )
        ][
            [
                "Date",
                "Entry_Date",
                "Exit_Date",
                "Ticker",
                "Stock_Outperformance_Prob",
                "Close_Momentum_5D",
                "Future_Return_5D",
                "Net_Profit",
                "Gross_Profit",
                "Fees",
                "Investment"
            ]
        ]
        .sort_values(["Date", "Stock_Outperformance_Prob"], ascending=[True, False])
        .reset_index(drop=True)
    )

    # ------------------------------------------
    # 11. Return Results
    # ------------------------------------------

    return strategy_results, selected_trades, latest_trades,  simulation_data

stock_test_predictions = stock_train(X_stock_train, y_stock_train, X_stock_val, y_stock_val, X_stock_test, y_stock_test)
strategy_results, strategy1_trades,latest_trades, simulation_data = strategy_stock_trading(
    stock_test_predictions,
    daily_data
)

vectorized_trades, vectorized_summary = vectorized_simulation(
    strategy1_trades,
    initial_capital=1500
)

start_date = strategy1_trades["Entry_Date"].min()
end_date = strategy1_trades["Exit_Date"].max()

trading_dates = sorted(
    daily_data.loc[
        daily_data["Date"].between(start_date, end_date),
        "Date"
    ].unique()
)

exact_trades, portfolio_s1, exact_summary = exact_simulation(
    strategy1_trades,
    daily_data=daily_data,
    initial_capital=1500,
    max_open_positions=15,
    position_fraction=1 / 15,
    trading_dates=trading_dates
)
portfolio_s1 = portfolio_s1.reset_index()
portfolio_risk_s1, risk_metrics = calculate_risk_metrics(
    portfolio_s1,
    initial_capital=1500
)

stop_loss_trades = apply_stop_loss(
    strategy1_trades,
    daily_data,
    stop_loss_pct=0.03
)


stop_loss_results, stop_loss_portfolio_s1, stop_loss_summary = (
    exact_simulation(
        stop_loss_trades,
        daily_data=daily_data,
        initial_capital=1500,
        max_open_positions=15,
        position_fraction=1 / 15,
        trading_dates=trading_dates
    )
)
stop_loss_portfolio_s1 = stop_loss_portfolio_s1.reset_index()
stop_loss_portfolio_risk_s1, stop_loss_risk = calculate_risk_metrics(
    stop_loss_portfolio_s1
)
def run():
    print("Running Strategy 1...")

    # Strategy 1 code
    # Stock selection
    # Exact simulation
    # Risk metrics

    return {
        "strategy1_results": strategy_results,
        "strategy1_trades": strategy1_trades,
        "portfolio_s1": portfolio_s1,
        "risk_s1": risk_metrics
    }
