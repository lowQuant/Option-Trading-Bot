# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-10-13 21:44:43 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector             | market_cap   | close    | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-------------------|:-------------|:---------|:-------------|:-------------|:--------------|
|  0 | ACI      | 2025-10-14 | Before market open | Consumer Defensive | $9.5B        | $17.12   | 19.56%       | 37.47%       | 1.92x         |
|  1 | JPM      | 2025-10-14 | Before market open | Financial Services | $846.8B      | $300.89  | 15.50%       | 28.17%       | 1.82x         |
|  2 | FBK      | 2025-10-14 | Before market open | Financial Services | $3.0B        | $55.89   | 16.95%       | 30.57%       | 1.80x         |
|  3 | C        | 2025-10-14 | Before market open | Financial Services | $176.9B      | $93.93   | 18.29%       | 32.96%       | 1.80x         |
|  4 | DPZ      | 2025-10-14 | Before market open | Consumer Cyclical  | $13.9B       | $406.37  | 20.35%       | 34.86%       | 1.71x         |
|  5 | GS       | 2025-10-14 | Before market open | Financial Services | $238.2B      | $764.36  | 18.90%       | 32.14%       | 1.70x         |
|  6 | WFC      | 2025-10-14 | Before market open | Financial Services | $252.8B      | $77.62   | 20.90%       | 32.11%       | 1.54x         |
|  7 | BLK      | 2025-10-14 | Before market open | Financial Services | $178.9B      | $1132.36 | 17.52%       | 26.79%       | 1.53x         |
|  8 | JNJ      | 2025-10-14 | Before market open | Healthcare         | $459.8B      | $190.72  | 14.07%       | 20.87%       | 1.48x         |
|  9 | ERIC     | 2025-10-14 | Before market open | Technology         | $27.3B       | $8.24    | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
