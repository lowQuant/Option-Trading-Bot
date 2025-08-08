# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-08-07 22:08:28 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | VIAV     | 2025-08-07 | After market close | Technology             | $2.3B        | $10.04  | 18.80%       | 52.84%       | 2.81x         |
|  1 | HCI      | 2025-08-07 | After market close | Financial Services     | $1.6B        | $139.86 | 18.32%       | 50.68%       | 2.77x         |
|  2 | ATGE     | 2025-08-07 | After market close | Consumer Defensive     | $4.3B        | $119.82 | 21.53%       | 56.50%       | 2.62x         |
|  3 | G        | 2025-08-07 | After market close | Technology             | $7.3B        | $42.20  | 23.99%       | 61.61%       | 2.57x         |
|  4 | CARG     | 2025-08-07 | After market close | Consumer Cyclical      | $3.1B        | $31.81  | 21.42%       | 54.76%       | 2.56x         |
|  5 | AKAM     | 2025-08-07 | After market close | Technology             | $10.6B       | $74.48  | 20.03%       | 50.32%       | 2.51x         |
|  6 | DOCS     | 2025-08-07 | After market close | Healthcare             | $11.0B       | $58.13  | 33.35%       | 77.07%       | 2.31x         |
|  7 | ARLO     | 2025-08-07 | After market close | Industrials            | $1.7B        | $16.10  | 32.50%       | 72.13%       | 2.22x         |
|  8 | TRUP     | 2025-08-07 | After market close | Financial Services     | $2.1B        | $48.63  | 32.31%       | 70.20%       | 2.17x         |
|  9 | CON      | 2025-08-07 | After market close | Healthcare             | $2.6B        | $19.94  | 25.84%       | 52.19%       | 2.02x         |
| 10 | GDDY     | 2025-08-07 | After market close | Technology             | $22.1B       | $154.82 | 19.26%       | 38.38%       | 1.99x         |
| 11 | CRSR     | 2025-08-07 | After market close | Technology             | $942.9M      | $8.91   | 35.62%       | 70.97%       | 1.99x         |
| 12 | TTD      | 2025-08-07 | After market close | Communication Services | $43.8B       | $89.58  | 37.16%       | 74.02%       | 1.99x         |
| 13 | FOXF     | 2025-08-07 | After market close | Consumer Cyclical      | $1.3B        | $29.22  | 48.86%       | 97.08%       | 1.99x         |
| 14 | AGO      | 2025-08-07 | After market close | Financial Services     | $4.2B        | $86.17  | 16.20%       | 32.05%       | 1.98x         |
| 15 | TTWO     | 2025-08-07 | After market close | Communication Services | $41.9B       | $227.21 | 17.27%       | 33.76%       | 1.95x         |
| 16 | SLVM     | 2025-08-08 | Before market open | Basic Materials        | $1.9B        | $47.40  | 32.93%       | 62.21%       | 1.89x         |
| 17 | SYNA     | 2025-08-07 | After market close | Technology             | $2.3B        | $60.10  | 30.97%       | 57.45%       | 1.86x         |
| 18 | ALRM     | 2025-08-07 | After market close | Technology             | $2.8B        | $55.77  | 20.36%       | 37.06%       | 1.82x         |
| 19 | DVAX     | 2025-08-07 | After market close | Healthcare             | $1.3B        | $11.19  | 23.97%       | 43.31%       | 1.81x         |
| 20 | AMN      | 2025-08-07 | After market close | Healthcare             | $657.8M      | $17.22  | 49.15%       | 87.19%       | 1.77x         |
| 21 | YELP     | 2025-08-07 | After market close | Communication Services | $2.2B        | $34.15  | 23.55%       | 41.69%       | 1.77x         |
| 22 | ICUI     | 2025-08-07 | After market close | Healthcare             | $3.2B        | $126.89 | 30.60%       | 53.91%       | 1.76x         |
| 23 | QNST     | 2025-08-07 | After market close | Communication Services | $961.3M      | $16.88  | 33.77%       | 59.44%       | 1.76x         |
| 24 | CYTK     | 2025-08-07 | After market close | Healthcare             | $4.2B        | $35.14  | 39.02%       | 66.73%       | 1.71x         |
| 25 | EXPE     | 2025-08-07 | After market close | Consumer Cyclical      | $23.5B       | $185.14 | 29.77%       | 50.89%       | 1.71x         |
| 26 | SHC      | 2025-08-08 | Before market open | Healthcare             | $3.2B        | $11.06  | 31.49%       | 52.98%       | 1.68x         |
| 27 | GEN      | 2025-08-07 | After market close | Technology             | $17.7B       | $28.69  | 21.88%       | 36.61%       | 1.67x         |
| 28 | UAA      | 2025-08-08 | Before market open | Consumer Cyclical      | $2.8B        | $6.73   | 35.26%       | 58.99%       | 1.67x         |
| 29 | MSI      | 2025-08-07 | After market close | Technology             | $74.3B       | $442.12 | 14.21%       | 23.73%       | 1.67x         |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
