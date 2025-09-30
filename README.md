# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-09-29 21:41:55 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | PRGS     | 2025-09-29 | After market close | Technology             | $1.8B        | $42.02  | 30.97%       | 71.46%       | 2.31x         |
|  1 | PAYX     | 2025-09-30 | Before market open | Technology             | $46.2B       | $128.21 | 17.02%       | 34.19%       | 2.01x         |
|  2 | UNFI     | 2025-09-30 | Before market open | Consumer Defensive     | $1.9B        | $31.62  | 35.85%       | 64.53%       | 1.80x         |
|  3 | LW       | 2025-09-30 | Before market open | Consumer Defensive     | $7.8B        | $55.22  | 32.11%       | 52.04%       | 1.62x         |
|  4 | MTN      | 2025-09-29 | After market close | Consumer Cyclical      | $5.5B        | $147.74 | 29.50%       | 42.79%       | 1.45x         |
|  5 | JEF      | 2025-09-29 | After market close | Financial Services     | $13.8B       | $66.71  | 31.78%       | 42.27%       | 1.33x         |
|  6 | FEAM     | 2025-09-29 | After market close | Basic Materials        | $82.4M       | $3.66   | nan%         | nan%         | nanx          |
|  7 | IDT      | 2025-09-29 | After market close | Communication Services | $1.6B        | $62.57  | nan%         | nan%         | nanx          |
|  8 | NVNI     | 2025-09-30 | Before market open | Technology             | $128.2M      | $1.45   | nan%         | nan%         | nanx          |
|  9 | TRAK     | 2025-09-29 | After market close | Technology             | $302.7M      | $16.93  | nan%         | nan%         | nanx          |
| 10 | VRAR     | 2025-09-30 | Before market open | Technology             | $38.1M       | $1.67   | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
