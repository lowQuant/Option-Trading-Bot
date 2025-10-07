# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-10-06 21:42:58 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector             | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | MKC      | 2025-10-07 | Before market open | Consumer Defensive | $18.1B       | $68.91  | 24.02%       | 34.21%       | 1.42x         |
|  1 | STZ      | 2025-10-06 | After market close | Consumer Defensive | $24.4B       | $142.20 | 33.34%       | 39.67%       | 1.19x         |
|  2 | AEHR     | 2025-10-06 | After market close | Technology         | $986.1M      | $31.02  | nan%         | nan%         | nanx          |
|  3 | MKC.V    | 2025-10-07 | Before market open | nan                | N/A          | $nan    | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
