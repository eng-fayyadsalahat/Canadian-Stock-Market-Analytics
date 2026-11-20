# Canadian Commodity Price Index (BCPI) Data Collection and Preparation

## 1. Data Source

The Bank of Canada Commodity Price Index (BCPI) dataset was obtained from the official Bank of Canada website.

- **Source:** [Bank of Canada](https://www.bankofcanada.ca/valet/observations/group/BCPI_MONTHLY/csv?start_date=1972-01-01)
- **Dataset:** Commodity Price Index (BCPI)
- **Frequency:** Monthly
- **Data format:** CSV
- **Selected version:** Monthly BCPI
- **Historical coverage:** January 1972 – October 2026

The BCPI is a chain Fisher price index that tracks spot or transaction prices, in US dollars, for 26 commodities produced in Canada and sold in world markets.

The index provides an overview of commodity price movements that are relevant to the Canadian economy.

## 2. Data Selection

The monthly dataset was selected instead of the annual version because monthly observations are more suitable for a project based on daily stock market data.

The downloaded CSV required identifying the correct header position:

- Header line: 21
- Original columns: 8
- Total observations: 658

The dataset contains seven commodity price index series:

| Column | Description                      |
| ------ | -------------------------------- |
| M.BCPI | Total Commodity Price Index      |
| M.BCNE | Non-Energy Commodity Price Index |
| M.ENER | Energy                           |
| M.MTLS | Metals and Minerals              |
| M.FOPR | Forestry Products                |
| M.AGRI | Agriculture                      |
| M.FISH | Fish and Fish Products           |

The date column was converted to datetime format.

All seven index columns were retained because they represent different commodity groups and may provide useful information for companies operating in different sectors.

## 3. Data Characteristics

The final dataset contains:

| Property           | Result       |
| ------------------ | ------------ |
| Total observations | 658          |
| Number of columns  | 8            |
| Starting date      | January 1972 |
| Ending date        | October 2026 |
| Frequency          | Monthly      |
| Missing values     | 0            |
| Duplicate dates    | 0            |

The dataset contains continuous monthly observations across the entire period, with no missing months or duplicate dates.

All index columns use the float64 data type, while the date column uses datetime64\[ns\].

## 4. Descriptive Statistics

The following table summarizes the seven index series:

| Statistic | M.BCPI | M.BCNE | M.ENER  | M.MTLS  | M.FOPR  | M.AGRI | M.FISH  |
| --------- | ------ | ------ | ------- | ------- | ------- | ------ | ------- |
| Mean      | 373.05 | 277.31 | 826.82  | 412.87  | 302.80  | 204.33 | 784.23  |
| Std       | 171.87 | 106.95 | 507.30  | 238.58  | 124.49  | 60.55  | 497.67  |
| Min       | 100.00 | 100.00 | 99.78   | 100.00  | 100.00  | 100.00 | 86.30   |
| Median    | 295.33 | 240.13 | 719.45  | 299.76  | 295.68  | 183.22 | 816.48  |
| Max       | 919.33 | 625.34 | 2755.75 | 1219.97 | 1023.04 | 387.22 | 2100.24 |

The statistics show substantial variation across commodity groups, particularly in the energy and fisheries indexes.

These values are index levels, not direct commodity prices or Canadian dollar amounts. Therefore, their absolute values should not be interpreted as actual market prices.

## 5. Economic Relevance to the Project

Commodity prices are particularly relevant to Canada because natural resources and commodity-producing industries play an important role in its economy.

The BCPI may provide useful macroeconomic context for analyzing Canadian stocks.

Potential applications include:

- Energy prices and the performance of energy companies.
- Metals and minerals prices and mining companies.
- Forestry prices and companies operating in the forestry sector.
- Agricultural commodity prices and related businesses.
- Overall commodity price movements and broader Canadian economic conditions.

The individual components may be more informative for sector-specific analysis than the total BCPI alone.

## 6. Potential Feature Engineering

The original seven index series will be preserved.

During the feature engineering stage, we may calculate:

- Month-over-month percentage changes (MoM).
- Year-over-year percentage changes (YoY).
- Rolling averages and historical volatility.

For example, the total BCPI may be transformed into:

BCPI_MoM and BCPI_YoY.

These features can help the model capture changes in commodity market conditions rather than relying only on index levels.

No additional features have been created in the current extraction and validation stage.

## 7. Data Quality and Limitations

The monthly BCPI dataset passed all initial quality checks:

- No missing values.
- No duplicate dates.
- Continuous monthly coverage.
- Correct datetime format.
- Numeric index values.
- Seven available commodity index components.

However, several methodological considerations should be addressed before integration.

**Publication timing:** The index date represents the reference month, not necessarily the date when the final information became available. The Bank of Canada notes that some commodity price observations may only become available weeks or months after the reference period.

**Data revisions:** Some commodity prices and index components may be revised when actual observations become available. This means historical values may differ from the values originally published.

**Currency:** The BCPI tracks commodity prices in US dollars. It is an index rather than a direct CAD-denominated price series. This distinction is important when analyzing its relationship with Canadian stocks and the USD/CAD exchange rate.

## 8. Final Assessment

The monthly BCPI dataset was successfully downloaded, structured, and validated.

It contains 658 monthly observations covering January 1972 through October 2026, with seven commodity index components and no missing values or duplicate dates.

The dataset will be retained as a macroeconomic input for the Canadian stock market research project. Its components may help capture commodity market conditions and sector-specific economic influences.

Feature engineering and integration with daily stock prices will be performed in later stages, taking publication timing and potential historical revisions into account.

# Canadian Commodity Price Index (BCPI) – Summary

**Source:** Bank of Canada  
**Dataset:** Commodity Price Index (BCPI)  
**Frequency:** Monthly  
**Period:** January 1972 – October 2026

### Data Collection

The monthly BCPI dataset was downloaded and prepared from the Bank of Canada. Seven index series were retained:

- M.BCPI: Total Commodity Price Index
- M.BCNE: Non-Energy Commodities
- M.ENER: Energy
- M.MTLS: Metals and Minerals
- M.FOPR: Forestry Products
- M.AGRI: Agriculture
- M.FISH: Fish and Fish Products

### Data Overview

| Property        | Result   |
| --------------- | -------- |
| Observations    | 658      |
| Columns         | 8        |
| Starting Date   | Jan 1972 |
| Ending Date     | Oct 2026 |
| Missing Values  | 0        |
| Duplicate Dates | 0        |
| Frequency       | Monthly  |

### Conclusion

The monthly BCPI dataset was successfully downloaded, structured, and validated. It provides historical information about commodity price movements relevant to the Canadian economy.

The seven commodity components will be retained for potential use in sector-specific stock analysis. Future feature engineering may include MoM and YoY percentage changes.

Publication delays and historical revisions must be considered before integrating the index with daily stock market data.
