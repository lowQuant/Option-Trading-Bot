# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-08-06 22:09:38 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | GVA      | 2025-08-07 | Before market open | Industrials            | $4.1B        | $94.50  | 16.92%       | 41.56%       | 2.46x         |
|  1 | RBA      | 2025-08-06 | After market close | Industrials            | $20.3B       | $109.58 | 14.29%       | 33.00%       | 2.31x         |
|  2 | RAMP     | 2025-08-06 | After market close | Technology             | $2.1B        | $32.05  | 27.69%       | 61.89%       | 2.24x         |
|  3 | RL       | 2025-08-07 | Before market open | Consumer Cyclical      | $18.1B       | $299.24 | 20.04%       | 44.55%       | 2.22x         |
|  4 | VRRM     | 2025-08-06 | After market close | Technology             | $4.0B        | $25.14  | 21.78%       | 47.05%       | 2.16x         |
|  5 | CTVA     | 2025-08-06 | After market close | Basic Materials        | $48.6B       | $72.31  | 16.53%       | 35.62%       | 2.15x         |
|  6 | LOPE     | 2025-08-06 | After market close | Consumer Defensive     | $4.9B        | $167.66 | 18.22%       | 39.23%       | 2.15x         |
|  7 | ADMA     | 2025-08-06 | After market close | Healthcare             | $4.4B        | $18.96  | 37.06%       | 79.77%       | 2.15x         |
|  8 | NTCT     | 2025-08-07 | Before market open | Technology             | $1.6B        | $21.39  | 28.74%       | 58.80%       | 2.05x         |
|  9 | HAE      | 2025-08-07 | Before market open | Healthcare             | $3.7B        | $76.11  | 24.20%       | 49.15%       | 2.03x         |
| 10 | AOSL     | 2025-08-06 | After market close | Technology             | $779.7M      | $26.07  | 44.33%       | 87.47%       | 1.97x         |
| 11 | ACAD     | 2025-08-06 | After market close | Healthcare             | $4.0B        | $23.64  | 32.30%       | 63.42%       | 1.96x         |
| 12 | ECPG     | 2025-08-06 | After market close | Financial Services     | $874.0M      | $36.64  | 30.36%       | 59.07%       | 1.95x         |
| 13 | APLE     | 2025-08-06 | After market close | Real Estate            | $2.8B        | $11.71  | 23.31%       | 45.18%       | 1.94x         |
| 14 | STE      | 2025-08-06 | After market close | Healthcare             | $21.8B       | $223.87 | 16.36%       | 31.62%       | 1.93x         |
| 15 | SABR     | 2025-08-07 | Before market open | Technology             | $1.2B        | $2.98   | 43.81%       | 83.13%       | 1.90x         |
| 16 | PRVA     | 2025-08-07 | Before market open | Healthcare             | $2.4B        | $19.45  | 34.50%       | 64.93%       | 1.88x         |
| 17 | MTSI     | 2025-08-07 | Before market open | Technology             | $10.3B       | $137.28 | 25.39%       | 47.78%       | 1.88x         |
| 18 | HBI      | 2025-08-07 | Before market open | Consumer Cyclical      | $1.5B        | $4.21   | 34.70%       | 64.82%       | 1.87x         |
| 19 | PODD     | 2025-08-07 | Before market open | Healthcare             | $19.5B       | $281.00 | 24.71%       | 46.04%       | 1.86x         |
| 20 | TKO      | 2025-08-06 | After market close | Communication Services | $13.4B       | $163.45 | 20.92%       | 38.94%       | 1.86x         |
| 21 | DUOL     | 2025-08-06 | After market close | Technology             | $15.5B       | $340.31 | 43.48%       | 80.93%       | 1.86x         |
| 22 | TNDM     | 2025-08-06 | After market close | Healthcare             | $1.0B        | $15.15  | 53.09%       | 98.73%       | 1.86x         |
| 23 | GOGO     | 2025-08-07 | Before market open | Communication Services | $2.1B        | $15.63  | 42.69%       | 78.34%       | 1.84x         |
| 24 | SDGR     | 2025-08-06 | After market close | Healthcare             | $1.4B        | $19.64  | 41.30%       | 74.98%       | 1.82x         |
| 25 | SONO     | 2025-08-06 | After market close | Technology             | $1.3B        | $10.86  | 39.68%       | 71.75%       | 1.81x         |
| 26 | WMS      | 2025-08-07 | Before market open | Industrials            | $9.1B        | $117.09 | 30.84%       | 55.57%       | 1.80x         |
| 27 | SGI      | 2025-08-07 | Before market open | Consumer Cyclical      | $15.4B       | $74.59  | 24.15%       | 43.01%       | 1.78x         |
| 28 | EPAM     | 2025-08-07 | Before market open | Technology             | $8.6B        | $149.33 | 32.27%       | 57.27%       | 1.77x         |
| 29 | USFD     | 2025-08-07 | Before market open | Consumer Defensive     | $19.6B       | $82.42  | 16.14%       | 28.51%       | 1.77x         |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
