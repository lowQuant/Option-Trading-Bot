# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-06-04 21:54:38 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector             | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | BF.B     | 2025-06-05 | Before market open | nan                | N/A          | $nan    | 20.11%       | 36.76%       | 1.83x         |
|  1 | CIEN     | 2025-06-05 | Before market open | Technology         | $11.9B       | $83.21  | 31.51%       | 55.83%       | 1.77x         |
|  2 | GEF      | 2025-06-04 | After market close | Consumer Cyclical  | $2.7B        | $55.72  | 23.35%       | 34.30%       | 1.47x         |
|  3 | TTC      | 2025-06-05 | Before market open | Industrials        | $7.7B        | $76.69  | 26.37%       | 38.58%       | 1.46x         |
|  4 | VSCO     | 2025-06-05 | Before market open | Consumer Cyclical  | $1.6B        | $20.27  | 58.90%       | 72.76%       | 1.24x         |
|  5 | PVH      | 2025-06-04 | After market close | Consumer Cyclical  | $4.0B        | $82.49  | 45.89%       | 56.20%       | 1.22x         |
|  6 | FIVE     | 2025-06-04 | After market close | Consumer Cyclical  | $6.7B        | $122.21 | 72.56%       | 61.61%       | 0.85x         |
|  7 | AGX      | 2025-06-04 | After market close | Industrials        | $3.0B        | $218.76 | nan%         | nan%         | nanx          |
|  8 | ALOT     | 2025-06-05 | Before market open | Technology         | $69.2M       | $9.06   | nan%         | nan%         | nanx          |
|  9 | BARK     | 2025-06-04 | After market close | Consumer Cyclical  | $236.1M      | $1.30   | nan%         | nan%         | nanx          |
| 10 | BF.A     | 2025-06-05 | Before market open | nan                | N/A          | $nan    | nan%         | nan%         | nanx          |
| 11 | CHPT     | 2025-06-04 | After market close | Consumer Cyclical  | $403.2M      | $0.78   | nan%         | nan%         | nanx          |
| 12 | DLTH     | 2025-06-05 | Before market open | Consumer Cyclical  | $75.7M       | $2.07   | nan%         | nan%         | nanx          |
| 13 | DSGX     | 2025-06-04 | After market close | Technology         | $9.9B        | $115.10 | nan%         | nan%         | nanx          |
| 14 | FUFU     | 2025-06-05 | Before market open | Financial Services | $576.7M      | $3.54   | nan%         | nan%         | nanx          |
| 15 | GEF.B    | 2025-06-04 | After market close | nan                | N/A          | $nan    | nan%         | nan%         | nanx          |
| 16 | LE       | 2025-06-05 | Before market open | Consumer Cyclical  | $263.1M      | $8.53   | nan%         | nan%         | nanx          |
| 17 | PL       | 2025-06-04 | After market close | Industrials        | $1.2B        | $3.84   | nan%         | nan%         | nanx          |
| 18 | TLYS     | 2025-06-04 | After market close | Consumer Cyclical  | $39.2M       | $1.33   | nan%         | nan%         | nanx          |
| 19 | VRNT     | 2025-06-04 | After market close | Technology         | $1.1B        | $17.81  | nan%         | nan%         | nanx          |
| 20 | WDH      | 2025-06-05 | Before market open | Financial Services | $531.6M      | $1.49   | nan%         | nan%         | nanx          |
| 21 | YB       | 2025-06-05 | Before market open | Technology         | $685.2M      | $15.20  | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
