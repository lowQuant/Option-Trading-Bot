# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-07-26 22:19:55 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector             | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | RVTY     | 2025-07-28 | Before market open | Healthcare         | $12.2B       | $101.97 | 34.51%       | 44.29%       | 1.28x         |
|  1 | BOH      | 2025-07-28 | Before market open | Financial Services | $2.6B        | $66.00  | 23.46%       | 28.75%       | 1.23x         |
|  2 | ALRS     | 2025-07-28 | Before market open | Financial Services | $550.9M      | $21.64  | nan%         | nan%         | nanx          |
|  3 | ARLP     | 2025-07-28 | Before market open | Energy             | $3.6B        | $27.97  | nan%         | nan%         | nanx          |
|  4 | BFST     | 2025-07-28 | Before market open | Financial Services | $754.7M      | $25.66  | nan%         | nan%         | nanx          |
|  5 | BMRC     | 2025-07-28 | Before market open | Financial Services | $385.6M      | $24.01  | nan%         | nan%         | nanx          |
|  6 | BWFG     | 2025-07-28 | Before market open | Financial Services | $294.4M      | $36.92  | nan%         | nan%         | nanx          |
|  7 | EPD      | 2025-07-28 | Before market open | Energy             | $68.4B       | $31.79  | nan%         | nan%         | nanx          |
|  8 | FMX      | 2025-07-28 | Before market open | Consumer Defensive | $34.9B       | $97.84  | nan%         | nan%         | nanx          |
|  9 | NGD      | 2025-07-28 | Before market open | Basic Materials    | $3.5B        | $4.43   | nan%         | nan%         | nanx          |
| 10 | PROV     | 2025-07-28 | Before market open | Financial Services | $102.6M      | $15.50  | nan%         | nan%         | nanx          |
| 11 | RITM     | 2025-07-28 | Before market open | Real Estate        | $6.5B        | $12.23  | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
