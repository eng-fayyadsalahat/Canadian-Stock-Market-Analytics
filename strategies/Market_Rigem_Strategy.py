
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.tree import DecisionTreeClassifier

from Data import *
from Strategy1_Stock_Trade import stock_test_predictions

TARGET = "Market_Regime_5D"

MARKET_FEATURES = ECONOMIC + CALENDAR


X = market_dataset[MARKET_FEATURES].copy()
y = market_dataset[TARGET].copy()

dates = market_dataset["Date"]

n = len(market_dataset)
train_end = int(n * 0.60)
val_end = int(n * 0.80)

# 5-day purge gap
X_market_train = X.iloc[:train_end - 5]
y_market_train = y.iloc[:train_end - 5]

X_market_val = X.iloc[train_end:val_end - 5]
y_market_val = y.iloc[train_end:val_end - 5]

X_market_test = X.iloc[val_end:]
y_market_test = y.iloc[val_end:]




MARKET_MODEL_FEATURES = [
    col for col in MARKET_FEATURES
    if col not in [
        "USD_CAD",
        "USD_CAD_Change_21D"
    ]
]

X_train_model = X_market_train[MARKET_MODEL_FEATURES]
X_val_model = X_market_val[MARKET_MODEL_FEATURES]
X_test_model = X_market_test[MARKET_MODEL_FEATURES]





def market_rigem_train(X_train_model, y_market_train, X_val_model, y_market_val, X_test_model, y_market_test):
    # Preprocessing
    market_model = Pipeline([
        (
            "imputer",
            SimpleImputer(
                strategy="median",
                add_indicator=True,
                keep_empty_features=True
            )
        ),
        (
            "model",
            DecisionTreeClassifier(
                max_depth=5,
                min_samples_leaf=30,
                class_weight="balanced",
                random_state=42
            )
        )
    ])

    # Train only
    market_model.fit(X_train_model, y_market_train)

    # Predict probabilities
    market_val_probabilities = market_model.predict_proba(X_val_model)
    market_test_probabilities = market_model.predict_proba(X_test_model)

    # Save validation predictions
    market_val_predictions = market_dataset.iloc[
        train_end:val_end - 5
    ][["Date", TARGET]].copy()

    for i, class_name in enumerate(
        market_model.named_steps["model"].classes_
    ):
        market_val_predictions[f"Prob_{class_name}"] = (
            market_val_probabilities[:, i]
        )


    # Save test predictions
    market_test_predictions = market_dataset.iloc[
        val_end:
    ][["Date", TARGET]].copy()

    for i, class_name in enumerate(
        market_model.named_steps["model"].classes_
    ):
        market_test_predictions[f"Prob_{class_name}"] = (
            market_test_probabilities[:, i]
        )
    return market_test_predictions





def market_rigime_strategy(market_test_predictions, stock_test_predictions):

    # 1. Select market regime prediction columns
    market_prob_cols = [
        "Prob_Bearish",
        "Prob_Bullish",
        "Prob_Sideways"
    ]

    market_signal = market_test_predictions[
        ["Date"] + market_prob_cols
    ].copy()

    # 2. Determine the predicted market regime
    market_signal["Predicted_Market_Regime"] = (
        market_signal[market_prob_cols]
        .idxmax(axis=1)
        .str.replace("Prob_", "", regex=False)
    )

    # 3. Merge market predictions with stock predictions
    strategy2_data = stock_test_predictions.merge(
        market_signal,
        on="Date",
        how="inner",
        validate="many_to_one"
    )

    # 4. Sort the combined dataset
    strategy2_data = (
        strategy2_data
        .sort_values(["Date", "Ticker"])
        .reset_index(drop=True)
    )
    return strategy2_data

market_test_predictions = market_rigem_train(X_train_model, y_market_train, X_val_model, y_market_val, X_test_model, y_market_test)

market_strategy = market_rigime_strategy(market_test_predictions, stock_test_predictions)

def run():
    print("Running Market Regime Model...")

    # Market Regime predictions
    # Model evaluation

    return {
        "market_predictions": market_strategy,
        "market_results": market_strategy.head(10)
    }