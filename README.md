# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-04-19 21:53:34 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | BOH      | 2025-04-21 | Before market open | Financial Services     | $2.6B        | $64.23  | 38.36%       | 43.15%       | 1.12x         |
|  1 | NFLX     | 2025-04-17 | After market close | Communication Services | $416.2B      | $961.63 | 48.28%       | 50.65%       | 1.05x         |
|  2 | CMA      | 2025-04-21 | Before market open | Financial Services     | $6.9B        | $52.54  | 51.16%       | 49.15%       | 0.96x         |
|  3 | INDB     | 2025-04-17 | After market close | Financial Services     | $2.4B        | $55.36  | 47.31%       | 34.15%       | 0.72x         |
|  4 | CCBG     | 2025-04-21 | Before market open | Financial Services     | $585.0M      | $33.90  | nan%         | nan%         | nanx          |
|  5 | DX       | 2025-04-21 | Before market open | Real Estate            | $1.1B        | $11.59  | nan%         | nan%         | nanx          |
|  6 | GNTY     | 2025-04-21 | Before market open | Financial Services     | $444.2M      | $39.09  | nan%         | nan%         | nanx          |
|  7 | HBT      | 2025-04-21 | Before market open | Financial Services     | $695.6M      | $21.98  | nan%         | nan%         | nanx          |
|  8 | WASH     | 2025-04-21 | Before market open | Financial Services     | $524.5M      | $27.13  | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
