# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-11-09 20:56:56 EST

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | NVRI     | 2025-11-10 | Before market open | Industrials            | $983.1M      | $12.23  | 39.57%       | 95.17%       | 2.41x         |
|  1 | TSN      | 2025-11-10 | Before market open | Consumer Defensive     | $18.7B       | $51.69  | 19.36%       | 39.78%       | 2.05x         |
|  2 | RDNT     | 2025-11-10 | Before market open | Healthcare             | $6.0B        | $78.91  | 33.26%       | 67.41%       | 2.03x         |
|  3 | ROIV     | 2025-11-10 | Before market open | Healthcare             | $14.1B       | $20.57  | 24.44%       | 49.51%       | 2.03x         |
|  4 | CART     | 2025-11-10 | Before market open | Consumer Cyclical      | $9.7B        | $34.98  | 47.14%       | 67.97%       | 1.44x         |
|  5 | THS      | 2025-11-10 | Before market open | Consumer Defensive     | $962.0M      | $18.64  | 62.46%       | 86.43%       | 1.38x         |
|  6 | STWD     | 2025-11-10 | Before market open | Real Estate            | $6.9B        | $18.27  | 16.71%       | 22.49%       | 1.35x         |
|  7 | CEVA     | 2025-11-10 | Before market open | Technology             | $624.8M      | $26.74  | 66.89%       | 84.41%       | 1.26x         |
|  8 | OGN      | 2025-11-10 | Before market open | Healthcare             | $1.8B        | $6.71   | 84.17%       | 89.68%       | 1.07x         |
|  9 | ACDC     | 2025-11-10 | Before market open | Energy                 | $909.8M      | $5.11   | nan%         | nan%         | nanx          |
| 10 | ADCT     | 2025-11-10 | Before market open | Healthcare             | $454.5M      | $4.16   | nan%         | nan%         | nanx          |
| 11 | AGEN     | 2025-11-10 | Before market open | Healthcare             | $126.8M      | $3.84   | nan%         | nan%         | nanx          |
| 12 | AIOT     | 2025-11-10 | Before market open | Technology             | $652.5M      | $4.78   | nan%         | nan%         | nanx          |
| 13 | AKBA     | 2025-11-10 | Before market open | Healthcare             | $540.9M      | $2.01   | nan%         | nan%         | nanx          |
| 14 | ANTA     | 2025-11-10 | Before market open | Financial Services     | $255.8M      | $11.17  | nan%         | nan%         | nanx          |
| 15 | AVD      | 2025-11-10 | Before market open | Basic Materials        | $145.0M      | $4.95   | nan%         | nan%         | nanx          |
| 16 | B        | 2025-11-10 | Before market open | Basic Materials        | $56.5B       | $32.55  | nan%         | nan%         | nanx          |
| 17 | BARK     | 2025-11-10 | Before market open | Consumer Cyclical      | $134.2M      | $0.79   | nan%         | nan%         | nanx          |
| 18 | BBGI     | 2025-11-10 | Before market open | Communication Services | $9.8M        | $4.85   | nan%         | nan%         | nanx          |
| 19 | BEKE     | 2025-11-10 | Before market open | Real Estate            | $18.4B       | $15.80  | nan%         | nan%         | nanx          |
| 20 | BKKT     | 2025-11-10 | Before market open | Technology             | $377.0M      | $21.31  | nan%         | nan%         | nanx          |
| 21 | BKV      | 2025-11-10 | Before market open | Energy                 | $2.3B        | $24.76  | nan%         | nan%         | nanx          |
| 22 | BTDR     | 2025-11-10 | Before market open | Technology             | $4.7B        | $21.22  | nan%         | nan%         | nanx          |
| 23 | BXSL     | 2025-11-10 | Before market open | Financial Services     | $6.1B        | $25.96  | nan%         | nan%         | nanx          |
| 24 | CAMT     | 2025-11-10 | Before market open | Technology             | $5.4B        | $120.25 | nan%         | nan%         | nanx          |
| 25 | CBAT     | 2025-11-10 | Before market open | Industrials            | $78.0M       | $0.90   | nan%         | nan%         | nanx          |
| 26 | CGEN     | 2025-11-10 | Before market open | Healthcare             | $151.5M      | $1.64   | nan%         | nan%         | nanx          |
| 27 | CMCL     | 2025-11-10 | Before market open | Basic Materials        | $527.6M      | $26.50  | nan%         | nan%         | nanx          |
| 28 | CNTY     | 2025-11-10 | Before market open | Consumer Cyclical      | $51.6M       | $1.73   | nan%         | nan%         | nanx          |
| 29 | DOLE     | 2025-11-10 | Before market open | Consumer Defensive     | $1.3B        | $13.05  | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
