# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-04-02 21:45:08 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector             | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | LNN      | 2025-04-03 | Before market open | Industrials        | $1.4B        | $127.59 | 22.42%       | 40.43%       | 1.80x         |
|  1 | LW       | 2025-04-03 | Before market open | Consumer Defensive | $7.7B        | $53.31  | 38.14%       | 60.80%       | 1.59x         |
|  2 | PENG     | 2025-04-02 | After market close | Technology         | $961.9M      | $17.27  | 52.42%       | 79.33%       | 1.51x         |
|  3 | RH       | 2025-04-02 | After market close | Consumer Cyclical  | $4.6B        | $239.06 | 69.39%       | 97.91%       | 1.41x         |
|  4 | AYI      | 2025-04-03 | Before market open | Industrials        | $8.2B        | $263.67 | 32.82%       | 41.41%       | 1.26x         |
|  5 | MSM      | 2025-04-03 | Before market open | Industrials        | $4.4B        | $77.82  | 30.83%       | 38.89%       | 1.26x         |
|  6 | CAG      | 2025-04-03 | Before market open | Consumer Defensive | $12.6B       | $26.60  | 29.91%       | 29.76%       | 0.99x         |
|  7 | BSET     | 2025-04-02 | After market close | Consumer Cyclical  | $137.3M      | $15.16  | nan%         | nan%         | nanx          |
|  8 | FC       | 2025-04-02 | After market close | Consumer Defensive | $368.0M      | $28.00  | nan%         | nan%         | nanx          |
|  9 | RGP      | 2025-04-02 | After market close | Industrials        | $219.4M      | $6.65   | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
