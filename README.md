# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-08-25 21:51:09 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector             | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | SMTC     | 2025-08-25 | After market close | Technology         | $4.4B        | $51.09  | 48.60%       | 79.21%       | 1.63x         |
|  1 | ATAT     | 2025-08-26 | Before market open | Consumer Cyclical  | $4.9B        | $35.73  | nan%         | nan%         | nanx          |
|  2 | BEKE     | 2025-08-26 | Before market open | Real Estate        | $21.9B       | $18.53  | nan%         | nan%         | nanx          |
|  3 | BMO      | 2025-08-26 | Before market open | Financial Services | $82.2B       | $114.73 | nan%         | nan%         | nanx          |
|  4 | BNS      | 2025-08-26 | Before market open | Financial Services | $71.4B       | $57.63  | nan%         | nan%         | nanx          |
|  5 | BWLP     | 2025-08-26 | Before market open | Industrials        | $2.4B        | $16.39  | nan%         | nan%         | nanx          |
|  6 | CDLR     | 2025-08-26 | Before market open | Industrials        | $1.9B        | $22.53  | nan%         | nan%         | nanx          |
|  7 | CTRN     | 2025-08-26 | Before market open | Consumer Cyclical  | $282.2M      | $32.59  | nan%         | nan%         | nanx          |
|  8 | DQ       | 2025-08-26 | Before market open | Technology         | $1.6B        | $22.86  | nan%         | nan%         | nanx          |
|  9 | ECX      | 2025-08-26 | Before market open | Consumer Cyclical  | $626.5M      | $1.67   | nan%         | nan%         | nanx          |
| 10 | EH       | 2025-08-26 | Before market open | Industrials        | $1.3B        | $18.51  | nan%         | nan%         | nanx          |
| 11 | FSCO     | 2025-08-25 | After market close | Financial Services | $1.5B        | $7.46   | nan%         | nan%         | nanx          |
| 12 | GOTU     | 2025-08-26 | Before market open | Consumer Defensive | $936.2M      | $3.69   | nan%         | nan%         | nanx          |
| 13 | HDL      | 2025-08-26 | Before market open | Consumer Cyclical  | $1.2B        | $20.40  | nan%         | nan%         | nanx          |
| 14 | HEI      | 2025-08-25 | After market close | Industrials        | $37.0B       | $309.59 | nan%         | nan%         | nanx          |
| 15 | HEI.A    | 2025-08-25 | After market close | nan                | N/A          | $nan    | nan%         | nan%         | nanx          |
| 16 | PDCC     | 2025-08-26 | Before market open | Financial Services | $109.8M      | $16.29  | nan%         | nan%         | nanx          |
| 17 | SNT      | 2025-08-25 | After market close | Industrials        | $108.2M      | $4.33   | nan%         | nan%         | nanx          |
| 18 | THCH     | 2025-08-26 | Before market open | Consumer Cyclical  | $79.7M       | $2.47   | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
