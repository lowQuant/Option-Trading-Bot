# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-02-13 20:37:22 EST

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | PDFS     | 2025-02-13 | After market close | Technology             | $1.1B        | $27.29  | 35.04%       | 77.21%       | 2.20x         |
|  1 | THS      | 2025-02-14 | Before market open | Consumer Defensive     | $1.7B        | $32.98  | 28.46%       | 56.63%       | 1.99x         |
|  2 | AL       | 2025-02-13 | After market close | Industrials            | $5.2B        | $45.70  | 23.33%       | 44.78%       | 1.92x         |
|  3 | DVA      | 2025-02-13 | After market close | Healthcare             | $14.5B       | $172.00 | 22.63%       | 41.93%       | 1.85x         |
|  4 | YELP     | 2025-02-13 | After market close | Communication Services | $2.7B        | $39.67  | 25.40%       | 46.53%       | 1.83x         |
|  5 | KN       | 2025-02-13 | After market close | Technology             | $1.6B        | $18.07  | 23.55%       | 41.64%       | 1.77x         |
|  6 | BGC      | 2025-02-14 | Before market open | Financial Services     | $4.6B        | $9.46   | 24.56%       | 42.71%       | 1.74x         |
|  7 | DXCM     | 2025-02-13 | After market close | Healthcare             | $32.8B       | $83.87  | 30.15%       | 50.88%       | 1.69x         |
|  8 | GDDY     | 2025-02-13 | After market close | Technology             | $29.8B       | $207.53 | 22.64%       | 37.47%       | 1.66x         |
|  9 | PANW     | 2025-02-13 | After market close | Technology             | $132.5B      | $196.73 | 28.99%       | 47.68%       | 1.64x         |
| 10 | MSI      | 2025-02-13 | After market close | Technology             | $77.9B       | $466.90 | 16.93%       | 27.56%       | 1.63x         |
| 11 | LEG      | 2025-02-13 | After market close | Consumer Cyclical      | $1.3B        | $9.73   | 39.52%       | 64.07%       | 1.62x         |
| 12 | ABNB     | 2025-02-13 | After market close | Consumer Cyclical      | $88.1B       | $140.52 | 29.91%       | 47.78%       | 1.60x         |
| 13 | HASI     | 2025-02-13 | After market close | Real Estate            | $3.4B        | $27.77  | 28.85%       | 45.91%       | 1.59x         |
| 14 | BIO      | 2025-02-13 | After market close | Healthcare             | $8.7B        | $312.36 | 32.50%       | 45.67%       | 1.41x         |
| 15 | KNSL     | 2025-02-13 | After market close | Financial Services     | $11.3B       | $476.67 | 31.80%       | 44.08%       | 1.39x         |
| 16 | RWT      | 2025-02-13 | After market close | Real Estate            | $856.1M      | $6.44   | 26.18%       | 36.13%       | 1.38x         |
| 17 | HCC      | 2025-02-13 | After market close | Basic Materials        | $2.8B        | $52.65  | 35.48%       | 48.64%       | 1.37x         |
| 18 | IR       | 2025-02-13 | After market close | Industrials            | $37.3B       | $91.35  | 21.29%       | 29.07%       | 1.37x         |
| 19 | RSG      | 2025-02-13 | After market close | Industrials            | $70.3B       | $223.50 | 15.74%       | 20.17%       | 1.28x         |
| 20 | AXL      | 2025-02-14 | Before market open | Consumer Cyclical      | $558.5M      | $4.72   | 49.88%       | 63.35%       | 1.27x         |
| 21 | WYNN     | 2025-02-13 | After market close | Consumer Cyclical      | $8.8B        | $78.37  | 32.54%       | 41.20%       | 1.27x         |
| 22 | FBRT     | 2025-02-13 | After market close | Real Estate            | $1.1B        | $12.85  | 18.55%       | 22.57%       | 1.22x         |
| 23 | AMAT     | 2025-02-13 | After market close | Technology             | $149.8B      | $180.89 | 38.30%       | 43.15%       | 1.13x         |
| 24 | SXT      | 2025-02-14 | Before market open | Basic Materials        | $3.3B        | $75.19  | 25.24%       | 27.90%       | 1.11x         |
| 25 | POR      | 2025-02-14 | Before market open | Utilities              | $4.4B        | $41.85  | 23.33%       | 25.51%       | 1.09x         |
| 26 | FRT      | 2025-02-13 | After market close | Real Estate            | $9.6B        | $110.55 | 22.53%       | 24.40%       | 1.08x         |
| 27 | AEE      | 2025-02-13 | After market close | Utilities              | $26.2B       | $97.26  | 20.48%       | 21.74%       | 1.06x         |
| 28 | DLR      | 2025-02-13 | After market close | Real Estate            | $55.7B       | $163.22 | 36.14%       | 31.22%       | 0.86x         |
| 29 | MRNA     | 2025-02-14 | Before market open | Healthcare             | $12.3B       | $30.54  | 96.77%       | 80.42%       | 0.83x         |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
