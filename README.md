# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-02-20 20:38:52 EST

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | REZI     | 2025-02-20 | After market close | Industrials            | $3.1B        | $21.86  | 25.48%       | 90.23%       | 3.54x         |
|  1 | FYBR     | 2025-02-20 | After market close | Communication Services | $8.9B        | $35.70  | 3.72%        | 11.36%       | 3.05x         |
|  2 | SEM      | 2025-02-20 | After market close | Healthcare             | $2.5B        | $19.25  | 32.61%       | 97.79%       | 3.00x         |
|  3 | PODD     | 2025-02-20 | After market close | Healthcare             | $20.2B       | $283.68 | 18.48%       | 53.43%       | 2.89x         |
|  4 | LYV      | 2025-02-20 | After market close | Communication Services | $35.1B       | $153.67 | 15.17%       | 42.57%       | 2.81x         |
|  5 | BJRI     | 2025-02-20 | After market close | Consumer Cyclical      | $815.5M      | $35.87  | 26.48%       | 72.51%       | 2.74x         |
|  6 | DBX      | 2025-02-20 | After market close | Technology             | $9.6B        | $32.67  | 17.13%       | 45.75%       | 2.67x         |
|  7 | ALRM     | 2025-02-20 | After market close | Technology             | $3.0B        | $60.73  | 19.86%       | 48.24%       | 2.43x         |
|  8 | CPRT     | 2025-02-20 | After market close | Industrials            | $56.1B       | $59.74  | 14.46%       | 34.87%       | 2.41x         |
|  9 | GMED     | 2025-02-20 | After market close | Healthcare             | $11.5B       | $84.09  | 25.08%       | 56.67%       | 2.26x         |
| 10 | AMN      | 2025-02-20 | After market close | Healthcare             | $983.8M      | $23.84  | 37.74%       | 83.47%       | 2.21x         |
| 11 | OLED     | 2025-02-20 | After market close | Technology             | $7.0B        | $146.62 | 27.15%       | 59.89%       | 2.21x         |
| 12 | WKC      | 2025-02-20 | After market close | Energy                 | $1.6B        | $27.27  | 21.17%       | 45.27%       | 2.14x         |
| 13 | TDS      | 2025-02-21 | Before market open | Communication Services | $4.5B        | $39.57  | 23.13%       | 47.97%       | 2.07x         |
| 14 | TXNM     | 2025-02-21 | Before market open | Utilities              | $4.6B        | $50.97  | 21.32%       | 41.89%       | 1.96x         |
| 15 | AKAM     | 2025-02-20 | After market close | Technology             | $14.7B       | $100.26 | 25.40%       | 48.45%       | 1.91x         |
| 16 | SFM      | 2025-02-20 | After market close | Consumer Defensive     | $17.0B       | $175.97 | 30.36%       | 57.25%       | 1.89x         |
| 17 | GKOS     | 2025-02-20 | After market close | Healthcare             | $8.7B        | $160.58 | 33.46%       | 62.63%       | 1.87x         |
| 18 | DVAX     | 2025-02-20 | After market close | Healthcare             | $1.8B        | $13.09  | 23.55%       | 43.97%       | 1.87x         |
| 19 | ABR      | 2025-02-21 | Before market open | Real Estate            | $2.6B        | $13.82  | 21.22%       | 38.85%       | 1.83x         |
| 20 | CARG     | 2025-02-20 | After market close | Consumer Cyclical      | $3.9B        | $38.14  | 32.29%       | 58.57%       | 1.81x         |
| 21 | TXRH     | 2025-02-20 | After market close | Consumer Cyclical      | $11.4B       | $174.02 | 20.07%       | 36.17%       | 1.80x         |
| 22 | NVEE     | 2025-02-20 | After market close | Industrials            | $1.1B        | $17.03  | 33.28%       | 59.60%       | 1.79x         |
| 23 | BCPC     | 2025-02-21 | Before market open | Basic Materials        | $5.2B        | $163.78 | 18.92%       | 33.15%       | 1.75x         |
| 24 | GDYN     | 2025-02-20 | After market close | Technology             | $1.7B        | $21.57  | 37.99%       | 63.99%       | 1.68x         |
| 25 | BCC      | 2025-02-20 | After market close | Basic Materials        | $4.5B        | $118.30 | 25.98%       | 40.73%       | 1.57x         |
| 26 | NEM      | 2025-02-20 | After market close | Basic Materials        | $54.7B       | $47.41  | 26.85%       | 40.54%       | 1.51x         |
| 27 | FND      | 2025-02-20 | After market close | Consumer Cyclical      | $10.0B       | $95.33  | 34.54%       | 52.08%       | 1.51x         |
| 28 | EXPI     | 2025-02-20 | After market close | Real Estate            | $1.7B        | $11.31  | 39.76%       | 59.60%       | 1.50x         |
| 29 | RYAN     | 2025-02-20 | After market close | Financial Services     | $18.0B       | $69.37  | 23.95%       | 33.98%       | 1.42x         |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
