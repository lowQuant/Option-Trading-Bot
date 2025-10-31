# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-10-30 21:50:57 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | RMD      | 2025-10-30 | After market close | Healthcare             | $36.8B       | $253.62 | 17.57%       | 44.46%       | 2.53x         |
|  1 | ATR      | 2025-10-30 | After market close | Healthcare             | $8.2B        | $124.31 | 13.71%       | 34.00%       | 2.48x         |
|  2 | CHTR     | 2025-10-31 | Before market open | Communication Services | $31.5B       | $241.56 | 29.36%       | 69.90%       | 2.38x         |
|  3 | SKYW     | 2025-10-30 | After market close | Industrials            | $3.8B        | $96.61  | 20.82%       | 47.52%       | 2.28x         |
|  4 | NWL      | 2025-10-31 | Before market open | Consumer Defensive     | $2.0B        | $4.93   | 32.93%       | 70.03%       | 2.13x         |
|  5 | FND      | 2025-10-30 | After market close | Consumer Cyclical      | $7.0B        | $69.08  | 30.57%       | 64.16%       | 2.10x         |
|  6 | WY       | 2025-10-30 | After market close | Real Estate            | $17.0B       | $23.20  | 18.11%       | 34.32%       | 1.90x         |
|  7 | SPSC     | 2025-10-30 | After market close | Technology             | $3.9B        | $105.18 | 28.98%       | 54.30%       | 1.87x         |
|  8 | RGA      | 2025-10-30 | After market close | Financial Services     | $12.5B       | $189.61 | 18.41%       | 33.67%       | 1.83x         |
|  9 | NVT      | 2025-10-31 | Before market open | Industrials            | $16.8B       | $106.28 | 27.35%       | 49.13%       | 1.80x         |
| 10 | NVST     | 2025-10-30 | After market close | Healthcare             | $3.3B        | $19.98  | 24.46%       | 43.87%       | 1.79x         |
| 11 | EXPO     | 2025-10-30 | After market close | Industrials            | $3.4B        | $65.41  | 20.49%       | 36.60%       | 1.79x         |
| 12 | PSMT     | 2025-10-30 | After market close | Consumer Defensive     | $3.8B        | $121.08 | 21.01%       | 37.38%       | 1.78x         |
| 13 | GDDY     | 2025-10-30 | After market close | Technology             | $17.5B       | $126.57 | 26.82%       | 47.53%       | 1.77x         |
| 14 | LYB      | 2025-10-31 | Before market open | Basic Materials        | $14.5B       | $46.71  | 34.20%       | 59.46%       | 1.74x         |
| 15 | AON      | 2025-10-31 | Before market open | Financial Services     | $70.8B       | $326.07 | 18.10%       | 31.12%       | 1.72x         |
| 16 | LUMN     | 2025-10-30 | After market close | Communication Services | $10.6B       | $11.00  | 78.49%       | 134.85%      | 1.72x         |
| 17 | IR       | 2025-10-30 | After market close | Industrials            | $31.3B       | $79.70  | 25.03%       | 43.00%       | 1.72x         |
| 18 | APPF     | 2025-10-30 | After market close | Technology             | $8.5B        | $238.67 | 34.47%       | 58.95%       | 1.71x         |
| 19 | ACA      | 2025-10-30 | After market close | Industrials            | $4.5B        | $93.18  | 23.85%       | 40.29%       | 1.69x         |
| 20 | AGCO     | 2025-10-31 | Before market open | Industrials            | $7.9B        | $108.30 | 25.33%       | 42.60%       | 1.68x         |
| 21 | ALEX     | 2025-10-30 | After market close | Real Estate            | $1.2B        | $16.42  | 15.90%       | 26.67%       | 1.68x         |
| 22 | TILE     | 2025-10-31 | Before market open | Consumer Cyclical      | $1.6B        | $26.57  | 23.67%       | 39.43%       | 1.67x         |
| 23 | RSG      | 2025-10-30 | After market close | Industrials            | $65.5B       | $210.50 | 17.05%       | 28.13%       | 1.65x         |
| 24 | AMZN     | 2025-10-30 | After market close | Consumer Cyclical      | $2.4tr       | $230.30 | 25.55%       | 41.90%       | 1.64x         |
| 25 | LIN      | 2025-10-31 | Before market open | Basic Materials        | $201.6B      | $432.01 | 14.65%       | 23.88%       | 1.63x         |
| 26 | GILD     | 2025-10-30 | After market close | Healthcare             | $147.0B      | $118.50 | 22.69%       | 36.96%       | 1.63x         |
| 27 | LEA      | 2025-10-31 | Before market open | Consumer Cyclical      | $5.5B        | $104.08 | 23.03%       | 36.69%       | 1.59x         |
| 28 | DXCM     | 2025-10-30 | After market close | Healthcare             | $26.7B       | $68.18  | 42.91%       | 68.04%       | 1.59x         |
| 29 | CL       | 2025-10-31 | Before market open | Consumer Defensive     | $61.8B       | $75.73  | 18.32%       | 28.74%       | 1.57x         |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
