# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-05-27 21:54:05 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | AMBR     | 2025-05-28 | Before market open | nan                    | $888.2M      | $9.81   | nan%         | nan%         | nanx          |
|  1 | ANF      | 2025-05-28 | Before market open | Consumer Cyclical      | $3.7B        | $73.17  | 46.56%       | nan%         | nanx          |
|  2 | API      | 2025-05-27 | After market close | Technology             | $335.7M      | $3.59   | nan%         | nan%         | nanx          |
|  3 | BMO      | 2025-05-28 | Before market open | Financial Services     | $76.3B       | $103.94 | nan%         | nan%         | nanx          |
|  4 | BOX      | 2025-05-27 | After market close | Technology             | $4.6B        | $31.09  | 16.00%       | nan%         | nanx          |
|  5 | CLGN     | 2025-05-28 | Before market open | Healthcare             | $22.1M       | $1.95   | nan%         | nan%         | nanx          |
|  6 | CMCO     | 2025-05-28 | Before market open | Industrials            | $508.7M      | $16.42  | nan%         | nan%         | nanx          |
|  7 | CPRI     | 2025-05-28 | Before market open | Consumer Cyclical      | $2.1B        | $16.80  | 47.00%       | nan%         | nanx          |
|  8 | DKS      | 2025-05-28 | Before market open | Consumer Cyclical      | $13.4B       | $167.22 | 64.98%       | nan%         | nanx          |
|  9 | ECC      | 2025-05-28 | Before market open | Financial Services     | $920.6M      | $7.50   | nan%         | nan%         | nanx          |
| 10 | EIC      | 2025-05-28 | Before market open | Financial Services     | $375.3M      | $14.41  | nan%         | nan%         | nanx          |
| 11 | HEI      | 2025-05-27 | After market close | Industrials            | $32.5B       | $268.05 | nan%         | nan%         | nanx          |
| 12 | HEI.A    | 2025-05-27 | After market close | nan                    | N/A          | $nan    | nan%         | nan%         | nanx          |
| 13 | ICCM     | 2025-05-28 | Before market open | Healthcare             | $66.2M       | $1.06   | nan%         | nan%         | nanx          |
| 14 | ITRN     | 2025-05-28 | Before market open | Technology             | $780.6M      | $37.26  | nan%         | nan%         | nanx          |
| 15 | KC       | 2025-05-28 | Before market open | Technology             | $3.4B        | $13.06  | nan%         | nan%         | nanx          |
| 16 | M        | 2025-05-28 | Before market open | Consumer Cyclical      | $3.4B        | $11.57  | 35.59%       | nan%         | nanx          |
| 17 | MNRO     | 2025-05-28 | Before market open | Consumer Cyclical      | $382.5M      | $12.66  | 50.56%       | nan%         | nanx          |
| 18 | OCFT     | 2025-05-28 | Before market open | Technology             | $283.9M      | $7.23   | nan%         | nan%         | nanx          |
| 19 | OKTA     | 2025-05-27 | After market close | Technology             | $21.7B       | $123.72 | nan%         | nan%         | nanx          |
| 20 | PHR      | 2025-05-28 | Before market open | Healthcare             | $1.5B        | $24.06  | nan%         | nan%         | nanx          |
| 21 | PLAB     | 2025-05-28 | Before market open | Technology             | $1.3B        | $19.47  | 29.36%       | nan%         | nanx          |
| 22 | REX      | 2025-05-28 | Before market open | Basic Materials        | $708.7M      | $41.58  | 23.75%       | nan%         | nanx          |
| 23 | RSVR     | 2025-05-28 | Before market open | Communication Services | $508.8M      | $7.23   | nan%         | nan%         | nanx          |
| 24 | SMTC     | 2025-05-27 | After market close | Technology             | $3.4B        | $37.28  | 57.83%       | nan%         | nanx          |
| 25 | SNT      | 2025-05-27 | After market close | Industrials            | $87.5M       | $3.74   | nan%         | nan%         | nanx          |
| 26 | SOTK     | 2025-05-28 | Before market open | Technology             | $60.8M       | $3.81   | nan%         | nan%         | nanx          |
| 27 | SQM      | 2025-05-27 | After market close | Basic Materials        | $9.2B        | $32.98  | nan%         | nan%         | nanx          |
| 28 | SUPV     | 2025-05-27 | After market close | Financial Services     | $1.4B        | $15.70  | nan%         | nan%         | nanx          |
| 29 | VNET     | 2025-05-28 | Before market open | Technology             | $1.6B        | $5.99   | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
