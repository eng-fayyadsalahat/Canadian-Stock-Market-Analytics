# Calendar Features – Detailed Report

## 1. Overview

In this stage, calendar-based features were extracted from the Date column of the integrated daily dataset. The objective was to capture potential temporal patterns in stock market behavior, including differences across weekdays, months, and quarters.

## 2. Feature Creation

Seven calendar features were created:

| Feature       | Description                                            |
| ------------- | ------------------------------------------------------ |
| DayOfWeek     | Represents the weekday, from Monday (0) to Friday (4). |
| Month         | Represents the calendar month, from 1 to 12.           |
| Quarter       | Represents the calendar quarter, from 1 to 4.          |
| DayOfWeek_Sin | Sine transformation of the weekday.                    |
| DayOfWeek_Cos | Cosine transformation of the weekday.                  |
| Month_Sin     | Sine transformation of the month.                      |
| Month_Cos     | Cosine transformation of the month.                    |

Cyclical encoding was applied to weekdays and months to preserve their circular relationships and avoid treating the end and beginning of each cycle as distant values.

## 3. Results and Observations

All seven features were successfully generated across 63,574 records, with no missing values.

The weekday distribution was relatively balanced, ranging from 11,647 Monday records to 13,068 Thursday records.

Monthly records were also distributed across all twelve months, ranging from 4,919 in December to 5,551 in March.

The cyclical features remained within their expected range of -1 to 1.

## 4. Conclusion

Calendar feature engineering was completed successfully. These features provide temporal information that may help machine learning models identify weekday patterns, monthly seasonality, and quarterly effects in Canadian stock market data.

The next step is a comprehensive review of all engineered features, including missing values, feature redundancy, data consistency, and potential target leakage before preparing the final modeling dataset.

# Calendar Features – Summary

Created seven calendar features from the Date column, including weekday, month, quarter, and cyclical sine/cosine transformations for weekdays and months.

All 63,574 records were successfully processed with no missing values. Weekday and monthly distributions were relatively balanced, covering all five trading days and twelve calendar months.

**Outcome:** Calendar features were successfully engineered to capture potential temporal patterns and seasonality in Canadian stock market data.