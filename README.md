# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-05-21 21:53:02 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | AAP      | 2025-05-22 | Before market open | Consumer Cyclical      | $1.9B        | $34.16  | 54.30%       | 74.55%       | 1.37x         |
|  1 | RAMP     | 2025-05-21 | After market close | Technology             | $1.8B        | $28.85  | 44.58%       | 55.46%       | 1.24x         |
|  2 | BJ       | 2025-05-22 | Before market open | Consumer Defensive     | $15.5B       | $119.08 | 33.82%       | 39.90%       | 1.18x         |
|  3 | URBN     | 2025-05-21 | After market close | Consumer Cyclical      | $5.5B        | $61.34  | 65.82%       | 55.52%       | 0.84x         |
|  4 | ENS      | 2025-05-21 | After market close | Industrials            | $3.8B        | $98.13  | 43.66%       | 36.29%       | 0.83x         |
|  5 | RL       | 2025-05-22 | Before market open | Consumer Cyclical      | $16.9B       | $280.20 | 54.13%       | 44.81%       | 0.83x         |
|  6 | LPG      | 2025-05-22 | Before market open | Energy                 | $969.9M      | $23.41  | 53.74%       | 43.28%       | 0.81x         |
|  7 | CSWI     | 2025-05-22 | Before market open | Industrials            | $5.3B        | $324.68 | 50.99%       | 34.22%       | 0.67x         |
|  8 | ADI      | 2025-05-22 | Before market open | Technology             | $110.2B      | $224.49 | 65.95%       | 35.82%       | 0.54x         |
|  9 | ARQQ     | 2025-05-22 | Before market open | Technology             | $330.0M      | $24.63  | nan%         | nan%         | nanx          |
| 10 | ATAT     | 2025-05-22 | Before market open | Consumer Cyclical      | $4.2B        | $30.82  | nan%         | nan%         | nanx          |
| 11 | BBAR     | 2025-05-21 | After market close | Financial Services     | $4.6B        | $21.98  | nan%         | nan%         | nanx          |
| 12 | BORR     | 2025-05-21 | After market close | Energy                 | $385.3M      | $1.69   | nan%         | nan%         | nanx          |
| 13 | BZ       | 2025-05-22 | Before market open | Communication Services | $8.0B        | $18.11  | nan%         | nan%         | nanx          |
| 14 | CLIR     | 2025-05-21 | After market close | Industrials            | $37.2M       | $0.68   | nan%         | nan%         | nanx          |
| 15 | DOMO     | 2025-05-21 | After market close | Technology             | $343.7M      | $8.55   | nan%         | nan%         | nanx          |
| 16 | EDUC     | 2025-05-21 | After market close | Communication Services | $11.9M       | $1.30   | nan%         | nan%         | nanx          |
| 17 | FLX      | 2025-05-22 | Before market open | Industrials            | $169.3M      | $2.33   | nan%         | nan%         | nanx          |
| 18 | LSPD     | 2025-05-22 | Before market open | Technology             | $1.6B        | $10.97  | nan%         | nan%         | nanx          |
| 19 | LX       | 2025-05-21 | After market close | Financial Services     | $1.5B        | $8.89   | nan%         | nan%         | nanx          |
| 20 | NNOX     | 2025-05-22 | Before market open | Healthcare             | $334.1M      | $5.49   | nan%         | nan%         | nanx          |
| 21 | SNOW     | 2025-05-21 | After market close | Technology             | $59.8B       | $182.88 | nan%         | nan%         | nanx          |
| 22 | STG      | 2025-05-22 | Before market open | Consumer Defensive     | $70.7M       | $5.40   | nan%         | nan%         | nanx          |
| 23 | TD       | 2025-05-22 | Before market open | Financial Services     | $113.5B      | $64.80  | nan%         | nan%         | nanx          |
| 24 | THR      | 2025-05-22 | Before market open | Industrials            | $981.1M      | $29.70  | nan%         | nan%         | nanx          |
| 25 | TITN     | 2025-05-22 | Before market open | Industrials            | $460.3M      | $20.63  | nan%         | nan%         | nanx          |
| 26 | ZM       | 2025-05-21 | After market close | Technology             | $25.1B       | $83.10  | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
