# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-01-25 20:42:09 EST

### Top 10 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | T        | 2025-01-27 | Before market open | Communication Services | $159.9B      | $22.02  | 17.21%       | 23.56%       | 1.37x         |
|  1 | BOH      | 2025-01-27 | Before market open | Financial Services     | $2.8B        | $71.12  | 26.08%       | 31.91%       | 1.22x         |
|  2 | BMRC     | 2025-01-27 | Before market open | Financial Services     | $385.8M      | $23.58  | nan%         | nan%         | nanx          |
|  3 | DX       | 2025-01-27 | Before market open | Real Estate            | $1.0B        | $12.60  | nan%         | nan%         | nanx          |
|  4 | HOPE     | 2025-01-27 | Before market open | Financial Services     | $1.5B        | $12.10  | 30.90%       | nan%         | nanx          |
|  5 | OXLC     | 2025-01-27 | Before market open | Financial Services     | $1.9B        | $5.09   | nan%         | nan%         | nanx          |
|  6 | SOFI     | 2025-01-27 | Before market open | Financial Services     | $19.4B       | $18.03  | nan%         | nan%         | nanx          |

### 📊 Historical Implied Volatility Analysis

#### Top 10Stocks with Low IV compared to their historical values before earnings

|    | symbol   | next_earnings_date   | earnings_time      | sector             |   market_cap |   iv_current |   iv_before_mean |   deviation_from_before |   iv_after_mean |   deviation_from_after |   iv_before_std |   iv_before_count |   iv_after_std |   iv_after_count |
|---:|:---------|:---------------------|:-------------------|:-------------------|-------------:|-------------:|-----------------:|------------------------:|----------------:|-----------------------:|----------------:|------------------:|---------------:|-----------------:|
|  0 | HUM      | 2025-02-11           | Before market open | Healthcare         |   34031.7614 |       0.4567 |           0.6209 |                 -0.1642 |          0.2824 |                 0.1743 |        nan      |                 1 |         0.0972 |               12 |
|  1 | AN       | 2025-02-11           | Before market open | Consumer Cyclical  |    7243.3608 |       0.3452 |           0.4435 |                 -0.0983 |          0.3583 |                -0.0131 |          0.0569 |                11 |         0.0377 |                7 |
|  2 | BHF      | 2025-02-11           | After market close | Financial Services |    3008.0760 |       0.3544 |           0.4521 |                 -0.0977 |          0.3362 |                 0.0182 |          0.0678 |                 6 |         0.0522 |                8 |
|  3 | FIS      | 2025-02-11           | Before market open | Technology         |   42411.5282 |       0.3118 |           0.4058 |                 -0.0940 |          0.3043 |                 0.0075 |          0.0698 |                11 |         0.0700 |                5 |
|  4 | MAR      | 2025-02-11           | Before market open | Consumer Cyclical  |   77026.3777 |       0.2522 |           0.3286 |                 -0.0764 |          0.2869 |                -0.0347 |          0.0551 |                10 |         0.0564 |                5 |
|  5 | AIZ      | 2025-02-11           | After market close | Financial Services |   10851.9004 |       0.2427 |           0.3052 |                 -0.0625 |          0.2579 |                -0.0152 |        nan      |                 1 |         0.0414 |               13 |
|  6 | MAS      | 2025-02-11           | Before market open | Industrials        |   16871.5704 |       0.2758 |           0.3379 |                 -0.0621 |          0.2877 |                -0.0119 |          0.0389 |                 9 |         0.0578 |                7 |
|  7 | SPGI     | 2025-02-11           | Before market open | Financial Services |  155727.1511 |       0.2148 |           0.2691 |                 -0.0543 |          0.2405 |                -0.0257 |          0.0495 |                14 |       nan      |                1 |
|  8 | AIG      | 2025-02-11           | After market close | Financial Services |   46838.8127 |       0.2714 |           0.3232 |                 -0.0518 |          0.2926 |                -0.0212 |          0.0445 |                 5 |         0.0472 |                9 |
|  9 | ECL      | 2025-02-11           | Before market open | Basic Materials    |   67228.3197 |       0.2336 |           0.2825 |                 -0.0489 |          0.1930 |                 0.0406 |          0.0445 |                15 |       nan      |                1 |

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
