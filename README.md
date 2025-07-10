# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-07-09 21:59:24 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector             | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | AZZ      | 2025-07-09 | After market close | Industrials        | $3.0B        | $98.81  | 23.98%       | 40.94%       | 1.71x         |
|  1 | SMPL     | 2025-07-10 | Before market open | Consumer Defensive | $3.3B        | $31.87  | 23.33%       | 39.24%       | 1.68x         |
|  2 | HELE     | 2025-07-10 | Before market open | Consumer Defensive | $718.3M      | $31.29  | 62.27%       | 94.78%       | 1.52x         |
|  3 | DAL      | 2025-07-10 | Before market open | Industrials        | $33.1B       | $50.52  | 36.35%       | 51.55%       | 1.42x         |
|  4 | CAG      | 2025-07-10 | Before market open | Consumer Defensive | $9.9B        | $20.65  | 22.90%       | 32.33%       | 1.41x         |
|  5 | BSET     | 2025-07-09 | After market close | Consumer Cyclical  | $147.9M      | $16.22  | nan%         | nan%         | nanx          |
|  6 | BYRN     | 2025-07-10 | Before market open | Industrials        | $732.5M      | $32.17  | nan%         | nan%         | nanx          |
|  7 | NTIC     | 2025-07-10 | Before market open | Basic Materials    | $77.0M       | $7.81   | nan%         | nan%         | nanx          |
|  8 | PCYO     | 2025-07-09 | After market close | Utilities          | $258.8M      | $10.75  | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
