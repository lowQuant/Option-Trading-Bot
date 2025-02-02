# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-02-01 20:48:49 EST

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

|    | symbol   | next_earnings_date   | earnings_time      | sector             |   market_cap |   iv_current |   iv_before_mean |   deviation_from_before |   iv_after_mean |   deviation_from_after |   iv_before_std |   iv_before_count |   iv_after_std |   iv_after_count |
|---:|:---------|:---------------------|:-------------------|:-------------------|-------------:|-------------:|-----------------:|------------------------:|----------------:|-----------------------:|----------------:|------------------:|---------------:|-----------------:|
|  0 | PUMP     | 2025-02-19           | Before market open | Energy             |     914.0184 |       0.5185 |           0.9204 |                 -0.4019 |          0.8130 |                -0.2945 |          0.3705 |                 3 |         0.3582 |               19 |
|  1 | SKT      | 2025-02-19           | After market close | Real Estate        |    3632.9441 |       0.3077 |           0.5856 |                 -0.2779 |          0.3441 |                -0.0364 |          0.2580 |                10 |         0.1278 |                9 |
|  2 | PK       | 2025-02-19           | After market close | Real Estate        |    2784.4032 |       0.3457 |           0.5965 |                 -0.2508 |          0.5095 |                -0.1638 |          0.3159 |                12 |         0.2209 |               10 |
|  3 | NYMT     | 2025-02-19           | After market close | Real Estate        |     546.1938 |       0.3355 |           0.5822 |                 -0.2467 |          0.4284 |                -0.0929 |          0.3779 |                11 |         0.2092 |                7 |
|  4 | CHDN     | 2025-02-19           | After market close | Consumer Cyclical  |    9082.7223 |       0.2812 |           0.4395 |                 -0.1583 |          0.2653 |                 0.0159 |          0.1357 |                21 |       nan      |                1 |
|  5 | OII      | 2025-02-19           | After market close | Energy             |    2511.3411 |       0.6142 |           0.7604 |                 -0.1462 |          0.5270 |                 0.0872 |          0.2262 |                17 |         0.1438 |                4 |
|  6 | CF       | 2025-02-19           | After market close | Basic Materials    |   16046.3841 |       0.2905 |           0.4280 |                 -0.1375 |          0.4162 |                -0.1257 |          0.0902 |                18 |         0.1501 |                2 |
|  7 | CAKE     | 2025-02-19           | After market close | Consumer Cyclical  |    2865.8793 |       0.3824 |           0.5116 |                 -0.1292 |          0.5911 |                -0.2087 |          0.1218 |                14 |         0.1869 |                5 |
|  8 | LOPE     | 2025-02-19           | After market close | Consumer Defensive |    5119.1685 |       0.3438 |           0.4646 |                 -0.1208 |          0.3092 |                 0.0346 |          0.0892 |                 6 |         0.0652 |               14 |
|  9 | TNL      | 2025-02-19           | Before market open | Consumer Cyclical  |    3715.0876 |       0.3452 |           0.4543 |                 -0.1091 |          0.3431 |                 0.0021 |          0.0748 |                 4 |         0.0431 |               12 |

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
