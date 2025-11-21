# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-11-20 20:51:38 EST

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector             | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | ROST     | 2025-11-20 | After market close | Consumer Cyclical  | $52.5B       | $160.45 | 19.69%       | 39.06%       | 1.98x         |
|  1 | INTU     | 2025-11-20 | After market close | Technology         | $177.8B      | $650.62 | 22.12%       | 41.33%       | 1.87x         |
|  2 | UGI      | 2025-11-20 | After market close | Utilities          | $7.6B        | $34.84  | 14.46%       | 26.20%       | 1.81x         |
|  3 | AZTA     | 2025-11-21 | Before market open | Healthcare         | $1.4B        | $30.03  | 37.04%       | 65.31%       | 1.76x         |
|  4 | BJ       | 2025-11-21 | Before market open | Consumer Defensive | $12.0B       | $91.31  | 24.75%       | 42.82%       | 1.73x         |
|  5 | GAP      | 2025-11-20 | After market close | Consumer Cyclical  | $8.6B        | $23.48  | 41.89%       | 71.74%       | 1.71x         |
|  6 | ESE      | 2025-11-20 | After market close | Technology         | $5.4B        | $217.03 | 22.66%       | 37.30%       | 1.65x         |
|  7 | MATW     | 2025-11-20 | After market close | Industrials        | $764.4M      | $24.84  | 32.06%       | 50.60%       | 1.58x         |
|  8 | MOG.A    | 2025-11-21 | Before market open | nan                | N/A          | $nan    | 21.89%       | 28.84%       | 1.32x         |
|  9 | POST     | 2025-11-20 | After market close | Consumer Defensive | $6.0B        | $106.95 | 22.64%       | 27.14%       | 1.20x         |
| 10 | AUNA     | 2025-11-20 | After market close | Healthcare         | $357.5M      | $4.92   | nan%         | nan%         | nanx          |
| 11 | BULL     | 2025-11-20 | After market close | Technology         | $4.1B        | $8.22   | nan%         | nan%         | nanx          |
| 12 | ESTC     | 2025-11-20 | After market close | Technology         | $8.7B        | $88.28  | nan%         | nan%         | nanx          |
| 13 | GEOS     | 2025-11-20 | After market close | Energy             | $221.5M      | $18.91  | nan%         | nan%         | nanx          |
| 14 | MNSO     | 2025-11-21 | Before market open | Consumer Cyclical  | $6.0B        | $20.58  | nan%         | nan%         | nanx          |
| 15 | MOG.B    | 2025-11-21 | Before market open | nan                | N/A          | $nan    | nan%         | nan%         | nanx          |
| 16 | NGVC     | 2025-11-20 | After market close | Consumer Defensive | $696.7M      | $31.36  | nan%         | nan%         | nanx          |
| 17 | VEEV     | 2025-11-20 | After market close | Healthcare         | $44.3B       | $273.00 | nan%         | nan%         | nanx          |
| 18 | XYF      | 2025-11-21 | Before market open | Financial Services | $384.5M      | $9.71   | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
