# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-03-24 21:45:19 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | CNM      | 2025-03-25 | Before market open | Industrials            | $9.9B        | $48.27  | 27.46%       | 52.20%       | 1.90x         |
|  1 | KBH      | 2025-03-24 | After market close | Consumer Cyclical      | $4.4B        | $59.75  | 30.72%       | 44.14%       | 1.44x         |
|  2 | EPAC     | 2025-03-24 | After market close | Industrials            | $2.4B        | $42.25  | 29.18%       | 32.75%       | 1.12x         |
|  3 | MKC      | 2025-03-25 | Before market open | Consumer Defensive     | $21.5B       | $80.17  | 25.85%       | 26.74%       | 1.03x         |
|  4 | ABVX     | 2025-03-24 | After market close | Healthcare             | $467.1M      | $7.38   | nan%         | nan%         | nanx          |
|  5 | ACCS     | 2025-03-25 | Before market open | Communication Services | $35.5M       | $9.31   | nan%         | nan%         | nanx          |
|  6 | ATAT     | 2025-03-25 | Before market open | Consumer Cyclical      | $4.2B        | $30.27  | nan%         | nan%         | nanx          |
|  7 | ATOS     | 2025-03-25 | Before market open | Healthcare             | $94.2M       | $0.75   | nan%         | nan%         | nanx          |
|  8 | CRMD     | 2025-03-25 | Before market open | Healthcare             | $653.5M      | $10.91  | nan%         | nan%         | nanx          |
|  9 | CSIQ     | 2025-03-25 | Before market open | Technology             | $642.2M      | $9.96   | nan%         | nan%         | nanx          |
| 10 | DFLI     | 2025-03-24 | After market close | Industrials            | $9.4M        | $1.38   | nan%         | nan%         | nanx          |
| 11 | FUFU     | 2025-03-25 | Before market open | Financial Services     | $726.5M      | $4.28   | nan%         | nan%         | nanx          |
| 12 | HDL      | 2025-03-25 | Before market open | Consumer Cyclical      | $1.5B        | $26.57  | nan%         | nan%         | nanx          |
| 13 | INLX     | 2025-03-24 | After market close | Technology             | $47.0M       | $11.10  | nan%         | nan%         | nanx          |
| 14 | IPM      | 2025-03-24 | After market close | Technology             | $25.8M       | $1.82   | nan%         | nan%         | nanx          |
| 15 | MKC.V    | 2025-03-25 | Before market open | nan                    | N/A          | $nan    | nan%         | nan%         | nanx          |
| 16 | nan      | 2025-03-25 | Before market open | Technology             | $78.1M       | $4.70   | nan%         | nan%         | nanx          |
| 17 | NXGL     | 2025-03-24 | After market close | Healthcare             | $21.0M       | $2.70   | nan%         | nan%         | nanx          |
| 18 | OCX      | 2025-03-24 | After market close | Healthcare             | $95.2M       | $3.40   | nan%         | nan%         | nanx          |
| 19 | OKLO     | 2025-03-24 | After market close | Utilities              | $4.2B        | $27.16  | nan%         | nan%         | nanx          |
| 20 | PAVM     | 2025-03-25 | Before market open | Healthcare             | $10.9M       | $0.81   | nan%         | nan%         | nanx          |
| 21 | PHGE     | 2025-03-25 | Before market open | Healthcare             | $15.7M       | $0.64   | nan%         | nan%         | nanx          |
| 22 | PONY     | 2025-03-25 | Before market open | Technology             | $4.6B        | $12.71  | nan%         | nan%         | nanx          |
| 23 | RUM      | 2025-03-25 | Before market open | Communication Services | $2.5B        | $7.74   | nan%         | nan%         | nanx          |
| 24 | SBS      | 2025-03-24 | After market close | Utilities              | $12.0B       | $17.66  | nan%         | nan%         | nanx          |
| 25 | SFD      | 2025-03-25 | Before market open | Consumer Defensive     | $7.7B        | $19.05  | nan%         | nan%         | nanx          |
| 26 | SMTI     | 2025-03-25 | Before market open | Healthcare             | $312.0M      | $33.60  | nan%         | nan%         | nanx          |
| 27 | VERB     | 2025-03-25 | Before market open | Technology             | $5.7M        | $5.46   | nan%         | nan%         | nanx          |
| 28 | VIOT     | 2025-03-25 | Before market open | Consumer Cyclical      | $162.6M      | $1.88   | nan%         | nan%         | nanx          |
| 29 | XFOR     | 2025-03-25 | Before market open | Healthcare             | $50.3M       | $0.31   | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
