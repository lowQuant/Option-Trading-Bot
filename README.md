# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-04-14 21:49:19 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector             | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | PNC      | 2025-04-15 | Before market open | Financial Services | $61.5B       | $151.99 | 45.36%       | 48.16%       | 1.06x         |
|  1 | FBK      | 2025-04-14 | After market close | Financial Services | $1.9B        | $40.56  | 50.64%       | 52.18%       | 1.03x         |
|  2 | ACI      | 2025-04-15 | Before market open | Consumer Defensive | $12.5B       | $21.19  | 35.82%       | 35.16%       | 0.98x         |
|  3 | BAC      | 2025-04-15 | Before market open | Financial Services | $278.8B      | $35.95  | 53.98%       | 47.39%       | 0.88x         |
|  4 | JNJ      | 2025-04-15 | Before market open | Healthcare         | $372.0B      | $151.73 | 31.23%       | 27.05%       | 0.87x         |
|  5 | C        | 2025-04-15 | Before market open | Financial Services | $119.0B      | $61.64  | 60.97%       | 52.15%       | 0.86x         |
|  6 | PNFP     | 2025-04-14 | After market close | Financial Services | $7.1B        | $90.04  | 65.89%       | 55.08%       | 0.84x         |
|  7 | APLD     | 2025-04-14 | After market close | Technology         | $1.2B        | $5.29   | nan%         | nan%         | nanx          |
|  8 | ERIC     | 2025-04-15 | Before market open | Technology         | $24.5B       | $7.29   | nan%         | nan%         | nanx          |
|  9 | HIT      | 2025-04-14 | After market close | Technology         | $37.5M       | $0.70   | nan%         | nan%         | nanx          |
| 10 | JCTC     | 2025-04-14 | After market close | Basic Materials    | $13.9M       | $3.57   | nan%         | nan%         | nanx          |
| 11 | KMTS     | 2025-04-14 | After market close | Healthcare         | $1.2B        | $24.28  | nan%         | nan%         | nanx          |
| 12 | RENT     | 2025-04-15 | Before market open | Consumer Cyclical  | $20.9M       | $5.26   | nan%         | nan%         | nanx          |
| 13 | SKIL     | 2025-04-14 | After market close | Consumer Defensive | $144.5M      | $17.09  | nan%         | nan%         | nanx          |
| 14 | ZBAO     | 2025-04-14 | After market close | Financial Services | $36.2M       | $1.02   | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
