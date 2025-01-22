# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-01-22 04:21:59 EST

### Top 10 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | PRGS     | 2025-01-21 | After market close | Technology             | $2.7B        | $62.94  | 18.39%       | 38.35%       | 2.09x         |
|  1 | NFLX     | 2025-01-21 | After market close | Communication Services | $366.8B      | $842.37 | 25.38%       | 44.03%       | 1.73x         |
|  2 | STX      | 2025-01-21 | After market close | Technology             | $20.7B       | $95.07  | 28.43%       | 43.90%       | 1.54x         |
|  3 | UAL      | 2025-01-21 | After market close | Industrials            | $35.3B       | $106.11 | 37.47%       | 56.25%       | 1.50x         |
|  4 | TEL      | 2025-01-22 | Before market open | Technology             | $43.6B       | $143.69 | 15.95%       | 23.91%       | 1.50x         |
|  5 | PG       | 2025-01-22 | Before market open | Consumer Defensive     | $379.5B      | $160.50 | 14.48%       | 20.81%       | 1.44x         |
|  6 | TRST     | 2025-01-21 | After market close | Financial Services     | $618.0M      | $32.22  | 29.60%       | 41.90%       | 1.42x         |
|  7 | UCB      | 2025-01-22 | Before market open | Financial Services     | $4.0B        | $32.61  | 30.97%       | 42.03%       | 1.36x         |
|  8 | COF      | 2025-01-21 | After market close | Financial Services     | $72.8B       | $188.44 | 25.54%       | 34.56%       | 1.35x         |
|  9 | TDY      | 2025-01-22 | Before market open | Technology             | $22.1B       | $472.08 | 15.68%       | 20.85%       | 1.33x         |

### 📊 Historical Implied Volatility Analysis

#### Top 10Stocks with Low IV compared to their historical values before earnings

|    | symbol   | next_earnings_date   | earnings_time      | sector             |   market_cap |   iv_current |   iv_before_mean |   deviation_from_before |   iv_after_mean |   deviation_from_after |   iv_before_std |   iv_before_count |   iv_after_std |   iv_after_count |
|---:|:---------|:---------------------|:-------------------|:-------------------|-------------:|-------------:|-----------------:|------------------------:|----------------:|-----------------------:|----------------:|------------------:|---------------:|-----------------:|
|  0 | CBOE     | 2025-02-07           | Before market open | Financial Services |   20390.7400 |       0.2123 |           0.3317 |                 -0.1194 |          0.2460 |                -0.0337 |        nan      |                 1 |         0.0519 |               13 |
|  1 | KIM      | 2025-02-07           | Before market open | Real Estate        |   15025.2667 |       0.2187 |           0.3141 |                 -0.0954 |          0.2716 |                -0.0529 |          0.0357 |                12 |         0.0149 |                2 |
|  2 | FTV      | 2025-02-07           | Before market open | Technology         |   27377.7459 |       0.2516 |           0.3195 |                 -0.0679 |          0.2336 |                 0.0180 |          0.0254 |                 4 |         0.0400 |               11 |
|  3 | AVTR     | 2025-02-07           | Before market open | Healthcare         |   14816.9677 |       0.5147 |           0.5383 |                 -0.0236 |          0.3604 |                 0.1543 |        nan      |                 1 |       nan      |                1 |

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
