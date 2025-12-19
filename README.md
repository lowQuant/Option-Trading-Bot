# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-12-18 20:59:04 EST

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | SCHL     | 2025-12-18 | After market close | Communication Services | $723.2M      | $28.65  | 29.08%       | 60.06%       | 2.07x         |
|  1 | PAYX     | 2025-12-19 | Before market open | Technology             | $41.1B       | $116.70 | 19.52%       | 33.09%       | 1.70x         |
|  2 | CAG      | 2025-12-19 | Before market open | Consumer Defensive     | $8.5B        | $17.92  | 20.62%       | 34.23%       | 1.66x         |
|  3 | LW       | 2025-12-19 | Before market open | Consumer Defensive     | $8.3B        | $59.46  | 26.89%       | 43.16%       | 1.61x         |
|  4 | NKE      | 2025-12-18 | After market close | Consumer Cyclical      | $97.0B       | $65.69  | 30.18%       | 45.00%       | 1.49x         |
|  5 | FDX      | 2025-12-18 | After market close | Industrials            | $67.7B       | $282.21 | 24.97%       | 36.87%       | 1.48x         |
|  6 | WGO      | 2025-12-19 | Before market open | Consumer Cyclical      | $1.1B        | $41.40  | 43.80%       | 62.87%       | 1.44x         |
|  7 | KBH      | 2025-12-18 | After market close | Consumer Cyclical      | $4.1B        | $62.94  | 32.01%       | 37.58%       | 1.17x         |
|  8 | CCL      | 2025-12-19 | Before market open | Consumer Cyclical      | $38.4B       | $28.03  | 41.82%       | 46.52%       | 1.11x         |
|  9 | AVO      | 2025-12-18 | After market close | Consumer Defensive     | $927.2M      | $13.14  | nan%         | nan%         | nanx          |
| 10 | BB       | 2025-12-18 | After market close | Technology             | $2.6B        | $4.26   | nan%         | nan%         | nanx          |
| 11 | CUK      | 2025-12-19 | Before market open | Consumer Cyclical      | $34.6B       | $26.05  | nan%         | nan%         | nanx          |
| 12 | HEI      | 2025-12-18 | After market close | Industrials            | $43.0B       | $306.89 | nan%         | nan%         | nanx          |
| 13 | HEI.A    | 2025-12-18 | After market close | nan                    | N/A          | $nan    | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
