## Stock Ranking Evaluation

After training the three classification models (Decision Tree, Random Forest, and XGBoost), their ability to rank stocks based on their predicted outperformance probabilities was evaluated.

Rather than relying only on traditional classification metrics, two ranking-oriented evaluation metrics were used: **Spearman Rank Correlation** and **Precision@3**.

### 1. Spearman Rank Correlation

Spearman correlation measures the relationship between the predicted stock ranking and the actual future outperformance ranking. A higher positive value indicates better agreement between the model's ranking and the actual stock performance.

The evaluation results were:

| Model         | Mean Spearman | Median Spearman | Positive Rank Correlation | Valid Days |
| ------------- | ------------- | --------------- | ------------------------- | ---------- |
| Decision Tree | 0.0368        | 0.0605          | 54.03%                    | 1,005      |
| XGBoost       | 0.0276        | 0.0424          | 54.33%                    | 1,005      |
| Random Forest | 0.0193        | 0.0182          | 51.54%                    | 1,005      |

**Interpretation:**

- Decision Tree achieved the highest mean and median Spearman correlation, indicating the strongest ranking performance among the three models.
- XGBoost achieved the highest percentage of days with positive rank correlation (54.33%), although its average correlation was lower than Decision Tree.
- Random Forest produced the weakest ranking correlation, with a mean of 0.0193.

However, all three models showed weak positive rank correlations, suggesting that their ability to reproduce the actual stock ranking remains limited.

### 2. Precision@3

Precision@3 evaluates how effectively each model identifies the three stocks most likely to outperform the others on each trading day.

The results were:

| Model                     | Precision@3 |
| ------------------------- | ----------- |
| Decision Tree             | 0.3473      |
| Random Forest             | 0.3469      |
| XGBoost                   | 0.3449      |
| Random Selection Baseline | 0.3000      |

**Interpretation:**

- Decision Tree achieved the highest Precision@3 of 34.73%.
- Random Forest followed very closely with 34.69%.
- XGBoost achieved 34.49%.
- All three models performed slightly better than the expected random selection baseline of 30%.

The small differences between the models indicate that none demonstrated a substantial advantage in selecting the top three outperforming stocks.

### 3. Overall Conclusion

Based on both ranking metrics, Decision Tree was selected as the strongest candidate for the stock selection strategy.

It achieved the highest mean Spearman correlation and Precision@3, suggesting a relatively better ability to rank and select outperforming stocks.

Nevertheless, the results indicate that the predictive ranking capability of all three models is limited. Their Precision@3 improvements over random selection are relatively small, and their Spearman correlations remain close to zero.

Therefore, Decision Tree was retained as the preferred model for the subsequent trading simulation, while its predictive limitations were taken into consideration when evaluating the strategy's financial performance.

### Stock Ranking Evaluation

Three classification models (Decision Tree, Random Forest, and XGBoost) were evaluated using Spearman Rank Correlation and Precision@3 to assess their ability to identify stocks with higher future outperformance probabilities.

Decision Tree achieved the best overall results, with a mean Spearman correlation of 0.0368 and Precision@3 of 34.73%. Random Forest achieved a Precision@3 of 34.69%, while XGBoost achieved 34.49%.

All models slightly outperformed the random selection baseline of 30%. However, the low Spearman correlation values indicate limited ranking ability.

Based on these results, Decision Tree was selected as the preferred candidate for the trading strategy, while acknowledging the relatively modest predictive performance.