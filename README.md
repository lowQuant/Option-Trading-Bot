# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-08-12 21:58:23 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | HRB      | 2025-08-12 | After market close | Consumer Cyclical      | $6.9B        | $54.45  | 15.81%       | 36.11%       | 2.28x         |
|  1 | ECG      | 2025-08-12 | After market close | Industrials            | $3.9B        | $70.88  | 35.38%       | 71.33%       | 2.02x         |
|  2 | PFGC     | 2025-08-13 | Before market open | Consumer Defensive     | $15.4B       | $97.46  | 22.82%       | 38.25%       | 1.68x         |
|  3 | LITE     | 2025-08-12 | After market close | Technology             | $8.3B        | $115.03 | 37.84%       | 63.22%       | 1.67x         |
|  4 | EAT      | 2025-08-13 | Before market open | Consumer Cyclical      | $6.9B        | $152.09 | 36.06%       | 58.52%       | 1.62x         |
|  5 | CAVA     | 2025-08-12 | After market close | Consumer Cyclical      | $9.8B        | $82.30  | 51.81%       | 69.31%       | 1.34x         |
|  6 | ABSI     | 2025-08-12 | After market close | Healthcare             | $428.4M      | $2.85   | nan%         | nan%         | nanx          |
|  7 | AII      | 2025-08-12 | After market close | Financial Services     | $347.8M      | $17.79  | nan%         | nan%         | nanx          |
|  8 | ALCO     | 2025-08-12 | After market close | Consumer Defensive     | $254.2M      | $32.40  | nan%         | nan%         | nanx          |
|  9 | ALXO     | 2025-08-12 | After market close | Healthcare             | $32.9M       | $0.61   | nan%         | nan%         | nanx          |
| 10 | AMS      | 2025-08-13 | Before market open | Healthcare             | $16.6M       | $2.48   | nan%         | nan%         | nanx          |
| 11 | ANTA     | 2025-08-12 | After market close | Financial Services     | $293.6M      | $12.75  | nan%         | nan%         | nanx          |
| 12 | AP       | 2025-08-12 | After market close | Industrials            | $68.3M       | $3.41   | nan%         | nan%         | nanx          |
| 13 | ARCO     | 2025-08-13 | Before market open | Consumer Cyclical      | $1.5B        | $6.76   | nan%         | nan%         | nanx          |
| 14 | ATEX     | 2025-08-12 | After market close | Communication Services | $418.8M      | $20.96  | nan%         | nan%         | nanx          |
| 15 | BEEP     | 2025-08-12 | After market close | Industrials            | $159.8M      | $3.81   | nan%         | nan%         | nanx          |
| 16 | BKYI     | 2025-08-13 | Before market open | Industrials            | $5.5M        | $0.78   | nan%         | nan%         | nanx          |
| 17 | BRTX     | 2025-08-12 | After market close | Healthcare             | $11.0M       | $1.42   | nan%         | nan%         | nanx          |
| 18 | BWAY     | 2025-08-13 | Before market open | Healthcare             | $230.4M      | $12.10  | nan%         | nan%         | nanx          |
| 19 | CAAS     | 2025-08-13 | Before market open | Consumer Cyclical      | $124.6M      | $4.05   | nan%         | nan%         | nanx          |
| 20 | CAE      | 2025-08-13 | Before market open | Industrials            | $9.5B        | $28.75  | nan%         | nan%         | nanx          |
| 21 | CAI      | 2025-08-12 | After market close | Healthcare             | $9.0B        | $30.08  | nan%         | nan%         | nanx          |
| 22 | CATX     | 2025-08-13 | Before market open | Healthcare             | $295.4M      | $3.72   | nan%         | nan%         | nanx          |
| 23 | CLPT     | 2025-08-12 | After market close | Healthcare             | $297.9M      | $10.60  | nan%         | nan%         | nanx          |
| 24 | CREX     | 2025-08-13 | Before market open | Technology             | $25.1M       | $2.39   | nan%         | nan%         | nanx          |
| 25 | CRWS     | 2025-08-13 | Before market open | Consumer Cyclical      | $30.1M       | $2.85   | nan%         | nan%         | nanx          |
| 26 | CRWV     | 2025-08-12 | After market close | Technology             | $71.6B       | $139.78 | nan%         | nan%         | nanx          |
| 27 | CSAI     | 2025-08-13 | Before market open | Technology             | $33.1M       | $1.88   | nan%         | nan%         | nanx          |
| 28 | CVV      | 2025-08-12 | After market close | Industrials            | $21.7M       | $3.68   | nan%         | nan%         | nanx          |
| 29 | CXAI     | 2025-08-12 | After market close | Technology             | $18.6M       | $0.89   | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
