# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-06-18 21:56:45 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector             | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | KMX      | 2025-06-20 | Before market open | Consumer Cyclical  | $9.8B        | $64.43  | 30.55%       | 53.76%       | 1.76x         |
|  1 | ACN      | 2025-06-20 | Before market open | Technology         | $195.3B      | $312.03 | 20.37%       | 35.66%       | 1.75x         |
|  2 | KR       | 2025-06-20 | Before market open | Consumer Defensive | $43.9B       | $65.95  | 20.32%       | 30.46%       | 1.50x         |
|  3 | DRI      | 2025-06-20 | Before market open | Consumer Cyclical  | $26.3B       | $224.78 | 22.83%       | 33.60%       | 1.47x         |
|  4 | SWBI     | 2025-06-18 | After market close | Industrials        | $478.7M      | $10.49  | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
