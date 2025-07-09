# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-07-08 21:59:21 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector             | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | PENG     | 2025-07-08 | After market close | Technology         | $1.1B        | $20.94  | 34.20%       | 74.34%       | 2.17x         |
|  1 | AEHR     | 2025-07-08 | After market close | Technology         | $451.6M      | $14.82  | nan%         | nan%         | nanx          |
|  2 | KRUS     | 2025-07-08 | After market close | Consumer Cyclical  | $1.0B        | $85.88  | nan%         | nan%         | nanx          |
|  3 | SAR      | 2025-07-08 | After market close | Financial Services | $390.9M      | $25.19  | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
