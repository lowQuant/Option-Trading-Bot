# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-02-07 05:57:53 EST

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close    | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:---------|:-------------|:-------------|:--------------|
|  0 | FTNT     | 2025-02-06 | After market close | Technology             | $80.3B       | $105.07  | 22.06%       | 58.32%       | 2.64x         |
|  1 | LESL     | 2025-02-06 | After market close | Consumer Cyclical      | $414.9M      | $2.22    | 42.79%       | 105.97%      | 2.48x         |
|  2 | NWL      | 2025-02-07 | Before market open | Consumer Defensive     | $4.0B        | $9.70    | 27.56%       | 66.02%       | 2.40x         |
|  3 | G        | 2025-02-06 | After market close | Technology             | $8.7B        | $49.41   | 15.95%       | 36.78%       | 2.31x         |
|  4 | BYD      | 2025-02-06 | After market close | Consumer Cyclical      | $6.9B        | $76.49   | 16.17%       | 36.89%       | 2.28x         |
|  5 | DOCS     | 2025-02-06 | After market close | Healthcare             | $10.9B       | $58.14   | 40.02%       | 90.10%       | 2.25x         |
|  6 | EXPO     | 2025-02-06 | After market close | Industrials            | $4.6B        | $92.61   | 19.75%       | 43.91%       | 2.22x         |
|  7 | EXPE     | 2025-02-06 | After market close | Consumer Cyclical      | $22.1B       | $169.73  | 24.93%       | 54.35%       | 2.18x         |
|  8 | BILL     | 2025-02-06 | After market close | Technology             | $10.0B       | $97.03   | 35.65%       | 75.24%       | 2.11x         |
|  9 | PRLB     | 2025-02-07 | Before market open | Industrials            | $1.1B        | $44.25   | 30.37%       | 62.60%       | 2.06x         |
| 10 | PFG      | 2025-02-06 | After market close | Financial Services     | $18.3B       | $80.57   | 15.65%       | 31.09%       | 1.99x         |
| 11 | FTV      | 2025-02-07 | Before market open | Technology             | $27.7B       | $79.49   | 15.25%       | 29.14%       | 1.91x         |
| 12 | PCTY     | 2025-02-06 | After market close | Technology             | $11.8B       | $209.12  | 24.92%       | 46.34%       | 1.86x         |
| 13 | QLYS     | 2025-02-06 | After market close | Technology             | $5.1B        | $145.97  | 26.41%       | 48.91%       | 1.85x         |
| 14 | FBIN     | 2025-02-06 | After market close | Industrials            | $8.6B        | $69.35   | 25.17%       | 44.36%       | 1.76x         |
| 15 | RGA      | 2025-02-06 | After market close | Financial Services     | $15.2B       | $229.50  | 16.49%       | 28.56%       | 1.73x         |
| 16 | VRSN     | 2025-02-06 | After market close | Technology             | $21.2B       | $220.91  | 14.83%       | 25.41%       | 1.71x         |
| 17 | SKX      | 2025-02-06 | After market close | Consumer Cyclical      | $11.4B       | $74.41   | 29.36%       | 50.27%       | 1.71x         |
| 18 | AMZN     | 2025-02-06 | After market close | Consumer Cyclical      | $2.5tr       | $236.17  | 22.33%       | 37.81%       | 1.69x         |
| 19 | QNST     | 2025-02-06 | After market close | Communication Services | $1.4B        | $25.00   | 50.45%       | 84.39%       | 1.67x         |
| 20 | ESE      | 2025-02-06 | After market close | Technology             | $3.4B        | $133.61  | 19.15%       | 31.93%       | 1.67x         |
| 21 | MCHP     | 2025-02-06 | After market close | Technology             | $28.5B       | $53.50   | 31.77%       | 52.93%       | 1.67x         |
| 22 | ELF      | 2025-02-06 | After market close | Consumer Defensive     | $5.0B        | $87.32   | 53.30%       | 87.32%       | 1.64x         |
| 23 | SONO     | 2025-02-06 | After market close | Technology             | $1.8B        | $14.26   | 29.92%       | 48.79%       | 1.63x         |
| 24 | MHK      | 2025-02-06 | After market close | Consumer Cyclical      | $7.7B        | $120.84  | 29.46%       | 47.07%       | 1.60x         |
| 25 | POWI     | 2025-02-06 | After market close | Technology             | $3.5B        | $62.50   | 31.60%       | 50.44%       | 1.60x         |
| 26 | AVTR     | 2025-02-07 | Before market open | Healthcare             | $14.8B       | $21.99   | 26.90%       | 42.82%       | 1.59x         |
| 27 | MTX      | 2025-02-06 | After market close | Basic Materials        | $2.4B        | $75.89   | 18.39%       | 29.15%       | 1.59x         |
| 28 | TTWO     | 2025-02-06 | After market close | Communication Services | $32.2B       | $184.92  | 24.49%       | 38.69%       | 1.58x         |
| 29 | MTD      | 2025-02-06 | After market close | Healthcare             | $28.6B       | $1363.56 | 21.84%       | 34.42%       | 1.58x         |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
