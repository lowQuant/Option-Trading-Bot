# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-09-10 21:44:48 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | KR       | 2025-09-11 | Before market open | Consumer Defensive     | $44.3B       | $67.63  | 22.28%       | 31.33%       | 1.41x         |
|  1 | OXM      | 2025-09-10 | After market close | Consumer Cyclical      | $603.5M      | $40.75  | 48.19%       | 67.69%       | 1.40x         |
|  2 | AENT     | 2025-09-10 | After market close | Communication Services | $355.0M      | $5.90   | nan%         | nan%         | nanx          |
|  3 | CMCM     | 2025-09-11 | Before market open | Communication Services | $226.5M      | $7.08   | nan%         | nan%         | nanx          |
|  4 | HOFT     | 2025-09-11 | Before market open | Consumer Cyclical      | $117.5M      | $10.85  | nan%         | nan%         | nanx          |
|  5 | KALV     | 2025-09-11 | Before market open | Healthcare             | $774.7M      | $15.61  | nan%         | nan%         | nanx          |
|  6 | KEQU     | 2025-09-10 | After market close | Consumer Cyclical      | $161.2M      | $53.68  | nan%         | nan%         | nanx          |
|  7 | LOVE     | 2025-09-11 | Before market open | Consumer Cyclical      | $301.9M      | $19.30  | nan%         | nan%         | nanx          |
|  8 | LSAK     | 2025-09-10 | After market close | Technology             | $384.3M      | $4.65   | nan%         | nan%         | nanx          |
|  9 | VNCE     | 2025-09-10 | After market close | Consumer Cyclical      | $21.3M       | $1.50   | nan%         | nan%         | nanx          |
| 10 | VRA      | 2025-09-11 | Before market open | Consumer Cyclical      | $63.7M       | $2.30   | nan%         | nan%         | nanx          |
| 11 | ZENV     | 2025-09-10 | After market close | Technology             | $93.6M       | $1.55   | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
