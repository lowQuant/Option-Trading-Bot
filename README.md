# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-11-04 20:53:15 EST

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | ANGI     | 2025-11-04 | After market close | Communication Services | $570.7M      | $13.05  | 42.05%       | 110.61%      | 2.63x         |
|  1 | PAYO     | 2025-11-05 | Before market open | Technology             | $2.1B        | $5.73   | 28.08%       | 73.32%       | 2.61x         |
|  2 | FTDR     | 2025-11-05 | Before market open | Consumer Cyclical      | $4.8B        | $65.47  | 22.86%       | 58.37%       | 2.55x         |
|  3 | SUPN     | 2025-11-04 | After market close | Healthcare             | $3.2B        | $55.70  | 23.26%       | 56.01%       | 2.41x         |
|  4 | MCY      | 2025-11-04 | After market close | Financial Services     | $4.4B        | $76.23  | 24.35%       | 56.23%       | 2.31x         |
|  5 | ELAN     | 2025-11-05 | Before market open | Healthcare             | $11.2B       | $22.85  | 26.91%       | 60.06%       | 2.23x         |
|  6 | SABR     | 2025-11-05 | Before market open | Technology             | $789.0M      | $2.01   | 60.92%       | 133.51%      | 2.19x         |
|  7 | PRGO     | 2025-11-05 | Before market open | Healthcare             | $2.8B        | $20.53  | 25.96%       | 56.69%       | 2.18x         |
|  8 | KD       | 2025-11-04 | After market close | Technology             | $6.3B        | $28.75  | 31.15%       | 67.72%       | 2.17x         |
|  9 | NYT      | 2025-11-05 | Before market open | Communication Services | $9.4B        | $57.06  | 15.65%       | 33.98%       | 2.17x         |
| 10 | MTCH     | 2025-11-04 | After market close | Communication Services | $7.6B        | $32.50  | 23.72%       | 50.35%       | 2.12x         |
| 11 | PFGC     | 2025-11-05 | Before market open | Consumer Defensive     | $15.4B       | $97.98  | 17.20%       | 36.27%       | 2.11x         |
| 12 | VOYA     | 2025-11-04 | After market close | Financial Services     | $7.1B        | $73.14  | 21.27%       | 44.81%       | 2.11x         |
| 13 | SMG      | 2025-11-05 | Before market open | Basic Materials        | $3.1B        | $54.00  | 25.43%       | 53.56%       | 2.11x         |
| 14 | IFF      | 2025-11-04 | After market close | Basic Materials        | $15.8B       | $62.08  | 21.01%       | 44.20%       | 2.10x         |
| 15 | XPEL     | 2025-11-05 | Before market open | Consumer Cyclical      | $968.0M      | $34.61  | 27.89%       | 55.77%       | 2.00x         |
| 16 | GO       | 2025-11-04 | After market close | Consumer Defensive     | $1.4B        | $14.24  | 37.22%       | 74.28%       | 2.00x         |
| 17 | SWX      | 2025-11-05 | Before market open | Utilities              | $5.9B        | $80.97  | 14.52%       | 28.91%       | 1.99x         |
| 18 | SHOO     | 2025-11-05 | Before market open | Consumer Cyclical      | $2.4B        | $32.80  | 34.24%       | 67.80%       | 1.98x         |
| 19 | MASI     | 2025-11-04 | After market close | Healthcare             | $8.1B        | $144.96 | 27.65%       | 54.58%       | 1.97x         |
| 20 | JCI      | 2025-11-05 | Before market open | Industrials            | $74.1B       | $113.18 | 20.45%       | 40.24%       | 1.97x         |
| 21 | QLYS     | 2025-11-04 | After market close | Technology             | $4.4B        | $125.12 | 22.11%       | 43.47%       | 1.97x         |
| 22 | PCTY     | 2025-11-04 | After market close | Technology             | $7.6B        | $140.81 | 24.14%       | 47.36%       | 1.96x         |
| 23 | TREX     | 2025-11-04 | After market close | Industrials            | $5.1B        | $47.94  | 29.44%       | 57.61%       | 1.96x         |
| 24 | DT       | 2025-11-05 | Before market open | Technology             | $15.0B       | $50.48  | 27.19%       | 53.05%       | 1.95x         |
| 25 | PSN      | 2025-11-05 | Before market open | Technology             | $8.5B        | $79.74  | 27.46%       | 53.31%       | 1.94x         |
| 26 | LIVN     | 2025-11-05 | Before market open | Healthcare             | $2.9B        | $52.58  | 27.55%       | 53.16%       | 1.93x         |
| 27 | JKHY     | 2025-11-04 | After market close | Technology             | $11.1B       | $150.63 | 17.86%       | 33.81%       | 1.89x         |
| 28 | WWW      | 2025-11-05 | Before market open | Consumer Cyclical      | $1.8B        | $22.34  | 41.19%       | 75.84%       | 1.84x         |
| 29 | BCO      | 2025-11-05 | Before market open | Industrials            | $4.4B        | $110.59 | 18.79%       | 34.59%       | 1.84x         |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
