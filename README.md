# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-01-24 20:28:27 EST

### Top 10 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | T        | 2025-01-27 | Before market open | Communication Services | $159.9B      | $22.02  | 17.98%       | 25.69%       | 1.43x         |
|  1 | BOH      | 2025-01-27 | Before market open | Financial Services     | $2.8B        | $71.12  | 26.14%       | 34.37%       | 1.31x         |
|  2 | BMRC     | 2025-01-27 | Before market open | Financial Services     | $385.8M      | $23.58  | nan%         | nan%         | nanx          |
|  3 | DX       | 2025-01-27 | Before market open | Real Estate            | $1.0B        | $12.60  | nan%         | nan%         | nanx          |
|  4 | HOPE     | 2025-01-27 | Before market open | Financial Services     | $1.5B        | $12.10  | 30.97%       | nan%         | nanx          |
|  5 | SOFI     | 2025-01-27 | Before market open | Financial Services     | $19.4B       | $18.03  | nan%         | nan%         | nanx          |

### 📊 Historical Implied Volatility Analysis

#### Top 10Stocks with Low IV compared to their historical values before earnings

|    | symbol   | next_earnings_date   | earnings_time      | sector             |   market_cap |   iv_current |   iv_before_mean |   deviation_from_before |   iv_after_mean |   deviation_from_after |   iv_before_std |   iv_before_count |   iv_after_std |   iv_after_count |
|---:|:---------|:---------------------|:-------------------|:-------------------|-------------:|-------------:|-----------------:|------------------------:|----------------:|-----------------------:|----------------:|------------------:|---------------:|-----------------:|
|  0 | HUM      | 2025-02-11           | Before market open | Healthcare         |   34031.7614 |       0.4718 |           0.6209 |                 -0.1491 |          0.2824 |                 0.1894 |        nan      |                 1 |         0.0972 |               12 |
|  1 | WELL     | 2025-02-11           | After market close | Real Estate        |   80538.7223 |       0.2102 |           0.2804 |                 -0.0702 |          0.2640 |                -0.0538 |          0.0333 |                 9 |         0.0465 |                7 |
|  2 | BHF      | 2025-02-11           | After market close | Financial Services |    3008.0760 |       0.3826 |           0.4521 |                 -0.0695 |          0.3362 |                 0.0464 |          0.0678 |                 6 |         0.0522 |                8 |
|  3 | SPGI     | 2025-02-11           | Before market open | Financial Services |  155727.1511 |       0.2102 |           0.2691 |                 -0.0589 |          0.2405 |                -0.0303 |          0.0495 |                14 |       nan      |                1 |
|  4 | ECL      | 2025-02-11           | Before market open | Basic Materials    |   67228.3197 |       0.2343 |           0.2825 |                 -0.0482 |          0.1930 |                 0.0413 |          0.0445 |                15 |       nan      |                1 |
|  5 | AIZ      | 2025-02-11           | After market close | Financial Services |   10851.9004 |       0.2620 |           0.3052 |                 -0.0432 |          0.2579 |                 0.0041 |        nan      |                 1 |         0.0414 |               13 |
|  6 | MAS      | 2025-02-11           | Before market open | Industrials        |   16871.5704 |       0.2971 |           0.3379 |                 -0.0408 |          0.2877 |                 0.0094 |          0.0389 |                 9 |         0.0578 |                7 |
|  7 | DD       | 2025-02-11           | Before market open | Basic Materials    |   32378.9742 |       0.2867 |           0.3217 |                 -0.0350 |          0.2251 |                 0.0616 |          0.0551 |                11 |         0.0317 |                3 |
|  8 | HIW      | 2025-02-11           | After market close | Real Estate        |    3181.3386 |       0.2816 |           0.3138 |                 -0.0322 |          0.3290 |                -0.0474 |        nan      |                 1 |         0.0768 |               13 |
|  9 | ADC      | 2025-02-11           | After market close | Real Estate        |    7824.4419 |       0.1820 |           0.2025 |                 -0.0205 |          0.2457 |                -0.0637 |          0.0390 |                 4 |         0.0526 |               11 |

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
