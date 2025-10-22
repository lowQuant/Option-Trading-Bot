# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-10-21 21:51:56 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close    | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:---------|:-------------|:-------------|:--------------|
|  0 | KREF     | 2025-10-21 | After market close | Real Estate            | $575.4M      | $8.55    | 22.36%       | 75.32%       | 3.37x         |
|  1 | PEGA     | 2025-10-21 | After market close | Technology             | $9.8B        | $54.74   | 29.48%       | 63.17%       | 2.14x         |
|  2 | MCRI     | 2025-10-21 | After market close | Consumer Cyclical      | $1.8B        | $96.52   | 19.64%       | 39.30%       | 2.00x         |
|  3 | AVY      | 2025-10-22 | Before market open | Consumer Cyclical      | $12.8B       | $160.25  | 15.48%       | 30.58%       | 1.98x         |
|  4 | PRG      | 2025-10-22 | Before market open | Industrials            | $1.3B        | $31.75   | 26.06%       | 49.63%       | 1.90x         |
|  5 | MANH     | 2025-10-21 | After market close | Technology             | $12.4B       | $200.02  | 29.96%       | 54.21%       | 1.81x         |
|  6 | TXN      | 2025-10-21 | After market close | Technology             | $164.4B      | $179.59  | 24.02%       | 41.56%       | 1.73x         |
|  7 | NFLX     | 2025-10-21 | After market close | Communication Services | $527.5B      | $1238.56 | 24.37%       | 41.03%       | 1.68x         |
|  8 | APH      | 2025-10-22 | Before market open | Technology             | $151.9B      | $127.67  | 27.56%       | 46.29%       | 1.68x         |
|  9 | CATY     | 2025-10-21 | After market close | Financial Services     | $3.3B        | $47.00   | 35.10%       | 56.26%       | 1.60x         |
| 10 | BSX      | 2025-10-22 | Before market open | Healthcare             | $148.0B      | $100.53  | 18.60%       | 29.37%       | 1.58x         |
| 11 | CME      | 2025-10-22 | Before market open | Financial Services     | $96.9B       | $267.62  | 15.72%       | 24.46%       | 1.56x         |
| 12 | LAD      | 2025-10-22 | Before market open | Consumer Cyclical      | $8.1B        | $309.22  | 30.21%       | 46.20%       | 1.53x         |
| 13 | MAT      | 2025-10-21 | After market close | Consumer Cyclical      | $6.1B        | $18.37   | 30.81%       | 46.20%       | 1.50x         |
| 14 | HLT      | 2025-10-22 | Before market open | Consumer Cyclical      | $62.6B       | $261.04  | 18.61%       | 27.70%       | 1.49x         |
| 15 | LII      | 2025-10-22 | Before market open | Industrials            | $19.3B       | $534.75  | 27.26%       | 40.47%       | 1.48x         |
| 16 | TNL      | 2025-10-22 | Before market open | Consumer Cyclical      | $3.9B        | $60.15   | 21.85%       | 32.04%       | 1.47x         |
| 17 | WGO      | 2025-10-22 | Before market open | Consumer Cyclical      | $886.3M      | $30.51   | 40.64%       | 58.55%       | 1.44x         |
| 18 | GEV      | 2025-10-22 | Before market open | Industrials            | $160.9B      | $594.07  | 41.53%       | 59.44%       | 1.43x         |
| 19 | TMHC     | 2025-10-22 | Before market open | Consumer Cyclical      | $6.2B        | $62.13   | 27.46%       | 38.70%       | 1.41x         |
| 20 | VICR     | 2025-10-21 | After market close | Technology             | $2.9B        | $58.04   | 55.92%       | 78.06%       | 1.40x         |
| 21 | WFRD     | 2025-10-21 | After market close | Energy                 | $4.8B        | $64.92   | 37.15%       | 51.29%       | 1.38x         |
| 22 | T        | 2025-10-22 | Before market open | Communication Services | $188.0B      | $26.10   | 20.52%       | 27.91%       | 1.36x         |
| 23 | UNF      | 2025-10-22 | Before market open | Industrials            | $3.2B        | $171.33  | 25.75%       | 34.84%       | 1.35x         |
| 24 | HCSG     | 2025-10-22 | Before market open | Healthcare             | $1.2B        | $16.45   | 33.84%       | 45.42%       | 1.34x         |
| 25 | MHO      | 2025-10-22 | Before market open | Consumer Cyclical      | $3.7B        | $139.01  | 31.70%       | 42.43%       | 1.34x         |
| 26 | WAB      | 2025-10-22 | Before market open | Industrials            | $33.8B       | $196.12  | 24.55%       | 32.81%       | 1.34x         |
| 27 | ADC      | 2025-10-21 | After market close | Real Estate            | $8.3B        | $75.76   | 14.82%       | 19.60%       | 1.32x         |
| 28 | CASH     | 2025-10-21 | After market close | Financial Services     | $1.6B        | $71.98   | 32.34%       | 42.49%       | 1.31x         |
| 29 | NTRS     | 2025-10-22 | Before market open | Financial Services     | $24.5B       | $128.85  | 26.55%       | 34.47%       | 1.30x         |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
