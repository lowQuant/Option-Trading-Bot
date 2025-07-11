# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-07-10 22:01:51 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector             | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | PSMT     | 2025-07-10 | After market close | Consumer Defensive | $3.2B        | $102.01 | 18.85%       | 41.52%       | 2.20x         |
|  1 | WDFC     | 2025-07-10 | After market close | Basic Materials    | $3.0B        | $229.73 | 20.87%       | 41.98%       | 2.01x         |
|  2 | ETWO     | 2025-07-10 | After market close | Technology         | $1.0B        | $3.25   | nan%         | nan%         | nanx          |
|  3 | LEVI     | 2025-07-10 | After market close | Consumer Cyclical  | $7.8B        | $19.40  | nan%         | nan%         | nanx          |
|  4 | VIST     | 2025-07-11 | Before market open | Energy             | $5.3B        | $47.23  | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
