# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-07-18 21:59:01 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | ROP      | 2025-07-21 | Before market open | Technology             | $58.6B       | $546.35 | 13.26%       | 22.14%       | 1.67x         |
|  1 | DPZ      | 2025-07-21 | Before market open | Consumer Cyclical      | $16.0B       | $468.70 | 21.33%       | 33.05%       | 1.55x         |
|  2 | VZ       | 2025-07-21 | Before market open | Communication Services | $172.2B      | $40.95  | 15.77%       | 23.70%       | 1.50x         |
|  3 | PFBC     | 2025-07-21 | Before market open | Financial Services     | $1.2B        | $93.03  | 25.36%       | 28.23%       | 1.11x         |
|  4 | CLF      | 2025-07-21 | Before market open | Basic Materials        | $4.7B        | $9.39   | 70.08%       | 70.50%       | 1.01x         |
|  5 | DX       | 2025-07-21 | Before market open | Real Estate            | $1.3B        | $12.58  | nan%         | nan%         | nanx          |
|  6 | HBT      | 2025-07-21 | Before market open | Financial Services     | $797.1M      | $25.72  | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
