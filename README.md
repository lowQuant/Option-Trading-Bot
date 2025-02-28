# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-02-27 20:40:59 EST

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector             | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | ARLO     | 2025-02-27 | After market close | Industrials        | $1.2B        | $11.88  | 31.24%       | 96.37%       | 3.08x         |
|  1 | DV       | 2025-02-27 | After market close | Technology         | $3.6B        | $21.59  | 27.35%       | 70.80%       | 2.59x         |
|  2 | GDOT     | 2025-02-27 | After market close | Financial Services | $439.4M      | $8.48   | 28.83%       | 71.86%       | 2.49x         |
|  3 | VRRM     | 2025-02-27 | After market close | Industrials        | $4.3B        | $25.91  | 16.81%       | 40.62%       | 2.42x         |
|  4 | HPQ      | 2025-02-27 | After market close | Technology         | $31.2B       | $33.83  | 17.78%       | 42.02%       | 2.36x         |
|  5 | PRGO     | 2025-02-27 | After market close | Healthcare         | $3.3B        | $24.90  | 23.41%       | 54.92%       | 2.35x         |
|  6 | FOXF     | 2025-02-27 | After market close | Consumer Cyclical  | $1.1B        | $26.16  | 33.70%       | 76.98%       | 2.28x         |
|  7 | PGNY     | 2025-02-27 | After market close | Healthcare         | $1.9B        | $23.00  | 33.96%       | 75.34%       | 2.22x         |
|  8 | EFC      | 2025-02-27 | After market close | Real Estate        | $1.2B        | $13.33  | 11.51%       | 25.38%       | 2.21x         |
|  9 | HCI      | 2025-02-27 | After market close | Financial Services | $1.3B        | $121.33 | 21.11%       | 45.67%       | 2.16x         |
| 10 | DRH      | 2025-02-27 | After market close | Real Estate        | $1.7B        | $8.19   | 21.84%       | 45.48%       | 2.08x         |
| 11 | ASTH     | 2025-02-27 | After market close | Healthcare         | $1.6B        | $35.10  | 43.40%       | 88.04%       | 2.03x         |
| 12 | ACHC     | 2025-02-27 | After market close | Healthcare         | $3.7B        | $41.00  | 35.26%       | 71.38%       | 2.02x         |
| 13 | ACA      | 2025-02-27 | After market close | Industrials        | $4.5B        | $93.37  | 26.82%       | 50.76%       | 1.89x         |
| 14 | LMAT     | 2025-02-27 | After market close | Healthcare         | $2.2B        | $103.05 | 25.67%       | 48.54%       | 1.89x         |
| 15 | AGO      | 2025-02-27 | After market close | Financial Services | $4.7B        | $91.62  | 18.75%       | 35.22%       | 1.88x         |
| 16 | ICUI     | 2025-02-27 | After market close | Healthcare         | $3.7B        | $154.27 | 29.60%       | 53.52%       | 1.81x         |
| 17 | TMDX     | 2025-02-27 | After market close | Healthcare         | $2.4B        | $73.76  | 63.41%       | 113.36%      | 1.79x         |
| 18 | COLL     | 2025-02-27 | After market close | Healthcare         | $916.6M      | $28.35  | 30.30%       | 53.88%       | 1.78x         |
| 19 | NTAP     | 2025-02-27 | After market close | Technology         | $24.0B       | $124.49 | 26.27%       | 45.20%       | 1.72x         |
| 20 | PCRX     | 2025-02-27 | After market close | Healthcare         | $1.2B        | $25.48  | 42.13%       | 71.18%       | 1.69x         |
| 21 | ADSK     | 2025-02-27 | After market close | Technology         | $60.8B       | $285.67 | 24.47%       | 41.32%       | 1.69x         |
| 22 | RUN      | 2025-02-27 | After market close | Technology         | $1.8B        | $8.39   | 63.89%       | 105.52%      | 1.65x         |
| 23 | FLGT     | 2025-02-28 | Before market open | Healthcare         | $479.9M      | $16.24  | 36.06%       | 56.04%       | 1.55x         |
| 24 | AES      | 2025-02-27 | After market close | Utilities          | $7.4B        | $10.92  | 37.07%       | 57.26%       | 1.54x         |
| 25 | GTLS     | 2025-02-28 | Before market open | Industrials        | $7.8B        | $185.92 | 43.00%       | 65.58%       | 1.53x         |
| 26 | DUOL     | 2025-02-27 | After market close | Technology         | $16.5B       | $386.56 | 55.72%       | 84.13%       | 1.51x         |
| 27 | RDNT     | 2025-02-28 | Before market open | Healthcare         | $4.3B        | $59.33  | 42.62%       | 63.03%       | 1.48x         |
| 28 | CUBE     | 2025-02-27 | After market close | Real Estate        | $9.7B        | $42.31  | 19.97%       | 28.88%       | 1.45x         |
| 29 | ANIP     | 2025-02-28 | Before market open | Healthcare         | $1.1B        | $55.01  | 27.78%       | 39.11%       | 1.41x         |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
