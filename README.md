# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-11-11 20:52:47 EST

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector             | market_cap   | close    | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-------------------|:-------------|:---------|:-------------|:-------------|:--------------|
|  0 | TDG      | 2025-11-12 | Before market open | Industrials        | $72.9B       | $1288.91 | 26.75%       | 34.66%       | 1.30x         |
|  1 | ABOS     | 2025-11-12 | Before market open | Healthcare         | $119.3M      | $1.89    | nan%         | nan%         | nanx          |
|  2 | ACXP     | 2025-11-12 | Before market open | Healthcare         | $11.6M       | $5.25    | nan%         | nan%         | nanx          |
|  3 | AFCG     | 2025-11-12 | Before market open | Real Estate        | $73.2M       | $3.13    | nan%         | nan%         | nanx          |
|  4 | AGRO     | 2025-11-11 | After market close | Consumer Defensive | $816.6M      | $8.02    | nan%         | nan%         | nanx          |
|  5 | AII      | 2025-11-11 | After market close | Financial Services | $512.6M      | $25.39   | nan%         | nan%         | nanx          |
|  6 | ALC      | 2025-11-11 | After market close | Healthcare         | $38.2B       | $74.39   | nan%         | nan%         | nanx          |
|  7 | ARCO     | 2025-11-12 | Before market open | Consumer Cyclical  | $1.5B        | $7.13    | nan%         | nan%         | nanx          |
|  8 | AUTL     | 2025-11-12 | Before market open | Healthcare         | $399.2M      | $1.32    | nan%         | nan%         | nanx          |
|  9 | BGSI     | 2025-11-12 | Before market open | Consumer Cyclical  | $4.2B        | $151.30  | nan%         | nan%         | nanx          |
| 10 | BRCB     | 2025-11-11 | After market close | Consumer Cyclical  | $425.6M      | $24.41   | nan%         | nan%         | nanx          |
| 11 | BYND     | 2025-11-11 | After market close | Consumer Defensive | $487.1M      | $1.34    | nan%         | nan%         | nanx          |
| 12 | CAE      | 2025-11-11 | After market close | Industrials        | $8.8B        | $27.22   | nan%         | nan%         | nanx          |
| 13 | CRCL     | 2025-11-12 | Before market open | Financial Services | $24.6B       | $104.10  | nan%         | nan%         | nanx          |
| 14 | CREX     | 2025-11-12 | Before market open | Technology         | $29.3M       | $2.80    | nan%         | nan%         | nanx          |
| 15 | CRMD     | 2025-11-12 | Before market open | Healthcare         | $876.7M      | $11.08   | nan%         | nan%         | nanx          |
| 16 | CRWS     | 2025-11-12 | Before market open | Consumer Cyclical  | $27.8M       | $2.65    | nan%         | nan%         | nanx          |
| 17 | CSTE     | 2025-11-12 | Before market open | Industrials        | $35.6M       | $0.97    | nan%         | nan%         | nanx          |
| 18 | DOX      | 2025-11-11 | After market close | Technology         | $9.2B        | $85.49   | nan%         | nan%         | nanx          |
| 19 | ENLT     | 2025-11-12 | Before market open | Utilities          | $4.8B        | $35.95   | nan%         | nan%         | nanx          |
| 20 | EPM      | 2025-11-11 | After market close | Energy             | $159.3M      | $4.45    | nan%         | nan%         | nanx          |
| 21 | EWCZ     | 2025-11-12 | Before market open | Consumer Defensive | $201.6M      | $3.66    | nan%         | nan%         | nanx          |
| 22 | FLNG     | 2025-11-12 | Before market open | Energy             | $1.4B        | $26.94   | nan%         | nan%         | nanx          |
| 23 | FTCI     | 2025-11-12 | Before market open | Technology         | $110.7M      | $7.38    | nan%         | nan%         | nanx          |
| 24 | FTHM     | 2025-11-11 | After market close | Real Estate        | $46.8M       | $1.29    | nan%         | nan%         | nanx          |
| 25 | FUFU     | 2025-11-12 | Before market open | Financial Services | $531.1M      | $3.27    | nan%         | nan%         | nanx          |
| 26 | GFS      | 2025-11-12 | Before market open | Technology         | $19.3B       | $34.62   | nan%         | nan%         | nanx          |
| 27 | GILT     | 2025-11-12 | Before market open | Technology         | $802.1M      | $12.48   | nan%         | nan%         | nanx          |
| 28 | HBM      | 2025-11-12 | Before market open | Basic Materials    | $6.6B        | $16.86   | nan%         | nan%         | nanx          |
| 29 | HUMA     | 2025-11-12 | Before market open | Healthcare         | $239.7M      | $1.35    | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
