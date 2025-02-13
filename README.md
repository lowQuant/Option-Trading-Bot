# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-02-12 20:38:09 EST

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | PAYC     | 2025-02-12 | After market close | Technology             | $11.6B       | $203.37 | 23.18%       | 50.93%       | 2.20x         |
|  1 | MGM      | 2025-02-12 | After market close | Consumer Cyclical      | $10.2B       | $34.27  | 21.65%       | 45.42%       | 2.10x         |
|  2 | WH       | 2025-02-12 | After market close | Consumer Cyclical      | $8.5B        | $107.45 | 13.53%       | 28.33%       | 2.09x         |
|  3 | WST      | 2025-02-13 | Before market open | Healthcare             | $23.3B       | $322.40 | 23.11%       | 48.06%       | 2.08x         |
|  4 | ROL      | 2025-02-12 | After market close | Consumer Cyclical      | $24.3B       | $49.94  | 15.57%       | 32.13%       | 2.06x         |
|  5 | VNT      | 2025-02-13 | Before market open | Technology             | $5.7B        | $37.82  | 23.34%       | 47.53%       | 2.04x         |
|  6 | HTZ      | 2025-02-13 | Before market open | Industrials            | $1.3B        | $4.45   | 52.44%       | 103.84%      | 1.98x         |
|  7 | CROX     | 2025-02-13 | Before market open | Consumer Cyclical      | $5.2B        | $88.95  | 31.93%       | 62.84%       | 1.97x         |
|  8 | EEFT     | 2025-02-13 | Before market open | Technology             | $4.1B        | $95.84  | 18.40%       | 36.09%       | 1.96x         |
|  9 | USFD     | 2025-02-13 | Before market open | Consumer Defensive     | $16.3B       | $69.69  | 15.13%       | 29.42%       | 1.94x         |
| 10 | SBH      | 2025-02-13 | Before market open | Consumer Cyclical      | $991.9M      | $9.68   | 44.34%       | 83.92%       | 1.89x         |
| 11 | YETI     | 2025-02-13 | Before market open | Consumer Cyclical      | $3.2B        | $37.82  | 30.45%       | 56.51%       | 1.86x         |
| 12 | GPN      | 2025-02-13 | Before market open | Industrials            | $27.7B       | $107.08 | 22.86%       | 41.63%       | 1.82x         |
| 13 | SCI      | 2025-02-12 | After market close | Consumer Cyclical      | $11.0B       | $77.35  | 20.01%       | 36.43%       | 1.82x         |
| 14 | FCPT     | 2025-02-12 | After market close | Real Estate            | $2.7B        | $27.95  | 19.86%       | 35.98%       | 1.81x         |
| 15 | CRSR     | 2025-02-12 | After market close | Technology             | $1.0B        | $9.95   | 50.77%       | 91.35%       | 1.80x         |
| 16 | IRDM     | 2025-02-13 | Before market open | Communication Services | $3.2B        | $27.81  | 35.87%       | 64.26%       | 1.79x         |
| 17 | HWM      | 2025-02-13 | Before market open | Industrials            | $52.0B       | $129.32 | 26.55%       | 46.72%       | 1.76x         |
| 18 | CEVA     | 2025-02-13 | Before market open | Technology             | $749.4M      | $32.15  | 39.28%       | 69.04%       | 1.76x         |
| 19 | AVNT     | 2025-02-13 | Before market open | Basic Materials        | $3.8B        | $42.31  | 28.15%       | 49.12%       | 1.74x         |
| 20 | WEN      | 2025-02-13 | Before market open | Consumer Cyclical      | $2.9B        | $14.32  | 20.83%       | 36.19%       | 1.74x         |
| 21 | CXT      | 2025-02-12 | After market close | Industrials            | $3.4B        | $59.62  | 26.36%       | 45.33%       | 1.72x         |
| 22 | HBI      | 2025-02-13 | Before market open | Consumer Cyclical      | $2.7B        | $7.53   | 35.26%       | 59.76%       | 1.69x         |
| 23 | CGNX     | 2025-02-12 | After market close | Technology             | $6.7B        | $39.62  | 28.05%       | 47.29%       | 1.69x         |
| 24 | GXO      | 2025-02-12 | After market close | Industrials            | $5.1B        | $43.00  | 25.71%       | 42.08%       | 1.64x         |
| 25 | QDEL     | 2025-02-12 | After market close | Healthcare             | $2.7B        | $41.47  | 43.71%       | 70.61%       | 1.62x         |
| 26 | PHIN     | 2025-02-13 | Before market open | Consumer Cyclical      | $2.1B        | $49.53  | 29.12%       | 46.64%       | 1.60x         |
| 27 | ZTS      | 2025-02-13 | Before market open | Healthcare             | $78.4B       | $174.29 | 19.97%       | 31.64%       | 1.58x         |
| 28 | ZBRA     | 2025-02-13 | Before market open | Technology             | $18.2B       | $354.40 | 28.33%       | 44.51%       | 1.57x         |
| 29 | PLMR     | 2025-02-12 | After market close | Financial Services     | $2.9B        | $110.32 | 28.97%       | 45.38%       | 1.57x         |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
