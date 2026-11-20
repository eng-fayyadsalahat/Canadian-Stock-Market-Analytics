### Model Evaluation

The Market Regime Classification models were evaluated to determine how effectively they predict the three Canadian market conditions: **Bearish, Bullish, and Sideways**.

The evaluation included examining class distributions across the training, validation, and test datasets, comparing multiple classification models, and using a Dummy Classifier as a baseline.

#### 1. Target Distribution Analysis

The distribution of Market_Regime_5D was examined across the three datasets.

| Market Regime | Training | Validation | Test  |
| ------------- | -------- | ---------- | ----- |
| Bearish       | 26.1%    | 15.4%      | 21.3% |
| Bullish       | 34.2%    | 27.4%      | 32.8% |
| Sideways      | 39.7%    | 57.2%      | 45.9% |

The results show an imbalance among the three market regimes, with Sideways being the most frequent class in all datasets.

However, the class proportions differ across the chronological splits. In particular, Sideways represents 57.2% of the validation data, compared with 39.7% in training. This variation indicates changes in market regime distribution over time and makes model evaluation more challenging.

#### 2. Baseline Model – Dummy Classifier

A Dummy Classifier was used as a baseline to establish the performance of a simple model that predicts the most frequent class.

| Metric            | Dummy  |
| ----------------- | ------ |
| Accuracy          | 0.5722 |
| Balanced Accuracy | 0.3333 |
| Macro F1          | 0.2426 |

The Dummy Classifier achieved 57.22% accuracy by predicting Sideways for every observation.

However, it completely failed to identify Bearish and Bullish conditions, resulting in zero precision, recall, and F1-score for both classes.

This demonstrates why accuracy alone is insufficient for evaluating this imbalanced multi-class classification problem.

#### 3. Model Comparison

Three classification models were evaluated:

- Decision Tree
- Random Forest
- XGBoost

Their performance was compared using Accuracy, Balanced Accuracy, and Macro F1.

| Model         | Accuracy   | Balanced Accuracy | Macro F1   |
| ------------- | ---------- | ----------------- | ---------- |
| Decision Tree | 0.4948     | **0.4016**        | **0.4010** |
| Random Forest | **0.5186** | 0.3772            | 0.3710     |
| Dummy         | 0.5722     | 0.3333            | 0.2426     |

The results show different strengths across the models:

- **Decision Tree:** Achieved the highest Balanced Accuracy and Macro F1, indicating the best overall balance across the three classes.
- **Random Forest:** Achieved higher Accuracy than Decision Tree but lower Balanced Accuracy and Macro F1.
- **Dummy:** Achieved the highest Accuracy but failed to recognize two of the three classes.

#### 4. Class-Level Performance

The classification reports provide further insight into the models' ability to recognize individual market regimes.

**Decision Tree:**

| Class    | Precision | Recall | F1-score |
| -------- | --------- | ------ | -------- |
| Bearish  | 0.24      | 0.26   | 0.25     |
| Bullish  | 0.33      | 0.29   | 0.31     |
| Sideways | 0.63      | 0.66   | 0.64     |

The Decision Tree performed best on the Sideways class, while its performance on Bearish and Bullish remained relatively weak.

**Random Forest:**

| Class    | Precision | Recall | F1-score |
| -------- | --------- | ------ | -------- |
| Bearish  | 0.10      | 0.06   | 0.07     |
| Bullish  | 0.40      | 0.35   | 0.37     |
| Sideways | 0.62      | 0.72   | 0.67     |

Random Forest achieved better performance on Bullish and Sideways than on Bearish. Its recall for Bearish was particularly low at 0.06.

**XGBoost:**

| Class    | Precision | Recall | F1-score |
| -------- | --------- | ------ | -------- |
| Bearish  | 0.11      | 0.04   | 0.06     |
| Bullish  | 0.35      | 0.46   | 0.40     |
| Sideways | 0.63      | 0.64   | 0.63     |

XGBoost achieved the highest recall for Bullish among the three evaluated models, but its ability to recognize Bearish conditions was limited.

#### 5. Final Model Selection

The Decision Tree was selected as the final model for Strategy 2.

Although Random Forest achieved higher Accuracy (51.86%), Decision Tree achieved the best Balanced Accuracy (40.16%) and Macro F1 (40.10%).

These metrics were prioritized because the project requires predictions across all three market regimes rather than favoring the most frequent class.

The selected model therefore provides the strongest overall balance among the evaluated candidates, although its classification performance remains modest.

#### 6. Evaluation Conclusion

The evaluation highlights several challenges in predicting future market regimes:

- The target classes are imbalanced.
- Their distributions vary across chronological datasets.
- Sideways conditions are easier to identify than Bearish conditions.
- All evaluated models struggle to recognize Bearish market conditions.
- Accuracy alone can be misleading, as demonstrated by the Dummy Classifier.

The Decision Tree was retained for Strategy 2 based on its Balanced Accuracy and Macro F1 performance. Its predictions are intended to serve as an additional market-level signal alongside stock outperformance probabilities.

However, the results do not indicate strong market regime prediction capability. The impact of incorporating this signal must therefore be assessed through the subsequent trading simulation.

### Market Regime Model Evaluation

The target distribution was examined across the training, validation, and test datasets. Sideways was the most frequent class in all three datasets, representing 39.7%, 57.2%, and 45.9%, respectively. The differences in class proportions indicate variation in market regime distribution across chronological periods.

Three classification models were evaluated: Decision Tree, Random Forest, and XGBoost. A Dummy Classifier was also used as a baseline.

| Model         | Accuracy | Balanced Accuracy | Macro F1   |
| ------------- | -------- | ----------------- | ---------- |
| Decision Tree | 0.4948   | **0.4016**        | **0.4010** |
| Random Forest | 0.5186   | 0.3772            | 0.3710     |
| Dummy         | 0.5722   | 0.3333            | 0.2426     |

The Dummy Classifier achieved the highest Accuracy by predicting only the majority class, Sideways, while completely failing to identify Bearish and Bullish conditions.

Decision Tree achieved the highest Balanced Accuracy and Macro F1, demonstrating the best overall balance across the three market regimes. Random Forest achieved higher Accuracy, while XGBoost showed better recall for Bullish conditions.

**Decision Tree was selected as the final model for Strategy 2**, prioritizing balanced performance across all classes rather than overall Accuracy.

Nevertheless, all models showed limited performance, particularly in identifying Bearish conditions. Therefore, the selected model's practical value will be further assessed through the trading simulation.