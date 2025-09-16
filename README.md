# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-09-15 21:42:12 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | PLAY     | 2025-09-15 | After market close | Communication Services | $836.4M      | $23.64  | 54.76%       | 85.36%       | 1.56x         |
|  1 | CSBR     | 2025-09-15 | After market close | Healthcare             | $114.4M      | $6.83   | nan%         | nan%         | nanx          |
|  2 | FERG     | 2025-09-16 | Before market open | Industrials            | $43.1B       | $211.61 | nan%         | nan%         | nanx          |
|  3 | HITI     | 2025-09-15 | After market close | Healthcare             | $320.4M      | $3.43   | nan%         | nan%         | nanx          |
|  4 | OPTT     | 2025-09-15 | After market close | Industrials            | $103.7M      | $0.57   | nan%         | nan%         | nanx          |
|  5 | RLGT     | 2025-09-15 | After market close | Industrials            | $324.3M      | $6.52   | nan%         | nan%         | nanx          |
|  6 | TBHC     | 2025-09-16 | Before market open | Consumer Cyclical      | $53.2M       | $2.37   | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
