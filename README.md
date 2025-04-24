# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-04-23 21:49:20 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector             | market_cap   | close    | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-------------------|:-------------|:---------|:-------------|:-------------|:--------------|
|  0 | FCN      | 2025-04-24 | Before market open | Industrials        | $6.0B        | $167.50  | 25.88%       | 44.58%       | 1.72x         |
|  1 | APOG     | 2025-04-24 | Before market open | Industrials        | $1.0B        | $45.61   | 37.80%       | 63.45%       | 1.68x         |
|  2 | CVBF     | 2025-04-23 | After market close | Financial Services | $2.6B        | $18.41   | 38.44%       | 58.81%       | 1.53x         |
|  3 | CHE      | 2025-04-23 | After market close | Healthcare         | $8.6B        | $579.50  | 26.28%       | 38.86%       | 1.48x         |
|  4 | FBP      | 2025-04-24 | Before market open | Financial Services | $3.2B        | $18.66   | 42.64%       | 62.17%       | 1.46x         |
|  5 | STRA     | 2025-04-24 | Before market open | Consumer Defensive | $2.0B        | $78.73   | 32.79%       | 47.06%       | 1.44x         |
|  6 | FCFS     | 2025-04-24 | Before market open | Financial Services | $5.5B        | $121.61  | 24.83%       | 35.53%       | 1.43x         |
|  7 | CACI     | 2025-04-23 | After market close | Technology         | $9.5B        | $422.71  | 32.94%       | 46.37%       | 1.41x         |
|  8 | PEN      | 2025-04-23 | After market close | Healthcare         | $10.8B       | $277.22  | 38.41%       | 53.63%       | 1.40x         |
|  9 | RMD      | 2025-04-23 | After market close | Healthcare         | $31.5B       | $214.08  | 36.70%       | 50.61%       | 1.38x         |
| 10 | EW       | 2025-04-23 | After market close | Healthcare         | $41.4B       | $70.60   | 28.81%       | 39.50%       | 1.37x         |
| 11 | GSHD     | 2025-04-23 | After market close | Financial Services | $3.9B        | $103.22  | 57.80%       | 77.09%       | 1.33x         |
| 12 | WST      | 2025-04-24 | Before market open | Healthcare         | $15.8B       | $215.13  | 45.05%       | 58.96%       | 1.31x         |
| 13 | MRK      | 2025-04-24 | Before market open | Healthcare         | $198.7B      | $78.97   | 34.74%       | 43.38%       | 1.25x         |
| 14 | CNP      | 2025-04-24 | Before market open | Utilities          | $24.4B       | $37.26   | 20.24%       | 25.25%       | 1.25x         |
| 15 | BMY      | 2025-04-24 | Before market open | Healthcare         | $101.4B      | $49.82   | 33.17%       | 40.42%       | 1.22x         |
| 16 | CCS      | 2025-04-23 | After market close | Real Estate        | $1.9B        | $61.54   | 45.92%       | 54.89%       | 1.20x         |
| 17 | CHDN     | 2025-04-23 | After market close | Consumer Cyclical  | $7.7B        | $103.00  | 37.95%       | 45.00%       | 1.19x         |
| 18 | ORLY     | 2025-04-23 | After market close | Consumer Cyclical  | $79.8B       | $1393.54 | 29.80%       | 35.13%       | 1.18x         |
| 19 | VRE      | 2025-04-23 | After market close | Real Estate        | $1.8B        | $16.10   | 34.40%       | 40.35%       | 1.17x         |
| 20 | BCPC     | 2025-04-24 | Before market open | Basic Materials    | $5.2B        | $157.50  | 31.42%       | 36.73%       | 1.17x         |
| 21 | TPH      | 2025-04-24 | Before market open | Consumer Cyclical  | $2.8B        | $30.93   | 40.26%       | 46.59%       | 1.16x         |
| 22 | GTY      | 2025-04-23 | After market close | Real Estate        | $1.6B        | $28.77   | 23.91%       | 27.11%       | 1.13x         |
| 23 | IBM      | 2025-04-23 | After market close | Technology         | $227.6B      | $240.90  | 38.33%       | 43.36%       | 1.13x         |
| 24 | CMG      | 2025-04-23 | After market close | Consumer Cyclical  | $66.1B       | $47.10   | 45.07%       | 50.07%       | 1.11x         |
| 25 | WHR      | 2025-04-23 | After market close | Consumer Cyclical  | $4.3B        | $77.32   | 49.23%       | 54.45%       | 1.11x         |
| 26 | MOH      | 2025-04-23 | After market close | Healthcare         | $18.2B       | $321.16  | 44.91%       | 49.15%       | 1.09x         |
| 27 | TYL      | 2025-04-23 | After market close | Technology         | $24.5B       | $563.84  | 35.94%       | 39.10%       | 1.09x         |
| 28 | XEL      | 2025-04-24 | Before market open | Utilities          | $41.2B       | $71.39   | 27.15%       | 29.31%       | 1.08x         |
| 29 | ITGR     | 2025-04-24 | Before market open | Healthcare         | $4.2B        | $117.98  | 39.64%       | 42.77%       | 1.08x         |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
