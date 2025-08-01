# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-07-31 22:24:04 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | RMD      | 2025-07-31 | After market close | Healthcare             | $39.9B       | $277.44 | 14.01%       | 37.23%       | 2.66x         |
|  1 | WKC      | 2025-07-31 | After market close | Energy                 | $1.5B        | $27.67  | 19.94%       | 49.76%       | 2.50x         |
|  2 | NSP      | 2025-08-01 | Before market open | Industrials            | $2.2B        | $60.19  | 25.53%       | 62.09%       | 2.43x         |
|  3 | OLED     | 2025-07-31 | After market close | Technology             | $6.9B        | $146.45 | 22.20%       | 50.04%       | 2.25x         |
|  4 | MTZ      | 2025-07-31 | After market close | Industrials            | $14.9B       | $189.87 | 21.39%       | 46.35%       | 2.17x         |
|  5 | MPWR     | 2025-07-31 | After market close | Technology             | $34.1B       | $730.54 | 25.31%       | 52.64%       | 2.08x         |
|  6 | APPF     | 2025-07-31 | After market close | Technology             | $9.6B        | $259.20 | 24.76%       | 50.82%       | 2.05x         |
|  7 | INGR     | 2025-08-01 | Before market open | Consumer Defensive     | $8.5B        | $132.11 | 13.65%       | 27.71%       | 2.03x         |
|  8 | NVT      | 2025-08-01 | Before market open | Industrials            | $12.9B       | $78.72  | 20.73%       | 41.68%       | 2.01x         |
|  9 | AAPL     | 2025-07-31 | After market close | Technology             | $3.1tr       | $209.05 | 15.59%       | 30.80%       | 1.98x         |
| 10 | BJRI     | 2025-07-31 | After market close | Consumer Cyclical      | $783.6M      | $36.72  | 32.58%       | 63.79%       | 1.96x         |
| 11 | NVST     | 2025-07-31 | After market close | Healthcare             | $3.2B        | $19.96  | 27.57%       | 52.77%       | 1.91x         |
| 12 | FLR      | 2025-08-01 | Before market open | Industrials            | $9.3B        | $56.03  | 28.26%       | 53.55%       | 1.89x         |
| 13 | REGN     | 2025-08-01 | Before market open | Healthcare             | $58.9B       | $554.58 | 23.91%       | 43.31%       | 1.81x         |
| 14 | PRDO     | 2025-07-31 | After market close | Consumer Defensive     | $1.9B        | $28.65  | 22.39%       | 39.43%       | 1.76x         |
| 15 | SEM      | 2025-07-31 | After market close | Healthcare             | $1.9B        | $14.48  | 25.31%       | 44.50%       | 1.76x         |
| 16 | LUMN     | 2025-07-31 | After market close | Communication Services | $4.6B        | $4.46   | 42.28%       | 74.02%       | 1.75x         |
| 17 | DLB      | 2025-07-31 | After market close | Industrials            | $7.2B        | $75.73  | 14.85%       | 25.96%       | 1.75x         |
| 18 | AMZN     | 2025-07-31 | After market close | Consumer Cyclical      | $2.5tr       | $230.19 | 19.38%       | 33.42%       | 1.72x         |
| 19 | WSC      | 2025-07-31 | After market close | Industrials            | $5.4B        | $30.10  | 34.45%       | 58.13%       | 1.69x         |
| 20 | BEN      | 2025-08-01 | Before market open | Financial Services     | $12.6B       | $24.31  | 18.49%       | 31.19%       | 1.69x         |
| 21 | EIX      | 2025-07-31 | After market close | Utilities              | $20.1B       | $51.69  | 24.85%       | 41.72%       | 1.68x         |
| 22 | CNH      | 2025-08-01 | Before market open | Industrials            | $16.2B       | $12.63  | 27.43%       | 46.03%       | 1.68x         |
| 23 | RGA      | 2025-07-31 | After market close | Financial Services     | $12.7B       | $190.51 | 20.85%       | 34.89%       | 1.67x         |
| 24 | COHU     | 2025-07-31 | After market close | Technology             | $830.5M      | $18.98  | 35.69%       | 59.63%       | 1.67x         |
| 25 | CHD      | 2025-08-01 | Before market open | Consumer Defensive     | $23.1B       | $95.95  | 14.90%       | 24.81%       | 1.67x         |
| 26 | FHI      | 2025-07-31 | After market close | Financial Services     | $3.9B        | $49.70  | 15.56%       | 25.54%       | 1.64x         |
| 27 | OSK      | 2025-08-01 | Before market open | Industrials            | $8.1B        | $125.48 | 24.17%       | 38.53%       | 1.59x         |
| 28 | AVTR     | 2025-08-01 | Before market open | Healthcare             | $9.2B        | $13.80  | 40.27%       | 63.69%       | 1.58x         |
| 29 | NWL      | 2025-08-01 | Before market open | Consumer Defensive     | $2.3B        | $5.72   | 51.30%       | 81.10%       | 1.58x         |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
