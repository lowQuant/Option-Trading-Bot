# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-11-07 20:45:28 EST

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector             | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | NVRI     | 2025-11-10 | Before market open | Industrials        | $983.1M      | $12.23  | 39.95%       | 86.63%       | 2.17x         |
|  1 | ROIV     | 2025-11-10 | Before market open | Healthcare         | $14.1B       | $20.57  | 24.37%       | 52.44%       | 2.15x         |
|  2 | RDNT     | 2025-11-10 | Before market open | Healthcare         | $6.1B        | $78.91  | 33.23%       | 66.06%       | 1.99x         |
|  3 | TSN      | 2025-11-10 | Before market open | Consumer Defensive | $18.7B       | $51.69  | 18.57%       | 32.63%       | 1.76x         |
|  4 | THS      | 2025-11-10 | Before market open | Consumer Defensive | $962.0M      | $18.64  | 63.48%       | 90.43%       | 1.42x         |
|  5 | STWD     | 2025-11-10 | Before market open | Real Estate        | $6.9B        | $18.27  | 16.35%       | 22.07%       | 1.35x         |
|  6 | CART     | 2025-11-10 | Before market open | Consumer Cyclical  | $9.7B        | $34.98  | 43.18%       | 50.80%       | 1.18x         |
|  7 | CEVA     | 2025-11-10 | Before market open | Technology         | $624.8M      | $26.74  | 66.38%       | 71.21%       | 1.07x         |
|  8 | ACDC     | 2025-11-10 | Before market open | Energy             | $924.3M      | $5.11   | nan%         | nan%         | nanx          |
|  9 | AIOT     | 2025-11-10 | Before market open | Technology         | $652.5M      | $4.78   | nan%         | nan%         | nanx          |
| 10 | AKBA     | 2025-11-10 | Before market open | Healthcare         | $540.9M      | $2.01   | nan%         | nan%         | nanx          |
| 11 | B        | 2025-11-10 | Before market open | Basic Materials    | $56.5B       | $32.55  | nan%         | nan%         | nanx          |
| 12 | BARK     | 2025-11-10 | Before market open | Consumer Cyclical  | $134.8M      | $0.79   | nan%         | nan%         | nanx          |
| 13 | BEKE     | 2025-11-10 | Before market open | Real Estate        | $19.1B       | $15.80  | nan%         | nan%         | nanx          |
| 14 | BKKT     | 2025-11-10 | Before market open | Technology         | $377.0M      | $21.31  | nan%         | nan%         | nanx          |
| 15 | BKV      | 2025-11-10 | Before market open | Energy             | $2.3B        | $24.76  | nan%         | nan%         | nanx          |
| 16 | BTDR     | 2025-11-10 | Before market open | Technology         | $4.5B        | $21.22  | nan%         | nan%         | nanx          |
| 17 | BXSL     | 2025-11-10 | Before market open | Financial Services | $6.1B        | $25.96  | nan%         | nan%         | nanx          |
| 18 | CAMT     | 2025-11-10 | Before market open | Technology         | $5.5B        | $120.25 | nan%         | nan%         | nanx          |
| 19 | CGEN     | 2025-11-10 | Before market open | Healthcare         | $151.5M      | $1.64   | nan%         | nan%         | nanx          |
| 20 | CMCL     | 2025-11-10 | Before market open | Basic Materials    | $527.6M      | $26.50  | nan%         | nan%         | nanx          |
| 21 | DOLE     | 2025-11-10 | Before market open | Consumer Defensive | $1.3B        | $13.05  | nan%         | nan%         | nanx          |
| 22 | ETOR     | 2025-11-10 | Before market open | Financial Services | $2.9B        | $33.47  | nan%         | nan%         | nanx          |
| 23 | EVGO     | 2025-11-10 | Before market open | Consumer Cyclical  | $1.1B        | $3.42   | nan%         | nan%         | nanx          |
| 24 | GBTG     | 2025-11-10 | Before market open | Consumer Cyclical  | $4.2B        | $7.77   | nan%         | nan%         | nanx          |
| 25 | GSL      | 2025-11-10 | Before market open | Industrials        | $1.1B        | $31.80  | nan%         | nan%         | nanx          |
| 26 | HE       | 2025-11-07 | After market close | Utilities          | $2.0B        | $11.59  | nan%         | nan%         | nanx          |
| 27 | HHH      | 2025-11-10 | Before market open | Real Estate        | $4.8B        | $78.25  | nan%         | nan%         | nanx          |
| 28 | IMVT     | 2025-11-10 | Before market open | Healthcare         | $4.1B        | $23.67  | nan%         | nan%         | nanx          |
| 29 | KSPI     | 2025-11-10 | Before market open | Technology         | $14.7B       | $71.78  | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
