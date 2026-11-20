### Market Regime Classification – Model Evaluation and Selection

The objective of this stage was to develop a classification model capable of predicting the Canadian market regime over the next five trading days using economic indicators.

The target variable was Market_Regime_5D, which contains three classes:

- **Bullish:** The market is expected to experience positive returns.
- **Bearish:** The market is expected to experience negative returns.
- **Sideways:** The market is expected to remain within the defined neutral return range.

#### Feature and Target Preparation

The economic indicators defined in MARKET_FEATURES were selected as input features, while Market_Regime_5D was used as the target variable.

```
TARGET = "Market_Regime_5D"
X = market_dataset[MARKET_FEATURES].copy()
y = market_dataset[TARGET].copy()
dates = market_dataset["Date"]
```

The dataset was prepared for chronological splitting, with the following proportions:

- 60% for training.
- 20% for validation.
- 20% for testing.

This approach preserves the temporal order of the observations, which is important when working with financial and economic time-series data.

#### Model Evaluation

Four classification approaches were evaluated: Dummy Classifier, Decision Tree, Random Forest, and XGBoost.

The Dummy Classifier served as a baseline, providing a reference for evaluating whether the machine learning models could improve upon a simple majority-class prediction.

| Model         | Accuracy | Balanced Accuracy | Macro F1 |
| ------------- | -------- | ----------------- | -------- |
| Dummy         | 0.5722   | 0.3333            | 0.2426   |
| Decision Tree | 0.4948   | 0.4016            | 0.4010   |
| Random Forest | 0.5186   | 0.3772            | 0.3710   |
| XGBoost       | 0.53     | 0.38              | 0.36     |

The Dummy Classifier achieved the highest accuracy because it primarily predicted the majority class, Sideways. However, it failed to identify Bullish and Bearish market conditions.

Decision Tree achieved the highest Balanced Accuracy and Macro F1 among the evaluated models, indicating a more balanced performance across the three market regimes.

#### Class-Level Performance

The Decision Tree classification report showed the following results:

| Market Regime | Precision | Recall | F1-score | Support |
| ------------- | --------- | ------ | -------- | ------- |
| Bearish       | 0.24      | 0.26   | 0.25     | 207     |
| Bullish       | 0.33      | 0.29   | 0.31     | 368     |
| Sideways      | 0.63      | 0.66   | 0.64     | 769     |

The model performed best when identifying Sideways conditions, while its performance on Bullish and Bearish regimes remained limited.

#### Model Selection

Decision Tree was selected as the final candidate for the Market Regime Prediction component because it achieved the best Balanced Accuracy (0.4016) and Macro F1 (0.4010) among the evaluated models.

Although its overall accuracy was lower than the Dummy baseline, its ability to recognize multiple market regimes made it more suitable for this task than a model that predominantly predicts the majority class.

The results also highlight an important limitation: predicting market regimes from economic indicators is challenging, particularly for the less frequent Bearish class. Therefore, the model's predictions should be treated as an additional market signal rather than highly reliable standalone forecasts.

### Market Regime Classification – Model Evaluation

The economic indicators in MARKET_FEATURES were used to predict the Market_Regime_5D target, which represents Bullish, Bearish, and Sideways market conditions over the next five trading days.

The dataset was prepared for chronological splitting into training (60%), validation (20%), and testing (20%) sets.

Four approaches were evaluated: Dummy Classifier, Decision Tree, Random Forest, and XGBoost.

Decision Tree was selected based on its superior performance in the two metrics that account for class-level balance:

- **Balanced Accuracy:** 0.4016
- **Macro F1:** 0.4010

Although the Dummy Classifier achieved higher overall accuracy (57.22%), it failed to identify the Bullish and Bearish classes. Decision Tree provided a more balanced classification performance.

However, the model still struggles to identify Bearish conditions, and its predictions should be considered supplementary signals rather than highly reliable market forecasts.