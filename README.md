# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-08-14 21:59:09 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | FLO      | 2025-08-15 | Before market open | Consumer Defensive     | $3.5B        | $16.76  | 25.08%       | 36.74%       | 1.46x         |
|  1 | AMAT     | 2025-08-14 | After market close | Technology             | $151.1B      | $190.00 | 28.30%       | 38.85%       | 1.37x         |
|  2 | SNDK     | 2025-08-14 | After market close | Technology             | $6.8B        | $47.01  | 52.01%       | 58.54%       | 1.13x         |
|  3 | ACOG     | 2025-08-14 | After market close | Healthcare             | $128.2M      | $9.99   | nan%         | nan%         | nanx          |
|  4 | ARAI     | 2025-08-14 | After market close | Technology             | $211.3M      | $6.77   | nan%         | nan%         | nanx          |
|  5 | AUID     | 2025-08-14 | After market close | Technology             | $52.7M       | $4.06   | nan%         | nan%         | nanx          |
|  6 | BAP      | 2025-08-14 | After market close | Financial Services     | $19.9B       | $249.37 | nan%         | nan%         | nanx          |
|  7 | BLNE     | 2025-08-14 | After market close | Consumer Defensive     | $28.0M       | $2.01   | nan%         | nan%         | nanx          |
|  8 | BNGO     | 2025-08-14 | After market close | Healthcare             | $10.8M       | $3.24   | nan%         | nan%         | nanx          |
|  9 | BNZI     | 2025-08-14 | After market close | Technology             | $12.0M       | $3.90   | nan%         | nan%         | nanx          |
| 10 | BZAI     | 2025-08-14 | After market close | Technology             | $387.3M      | $3.74   | nan%         | nan%         | nanx          |
| 11 | CBUS     | 2025-08-14 | After market close | Healthcare             | $73.6M       | $1.42   | nan%         | nan%         | nanx          |
| 12 | CELC     | 2025-08-14 | After market close | Healthcare             | $2.1B        | $52.37  | nan%         | nan%         | nanx          |
| 13 | CLIR     | 2025-08-14 | After market close | Industrials            | $32.1M       | $0.59   | nan%         | nan%         | nanx          |
| 14 | CNVS     | 2025-08-14 | After market close | Communication Services | $100.8M      | $5.98   | nan%         | nan%         | nanx          |
| 15 | CODX     | 2025-08-14 | After market close | Healthcare             | $8.9M        | $0.26   | nan%         | nan%         | nanx          |
| 16 | CSAN     | 2025-08-14 | After market close | Energy                 | $1.9B        | $4.28   | nan%         | nan%         | nanx          |
| 17 | CV       | 2025-08-14 | After market close | Healthcare             | $186.8M      | $4.07   | nan%         | nan%         | nanx          |
| 18 | DARE     | 2025-08-14 | After market close | Healthcare             | $18.3M       | $2.11   | nan%         | nan%         | nanx          |
| 19 | DFLI     | 2025-08-14 | After market close | Industrials            | $16.4M       | $0.27   | nan%         | nan%         | nanx          |
| 20 | DMRC     | 2025-08-14 | After market close | Technology             | $237.7M      | $11.62  | nan%         | nan%         | nanx          |
| 21 | DUOT     | 2025-08-14 | After market close | Technology             | $120.2M      | $6.14   | nan%         | nan%         | nanx          |
| 22 | ELUT     | 2025-08-14 | After market close | Healthcare             | $88.4M       | $2.16   | nan%         | nan%         | nanx          |
| 23 | EVLV     | 2025-08-14 | After market close | Industrials            | $1.2B        | $7.49   | nan%         | nan%         | nanx          |
| 24 | FTLF     | 2025-08-14 | After market close | Consumer Defensive     | $151.7M      | $16.22  | nan%         | nan%         | nanx          |
| 25 | FUFU     | 2025-08-15 | Before market open | Financial Services     | $650.9M      | $3.91   | nan%         | nan%         | nanx          |
| 26 | GAMB     | 2025-08-14 | After market close | Consumer Cyclical      | $369.6M      | $10.81  | nan%         | nan%         | nanx          |
| 27 | GLOB     | 2025-08-14 | After market close | Technology             | $3.4B        | $79.67  | nan%         | nan%         | nanx          |
| 28 | GNSS     | 2025-08-14 | After market close | Technology             | $74.1M       | $1.62   | nan%         | nan%         | nanx          |
| 29 | ICCC     | 2025-08-15 | Before market open | Healthcare             | $60.7M       | $6.53   | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
