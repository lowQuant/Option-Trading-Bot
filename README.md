# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-04-10 21:46:28 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector             | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | BK       | 2025-04-11 | Before market open | Financial Services | $57.0B       | $79.35  | 44.19%       | 47.69%       | 1.08x         |
|  1 | FAST     | 2025-04-11 | Before market open | Industrials        | $43.8B       | $76.47  | 38.07%       | 34.71%       | 0.91x         |
|  2 | JPM      | 2025-04-11 | Before market open | Financial Services | $652.2B      | $234.34 | 48.28%       | 40.63%       | 0.84x         |
|  3 | WFC      | 2025-04-11 | Before market open | Financial Services | $216.6B      | $66.33  | 52.04%       | 43.64%       | 0.84x         |
|  4 | BLK      | 2025-04-11 | Before market open | Financial Services | $139.1B      | $897.08 | 49.09%       | 36.88%       | 0.75x         |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
