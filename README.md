# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-05-12 21:53:42 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | ACHC     | 2025-05-12 | After market close | Healthcare             | $2.4B        | $23.84  | 60.62%       | 84.86%       | 1.40x         |
|  1 | DVA      | 2025-05-12 | After market close | Healthcare             | $11.1B       | $143.76 | 33.31%       | 46.21%       | 1.39x         |
|  2 | MODG     | 2025-05-12 | After market close | Consumer Cyclical      | $1.5B        | $7.34   | 70.20%       | 77.62%       | 1.11x         |
|  3 | ZI       | 2025-05-12 | After market close | Technology             | $3.8B        | $9.35   | 85.75%       | 82.91%       | 0.97x         |
|  4 | BCO      | 2025-05-12 | After market close | Industrials            | $4.1B        | $92.56  | 38.52%       | 35.30%       | 0.92x         |
|  5 | ARWR     | 2025-05-12 | After market close | Healthcare             | $1.9B        | $13.03  | 93.82%       | 79.48%       | 0.85x         |
|  6 | VTLE     | 2025-05-12 | After market close | Energy                 | $656.8M      | $16.05  | 132.09%      | 93.39%       | 0.71x         |
|  7 | UA       | 2025-05-13 | Before market open | Consumer Cyclical      | $2.6B        | $5.58   | 81.67%       | 57.15%       | 0.70x         |
|  8 | UAA      | 2025-05-13 | Before market open | Consumer Cyclical      | $2.6B        | $5.84   | 86.70%       | 59.00%       | 0.68x         |
|  9 | SLAB     | 2025-05-13 | Before market open | Technology             | $4.1B        | $117.05 | 87.72%       | 58.65%       | 0.67x         |
| 10 | POWI     | 2025-05-12 | After market close | Technology             | $3.4B        | $54.11  | 72.37%       | 46.68%       | 0.65x         |
| 11 | HTZ      | 2025-05-12 | After market close | Industrials            | $2.1B        | $6.72   | 196.67%      | 121.68%      | 0.62x         |
| 12 | SPG      | 2025-05-12 | After market close | Real Estate            | $64.6B       | $163.19 | 48.59%       | 27.90%       | 0.57x         |
| 13 | ABOS     | 2025-05-13 | Before market open | Healthcare             | $63.6M       | $0.98   | nan%         | nan%         | nanx          |
| 14 | ACCS     | 2025-05-13 | Before market open | Communication Services | $34.6M       | $8.98   | nan%         | nan%         | nanx          |
| 15 | ACHR     | 2025-05-12 | After market close | Industrials            | $5.0B        | $8.81   | nan%         | nan%         | nanx          |
| 16 | ACHV     | 2025-05-13 | Before market open | Healthcare             | $86.0M       | $2.35   | nan%         | nan%         | nanx          |
| 17 | ACNT     | 2025-05-12 | After market close | Basic Materials        | $128.6M      | $12.86  | nan%         | nan%         | nanx          |
| 18 | ACXP     | 2025-05-13 | Before market open | Healthcare             | $8.7M        | $0.36   | nan%         | nan%         | nanx          |
| 19 | ADAP     | 2025-05-13 | Before market open | Healthcare             | $77.9M       | $0.30   | nan%         | nan%         | nanx          |
| 20 | AIRJ     | 2025-05-12 | After market close | Industrials            | $263.8M      | $4.74   | nan%         | nan%         | nanx          |
| 21 | ALT      | 2025-05-13 | Before market open | Healthcare             | $462.9M      | $5.59   | nan%         | nan%         | nanx          |
| 22 | ALTI     | 2025-05-12 | After market close | Financial Services     | $502.3M      | $3.44   | nan%         | nan%         | nanx          |
| 23 | AMBC     | 2025-05-12 | After market close | Financial Services     | $426.6M      | $8.21   | nan%         | nan%         | nanx          |
| 24 | AMPY     | 2025-05-12 | After market close | Energy                 | $118.2M      | $2.89   | nan%         | nan%         | nanx          |
| 25 | AP       | 2025-05-13 | Before market open | Industrials            | $57.5M       | $2.69   | nan%         | nan%         | nanx          |
| 26 | APEI     | 2025-05-12 | After market close | Consumer Defensive     | $469.7M      | $27.49  | nan%         | nan%         | nanx          |
| 27 | AQST     | 2025-05-12 | After market close | Healthcare             | $281.8M      | $2.79   | nan%         | nan%         | nanx          |
| 28 | ARCT     | 2025-05-12 | After market close | Healthcare             | $314.3M      | $10.98  | nan%         | nan%         | nanx          |
| 29 | ASRT     | 2025-05-12 | After market close | Healthcare             | $58.9M       | $0.61   | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
