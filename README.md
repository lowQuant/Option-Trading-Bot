# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-04-29 21:50:19 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | AMSF     | 2025-04-29 | After market close | Financial Services     | $949.5M      | $49.02  | 25.07%       | 81.95%       | 3.27x         |
|  1 | FYBR     | 2025-04-29 | After market close | Communication Services | $9.1B        | $36.25  | 5.02%        | 15.30%       | 3.05x         |
|  2 | LRN      | 2025-04-29 | After market close | Consumer Defensive     | $6.2B        | $140.86 | 32.76%       | 61.65%       | 1.88x         |
|  3 | FDP      | 2025-04-30 | Before market open | Consumer Defensive     | $1.7B        | $34.49  | 23.42%       | 38.52%       | 1.64x         |
|  4 | LANC     | 2025-04-30 | Before market open | Consumer Defensive     | $5.3B        | $189.71 | 23.74%       | 36.37%       | 1.53x         |
|  5 | PSN      | 2025-04-30 | Before market open | Technology             | $7.3B        | $68.32  | 36.44%       | 52.79%       | 1.45x         |
|  6 | SHEN     | 2025-04-30 | Before market open | Communication Services | $714.2M      | $12.83  | 34.47%       | 48.94%       | 1.42x         |
|  7 | VICR     | 2025-04-29 | After market close | Technology             | $2.3B        | $51.53  | 66.82%       | 87.21%       | 1.31x         |
|  8 | CHEF     | 2025-04-30 | Before market open | Consumer Defensive     | $2.2B        | $53.08  | 39.31%       | 50.45%       | 1.28x         |
|  9 | BLKB     | 2025-04-30 | Before market open | Technology             | $3.1B        | $63.85  | 27.21%       | 32.83%       | 1.21x         |
| 10 | HUM      | 2025-04-30 | Before market open | Healthcare             | $31.8B       | $263.20 | 53.18%       | 63.93%       | 1.20x         |
| 11 | NWL      | 2025-04-30 | Before market open | Consumer Defensive     | $2.2B        | $5.11   | 81.00%       | 96.93%       | 1.20x         |
| 12 | ETSY     | 2025-04-30 | Before market open | Consumer Cyclical      | $4.9B        | $45.88  | 50.57%       | 59.05%       | 1.17x         |
| 13 | SR       | 2025-04-30 | Before market open | Utilities              | $4.5B        | $77.39  | 19.09%       | 22.28%       | 1.17x         |
| 14 | HIW      | 2025-04-29 | After market close | Real Estate            | $3.1B        | $28.41  | 38.09%       | 43.91%       | 1.15x         |
| 15 | WING     | 2025-04-30 | Before market open | Consumer Cyclical      | $6.4B        | $224.67 | 53.59%       | 60.31%       | 1.13x         |
| 16 | VMC      | 2025-04-30 | Before market open | Basic Materials        | $32.4B       | $245.39 | 31.14%       | 34.52%       | 1.11x         |
| 17 | ENSG     | 2025-04-29 | After market close | Healthcare             | $7.4B        | $127.07 | 32.74%       | 35.71%       | 1.09x         |
| 18 | SMG      | 2025-04-30 | Before market open | Basic Materials        | $3.1B        | $53.72  | 56.90%       | 61.94%       | 1.09x         |
| 19 | CLH      | 2025-04-30 | Before market open | Industrials            | $11.6B       | $212.63 | 36.52%       | 39.69%       | 1.09x         |
| 20 | DAN      | 2025-04-30 | Before market open | Consumer Cyclical      | $1.9B        | $12.90  | 82.26%       | 89.00%       | 1.08x         |
| 21 | UTHR     | 2025-04-30 | Before market open | Healthcare             | $13.5B       | $297.04 | 37.15%       | 40.10%       | 1.08x         |
| 22 | MDLZ     | 2025-04-29 | After market close | Consumer Defensive     | $85.1B       | $65.10  | 24.90%       | 26.69%       | 1.07x         |
| 23 | OI       | 2025-04-29 | After market close | Consumer Cyclical      | $1.9B        | $11.97  | 53.62%       | 56.73%       | 1.06x         |
| 24 | CSGP     | 2025-04-29 | After market close | Real Estate            | $34.9B       | $81.74  | 42.59%       | 43.94%       | 1.03x         |
| 25 | FSLR     | 2025-04-29 | After market close | Technology             | $15.1B       | $140.73 | 64.05%       | 64.88%       | 1.01x         |
| 26 | ROCK     | 2025-04-30 | Before market open | Industrials            | $1.6B        | $52.59  | 53.06%       | 53.31%       | 1.00x         |
| 27 | NMIH     | 2025-04-29 | After market close | Financial Services     | $2.6B        | $33.47  | 34.00%       | 33.84%       | 1.00x         |
| 28 | NWE      | 2025-04-29 | After market close | Utilities              | $3.6B        | $58.80  | 21.30%       | 20.74%       | 0.97x         |
| 29 | EXLS     | 2025-04-29 | After market close | Technology             | $7.3B        | $44.46  | 38.92%       | 36.79%       | 0.95x         |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
