# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-02-02 20:48:50 EST

### Top 10 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector             | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | IDXX     | 2025-02-03 | Before market open | Healthcare         | $34.6B       | $423.99 | 24.66%       | 38.40%       | 1.56x         |
|  1 | TSN      | 2025-02-03 | Before market open | Consumer Defensive | $20.1B       | $56.76  | 20.74%       | 31.97%       | 1.54x         |
|  2 | SAIA     | 2025-02-03 | Before market open | Industrials        | $12.8B       | $495.00 | 39.16%       | 58.20%       | 1.49x         |
|  3 | ARLP     | 2025-02-03 | Before market open | Energy             | $3.7B        | $28.38  | nan%         | nan%         | nanx          |
|  4 | JOUT     | 2025-02-03 | Before market open | Consumer Cyclical  | $334.6M      | $32.93  | nan%         | nan%         | nanx          |
|  5 | LVRO     | 2025-02-03 | Before market open | Basic Materials    | $574.3M      | $4.39   | nan%         | nan%         | nanx          |
|  6 | NSSC     | 2025-02-03 | Before market open | Industrials        | $1.3B        | $37.20  | nan%         | nan%         | nanx          |
|  7 | TWST     | 2025-02-03 | Before market open | Healthcare         | $3.1B        | $51.14  | nan%         | nan%         | nanx          |

### 📊 Historical Implied Volatility Analysis

#### Top 10Stocks with Low IV compared to their historical values before earnings

|    | symbol   | next_earnings_date   | earnings_time      | sector            |   market_cap |   iv_current |   iv_before_mean |   deviation_from_before |   iv_after_mean |   deviation_from_after |   iv_before_std |   iv_before_count |   iv_after_std |   iv_after_count |
|---:|:---------|:---------------------|:-------------------|:------------------|-------------:|-------------:|-----------------:|------------------------:|----------------:|-----------------------:|----------------:|------------------:|---------------:|-----------------:|
|  0 | REZI     | 2025-02-20           | After market close | Industrials       |    3309.8094 |       0.4038 |           0.8008 |                 -0.3970 |          0.4314 |                -0.0276 |          0.2262 |                 8 |         0.1030 |               11 |
|  1 | ESAB     | 2025-02-20           | Before market open | Industrials       |    7485.8926 |       0.2971 |           0.4548 |                 -0.1577 |          0.3438 |                -0.0467 |          0.1046 |                 7 |         0.0563 |                4 |
|  2 | NVRI     | 2025-02-20           | Before market open | Industrials       |     767.6952 |       0.4514 |           0.6065 |                 -0.1551 |          0.6433 |                -0.1919 |          0.1098 |                 3 |       nan      |                1 |
|  3 | LAMR     | 2025-02-20           | Before market open | Real Estate       |   12940.0986 |       0.2680 |           0.3734 |                 -0.1054 |          0.2830 |                -0.0150 |          0.1418 |                12 |         0.0618 |                7 |
|  4 | LNT      | 2025-02-20           | After market close | Utilities         |   15108.5496 |       0.2014 |           0.3024 |                 -0.1010 |          0.2211 |                -0.0197 |          0.0005 |                 2 |         0.0455 |               13 |
|  5 | DINO     | 2025-02-20           | Before market open | Energy            |    6797.6888 |       0.3693 |           0.4566 |                 -0.0873 |          0.4217 |                -0.0524 |          0.0717 |                 7 |         0.0981 |                7 |
|  6 | TPX      | 2025-02-20           | Before market open | Consumer Cyclical |   10964.4503 |       0.4354 |           0.5146 |                 -0.0792 |          0.3790 |                 0.0564 |          0.1066 |                16 |         0.1317 |                2 |
|  7 | ALRM     | 2025-02-20           | After market close | Technology        |    2998.8634 |       0.3862 |           0.4601 |                 -0.0739 |          0.4078 |                -0.0216 |          0.0711 |                 5 |         0.1045 |               17 |
|  8 | ITGR     | 2025-02-20           | Before market open | Healthcare        |    4770.3434 |       0.3497 |           0.4217 |                 -0.0720 |          0.4168 |                -0.0671 |          0.0872 |                18 |         0.0742 |                2 |
|  9 | BLDR     | 2025-02-20           | Before market open | Industrials       |   19251.4191 |       0.4519 |           0.5191 |                 -0.0672 |          0.4774 |                -0.0255 |          0.0758 |                10 |         0.0827 |                8 |

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
