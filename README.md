# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-06-11 21:55:03 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               |   sector | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|---------:|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | ORCL     | 2025-06-11 | After market close |      nan | $494.6B      | $nan    | 26.40%       | 41.19%       | 1.56x         |
|  1 | OXM      | 2025-06-11 | After market close |      nan | $744.2M      | $nan    | 44.41%       | 55.18%       | 1.24x         |
|  2 | CRMT     | 2025-06-12 | Before market open |      nan | $477.0M      | $nan    | nan%         | nan%         | nanx          |
|  3 | HOFT     | 2025-06-12 | Before market open |      nan | $121.6M      | $nan    | nan%         | nan%         | nanx          |
|  4 | LOVE     | 2025-06-12 | Before market open |      nan | $304.3M      | $nan    | nan%         | nan%         | nanx          |
|  5 | TOUR     | 2025-06-12 | Before market open |      nan | $112.6M      | $nan    | nan%         | nan%         | nanx          |
|  6 | YRD      | 2025-06-12 | Before market open |      nan | $642.0M      | $nan    | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
