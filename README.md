# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-10-09 21:44:46 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | APOG     | 2025-10-09 | After market close | Industrials            | $892.2M      | $43.32  | 36.09%       | 63.96%       | 1.77x         |
|  1 | APLD     | 2025-10-09 | After market close | Technology             | $7.9B        | $27.94  | nan%         | nan%         | nanx          |
|  2 | EDUC     | 2025-10-09 | After market close | Communication Services | $13.8M       | $1.52   | nan%         | nan%         | nanx          |
|  3 | LEVI     | 2025-10-09 | After market close | Consumer Cyclical      | $9.7B        | $24.66  | nan%         | nan%         | nanx          |
|  4 | ODC      | 2025-10-09 | After market close | Basic Materials        | $876.7M      | $60.67  | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
