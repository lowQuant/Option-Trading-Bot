# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-11-19 20:50:43 EST

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | MMS      | 2025-11-20 | Before market open | Industrials            | $4.4B        | $78.95  | 19.05%       | 46.66%       | 2.45x         |
|  1 | WMG      | 2025-11-20 | Before market open | Communication Services | $15.9B       | $29.81  | 21.47%       | 47.07%       | 2.19x         |
|  2 | LQDT     | 2025-11-20 | Before market open | Consumer Cyclical      | $708.5M      | $22.58  | 37.91%       | 74.26%       | 1.96x         |
|  3 | BBWI     | 2025-11-20 | Before market open | Consumer Cyclical      | $4.5B        | $21.10  | 36.17%       | 66.97%       | 1.85x         |
|  4 | PANW     | 2025-11-19 | After market close | Technology             | $136.7B      | $201.00 | 27.06%       | 45.60%       | 1.69x         |
|  5 | CPRT     | 2025-11-20 | Before market open | Industrials            | $40.0B       | $41.32  | 25.01%       | 41.25%       | 1.65x         |
|  6 | WMT      | 2025-11-20 | Before market open | Consumer Defensive     | $802.9B      | $101.39 | 20.68%       | 32.00%       | 1.55x         |
|  7 | SCVL     | 2025-11-20 | Before market open | Consumer Cyclical      | $457.1M      | $16.68  | 47.99%       | 63.25%       | 1.32x         |
|  8 | J        | 2025-11-20 | Before market open | Industrials            | $17.4B       | $150.76 | 28.65%       | 36.13%       | 1.26x         |
|  9 | NVDA     | 2025-11-19 | After market close | Technology             | $4.5tr       | $181.36 | 43.80%       | 54.93%       | 1.25x         |
| 10 | KLIC     | 2025-11-19 | After market close | Technology             | $1.9B        | $35.56  | 41.50%       | 49.97%       | 1.20x         |
| 11 | ALLT     | 2025-11-20 | Before market open | Technology             | $413.6M      | $8.54   | nan%         | nan%         | nanx          |
| 12 | API      | 2025-11-19 | After market close | Technology             | $309.5M      | $3.29   | nan%         | nan%         | nanx          |
| 13 | ATKR     | 2025-11-20 | Before market open | Industrials            | $2.2B        | $65.10  | nan%         | nan%         | nanx          |
| 14 | BV       | 2025-11-19 | After market close | Industrials            | $1.1B        | $11.89  | nan%         | nan%         | nanx          |
| 15 | CDLR     | 2025-11-20 | Before market open | Industrials            | $1.4B        | $17.37  | nan%         | nan%         | nanx          |
| 16 | CLCO     | 2025-11-20 | Before market open | Energy                 | $523.0M      | $9.80   | nan%         | nan%         | nanx          |
| 17 | CPA      | 2025-11-19 | After market close | Industrials            | $5.2B        | $123.21 | nan%         | nan%         | nanx          |
| 18 | CRNC     | 2025-11-19 | After market close | Technology             | $343.1M      | $7.82   | nan%         | nan%         | nanx          |
| 19 | DAO      | 2025-11-20 | Before market open | Consumer Defensive     | $1.2B        | $9.69   | nan%         | nan%         | nanx          |
| 20 | DLNG     | 2025-11-20 | Before market open | Energy                 | $129.3M      | $3.58   | nan%         | nan%         | nanx          |
| 21 | DSX      | 2025-11-20 | Before market open | Industrials            | $203.8M      | $1.74   | nan%         | nan%         | nanx          |
| 22 | EARN     | 2025-11-19 | After market close | Financial Services     | $191.6M      | $5.17   | nan%         | nan%         | nanx          |
| 23 | EVGN     | 2025-11-20 | Before market open | Healthcare             | $10.7M       | $1.17   | nan%         | nan%         | nanx          |
| 24 | FINV     | 2025-11-19 | After market close | Financial Services     | $1.4B        | $5.97   | nan%         | nan%         | nanx          |
| 25 | JACK     | 2025-11-19 | After market close | Consumer Cyclical      | $271.5M      | $14.25  | nan%         | nan%         | nanx          |
| 26 | JOYY     | 2025-11-19 | After market close | Communication Services | $3.1B        | $59.35  | nan%         | nan%         | nanx          |
| 27 | MAGN     | 2025-11-20 | Before market open | Basic Materials        | $283.4M      | $8.05   | nan%         | nan%         | nanx          |
| 28 | MDWD     | 2025-11-20 | Before market open | Healthcare             | $229.0M      | $18.28  | nan%         | nan%         | nanx          |
| 29 | NJR      | 2025-11-19 | After market close | Utilities              | $4.6B        | $46.38  | 16.07%       | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
