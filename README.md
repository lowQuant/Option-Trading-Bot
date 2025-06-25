# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-06-24 21:57:37 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | WOR      | 2025-06-24 | After market close | Industrials            | $3.0B        | $59.20  | 22.49%       | 44.38%       | 1.97x         |
|  1 | PAYX     | 2025-06-25 | Before market open | Technology             | $54.8B       | $151.25 | 14.22%       | 26.14%       | 1.84x         |
|  2 | GIS      | 2025-06-25 | Before market open | Consumer Defensive     | $29.2B       | $53.47  | 16.79%       | 30.24%       | 1.80x         |
|  3 | AVAV     | 2025-06-24 | After market close | Industrials            | $8.8B        | $191.23 | 35.43%       | 63.33%       | 1.79x         |
|  4 | FDX      | 2025-06-24 | After market close | Industrials            | $55.0B       | $229.23 | 27.76%       | 42.81%       | 1.54x         |
|  5 | WGO      | 2025-06-25 | Before market open | Consumer Cyclical      | $878.0M      | $31.34  | 46.81%       | 61.10%       | 1.31x         |
|  6 | ATEX     | 2025-06-24 | After market close | Communication Services | $534.9M      | $28.34  | nan%         | nan%         | nanx          |
|  7 | BB       | 2025-06-24 | After market close | Technology             | $2.6B        | $4.32   | nan%         | nan%         | nanx          |
|  8 | CRWS     | 2025-06-25 | Before market open | Consumer Cyclical      | $33.3M       | $3.04   | nan%         | nan%         | nanx          |
|  9 | DAKT     | 2025-06-25 | Before market open | Technology             | $746.5M      | $14.87  | nan%         | nan%         | nanx          |
| 10 | LOT      | 2025-06-25 | Before market open | Consumer Cyclical      | $1.6B        | $2.23   | nan%         | nan%         | nanx          |
| 11 | NG       | 2025-06-25 | Before market open | Basic Materials        | $1.7B        | $4.08   | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
