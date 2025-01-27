# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-01-26 20:47:10 EST

### Top 10 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | T        | 2025-01-27 | Before market open | Communication Services | $163.0B      | $22.53  | 17.21%       | 23.56%       | 1.37x         |
|  1 | BOH      | 2025-01-27 | Before market open | Financial Services     | $2.8B        | $71.12  | 26.08%       | 31.91%       | 1.22x         |
|  2 | BMRC     | 2025-01-27 | Before market open | Financial Services     | $385.8M      | $23.58  | nan%         | nan%         | nanx          |
|  3 | DX       | 2025-01-27 | Before market open | Real Estate            | $1.0B        | $12.60  | nan%         | nan%         | nanx          |
|  4 | HOPE     | 2025-01-27 | Before market open | Financial Services     | $1.5B        | $12.10  | 30.90%       | nan%         | nanx          |
|  5 | OXLC     | 2025-01-27 | Before market open | Financial Services     | $1.9B        | $5.09   | nan%         | nan%         | nanx          |
|  6 | SOFI     | 2025-01-27 | Before market open | Financial Services     | $19.4B       | $18.03  | nan%         | nan%         | nanx          |

### 📊 Historical Implied Volatility Analysis

#### Top 10Stocks with Low IV compared to their historical values before earnings

|    | symbol   | next_earnings_date   | earnings_time      | sector            |   market_cap |   iv_current |   iv_before_mean |   deviation_from_before |   iv_after_mean |   deviation_from_after |   iv_before_std |   iv_before_count |   iv_after_std |   iv_after_count |
|---:|:---------|:---------------------|:-------------------|:------------------|-------------:|-------------:|-----------------:|------------------------:|----------------:|-----------------------:|----------------:|------------------:|---------------:|-----------------:|
|  0 | STAG     | 2025-02-12           | After market close | Real Estate       |    6399.7435 |       0.2138 |           0.4017 |                 -0.1879 |          0.2642 |                -0.0504 |        nan      |                 1 |         0.0666 |                3 |
|  1 | SAH      | 2025-02-12           | Before market open | Consumer Cyclical |    2430.9161 |       0.3680 |           0.5426 |                 -0.1746 |          0.4132 |                -0.0452 |          0.0792 |                11 |         0.0426 |                5 |
|  2 | PAYC     | 2025-02-12           | After market close | Technology        |   11964.8645 |       0.4708 |           0.6175 |                 -0.1467 |          0.4087 |                 0.0621 |          0.0801 |                 3 |         0.0572 |               11 |
|  3 | TMHC     | 2025-02-12           | Before market open | Consumer Cyclical |    6780.9132 |       0.3232 |           0.4455 |                 -0.1223 |          0.3970 |                -0.0738 |          0.0672 |                 5 |         0.0858 |               11 |
|  4 | AR       | 2025-02-12           | After market close | Energy            |   12493.2352 |       0.3824 |           0.4776 |                 -0.0952 |          0.4357 |                -0.0533 |          0.0562 |                 7 |       nan      |                1 |
|  5 | NBR      | 2025-02-12           | After market close | Energy            |     597.6935 |       0.6186 |           0.7118 |                 -0.0932 |          0.6466 |                -0.0280 |          0.1433 |                 6 |         0.0847 |                7 |
|  6 | AEIS     | 2025-02-12           | After market close | Industrials       |    4722.6998 |       0.3996 |           0.4815 |                 -0.0819 |          0.4408 |                -0.0412 |          0.0521 |                 8 |         0.0570 |                6 |
|  7 | AM       | 2025-02-12           | After market close | Energy            |    7888.9001 |       0.2276 |           0.3083 |                 -0.0807 |          0.2418 |                -0.0142 |          0.0771 |                14 |       nan      |                1 |
|  8 | SW       | 2025-02-12           | Before market open | Consumer Cyclical |   29139.1386 |       0.3098 |           0.3855 |                 -0.0757 |          0.3828 |                -0.0730 |        nan      |                 1 |       nan      |                1 |
|  9 | EXC      | 2025-02-12           | Before market open | Utilities         |   39570.2067 |       0.1808 |           0.2435 |                 -0.0627 |          0.2134 |                -0.0326 |          0.0390 |                12 |         0.0311 |                9 |

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
