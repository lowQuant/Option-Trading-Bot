# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-10-28 21:55:05 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector             | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | GTLS     | 2025-10-29 | Before market open | Industrials        | $9.0B        | $199.50 | 2.24%        | 13.84%       | 6.18x         |
|  1 | GBX      | 2025-10-28 | After market close | Industrials        | $1.4B        | $45.70  | 22.65%       | 59.51%       | 2.63x         |
|  2 | ZWS      | 2025-10-28 | After market close | Industrials        | $7.8B        | $46.62  | 18.01%       | 42.76%       | 2.37x         |
|  3 | CVS      | 2025-10-29 | Before market open | Healthcare         | $104.3B      | $82.45  | 15.54%       | 35.19%       | 2.26x         |
|  4 | LRN      | 2025-10-28 | After market close | Consumer Defensive | $6.7B        | $152.64 | 27.43%       | 62.10%       | 2.26x         |
|  5 | CHE      | 2025-10-28 | After market close | Healthcare         | $6.4B        | $436.78 | 19.32%       | 41.66%       | 2.16x         |
|  6 | MGPI     | 2025-10-29 | Before market open | Consumer Defensive | $504.0M      | $23.56  | 23.58%       | 50.40%       | 2.14x         |
|  7 | FI       | 2025-10-29 | Before market open | Technology         | $68.6B       | $126.54 | 23.23%       | 49.21%       | 2.12x         |
|  8 | SLGN     | 2025-10-29 | Before market open | Consumer Cyclical  | $4.8B        | $44.74  | 17.74%       | 37.28%       | 2.10x         |
|  9 | FCPT     | 2025-10-28 | After market close | Real Estate        | $2.5B        | $24.34  | 12.48%       | 26.15%       | 2.10x         |
| 10 | CAKE     | 2025-10-28 | After market close | Consumer Cyclical  | $2.7B        | $55.91  | 23.15%       | 47.26%       | 2.04x         |
| 11 | REG      | 2025-10-28 | After market close | Real Estate        | $13.1B       | $73.18  | 11.74%       | 23.93%       | 2.04x         |
| 12 | BLKB     | 2025-10-29 | Before market open | Technology         | $3.1B        | $64.46  | 20.67%       | 41.82%       | 2.02x         |
| 13 | MSA      | 2025-10-28 | After market close | Industrials        | $6.4B        | $166.78 | 14.94%       | 29.83%       | 2.00x         |
| 14 | TEL      | 2025-10-29 | Before market open | Technology         | $69.9B       | $236.74 | 18.38%       | 36.33%       | 1.98x         |
| 15 | VLTO     | 2025-10-28 | After market close | Industrials        | $25.4B       | $104.12 | 11.73%       | 23.18%       | 1.98x         |
| 16 | ADP      | 2025-10-29 | Before market open | Technology         | $113.3B      | $280.53 | 11.58%       | 22.87%       | 1.97x         |
| 17 | NBIX     | 2025-10-28 | After market close | Healthcare         | $14.6B       | $148.94 | 22.93%       | 45.06%       | 1.97x         |
| 18 | DAN      | 2025-10-29 | Before market open | Consumer Cyclical  | $2.6B        | $19.79  | 25.78%       | 50.14%       | 1.94x         |
| 19 | GRMN     | 2025-10-29 | Before market open | Technology         | $48.4B       | $251.42 | 20.32%       | 39.31%       | 1.93x         |
| 20 | CSGP     | 2025-10-28 | After market close | Real Estate        | $33.1B       | $78.12  | 22.57%       | 42.34%       | 1.88x         |
| 21 | EXLS     | 2025-10-28 | After market close | Technology         | $6.7B        | $41.47  | 17.44%       | 32.44%       | 1.86x         |
| 22 | OTIS     | 2025-10-29 | Before market open | Industrials        | $35.8B       | $92.05  | 14.68%       | 27.21%       | 1.85x         |
| 23 | IEX      | 2025-10-29 | Before market open | Industrials        | $12.6B       | $167.60 | 18.40%       | 34.02%       | 1.85x         |
| 24 | ENPH     | 2025-10-28 | After market close | Technology         | $4.8B        | $36.81  | 48.26%       | 87.50%       | 1.81x         |
| 25 | AKR      | 2025-10-28 | After market close | Real Estate        | $2.8B        | $19.84  | 14.99%       | 27.03%       | 1.80x         |
| 26 | MTH      | 2025-10-28 | After market close | Consumer Cyclical  | $5.1B        | $71.41  | 26.02%       | 46.83%       | 1.80x         |
| 27 | OKE      | 2025-10-28 | After market close | Energy             | $43.5B       | $69.29  | 19.01%       | 34.18%       | 1.80x         |
| 28 | EXTR     | 2025-10-29 | Before market open | Technology         | $2.8B        | $20.74  | 34.71%       | 61.35%       | 1.77x         |
| 29 | VIRT     | 2025-10-29 | Before market open | Financial Services | $7.4B        | $33.86  | 22.36%       | 39.09%       | 1.75x         |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
