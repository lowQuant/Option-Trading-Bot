# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-04-30 21:59:18 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector             | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | CWT      | 2025-05-01 | Before market open | Utilities          | $3.0B        | $50.47  | 23.77%       | 48.62%       | 2.05x         |
|  1 | RGR      | 2025-04-30 | After market close | Industrials        | $673.1M      | $40.68  | 17.16%       | 33.01%       | 1.92x         |
|  2 | K        | 2025-05-01 | Before market open | Consumer Defensive | $28.6B       | $82.58  | 3.79%        | 7.18%        | 1.89x         |
|  3 | FTDR     | 2025-05-01 | Before market open | Consumer Cyclical  | $3.0B        | $41.18  | 33.08%       | 59.11%       | 1.79x         |
|  4 | TNDM     | 2025-04-30 | After market close | Healthcare         | $1.1B        | $16.77  | 49.59%       | 86.12%       | 1.74x         |
|  5 | ALKS     | 2025-05-01 | Before market open | Healthcare         | $4.7B        | $28.77  | 37.90%       | 62.28%       | 1.64x         |
|  6 | SFM      | 2025-04-30 | After market close | Consumer Defensive | $16.8B       | $172.30 | 34.55%       | 54.37%       | 1.57x         |
|  7 | JBSS     | 2025-04-30 | After market close | Consumer Defensive | $771.3M      | $66.74  | 19.49%       | 29.76%       | 1.53x         |
|  8 | GPK      | 2025-05-01 | Before market open | Consumer Cyclical  | $7.7B        | $25.64  | 30.38%       | 44.19%       | 1.45x         |
|  9 | MCW      | 2025-04-30 | After market close | Consumer Cyclical  | $2.2B        | $7.04   | 46.53%       | 67.23%       | 1.44x         |
| 10 | CNXN     | 2025-04-30 | After market close | Technology         | $1.6B        | $62.50  | 27.33%       | 37.41%       | 1.37x         |
| 11 | HSY      | 2025-05-01 | Before market open | Consumer Defensive | $33.9B       | $165.07 | 25.76%       | 34.10%       | 1.32x         |
| 12 | DLX      | 2025-04-30 | After market close | Industrials        | $652.9M      | $15.50  | 45.34%       | 59.33%       | 1.31x         |
| 13 | PPC      | 2025-04-30 | After market close | Consumer Defensive | $13.0B       | $53.98  | 31.48%       | 40.72%       | 1.29x         |
| 14 | GVA      | 2025-05-01 | Before market open | Industrials        | $3.6B        | $80.67  | 36.48%       | 46.29%       | 1.27x         |
| 15 | SHC      | 2025-05-01 | Before market open | Healthcare         | $3.3B        | $11.31  | 61.04%       | 76.52%       | 1.25x         |
| 16 | TTMI     | 2025-04-30 | After market close | Technology         | $2.0B        | $20.42  | 62.91%       | 78.72%       | 1.25x         |
| 17 | WSR      | 2025-04-30 | After market close | Real Estate        | $672.1M      | $13.09  | 28.43%       | 35.10%       | 1.23x         |
| 18 | CVS      | 2025-05-01 | Before market open | Healthcare         | $84.2B       | $65.03  | 31.81%       | 38.58%       | 1.21x         |
| 19 | SCI      | 2025-04-30 | After market close | Consumer Cyclical  | $11.5B       | $80.10  | 29.40%       | 35.28%       | 1.20x         |
| 20 | PATK     | 2025-05-01 | Before market open | Consumer Cyclical  | $2.6B        | $78.52  | 48.37%       | 57.99%       | 1.20x         |
| 21 | GRBK     | 2025-04-30 | After market close | Consumer Cyclical  | $2.6B        | $58.22  | 41.66%       | 49.66%       | 1.19x         |
| 22 | MGPI     | 2025-05-01 | Before market open | Consumer Defensive | $626.8M      | $29.55  | 41.65%       | 49.33%       | 1.18x         |
| 23 | IDCC     | 2025-05-01 | Before market open | Technology         | $5.2B        | $200.53 | 42.16%       | 49.79%       | 1.18x         |
| 24 | MPW      | 2025-05-01 | Before market open | Real Estate        | $3.3B        | $5.49   | 45.34%       | 53.03%       | 1.17x         |
| 25 | NSIT     | 2025-05-01 | Before market open | Technology         | $4.4B        | $139.32 | 41.84%       | 48.44%       | 1.16x         |
| 26 | MRNA     | 2025-05-01 | Before market open | Healthcare         | $11.0B       | $27.82  | 67.19%       | 77.59%       | 1.15x         |
| 27 | ALGN     | 2025-04-30 | After market close | Healthcare         | $12.7B       | $177.75 | 55.05%       | 63.30%       | 1.15x         |
| 28 | ITRI     | 2025-05-01 | Before market open | Technology         | $5.1B        | $110.88 | 44.07%       | 50.61%       | 1.15x         |
| 29 | BIIB     | 2025-05-01 | Before market open | Healthcare         | $17.7B       | $120.17 | 40.71%       | 46.37%       | 1.14x         |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
