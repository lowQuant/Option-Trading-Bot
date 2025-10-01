# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-09-30 21:54:18 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector             | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | NKE      | 2025-09-30 | After market close | Consumer Cyclical  | $102.6B      | $69.55  | 20.20%       | 45.98%       | 2.28x         |
|  1 | AYI      | 2025-10-01 | Before market open | Industrials        | $10.6B       | $339.11 | 24.26%       | 39.88%       | 1.64x         |
|  2 | CAG      | 2025-10-01 | Before market open | Consumer Defensive | $8.8B        | $18.04  | 24.07%       | 38.12%       | 1.58x         |
|  3 | RPM      | 2025-10-01 | Before market open | Basic Materials    | $15.1B       | $117.03 | 22.22%       | 33.33%       | 1.50x         |
|  4 | CALM     | 2025-10-01 | Before market open | Consumer Defensive | $4.7B        | $96.12  | 33.41%       | 44.05%       | 1.32x         |
|  5 | NG       | 2025-10-01 | Before market open | Basic Materials    | $3.6B        | $8.48   | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
