# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-09-23 21:44:09 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector            | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | CTAS     | 2025-09-24 | Before market open | Industrials       | $80.8B       | $202.59 | 16.50%       | 31.57%       | 1.91x         |
|  1 | MLKN     | 2025-09-23 | After market close | Consumer Cyclical | $1.3B        | $19.90  | 36.35%       | 62.03%       | 1.71x         |
|  2 | AIR      | 2025-09-23 | After market close | Industrials       | $2.8B        | $76.90  | 30.27%       | 49.80%       | 1.65x         |
|  3 | WOR      | 2025-09-23 | After market close | Industrials       | $3.0B        | $61.03  | 31.70%       | 43.15%       | 1.36x         |
|  4 | MU       | 2025-09-23 | After market close | Technology        | $186.2B      | $164.62 | 46.53%       | 62.30%       | 1.34x         |
|  5 | THO      | 2025-09-24 | Before market open | Consumer Cyclical | $5.4B        | $101.67 | 42.05%       | 50.17%       | 1.19x         |
|  6 | AYTU     | 2025-09-23 | After market close | Healthcare        | $22.5M       | $2.49   | nan%         | nan%         | nanx          |
|  7 | UEC      | 2025-09-24 | Before market open | Energy            | $6.2B        | $13.42  | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
