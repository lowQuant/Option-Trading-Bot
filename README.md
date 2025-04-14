# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-04-13 21:50:12 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector             | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | MTB      | 2025-04-14 | Before market open | Financial Services | $25.9B       | $157.85 | 46.83%       | 49.04%       | 1.05x         |
|  1 | GS       | 2025-04-14 | Before market open | Financial Services | $153.7B      | $489.80 | 61.18%       | 50.62%       | 0.83x         |
|  2 | ALOT     | 2025-04-14 | Before market open | Technology         | $64.2M       | $8.70   | nan%         | nan%         | nanx          |
|  3 | PLCE     | 2025-04-11 | After market close | Consumer Cyclical  | $86.7M       | $7.08   | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
