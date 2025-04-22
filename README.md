# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-04-21 21:48:21 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | DCOM     | 2025-04-22 | Before market open | Financial Services     | $1.1B        | $25.21  | 44.99%       | 92.29%       | 2.05x         |
|  1 | IRDM     | 2025-04-22 | Before market open | Communication Services | $2.5B        | $23.77  | 49.26%       | 62.70%       | 1.27x         |
|  2 | ONB      | 2025-04-22 | Before market open | Financial Services     | $6.1B        | $19.59  | 60.91%       | 76.63%       | 1.26x         |
|  3 | DGX      | 2025-04-22 | Before market open | Healthcare             | $18.0B       | $163.80 | 25.59%       | 31.82%       | 1.24x         |
|  4 | MEDP     | 2025-04-21 | After market close | Healthcare             | $8.7B        | $296.28 | 51.75%       | 63.71%       | 1.23x         |
|  5 | ELV      | 2025-04-22 | Before market open | Healthcare             | $92.1B       | $424.53 | 30.80%       | 36.78%       | 1.19x         |
|  6 | SFBS     | 2025-04-21 | After market close | Financial Services     | $3.8B        | $69.72  | 49.01%       | 57.19%       | 1.17x         |
|  7 | PHM      | 2025-04-22 | Before market open | Consumer Cyclical      | $18.8B       | $94.95  | 41.44%       | 43.83%       | 1.06x         |
|  8 | CALX     | 2025-04-21 | After market close | Technology             | $2.2B        | $33.84  | 60.85%       | 62.46%       | 1.03x         |
|  9 | AZZ      | 2025-04-21 | After market close | Industrials            | $2.3B        | $81.00  | 51.62%       | 52.35%       | 1.01x         |
| 10 | UCB      | 2025-04-22 | Before market open | Financial Services     | $2.9B        | $24.79  | 49.35%       | 49.55%       | 1.00x         |
| 11 | WRB      | 2025-04-21 | After market close | Financial Services     | $25.5B       | $68.80  | 35.06%       | 34.00%       | 0.97x         |
| 12 | NOC      | 2025-04-22 | Before market open | Industrials            | $76.6B       | $540.39 | 31.43%       | 30.36%       | 0.97x         |
| 13 | LMT      | 2025-04-22 | Before market open | Industrials            | $107.5B      | $464.08 | 33.67%       | 31.87%       | 0.95x         |
| 14 | ELS      | 2025-04-21 | After market close | Real Estate            | $12.9B       | $65.32  | 25.75%       | 24.22%       | 0.94x         |
| 15 | GPC      | 2025-04-22 | Before market open | Consumer Cyclical      | $15.5B       | $114.10 | 40.47%       | 38.02%       | 0.94x         |
| 16 | MMM      | 2025-04-22 | Before market open | Industrials            | $68.0B       | $130.21 | 49.05%       | 45.29%       | 0.92x         |
| 17 | VMI      | 2025-04-22 | Before market open | Industrials            | $5.4B        | $277.83 | 57.44%       | 51.95%       | 0.90x         |
| 18 | EFX      | 2025-04-22 | Before market open | Industrials            | $26.9B       | $221.25 | 51.01%       | 46.00%       | 0.90x         |
| 19 | MSCI     | 2025-04-22 | Before market open | Financial Services     | $41.4B       | $546.89 | 42.75%       | 38.42%       | 0.90x         |
| 20 | KMB      | 2025-04-22 | Before market open | Consumer Defensive     | $46.5B       | $142.81 | 26.55%       | 23.56%       | 0.89x         |
| 21 | NTRS     | 2025-04-22 | Before market open | Financial Services     | $16.9B       | $88.30  | 50.53%       | 42.88%       | 0.85x         |
| 22 | RTX      | 2025-04-22 | Before market open | Industrials            | $168.4B      | $128.89 | 39.60%       | 33.41%       | 0.84x         |
| 23 | DHR      | 2025-04-22 | Before market open | Healthcare             | $132.3B      | $186.83 | 49.96%       | 40.86%       | 0.82x         |
| 24 | ZION     | 2025-04-21 | After market close | Financial Services     | $6.4B        | $44.28  | 62.40%       | 49.99%       | 0.80x         |
| 25 | WAL      | 2025-04-21 | After market close | Financial Services     | $7.2B        | $66.32  | 75.25%       | 58.51%       | 0.78x         |
| 26 | IVZ      | 2025-04-22 | Before market open | Financial Services     | $5.6B        | $12.80  | 66.97%       | 50.91%       | 0.76x         |
| 27 | PNR      | 2025-04-22 | Before market open | Industrials            | $13.0B       | $80.36  | 48.16%       | 36.52%       | 0.76x         |
| 28 | GE       | 2025-04-22 | Before market open | Industrials            | $190.2B      | $181.79 | 55.37%       | 41.95%       | 0.76x         |
| 29 | VZ       | 2025-04-22 | Before market open | Communication Services | $184.2B      | $44.04  | 34.82%       | 26.11%       | 0.75x         |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
