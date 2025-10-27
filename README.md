# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-10-26 21:58:07 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector             | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | RVTY     | 2025-10-27 | Before market open | Healthcare         | $11.5B       | $97.57  | 30.08%       | 60.26%       | 2.00x         |
|  1 | CRI      | 2025-10-27 | Before market open | Consumer Cyclical  | $1.2B        | $31.78  | 52.88%       | 69.45%       | 1.31x         |
|  2 | DEA      | 2025-10-27 | Before market open | Real Estate        | $1.1B        | $22.39  | 21.98%       | 27.74%       | 1.26x         |
|  3 | BOH      | 2025-10-27 | Before market open | Financial Services | $2.5B        | $62.30  | 26.21%       | 31.08%       | 1.19x         |
|  4 | LKFN     | 2025-10-27 | Before market open | Financial Services | $1.6B        | $60.14  | 29.24%       | 32.84%       | 1.12x         |
|  5 | ARLP     | 2025-10-27 | Before market open | Energy             | $3.0B        | $24.05  | nan%         | nan%         | nanx          |
|  6 | BMRC     | 2025-10-27 | Before market open | Financial Services | $394.6M      | $23.49  | nan%         | nan%         | nanx          |
|  7 | DQ       | 2025-10-27 | Before market open | Technology         | $1.7B        | $26.20  | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
