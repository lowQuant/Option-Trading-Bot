# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-07-22 22:05:22 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | VICR     | 2025-07-22 | After market close | Technology             | $2.0B        | $47.80  | 29.47%       | 88.95%       | 3.02x         |
|  1 | APH      | 2025-07-23 | Before market open | Technology             | $123.1B      | $103.71 | 15.60%       | 37.03%       | 2.37x         |
|  2 | MANH     | 2025-07-22 | After market close | Technology             | $12.3B       | $199.73 | 22.38%       | 49.57%       | 2.21x         |
|  3 | LW       | 2025-07-23 | Before market open | Consumer Defensive     | $6.9B        | $48.04  | 23.95%       | 52.05%       | 2.17x         |
|  4 | PEGA     | 2025-07-22 | After market close | Technology             | $8.7B        | $51.34  | 30.08%       | 64.39%       | 2.14x         |
|  5 | CSGP     | 2025-07-22 | After market close | Real Estate            | $35.9B       | $85.01  | 18.50%       | 37.65%       | 2.04x         |
|  6 | KREF     | 2025-07-22 | After market close | Real Estate            | $613.6M      | $8.88   | 24.80%       | 45.59%       | 1.84x         |
|  7 | HCSG     | 2025-07-23 | Before market open | Healthcare             | $951.6M      | $12.74  | 30.96%       | 56.21%       | 1.82x         |
|  8 | TRMK     | 2025-07-22 | After market close | Financial Services     | $2.3B        | $38.52  | 21.35%       | 36.82%       | 1.72x         |
|  9 | FI       | 2025-07-23 | Before market open | Technology             | $92.0B       | $165.46 | 22.68%       | 38.55%       | 1.70x         |
| 10 | TEL      | 2025-07-23 | Before market open | Technology             | $53.5B       | $179.51 | 15.73%       | 26.59%       | 1.69x         |
| 11 | BKU      | 2025-07-23 | Before market open | Financial Services     | $2.9B        | $37.81  | 26.40%       | 44.30%       | 1.68x         |
| 12 | BSX      | 2025-07-23 | Before market open | Healthcare             | $152.6B      | $103.78 | 17.41%       | 29.21%       | 1.68x         |
| 13 | GEV      | 2025-07-23 | Before market open | Industrials            | $149.8B      | $565.91 | 29.28%       | 49.06%       | 1.68x         |
| 14 | TXN      | 2025-07-22 | After market close | Technology             | $195.2B      | $214.57 | 20.33%       | 34.03%       | 1.67x         |
| 15 | HAS      | 2025-07-23 | Before market open | Consumer Cyclical      | $10.9B       | $77.67  | 26.79%       | 43.50%       | 1.62x         |
| 16 | ISRG     | 2025-07-22 | After market close | Healthcare             | $183.2B      | $516.12 | 24.57%       | 37.72%       | 1.54x         |
| 17 | GD       | 2025-07-23 | Before market open | Industrials            | $79.9B       | $297.05 | 13.57%       | 20.58%       | 1.52x         |
| 18 | T        | 2025-07-23 | Before market open | Communication Services | $197.4B      | $27.38  | 18.26%       | 27.37%       | 1.50x         |
| 19 | OTIS     | 2025-07-23 | Before market open | Industrials            | $39.9B       | $98.50  | 15.67%       | 23.32%       | 1.49x         |
| 20 | TDY      | 2025-07-23 | Before market open | Technology             | $26.1B       | $559.27 | 15.84%       | 23.55%       | 1.49x         |
| 21 | CALM     | 2025-07-22 | After market close | Consumer Defensive     | $5.1B        | $106.17 | 26.34%       | 38.67%       | 1.47x         |
| 22 | CME      | 2025-07-23 | Before market open | Financial Services     | $99.0B       | $275.00 | 14.90%       | 21.87%       | 1.47x         |
| 23 | LII      | 2025-07-23 | Before market open | Industrials            | $22.0B       | $601.03 | 23.42%       | 33.71%       | 1.44x         |
| 24 | COF      | 2025-07-22 | After market close | Financial Services     | $139.1B      | $215.88 | 21.93%       | 30.82%       | 1.41x         |
| 25 | PRG      | 2025-07-23 | Before market open | Industrials            | $1.2B        | $28.22  | 33.01%       | 45.50%       | 1.38x         |
| 26 | TMO      | 2025-07-23 | Before market open | Healthcare             | $161.4B      | $404.94 | 29.03%       | 39.51%       | 1.36x         |
| 27 | COOP     | 2025-07-23 | Before market open | Financial Services     | $10.8B       | $160.81 | 43.09%       | 58.23%       | 1.35x         |
| 28 | HLT      | 2025-07-23 | Before market open | Consumer Cyclical      | $65.1B       | $270.85 | 18.45%       | 24.80%       | 1.34x         |
| 29 | MCO      | 2025-07-23 | Before market open | Financial Services     | $89.8B       | $500.16 | 18.37%       | 24.47%       | 1.33x         |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
