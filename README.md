# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-09-11 21:41:06 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector             | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | ADBE     | 2025-09-11 | After market close | Technology         | $148.7B      | $350.16 | 28.91%       | 53.34%       | 1.85x         |
|  1 | FARM     | 2025-09-11 | After market close | Consumer Defensive | $50.2M       | $1.96   | nan%         | nan%         | nanx          |
|  2 | HUIZ     | 2025-09-12 | Before market open | Financial Services | $27.5M       | $2.73   | nan%         | nan%         | nanx          |
|  3 | IBEX     | 2025-09-11 | After market close | Technology         | $407.3M      | $28.92  | nan%         | nan%         | nanx          |
|  4 | KMTS     | 2025-09-11 | After market close | Healthcare         | $944.8M      | $18.19  | nan%         | nan%         | nanx          |
|  5 | RENT     | 2025-09-11 | After market close | Consumer Cyclical  | $31.1M       | $6.09   | nan%         | nan%         | nanx          |
|  6 | RFIL     | 2025-09-11 | After market close | Industrials        | $91.1M       | $7.68   | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
