# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-01-18 10:32:48 EST

### Top 10 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector             | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | MMM      | 2025-01-21 | Before market open | Industrials        | $76.8B       | $139.18 | 19.58%       | 33.13%       | 1.69x         |
|  1 | DHI      | 2025-01-21 | Before market open | Consumer Cyclical  | $47.4B       | $146.60 | 27.31%       | 35.92%       | 1.32x         |
|  2 | FBK      | 2025-01-21 | Before market open | Financial Services | $2.4B        | $52.23  | 28.34%       | 36.90%       | 1.30x         |
|  3 | KEY      | 2025-01-21 | Before market open | Financial Services | $20.2B       | $17.84  | 27.29%       | 30.42%       | 1.11x         |
|  4 | PLD      | 2025-01-21 | Before market open | Real Estate        | $101.4B      | $110.93 | 27.94%       | 26.18%       | 0.94x         |
|  5 | FITB     | 2025-01-21 | Before market open | Financial Services | $29.4B       | $43.27  | 26.42%       | 24.74%       | 0.94x         |
|  6 | ONB      | 2025-01-21 | Before market open | Financial Services | $7.8B        | $22.70  | 29.53%       | 26.55%       | 0.90x         |
|  7 | CBU      | 2025-01-21 | Before market open | Financial Services | $3.3B        | $62.60  | 30.67%       | 27.42%       | 0.89x         |
|  8 | EDU      | 2025-01-21 | Before market open | Consumer Defensive | $9.9B        | $59.20  | nan%         | nan%         | nanx          |
|  9 | FOR      | 2025-01-21 | Before market open | Real Estate        | $1.4B        | $27.26  | nan%         | nan%         | nanx          |

### 📊 Historical Implied Volatility Analysis

#### Top 10Stocks with Low IV compared to their historical values before earnings

|    | symbol   | next_earnings_date   | earnings_time      | sector             |   market_cap |   iv_current |   iv_before_mean |   deviation_from_before |   iv_after_mean |   deviation_from_after |   iv_before_std |   iv_before_count |   iv_after_std |   iv_after_count |
|---:|:---------|:---------------------|:-------------------|:-------------------|-------------:|-------------:|-----------------:|------------------------:|----------------:|-----------------------:|----------------:|------------------:|---------------:|-----------------:|
|  0 | MUR      | 2025-01-30           | Before market open | Energy             |    4701.9786 |       0.3281 |           0.4943 |                 -0.1662 |          0.4572 |                -0.1291 |          0.1264 |                11 |         0.1091 |                3 |
|  1 | INTC     | 2025-01-30           | After market close | Technology         |   92686.3688 |       0.6731 |           0.8157 |                 -0.1426 |          0.3236 |                 0.3495 |        nan      |                 1 |         0.0735 |               12 |
|  2 | ATGE     | 2025-01-30           | After market close | Consumer Defensive |    3680.4718 |       0.3949 |           0.5091 |                 -0.1142 |          0.3948 |                 0.0001 |          0.0109 |                 2 |         0.0996 |               13 |
|  3 | BFH      | 2025-01-30           | Before market open | Financial Services |    3058.9701 |       0.4676 |           0.5811 |                 -0.1135 |          0.5535 |                -0.0859 |          0.0934 |                10 |       nan      |                1 |
|  4 | CNX      | 2025-01-30           | Before market open | Energy             |    4499.0280 |       0.3407 |           0.4519 |                 -0.1112 |          0.3657 |                -0.0250 |          0.0904 |                13 |         0.0387 |                2 |
|  5 | GEN      | 2025-01-30           | After market close | Technology         |   16960.4659 |       0.3273 |           0.4130 |                 -0.0857 |          0.2662 |                 0.0611 |          0.0011 |                 2 |         0.0310 |                6 |
|  6 | BKR      | 2025-01-30           | After market close | Energy             |   46052.5404 |       0.2841 |           0.3688 |                 -0.0847 |          0.3548 |                -0.0707 |          0.0444 |                 4 |         0.0875 |               13 |
|  7 | VLO      | 2025-01-30           | Before market open | Energy             |   44654.3135 |       0.3062 |           0.3833 |                 -0.0771 |          0.3320 |                -0.0258 |          0.0670 |                14 |       nan      |                1 |
|  8 | CAH      | 2025-01-30           | Before market open | Healthcare         |   30558.6012 |       0.2527 |           0.3227 |                 -0.0700 |          0.2191 |                 0.0336 |          0.0610 |                12 |         0.0292 |                4 |
|  9 | PPG      | 2025-01-30           | After market close | Basic Materials    |   27895.6790 |       0.2308 |           0.3002 |                 -0.0694 |          0.2430 |                -0.0122 |          0.0671 |                 5 |         0.0597 |               10 |

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
