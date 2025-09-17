# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-09-16 21:42:14 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector             | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | GIS      | 2025-09-17 | Before market open | Consumer Defensive | $26.5B       | $49.01  | 16.22%       | 31.79%       | 1.96x         |
|  1 | EPM      | 2025-09-16 | After market close | Energy             | $188.7M      | $5.27   | nan%         | nan%         | nanx          |
|  2 | FLUX     | 2025-09-16 | After market close | Industrials        | $53.0M       | $2.07   | nan%         | nan%         | nanx          |
|  3 | IPHA     | 2025-09-17 | Before market open | Healthcare         | $191.7M      | $2.08   | nan%         | nan%         | nanx          |
|  4 | QSG      | 2025-09-17 | Before market open | Consumer Defensive | $518.8M      | $9.60   | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
