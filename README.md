# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-01-27 20:34:59 EST

### Top 10 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector             | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | SANM     | 2025-01-27 | After market close | Technology         | $4.2B        | $84.01  | 18.50%       | 52.00%       | 2.81x         |
|  1 | MRTN     | 2025-01-27 | After market close | Industrials        | $1.3B        | $15.94  | 25.13%       | 63.32%       | 2.52x         |
|  2 | CVLT     | 2025-01-28 | Before market open | Technology         | $6.9B        | $159.88 | 32.60%       | 79.46%       | 2.44x         |
|  3 | SYY      | 2025-01-28 | Before market open | Consumer Defensive | $37.8B       | $74.77  | 11.36%       | 22.76%       | 2.00x         |
|  4 | PII      | 2025-01-28 | Before market open | Consumer Cyclical  | $3.2B        | $53.83  | 30.00%       | 59.85%       | 2.00x         |
|  5 | ADNT     | 2025-01-28 | Before market open | Consumer Cyclical  | $1.5B        | $17.14  | 35.66%       | 54.77%       | 1.54x         |
|  6 | RCL      | 2025-01-28 | Before market open | Consumer Cyclical  | $63.7B       | $232.10 | 26.80%       | 39.98%       | 1.49x         |
|  7 | PCAR     | 2025-01-28 | Before market open | Industrials        | $57.6B       | $109.90 | 20.05%       | 29.81%       | 1.49x         |
|  8 | KMB      | 2025-01-28 | Before market open | Consumer Defensive | $43.8B       | $128.41 | 14.55%       | 21.37%       | 1.47x         |
|  9 | BRO      | 2025-01-27 | After market close | Financial Services | $30.8B       | $106.00 | 16.87%       | 24.67%       | 1.46x         |

### 📊 Historical Implied Volatility Analysis

#### Top 10Stocks with Low IV compared to their historical values before earnings

|    | symbol   | next_earnings_date   | earnings_time      | sector            |   market_cap |   iv_current |   iv_before_mean |   deviation_from_before |   iv_after_mean |   deviation_from_after |   iv_before_std |   iv_before_count |   iv_after_std |   iv_after_count |
|---:|:---------|:---------------------|:-------------------|:------------------|-------------:|-------------:|-----------------:|------------------------:|----------------:|-----------------------:|----------------:|------------------:|---------------:|-----------------:|
|  0 | PBF      | 2025-02-13           | Before market open | Energy            |    3468.6559 |       0.4405 |           0.6800 |                 -0.2395 |          0.5736 |                -0.1331 |          0.1807 |                12 |         0.0023 |                2 |
|  1 | HCC      | 2025-02-13           | After market close | Basic Materials   |    2784.5412 |       0.4480 |           0.5689 |                 -0.1209 |          0.6352 |                -0.1872 |          0.0740 |                10 |         0.0915 |                4 |
|  2 | YETI     | 2025-02-13           | Before market open | Consumer Cyclical |    3293.7705 |       0.5065 |           0.6255 |                 -0.1190 |          0.4744 |                 0.0321 |          0.0984 |                11 |         0.1722 |                3 |
|  3 | OGN      | 2025-02-13           | Before market open | Healthcare        |    4187.5843 |       0.2995 |           0.4156 |                 -0.1161 |          0.4116 |                -0.1121 |          0.1038 |                12 |       nan      |                1 |
|  4 | FRT      | 2025-02-13           | After market close | Real Estate       |    9410.0511 |       0.1919 |           0.3030 |                 -0.1111 |          0.2486 |                -0.0567 |          0.0473 |                 7 |         0.0398 |                6 |
|  5 | AVNT     | 2025-02-13           | Before market open | Basic Materials   |    3943.2876 |       0.3554 |           0.4340 |                 -0.0786 |          0.4575 |                -0.1021 |          0.1058 |                 7 |         0.1657 |                7 |
|  6 | AMAT     | 2025-02-13           | After market close | Technology        |  141873.2175 |       0.3896 |           0.4666 |                 -0.0770 |          0.3846 |                 0.0050 |          0.0568 |                 2 |         0.0508 |               15 |
|  7 | ZBRA     | 2025-02-13           | Before market open | Technology        |   20598.9888 |       0.3786 |           0.4479 |                 -0.0693 |          0.3679 |                 0.0107 |          0.0559 |                14 |         0.1277 |                2 |
|  8 | IR       | 2025-02-13           | After market close | Industrials       |   37048.8934 |       0.2858 |           0.3465 |                 -0.0607 |          0.2479 |                 0.0379 |          0.0533 |                11 |         0.0617 |                3 |
|  9 | H        | 2025-02-13           | Before market open | Consumer Cyclical |   14979.1089 |       0.2841 |           0.3348 |                 -0.0507 |          0.3096 |                -0.0255 |          0.0374 |                 4 |       nan      |                1 |

## 📝 Data Interpretation

- **Top 10 Upcoming Earnings**: 
  - Ratio of current implied volatility to historical volatility
  - Potential candidates for short puts

- **Historical IV Deviation**: 
  - Measures difference between current and historical pre-earnings implied volatility
  - Negative values indicate current IV is lower than historical pre-earnings IV
  - Potential candidates for long straddles

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
