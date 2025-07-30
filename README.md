# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-07-29 22:07:34 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | FYBR     | 2025-07-29 | After market close | Communication Services | $9.1B        | $36.60  | 3.40%        | 12.92%       | 3.80x         |
|  1 | UTHR     | 2025-07-30 | Before market open | Healthcare             | $13.4B       | $298.14 | 21.19%       | 57.63%       | 2.72x         |
|  2 | PEN      | 2025-07-29 | After market close | Healthcare             | $8.8B        | $230.17 | 18.07%       | 46.51%       | 2.57x         |
|  3 | CLH      | 2025-07-30 | Before market open | Industrials            | $12.8B       | $234.08 | 14.08%       | 34.91%       | 2.48x         |
|  4 | QRVO     | 2025-07-29 | After market close | Technology             | $7.9B        | $84.32  | 22.04%       | 49.54%       | 2.25x         |
|  5 | STRA     | 2025-07-30 | Before market open | Consumer Defensive     | $1.9B        | $78.90  | 18.67%       | 39.25%       | 2.10x         |
|  6 | REG      | 2025-07-29 | After market close | Real Estate            | $13.1B       | $70.04  | 16.54%       | 33.74%       | 2.04x         |
|  7 | THRY     | 2025-07-30 | Before market open | Communication Services | $531.0M      | $12.21  | 38.58%       | 75.13%       | 1.95x         |
|  8 | WING     | 2025-07-30 | Before market open | Consumer Cyclical      | $8.1B        | $289.44 | 33.03%       | 63.12%       | 1.91x         |
|  9 | OPCH     | 2025-07-30 | Before market open | Healthcare             | $4.9B        | $29.77  | 23.49%       | 44.63%       | 1.90x         |
| 10 | GRMN     | 2025-07-30 | Before market open | Technology             | $46.1B       | $236.36 | 20.99%       | 39.72%       | 1.89x         |
| 11 | ZWS      | 2025-07-29 | After market close | Industrials            | $6.4B        | $38.42  | 19.83%       | 35.56%       | 1.79x         |
| 12 | HAYW     | 2025-07-30 | Before market open | Industrials            | $3.2B        | $14.97  | 27.84%       | 49.86%       | 1.79x         |
| 13 | SMG      | 2025-07-30 | Before market open | Basic Materials        | $3.9B        | $69.16  | 27.32%       | 48.42%       | 1.77x         |
| 14 | FSS      | 2025-07-30 | Before market open | Industrials            | $6.4B        | $107.72 | 20.31%       | 35.81%       | 1.76x         |
| 15 | GTES     | 2025-07-30 | Before market open | Industrials            | $6.4B        | $25.26  | 21.13%       | 37.22%       | 1.76x         |
| 16 | TKR      | 2025-07-30 | Before market open | Industrials            | $5.7B        | $81.69  | 23.79%       | 40.80%       | 1.72x         |
| 17 | WERN     | 2025-07-29 | After market close | Industrials            | $1.7B        | $28.61  | 30.15%       | 51.50%       | 1.71x         |
| 18 | GEHC     | 2025-07-30 | Before market open | Healthcare             | $35.6B       | $77.74  | 22.34%       | 37.92%       | 1.70x         |
| 19 | SBUX     | 2025-07-29 | After market close | Consumer Cyclical      | $105.6B      | $93.67  | 22.80%       | 38.62%       | 1.69x         |
| 20 | ARI      | 2025-07-29 | After market close | Real Estate            | $1.4B        | $9.76   | 14.17%       | 23.81%       | 1.68x         |
| 21 | LXP      | 2025-07-30 | Before market open | Real Estate            | $2.4B        | $7.93   | 21.55%       | 35.46%       | 1.65x         |
| 22 | WSO      | 2025-07-30 | Before market open | Industrials            | $18.6B       | $479.86 | 22.06%       | 35.98%       | 1.63x         |
| 23 | MCY      | 2025-07-29 | After market close | Financial Services     | $3.9B        | $69.92  | 25.70%       | 41.91%       | 1.63x         |
| 24 | EA       | 2025-07-29 | After market close | Communication Services | $37.1B       | $151.99 | 19.14%       | 30.98%       | 1.62x         |
| 25 | HIW      | 2025-07-29 | After market close | Real Estate            | $3.3B        | $29.73  | 17.65%       | 28.52%       | 1.62x         |
| 26 | GNRC     | 2025-07-30 | Before market open | Industrials            | $8.9B        | $155.46 | 28.10%       | 45.03%       | 1.60x         |
| 27 | NAVI     | 2025-07-30 | Before market open | Financial Services     | $1.4B        | $14.06  | 34.94%       | 55.19%       | 1.58x         |
| 28 | TER      | 2025-07-29 | After market close | Technology             | $14.5B       | $91.14  | 34.95%       | 55.20%       | 1.58x         |
| 29 | STX      | 2025-07-29 | After market close | Technology             | $32.4B       | $150.46 | 27.55%       | 43.16%       | 1.57x         |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
