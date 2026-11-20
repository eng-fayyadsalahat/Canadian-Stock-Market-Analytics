# OHLC Integrity Audit

## 1. Objective

The OHLC Integrity Audit was conducted to assess the consistency and validity of historical stock price data collected for the ten selected Canadian stocks listed on the Toronto Stock Exchange (TSX).

The purpose was to identify invalid price records, inconsistent Open-High-Low-Close relationships, and invalid trading volume values before proceeding with feature engineering and model development.

## 2. Audit Scope

The audit examined the following price and volume fields:

- Open
- High
- Low
- Close
- Volume

The checks were performed on the cleaned daily stock dataset, which contains 63,574 observations covering ten Canadian stocks.

## 3. Validation Checks

Three main integrity checks were performed.

### A. Positive Price Validation

All OHLC price values were checked to ensure that they were strictly positive.

This validation helps identify invalid records containing zero or negative prices that could affect return calculations, technical indicators, and other price-derived features.

**Result: 0 positive price violations.**

### B. OHLC Consistency Validation

The relationships between the four daily price fields were examined using the following conditions:

- High must be greater than or equal to Open.
- High must be greater than or equal to Close.
- Low must be less than or equal to Open.
- Low must be less than or equal to Close.
- High must be greater than or equal to Low.

These conditions ensure that the daily trading range is internally consistent.

**Result: 0 OHLC inconsistencies.**

### C. Trading Volume Validation

Trading volume values were checked to ensure that no negative volume records existed.

Zero-volume observations were not automatically classified as invalid because they may represent special market conditions or data-provider reporting behavior.

**Result: 0 negative volume records.**

## 4. Audit Results

| Validation Check           | Violations | Status |
| -------------------------- | ---------- | ------ |
| Positive Price Validation  | 0          | Passed |
| OHLC Consistency           | 0          | Passed |
| Negative Volume Validation | 0          | Passed |

All three validation checks passed successfully.

## 5. Interpretation

The results indicate that the cleaned stock dataset contains internally consistent OHLC price records.

No zero or negative prices were detected, and all daily price relationships satisfied the expected OHLC constraints.

Similarly, no negative trading volume values were found.

These results support the reliability of the dataset for subsequent calculations involving daily returns, moving averages, momentum indicators, volatility, and other technical features.

It is important to distinguish between OHLC integrity and broader financial data accuracy. Passing these checks confirms internal consistency, but does not independently prove that every historical price matches an official exchange record.

Corporate actions, historical adjustments, and unusual price movements should therefore be considered separately when interpreting extreme returns.

## 6. Conclusion

The OHLC Integrity Audit passed all validation checks without detecting any violations.

The dataset contains valid positive price values, consistent daily OHLC relationships, and no negative trading volume records.

No additional row removal or price correction was required based on these three checks.

The cleaned stock dataset was therefore considered suitable for proceeding with the next stages of feature engineering and machine learning preparation, subject to the separate review of corporate actions and historical outliers.

# OHLC Integrity Audit – Summary

An OHLC integrity audit was performed on the cleaned Canadian stock dataset containing 63,574 daily observations across ten TSX-listed stocks.

The audit examined three main aspects:

- **Positive Prices:** No zero or negative OHLC price values were detected.
- **OHLC Consistency:** All Open, High, Low, and Close relationships satisfied the expected validation rules.
- **Trading Volume:** No negative volume records were identified.

All validation checks passed successfully:

| Check                     | Violations |
| ------------------------- | ---------- |
| Positive Price Violations | 0          |
| OHLC Inconsistencies      | 0          |
| Negative Volume Records   | 0          |

The results confirmed that the dataset was internally consistent, and no additional corrections or row removals were required based on these checks.

The dataset was considered suitable for subsequent feature engineering and model preparation.