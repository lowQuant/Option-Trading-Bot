# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-08-20 21:49:22 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | COTY     | 2025-08-20 | After market close | Consumer Defensive     | $4.2B        | $4.89   | 35.16%       | 64.38%       | 1.83x         |
|  1 | MZTI     | 2025-08-21 | Before market open | Consumer Defensive     | $4.9B        | $180.48 | 18.45%       | 29.18%       | 1.58x         |
|  2 | WMT      | 2025-08-21 | Before market open | Consumer Defensive     | $818.6B      | $101.29 | 17.68%       | 27.43%       | 1.55x         |
|  3 | NDSN     | 2025-08-20 | After market close | Industrials            | $12.1B       | $217.50 | 21.88%       | 28.99%       | 1.32x         |
|  4 | OSIS     | 2025-08-21 | Before market open | Technology             | $3.8B        | $226.91 | 34.13%       | 43.71%       | 1.28x         |
|  5 | JBSS     | 2025-08-20 | After market close | Consumer Defensive     | $730.1M      | $63.23  | 26.03%       | 25.96%       | 1.00x         |
|  6 | AAPG     | 2025-08-20 | After market close | Healthcare             | $4.4B        | $46.40  | nan%         | nan%         | nanx          |
|  7 | AEG      | 2025-08-21 | Before market open | Financial Services     | $11.7B       | $7.44   | nan%         | nan%         | nanx          |
|  8 | BBAR     | 2025-08-20 | After market close | Financial Services     | $3.3B        | $14.94  | nan%         | nan%         | nanx          |
|  9 | BILI     | 2025-08-21 | Before market open | Communication Services | $10.4B       | $25.07  | nan%         | nan%         | nanx          |
| 10 | BOSC     | 2025-08-21 | Before market open | Technology             | $29.1M       | $4.93   | nan%         | nan%         | nanx          |
| 11 | CSIQ     | 2025-08-21 | Before market open | Technology             | $853.9M      | $12.54  | nan%         | nan%         | nanx          |
| 12 | FINV     | 2025-08-20 | After market close | Financial Services     | $2.2B        | $8.79   | nan%         | nan%         | nanx          |
| 13 | HOV      | 2025-08-21 | Before market open | Consumer Cyclical      | $755.0M      | $155.36 | nan%         | nan%         | nanx          |
| 14 | LYTS     | 2025-08-21 | Before market open | Technology             | $579.1M      | $18.98  | nan%         | nan%         | nanx          |
| 15 | MNSO     | 2025-08-21 | Before market open | Consumer Cyclical      | $6.4B        | $20.13  | nan%         | nan%         | nanx          |
| 16 | OCFT     | 2025-08-21 | Before market open | Technology             | $289.9M      | $7.31   | nan%         | nan%         | nanx          |
| 17 | SCSC     | 2025-08-21 | Before market open | Technology             | $961.0M      | $43.06  | 34.56%       | nan%         | nanx          |
| 18 | SLQT     | 2025-08-21 | Before market open | Financial Services     | $316.1M      | $1.88   | nan%         | nan%         | nanx          |
| 19 | TWIN     | 2025-08-21 | Before market open | Industrials            | $122.0M      | $8.69   | nan%         | nan%         | nanx          |
| 20 | UFI      | 2025-08-20 | After market close | Consumer Cyclical      | $81.7M       | $4.49   | nan%         | nan%         | nanx          |
| 21 | VNET     | 2025-08-21 | Before market open | Technology             | $2.1B        | $7.84   | nan%         | nan%         | nanx          |
| 22 | YMM      | 2025-08-21 | Before market open | Technology             | $11.5B       | $10.93  | nan%         | nan%         | nanx          |
| 23 | YRD      | 2025-08-21 | Before market open | Financial Services     | $503.7M      | $5.92   | nan%         | nan%         | nanx          |
| 24 | YSG      | 2025-08-21 | Before market open | Consumer Defensive     | $879.8M      | $9.48   | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
