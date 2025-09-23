# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-09-22 21:42:40 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector            | market_cap   | close    | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:------------------|:-------------|:---------|:-------------|:-------------|:--------------|
|  0 | AZO      | 2025-09-23 | Before market open | Consumer Cyclical | $69.3B       | $4140.36 | 16.60%       | 27.48%       | 1.66x         |
|  1 | FLY      | 2025-09-22 | After market close | Industrials       | $7.3B        | $45.20   | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
