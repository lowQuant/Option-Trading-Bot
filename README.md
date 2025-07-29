# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-07-28 22:22:30 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector             | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | JCI      | 2025-07-29 | Before market open | Industrials        | $73.4B       | $111.73 | 15.09%       | 36.59%       | 2.42x         |
|  1 | CR       | 2025-07-28 | After market close | Industrials        | $11.0B       | $190.73 | 18.87%       | 43.54%       | 2.31x         |
|  2 | WWD      | 2025-07-28 | After market close | Industrials        | $15.4B       | $257.26 | 19.32%       | 39.22%       | 2.03x         |
|  3 | CVLT     | 2025-07-29 | Before market open | Technology         | $7.3B        | $164.35 | 30.50%       | 59.32%       | 1.94x         |
|  4 | AWI      | 2025-07-29 | Before market open | Industrials        | $7.3B        | $168.54 | 17.07%       | 32.84%       | 1.92x         |
|  5 | HLIT     | 2025-07-28 | After market close | Technology         | $1.0B        | $9.00   | 42.76%       | 80.35%       | 1.88x         |
|  6 | KRC      | 2025-07-28 | After market close | Real Estate        | $4.4B        | $37.08  | 20.27%       | 36.86%       | 1.82x         |
|  7 | SANM     | 2025-07-28 | After market close | Technology         | $5.3B        | $98.58  | 27.62%       | 49.98%       | 1.81x         |
|  8 | AMKR     | 2025-07-28 | After market close | Technology         | $5.2B        | $21.16  | 28.83%       | 51.82%       | 1.80x         |
|  9 | UPS      | 2025-07-29 | Before market open | Industrials        | $86.0B       | $103.56 | 21.58%       | 35.71%       | 1.65x         |
| 10 | BRO      | 2025-07-28 | After market close | Financial Services | $33.8B       | $103.38 | 17.27%       | 28.39%       | 1.64x         |
| 11 | ALKS     | 2025-07-29 | Before market open | Healthcare         | $4.3B        | $26.13  | 33.66%       | 54.68%       | 1.62x         |
| 12 | VLTO     | 2025-07-28 | After market close | Industrials        | $25.6B       | $103.28 | 15.66%       | 25.17%       | 1.61x         |
| 13 | NXRT     | 2025-07-29 | Before market open | Real Estate        | $1.7B        | $33.85  | 20.75%       | 32.89%       | 1.59x         |
| 14 | JBLU     | 2025-07-29 | Before market open | Industrials        | $1.5B        | $4.38   | 54.16%       | 84.83%       | 1.57x         |
| 15 | NSC      | 2025-07-29 | Before market open | Industrials        | $64.6B       | $282.38 | 18.79%       | 29.40%       | 1.56x         |
| 16 | WU       | 2025-07-28 | After market close | Financial Services | $2.8B        | $8.58   | 32.38%       | 50.23%       | 1.55x         |
| 17 | HUBB     | 2025-07-29 | Before market open | Industrials        | $23.4B       | $442.54 | 22.27%       | 34.20%       | 1.54x         |
| 18 | WELL     | 2025-07-28 | After market close | Real Estate        | $103.5B      | $161.56 | 15.17%       | 23.19%       | 1.53x         |
| 19 | CARR     | 2025-07-29 | Before market open | Industrials        | $68.4B       | $80.73  | 20.08%       | 30.35%       | 1.51x         |
| 20 | RMBS     | 2025-07-28 | After market close | Technology         | $6.9B        | $62.85  | 33.34%       | 50.17%       | 1.50x         |
| 21 | CDNS     | 2025-07-28 | After market close | Technology         | $91.1B       | $332.19 | 23.48%       | 35.19%       | 1.50x         |
| 22 | WM       | 2025-07-28 | After market close | Industrials        | $91.7B       | $229.67 | 15.69%       | 23.42%       | 1.49x         |
| 23 | GPK      | 2025-07-29 | Before market open | Consumer Cyclical  | $7.0B        | $23.32  | 24.16%       | 36.06%       | 1.49x         |
| 24 | PJT      | 2025-07-29 | Before market open | Financial Services | $7.3B        | $184.10 | 24.63%       | 36.74%       | 1.49x         |
| 25 | SSD      | 2025-07-28 | After market close | Basic Materials    | $7.0B        | $165.66 | 25.73%       | 38.36%       | 1.49x         |
| 26 | CNO      | 2025-07-28 | After market close | Financial Services | $3.7B        | $37.82  | 22.90%       | 33.51%       | 1.46x         |
| 27 | GATX     | 2025-07-29 | Before market open | Industrials        | $5.4B        | $153.47 | 17.58%       | 25.37%       | 1.44x         |
| 28 | UHS      | 2025-07-28 | After market close | Healthcare         | $10.0B       | $155.60 | 31.33%       | 45.13%       | 1.44x         |
| 29 | RCL      | 2025-07-29 | Before market open | Consumer Cyclical  | $95.6B       | $352.80 | 27.41%       | 39.32%       | 1.43x         |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
