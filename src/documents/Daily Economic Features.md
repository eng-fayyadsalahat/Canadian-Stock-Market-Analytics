## Daily Economic Features

Three daily economic features were engineered to capture the relationship between Canadian monetary conditions, bond-market expectations, and currency movements.

### 1. Yield Spread

The Yield_Spread feature was calculated as the difference between the 10-year Canadian government bond yield and the Bank of Canada's policy rate.

**Formula:**

Yield_Spread = Bond_Yield_10Y - Policy_Rate

This feature represents the difference between long-term and short-term interest rates and provides information about the yield curve. A higher spread indicates a larger difference between long-term and policy rates, while a negative spread indicates that the 10-year yield is below the policy rate.

**Statistics:**

- Mean: 0.8024
- Standard deviation: 1.1096
- Minimum: -1.94
- Median: 0.94
- Maximum: 3.47

The average positive spread indicates that long-term bond yields were generally higher than the policy rate over the available observations.

### 2. Policy Rate Change (21 Days)

The Policy_Rate_Change_21D feature measures the change in the Bank of Canada's policy rate over 21 observations.

**Formula:**

Policy_Rate_Change_21D = Policy_Rate(t) - Policy_Rate(t-21)

This feature captures recent monetary policy changes and helps represent the direction and magnitude of interest-rate adjustments.

**Statistics:**

- Mean: 0.0098
- Standard deviation: 0.1689
- Minimum: -1.50
- Median: 0.00
- Maximum: 1.00

The median of zero indicates that the policy rate usually remained unchanged over the selected observation window.

**Methodological Note:** The calculation currently uses 21 stock trading observations rather than exactly 21 calendar days. Since Bank of Canada observations are merged into the stock dataset, this definition should be documented or refined using the original unique daily economic series.

### 3. USD/CAD Change (21 Days)

The USD_CAD_Change_21D feature measures the percentage change in the USD/CAD exchange rate over 21 observations.

**Formula:**

USD_CAD_Change_21D = ((USD_CAD(t) / USD_CAD(t-21)) - 1) × 100

This feature captures recent currency movements. An increase in USD/CAD generally indicates that the US dollar has strengthened relative to the Canadian dollar, while a decrease indicates relative Canadian dollar appreciation.

**Statistics:**

- Mean: 0.0676%
- Standard deviation: 1.8255%
- Minimum: -5.7356%
- Median: 0.0592%
- Maximum: 9.5533%

The results indicate that exchange-rate movements varied considerably over the observation period.

### Missing Values Analysis

Missing values were observed in the economic features:

- Yield_Spread: 21,294 missing values.
- Policy_Rate_Change_21D: 21,320 missing values.
- USD_CAD_Change_21D: 39,324 missing values.

These missing values are mainly related to differences in historical data coverage, unavailable source observations, and the initial periods required to calculate 21-observation changes.

No arbitrary values were inserted to replace these missing observations.

**Conclusion:**

The three features provide additional economic context for the machine learning dataset by representing interest-rate differences, monetary policy changes, and currency movements. However, their historical coverage and calculation windows must be considered during feature selection and model evaluation.

## Daily Economic Features – Summary

Three economic features were created using Bank of Canada data:

1. **Yield_Spread:** Measures the difference between the 10-year bond yield and the policy rate. Its mean was 0.8024 percentage points, indicating that long-term yields were generally higher.
2. **Policy_Rate_Change_21D:** Measures the policy-rate change over 21 observations. Its mean was 0.0098, while the median was zero, suggesting that the policy rate frequently remained unchanged.
3. **USD_CAD_Change_21D:** Measures the percentage change in the USD/CAD exchange rate over 21 observations. Its mean was 0.0676%, with a standard deviation of 1.8255%.

Missing values were retained without arbitrary imputation because they mainly reflect differences in historical coverage and the calculation requirements of rolling changes.

**Final Outcome:** Three economic features were added to capture monetary policy, bond-market conditions, and exchange-rate movements.