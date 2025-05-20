# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-05-19 21:54:04 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | AGYS     | 2025-05-19 | After market close | Technology             | $2.3B        | $86.00  | 45.22%       | 65.41%       | 1.45x         |
|  1 | HD       | 2025-05-20 | Before market open | Consumer Cyclical      | $377.1B      | $380.78 | 29.24%       | 25.20%       | 0.86x         |
|  2 | EXP      | 2025-05-20 | Before market open | Basic Materials        | $8.1B        | $239.93 | 45.43%       | 35.58%       | 0.78x         |
|  3 | ARBE     | 2025-05-20 | Before market open | Technology             | $171.4M      | $1.77   | nan%         | nan%         | nanx          |
|  4 | AS       | 2025-05-20 | Before market open | Consumer Cyclical      | $17.4B       | $31.14  | nan%         | nan%         | nanx          |
|  5 | BILI     | 2025-05-20 | Before market open | Communication Services | $7.3B        | $18.93  | nan%         | nan%         | nanx          |
|  6 | BWLP     | 2025-05-20 | Before market open | Industrials            | $1.7B        | $11.72  | nan%         | nan%         | nanx          |
|  7 | CAN      | 2025-05-20 | Before market open | Technology             | $344.6M      | $0.79   | nan%         | nan%         | nanx          |
|  8 | CRGO     | 2025-05-20 | Before market open | Industrials            | $111.6M      | $2.27   | nan%         | nan%         | nanx          |
|  9 | DOYU     | 2025-05-20 | Before market open | Communication Services | $209.4M      | $6.93   | nan%         | nan%         | nanx          |
| 10 | EGHT     | 2025-05-19 | After market close | Technology             | $237.0M      | $1.81   | nan%         | nan%         | nanx          |
| 11 | ELTK     | 2025-05-20 | Before market open | Technology             | $66.7M       | $10.60  | nan%         | nan%         | nanx          |
| 12 | ESLT     | 2025-05-20 | Before market open | Industrials            | $18.1B       | $395.15 | nan%         | nan%         | nanx          |
| 13 | FSCO     | 2025-05-19 | After market close | Financial Services     | $1.4B        | $7.16   | nan%         | nan%         | nanx          |
| 14 | GDS      | 2025-05-20 | Before market open | Technology             | $5.2B        | $27.23  | nan%         | nan%         | nanx          |
| 15 | HOV      | 2025-05-20 | Before market open | Consumer Cyclical      | $646.1M      | $111.51 | nan%         | nan%         | nanx          |
| 16 | HTHT     | 2025-05-20 | Before market open | Consumer Cyclical      | $11.4B       | $37.58  | nan%         | nan%         | nanx          |
| 17 | IHS      | 2025-05-20 | Before market open | Communication Services | $2.1B        | $6.28   | nan%         | nan%         | nanx          |
| 18 | PONY     | 2025-05-20 | Before market open | Technology             | $6.0B        | $18.43  | nan%         | nan%         | nanx          |
| 19 | PRPH     | 2025-05-20 | Before market open | Healthcare             | $13.4M       | $0.39   | nan%         | nan%         | nanx          |
| 20 | QFIN     | 2025-05-19 | After market close | Financial Services     | $6.2B        | $44.27  | nan%         | nan%         | nanx          |
| 21 | RERE     | 2025-05-20 | Before market open | Consumer Cyclical      | $630.6M      | $2.81   | nan%         | nan%         | nanx          |
| 22 | SB       | 2025-05-19 | After market close | Industrials            | $390.6M      | $3.75   | nan%         | nan%         | nanx          |
| 23 | TATT     | 2025-05-19 | After market close | Industrials            | $380.9M      | $34.64  | nan%         | nan%         | nanx          |
| 24 | TCOM     | 2025-05-19 | After market close | Consumer Cyclical      | $43.9B       | $64.97  | nan%         | nan%         | nanx          |
| 25 | TRNS     | 2025-05-19 | After market close | Industrials            | $755.7M      | $81.25  | nan%         | nan%         | nanx          |
| 26 | VIK      | 2025-05-20 | Before market open | Consumer Cyclical      | $20.9B       | $48.23  | nan%         | nan%         | nanx          |
| 27 | VIPS     | 2025-05-20 | Before market open | Consumer Cyclical      | $8.0B        | $15.33  | nan%         | nan%         | nanx          |
| 28 | XYF      | 2025-05-20 | Before market open | Financial Services     | $633.1M      | $15.00  | nan%         | nan%         | nanx          |
| 29 | YALA     | 2025-05-19 | After market close | Technology             | $1.2B        | $7.85   | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
