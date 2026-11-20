# Stock Classification – Model Development and Prediction

### 1. Feature and Target Selection

The stock prediction model was developed using a combination of technical, economic, and calendar features, along with the stock ticker as a categorical variable.

The target variable was defined as Future_Outperformance_5D, which indicates whether a stock outperforms the median five-day future return of the selected Canadian stocks.

### 2. Chronological Data Splitting

To preserve the temporal order of financial data and prevent future observations from influencing model training, the dataset was divided chronologically into three subsets:

- **Training Set (60%):** Used to train the classification model.
- **Validation Set (20%):** Used for model evaluation and selection.
- **Test Set (20%):** Reserved for the final evaluation and trading strategy simulation.

A five-trading-day gap was introduced before the validation and test periods to reduce target overlap and potential information leakage caused by the five-day future return calculation.

### 3. Data Preprocessing

A preprocessing pipeline was implemented using ColumnTransformer:

- **Numerical Features:** Missing values were replaced using median imputation. Missing-value indicators were also added to preserve information about originally missing observations.
- **Categorical Features:** The Ticker column was encoded using One-Hot Encoding, with unknown categories handled safely.

The preprocessing operations were integrated into a single Scikit-learn Pipeline to ensure consistent transformations during training and prediction.

### 4. Decision Tree Model Selection

After evaluating and tuning multiple classification models, the Decision Tree Classifier was selected as the preferred model for stock outperformance prediction.

The selected configuration was:

| Hyperparameter    | Value    |
| ----------------- | -------- |
| Criterion         | Gini     |
| Max Depth         | 10       |
| Min Samples Leaf  | 20       |
| Min Samples Split | 100      |
| Class Weight      | Balanced |
| Random State      | 42       |

The model was fitted exclusively on the training dataset, while validation and test datasets were kept separate from the training process.

### 5. Probability Prediction

Instead of relying only on binary class predictions, the model generated the probability that each stock would outperform its peers over the next five trading days.

The probability of class 1 was extracted using predict_proba().

The resulting predictions were stored in two separate DataFrames:

- stock_val_predictions: Validation predictions.
- stock_test_predictions: Test predictions.

Each DataFrame contains:

- Date
- Ticker
- Future_Outperformance_5D
- Stock_Outperformance_Prob

### 6. Role in the Trading Strategy

The predicted probabilities serve as the primary stock-ranking signal for the trading simulation.

For each trading day, stocks can be ranked by their predicted outperformance probabilities, allowing the strategy to select the highest-ranked candidates.

The test predictions are subsequently used to evaluate the trading strategy on unseen data.

### Stock Classification Model Development

A Decision Tree Classifier was developed using technical, economic, and calendar features, with the stock ticker included as a categorical variable. The target variable was Future_Outperformance_5D, representing whether a stock outperforms the median five-day future return of the selected stocks.

The dataset was divided chronologically into training, validation, and test sets using a 60/20/20 split, with a five-trading-day gap to reduce target overlap. Numerical missing values were handled using median imputation with missing-value indicators, while the ticker was encoded using One-Hot Encoding.

After model comparison and hyperparameter tuning, the selected Decision Tree configuration used a maximum depth of 10, a minimum of 20 samples per leaf, and a minimum of 100 samples required for splitting, with balanced class weights.

The model was trained exclusively on the training set and generated outperformance probabilities for the validation and test sets. These probabilities were then used to rank stocks and support the subsequent trading strategy simulations.