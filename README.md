# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-07-17 22:05:14 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close    | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:---------|:-------------|:-------------|:--------------|
|  0 | SCHW     | 2025-07-18 | Before market open | Financial Services     | $169.2B      | $91.26   | 12.92%       | 28.10%       | 2.17x         |
|  1 | NFLX     | 2025-07-17 | After market close | Communication Services | $542.2B      | $1250.31 | 22.19%       | 40.38%       | 1.82x         |
|  2 | MMM      | 2025-07-18 | Before market open | Industrials            | $85.6B       | $157.56  | 19.49%       | 32.70%       | 1.68x         |
|  3 | IBKR     | 2025-07-17 | After market close | Financial Services     | $100.5B      | $59.45   | 27.38%       | 43.04%       | 1.57x         |
|  4 | ALV      | 2025-07-18 | Before market open | Consumer Cyclical      | $9.0B        | $116.81  | 20.93%       | 32.43%       | 1.55x         |
|  5 | ALLY     | 2025-07-18 | Before market open | Financial Services     | $12.4B       | $39.33   | 24.90%       | 35.20%       | 1.41x         |
|  6 | OZK      | 2025-07-17 | After market close | Financial Services     | $5.8B        | $51.17   | 27.13%       | 36.94%       | 1.36x         |
|  7 | HBAN     | 2025-07-18 | Before market open | Financial Services     | $24.8B       | $16.64   | 23.38%       | 31.63%       | 1.35x         |
|  8 | FNB      | 2025-07-17 | After market close | Financial Services     | $5.7B        | $15.51   | 23.76%       | 32.01%       | 1.35x         |
|  9 | TFC      | 2025-07-18 | Before market open | Financial Services     | $58.9B       | $44.36   | 21.74%       | 28.36%       | 1.30x         |
| 10 | RF       | 2025-07-18 | Before market open | Financial Services     | $22.0B       | $24.08   | 22.05%       | 27.66%       | 1.25x         |
| 11 | WAL      | 2025-07-17 | After market close | Financial Services     | $9.3B        | $82.36   | 32.02%       | 40.02%       | 1.25x         |
| 12 | AXP      | 2025-07-18 | Before market open | Financial Services     | $220.9B      | $311.90  | 24.00%       | 29.43%       | 1.23x         |
| 13 | CMA      | 2025-07-18 | Before market open | Financial Services     | $8.2B        | $61.14   | 27.25%       | 32.99%       | 1.21x         |
| 14 | CNS      | 2025-07-17 | After market close | Financial Services     | $3.9B        | $75.99   | 25.25%       | 28.71%       | 1.14x         |
| 15 | SLB      | 2025-07-18 | Before market open | Energy                 | $46.8B       | $34.59   | 36.46%       | 35.87%       | 0.98x         |
| 16 | INDB     | 2025-07-17 | After market close | Financial Services     | $3.3B        | $64.17   | 30.10%       | 25.38%       | 0.84x         |
| 17 | SFNC     | 2025-07-17 | After market close | Financial Services     | $2.5B        | $19.49   | 25.64%       | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
