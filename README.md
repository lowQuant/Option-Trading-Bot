# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-07-14 22:06:14 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector             | market_cap   | close    | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-------------------|:-------------|:---------|:-------------|:-------------|:--------------|
|  0 | FBK      | 2025-07-14 | After market close | Financial Services | $2.7B        | $48.22   | 20.33%       | 36.86%       | 1.81x         |
|  1 | BLK      | 2025-07-15 | Before market open | Financial Services | $172.2B      | $1101.64 | 13.85%       | 22.06%       | 1.59x         |
|  2 | BK       | 2025-07-15 | Before market open | Financial Services | $68.1B       | $93.72   | 16.60%       | 25.33%       | 1.53x         |
|  3 | STT      | 2025-07-15 | Before market open | Financial Services | $31.4B       | $109.56  | 17.75%       | 26.59%       | 1.50x         |
|  4 | C        | 2025-07-15 | Before market open | Financial Services | $163.4B      | $86.73   | 19.57%       | 28.36%       | 1.45x         |
|  5 | WFC      | 2025-07-15 | Before market open | Financial Services | $271.5B      | $82.55   | 19.48%       | 28.15%       | 1.45x         |
|  6 | JPM      | 2025-07-15 | Before market open | Financial Services | $802.3B      | $286.86  | 17.64%       | 24.02%       | 1.36x         |
|  7 | ACI      | 2025-07-15 | Before market open | Consumer Defensive | $12.5B       | $22.15   | 22.91%       | 30.31%       | 1.32x         |
|  8 | SLP      | 2025-07-14 | After market close | Healthcare         | $351.3M      | $16.96   | 102.58%      | 74.32%       | 0.72x         |
|  9 | ANGO     | 2025-07-15 | Before market open | Healthcare         | $391.0M      | $9.32    | nan%         | nan%         | nanx          |
| 10 | EQBK     | 2025-07-14 | After market close | Financial Services | $771.7M      | $42.93   | nan%         | nan%         | nanx          |
| 11 | ERIC     | 2025-07-15 | Before market open | Technology         | $26.9B       | $8.04    | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
