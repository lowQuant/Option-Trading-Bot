# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-03-19 21:42:49 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector             | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | FDS      | 2025-03-20 | Before market open | Financial Services | $16.7B       | $439.82 | 18.17%       | 34.28%       | 1.89x         |
|  1 | CAL      | 2025-03-20 | Before market open | Consumer Cyclical  | $551.2M      | $16.23  | 47.00%       | 87.51%       | 1.86x         |
|  2 | FIVE     | 2025-03-19 | After market close | Consumer Cyclical  | $4.2B        | $73.91  | 42.93%       | 79.36%       | 1.85x         |
|  3 | SCVL     | 2025-03-20 | Before market open | Consumer Cyclical  | $615.5M      | $22.72  | 39.19%       | 63.40%       | 1.62x         |
|  4 | ACN      | 2025-03-20 | Before market open | Technology         | $202.9B      | $324.07 | 24.70%       | 38.75%       | 1.57x         |
|  5 | ASO      | 2025-03-20 | Before market open | Consumer Cyclical  | $3.3B        | $46.39  | 39.20%       | 56.52%       | 1.44x         |
|  6 | JBL      | 2025-03-20 | Before market open | Technology         | $15.3B       | $135.62 | 34.36%       | 46.06%       | 1.34x         |
|  7 | CMC      | 2025-03-20 | Before market open | Basic Materials    | $5.3B        | $46.35  | 38.19%       | 46.75%       | 1.22x         |
|  8 | DRI      | 2025-03-20 | Before market open | Consumer Cyclical  | $22.0B       | $188.07 | 30.18%       | 36.36%       | 1.20x         |
|  9 | ADAP     | 2025-03-20 | Before market open | Healthcare         | $116.5M      | $0.46   | nan%         | nan%         | nanx          |
| 10 | AEVA     | 2025-03-19 | After market close | Technology         | $167.6M      | $2.68   | nan%         | nan%         | nanx          |
| 11 | ALAR     | 2025-03-20 | Before market open | Technology         | $55.8M       | $8.10   | nan%         | nan%         | nanx          |
| 12 | AUTL     | 2025-03-20 | Before market open | Healthcare         | $516.3M      | $1.79   | nan%         | nan%         | nanx          |
| 13 | BRAG     | 2025-03-20 | Before market open | Consumer Cyclical  | $112.1M      | $4.25   | nan%         | nan%         | nanx          |
| 14 | BZUN     | 2025-03-20 | Before market open | Consumer Cyclical  | $192.2M      | $3.48   | nan%         | nan%         | nanx          |
| 15 | CAPR     | 2025-03-19 | After market close | Healthcare         | $555.6M      | $11.61  | nan%         | nan%         | nanx          |
| 16 | CVV      | 2025-03-19 | After market close | Industrials        | $22.0M       | $3.14   | nan%         | nan%         | nanx          |
| 17 | DBI      | 2025-03-20 | Before market open | Consumer Cyclical  | $182.1M      | $3.72   | nan%         | nan%         | nanx          |
| 18 | DXLG     | 2025-03-20 | Before market open | Consumer Cyclical  | $109.7M      | $2.01   | nan%         | nan%         | nanx          |
| 19 | FVR      | 2025-03-19 | After market close | Real Estate        | $233.3M      | $14.38  | nan%         | nan%         | nanx          |
| 20 | GLUE     | 2025-03-20 | Before market open | Healthcare         | $411.6M      | $6.67   | nan%         | nan%         | nanx          |
| 21 | GROY     | 2025-03-19 | After market close | Basic Materials    | $259.1M      | $1.54   | nan%         | nan%         | nanx          |
| 22 | HTHT     | 2025-03-20 | Before market open | Consumer Cyclical  | $11.9B       | $38.48  | nan%         | nan%         | nanx          |
| 23 | ICAD     | 2025-03-19 | After market close | Healthcare         | $65.1M       | $2.32   | nan%         | nan%         | nanx          |
| 24 | IFRX     | 2025-03-20 | Before market open | Healthcare         | $85.9M       | $1.21   | nan%         | nan%         | nanx          |
| 25 | IPM      | 2025-03-19 | After market close | Technology         | $25.4M       | $1.85   | nan%         | nan%         | nanx          |
| 26 | KNOP     | 2025-03-20 | Before market open | Energy             | $196.7M      | $5.56   | nan%         | nan%         | nanx          |
| 27 | LE       | 2025-03-20 | Before market open | Consumer Cyclical  | $353.8M      | $11.13  | nan%         | nan%         | nanx          |
| 28 | LENZ     | 2025-03-19 | After market close | Healthcare         | $701.8M      | $24.40  | nan%         | nan%         | nanx          |
| 29 | LFT      | 2025-03-19 | After market close | Real Estate        | $145.9M      | $2.75   | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
