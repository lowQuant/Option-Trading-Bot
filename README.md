# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-10-24 21:45:07 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector             | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | RVTY     | 2025-10-27 | Before market open | Healthcare         | $11.5B       | $97.57  | 32.05%       | 61.41%       | 1.92x         |
|  1 | DEA      | 2025-10-27 | Before market open | Real Estate        | $1.1B        | $22.39  | 22.16%       | 29.18%       | 1.32x         |
|  2 | LKFN     | 2025-10-27 | Before market open | Financial Services | $1.6B        | $60.14  | 28.63%       | 32.82%       | 1.15x         |
|  3 | BOH      | 2025-10-27 | Before market open | Financial Services | $2.5B        | $62.30  | 25.02%       | 27.48%       | 1.10x         |
|  4 | ARLP     | 2025-10-27 | Before market open | Energy             | $3.1B        | $24.05  | nan%         | nan%         | nanx          |
|  5 | BMRC     | 2025-10-27 | Before market open | Financial Services | $394.6M      | $23.49  | nan%         | nan%         | nanx          |
|  6 | DQ       | 2025-10-27 | Before market open | Technology         | $1.8B        | $26.20  | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
