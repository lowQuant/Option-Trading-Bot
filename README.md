# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-06-03 21:55:41 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | CXM      | 2025-06-04 | Before market open | Technology             | $2.2B        | $8.21   | 31.69%       | 61.54%       | 1.94x         |
|  1 | GWRE     | 2025-06-03 | After market close | Technology             | $18.3B       | $215.23 | 24.75%       | 47.98%       | 1.94x         |
|  2 | HPE      | 2025-06-03 | After market close | Technology             | $23.2B       | $17.35  | 29.59%       | 52.83%       | 1.79x         |
|  3 | DLTR     | 2025-06-04 | Before market open | Consumer Defensive     | $20.3B       | $91.24  | 29.85%       | 53.07%       | 1.78x         |
|  4 | THO      | 2025-06-04 | Before market open | Consumer Cyclical      | $4.4B        | $79.23  | 32.67%       | 58.04%       | 1.78x         |
|  5 | HQY      | 2025-06-03 | After market close | Healthcare             | $9.0B        | $102.81 | 36.12%       | 50.56%       | 1.40x         |
|  6 | CRWD     | 2025-06-03 | After market close | Technology             | $121.7B      | $479.17 | 41.65%       | 47.51%       | 1.14x         |
|  7 | ASAN     | 2025-06-03 | After market close | Technology             | $4.5B        | $18.39  | nan%         | nan%         | nanx          |
|  8 | BASE     | 2025-06-03 | After market close | Technology             | $1.0B        | $18.35  | nan%         | nan%         | nanx          |
|  9 | GCO      | 2025-06-04 | Before market open | Consumer Cyclical      | $240.9M      | $21.29  | nan%         | nan%         | nanx          |
| 10 | JFIN     | 2025-06-04 | Before market open | Communication Services | $788.8M      | $14.78  | nan%         | nan%         | nanx          |
| 11 | MAMA     | 2025-06-03 | After market close | Consumer Defensive     | $319.6M      | $8.50   | nan%         | nan%         | nanx          |
| 12 | REVG     | 2025-06-04 | Before market open | Industrials            | $1.9B        | $36.55  | nan%         | nan%         | nanx          |
| 13 | SPWH     | 2025-06-03 | After market close | Consumer Cyclical      | $88.8M       | $2.05   | nan%         | nan%         | nanx          |
| 14 | VBNK     | 2025-06-04 | Before market open | Financial Services     | $375.9M      | $11.27  | nan%         | nan%         | nanx          |
| 15 | YEXT     | 2025-06-03 | After market close | Technology             | $849.7M      | $6.68   | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
