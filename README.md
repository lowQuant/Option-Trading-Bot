# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-09-17 21:41:56 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector             | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | DRI      | 2025-09-18 | Before market open | Consumer Cyclical  | $24.3B       | $210.04 | 13.22%       | 31.46%       | 2.38x         |
|  1 | FDS      | 2025-09-18 | Before market open | Financial Services | $12.7B       | $345.19 | 27.31%       | 38.39%       | 1.41x         |
|  2 | CBRL     | 2025-09-17 | After market close | Consumer Cyclical  | $1.1B        | $51.21  | 57.64%       | 60.31%       | 1.05x         |
|  3 | BLSH     | 2025-09-17 | After market close | Technology         | $7.9B        | $51.36  | nan%         | nan%         | nanx          |
|  4 | NNDM     | 2025-09-17 | After market close | Technology         | $321.6M      | $1.47   | nan%         | nan%         | nanx          |
|  5 | SANG     | 2025-09-17 | After market close | Technology         | $203.9M      | $5.88   | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
