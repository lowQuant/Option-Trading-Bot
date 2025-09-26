# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-09-25 21:44:28 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector             | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | CNXC     | 2025-09-25 | After market close | Technology         | $3.5B        | $55.60  | 37.57%       | 65.28%       | 1.74x         |
|  1 | COST     | 2025-09-25 | After market close | Consumer Defensive | $419.2B      | $945.27 | 16.31%       | 25.76%       | 1.58x         |
|  2 | KNOP     | 2025-09-26 | Before market open | Energy             | $326.0M      | $9.33   | nan%         | nan%         | nanx          |
|  3 | LPTH     | 2025-09-25 | After market close | Technology         | $294.3M      | $6.86   | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
