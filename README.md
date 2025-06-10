# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-06-09 21:57:04 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector             | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | CASY     | 2025-06-09 | After market close | Consumer Cyclical  | $16.2B       | $444.04 | 22.87%       | 35.99%       | 1.57x         |
|  1 | UNFI     | 2025-06-10 | Before market open | Consumer Defensive | $1.7B        | $27.84  | 46.03%       | 71.51%       | 1.55x         |
|  2 | SJM      | 2025-06-10 | Before market open | Consumer Defensive | $11.9B       | $110.89 | 17.85%       | 27.53%       | 1.54x         |
|  3 | CNM      | 2025-06-10 | Before market open | Industrials        | $11.7B       | $59.66  | 38.67%       | 49.50%       | 1.28x         |
|  4 | ASO      | 2025-06-10 | Before market open | Consumer Cyclical  | $3.0B        | $43.46  | 59.74%       | 54.12%       | 0.91x         |
|  5 | AII      | 2025-06-09 | After market close | nan                | $332.9M      | $16.95  | nan%         | nan%         | nanx          |
|  6 | CMTL     | 2025-06-09 | After market close | Technology         | $74.5M       | $2.27   | nan%         | nan%         | nanx          |
|  7 | CVGW     | 2025-06-09 | After market close | Consumer Defensive | $493.7M      | $27.68  | nan%         | nan%         | nanx          |
|  8 | DBI      | 2025-06-10 | Before market open | Consumer Cyclical  | $185.7M      | $3.82   | nan%         | nan%         | nanx          |
|  9 | LAKE     | 2025-06-09 | After market close | Consumer Cyclical  | $184.1M      | $18.02  | nan%         | nan%         | nanx          |
| 10 | LMNR     | 2025-06-09 | After market close | Consumer Defensive | $292.0M      | $15.35  | nan%         | nan%         | nanx          |
| 11 | SKIL     | 2025-06-09 | After market close | Consumer Defensive | $154.6M      | $17.86  | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
