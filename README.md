# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-11-24 20:53:39 EST

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | ANF      | 2025-11-25 | Before market open | Consumer Cyclical      | $3.1B        | $69.87  | 33.79%       | 74.36%       | 2.20x         |
|  1 | EMBC     | 2025-11-25 | Before market open | Healthcare             | $856.2M      | $14.57  | 34.62%       | 59.61%       | 1.72x         |
|  2 | A        | 2025-11-24 | After market close | Healthcare             | $43.6B       | $151.25 | 21.73%       | 37.03%       | 1.70x         |
|  3 | SMTC     | 2025-11-24 | After market close | Technology             | $6.1B        | $63.85  | 51.38%       | 85.70%       | 1.67x         |
|  4 | DKS      | 2025-11-25 | Before market open | Consumer Cyclical      | $18.5B       | $208.45 | 34.04%       | 55.65%       | 1.63x         |
|  5 | KSS      | 2025-11-25 | Before market open | Consumer Cyclical      | $1.8B        | $15.71  | 57.71%       | 92.23%       | 1.60x         |
|  6 | WWD      | 2025-11-24 | After market close | Industrials            | $15.7B       | $262.70 | 30.16%       | 44.97%       | 1.49x         |
|  7 | SJM      | 2025-11-25 | Before market open | Consumer Defensive     | $11.1B       | $105.54 | 23.63%       | 32.98%       | 1.40x         |
|  8 | KEYS     | 2025-11-24 | After market close | Technology             | $30.6B       | $172.71 | 31.50%       | 43.72%       | 1.39x         |
|  9 | BURL     | 2025-11-25 | Before market open | Consumer Cyclical      | $17.9B       | $296.51 | 36.44%       | 50.38%       | 1.38x         |
| 10 | BBY      | 2025-11-25 | Before market open | Consumer Cyclical      | $16.0B       | $76.45  | 36.01%       | 49.26%       | 1.37x         |
| 11 | SNEX     | 2025-11-24 | After market close | Financial Services     | $4.4B        | $83.71  | 36.00%       | 48.37%       | 1.34x         |
| 12 | ADI      | 2025-11-25 | Before market open | Technology             | $117.8B      | $232.32 | 30.16%       | 39.38%       | 1.31x         |
| 13 | AMTM     | 2025-11-25 | Before market open | Industrials            | $6.2B        | $24.26  | 56.75%       | 68.79%       | 1.21x         |
| 14 | ALCO     | 2025-11-24 | After market close | Consumer Defensive     | $242.6M      | $31.73  | nan%         | nan%         | nanx          |
| 15 | ATAT     | 2025-11-25 | Before market open | Consumer Cyclical      | $5.2B        | $37.09  | nan%         | nan%         | nanx          |
| 16 | AVXL     | 2025-11-25 | Before market open | Healthcare             | $264.6M      | $3.26   | nan%         | nan%         | nanx          |
| 17 | BABA     | 2025-11-25 | Before market open | Consumer Cyclical      | $383.5B      | $152.93 | nan%         | nan%         | nanx          |
| 18 | BLBD     | 2025-11-24 | After market close | Industrials            | $1.7B        | $53.82  | nan%         | nan%         | nanx          |
| 19 | BOSC     | 2025-11-25 | Before market open | Technology             | $27.0M       | $4.37   | nan%         | nan%         | nanx          |
| 20 | BZUN     | 2025-11-25 | Before market open | Consumer Cyclical      | $176.6M      | $2.84   | nan%         | nan%         | nanx          |
| 21 | CENT     | 2025-11-24 | After market close | Consumer Defensive     | $2.0B        | $32.29  | 25.41%       | nan%         | nanx          |
| 22 | CENTA    | 2025-11-24 | After market close | Consumer Defensive     | $1.8B        | $29.24  | 25.80%       | nan%         | nanx          |
| 23 | CLFD     | 2025-11-25 | Before market open | Technology             | $406.4M      | $29.26  | nan%         | nan%         | nanx          |
| 24 | FLNC     | 2025-11-24 | After market close | Utilities              | $2.9B        | $15.40  | nan%         | nan%         | nanx          |
| 25 | FSCO     | 2025-11-24 | After market close | Financial Services     | $1.2B        | $6.10   | nan%         | nan%         | nanx          |
| 26 | GMHS     | 2025-11-25 | Before market open | Communication Services | $63.2M       | $1.03   | nan%         | nan%         | nanx          |
| 27 | JFIN     | 2025-11-25 | Before market open | Communication Services | $385.3M      | $7.44   | nan%         | nan%         | nanx          |
| 28 | MOV      | 2025-11-25 | Before market open | Consumer Cyclical      | $432.5M      | $19.24  | nan%         | nan%         | nanx          |
| 29 | NIO      | 2025-11-25 | Before market open | Consumer Cyclical      | $14.2B       | $5.58   | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
