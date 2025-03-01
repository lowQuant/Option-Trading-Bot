# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-02-28 20:45:59 EST

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector             | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | FTRE     | 2025-03-03 | Before market open | Healthcare         | $1.2B        | $14.05  | 45.57%       | 96.32%       | 2.11x         |
|  1 | NABL     | 2025-03-03 | Before market open | Technology         | $1.9B        | $10.09  | 21.50%       | 41.20%       | 1.92x         |
|  2 | RC       | 2025-03-03 | Before market open | Real Estate        | $1.1B        | $6.80   | 25.06%       | 36.77%       | 1.47x         |
|  3 | CRC      | 2025-03-03 | Before market open | Energy             | $4.1B        | $44.68  | 29.62%       | 41.39%       | 1.40x         |
|  4 | HUT      | 2025-03-03 | Before market open | Financial Services | $1.4B        | $14.41  | nan%         | nan%         | nanx          |
|  5 | MSEX     | 2025-02-28 | After market close | Utilities          | $895.1M      | $51.05  | 29.20%       | nan%         | nanx          |
|  6 | NOVA     | 2025-03-03 | Before market open | Technology         | $207.4M      | $1.72   | nan%         | nan%         | nanx          |
|  7 | SGRY     | 2025-03-03 | Before market open | Healthcare         | $3.1B        | $24.62  | nan%         | nan%         | nanx          |
|  8 | STXS     | 2025-03-03 | Before market open | Healthcare         | $174.5M      | $2.17   | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
