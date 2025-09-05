# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-09-04 21:44:01 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector             | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | GWRE     | 2025-09-04 | After market close | Technology         | $18.5B       | $219.25 | 20.96%       | 49.52%       | 2.36x         |
|  1 | CPRT     | 2025-09-04 | After market close | Industrials        | $48.3B       | $48.12  | 17.82%       | 37.60%       | 2.11x         |
|  2 | ABM      | 2025-09-05 | Before market open | Industrials        | $3.0B        | $48.72  | 21.35%       | 43.34%       | 2.03x         |
|  3 | LULU     | 2025-09-04 | After market close | Consumer Cyclical  | $23.8B       | $198.53 | 34.80%       | 67.28%       | 1.93x         |
|  4 | AVGO     | 2025-09-04 | After market close | Technology         | $1.4tr       | $302.39 | 29.45%       | 46.82%       | 1.59x         |
|  5 | DOCU     | 2025-09-04 | After market close | Technology         | $15.4B       | $75.90  | 40.29%       | 59.20%       | 1.47x         |
|  6 | NX       | 2025-09-04 | After market close | Industrials        | $961.3M      | $20.09  | 46.60%       | 64.09%       | 1.38x         |
|  7 | AGX      | 2025-09-04 | After market close | Industrials        | $3.2B        | $227.03 | nan%         | nan%         | nanx          |
|  8 | AMBQ     | 2025-09-04 | After market close | Technology         | $740.2M      | $38.40  | nan%         | nan%         | nanx          |
|  9 | AOUT     | 2025-09-04 | After market close | Consumer Cyclical  | $132.7M      | $10.24  | nan%         | nan%         | nanx          |
| 10 | BBCP     | 2025-09-04 | After market close | Industrials        | $354.3M      | $6.77   | nan%         | nan%         | nanx          |
| 11 | BRZE     | 2025-09-04 | After market close | Technology         | $2.9B        | $26.99  | nan%         | nan%         | nanx          |
| 12 | CURV     | 2025-09-04 | After market close | Consumer Cyclical  | $235.7M      | $2.36   | nan%         | nan%         | nanx          |
| 13 | EGAN     | 2025-09-04 | After market close | Technology         | $171.2M      | $6.24   | nan%         | nan%         | nanx          |
| 14 | IOT      | 2025-09-04 | After market close | Technology         | $20.2B       | $35.51  | nan%         | nan%         | nanx          |
| 15 | LFVN     | 2025-09-04 | After market close | Consumer Defensive | $170.8M      | $13.57  | nan%         | nan%         | nanx          |
| 16 | PATH     | 2025-09-04 | After market close | Technology         | $5.8B        | $10.88  | nan%         | nan%         | nanx          |
| 17 | PHR      | 2025-09-04 | After market close | Healthcare         | $1.9B        | $30.44  | nan%         | nan%         | nanx          |
| 18 | SPWH     | 2025-09-04 | After market close | Consumer Cyclical  | $115.3M      | $2.64   | nan%         | nan%         | nanx          |
| 19 | SWBI     | 2025-09-04 | After market close | Industrials        | $363.8M      | $8.02   | nan%         | nan%         | nanx          |
| 20 | TTAN     | 2025-09-04 | After market close | Technology         | $9.3B        | $102.82 | nan%         | nan%         | nanx          |
| 21 | ZUMZ     | 2025-09-04 | After market close | Consumer Cyclical  | $327.9M      | $17.54  | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
