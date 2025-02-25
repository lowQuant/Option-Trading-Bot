# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-02-24 20:40:41 EST

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | XHR      | 2025-02-25 | Before market open | Real Estate            | $1.5B        | $14.00  | 21.09%       | 69.45%       | 3.29x         |
|  1 | MODG     | 2025-02-24 | After market close | Consumer Cyclical      | $1.2B        | $7.01   | 45.94%       | 115.86%      | 2.52x         |
|  2 | NOVT     | 2025-02-25 | Before market open | Technology             | $5.0B        | $140.51 | 19.42%       | 43.43%       | 2.24x         |
|  3 | SEE      | 2025-02-25 | Before market open | Consumer Cyclical      | $4.7B        | $32.35  | 19.88%       | 41.08%       | 2.07x         |
|  4 | CRI      | 2025-02-25 | Before market open | Consumer Cyclical      | $1.9B        | $52.05  | 25.73%       | 52.61%       | 2.04x         |
|  5 | PRA      | 2025-02-24 | After market close | Financial Services     | $721.8M      | $13.99  | 33.25%       | 66.08%       | 1.99x         |
|  6 | TILE     | 2025-02-25 | Before market open | Industrials            | $1.2B        | $21.48  | 30.72%       | 56.20%       | 1.83x         |
|  7 | ITRI     | 2025-02-25 | Before market open | Technology             | $4.2B        | $93.94  | 29.73%       | 52.28%       | 1.76x         |
|  8 | PLNT     | 2025-02-25 | Before market open | Consumer Cyclical      | $8.4B        | $96.89  | 27.12%       | 47.12%       | 1.74x         |
|  9 | LIVN     | 2025-02-25 | Before market open | Healthcare             | $2.7B        | $47.44  | 23.52%       | 40.70%       | 1.73x         |
| 10 | INN      | 2025-02-24 | After market close | Real Estate            | $687.4M      | $6.32   | 22.57%       | 37.60%       | 1.67x         |
| 11 | JBTM     | 2025-02-24 | After market close | Industrials            | $6.1B        | $118.92 | 26.45%       | 43.57%       | 1.65x         |
| 12 | KBR      | 2025-02-24 | After market close | Industrials            | $6.7B        | $49.14  | 24.81%       | 40.17%       | 1.62x         |
| 13 | HLX      | 2025-02-24 | After market close | Energy                 | $1.2B        | $7.89   | 32.00%       | 50.81%       | 1.59x         |
| 14 | ZD       | 2025-02-24 | After market close | Communication Services | $2.1B        | $47.93  | 30.30%       | 45.20%       | 1.49x         |
| 15 | TREX     | 2025-02-24 | After market close | Industrials            | $6.6B        | $60.58  | 37.54%       | 54.98%       | 1.46x         |
| 16 | PSA      | 2025-02-24 | After market close | Real Estate            | $53.1B       | $304.19 | 17.96%       | 25.99%       | 1.45x         |
| 17 | VNOM     | 2025-02-24 | After market close | Energy                 | $10.3B       | $48.33  | 27.18%       | 39.16%       | 1.44x         |
| 18 | GSHD     | 2025-02-24 | After market close | Financial Services     | $3.9B        | $106.68 | 45.31%       | 65.18%       | 1.44x         |
| 19 | CWEN     | 2025-02-24 | After market close | Utilities              | $5.3B        | $27.43  | 28.20%       | 40.25%       | 1.43x         |
| 20 | DOCN     | 2025-02-25 | Before market open | Technology             | $3.4B        | $39.30  | 49.20%       | 69.08%       | 1.40x         |
| 21 | MYGN     | 2025-02-24 | After market close | Healthcare             | $1.3B        | $14.18  | 54.98%       | 76.59%       | 1.39x         |
| 22 | HSIC     | 2025-02-25 | Before market open | Healthcare             | $9.6B        | $77.24  | 24.33%       | 33.88%       | 1.39x         |
| 23 | UFPT     | 2025-02-25 | Before market open | Healthcare             | $1.8B        | $254.56 | 47.15%       | 64.12%       | 1.36x         |
| 24 | FANG     | 2025-02-24 | After market close | Energy                 | $45.3B       | $156.12 | 27.22%       | 35.35%       | 1.30x         |
| 25 | HD       | 2025-02-25 | Before market open | Consumer Cyclical      | $379.9B      | $385.30 | 22.85%       | 29.61%       | 1.30x         |
| 26 | UCTT     | 2025-02-24 | After market close | Technology             | $1.6B        | $37.35  | 49.68%       | 63.18%       | 1.27x         |
| 27 | LGIH     | 2025-02-25 | Before market open | Consumer Cyclical      | $1.8B        | $77.80  | 43.09%       | 53.33%       | 1.24x         |
| 28 | BLD      | 2025-02-25 | Before market open | Industrials            | $8.9B        | $303.78 | 36.89%       | 45.15%       | 1.22x         |
| 29 | KTB      | 2025-02-25 | Before market open | Consumer Cyclical      | $4.8B        | $87.93  | 37.97%       | 46.42%       | 1.22x         |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
