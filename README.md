# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-07-24 22:04:24 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | KN       | 2025-07-24 | After market close | Technology             | $1.6B        | $19.00  | 25.87%       | 65.52%       | 2.53x         |
|  1 | EW       | 2025-07-24 | After market close | Healthcare             | $44.5B       | $76.91  | 16.09%       | 40.03%       | 2.49x         |
|  2 | HXL      | 2025-07-24 | After market close | Industrials            | $5.0B        | $62.60  | 21.49%       | 45.99%       | 2.14x         |
|  3 | DECK     | 2025-07-24 | After market close | Consumer Cyclical      | $15.7B       | $108.09 | 33.78%       | 65.69%       | 1.94x         |
|  4 | SLM      | 2025-07-24 | After market close | Financial Services     | $6.7B        | $33.02  | 20.33%       | 37.07%       | 1.82x         |
|  5 | SXT      | 2025-07-25 | Before market open | Basic Materials        | $4.7B        | $108.26 | 21.21%       | 38.64%       | 1.82x         |
|  6 | DLR      | 2025-07-24 | After market close | Real Estate            | $61.8B       | $179.24 | 18.03%       | 32.24%       | 1.79x         |
|  7 | VRSN     | 2025-07-24 | After market close | Technology             | $26.9B       | $289.36 | 15.14%       | 26.88%       | 1.78x         |
|  8 | SAIA     | 2025-07-25 | Before market open | Industrials            | $8.3B        | $310.98 | 38.23%       | 65.94%       | 1.72x         |
|  9 | KNSL     | 2025-07-24 | After market close | Financial Services     | $11.1B       | $479.18 | 25.39%       | 43.68%       | 1.72x         |
| 10 | AON      | 2025-07-25 | Before market open | Financial Services     | $77.0B       | $357.28 | 15.68%       | 26.01%       | 1.66x         |
| 11 | HCA      | 2025-07-25 | Before market open | Healthcare             | $82.2B       | $353.27 | 21.67%       | 35.04%       | 1.62x         |
| 12 | TBBK     | 2025-07-24 | After market close | Financial Services     | $3.3B        | $69.50  | 32.55%       | 52.44%       | 1.61x         |
| 13 | CUBI     | 2025-07-24 | After market close | Financial Services     | $1.9B        | $62.55  | 32.55%       | 51.73%       | 1.59x         |
| 14 | ENVA     | 2025-07-24 | After market close | Financial Services     | $2.8B        | $117.63 | 26.69%       | 41.88%       | 1.57x         |
| 15 | SKYW     | 2025-07-24 | After market close | Industrials            | $4.5B        | $113.46 | 31.38%       | 47.62%       | 1.52x         |
| 16 | LKFN     | 2025-07-25 | Before market open | Financial Services     | $1.6B        | $64.92  | 22.58%       | 33.87%       | 1.50x         |
| 17 | SAM      | 2025-07-24 | After market close | Consumer Defensive     | $2.2B        | $207.82 | 33.10%       | 49.54%       | 1.50x         |
| 18 | COKE     | 2025-07-24 | After market close | Consumer Defensive     | $9.7B        | $114.26 | 26.17%       | 38.80%       | 1.48x         |
| 19 | POR      | 2025-07-25 | Before market open | Utilities              | $4.4B        | $40.09  | 17.72%       | 25.63%       | 1.45x         |
| 20 | CHTR     | 2025-07-25 | Before market open | Communication Services | $51.9B       | $398.11 | 30.77%       | 44.33%       | 1.44x         |
| 21 | ASB      | 2025-07-24 | After market close | Financial Services     | $4.2B        | $25.90  | 24.55%       | 35.06%       | 1.43x         |
| 22 | SBCF     | 2025-07-24 | After market close | Financial Services     | $2.5B        | $28.93  | 27.27%       | 38.08%       | 1.40x         |
| 23 | GNTX     | 2025-07-25 | Before market open | Consumer Cyclical      | $5.3B        | $23.86  | 24.39%       | 33.83%       | 1.39x         |
| 24 | SCHL     | 2025-07-24 | After market close | Communication Services | $575.1M      | $22.58  | 42.03%       | 57.70%       | 1.37x         |
| 25 | AN       | 2025-07-25 | Before market open | Consumer Cyclical      | $7.5B        | $204.67 | 27.14%       | 36.69%       | 1.35x         |
| 26 | MHK      | 2025-07-24 | After market close | Consumer Cyclical      | $7.3B        | $116.65 | 36.80%       | 48.94%       | 1.33x         |
| 27 | DOC      | 2025-07-24 | After market close | Real Estate            | $13.1B       | $19.05  | 19.12%       | 24.56%       | 1.28x         |
| 28 | COLB     | 2025-07-24 | After market close | Financial Services     | $4.9B        | $24.38  | 29.60%       | 37.65%       | 1.27x         |
| 29 | WSFS     | 2025-07-24 | After market close | Financial Services     | $3.2B        | $58.16  | 24.74%       | 31.18%       | 1.26x         |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
