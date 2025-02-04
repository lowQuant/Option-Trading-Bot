# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-02-03 20:36:51 EST

### Top 10 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | FOX      | 2025-02-04 | Before market open | Communication Services | $23.0B       | $48.60  | 18.50%       | 44.68%       | 2.42x         |
|  1 | INGR     | 2025-02-04 | Before market open | Consumer Defensive     | $8.8B        | $136.44 | 14.79%       | 31.55%       | 2.13x         |
|  2 | KD       | 2025-02-03 | After market close | Technology             | $8.8B        | $37.96  | 31.26%       | 64.55%       | 2.06x         |
|  3 | BERY     | 2025-02-04 | Before market open | Consumer Cyclical      | $7.7B        | $67.92  | 15.96%       | 32.37%       | 2.03x         |
|  4 | EL       | 2025-02-04 | Before market open | Consumer Defensive     | $29.7B       | $83.43  | 29.41%       | 55.34%       | 1.88x         |
|  5 | WWD      | 2025-02-03 | After market close | Industrials            | $11.2B       | $185.25 | 23.11%       | 43.20%       | 1.87x         |
|  6 | AMCR     | 2025-02-04 | Before market open | Consumer Cyclical      | $13.8B       | $9.72   | 14.77%       | 27.19%       | 1.84x         |
|  7 | SNCY     | 2025-02-03 | After market close | Industrials            | $879.9M      | $16.96  | 35.48%       | 64.64%       | 1.82x         |
|  8 | J        | 2025-02-04 | Before market open | Industrials            | $17.2B       | $140.13 | 16.78%       | 29.74%       | 1.77x         |
|  9 | JJSF     | 2025-02-03 | After market close | Consumer Defensive     | $2.6B        | $137.23 | 20.82%       | 36.40%       | 1.75x         |

### 📊 Historical Implied Volatility Analysis

#### Top 10Stocks with Low IV compared to their historical values before earnings

|    | symbol   | next_earnings_date   | earnings_time      | sector          |   market_cap |   iv_current |   iv_before_mean |   deviation_from_before |   iv_after_mean |   deviation_from_after |   iv_before_std |   iv_before_count |   iv_after_std |   iv_after_count |
|---:|:---------|:---------------------|:-------------------|:----------------|-------------:|-------------:|-----------------:|------------------------:|----------------:|-----------------------:|----------------:|------------------:|---------------:|-----------------:|
|  0 | TXNM     | 2025-02-21           | Before market open | Utilities       |    4362.0915 |       0.2031 |           0.8051 |                 -0.6020 |        nan      |               nan      |        nan      |                 1 |       nan      |                0 |
|  1 | UNIT     | 2025-02-21           | Before market open | Real Estate     |    1293.8095 |       0.5246 |           0.5902 |                 -0.0656 |          0.5950 |                -0.0704 |          0.1469 |                12 |         0.2627 |                9 |
|  2 | ASIX     | 2025-02-21           | Before market open | Basic Materials |     816.3647 |       0.5662 |           0.4634 |                  0.1028 |          0.5364 |                 0.0298 |          0.0260 |                 2 |         0.2006 |               18 |
|  3 | HE       | 2025-02-21           | After market close | Utilities       |    1609.1077 |     nan      |           0.2834 |                nan      |          0.2634 |               nan      |          0.0938 |                 5 |         0.0478 |                7 |
|  4 | SHO      | 2025-02-21           | Before market open | Real Estate     |    2246.0731 |     nan      |           0.3638 |                nan      |          0.3688 |               nan      |          0.0678 |                 2 |         0.0698 |                4 |

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
