# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-04-08 21:45:55 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector             | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | SMPL     | 2025-04-09 | Before market open | Consumer Defensive | $3.4B        | $33.89  | 24.66%       | 38.02%       | 1.54x         |
|  1 | DAL      | 2025-04-09 | Before market open | Industrials        | $23.2B       | $37.29  | 59.26%       | 83.57%       | 1.41x         |
|  2 | CALM     | 2025-04-08 | After market close | Consumer Defensive | $4.4B        | $93.45  | 48.44%       | 62.88%       | 1.30x         |
|  3 | AEHR     | 2025-04-08 | After market close | Technology         | $201.4M      | $7.22   | nan%         | nan%         | nanx          |
|  4 | KRUS     | 2025-04-08 | After market close | Consumer Cyclical  | $500.3M      | $43.34  | nan%         | nan%         | nanx          |
|  5 | MAMA     | 2025-04-08 | After market close | Consumer Defensive | $259.3M      | $7.04   | nan%         | nan%         | nanx          |
|  6 | NEOG     | 2025-04-09 | Before market open | Healthcare         | $1.5B        | $7.85   | 47.88%       | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
