# Canadian Labour Market 

## Part 1: Detailed Technical Report

### 1. Project Overview

As part of the Canadian Stock Market Analysis and Machine Learning project, we started collecting macroeconomic data to complement historical stock market data.

The objective of this stage was to collect, process, and prepare Canadian labour market indicators that could potentially help explain economic conditions and their relationship with future stock market returns.

We selected Statistics Canada as the primary source for labour market data.

### 2. Data Source

We used the following official dataset:

- **Source:** [Statistics Canada](https://www150.statcan.gc.ca/t1/wds/rest/getFullTableDownloadCSV/14100287/en)
- **Dataset:** Labour force characteristics, monthly, seasonally adjusted and trend-cycle.
- **Table ID:** 14-10-0287 (14100287).
- **Frequency:** Monthly.
- **Geographical Coverage:** Canada.
- **Time Period:** January 1976 – October 2026.

The data was downloaded through the Statistics Canada Web Data Service (WDS), using the getFullTableDownloadCSV function.

The downloaded CSV file was approximately 1.2 GB in size. An additional metadata file was also downloaded to understand the dataset structure, dimensions, and available classifications.

### 3. Understanding the Dataset Structure

Before processing the data, we examined the metadata file to understand the available dimensions and their possible values.

The dataset contains six main dimensions:

1. Geography
2. Labour force characteristics
3. Gender
4. Age group
5. Statistics
6. Data type

After examining these dimensions, we selected the appropriate values based on the project's objectives.

### 4. Data Selection and Filtering

Instead of using the entire dataset, we focused on extracting relevant national-level labour market indicators.

The following filtering criteria were applied:

| Dimension  | Selected Value      |
| ---------- | ------------------- |
| Geography  | Canada              |
| Gender     | Total - Gender      |
| Age Group  | 15 years and over   |
| Statistics | Estimate            |
| Data Type  | Seasonally adjusted |

We extracted four main economic indicators:

| Indicator          | Description                                                    |
| ------------------ | -------------------------------------------------------------- |
| Employment         | Total number of employed people                                |
| Labour force       | Total labour force                                             |
| Unemployment rate  | Percentage of the labour force that is unemployed              |
| Participation rate | Percentage of the population participating in the labour force |

**Why Seasonally Adjusted Data?**

We selected seasonally adjusted data to reduce the influence of recurring seasonal patterns on economic indicators. This makes comparisons across different months more suitable for analysing underlying economic changes.

### 5. Memory-Efficient Data Processing

Since the original CSV file was approximately 1.2 GB, loading the entire dataset into memory was unnecessary.

Instead, we used Pandas with chunk-based processing:

```
pd.read_csv(
    file_path,
    usecols=usecols,
    chunksize=200_000
)
```

This approach allowed us to read and process the dataset in batches of 200,000 rows.

For each batch, we applied the selected filtering conditions and retained only the relevant observations.

**Processing Results:**

- Processed the original dataset in multiple batches.
- Retained only 2,440 rows after filtering.
- Significantly reduced the dataset size.
- Avoided loading the entire original file into memory.

### 6. Data Transformation

Initially, the extracted data was structured in Long Format, where each row represented a separate economic indicator for a particular month.

For example:

| REF_DATE | Labour force characteristics | VALUE   |
| -------- | ---------------------------- | ------- |
| 1976-01  | Labour force                 | 10369.7 |
| 1976-01  | Employment                   | 9636.7  |
| 1976-01  | Unemployment rate            | 7.1     |
| 1976-01  | Participation rate           | 61.5    |

We used Pandas pivot_table() to transform the dataset into Wide Format, where each month represents one row and each economic indicator has its own column.

We also converted the date column from the YYYY-MM format into the datetime64 data type and sorted the observations chronologically.

The resulting structure was:

| Date       | Employment | Labour force | Participation rate | Unemployment rate |
| ---------- | ---------- | ------------ | ------------------ | ----------------- |
| 1976-01-01 | 9636.7     | 10369.7      | 61.5               | 7.1               |
| 1976-02-01 | 9659.8     | 10389.8      | 61.5               | 7.0               |
| 1976-03-01 | 9704.2     | 10395.7      | 61.4               | 6.7               |

### 7. Data Quality Assessment

After completing the extraction and transformation processes, we performed several data quality checks.

#### Dataset Structure

| Property           | Result     |
| ------------------ | ---------- |
| Total observations | 610        |
| Total columns      | 5          |
| Numerical features | 4          |
| Date column        | 1          |
| Data frequency     | Monthly    |
| Start date         | 1976-01-01 |
| End date           | 2026-10-01 |
| Memory usage       | 24 KB      |

#### Missing Values

We checked all columns for missing values.

The results showed zero missing values across the entire dataset.

#### Duplicate Records

We checked for duplicate dates and found no duplicated observations.

#### Chronological Ordering

We verified that the dataset was sorted in ascending chronological order using:

```
labour_monthly['Date'].is_monotonic_increasing
```

The result was:

```
True
```

#### Statistical Validation

We calculated descriptive statistics using Pandas describe().

The results were:

| Indicator                | Mean      | Minimum  | Maximum  |
| ------------------------ | --------- | -------- | -------- |
| Employment (thousands)   | 15,075.68 | 9,636.7  | 21,214.8 |
| Labour force (thousands) | 16,353.02 | 10,369.7 | 22,697.7 |
| Participation rate (%)   | 65.71     | 60.1     | 67.7     |
| Unemployment rate (%)    | 8.01      | 4.8      | 14.2     |

The observed values were within reasonable ranges.

We also confirmed that the labour force values were consistently greater than employment values, which is consistent with the definition of the labour force.

**Unit Considerations:**

The Employment and Labour force indicators are measured in thousands of persons, while the Unemployment rate and Participation rate are expressed as percentages.

For example, an Employment value of 15,000 represents approximately 15 million employed people, not 15,000 people.

### 8. Final Dataset

After completing the data extraction, filtering, transformation, and validation processes, we obtained a clean and structured monthly dataset.

The final dataset contains:

- 610 monthly observations.
- Four economic indicators.
- A historical period from January 1976 to October 2026.
- Zero missing values.
- Zero duplicate dates.
- Chronologically ordered observations.

The processed dataset was saved as:

canada_labour_market_monthly.csv

It is now ready for use in subsequent analytical stages.

### 9. How This Dataset Will Be Used

The extracted labour market indicators will serve as macroeconomic features in our Canadian stock market prediction project.

These indicators may help represent the overall economic environment and allow us to investigate potential relationships between labour market conditions and future stock returns.

However, the dataset has not yet been merged with stock price data or used to train machine learning models.

**Important Methodological Consideration:**

The Date column represents the reference month of each observation, not necessarily the date when the information became publicly available.

Before merging this dataset with daily stock prices, we must account for the actual publication or release dates of the economic indicators.

This is essential to prevent data leakage and ensure that the models only use information that would have been available at the prediction time.

### 10. Next Steps

The planned next stages of the project are:

1. Collect interest rates, government bond yields, and exchange rates using the Bank of Canada Valet API.
2. Collect historical Canadian stock market data using yfinance.
3. Calculate technical indicators from historical stock prices.
4. Integrate the different data sources into a unified dataset.
5. Handle different data frequencies and publication dates.
6. Perform feature engineering to create relevant predictive variables.
7. Train and evaluate machine learning models.
8. Conduct historical backtesting and paper trading simulations.

# Part 2: Concise Project Summary

## Canadian Labour Market Data Collection and Preprocessing

We collected and processed Canadian labour market data from Statistics Canada using Table 14-10-0287, which provides monthly seasonally adjusted economic indicators covering January 1976 to October 2026.

The original dataset was approximately 1.2 GB in size. To process it efficiently, we used Pandas chunk-based processing with a batch size of 200,000 rows instead of loading the entire file into memory.

After examining the metadata and understanding the dataset dimensions, we applied filtering criteria based on Canada, Total Gender, individuals aged 15 years and over, Estimates, and Seasonally Adjusted data.

We extracted four key economic indicators:

- Employment
- Labour force
- Unemployment rate
- Participation rate

The extracted data was initially in Long Format. We transformed it into Wide Format using Pandas pivot_table(), converted the date column into a datetime format, and sorted the observations chronologically.

The final dataset contains **610 monthly observations and four economic indicators**, with no missing values or duplicate dates. Its historical coverage extends from January 1976 to October 2026, and its final memory usage is approximately 24 KB.

The processed dataset was saved as canada_labour_market_monthly.csv and will serve as one of the macroeconomic data sources in our Canadian stock market prediction project.

It will later be integrated with historical stock prices, financial indicators, and other economic variables to develop machine learning models for predicting future stock returns.

# Part 3: Key Project Statistics

| Item                | Value                            |
| ------------------- | -------------------------------- |
| Data Source         | Statistics Canada                |
| Table ID            | 14-10-0287                       |
| Original File Size  | Approximately 1.2 GB             |
| Processing Method   | Pandas Chunk Processing          |
| Chunk Size          | 200,000 rows                     |
| Filtered Rows       | 2,440                            |
| Final Observations  | 610                              |
| Economic Indicators | 4                                |
| Data Frequency      | Monthly                          |
| Historical Period   | 1976–2026                        |
| Missing Values      | 0                                |
| Duplicate Dates     | 0                                |
| Final Memory Usage  | 24 KB                            |
| Output File         | canada_labour_market_monthly.csv |

**Overall Conclusion**

We successfully transformed a large and complex raw economic dataset into a clean, compact, and structured monthly dataset. This represents the completion of the labour market data collection and preprocessing stage and establishes one of the economic data foundations for our Canadian stock market prediction project.
