# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-05-13 21:52:29 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector             | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | EXEL     | 2025-05-13 | After market close | Healthcare         | $10.2B       | $36.98  | 38.46%       | 55.92%       | 1.45x         |
|  1 | MRP      | 2025-05-14 | Before market open | Real Estate        | $4.4B        | $26.29  | 41.47%       | 41.99%       | 1.01x         |
|  2 | DT       | 2025-05-14 | Before market open | Technology         | $15.1B       | $50.48  | 48.49%       | 36.56%       | 0.75x         |
|  3 | LSTR     | 2025-05-13 | After market close | Industrials        | $4.9B        | $143.81 | 46.92%       | 35.07%       | 0.75x         |
|  4 | ABSI     | 2025-05-13 | After market close | Healthcare         | $377.5M      | $2.93   | nan%         | nan%         | nanx          |
|  5 | ADCT     | 2025-05-14 | Before market open | Healthcare         | $132.9M      | $1.34   | nan%         | nan%         | nanx          |
|  6 | AFCG     | 2025-05-14 | Before market open | Real Estate        | $130.4M      | $5.65   | nan%         | nan%         | nanx          |
|  7 | AIP      | 2025-05-13 | After market close | Technology         | $346.2M      | $7.87   | nan%         | nan%         | nanx          |
|  8 | AKA      | 2025-05-13 | After market close | Consumer Cyclical  | $93.0M       | $8.69   | nan%         | nan%         | nanx          |
|  9 | ALC      | 2025-05-13 | After market close | Healthcare         | $46.7B       | $94.79  | nan%         | nan%         | nanx          |
| 10 | ALCO     | 2025-05-13 | After market close | Consumer Defensive | $224.9M      | $29.24  | nan%         | nan%         | nanx          |
| 11 | ALLO     | 2025-05-13 | After market close | Healthcare         | $255.9M      | $1.17   | nan%         | nan%         | nanx          |
| 12 | ALUR     | 2025-05-14 | Before market open | Healthcare         | $14.1M       | $2.36   | nan%         | nan%         | nanx          |
| 13 | ARCO     | 2025-05-14 | Before market open | Consumer Cyclical  | $1.7B        | $7.93   | nan%         | nan%         | nanx          |
| 14 | ASM      | 2025-05-13 | After market close | Basic Materials    | $343.2M      | $2.40   | nan%         | nan%         | nanx          |
| 15 | ASNS     | 2025-05-13 | After market close | Technology         | $6.8M        | $0.77   | nan%         | nan%         | nanx          |
| 16 | AUID     | 2025-05-13 | After market close | Technology         | $65.3M       | $5.50   | nan%         | nan%         | nanx          |
| 17 | BDSX     | 2025-05-13 | After market close | Healthcare         | $52.6M       | $0.36   | nan%         | nan%         | nanx          |
| 18 | BEAT     | 2025-05-13 | After market close | Healthcare         | $57.7M       | $1.72   | nan%         | nan%         | nanx          |
| 19 | BITF     | 2025-05-14 | Before market open | Financial Services | $655.7M      | $1.09   | nan%         | nan%         | nanx          |
| 20 | CAAS     | 2025-05-14 | Before market open | Consumer Cyclical  | $127.3M      | $4.22   | nan%         | nan%         | nanx          |
| 21 | CAE      | 2025-05-13 | After market close | Industrials        | $8.5B        | $26.45  | nan%         | nan%         | nanx          |
| 22 | CAPR     | 2025-05-13 | After market close | Healthcare         | $333.4M      | $7.11   | nan%         | nan%         | nanx          |
| 23 | CINT     | 2025-05-13 | After market close | Technology         | $848.5M      | $6.30   | nan%         | nan%         | nanx          |
| 24 | CLBT     | 2025-05-14 | Before market open | Technology         | $4.8B        | $19.85  | nan%         | nan%         | nanx          |
| 25 | CLPT     | 2025-05-13 | After market close | Healthcare         | $397.3M      | $13.64  | nan%         | nan%         | nanx          |
| 26 | CREX     | 2025-05-14 | Before market open | Technology         | $18.6M       | $1.64   | nan%         | nan%         | nanx          |
| 27 | CSPI     | 2025-05-14 | Before market open | Technology         | $158.8M      | $15.99  | nan%         | nan%         | nanx          |
| 28 | CVV      | 2025-05-13 | After market close | Industrials        | $20.0M       | $2.90   | nan%         | nan%         | nanx          |
| 29 | DAC      | 2025-05-13 | After market close | Industrials        | $1.7B        | $87.16  | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
