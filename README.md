# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-09-24 21:44:50 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector            | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | WS       | 2025-09-24 | After market close | Basic Materials   | $1.7B        | $33.05  | 37.46%       | 81.52%       | 2.18x         |
|  1 | ACN      | 2025-09-25 | Before market open | Technology        | $148.9B      | $235.50 | 22.68%       | 45.06%       | 1.99x         |
|  2 | KMX      | 2025-09-25 | Before market open | Consumer Cyclical | $8.6B        | $57.60  | 31.46%       | 58.36%       | 1.86x         |
|  3 | SNX      | 2025-09-25 | Before market open | Technology        | $12.4B       | $151.88 | 21.72%       | 36.14%       | 1.66x         |
|  4 | JBL      | 2025-09-25 | Before market open | Technology        | $24.2B       | $234.45 | 33.28%       | 54.60%       | 1.64x         |
|  5 | KBH      | 2025-09-24 | After market close | Consumer Cyclical | $4.2B        | $62.41  | 36.35%       | 42.72%       | 1.18x         |
|  6 | FUL      | 2025-09-24 | After market close | Basic Materials   | $3.2B        | $59.62  | 33.37%       | 30.76%       | 0.92x         |
|  7 | BB       | 2025-09-25 | Before market open | Technology        | $2.5B        | $4.27   | nan%         | nan%         | nanx          |
|  8 | IVA      | 2025-09-25 | Before market open | Healthcare        | $767.6M      | $5.67   | nan%         | nan%         | nanx          |
|  9 | LUXE     | 2025-09-25 | Before market open | Consumer Cyclical | $1.1B        | $8.25   | nan%         | nan%         | nanx          |
| 10 | SCS      | 2025-09-24 | After market close | Consumer Cyclical | $1.9B        | $16.87  | nan%         | nan%         | nanx          |
| 11 | SFIX     | 2025-09-24 | After market close | Consumer Cyclical | $735.9M      | $5.46   | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
