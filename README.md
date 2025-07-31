# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-07-30 22:07:33 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector             | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | ITRI     | 2025-07-31 | Before market open | Technology         | $6.3B        | $136.62 | 15.03%       | 42.64%       | 2.84x         |
|  1 | TTEK     | 2025-07-30 | After market close | Industrials        | $9.8B        | $37.54  | 14.93%       | 38.89%       | 2.60x         |
|  2 | PRLB     | 2025-07-31 | Before market open | Industrials        | $932.5M      | $40.02  | 23.71%       | 56.27%       | 2.37x         |
|  3 | PI       | 2025-07-30 | After market close | Technology         | $3.5B        | $122.81 | 35.64%       | 80.48%       | 2.26x         |
|  4 | RGR      | 2025-07-30 | After market close | Industrials        | $573.1M      | $34.92  | 21.75%       | 48.53%       | 2.23x         |
|  5 | GKOS     | 2025-07-30 | After market close | Healthcare         | $5.4B        | $93.76  | 31.18%       | 69.55%       | 2.23x         |
|  6 | MYRG     | 2025-07-30 | After market close | Industrials        | $3.1B        | $198.15 | 25.36%       | 55.36%       | 2.18x         |
|  7 | CRS      | 2025-07-31 | Before market open | Industrials        | $14.1B       | $275.26 | 22.04%       | 47.84%       | 2.17x         |
|  8 | MSFT     | 2025-07-30 | After market close | Technology         | $3.8tr       | $512.57 | 11.36%       | 24.49%       | 2.16x         |
|  9 | IDCC     | 2025-07-31 | Before market open | Technology         | $6.4B        | $221.35 | 19.88%       | 42.34%       | 2.13x         |
| 10 | MGY      | 2025-07-30 | After market close | Energy             | $4.7B        | $24.60  | 29.93%       | 60.72%       | 2.03x         |
| 11 | ATI      | 2025-07-31 | Before market open | Industrials        | $13.3B       | $94.11  | 23.30%       | 46.52%       | 2.00x         |
| 12 | QCOM     | 2025-07-30 | After market close | Technology         | $174.6B      | $162.08 | 19.57%       | 38.90%       | 1.99x         |
| 13 | SHAK     | 2025-07-31 | Before market open | Consumer Cyclical  | $6.0B        | $137.12 | 27.38%       | 54.14%       | 1.98x         |
| 14 | VNT      | 2025-07-31 | Before market open | Technology         | $5.9B        | $39.93  | 19.92%       | 39.32%       | 1.97x         |
| 15 | ICE      | 2025-07-31 | Before market open | Financial Services | $106.5B      | $184.71 | 11.23%       | 21.99%       | 1.96x         |
| 16 | NBIX     | 2025-07-30 | After market close | Healthcare         | $13.5B       | $134.19 | 20.89%       | 40.73%       | 1.95x         |
| 17 | AME      | 2025-07-31 | Before market open | Industrials        | $40.8B       | $178.96 | 14.12%       | 27.39%       | 1.94x         |
| 18 | FFIV     | 2025-07-30 | After market close | Technology         | $17.2B       | $299.24 | 19.27%       | 36.89%       | 1.91x         |
| 19 | XYL      | 2025-07-31 | Before market open | Industrials        | $31.8B       | $131.96 | 13.66%       | 26.00%       | 1.90x         |
| 20 | HWKN     | 2025-07-30 | After market close | Basic Materials    | $3.3B        | $160.63 | 23.58%       | 44.62%       | 1.89x         |
| 21 | WCC      | 2025-07-31 | Before market open | Industrials        | $10.4B       | $216.19 | 24.85%       | 46.95%       | 1.89x         |
| 22 | BHE      | 2025-07-30 | After market close | Technology         | $1.4B        | $40.19  | 26.76%       | 49.68%       | 1.86x         |
| 23 | XPO      | 2025-07-31 | Before market open | Industrials        | $15.6B       | $134.46 | 27.86%       | 51.25%       | 1.84x         |
| 24 | WDC      | 2025-07-30 | After market close | Technology         | $24.9B       | $70.61  | 22.88%       | 42.04%       | 1.84x         |
| 25 | ALGN     | 2025-07-30 | After market close | Healthcare         | $14.8B       | $205.81 | 30.52%       | 55.94%       | 1.83x         |
| 26 | MPW      | 2025-07-31 | Before market open | Real Estate        | $2.5B        | $4.22   | 34.29%       | 61.88%       | 1.80x         |
| 27 | CNXN     | 2025-07-30 | After market close | Technology         | $1.6B        | $64.22  | 17.54%       | 31.47%       | 1.79x         |
| 28 | PATK     | 2025-07-31 | Before market open | Consumer Cyclical  | $3.4B        | $101.29 | 26.71%       | 47.66%       | 1.78x         |
| 29 | PPC      | 2025-07-30 | After market close | Consumer Defensive | $11.3B       | $46.92  | 22.61%       | 40.32%       | 1.78x         |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
