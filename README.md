# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-11-10 20:53:45 EST

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | PSKY     | 2025-11-10 | After market close | Communication Services | $16.7B       | $15.10  | 33.25%       | 55.01%       | 1.65x         |
|  1 | TDW      | 2025-11-10 | After market close | Energy                 | $2.7B        | $52.90  | 46.48%       | 75.80%       | 1.63x         |
|  2 | OXY      | 2025-11-10 | After market close | Energy                 | $41.1B       | $41.31  | 34.67%       | 34.97%       | 1.01x         |
|  3 | ACCS     | 2025-11-11 | Before market open | Communication Services | $34.4M       | $9.09   | nan%         | nan%         | nanx          |
|  4 | AIV      | 2025-11-10 | After market close | Real Estate            | $765.7M      | $5.38   | nan%         | nan%         | nanx          |
|  5 | ALTI     | 2025-11-10 | After market close | Financial Services     | $626.2M      | $4.07   | nan%         | nan%         | nanx          |
|  6 | AMBC     | 2025-11-10 | After market close | Financial Services     | $403.2M      | $8.48   | nan%         | nan%         | nanx          |
|  7 | APEI     | 2025-11-10 | After market close | Consumer Defensive     | $596.0M      | $31.07  | nan%         | nan%         | nanx          |
|  8 | ARCT     | 2025-11-10 | After market close | Healthcare             | $238.4M      | $8.72   | nan%         | nan%         | nanx          |
|  9 | ASTS     | 2025-11-10 | After market close | Technology             | $25.2B       | $69.19  | nan%         | nan%         | nanx          |
| 10 | AU       | 2025-11-11 | Before market open | Basic Materials        | $37.4B       | $69.41  | nan%         | nan%         | nanx          |
| 11 | BALY     | 2025-11-10 | After market close | Consumer Cyclical      | $951.0M      | $18.56  | nan%         | nan%         | nanx          |
| 12 | BBAI     | 2025-11-10 | After market close | Technology             | $2.5B        | $5.68   | nan%         | nan%         | nanx          |
| 13 | BCSF     | 2025-11-10 | After market close | Financial Services     | $903.0M      | $13.89  | nan%         | nan%         | nanx          |
| 14 | BEEP     | 2025-11-10 | After market close | Industrials            | $139.6M      | $3.36   | nan%         | nan%         | nanx          |
| 15 | BLNE     | 2025-11-10 | After market close | Financial Services     | $58.6M       | $2.11   | nan%         | nan%         | nanx          |
| 16 | BLTE     | 2025-11-10 | After market close | Healthcare             | $4.1B        | $113.19 | nan%         | nan%         | nanx          |
| 17 | BODI     | 2025-11-10 | After market close | Communication Services | $35.5M       | $5.00   | nan%         | nan%         | nanx          |
| 18 | BWAY     | 2025-11-11 | Before market open | Healthcare             | $322.6M      | $15.59  | nan%         | nan%         | nanx          |
| 19 | CAPR     | 2025-11-10 | After market close | Healthcare             | $254.2M      | $5.93   | nan%         | nan%         | nanx          |
| 20 | CATX     | 2025-11-10 | After market close | Healthcare             | $164.9M      | $2.19   | nan%         | nan%         | nanx          |
| 21 | CHGG     | 2025-11-10 | After market close | Consumer Defensive     | $96.4M       | $0.89   | nan%         | nan%         | nanx          |
| 22 | CNNE     | 2025-11-10 | After market close | Consumer Cyclical      | $861.4M      | $17.36  | nan%         | nan%         | nanx          |
| 23 | CRNT     | 2025-11-11 | Before market open | Technology             | $204.9M      | $2.33   | nan%         | nan%         | nanx          |
| 24 | CRWV     | 2025-11-10 | After market close | Technology             | $52.3B       | $104.01 | nan%         | nan%         | nanx          |
| 25 | CVGI     | 2025-11-10 | After market close | Consumer Cyclical      | $55.5M       | $1.34   | nan%         | nan%         | nanx          |
| 26 | CVV      | 2025-11-10 | After market close | Industrials            | $23.7M       | $3.45   | nan%         | nan%         | nanx          |
| 27 | CWCO     | 2025-11-10 | After market close | Utilities              | $550.4M      | $34.81  | nan%         | nan%         | nanx          |
| 28 | DAVA     | 2025-11-11 | Before market open | Technology             | $512.3M      | $9.30   | nan%         | nan%         | nanx          |
| 29 | DCGO     | 2025-11-10 | After market close | Healthcare             | $108.6M      | $1.11   | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
