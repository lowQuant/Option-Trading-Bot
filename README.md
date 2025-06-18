# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-06-17 21:55:53 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | KFY      | 2025-06-18 | Before market open | Industrials            | $3.5B        | $67.62  | 22.19%       | 49.36%       | 2.22x         |
|  1 | LZB      | 2025-06-17 | After market close | Consumer Cyclical      | $1.6B        | $38.92  | 29.60%       | 47.32%       | 1.60x         |
|  2 | GMS      | 2025-06-18 | Before market open | Industrials            | $2.8B        | $76.14  | 31.38%       | 48.36%       | 1.54x         |
|  3 | ACB      | 2025-06-18 | Before market open | nan                    | $336.3M      | $nan    | nan%         | nan%         | nanx          |
|  4 | LVO      | 2025-06-18 | Before market open | Communication Services | $83.0M       | $0.86   | nan%         | nan%         | nanx          |
|  5 | VTGN     | 2025-06-17 | After market close | Healthcare             | $68.7M       | $2.36   | nan%         | nan%         | nanx          |
|  6 | XAIR     | 2025-06-17 | After market close | Healthcare             | $24.6M       | $0.18   | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
