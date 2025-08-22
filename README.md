# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-08-21 21:49:58 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector             | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | BJ       | 2025-08-22 | Before market open | Consumer Defensive | $14.0B       | $107.34 | 23.60%       | 40.79%       | 1.73x         |
|  1 | ROST     | 2025-08-21 | After market close | Consumer Cyclical  | $47.6B       | $146.35 | 23.43%       | 34.05%       | 1.45x         |
|  2 | WDAY     | 2025-08-21 | After market close | Technology         | $60.7B       | $227.49 | 33.72%       | 47.28%       | 1.40x         |
|  3 | INTU     | 2025-08-21 | After market close | Technology         | $194.6B      | $699.15 | 26.63%       | 37.22%       | 1.40x         |
|  4 | BKE      | 2025-08-22 | Before market open | Consumer Cyclical  | $2.8B        | $55.04  | 25.83%       | 35.81%       | 1.39x         |
|  5 | RLX      | 2025-08-22 | Before market open | Consumer Defensive | $2.7B        | $2.24   | nan%         | nan%         | nanx          |
|  6 | ZKH      | 2025-08-22 | Before market open | Consumer Cyclical  | $470.8M      | $2.99   | nan%         | nan%         | nanx          |
|  7 | ZM       | 2025-08-21 | After market close | Technology         | $22.1B       | $72.16  | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
