# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-04-15 21:48:55 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | ABT      | 2025-04-16 | Before market open | Healthcare             | $218.9B      | $127.37 | 29.02%       | 31.23%       | 1.08x         |
|  1 | ALV      | 2025-04-16 | Before market open | Consumer Cyclical      | $6.4B        | $82.76  | 51.33%       | 53.80%       | 1.05x         |
|  2 | OMC      | 2025-04-15 | After market close | Communication Services | $15.1B       | $76.54  | 42.44%       | 39.05%       | 0.92x         |
|  3 | JBHT     | 2025-04-15 | After market close | Industrials            | $13.5B       | $137.82 | 52.81%       | 48.06%       | 0.91x         |
|  4 | TRV      | 2025-04-16 | Before market open | Financial Services     | $56.6B       | $250.84 | 34.37%       | 31.01%       | 0.90x         |
|  5 | HWC      | 2025-04-15 | After market close | Financial Services     | $4.2B        | $47.63  | 53.07%       | 46.43%       | 0.87x         |
|  6 | PLD      | 2025-04-16 | Before market open | Real Estate            | $91.3B       | $98.30  | 51.87%       | 42.58%       | 0.82x         |
|  7 | CBSH     | 2025-04-16 | Before market open | Financial Services     | $7.9B        | $58.40  | 39.43%       | 31.93%       | 0.81x         |
|  8 | USB      | 2025-04-16 | Before market open | Financial Services     | $60.2B       | $38.20  | 50.47%       | 39.89%       | 0.79x         |
|  9 | CFG      | 2025-04-16 | Before market open | Financial Services     | $15.8B       | $35.59  | 60.76%       | 46.97%       | 0.77x         |
| 10 | FHN      | 2025-04-16 | Before market open | Financial Services     | $9.0B        | $17.26  | 62.85%       | 47.86%       | 0.76x         |
| 11 | FULT     | 2025-04-15 | After market close | Financial Services     | $2.9B        | $15.67  | 51.70%       | 38.82%       | 0.75x         |
| 12 | IBKR     | 2025-04-15 | After market close | Financial Services     | $73.3B       | $172.99 | 81.95%       | 57.60%       | 0.70x         |
| 13 | UAL      | 2025-04-15 | After market close | Industrials            | $22.0B       | $65.69  | 110.01%      | 73.95%       | 0.67x         |
| 14 | ASML     | 2025-04-16 | Before market open | Technology             | $268.6B      | $672.87 | nan%         | nan%         | nanx          |
| 15 | EQBK     | 2025-04-15 | After market close | Financial Services     | $629.6M      | $35.54  | nan%         | nan%         | nanx          |
| 16 | WIT      | 2025-04-16 | Before market open | Technology             | $29.5B       | $2.85   | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
