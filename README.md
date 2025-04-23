# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-04-22 21:48:42 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | USNA     | 2025-04-22 | After market close | Consumer Defensive     | $457.2M      | $23.83  | 40.74%       | 66.44%       | 1.63x         |
|  1 | PRG      | 2025-04-23 | Before market open | Industrials            | $1.1B        | $25.78  | 56.50%       | 88.74%       | 1.57x         |
|  2 | CASH     | 2025-04-22 | After market close | Financial Services     | $1.8B        | $70.31  | 37.34%       | 57.64%       | 1.54x         |
|  3 | TMHC     | 2025-04-23 | Before market open | Consumer Cyclical      | $5.9B        | $55.59  | 41.74%       | 63.76%       | 1.53x         |
|  4 | HCSG     | 2025-04-23 | Before market open | Healthcare             | $694.2M      | $9.37   | 29.87%       | 44.14%       | 1.48x         |
|  5 | MCRI     | 2025-04-22 | After market close | Consumer Cyclical      | $1.5B        | $73.73  | 33.84%       | 45.39%       | 1.34x         |
|  6 | PM       | 2025-04-23 | Before market open | Consumer Defensive     | $255.4B      | $162.18 | 30.43%       | 39.83%       | 1.31x         |
|  7 | MHO      | 2025-04-23 | Before market open | Consumer Cyclical      | $2.9B        | $103.90 | 41.57%       | 51.65%       | 1.24x         |
|  8 | VBTX     | 2025-04-22 | After market close | Financial Services     | $1.2B        | $21.53  | 48.67%       | 59.63%       | 1.23x         |
|  9 | ENPH     | 2025-04-22 | After market close | Technology             | $7.0B        | $51.62  | 70.60%       | 85.98%       | 1.22x         |
| 10 | GATX     | 2025-04-23 | Before market open | Industrials            | $5.3B        | $145.62 | 31.69%       | 38.35%       | 1.21x         |
| 11 | WSO      | 2025-04-23 | Before market open | Industrials            | $20.4B       | $494.91 | 39.10%       | 45.92%       | 1.17x         |
| 12 | T        | 2025-04-23 | Before market open | Communication Services | $194.1B      | $26.33  | 31.85%       | 36.03%       | 1.13x         |
| 13 | PMT      | 2025-04-22 | After market close | Real Estate            | $1.1B        | $12.90  | 37.73%       | 42.16%       | 1.12x         |
| 14 | CME      | 2025-04-23 | Before market open | Financial Services     | $95.7B       | $260.33 | 23.53%       | 25.66%       | 1.09x         |
| 15 | AVY      | 2025-04-23 | Before market open | Consumer Cyclical      | $13.8B       | $169.03 | 31.84%       | 34.16%       | 1.07x         |
| 16 | TMO      | 2025-04-23 | Before market open | Healthcare             | $164.1B      | $421.85 | 43.61%       | 46.29%       | 1.06x         |
| 17 | TDY      | 2025-04-23 | Before market open | Technology             | $21.6B       | $453.35 | 39.46%       | 41.26%       | 1.05x         |
| 18 | ADC      | 2025-04-22 | After market close | Real Estate            | $8.6B        | $78.72  | 23.97%       | 25.02%       | 1.04x         |
| 19 | LAD      | 2025-04-23 | Before market open | Consumer Cyclical      | $7.8B        | $283.82 | 55.62%       | 56.64%       | 1.02x         |
| 20 | LII      | 2025-04-23 | Before market open | Industrials            | $19.8B       | $541.02 | 46.89%       | 47.12%       | 1.00x         |
| 21 | MAS      | 2025-04-23 | Before market open | Industrials            | $13.0B       | $60.05  | 46.88%       | 46.79%       | 1.00x         |
| 22 | CB       | 2025-04-22 | After market close | Financial Services     | $116.4B      | $279.78 | 30.81%       | 30.66%       | 1.00x         |
| 23 | ODFL     | 2025-04-23 | Before market open | Industrials            | $32.7B       | $149.87 | 56.06%       | 55.72%       | 0.99x         |
| 24 | EQT      | 2025-04-22 | After market close | Energy                 | $30.5B       | $47.68  | 53.47%       | 52.79%       | 0.99x         |
| 25 | PKG      | 2025-04-22 | After market close | Consumer Cyclical      | $16.8B       | $182.07 | 38.92%       | 38.41%       | 0.99x         |
| 26 | PB       | 2025-04-23 | Before market open | Financial Services     | $6.4B        | $65.53  | 36.04%       | 34.88%       | 0.97x         |
| 27 | MANH     | 2025-04-22 | After market close | Technology             | $9.9B        | $160.51 | 65.30%       | 62.93%       | 0.96x         |
| 28 | VIRT     | 2025-04-23 | Before market open | Financial Services     | $6.0B        | $37.16  | 54.02%       | 51.99%       | 0.96x         |
| 29 | ZWS      | 2025-04-22 | After market close | Industrials            | $5.3B        | $29.69  | 41.05%       | 39.03%       | 0.95x         |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
