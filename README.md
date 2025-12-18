# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-12-17 20:56:08 EST

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector             | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | CTAS     | 2025-12-18 | Before market open | Industrials        | $75.5B       | $187.62 | 15.44%       | 30.08%       | 1.95x         |
|  1 | FDS      | 2025-12-18 | Before market open | Financial Services | $11.2B       | $293.00 | 25.43%       | 45.72%       | 1.80x         |
|  2 | EPAC     | 2025-12-17 | After market close | Industrials        | $2.1B        | $39.40  | 24.99%       | 43.33%       | 1.73x         |
|  3 | MLKN     | 2025-12-17 | After market close | Consumer Cyclical  | $1.2B        | $16.69  | 38.67%       | 58.27%       | 1.51x         |
|  4 | ACN      | 2025-12-18 | Before market open | Technology         | $180.8B      | $272.04 | 29.45%       | 38.53%       | 1.31x         |
|  5 | DRI      | 2025-12-18 | Before market open | Consumer Cyclical  | $22.1B       | $185.53 | 25.07%       | 31.18%       | 1.24x         |
|  6 | MU       | 2025-12-17 | After market close | Technology         | $253.8B      | $232.51 | 72.87%       | 66.79%       | 0.92x         |
|  7 | KMX      | 2025-12-18 | Before market open | Consumer Cyclical  | $6.2B        | $40.63  | 92.70%       | 61.32%       | 0.66x         |
|  8 | BIRK     | 2025-12-18 | Before market open | Consumer Cyclical  | $8.5B        | $47.27  | nan%         | nan%         | nanx          |
|  9 | FCEL     | 2025-12-18 | Before market open | Industrials        | $376.6M      | $8.47   | nan%         | nan%         | nanx          |
| 10 | ISSC     | 2025-12-18 | Before market open | Industrials        | $193.8M      | $11.90  | nan%         | nan%         | nanx          |
| 11 | OPXS     | 2025-12-17 | After market close | Industrials        | $88.1M       | $14.31  | nan%         | nan%         | nanx          |
| 12 | WS       | 2025-12-17 | After market close | Basic Materials    | $1.8B        | $35.46  | 33.33%       | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
