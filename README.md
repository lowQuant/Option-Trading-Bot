# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-02-25 20:40:16 EST

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector             | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | EYE      | 2025-02-26 | Before market open | Consumer Cyclical  | $900.9M      | $11.66  | 34.76%       | 106.70%      | 3.07x         |
|  1 | ZI       | 2025-02-25 | After market close | Technology         | $3.5B        | $9.64   | 31.58%       | 84.36%       | 2.67x         |
|  2 | PLAB     | 2025-02-26 | Before market open | Technology         | $1.3B        | $21.57  | 23.79%       | 61.34%       | 2.58x         |
|  3 | BCO      | 2025-02-26 | Before market open | Industrials        | $4.1B        | $92.18  | 22.32%       | 45.51%       | 2.04x         |
|  4 | LNTH     | 2025-02-26 | Before market open | Healthcare         | $5.6B        | $78.95  | 40.38%       | 81.99%       | 2.03x         |
|  5 | INTU     | 2025-02-25 | After market close | Technology         | $155.5B      | $567.24 | 19.47%       | 39.44%       | 2.03x         |
|  6 | YOU      | 2025-02-26 | Before market open | Technology         | $3.3B        | $24.13  | 36.71%       | 74.22%       | 2.02x         |
|  7 | TJX      | 2025-02-26 | Before market open | Consumer Cyclical  | $137.9B      | $121.47 | 13.90%       | 26.58%       | 1.91x         |
|  8 | XPEL     | 2025-02-26 | Before market open | Consumer Cyclical  | $1.1B        | $41.02  | 36.17%       | 68.90%       | 1.90x         |
|  9 | EXR      | 2025-02-25 | After market close | Real Estate        | $35.6B       | $159.04 | 16.72%       | 30.72%       | 1.84x         |
| 10 | AAP      | 2025-02-26 | Before market open | Consumer Cyclical  | $2.7B        | $42.81  | 38.98%       | 71.43%       | 1.83x         |
| 11 | JACK     | 2025-02-25 | After market close | Consumer Cyclical  | $640.1M      | $36.78  | 37.46%       | 66.14%       | 1.77x         |
| 12 | MASI     | 2025-02-25 | After market close | Healthcare         | $9.1B        | $170.72 | 30.44%       | 53.65%       | 1.76x         |
| 13 | ENOV     | 2025-02-26 | Before market open | Industrials        | $2.4B        | $43.53  | 29.94%       | 51.03%       | 1.70x         |
| 14 | FSLR     | 2025-02-25 | After market close | Technology         | $15.8B       | $152.91 | 39.12%       | 65.83%       | 1.68x         |
| 15 | MGPI     | 2025-02-26 | Before market open | Consumer Defensive | $715.5M      | $32.83  | 38.12%       | 63.24%       | 1.66x         |
| 16 | SAM      | 2025-02-25 | After market close | Consumer Defensive | $2.7B        | $233.83 | 31.15%       | 51.18%       | 1.64x         |
| 17 | FSS      | 2025-02-26 | Before market open | Industrials        | $5.5B        | $90.78  | 25.88%       | 41.49%       | 1.60x         |
| 18 | GO       | 2025-02-25 | After market close | Consumer Defensive | $1.5B        | $15.80  | 42.38%       | 67.23%       | 1.59x         |
| 19 | OUT      | 2025-02-25 | After market close | Real Estate        | $3.0B        | $18.22  | 27.08%       | 42.53%       | 1.57x         |
| 20 | CART     | 2025-02-25 | After market close | Consumer Cyclical  | $12.5B       | $49.36  | 37.26%       | 58.20%       | 1.56x         |
| 21 | KEYS     | 2025-02-25 | After market close | Technology         | $29.8B       | $173.47 | 28.25%       | 43.61%       | 1.54x         |
| 22 | JAZZ     | 2025-02-25 | After market close | Healthcare         | $8.4B        | $136.69 | 24.79%       | 38.24%       | 1.54x         |
| 23 | WDAY     | 2025-02-25 | After market close | Technology         | $67.9B       | $261.81 | 30.33%       | 45.82%       | 1.51x         |
| 24 | BGS      | 2025-02-25 | After market close | Consumer Defensive | $540.7M      | $6.74   | 41.95%       | 63.16%       | 1.51x         |
| 25 | BLMN     | 2025-02-26 | Before market open | Consumer Cyclical  | $1.0B        | $11.66  | 45.70%       | 67.34%       | 1.47x         |
| 26 | AVNS     | 2025-02-26 | Before market open | Healthcare         | $715.1M      | $15.63  | 38.06%       | 55.63%       | 1.46x         |
| 27 | EXLS     | 2025-02-25 | After market close | Technology         | $7.8B        | $48.21  | 27.54%       | 40.25%       | 1.46x         |
| 28 | ODP      | 2025-02-26 | Before market open | Consumer Cyclical  | $578.0M      | $18.86  | 47.74%       | 69.07%       | 1.45x         |
| 29 | LOW      | 2025-02-26 | Before market open | Consumer Cyclical  | $136.9B      | $237.08 | 22.49%       | 31.37%       | 1.39x         |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
