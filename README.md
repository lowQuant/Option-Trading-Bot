# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-10-19 21:54:42 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector             | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | CLF      | 2025-10-20 | Before market open | Basic Materials    | $6.6B        | $13.56  | 51.59%       | 74.61%       | 1.45x         |
|  1 | DX       | 2025-10-20 | Before market open | Real Estate        | $1.7B        | $13.20  | nan%         | nan%         | nanx          |
|  2 | HBT      | 2025-10-20 | Before market open | Financial Services | $743.3M      | $23.18  | nan%         | nan%         | nanx          |
|  3 | SMMT     | 2025-10-20 | Before market open | Healthcare         | $15.6B       | $21.97  | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
