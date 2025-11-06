# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-11-05 20:54:04 EST

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | HBI      | 2025-11-06 | Before market open | Consumer Cyclical      | $2.3B        | $6.47   | 19.40%       | 61.61%       | 3.18x         |
|  1 | LNTH     | 2025-11-06 | Before market open | Healthcare             | $3.9B        | $57.71  | 32.10%       | 88.04%       | 2.74x         |
|  2 | JAZZ     | 2025-11-05 | After market close | Healthcare             | $8.3B        | $137.82 | 20.55%       | 55.09%       | 2.68x         |
|  3 | DVAX     | 2025-11-05 | After market close | Healthcare             | $1.2B        | $10.05  | 27.34%       | 71.72%       | 2.62x         |
|  4 | UAA      | 2025-11-06 | Before market open | Consumer Cyclical      | $1.9B        | $4.48   | 26.75%       | 67.22%       | 2.51x         |
|  5 | ADMA     | 2025-11-05 | After market close | Healthcare             | $3.7B        | $14.63  | 39.53%       | 97.59%       | 2.47x         |
|  6 | EFC      | 2025-11-05 | After market close | Real Estate            | $1.4B        | $13.69  | 13.71%       | 33.46%       | 2.44x         |
|  7 | RAL      | 2025-11-05 | After market close | Technology             | $5.0B        | $43.18  | 26.42%       | 64.24%       | 2.43x         |
|  8 | PODD     | 2025-11-06 | Before market open | Healthcare             | $22.1B       | $320.27 | 21.86%       | 52.99%       | 2.42x         |
|  9 | AMCR     | 2025-11-05 | After market close | Consumer Cyclical      | $18.6B       | $7.87   | 20.16%       | 48.61%       | 2.41x         |
| 10 | GVA      | 2025-11-06 | Before market open | Industrials            | $4.5B        | $102.40 | 13.42%       | 32.35%       | 2.41x         |
| 11 | FTNT     | 2025-11-05 | After market close | Technology             | $65.9B       | $85.22  | 22.56%       | 53.48%       | 2.37x         |
| 12 | USPH     | 2025-11-05 | After market close | Healthcare             | $1.3B        | $87.04  | 23.53%       | 55.26%       | 2.35x         |
| 13 | LNW      | 2025-11-05 | After market close | Consumer Cyclical      | $6.2B        | $73.33  | 25.05%       | 57.97%       | 2.31x         |
| 14 | CCOI     | 2025-11-06 | Before market open | Communication Services | $1.9B        | $39.96  | 39.32%       | 89.91%       | 2.29x         |
| 15 | VTRS     | 2025-11-06 | Before market open | Healthcare             | $12.4B       | $10.49  | 18.80%       | 42.69%       | 2.27x         |
| 16 | SATS     | 2025-11-06 | Before market open | Communication Services | $20.8B       | $73.48  | 29.00%       | 64.15%       | 2.21x         |
| 17 | HAE      | 2025-11-06 | Before market open | Healthcare             | $2.4B        | $50.38  | 30.21%       | 65.61%       | 2.17x         |
| 18 | PAHC     | 2025-11-05 | After market close | Healthcare             | $1.7B        | $42.11  | 34.56%       | 73.90%       | 2.14x         |
| 19 | FWRD     | 2025-11-05 | After market close | Industrials            | $544.7M      | $18.14  | 49.98%       | 105.38%      | 2.11x         |
| 20 | ROK      | 2025-11-06 | Before market open | Industrials            | $40.8B       | $359.85 | 19.27%       | 40.48%       | 2.10x         |
| 21 | COTY     | 2025-11-05 | After market close | Consumer Defensive     | $3.3B        | $3.83   | 39.03%       | 81.49%       | 2.09x         |
| 22 | UA       | 2025-11-06 | Before market open | Consumer Cyclical      | $1.9B        | $4.30   | 26.39%       | 55.00%       | 2.08x         |
| 23 | USFD     | 2025-11-06 | Before market open | Consumer Defensive     | $16.7B       | $73.39  | 17.00%       | 34.31%       | 2.02x         |
| 24 | FOUR     | 2025-11-06 | Before market open | Technology             | $5.9B        | $66.74  | 38.40%       | 76.72%       | 2.00x         |
| 25 | WMS      | 2025-11-06 | Before market open | Industrials            | $10.5B       | $135.75 | 28.32%       | 56.54%       | 2.00x         |
| 26 | BGC      | 2025-11-06 | Before market open | Financial Services     | $4.3B        | $9.21   | 22.95%       | 45.80%       | 2.00x         |
| 27 | PEB      | 2025-11-05 | After market close | Real Estate            | $1.2B        | $10.28  | 25.24%       | 50.26%       | 1.99x         |
| 28 | NATL     | 2025-11-05 | After market close | Technology             | $2.8B        | $36.69  | 24.22%       | 47.89%       | 1.98x         |
| 29 | SGI      | 2025-11-06 | Before market open | Consumer Cyclical      | $16.7B       | $80.11  | 21.27%       | 41.38%       | 1.95x         |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
