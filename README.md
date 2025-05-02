# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-05-01 21:50:40 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | SEM      | 2025-05-01 | After market close | Healthcare             | $2.4B        | $18.24  | 41.12%       | 79.07%       | 1.92x         |
|  1 | ATEN     | 2025-05-01 | After market close | Technology             | $1.2B        | $16.48  | 43.73%       | 72.69%       | 1.66x         |
|  2 | PRDO     | 2025-05-01 | After market close | Consumer Defensive     | $1.6B        | $25.12  | 29.97%       | 46.63%       | 1.56x         |
|  3 | HOLX     | 2025-05-01 | After market close | Healthcare             | $12.9B       | $58.20  | 26.16%       | 38.27%       | 1.46x         |
|  4 | WEN      | 2025-05-02 | Before market open | Consumer Cyclical      | $2.5B        | $12.50  | 39.00%       | 51.68%       | 1.33x         |
|  5 | CI       | 2025-05-02 | Before market open | Healthcare             | $90.9B       | $340.04 | 24.54%       | 31.84%       | 1.30x         |
|  6 | VIAV     | 2025-05-01 | After market close | Technology             | $2.4B        | $10.58  | 43.04%       | 54.96%       | 1.28x         |
|  7 | TRUP     | 2025-05-01 | After market close | Financial Services     | $1.5B        | $36.60  | 63.63%       | 80.12%       | 1.26x         |
|  8 | PCTY     | 2025-05-01 | After market close | Technology             | $10.9B       | $192.10 | 36.82%       | 46.31%       | 1.26x         |
|  9 | CART     | 2025-05-01 | After market close | Consumer Cyclical      | $10.4B       | $39.89  | 43.30%       | 52.88%       | 1.22x         |
| 10 | MSEX     | 2025-05-01 | After market close | Utilities              | $1.1B        | $63.12  | 26.35%       | 31.30%       | 1.19x         |
| 11 | CNK      | 2025-05-02 | Before market open | Communication Services | $3.5B        | $29.91  | 32.79%       | 38.94%       | 1.19x         |
| 12 | EXPO     | 2025-05-01 | After market close | Industrials            | $3.9B        | $78.68  | 27.01%       | 31.65%       | 1.17x         |
| 13 | NVST     | 2025-05-01 | After market close | Healthcare             | $2.8B        | $16.08  | 56.33%       | 65.00%       | 1.15x         |
| 14 | PRLB     | 2025-05-02 | Before market open | Industrials            | $851.0M      | $35.16  | 55.20%       | 62.22%       | 1.13x         |
| 15 | OHI      | 2025-05-01 | After market close | Real Estate            | $11.4B       | $39.05  | 23.01%       | 25.91%       | 1.13x         |
| 16 | X        | 2025-05-01 | After market close | Basic Materials        | $9.8B        | $43.71  | 66.86%       | 75.26%       | 1.13x         |
| 17 | LUMN     | 2025-05-01 | After market close | Communication Services | $3.6B        | $3.54   | 85.40%       | 95.35%       | 1.12x         |
| 18 | AIG      | 2025-05-01 | After market close | Financial Services     | $47.2B       | $81.52  | 38.07%       | 41.55%       | 1.09x         |
| 19 | DXCM     | 2025-05-01 | After market close | Healthcare             | $27.5B       | $71.38  | 53.89%       | 58.61%       | 1.09x         |
| 20 | DUOL     | 2025-05-01 | After market close | Technology             | $18.2B       | $389.48 | 73.58%       | 79.34%       | 1.08x         |
| 21 | CTRE     | 2025-05-01 | After market close | Real Estate            | $5.5B        | $29.27  | 24.18%       | 25.90%       | 1.07x         |
| 22 | GDYN     | 2025-05-01 | After market close | Technology             | $1.2B        | $14.16  | 61.66%       | 65.49%       | 1.06x         |
| 23 | BJRI     | 2025-05-01 | After market close | Consumer Cyclical      | $747.4M      | $33.29  | 52.88%       | 55.36%       | 1.05x         |
| 24 | ASIX     | 2025-05-02 | Before market open | Basic Materials        | $571.1M      | $21.42  | 54.22%       | 56.71%       | 1.05x         |
| 25 | LMAT     | 2025-05-01 | After market close | Healthcare             | $2.0B        | $90.74  | 38.87%       | 40.57%       | 1.04x         |
| 26 | ED       | 2025-05-01 | After market close | Utilities              | $40.5B       | $112.75 | 23.46%       | 24.14%       | 1.03x         |
| 27 | GDDY     | 2025-05-01 | After market close | Technology             | $26.6B       | $188.33 | 41.43%       | 41.65%       | 1.01x         |
| 28 | AMGN     | 2025-05-01 | After market close | Healthcare             | $152.6B      | $290.92 | 32.30%       | 32.32%       | 1.00x         |
| 29 | FLR      | 2025-05-02 | Before market open | Industrials            | $6.0B        | $34.89  | 60.33%       | 59.72%       | 0.99x         |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
