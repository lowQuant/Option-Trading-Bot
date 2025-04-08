# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-04-07 21:45:57 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | WDFC     | 2025-04-08 | Before market open | Basic Materials        | $3.2B        | $245.09 | 25.97%       | 50.68%       | 1.95x         |
|  1 | GBX      | 2025-04-07 | After market close | Industrials            | $1.4B        | $45.61  | 39.06%       | 75.80%       | 1.94x         |
|  2 | RPM      | 2025-04-08 | Before market open | Basic Materials        | $13.7B       | $108.23 | 26.30%       | 47.93%       | 1.82x         |
|  3 | PLAY     | 2025-04-07 | After market close | Communication Services | $623.4M      | $16.84  | 79.04%       | 116.73%      | 1.48x         |
|  4 | LEVI     | 2025-04-07 | After market close | Consumer Cyclical      | $5.3B        | $13.89  | nan%         | nan%         | nanx          |
|  5 | TLRY     | 2025-04-08 | Before market open | Healthcare             | $541.1M      | $0.59   | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
