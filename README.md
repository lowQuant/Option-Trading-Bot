# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-10-23 21:43:29 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector             | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | WKC      | 2025-10-23 | After market close | Energy             | $1.4B        | $25.58  | 20.35%       | 40.47%       | 1.99x         |
|  1 | BYD      | 2025-10-23 | After market close | Consumer Cyclical  | $6.8B        | $82.99  | 18.15%       | 34.85%       | 1.92x         |
|  2 | HCA      | 2025-10-24 | Before market open | Healthcare         | $103.2B      | $441.19 | 17.91%       | 33.59%       | 1.88x         |
|  3 | DECK     | 2025-10-23 | After market close | Consumer Cyclical  | $15.2B       | $100.89 | 36.28%       | 67.52%       | 1.86x         |
|  4 | DLR      | 2025-10-23 | After market close | Real Estate        | $59.9B       | $172.41 | 19.17%       | 35.32%       | 1.84x         |
|  5 | SLM      | 2025-10-23 | After market close | Financial Services | $5.6B        | $27.00  | 26.72%       | 47.75%       | 1.79x         |
|  6 | MTX      | 2025-10-23 | After market close | Basic Materials    | $1.9B        | $60.51  | 26.76%       | 47.53%       | 1.78x         |
|  7 | DOC      | 2025-10-23 | After market close | Real Estate        | $12.9B       | $18.62  | 18.17%       | 32.21%       | 1.77x         |
|  8 | WU       | 2025-10-23 | After market close | Financial Services | $2.6B        | $8.13   | 22.64%       | 39.84%       | 1.76x         |
|  9 | NSC      | 2025-10-23 | After market close | Industrials        | $64.8B       | $288.63 | 13.19%       | 22.29%       | 1.69x         |
| 10 | GNTX     | 2025-10-24 | Before market open | Consumer Cyclical  | $5.8B        | $26.21  | 20.66%       | 34.86%       | 1.69x         |
| 11 | ITW      | 2025-10-24 | Before market open | Industrials        | $75.0B       | $252.96 | 15.01%       | 24.26%       | 1.62x         |
| 12 | NXT      | 2025-10-23 | After market close | Technology         | $13.4B       | $87.55  | 47.43%       | 74.07%       | 1.56x         |
| 13 | MXL      | 2025-10-23 | After market close | Technology         | $1.5B        | $16.78  | 65.58%       | 99.92%       | 1.52x         |
| 14 | ALK      | 2025-10-23 | After market close | Industrials        | $5.5B        | $47.68  | 34.76%       | 52.94%       | 1.52x         |
| 15 | MHK      | 2025-10-23 | After market close | Consumer Cyclical  | $8.0B        | $128.30 | 31.83%       | 48.43%       | 1.52x         |
| 16 | PG       | 2025-10-24 | Before market open | Consumer Defensive | $356.2B      | $152.20 | 15.32%       | 22.88%       | 1.49x         |
| 17 | VRSN     | 2025-10-23 | After market close | Technology         | $23.5B       | $251.94 | 23.29%       | 33.60%       | 1.44x         |
| 18 | BKR      | 2025-10-23 | After market close | Energy             | $48.2B       | $47.30  | 28.40%       | 39.12%       | 1.38x         |
| 19 | GD       | 2025-10-24 | Before market open | Industrials        | $91.9B       | $338.24 | 17.28%       | 22.38%       | 1.30x         |
| 20 | CUBI     | 2025-10-23 | After market close | Financial Services | $2.2B        | $64.01  | 37.43%       | 47.87%       | 1.28x         |
| 21 | EGP      | 2025-10-23 | After market close | Real Estate        | $9.6B        | $180.67 | 20.58%       | 25.79%       | 1.25x         |
| 22 | ENVA     | 2025-10-23 | After market close | Financial Services | $2.9B        | $113.95 | 37.34%       | 46.65%       | 1.25x         |
| 23 | WSFS     | 2025-10-23 | After market close | Financial Services | $3.0B        | $52.74  | 28.65%       | 35.53%       | 1.24x         |
| 24 | FLG      | 2025-10-24 | Before market open | Financial Services | $4.8B        | $11.50  | 35.31%       | 43.56%       | 1.23x         |
| 25 | F        | 2025-10-23 | After market close | Consumer Cyclical  | $49.1B       | $12.43  | 32.04%       | 39.30%       | 1.23x         |
| 26 | ASB      | 2025-10-23 | After market close | Financial Services | $4.2B        | $25.22  | 35.49%       | 42.05%       | 1.18x         |
| 27 | KNSL     | 2025-10-23 | After market close | Financial Services | $10.6B       | $452.60 | 36.00%       | 41.45%       | 1.15x         |
| 28 | NEM      | 2025-10-23 | After market close | Basic Materials    | $97.7B       | $87.01  | 50.34%       | 54.54%       | 1.08x         |
| 29 | FFBC     | 2025-10-23 | After market close | Financial Services | $2.3B        | $24.35  | 34.02%       | 36.68%       | 1.08x         |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
