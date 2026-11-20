### Market Regime Classification Model Development

A Decision Tree Classifier was developed to predict the Canadian stock market's future regime over the next five trading days. The model uses economic indicators as input features and classifies the market into three categories: **Bearish, Bullish, and Sideways**.

#### 1. Data Preprocessing

A preprocessing pipeline was implemented using SimpleImputer to handle missing numerical values.

The imputer uses the following configuration:

- **strategy="median":** Replaces missing values with the median of each feature.
- **add_indicator=True:** Adds binary indicators to identify missing values.
- **keep_empty_features=True:** Preserves features that contain only missing values during fitting.

This preprocessing step is integrated into the model pipeline to ensure consistent treatment of missing values during training and prediction.

#### 2. Model Configuration

A DecisionTreeClassifier was selected with the following parameters:

| Parameter        | Value    |
| ---------------- | -------- |
| max_depth        | 5        |
| min_samples_leaf | 30       |
| class_weight     | balanced |
| random_state     | 42       |

The maximum depth limits tree complexity, while the minimum leaf size helps reduce overfitting. Balanced class weights are used to account for potential differences in the distribution of market regime classes.

#### 3. Model Training

The complete pipeline was fitted using only the training dataset:

market_model.fit(X_train_model, y_market_train)

The validation and test datasets were kept separate from the training process and used for generating predictions.

#### 4. Probability Predictions

Instead of relying only on predicted class labels, the model uses predict_proba() to estimate the probability of each market regime.

Predictions were generated separately for:

- **Validation set:** market_val_probabilities
- **Test set:** market_test_probabilities

The resulting probabilities were associated with their corresponding market regime classes.

#### 5. Prediction Results

The validation predictions were stored in market_val_predictions, while test predictions were stored in market_test_predictions.

Each prediction dataset contains:

- **Date:** The corresponding trading date.
- **Market_Regime_5D:** The actual market regime label.
- **Prob_Bearish:** Predicted probability of a Bearish market.
- **Prob_Bullish:** Predicted probability of a Bullish market.
- **Prob_Sideways:** Predicted probability of a Sideways market.

An example of the validation predictions:

| Date       | Actual Regime | Bearish Probability | Bullish Probability | Sideways Probability |
| ---------- | ------------- | ------------------- | ------------------- | -------------------- |
| 2016-02-08 | Sideways      | 0.3626              | 0.3648              | 0.2726               |
| 2016-02-09 | Bullish       | 0.3626              | 0.3648              | 0.2726               |
| 2016-02-10 | Bullish       | 0.3626              | 0.3648              | 0.2726               |

The predicted probabilities represent the model's estimated confidence in each market regime. Identical probabilities across consecutive dates can occur when observations are assigned to the same terminal leaf of the Decision Tree.

#### 6. Role in Strategy 2

The predicted market regime probabilities provide an additional market-level signal for the trading strategy. They can be combined with stock-level outperformance probabilities to evaluate whether market conditions can improve stock selection and trading decisions.

This approach allows Strategy 2 to incorporate both individual stock predictions and broader Canadian market conditions.

### Market Regime Classification

A Decision Tree Classifier was developed to predict the Canadian market regime over the next five trading days, classifying market conditions into **Bearish, Bullish, and Sideways**.

A preprocessing pipeline using SimpleImputer was applied to handle missing numerical values through median imputation, while also adding missing-value indicators and preserving empty features.

The model was configured with max_depth=5, min_samples_leaf=30, class_weight="balanced", and random_state=42.

The pipeline was trained exclusively on the training dataset. Subsequently, predict_proba() was used to generate class probabilities for the validation and test datasets.

The resulting prediction datasets contain the trading date, actual market regime, and predicted probabilities for each of the three classes.

These probabilities provide a market-level signal that can be combined with stock outperformance predictions in Strategy 2 to evaluate the impact of market conditions on trading decisions.