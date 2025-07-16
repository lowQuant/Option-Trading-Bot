# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-07-15 22:03:03 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | MS       | 2025-07-16 | Before market open | Financial Services     | $227.2B      | $143.97 | 14.69%       | 28.41%       | 1.93x         |
|  1 | PLD      | 2025-07-16 | Before market open | Real Estate            | $100.8B      | $109.35 | 16.97%       | 29.32%       | 1.73x         |
|  2 | BAC      | 2025-07-16 | Before market open | Financial Services     | $347.6B      | $47.07  | 16.78%       | 27.23%       | 1.62x         |
|  3 | FHN      | 2025-07-16 | Before market open | Financial Services     | $10.8B       | $21.97  | 21.35%       | 34.11%       | 1.60x         |
|  4 | JNJ      | 2025-07-16 | Before market open | Healthcare             | $373.3B      | $156.82 | 12.77%       | 19.16%       | 1.50x         |
|  5 | JBHT     | 2025-07-15 | After market close | Industrials            | $14.8B       | $152.20 | 27.34%       | 39.26%       | 1.44x         |
|  6 | CBSH     | 2025-07-16 | Before market open | Financial Services     | $8.4B        | $66.11  | 17.08%       | 24.15%       | 1.41x         |
|  7 | GS       | 2025-07-16 | Before market open | Financial Services     | $215.6B      | $713.30 | 19.99%       | 28.25%       | 1.41x         |
|  8 | MTB      | 2025-07-16 | Before market open | Financial Services     | $31.7B       | $203.05 | 20.66%       | 28.88%       | 1.40x         |
|  9 | PNC      | 2025-07-16 | Before market open | Financial Services     | $76.0B       | $195.69 | 18.30%       | 25.19%       | 1.38x         |
| 10 | HWC      | 2025-07-15 | After market close | Financial Services     | $5.0B        | $60.23  | 26.39%       | 33.77%       | 1.28x         |
| 11 | OMC      | 2025-07-15 | After market close | Communication Services | $13.9B       | $72.65  | 27.75%       | 34.23%       | 1.23x         |
| 12 | FULT     | 2025-07-15 | After market close | Financial Services     | $3.5B        | $19.57  | 23.93%       | 29.47%       | 1.23x         |
| 13 | PNFP     | 2025-07-15 | After market close | Financial Services     | $8.9B        | $119.04 | 23.87%       | 28.34%       | 1.19x         |
| 14 | PGR      | 2025-07-16 | Before market open | Financial Services     | $142.0B      | $247.37 | 24.15%       | 27.71%       | 1.15x         |
| 15 | ASML     | 2025-07-16 | Before market open | Technology             | $323.6B      | $806.73 | nan%         | nan%         | nanx          |
| 16 | KMTS     | 2025-07-15 | After market close | Healthcare             | $836.5M      | $15.43  | nan%         | nan%         | nanx          |
| 17 | RMCF     | 2025-07-15 | After market close | Consumer Defensive     | $14.9M       | $1.80   | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
