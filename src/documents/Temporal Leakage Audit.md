# Temporal Leakage Audit

## 1. Objective

The Temporal Leakage Audit was conducted to verify that financial and macroeconomic features were not assigned to stock records using information from future dates. This is a critical step in ensuring that the machine learning model uses only information that would have been available at the time of prediction.

## 2. Audit Methodology

The audit examined the temporal alignment of three groups of data:

- **Bank of Canada Data:** Daily financial indicators, including the policy rate, 10-year bond yield, and USD/CAD exchange rate.
- **Monthly Macroeconomic Data:** CPI, GDP, labour market indicators, and the Bank of Canada Commodity Price Index (BCPI).
- **Engineered Macroeconomic Features:** Additional features derived from monthly economic indicators, including 12-month changes and growth rates.

The integration process used backward merge_asof operations to associate each stock observation with the most recent eligible economic observation.

For daily Bank of Canada indicators, a maximum matching tolerance of seven days was applied.

For monthly macroeconomic indicators and their engineered features, a temporary three-month availability delay was applied before integration. This was intended to reduce the risk of using unreleased economic information.

## 3. Audit Results

The following checks were performed:

| Audit Check                                | Violations |
| ------------------------------------------ | ---------- |
| Bank of Canada Availability Violations     | 0          |
| Monthly Macro Availability Violations      | 0          |
| Macro Feature Availability Violations      | 0          |
| Macro Reference Date Violations            | 0          |
| Macro Feature Availability Date Mismatches | 0          |

All implemented temporal checks passed without detecting future-date violations.

### Bank Data Age Analysis

The age of matched Bank of Canada observations was also examined.

| Statistic          | Data Age      |
| ------------------ | ------------- |
| Count              | 61,315        |
| Mean               | 0.002675 days |
| Standard Deviation | 0.078679 days |
| Minimum            | 0 days        |
| 25th Percentile    | 0 days        |
| Median             | 0 days        |
| 75th Percentile    | 0 days        |
| Maximum            | 3 days        |

No matched Bank of Canada observation was older than seven days.

A total of 2,259 stock records had no matching Bank availability date, indicating that a daily Bank of Canada observation could not be matched within the specified tolerance.

## 4. Interpretation

The results indicate that the implemented temporal integration logic successfully prevented the use of observations dated after the corresponding stock records.

The backward matching strategy ensured that financial indicators were matched using previously available observations rather than future observations.

Furthermore, the Bank of Canada data-age analysis confirmed that all successfully matched observations were within the defined seven-day tolerance.

However, an important limitation remains regarding monthly macroeconomic data.

The three-month availability delay is a conservative methodological assumption, not a verified record of the actual publication date of each economic indicator. The reference date of a monthly observation does not necessarily represent the date on which that information became publicly available.

Therefore, the absence of temporal violations confirms the correctness of the implemented date-matching rules, but does not independently establish that every monthly observation was historically available on its assigned availability date.

## 5. Conclusion

The Temporal Leakage Audit passed all implemented validation checks:

- No Bank of Canada availability violations were detected.
- No monthly macroeconomic availability violations were detected.
- No engineered macroeconomic feature availability violations were detected.
- No macro reference-date violations were detected.
- All matched daily Bank of Canada observations were within seven days of their corresponding stock dates.

The integration process is therefore temporally consistent under the assumptions currently implemented.

Before final model evaluation and historical backtesting, the assumed three-month macroeconomic delay should be verified against official publication dates or replaced with defensible series-specific publication lags.

This additional verification is necessary to strengthen the project's protection against look-ahead bias.

# Temporal Leakage Audit – Summary

A temporal leakage audit was performed to verify the chronological alignment of daily financial data, monthly macroeconomic indicators, and engineered economic features.

Backward merge_asof operations were used to ensure that stock observations were matched with previously dated economic information. Daily Bank of Canada data was integrated using a seven-day tolerance, while monthly macroeconomic data used a temporary three-month availability delay.

All implemented checks passed:

- Bank availability violations: 0
- Macro availability violations: 0
- Macro feature availability violations: 0
- Macro reference date violations: 0
- Macro availability date mismatches: 0

The matched Bank of Canada observations had a maximum age of three days, with no records exceeding the seven-day tolerance.

Overall, the audit confirmed that the implemented integration rules did not introduce future-date matching. However, the three-month macroeconomic delay remains an assumption that requires verification against official publication dates before final model evaluation and backtesting.