# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-08-04 22:10:17 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector             | market_cap   | close    | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-------------------|:-------------|:---------|:-------------|:-------------|:--------------|
|  0 | OTTR     | 2025-08-04 | After market close | Industrials        | $3.2B        | $75.29   | 19.48%       | 51.68%       | 2.65x         |
|  1 | NVRI     | 2025-08-05 | Before market open | Industrials        | $694.7M      | $8.60    | 31.83%       | 83.94%       | 2.64x         |
|  2 | MWA      | 2025-08-04 | After market close | Industrials        | $3.8B        | $24.24   | 21.96%       | 56.36%       | 2.57x         |
|  3 | FTDR     | 2025-08-05 | Before market open | Consumer Cyclical  | $4.3B        | $58.10   | 21.29%       | 52.25%       | 2.45x         |
|  4 | FOUR     | 2025-08-05 | Before market open | Technology         | $8.9B        | $101.94  | 25.01%       | 60.21%       | 2.41x         |
|  5 | DOCN     | 2025-08-05 | Before market open | Technology         | $2.5B        | $25.74   | 34.67%       | 80.79%       | 2.33x         |
|  6 | LDOS     | 2025-08-05 | Before market open | Technology         | $20.7B       | $159.20  | 16.34%       | 37.57%       | 2.30x         |
|  7 | HRMY     | 2025-08-05 | Before market open | Healthcare         | $2.0B        | $34.40   | 31.89%       | 71.07%       | 2.23x         |
|  8 | MD       | 2025-08-05 | Before market open | Healthcare         | $1.1B        | $11.98   | 30.49%       | 66.95%       | 2.20x         |
|  9 | BRBR     | 2025-08-04 | After market close | Consumer Defensive | $6.8B        | $54.11   | 27.14%       | 57.96%       | 2.14x         |
| 10 | AL       | 2025-08-04 | After market close | Industrials        | $6.2B        | $54.35   | 17.99%       | 38.33%       | 2.13x         |
| 11 | ZBRA     | 2025-08-05 | Before market open | Technology         | $17.4B       | $335.24  | 21.64%       | 45.55%       | 2.10x         |
| 12 | PRAA     | 2025-08-04 | After market close | Financial Services | $619.9M      | $15.06   | 32.73%       | 68.79%       | 2.10x         |
| 13 | ACM      | 2025-08-04 | After market close | Industrials        | $14.8B       | $111.08  | 14.55%       | 30.13%       | 2.07x         |
| 14 | ADUS     | 2025-08-04 | After market close | Healthcare         | $2.0B        | $104.96  | 21.94%       | 45.13%       | 2.06x         |
| 15 | ARMK     | 2025-08-05 | Before market open | Industrials        | $11.3B       | $42.49   | 15.25%       | 31.26%       | 2.05x         |
| 16 | ANDE     | 2025-08-04 | After market close | Consumer Defensive | $1.2B        | $34.69   | 26.22%       | 52.63%       | 2.01x         |
| 17 | IPGP     | 2025-08-05 | Before market open | Technology         | $3.3B        | $75.22   | 27.79%       | 55.60%       | 2.00x         |
| 18 | YOU      | 2025-08-05 | Before market open | Technology         | $4.0B        | $28.84   | 32.17%       | 63.60%       | 1.98x         |
| 19 | LSCC     | 2025-08-04 | After market close | Technology         | $6.7B        | $48.99   | 36.68%       | 70.85%       | 1.93x         |
| 20 | OGN      | 2025-08-05 | Before market open | Healthcare         | $2.5B        | $9.75    | 29.52%       | 56.98%       | 1.93x         |
| 21 | NPO      | 2025-08-05 | Before market open | Industrials        | $4.5B        | $209.91  | 21.24%       | 40.87%       | 1.92x         |
| 22 | INSP     | 2025-08-04 | After market close | Healthcare         | $3.8B        | $126.10  | 37.57%       | 70.92%       | 1.89x         |
| 23 | KD       | 2025-08-04 | After market close | Technology         | $8.5B        | $36.38   | 32.06%       | 60.49%       | 1.89x         |
| 24 | DORM     | 2025-08-04 | After market close | Consumer Cyclical  | $3.8B        | $119.13  | 20.96%       | 39.49%       | 1.88x         |
| 25 | BALL     | 2025-08-05 | Before market open | Consumer Cyclical  | $16.0B       | $57.14   | 17.33%       | 32.29%       | 1.86x         |
| 26 | TDG      | 2025-08-05 | Before market open | Industrials        | $90.4B       | $1585.00 | 15.19%       | 28.29%       | 1.86x         |
| 27 | IT       | 2025-08-05 | Before market open | Technology         | $25.9B       | $328.54  | 22.01%       | 40.57%       | 1.84x         |
| 28 | FIS      | 2025-08-05 | Before market open | Technology         | $41.5B       | $78.36   | 18.87%       | 34.52%       | 1.83x         |
| 29 | UFPT     | 2025-08-04 | After market close | Healthcare         | $1.7B        | $226.57  | 40.72%       | 73.97%       | 1.82x         |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
