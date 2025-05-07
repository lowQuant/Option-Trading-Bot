# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-05-06 21:52:37 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | RCUS     | 2025-05-06 | After market close | Healthcare             | $946.6M      | $8.94   | 79.25%       | 144.48%      | 1.82x         |
|  1 | LNTH     | 2025-05-07 | Before market open | Healthcare             | $7.4B        | $107.98 | 39.01%       | 69.08%       | 1.77x         |
|  2 | MRCY     | 2025-05-06 | After market close | Industrials            | $3.1B        | $51.16  | 35.48%       | 58.81%       | 1.66x         |
|  3 | GO       | 2025-05-06 | After market close | Consumer Defensive     | $1.6B        | $16.30  | 40.66%       | 62.31%       | 1.53x         |
|  4 | LIVN     | 2025-05-07 | Before market open | Healthcare             | $2.0B        | $36.28  | 39.71%       | 60.71%       | 1.53x         |
|  5 | ANGI     | 2025-05-06 | After market close | Communication Services | $539.4M      | $11.20  | 63.59%       | 91.85%       | 1.44x         |
|  6 | PAYO     | 2025-05-07 | Before market open | Technology             | $2.6B        | $7.11   | 65.21%       | 93.86%       | 1.44x         |
|  7 | PRGO     | 2025-05-07 | Before market open | Healthcare             | $3.4B        | $25.24  | 37.23%       | 52.14%       | 1.40x         |
|  8 | MBC      | 2025-05-06 | After market close | Consumer Cyclical      | $1.6B        | $12.24  | 58.08%       | 81.10%       | 1.40x         |
|  9 | MYGN     | 2025-05-06 | After market close | Healthcare             | $709.7M      | $7.70   | 51.55%       | 71.10%       | 1.38x         |
| 10 | SUPN     | 2025-05-06 | After market close | Healthcare             | $1.8B        | $32.39  | 31.24%       | 42.96%       | 1.38x         |
| 11 | AVA      | 2025-05-07 | Before market open | Utilities              | $3.4B        | $41.95  | 21.08%       | 28.55%       | 1.35x         |
| 12 | EXPI     | 2025-05-06 | After market close | Real Estate            | $1.3B        | $8.72   | 49.31%       | 66.47%       | 1.35x         |
| 13 | DEI      | 2025-05-06 | After market close | Real Estate            | $2.8B        | $14.14  | 55.18%       | 73.69%       | 1.34x         |
| 14 | POWL     | 2025-05-06 | After market close | Industrials            | $2.3B        | $191.96 | 64.41%       | 85.69%       | 1.33x         |
| 15 | GEO      | 2025-05-07 | Before market open | Industrials            | $4.5B        | $31.36  | 52.56%       | 68.34%       | 1.30x         |
| 16 | HALO     | 2025-05-06 | After market close | Healthcare             | $7.5B        | $60.62  | 37.77%       | 48.89%       | 1.29x         |
| 17 | MKTX     | 2025-05-07 | Before market open | Financial Services     | $8.5B        | $226.80 | 27.42%       | 34.47%       | 1.26x         |
| 18 | NYT      | 2025-05-07 | Before market open | Communication Services | $8.6B        | $52.27  | 26.99%       | 33.92%       | 1.26x         |
| 19 | BL       | 2025-05-06 | After market close | Technology             | $3.0B        | $47.15  | 42.72%       | 52.77%       | 1.24x         |
| 20 | COR      | 2025-05-07 | Before market open | Healthcare             | $56.6B       | $291.97 | 20.95%       | 25.68%       | 1.23x         |
| 21 | KMT      | 2025-05-07 | Before market open | Industrials            | $1.5B        | $19.96  | 52.16%       | 63.29%       | 1.21x         |
| 22 | QLYS     | 2025-05-06 | After market close | Technology             | $4.7B        | $128.16 | 39.29%       | 47.54%       | 1.21x         |
| 23 | ANDE     | 2025-05-06 | After market close | Consumer Defensive     | $1.3B        | $36.98  | 39.38%       | 46.68%       | 1.19x         |
| 24 | UTL      | 2025-05-06 | After market close | Utilities              | $971.0M      | $59.26  | 18.82%       | 22.12%       | 1.18x         |
| 25 | MCY      | 2025-05-06 | After market close | Financial Services     | $3.3B        | $58.58  | 41.56%       | 48.22%       | 1.16x         |
| 26 | CYTK     | 2025-05-06 | After market close | Healthcare             | $4.4B        | $36.67  | 73.19%       | 84.31%       | 1.15x         |
| 27 | TDC      | 2025-05-06 | After market close | Technology             | $2.1B        | $22.10  | 55.04%       | 60.49%       | 1.10x         |
| 28 | AMTM     | 2025-05-06 | After market close | Industrials            | $5.4B        | $21.83  | 62.63%       | 68.78%       | 1.10x         |
| 29 | DNOW     | 2025-05-07 | Before market open | Industrials            | $1.7B        | $16.07  | 54.21%       | 58.78%       | 1.08x         |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
