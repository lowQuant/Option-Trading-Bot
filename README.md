# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-04-24 21:49:45 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | SAM      | 2025-04-24 | After market close | Consumer Defensive     | $2.7B        | $245.42 | 32.93%       | 47.07%       | 1.43x         |
|  1 | WKC      | 2025-04-24 | After market close | Energy                 | $1.4B        | $23.99  | 42.09%       | 57.45%       | 1.36x         |
|  2 | CNC      | 2025-04-25 | Before market open | Healthcare             | $30.5B       | $62.12  | 32.81%       | 44.63%       | 1.36x         |
|  3 | HCA      | 2025-04-25 | Before market open | Healthcare             | $84.1B       | $335.98 | 32.18%       | 43.57%       | 1.35x         |
|  4 | SXT      | 2025-04-25 | Before market open | Basic Materials        | $3.4B        | $79.16  | 32.13%       | 41.19%       | 1.28x         |
|  5 | GNTX     | 2025-04-25 | Before market open | Consumer Cyclical      | $5.0B        | $21.67  | 33.38%       | 42.74%       | 1.28x         |
|  6 | FLG      | 2025-04-25 | Before market open | Financial Services     | $4.7B        | $11.21  | 44.71%       | 56.83%       | 1.27x         |
|  7 | GILD     | 2025-04-24 | After market close | Healthcare             | $132.3B      | $106.38 | 27.22%       | 33.42%       | 1.23x         |
|  8 | APPF     | 2025-04-24 | After market close | Technology             | $8.2B        | $225.66 | 46.72%       | 55.76%       | 1.19x         |
|  9 | EHC      | 2025-04-24 | After market close | Healthcare             | $10.2B       | $100.72 | 36.10%       | 41.50%       | 1.15x         |
| 10 | CHTR     | 2025-04-25 | Before market open | Communication Services | $47.6B       | $337.51 | 47.71%       | 54.62%       | 1.14x         |
| 11 | KNSL     | 2025-04-24 | After market close | Financial Services     | $11.7B       | $491.66 | 42.64%       | 48.54%       | 1.14x         |
| 12 | SPSC     | 2025-04-24 | After market close | Technology             | $5.3B        | $132.52 | 48.84%       | 54.66%       | 1.12x         |
| 13 | GLPI     | 2025-04-24 | After market close | Real Estate            | $13.6B       | $49.56  | 24.95%       | 27.87%       | 1.12x         |
| 14 | POR      | 2025-04-25 | Before market open | Utilities              | $4.7B        | $43.32  | 24.47%       | 26.82%       | 1.10x         |
| 15 | TMUS     | 2025-04-24 | After market close | Communication Services | $298.0B      | $259.35 | 32.51%       | 35.39%       | 1.09x         |
| 16 | PFS      | 2025-04-24 | After market close | Financial Services     | $2.2B        | $16.37  | 46.46%       | 50.50%       | 1.09x         |
| 17 | LKFN     | 2025-04-25 | Before market open | Financial Services     | $1.4B        | $54.49  | 36.66%       | 38.38%       | 1.05x         |
| 18 | MMSI     | 2025-04-24 | After market close | Healthcare             | $5.6B        | $93.76  | 50.19%       | 51.91%       | 1.03x         |
| 19 | VRSN     | 2025-04-24 | After market close | Technology             | $23.8B       | $251.36 | 29.21%       | 29.43%       | 1.01x         |
| 20 | AON      | 2025-04-25 | Before market open | Financial Services     | $78.9B       | $368.83 | 28.87%       | 29.08%       | 1.01x         |
| 21 | PFBC     | 2025-04-25 | Before market open | Financial Services     | $1.1B        | $84.78  | 37.15%       | 36.97%       | 1.00x         |
| 22 | CUBI     | 2025-04-24 | After market close | Financial Services     | $1.6B        | $48.46  | 62.84%       | 60.85%       | 0.97x         |
| 23 | ABBV     | 2025-04-25 | Before market open | Healthcare             | $319.1B      | $177.05 | 36.66%       | 35.48%       | 0.97x         |
| 24 | MTX      | 2025-04-24 | After market close | Basic Materials        | $1.9B        | $57.55  | 43.38%       | 41.76%       | 0.96x         |
| 25 | FFBC     | 2025-04-24 | After market close | Financial Services     | $2.3B        | $23.83  | 41.11%       | 39.51%       | 0.96x         |
| 26 | SSB      | 2025-04-24 | After market close | Financial Services     | $9.1B        | $88.66  | 52.25%       | 50.14%       | 0.96x         |
| 27 | AVTR     | 2025-04-25 | Before market open | Healthcare             | $10.6B       | $15.47  | 56.38%       | 53.83%       | 0.95x         |
| 28 | DLR      | 2025-04-24 | After market close | Real Estate            | $52.7B       | $151.59 | 40.87%       | 39.01%       | 0.95x         |
| 29 | DOC      | 2025-04-24 | After market close | Real Estate            | $13.1B       | $18.82  | 28.40%       | 27.07%       | 0.95x         |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
