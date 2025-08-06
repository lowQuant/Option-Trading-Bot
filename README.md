# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-08-05 22:08:43 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | LRN      | 2025-08-05 | After market close | Consumer Defensive     | $5.6B        | $130.31 | 18.44%       | 58.16%       | 3.15x         |
|  1 | JAZZ     | 2025-08-05 | After market close | Healthcare             | $6.8B        | $116.10 | 22.50%       | 64.62%       | 2.87x         |
|  2 | PRGO     | 2025-08-06 | Before market open | Healthcare             | $3.7B        | $26.96  | 19.69%       | 52.07%       | 2.64x         |
|  3 | BL       | 2025-08-05 | After market close | Technology             | $3.4B        | $53.50  | 23.78%       | 57.25%       | 2.41x         |
|  4 | NWS      | 2025-08-05 | After market close | Communication Services | $17.4B       | $33.60  | 14.51%       | 34.63%       | 2.39x         |
|  5 | DV       | 2025-08-05 | After market close | Technology             | $2.5B        | $15.45  | 26.99%       | 63.95%       | 2.37x         |
|  6 | EYE      | 2025-08-06 | Before market open | Consumer Cyclical      | $2.0B        | $25.07  | 31.42%       | 72.09%       | 2.29x         |
|  7 | TRMB     | 2025-08-06 | Before market open | Technology             | $19.7B       | $84.25  | 15.66%       | 35.33%       | 2.26x         |
|  8 | ANGI     | 2025-08-05 | After market close | Communication Services | $752.0M      | $16.29  | 40.15%       | 89.04%       | 2.22x         |
|  9 | NWSA     | 2025-08-05 | After market close | Communication Services | $17.3B       | $29.51  | 13.93%       | 30.04%       | 2.16x         |
| 10 | PCRX     | 2025-08-05 | After market close | Healthcare             | $1.0B        | $22.94  | 35.12%       | 72.35%       | 2.06x         |
| 11 | EXTR     | 2025-08-06 | Before market open | Technology             | $2.4B        | $18.07  | 27.73%       | 56.92%       | 2.05x         |
| 12 | ROK      | 2025-08-06 | Before market open | Industrials            | $39.0B       | $350.16 | 17.64%       | 36.18%       | 2.05x         |
| 13 | DIS      | 2025-08-06 | Before market open | Communication Services | $212.7B      | $119.35 | 16.84%       | 33.69%       | 2.00x         |
| 14 | PAYO     | 2025-08-06 | Before market open | Technology             | $2.4B        | $6.35   | 42.16%       | 83.06%       | 1.97x         |
| 15 | PSN      | 2025-08-06 | Before market open | Technology             | $8.2B        | $74.60  | 22.60%       | 44.46%       | 1.97x         |
| 16 | CWEN     | 2025-08-05 | After market close | Utilities              | $6.3B        | $32.70  | 20.79%       | 40.86%       | 1.97x         |
| 17 | GEO      | 2025-08-06 | Before market open | Industrials            | $3.7B        | $24.90  | 37.66%       | 72.70%       | 1.93x         |
| 18 | AMTM     | 2025-08-05 | After market close | Industrials            | $6.2B        | $24.48  | 32.03%       | 61.35%       | 1.92x         |
| 19 | AEIS     | 2025-08-05 | After market close | Industrials            | $5.3B        | $140.56 | 26.51%       | 50.67%       | 1.91x         |
| 20 | TDC      | 2025-08-05 | After market close | Technology             | $1.9B        | $20.36  | 31.63%       | 60.22%       | 1.90x         |
| 21 | SWKS     | 2025-08-05 | After market close | Technology             | $10.2B       | $67.94  | 25.02%       | 47.07%       | 1.88x         |
| 22 | GO       | 2025-08-05 | After market close | Consumer Defensive     | $1.3B        | $13.42  | 35.74%       | 66.88%       | 1.87x         |
| 23 | MKTX     | 2025-08-06 | Before market open | Financial Services     | $7.8B        | $209.43 | 20.47%       | 38.18%       | 1.87x         |
| 24 | HALO     | 2025-08-05 | After market close | Healthcare             | $7.5B        | $59.99  | 25.00%       | 46.57%       | 1.86x         |
| 25 | XPEL     | 2025-08-06 | Before market open | Consumer Cyclical      | $906.0M      | $33.23  | 39.90%       | 72.89%       | 1.83x         |
| 26 | NYT      | 2025-08-06 | Before market open | Communication Services | $8.7B        | $53.75  | 17.22%       | 31.32%       | 1.82x         |
| 27 | WWW      | 2025-08-06 | Before market open | Consumer Cyclical      | $1.9B        | $22.88  | 40.88%       | 73.41%       | 1.80x         |
| 28 | PLNT     | 2025-08-06 | Before market open | Consumer Cyclical      | $9.2B        | $110.28 | 24.46%       | 43.52%       | 1.78x         |
| 29 | GFF      | 2025-08-06 | Before market open | Industrials            | $3.9B        | $81.55  | 27.07%       | 47.86%       | 1.77x         |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
