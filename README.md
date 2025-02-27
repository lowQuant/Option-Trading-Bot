# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-02-26 20:41:14 EST

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | SHC      | 2025-02-27 | Before market open | Healthcare             | $3.9B        | $13.73  | 22.27%       | 72.16%       | 3.24x         |
|  1 | XRAY     | 2025-02-27 | Before market open | Healthcare             | $3.7B        | $18.82  | 27.55%       | 82.18%       | 2.98x         |
|  2 | AMBC     | 2025-02-26 | After market close | Financial Services     | $553.2M      | $11.90  | 19.40%       | 51.45%       | 2.65x         |
|  3 | HAYW     | 2025-02-27 | Before market open | Industrials            | $3.1B        | $14.41  | 29.31%       | 72.86%       | 2.49x         |
|  4 | INVH     | 2025-02-26 | After market close | Real Estate            | $19.3B       | $32.10  | 16.14%       | 38.34%       | 2.38x         |
|  5 | FTDR     | 2025-02-27 | Before market open | Consumer Cyclical      | $4.3B        | $57.55  | 27.95%       | 64.70%       | 2.31x         |
|  6 | STRA     | 2025-02-27 | Before market open | Consumer Defensive     | $2.4B        | $97.40  | 18.51%       | 42.48%       | 2.29x         |
|  7 | CPRX     | 2025-02-26 | After market close | Healthcare             | $2.5B        | $20.80  | 29.65%       | 65.15%       | 2.20x         |
|  8 | VTRS     | 2025-02-27 | Before market open | Healthcare             | $13.7B       | $11.48  | 19.90%       | 43.39%       | 2.18x         |
|  9 | TNDM     | 2025-02-26 | After market close | Healthcare             | $2.2B        | $33.34  | 40.48%       | 88.12%       | 2.18x         |
| 10 | DORM     | 2025-02-26 | After market close | Consumer Cyclical      | $3.8B        | $125.57 | 19.22%       | 41.83%       | 2.18x         |
| 11 | AMWD     | 2025-02-27 | Before market open | Consumer Cyclical      | $1.1B        | $71.74  | 29.55%       | 62.97%       | 2.13x         |
| 12 | EVTC     | 2025-02-26 | After market close | Technology             | $2.1B        | $32.66  | 15.89%       | 32.94%       | 2.07x         |
| 13 | PEB      | 2025-02-26 | After market close | Real Estate            | $1.4B        | $11.53  | 27.32%       | 56.21%       | 2.06x         |
| 14 | ACIW     | 2025-02-27 | Before market open | Technology             | $5.3B        | $50.56  | 22.25%       | 45.53%       | 2.05x         |
| 15 | TGNA     | 2025-02-27 | Before market open | Communication Services | $2.7B        | $16.93  | 18.78%       | 38.18%       | 2.03x         |
| 16 | MORN     | 2025-02-26 | After market close | Financial Services     | $13.9B       | $323.21 | 15.31%       | 30.74%       | 2.01x         |
| 17 | PENN     | 2025-02-27 | Before market open | Consumer Cyclical      | $3.1B        | $20.37  | 34.49%       | 69.12%       | 2.00x         |
| 18 | PAYO     | 2025-02-27 | Before market open | Technology             | $3.6B        | $9.95   | 39.40%       | 78.08%       | 1.98x         |
| 19 | CRGY     | 2025-02-26 | After market close | Energy                 | $3.5B        | $13.69  | 30.99%       | 60.76%       | 1.96x         |
| 20 | EBAY     | 2025-02-26 | After market close | Consumer Cyclical      | $33.1B       | $70.93  | 19.37%       | 37.50%       | 1.94x         |
| 21 | PRVA     | 2025-02-27 | Before market open | Healthcare             | $2.9B        | $24.53  | 27.98%       | 53.99%       | 1.93x         |
| 22 | NXST     | 2025-02-27 | Before market open | Communication Services | $4.6B        | $149.23 | 18.63%       | 35.52%       | 1.91x         |
| 23 | ECPG     | 2025-02-26 | After market close | Financial Services     | $1.2B        | $49.89  | 23.45%       | 44.13%       | 1.88x         |
| 24 | CCOI     | 2025-02-27 | Before market open | Communication Services | $3.9B        | $79.22  | 21.71%       | 40.67%       | 1.87x         |
| 25 | GEO      | 2025-02-27 | Before market open | Industrials            | $3.6B        | $25.84  | 50.91%       | 94.12%       | 1.85x         |
| 26 | VTOL     | 2025-02-26 | After market close | Energy                 | $1.0B        | $35.47  | 25.99%       | 47.77%       | 1.84x         |
| 27 | WBD      | 2025-02-27 | Before market open | Communication Services | $25.8B       | $10.69  | 33.08%       | 60.58%       | 1.83x         |
| 28 | FWRD     | 2025-02-26 | After market close | Industrials            | $793.1M      | $27.43  | 44.95%       | 79.81%       | 1.78x         |
| 29 | HGV      | 2025-02-27 | Before market open | Consumer Cyclical      | $4.0B        | $40.47  | 26.33%       | 45.34%       | 1.72x         |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
