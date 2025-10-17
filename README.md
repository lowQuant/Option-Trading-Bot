# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-10-16 21:45:51 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector             | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | LBRT     | 2025-10-16 | After market close | Energy             | $1.9B        | $12.34  | 46.97%       | 76.05%       | 1.62x         |
|  1 | SLB      | 2025-10-17 | Before market open | Energy             | $49.2B       | $32.57  | 26.60%       | 41.44%       | 1.56x         |
|  2 | FNB      | 2025-10-16 | After market close | Financial Services | $5.3B        | $15.79  | 24.20%       | 36.92%       | 1.53x         |
|  3 | OZK      | 2025-10-16 | After market close | Financial Services | $5.3B        | $50.50  | 23.94%       | 35.99%       | 1.50x         |
|  4 | AXP      | 2025-10-17 | Before market open | Financial Services | $224.9B      | $330.66 | 22.16%       | 33.20%       | 1.50x         |
|  5 | TFC      | 2025-10-17 | Before market open | Financial Services | $53.0B       | $43.26  | 21.23%       | 31.17%       | 1.47x         |
|  6 | ALV      | 2025-10-17 | Before market open | Consumer Cyclical  | $9.3B        | $120.90 | 24.68%       | 35.55%       | 1.44x         |
|  7 | RF       | 2025-10-17 | Before market open | Financial Services | $20.8B       | $24.74  | 22.53%       | 32.28%       | 1.43x         |
|  8 | STT      | 2025-10-17 | Before market open | Financial Services | $32.0B       | $116.71 | 24.47%       | 33.37%       | 1.36x         |
|  9 | FITB     | 2025-10-17 | Before market open | Financial Services | $26.4B       | $42.92  | 23.66%       | 32.20%       | 1.36x         |
| 10 | ALLY     | 2025-10-17 | Before market open | Financial Services | $11.8B       | $39.70  | 32.32%       | 42.94%       | 1.33x         |
| 11 | GBCI     | 2025-10-16 | After market close | Financial Services | $5.9B        | $48.02  | 27.36%       | 36.26%       | 1.33x         |
| 12 | HBAN     | 2025-10-17 | Before market open | Financial Services | $22.4B       | $16.21  | 24.01%       | 31.15%       | 1.30x         |
| 13 | SFNC     | 2025-10-16 | After market close | Financial Services | $2.6B        | $19.00  | 23.74%       | 30.79%       | 1.30x         |
| 14 | CSX      | 2025-10-16 | After market close | Industrials        | $67.1B       | $36.24  | 22.91%       | 28.32%       | 1.24x         |
| 15 | INDB     | 2025-10-16 | After market close | Financial Services | $3.2B        | $67.92  | 29.13%       | 34.84%       | 1.20x         |
| 16 | WBS      | 2025-10-17 | Before market open | Financial Services | $9.0B        | $58.20  | 31.10%       | 37.11%       | 1.19x         |
| 17 | IBKR     | 2025-10-16 | After market close | Financial Services | $116.5B      | $69.77  | 37.23%       | 43.02%       | 1.16x         |
| 18 | CMA      | 2025-10-17 | Before market open | Financial Services | $9.4B        | $78.61  | 44.98%       | 29.72%       | 0.66x         |
| 19 | CNS      | 2025-10-16 | After market close | Financial Services | $3.4B        | $66.55  | 16.05%       | nan%         | nanx          |
| 20 | WAFD     | 2025-10-16 | After market close | Financial Services | $2.2B        | $28.89  | 18.46%       | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
