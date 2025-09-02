# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-09-01 21:48:38 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector            | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | SIG      | 2025-09-02 | Before market open | Consumer Cyclical | $3.6B        | $89.86  | 47.44%       | 65.35%       | 1.38x         |
|  1 | ASO      | 2025-09-02 | Before market open | Consumer Cyclical | $3.6B        | $53.66  | 44.59%       | 48.36%       | 1.08x         |
|  2 | CISS     | 2025-09-02 | Before market open | Industrials       | $2.4M        | $2.99   | nan%         | nan%         | nanx          |
|  3 | NIO      | 2025-09-02 | Before market open | Consumer Cyclical | $14.6B       | $6.51   | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
