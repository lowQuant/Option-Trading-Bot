# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-06-26 21:57:28 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector            | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | APOG     | 2025-06-27 | Before market open | Industrials       | $855.8M      | $38.93  | 28.62%       | 83.88%       | 2.93x         |
|  1 | EPAC     | 2025-06-26 | After market close | Industrials       | $2.4B        | $43.18  | 19.80%       | 45.80%       | 2.31x         |
|  2 | CNXC     | 2025-06-26 | After market close | Technology        | $3.5B        | $54.17  | 39.22%       | 61.35%       | 1.56x         |
|  3 | NKE      | 2025-06-26 | After market close | Consumer Cyclical | $89.8B       | $60.83  | 31.19%       | 48.19%       | 1.55x         |
|  4 | AOUT     | 2025-06-26 | After market close | Consumer Cyclical | $152.3M      | $10.93  | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
