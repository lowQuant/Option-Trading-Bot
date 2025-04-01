# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-03-31 21:56:34 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector             | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | PRGS     | 2025-03-31 | After market close | Technology         | $2.2B        | $51.39  | 26.82%       | 48.53%       | 1.81x         |
|  1 | PVH      | 2025-03-31 | After market close | Consumer Cyclical  | $3.6B        | $64.69  | 38.42%       | 64.31%       | 1.67x         |
|  2 | TTGT     | 2025-03-31 | After market close | Technology         | $1.1B        | $14.30  | 59.81%       | 62.23%       | 1.04x         |
|  3 | ACOG     | 2025-03-31 | After market close | Healthcare         | $87.7M       | $5.38   | nan%         | nan%         | nanx          |
|  4 | AQMS     | 2025-03-31 | After market close | Industrials        | $14.5M       | $2.04   | nan%         | nan%         | nanx          |
|  5 | BHST     | 2025-03-31 | After market close | Consumer Defensive | $113.6M      | $6.55   | nan%         | nan%         | nanx          |
|  6 | BNGO     | 2025-03-31 | After market close | Healthcare         | $7.9M        | $2.90   | nan%         | nan%         | nanx          |
|  7 | BW       | 2025-03-31 | After market close | Industrials        | $66.9M       | $0.71   | nan%         | nan%         | nanx          |
|  8 | CELC     | 2025-03-31 | After market close | Healthcare         | $379.1M      | $10.24  | nan%         | nan%         | nanx          |
|  9 | CTSO     | 2025-03-31 | After market close | Healthcare         | $62.3M       | $1.00   | nan%         | nan%         | nanx          |
| 10 | CWD      | 2025-03-31 | After market close | Financial Services | $13.4M       | $0.60   | nan%         | nan%         | nanx          |
| 11 | CXAI     | 2025-03-31 | After market close | Technology         | $16.8M       | $0.82   | nan%         | nan%         | nanx          |
| 12 | DARE     | 2025-03-31 | After market close | Healthcare         | $25.1M       | $2.88   | nan%         | nan%         | nanx          |
| 13 | DGXX     | 2025-03-31 | After market close | Utilities          | $40.5M       | $1.07   | nan%         | nan%         | nanx          |
| 14 | DUOT     | 2025-03-31 | After market close | Technology         | $52.2M       | $5.31   | nan%         | nan%         | nanx          |
| 15 | FORA     | 2025-03-31 | After market close | Healthcare         | $62.0M       | $2.00   | nan%         | nan%         | nanx          |
| 16 | GRRR     | 2025-03-31 | After market close | Technology         | $546.6M      | $25.04  | nan%         | nan%         | nanx          |
| 17 | GRYP     | 2025-03-31 | After market close | Financial Services | $11.7M       | $0.16   | nan%         | nan%         | nanx          |
| 18 | GWH      | 2025-03-31 | After market close | Industrials        | $39.8M       | $3.35   | nan%         | nan%         | nanx          |
| 19 | IAUX     | 2025-03-31 | After market close | Basic Materials    | $270.5M      | $0.61   | nan%         | nan%         | nanx          |
| 20 | MDBH     | 2025-03-31 | After market close | Financial Services | $62.8M       | $6.25   | nan%         | nan%         | nanx          |
| 21 | MVST     | 2025-03-31 | After market close | Consumer Cyclical  | $379.0M      | $1.15   | nan%         | nan%         | nanx          |
| 22 | NSYS     | 2025-03-31 | After market close | Healthcare         | $27.8M       | $9.77   | nan%         | nan%         | nanx          |
| 23 | NVVE     | 2025-03-31 | After market close | Consumer Cyclical  | $2.1M        | $1.62   | nan%         | nan%         | nanx          |
| 24 | OMER     | 2025-03-31 | After market close | Healthcare         | $490.8M      | $8.47   | nan%         | nan%         | nanx          |
| 25 | RANI     | 2025-03-31 | After market close | Healthcare         | $79.3M       | $1.36   | nan%         | nan%         | nanx          |
| 26 | SIDU     | 2025-03-31 | After market close | Industrials        | $21.6M       | $1.50   | nan%         | nan%         | nanx          |
| 27 | SPIR     | 2025-03-31 | After market close | Industrials        | $250.4M      | $8.19   | nan%         | nan%         | nanx          |
| 28 | SPRU     | 2025-03-31 | After market close | Technology         | $45.9M       | $2.47   | nan%         | nan%         | nanx          |
| 29 | TLPH     | 2025-03-31 | After market close | Healthcare         | $9.6M        | $0.59   | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
