# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-03-12 21:43:27 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | ADBE     | 2025-03-12 | After market close | Technology             | $190.7B      | $433.66 | 21.74%       | 49.35%       | 2.27x         |
|  1 | GIII     | 2025-03-13 | Before market open | Consumer Cyclical      | $1.1B        | $25.92  | 36.34%       | 77.22%       | 2.12x         |
|  2 | AEO      | 2025-03-12 | After market close | Consumer Cyclical      | $2.2B        | $11.49  | 42.28%       | 72.10%       | 1.71x         |
|  3 | DG       | 2025-03-13 | Before market open | Consumer Defensive     | $16.5B       | $78.64  | 38.44%       | 60.43%       | 1.57x         |
|  4 | CCI      | 2025-03-12 | After market close | Real Estate            | $41.4B       | $97.63  | 22.84%       | 32.55%       | 1.43x         |
|  5 | ACTG     | 2025-03-13 | Before market open | Industrials            | $410.9M      | $4.23   | nan%         | nan%         | nanx          |
|  6 | AEYE     | 2025-03-12 | After market close | Technology             | $154.8M      | $12.08  | nan%         | nan%         | nanx          |
|  7 | AFCG     | 2025-03-13 | Before market open | Real Estate            | $186.4M      | $8.36   | nan%         | nan%         | nanx          |
|  8 | AKBA     | 2025-03-13 | Before market open | Healthcare             | $421.1M      | $1.93   | nan%         | nan%         | nanx          |
|  9 | ANIK     | 2025-03-12 | After market close | Healthcare             | $250.6M      | $16.79  | nan%         | nan%         | nanx          |
| 10 | AP       | 2025-03-13 | Before market open | Industrials            | $36.0M       | $1.84   | nan%         | nan%         | nanx          |
| 11 | APYX     | 2025-03-13 | Before market open | Healthcare             | $40.3M       | $1.05   | nan%         | nan%         | nanx          |
| 12 | ARMN     | 2025-03-12 | After market close | Basic Materials        | $693.9M      | $3.98   | nan%         | nan%         | nanx          |
| 13 | AVAH     | 2025-03-13 | Before market open | Healthcare             | $722.7M      | $3.82   | nan%         | nan%         | nanx          |
| 14 | BBW      | 2025-03-13 | Before market open | Consumer Cyclical      | $477.1M      | $36.09  | nan%         | nan%         | nanx          |
| 15 | BGSF     | 2025-03-12 | After market close | Industrials            | $42.8M       | $4.06   | nan%         | nan%         | nanx          |
| 16 | BLDE     | 2025-03-13 | Before market open | Industrials            | $221.6M      | $2.91   | nan%         | nan%         | nanx          |
| 17 | BLDP     | 2025-03-13 | Before market open | Industrials            | $370.1M      | $1.20   | nan%         | nan%         | nanx          |
| 18 | BRLT     | 2025-03-12 | After market close | Consumer Cyclical      | $132.6M      | $1.30   | nan%         | nan%         | nanx          |
| 19 | BRY      | 2025-03-12 | After market close | Energy                 | $280.1M      | $3.53   | nan%         | nan%         | nanx          |
| 20 | BTMD     | 2025-03-12 | After market close | Healthcare             | $216.3M      | $4.13   | nan%         | nan%         | nanx          |
| 21 | CCLD     | 2025-03-13 | Before market open | Healthcare             | $26.0M       | $1.60   | nan%         | nan%         | nanx          |
| 22 | CDLX     | 2025-03-12 | After market close | Communication Services | $100.6M      | $2.02   | nan%         | nan%         | nanx          |
| 23 | CINT     | 2025-03-12 | After market close | Technology             | $887.6M      | $6.50   | nan%         | nan%         | nanx          |
| 24 | CION     | 2025-03-13 | Before market open | Financial Services     | $641.6M      | $12.12  | nan%         | nan%         | nanx          |
| 25 | CLRB     | 2025-03-13 | Before market open | Healthcare             | $14.6M       | $0.31   | nan%         | nan%         | nanx          |
| 26 | CNTY     | 2025-03-13 | Before market open | Consumer Cyclical      | $74.6M       | $2.40   | nan%         | nan%         | nanx          |
| 27 | CPSH     | 2025-03-13 | Before market open | Technology             | $22.1M       | $1.57   | nan%         | nan%         | nanx          |
| 28 | CVGW     | 2025-03-12 | After market close | Consumer Defensive     | $388.5M      | $22.39  | nan%         | nan%         | nanx          |
| 29 | DLTH     | 2025-03-13 | Before market open | Consumer Cyclical      | $99.6M       | $2.96   | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
