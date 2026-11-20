# Canadian Consumer Price Index (CPI)

## 1. Data Source

The Consumer Price Index (CPI) data was obtained from Statistics Canada through its Web Data Service (WDS).

- **Source:** [Statistics Canada](https://www150.statcan.gc.ca/t1/wds/rest/getFullTableDownloadCSV/18100004/en)
- **Table ID:** 18-10-0004-01
- **Dataset:** Consumer Price Index, monthly, not seasonally adjusted
- **Geographic coverage:** Canada
- **Frequency:** Monthly
- **Historical coverage:** January 1914 – September 2026

The original CSV dataset contained approximately 1,154,918 rows and 15 columns, with a file size of approximately 153.82 MB.

## 2. Data Extraction and Filtering

The original dataset contained CPI observations for multiple geographical regions and product groups.

To obtain a focused dataset suitable for macroeconomic analysis, the following filters were applied:

- GEO = Canada
- Products and product groups = All-items

Only the following columns were retained:

- REF_DATE
- VALUE

The resulting columns were renamed:

- REF_DATE → Date
- VALUE → CPI

The date column was converted into a datetime format, and the observations were sorted chronologically.

## 3. Feature Engineering

An additional feature was created to calculate the annual inflation rate using the year-over-year percentage change in CPI.

The calculation was performed using:

```
cpi_canada["Inflation_YoY"] = (
    cpi_canada["CPI"].pct_change(periods=12) * 100
)
```

This measures the percentage change in the CPI compared with the same month in the previous year.

The resulting dataset contains three columns:

| Column        | Description                     |
| ------------- | ------------------------------- |
| Date          | Monthly reference date          |
| CPI           | All-items Consumer Price Index  |
| Inflation_YoY | Annual percentage change in CPI |

Both CPI and the derived annual inflation rate were retained because they represent different economic information.

## 4. Final Dataset Structure

After filtering and feature engineering, the final dataset contains:

- **Rows:** 1,353
- **Columns:** 3
- **Start date:** January 1914
- **End date:** September 2026
- **Frequency:** Monthly
- **Duplicate dates:** 0

The final dataset is significantly smaller than the original file and contains only the information required for the project's macroeconomic analysis.

## 5. Data Quality Assessment

Several validation checks were performed.

| Validation Check             | Result    |
| ---------------------------- | --------- |
| Total observations           | 1,353     |
| Missing Date values          | 0         |
| Missing CPI values           | 0         |
| Missing Inflation_YoY values | 12        |
| Duplicate dates              | 0         |
| Chronological sorting        | Confirmed |

The 12 missing values in Inflation_YoY correspond to the first 12 observations. This is expected because calculating a year-over-year change requires CPI values from 12 months earlier.

No missing values were found in the original CPI series.

## 6. Descriptive Statistics

The main descriptive statistics are:

| Statistic          | CPI    | Inflation_YoY (%) |
| ------------------ | ------ | ----------------- |
| Count              | 1,353  | 1,341             |
| Mean               | 50.93  | 3.13              |
| Standard Deviation | 48.87  | 4.73              |
| Minimum            | 5.90   | \-17.80           |
| Median             | 20.30  | 2.28              |
| Maximum            | 170.00 | 21.65             |

These statistics summarize the long-term behavior of Canadian consumer prices.

The CPI increased substantially over the historical period, reflecting the long-term change in the general price level.

The inflation rate also shows considerable historical variation, including periods of negative annual inflation and periods of elevated price increases.

For September 2026, the observed values were:

- CPI: 170.0
- Annual inflation rate: approximately 3.09%

## 7. Relevance to the Stock Market Prediction Project

The CPI dataset provides an additional macroeconomic perspective for the Canadian stock market analysis.

Potential uses include:

- Capturing changes in the general price level.
- Measuring inflationary conditions.
- Studying potential relationships between inflation and stock returns.
- Providing macroeconomic context alongside employment, interest rates, bond yields, and exchange rates.

The CPI level and annual inflation rate may provide complementary information to machine learning models.

However, their usefulness will need to be evaluated during feature selection and model validation rather than assumed in advance.

## 8. Data Integration Considerations

The CPI dataset is monthly, whereas stock prices and several Bank of Canada indicators are daily.

Therefore, special attention will be required when integrating these datasets.

In particular:

- Monthly CPI observations must be aligned with daily stock trading dates.
- The reference month must not be confused with the publication date.
- CPI information should only become available to the model from its actual publication date.
- Forward-filling may be considered after the release date, provided that the timing is handled correctly.
- No future observations should be introduced into historical training data.

These precautions are essential to prevent data leakage.

## 9. Output File

The processed dataset is intended to be saved as:

canada_cpi_monthly.csv

The file contains the monthly CPI index and its derived year-over-year inflation rate.

## 10. Completion Status

The following tasks have been completed:

- Retrieved the CPI dataset from Statistics Canada.
- Filtered the data for Canada and the All-items category.
- Selected and renamed the required columns.
- Converted dates into datetime format.
- Sorted observations chronologically.
- Calculated the year-over-year inflation rate.
- Performed data quality checks.
- Reviewed descriptive statistics.
- Prepared the dataset for future integration.

**The CPI data collection and preprocessing stage is complete.** Integration with stock market data, feature selection, model training, and historical strategy simulation remain future project stages.

### Canadian Consumer Price Index (CPI)

Collected monthly Consumer Price Index data from Statistics Canada using Table 18-10-0004-01 (Consumer Price Index, monthly, not seasonally adjusted).

The original dataset contained approximately 1.15 million rows and 15 columns. The data was filtered to retain Canadian observations for the All-items category, keeping only the reference date and CPI value.

A new feature, Inflation_YoY, was calculated using the 12-month percentage change in CPI.

**Final Dataset:**

- 1,353 monthly observations.
- Three columns: Date, CPI, and Inflation_YoY.
- Historical coverage: January 1914 – September 2026.
- No missing CPI values.
- 12 expected missing values in the first 12 inflation observations.
- No duplicate dates.
- Chronologically sorted.

The processed dataset provides historical information about Canadian consumer prices and inflation. It will complement the employment indicators from Statistics Canada and the monetary and financial indicators from the Bank of Canada.

**Output file:** canada_cpi_monthly.csv

Data collection, preprocessing, feature engineering, and initial quality checks have been completed. The dataset is ready for future integration, subject to publication-date alignment to prevent data leakage.
