# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-11-06 20:52:16 EST

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | TDS      | 2025-11-07 | Before market open | Communication Services | $4.4B        | $38.77  | 19.09%       | 56.62%       | 2.97x         |
|  1 | TRUP     | 2025-11-06 | After market close | Financial Services     | $1.8B        | $42.49  | 31.80%       | 83.71%       | 2.63x         |
|  2 | G        | 2025-11-06 | After market close | Technology             | $6.7B        | $38.82  | 17.41%       | 43.46%       | 2.50x         |
|  3 | CON      | 2025-11-06 | After market close | Healthcare             | $2.4B        | $19.14  | 18.53%       | 45.63%       | 2.46x         |
|  4 | BILL     | 2025-11-06 | After market close | Technology             | $4.5B        | $46.52  | 30.61%       | 72.10%       | 2.36x         |
|  5 | ANIP     | 2025-11-07 | Before market open | Healthcare             | $2.0B        | $92.62  | 23.70%       | 55.37%       | 2.34x         |
|  6 | TTD      | 2025-11-06 | After market close | Communication Services | $22.4B       | $47.70  | 40.45%       | 93.74%       | 2.32x         |
|  7 | ABNB     | 2025-11-06 | After market close | Consumer Cyclical      | $73.8B       | $122.50 | 20.69%       | 47.88%       | 2.31x         |
|  8 | DV       | 2025-11-07 | Before market open | Communication Services | $1.8B        | $11.15  | 31.82%       | 73.40%       | 2.31x         |
|  9 | AKAM     | 2025-11-06 | After market close | Technology             | $10.5B       | $72.98  | 25.94%       | 59.06%       | 2.28x         |
| 10 | TTWO     | 2025-11-06 | After market close | Communication Services | $46.6B       | $254.76 | 20.24%       | 44.00%       | 2.17x         |
| 11 | SOLV     | 2025-11-06 | After market close | Healthcare             | $11.5B       | $67.69  | 17.65%       | 38.08%       | 2.16x         |
| 12 | KOP      | 2025-11-07 | Before market open | Basic Materials        | $548.9M      | $28.05  | 28.09%       | 59.80%       | 2.13x         |
| 13 | BL       | 2025-11-06 | After market close | Technology             | $3.5B        | $56.92  | 31.27%       | 65.09%       | 2.08x         |
| 14 | ARLO     | 2025-11-06 | After market close | Industrials            | $1.8B        | $17.71  | 34.63%       | 71.64%       | 2.07x         |
| 15 | FLO      | 2025-11-06 | After market close | Consumer Defensive     | $2.5B        | $12.10  | 23.57%       | 47.47%       | 2.01x         |
| 16 | MKTX     | 2025-11-07 | Before market open | Financial Services     | $6.2B        | $161.00 | 21.82%       | 42.96%       | 1.97x         |
| 17 | GMED     | 2025-11-06 | After market close | Healthcare             | $8.3B        | $61.51  | 28.61%       | 56.19%       | 1.96x         |
| 18 | AORT     | 2025-11-06 | After market close | Healthcare             | $2.2B        | $46.51  | 21.31%       | 41.71%       | 1.96x         |
| 19 | CARG     | 2025-11-06 | After market close | Consumer Cyclical      | $3.3B        | $34.06  | 29.89%       | 56.69%       | 1.90x         |
| 20 | DOCS     | 2025-11-06 | After market close | Healthcare             | $11.7B       | $63.99  | 40.04%       | 74.25%       | 1.85x         |
| 21 | GEN      | 2025-11-06 | After market close | Technology             | $15.7B       | $25.84  | 19.02%       | 34.80%       | 1.83x         |
| 22 | BLFS     | 2025-11-06 | After market close | Healthcare             | $1.3B        | $27.57  | 35.45%       | 63.73%       | 1.80x         |
| 23 | HRB      | 2025-11-06 | After market close | Consumer Cyclical      | $6.6B        | $50.58  | 20.46%       | 36.47%       | 1.78x         |
| 24 | PCRX     | 2025-11-06 | After market close | Healthcare             | $948.1M      | $21.85  | 32.34%       | 56.65%       | 1.75x         |
| 25 | CE       | 2025-11-06 | After market close | Basic Materials        | $4.0B        | $36.94  | 52.02%       | 90.21%       | 1.73x         |
| 26 | WSC      | 2025-11-06 | After market close | Industrials            | $3.6B        | $20.79  | 32.39%       | 55.30%       | 1.71x         |
| 27 | DBX      | 2025-11-06 | After market close | Technology             | $7.7B        | $29.13  | 27.01%       | 46.00%       | 1.70x         |
| 28 | ICUI     | 2025-11-06 | After market close | Healthcare             | $3.2B        | $127.38 | 33.35%       | 56.76%       | 1.70x         |
| 29 | ASTH     | 2025-11-06 | After market close | Healthcare             | $1.5B        | $33.24  | 42.08%       | 71.26%       | 1.69x         |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
