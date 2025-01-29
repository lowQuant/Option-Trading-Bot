# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-01-28 20:28:59 EST

### Top 10 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector             | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | LRN      | 2025-01-28 | After market close | Consumer Defensive | $5.3B        | $118.91 | 19.58%       | 55.88%       | 2.85x         |
|  1 | MNRO     | 2025-01-29 | Before market open | Consumer Cyclical  | $659.2M      | $21.90  | 23.18%       | 51.26%       | 2.21x         |
|  2 | WNC      | 2025-01-29 | Before market open | Industrials        | $677.8M      | $15.26  | 32.36%       | 65.31%       | 2.02x         |
|  3 | PKG      | 2025-01-28 | After market close | Consumer Cyclical  | $21.4B       | $239.72 | 13.28%       | 26.79%       | 2.02x         |
|  4 | EXTR     | 2025-01-29 | Before market open | Technology         | $2.1B        | $16.25  | 30.17%       | 59.90%       | 1.99x         |
|  5 | GPI      | 2025-01-29 | Before market open | Consumer Cyclical  | $6.1B        | $454.46 | 18.68%       | 36.17%       | 1.94x         |
|  6 | VFC      | 2025-01-29 | Before market open | Consumer Cyclical  | $10.4B       | $25.99  | 32.81%       | 62.07%       | 1.89x         |
|  7 | AVT      | 2025-01-29 | Before market open | Technology         | $4.6B        | $52.89  | 17.23%       | 31.84%       | 1.85x         |
|  8 | LFUS     | 2025-01-28 | After market close | Technology         | $5.6B        | $229.21 | 19.30%       | 35.43%       | 1.84x         |
|  9 | FFIV     | 2025-01-28 | After market close | Technology         | $15.8B       | $263.01 | 21.17%       | 38.34%       | 1.81x         |

### 📊 Historical Implied Volatility Analysis

#### Top 10Stocks with Low IV compared to their historical values before earnings

|    | symbol   | next_earnings_date   | earnings_time      | sector             |   market_cap |   iv_current |   iv_before_mean |   deviation_from_before |   iv_after_mean |   deviation_from_after |   iv_before_std |   iv_before_count |   iv_after_std |   iv_after_count |
|---:|:---------|:---------------------|:-------------------|:-------------------|-------------:|-------------:|-----------------:|------------------------:|----------------:|-----------------------:|----------------:|------------------:|---------------:|-----------------:|
|  0 | THS      | 2025-02-14           | Before market open | Consumer Defensive |    1755.1360 |       0.4672 |           0.4654 |                  0.0018 |          0.3460 |                 0.1212 |          0.0753 |                17 |         0.0899 |               11 |
|  1 | POR      | 2025-02-14           | Before market open | Utilities          |    4399.6247 |       0.2857 |           0.2699 |                  0.0158 |          0.2500 |                 0.0357 |          0.0376 |                 4 |         0.0493 |                6 |
|  2 | BGC      | 2025-02-14           | Before market open | Financial Services |    4563.0116 |       0.6073 |           0.4867 |                  0.1206 |          0.3984 |                 0.2089 |          0.0665 |                 3 |       nan      |                1 |

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
