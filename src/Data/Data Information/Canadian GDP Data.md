# Canadian GDP Data Collection and Preparation

## 1. Data Source

The GDP dataset was obtained from Statistics Canada through the Web Data Service (WDS).

- **Source:** [Statistics Canada](https://www150.statcan.gc.ca/t1/wds/rest/getFullTableDownloadCSV/36100434/en)
- **Dataset:** Gross domestic product (GDP) at basic prices, by industry, monthly.
- **Table ID:** 36-10-0434-01
- **Product ID:** 36100434
- **Former CANSIM ID:** 379-0031
- **Frequency:** Monthly
- **Geography:** Canada
- **Original data format:** CSV

The dataset provides monthly GDP estimates for Canada, with multiple dimensions covering geographical areas, seasonal adjustments, price measurements, and industries.

## 2. Data Filtering and Selection

The original dataset contained multiple combinations of dimensions. To obtain a single representative series for the Canadian economy, the following filters were applied:

| Dimension           | Selected Value                      |
| ------------------- | ----------------------------------- |
| Geography           | Canada                              |
| Seasonal Adjustment | Seasonally adjusted at annual rates |
| Prices              | Chained (2017) dollars              |
| Industry            | All industries \[T001\]             |

These selections provide an aggregate measure of Canadian economic activity, rather than GDP for an individual industry.

The resulting dataset was reduced to two columns:

- Date
- GDP_Real_Millions_CAD

The original reference date column was converted to the Pandas datetime format, and the observations were sorted chronologically.

## 3. Data Characteristics

The extracted dataset contains:

| Property           | Result       |
| ------------------ | ------------ |
| Total observations | 356          |
| Number of columns  | 2            |
| Starting date      | January 1997 |
| Ending date        | August 2026  |
| Frequency          | Monthly      |
| Missing values     | 0            |
| Duplicate dates    | 0            |

The dataset contains 356 consecutive monthly observations, with no missing months, missing values, or duplicate dates.

## 4. Descriptive Statistics

The main variable is GDP_Real_Millions_CAD.

| Statistic          | Value     |
| ------------------ | --------- |
| Count              | 356       |
| Mean               | 1,795,460 |
| Standard Deviation | 314,749.6 |
| Minimum            | 1,200,427 |
| 25th Percentile    | 1,557,858 |
| Median             | 1,778,362 |
| 75th Percentile    | 2,051,796 |
| Maximum            | 2,371,788 |

The values represent millions of Canadian dollars measured using chained 2017 prices.

The series therefore provides a real, inflation-adjusted measure of economic activity rather than nominal GDP measured at current prices.

## 5. Economic Relevance to the Project

GDP is an important macroeconomic indicator because it measures changes in economic production and activity.

For the Canadian stock market research project, GDP may help capture the broader economic environment in which publicly listed companies operate.

Potential relationships include:

- Economic growth and corporate revenue.
- Economic contractions and market performance.
- Changes in economic activity and sector performance.
- The relationship between macroeconomic conditions and future stock returns.

GDP is particularly useful as a complementary feature alongside inflation, labour market indicators, interest rates, exchange rates, and commodity prices.

## 6. Potential Feature Engineering

The original GDP series will be preserved. Additional features may be created during the feature engineering stage.

Two potential features are:

- GDP_MoM: Month-over-month percentage change.
- GDP_YoY: Year-over-year percentage change.

These features can help represent the direction and pace of economic growth.

They have not yet been added to the extracted dataset.

## 7. Data Quality and Limitations

The extracted series passed the initial quality checks:

- No missing observations.
- No duplicate dates.
- Correct datetime format.
- Numeric GDP values.
- Continuous monthly coverage.

However, two methodological considerations remain important.

**Publication timing:** The reference date represents the month measured by the GDP estimate, not necessarily the date when the information became publicly available. The actual publication date must be considered when aligning GDP with daily stock prices.

**Data revisions:** Statistics Canada may revise historical GDP estimates. For a realistic historical simulation, the project should consider whether revised historical values introduce information that was not available at the original prediction date. Statistics Canada's real-time historical GDP release table may help address this issue.

## 8. Final Assessment

The Canadian GDP dataset was successfully extracted and validated.

It contains 356 monthly observations covering January 1997 through August 2026, with no missing values or duplicate dates.

The dataset will be retained as a macroeconomic input for the Canadian stock market research project. Feature engineering and integration with daily stock prices will be performed in later stages, with appropriate consideration of publication dates and data availability.

# Canadian GDP Data – Summary

**Source:** Statistics Canada  
**Table:** 36-10-0434-01  
**Product ID:** 36100434  
**Dataset:** Gross domestic product (GDP) at basic prices, by industry, monthly.

### Data Selection

The dataset was filtered using the following criteria:

- Geography: Canada
- Seasonal Adjustment: Seasonally adjusted at annual rates
- Prices: Chained (2017) dollars
- Industry: All industries \[T001\]

The final dataset contains two columns: Date and GDP_Real_Millions_CAD.

### Data Overview

| Property        | Result                |
| --------------- | --------------------- |
| Observations    | 356                   |
| Period          | Jan 1997 – Aug 2026   |
| Frequency       | Monthly               |
| Missing Values  | 0                     |
| Duplicate Dates | 0                     |
| Mean GDP        | 1,795,460 million CAD |
| Minimum GDP     | 1,200,427 million CAD |
| Maximum GDP     | 2,371,788 million CAD |

### Conclusion

The GDP dataset was successfully extracted, filtered, and validated. It provides a monthly, inflation-adjusted measure of Canadian economic activity and will be used as a macroeconomic input in the stock market research project.

Potential future features include month-over-month and year-over-year GDP growth. Publication timing and historical revisions must be considered before integrating the data with daily stock prices.
