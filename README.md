# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-05-23 21:48:37 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close    | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:---------|:-------------|:-------------|:--------------|
|  0 | SKY      | 2025-05-27 | Before market open | Consumer Cyclical      | $4.8B        | $85.66   | 32.84%       | 54.20%       | 1.65x         |
|  1 | AZO      | 2025-05-27 | Before market open | Consumer Cyclical      | $64.0B       | $3859.25 | 20.65%       | 28.10%       | 1.36x         |
|  2 | ZH       | 2025-05-27 | Before market open | Communication Services | $346.4M      | $4.01    | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
