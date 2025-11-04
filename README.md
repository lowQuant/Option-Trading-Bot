# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-11-03 20:51:49 EST

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | HLIT     | 2025-11-03 | After market close | Technology             | $1.2B        | $10.70  | 28.56%       | 88.37%       | 3.09x         |
|  1 | INGR     | 2025-11-04 | Before market open | Consumer Defensive     | $7.3B        | $115.41 | 11.88%       | 31.47%       | 2.65x         |
|  2 | GT       | 2025-11-03 | After market close | Consumer Cyclical      | $2.0B        | $6.89   | 29.05%       | 71.67%       | 2.47x         |
|  3 | MZTI     | 2025-11-04 | Before market open | Consumer Defensive     | $4.4B        | $156.79 | 15.67%       | 35.91%       | 2.29x         |
|  4 | ENSG     | 2025-11-03 | After market close | Healthcare             | $10.6B       | $180.10 | 14.61%       | 32.82%       | 2.25x         |
|  5 | INSP     | 2025-11-03 | After market close | Healthcare             | $2.2B        | $72.08  | 36.94%       | 82.54%       | 2.23x         |
|  6 | ZTS      | 2025-11-04 | Before market open | Healthcare             | $64.0B       | $144.09 | 15.43%       | 33.29%       | 2.16x         |
|  7 | BALL     | 2025-11-04 | Before market open | Consumer Cyclical      | $12.8B       | $47.00  | 17.84%       | 38.08%       | 2.13x         |
|  8 | HSIC     | 2025-11-04 | Before market open | Healthcare             | $7.8B        | $63.20  | 19.88%       | 42.33%       | 2.13x         |
|  9 | APLE     | 2025-11-03 | After market close | Real Estate            | $2.7B        | $11.19  | 15.58%       | 32.99%       | 2.12x         |
| 10 | BCC      | 2025-11-03 | After market close | Basic Materials        | $2.6B        | $70.49  | 27.56%       | 58.27%       | 2.11x         |
| 11 | SBAC     | 2025-11-03 | After market close | Real Estate            | $20.8B       | $191.48 | 16.08%       | 32.79%       | 2.04x         |
| 12 | HALO     | 2025-11-03 | After market close | Healthcare             | $7.7B        | $65.19  | 25.59%       | 51.18%       | 2.00x         |
| 13 | HTZ      | 2025-11-04 | Before market open | Industrials            | $1.5B        | $5.13   | 59.36%       | 117.10%      | 1.97x         |
| 14 | MYGN     | 2025-11-03 | After market close | Healthcare             | $761.1M      | $8.04   | 47.45%       | 91.48%       | 1.93x         |
| 15 | JBTM     | 2025-11-03 | After market close | Industrials            | $6.5B        | $126.10 | 28.50%       | 53.68%       | 1.88x         |
| 16 | SRPT     | 2025-11-03 | After market close | Healthcare             | $2.6B        | $24.01  | 62.57%       | 115.18%      | 1.84x         |
| 17 | FN       | 2025-11-03 | After market close | Technology             | $15.9B       | $440.57 | 41.73%       | 76.47%       | 1.83x         |
| 18 | NCLH     | 2025-11-04 | Before market open | Consumer Cyclical      | $10.1B       | $22.42  | 28.10%       | 50.61%       | 1.80x         |
| 19 | UBER     | 2025-11-04 | Before market open | Technology             | $208.0B      | $96.50  | 25.13%       | 45.24%       | 1.80x         |
| 20 | UNM      | 2025-11-03 | After market close | Financial Services     | $12.4B       | $73.42  | 19.14%       | 34.41%       | 1.80x         |
| 21 | VRTX     | 2025-11-03 | After market close | Healthcare             | $109.2B      | $425.57 | 21.01%       | 37.23%       | 1.77x         |
| 22 | NNN      | 2025-11-04 | Before market open | Real Estate            | $7.7B        | $40.46  | 12.19%       | 21.54%       | 1.77x         |
| 23 | SEE      | 2025-11-04 | Before market open | Consumer Cyclical      | $5.0B        | $33.51  | 24.74%       | 43.62%       | 1.76x         |
| 24 | WING     | 2025-11-04 | Before market open | Consumer Cyclical      | $6.0B        | $216.63 | 51.28%       | 89.77%       | 1.75x         |
| 25 | IAC      | 2025-11-03 | After market close | Communication Services | $2.6B        | $32.22  | 25.82%       | 45.05%       | 1.74x         |
| 26 | TNC      | 2025-11-03 | After market close | Industrials            | $1.5B        | $80.00  | 17.61%       | 30.71%       | 1.74x         |
| 27 | PRAA     | 2025-11-03 | After market close | Financial Services     | $572.4M      | $13.71  | 37.36%       | 64.94%       | 1.74x         |
| 28 | NSP      | 2025-11-03 | After market close | Industrials            | $1.7B        | $44.12  | 30.83%       | 53.15%       | 1.72x         |
| 29 | LSCC     | 2025-11-03 | After market close | Technology             | $10.0B       | $72.96  | 39.17%       | 66.90%       | 1.71x         |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
