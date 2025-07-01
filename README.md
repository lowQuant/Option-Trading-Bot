# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-06-30 22:08:22 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector      | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | PRGS     | 2025-06-30 | After market close | Technology  | $2.7B        | $63.76  | 16.96%       | 44.71%       | 2.64x         |
|  1 | MSM      | 2025-07-01 | Before market open | Industrials | $4.8B        | $85.48  | 27.22%       | 27.62%       | 1.01x         |
|  2 | QMCO     | 2025-06-30 | After market close | Technology  | $69.3M       | $9.04   | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
