# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-03-25 21:44:31 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | REX      | 2025-03-26 | Before market open | Basic Materials        | $648.4M      | $36.91  | 29.22%       | 65.65%       | 2.25x         |
|  1 | CTAS     | 2025-03-26 | Before market open | Industrials            | $78.5B       | $194.57 | 20.48%       | 35.83%       | 1.75x         |
|  2 | DLTR     | 2025-03-26 | Before market open | Consumer Defensive     | $15.0B       | $69.74  | 45.84%       | 67.93%       | 1.48x         |
|  3 | GME      | 2025-03-25 | After market close | Consumer Cyclical      | $11.4B       | $25.61  | 53.77%       | 73.22%       | 1.36x         |
|  4 | WOR      | 2025-03-25 | After market close | Industrials            | $2.1B        | $41.03  | 34.73%       | 42.88%       | 1.23x         |
|  5 | CHWY     | 2025-03-26 | Before market open | Consumer Cyclical      | $13.7B       | $34.02  | 50.02%       | 60.67%       | 1.21x         |
|  6 | PAYX     | 2025-03-26 | Before market open | Technology             | $52.1B       | $144.83 | 23.78%       | 26.75%       | 1.12x         |
|  7 | AACG     | 2025-03-25 | After market close | Consumer Defensive     | $31.8M       | $0.99   | nan%         | nan%         | nanx          |
|  8 | ALUR     | 2025-03-26 | Before market open | Healthcare             | $18.5M       | $3.45   | nan%         | nan%         | nanx          |
|  9 | BBNX     | 2025-03-25 | After market close | Healthcare             | $659.5M      | $14.85  | nan%         | nan%         | nanx          |
| 10 | CAN      | 2025-03-26 | Before market open | Technology             | $386.1M      | $1.07   | nan%         | nan%         | nanx          |
| 11 | CLGN     | 2025-03-26 | Before market open | Healthcare             | $32.1M       | $3.15   | nan%         | nan%         | nanx          |
| 12 | CMCM     | 2025-03-26 | Before market open | Communication Services | $150.3M      | $5.03   | nan%         | nan%         | nanx          |
| 13 | CRVS     | 2025-03-25 | After market close | Healthcare             | $273.1M      | $4.25   | nan%         | nan%         | nanx          |
| 14 | DOOO     | 2025-03-26 | Before market open | Consumer Cyclical      | $2.8B        | $38.10  | nan%         | nan%         | nanx          |
| 15 | GCTS     | 2025-03-25 | After market close | Technology             | $99.8M       | $2.06   | nan%         | nan%         | nanx          |
| 16 | JKS      | 2025-03-26 | Before market open | Technology             | $1.0B        | $21.07  | nan%         | nan%         | nanx          |
| 17 | NOAH     | 2025-03-25 | After market close | Financial Services     | $807.4M      | $11.16  | nan%         | nan%         | nanx          |
| 18 | PAYS     | 2025-03-25 | After market close | Technology             | $134.9M      | $2.52   | nan%         | nan%         | nanx          |
| 19 | PRTS     | 2025-03-25 | After market close | Consumer Cyclical      | $58.4M       | $1.09   | nan%         | nan%         | nanx          |
| 20 | REED     | 2025-03-26 | Before market open | Consumer Defensive     | $67.1M       | $1.25   | nan%         | nan%         | nanx          |
| 21 | SAIL     | 2025-03-26 | Before market open | Technology             | $12.1B       | $21.23  | nan%         | nan%         | nanx          |
| 22 | SURG     | 2025-03-25 | After market close | Communication Services | $27.8M       | $1.31   | nan%         | nan%         | nanx          |
| 23 | TH       | 2025-03-26 | Before market open | Industrials            | $606.5M      | $6.11   | nan%         | nan%         | nanx          |
| 24 | TOI      | 2025-03-25 | After market close | Healthcare             | $95.2M       | $1.24   | nan%         | nan%         | nanx          |
| 25 | TTAM     | 2025-03-26 | Before market open | nan                    | $2.5B        | $13.20  | nan%         | nan%         | nanx          |
| 26 | ZH       | 2025-03-26 | Before market open | Communication Services | $417.3M      | $4.70   | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
