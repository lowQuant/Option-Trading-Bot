# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-05-20 21:53:38 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | DY       | 2025-05-21 | Before market open | Industrials            | $5.6B        | $192.12 | 37.59%       | 53.32%       | 1.42x         |
|  1 | VSAT     | 2025-05-20 | After market close | Technology             | $1.4B        | $10.71  | 71.03%       | 88.39%       | 1.24x         |
|  2 | TGT      | 2025-05-21 | Before market open | Consumer Defensive     | $44.6B       | $97.99  | 48.44%       | 55.00%       | 1.14x         |
|  3 | TJX      | 2025-05-21 | Before market open | Consumer Cyclical      | $150.6B      | $135.03 | 23.66%       | 24.86%       | 1.05x         |
|  4 | MDT      | 2025-05-21 | Before market open | Healthcare             | $110.8B      | $86.97  | 24.20%       | 25.08%       | 1.04x         |
|  5 | TOL      | 2025-05-20 | After market close | Consumer Cyclical      | $10.4B       | $106.05 | 43.42%       | 43.75%       | 1.01x         |
|  6 | LOW      | 2025-05-21 | Before market open | Consumer Cyclical      | $129.4B      | $234.43 | 31.92%       | 30.89%       | 0.97x         |
|  7 | PANW     | 2025-05-20 | After market close | Technology             | $128.8B      | $194.30 | 46.02%       | 43.42%       | 0.94x         |
|  8 | KEYS     | 2025-05-20 | After market close | Technology             | $28.1B       | $162.77 | 45.52%       | 38.64%       | 0.85x         |
|  9 | VFC      | 2025-05-21 | Before market open | Consumer Cyclical      | $5.6B        | $14.32  | 99.59%       | 77.42%       | 0.78x         |
| 10 | AUNA     | 2025-05-20 | After market close | Healthcare             | $518.1M      | $7.08   | nan%         | nan%         | nanx          |
| 11 | BIDU     | 2025-05-21 | Before market open | Communication Services | $30.5B       | $89.25  | nan%         | nan%         | nanx          |
| 12 | BIOX     | 2025-05-20 | After market close | Basic Materials        | $281.1M      | $4.76   | nan%         | nan%         | nanx          |
| 13 | BZUN     | 2025-05-21 | Before market open | Consumer Cyclical      | $182.9M      | $3.32   | nan%         | nan%         | nanx          |
| 14 | CCIF     | 2025-05-20 | After market close | Financial Services     | $111.0M      | $6.64   | nan%         | nan%         | nanx          |
| 15 | CLCO     | 2025-05-21 | Before market open | Energy                 | $326.5M      | $6.23   | nan%         | nan%         | nanx          |
| 16 | CMBT     | 2025-05-21 | Before market open | Energy                 | $1.8B        | $9.52   | nan%         | nan%         | nanx          |
| 17 | EARN     | 2025-05-20 | After market close | Financial Services     | $210.0M      | $5.62   | nan%         | nan%         | nanx          |
| 18 | EVGN     | 2025-05-21 | Before market open | Healthcare             | $8.5M        | $1.38   | nan%         | nan%         | nanx          |
| 19 | EVLV     | 2025-05-20 | After market close | Industrials            | $905.6M      | $5.74   | nan%         | nan%         | nanx          |
| 20 | FINV     | 2025-05-20 | After market close | Financial Services     | $2.2B        | $8.81   | nan%         | nan%         | nanx          |
| 21 | GOOS     | 2025-05-21 | Before market open | Consumer Cyclical      | $876.9M      | $8.99   | nan%         | nan%         | nanx          |
| 22 | HDL      | 2025-05-21 | Before market open | Consumer Cyclical      | $1.3B        | $22.27  | nan%         | nan%         | nanx          |
| 23 | IQ       | 2025-05-21 | Before market open | Communication Services | $1.8B        | $1.89   | nan%         | nan%         | nanx          |
| 24 | JHX      | 2025-05-20 | After market close | Basic Materials        | $10.6B       | $25.25  | nan%         | nan%         | nanx          |
| 25 | KNOP     | 2025-05-21 | Before market open | Energy                 | $240.0M      | $6.68   | nan%         | nan%         | nanx          |
| 26 | MDWD     | 2025-05-21 | Before market open | Healthcare             | $225.6M      | $20.51  | nan%         | nan%         | nanx          |
| 27 | MOD      | 2025-05-20 | After market close | Consumer Cyclical      | $5.6B        | $104.11 | nan%         | nan%         | nanx          |
| 28 | TUYA     | 2025-05-20 | After market close | Technology             | $1.7B        | $2.64   | nan%         | nan%         | nanx          |
| 29 | UCL      | 2025-05-21 | Before market open | Communication Services | $49.1M       | $1.34   | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
