# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-05-05 21:51:55 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector             | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | HRMY     | 2025-05-06 | Before market open | Healthcare         | $1.7B        | $30.32  | 34.45%       | 71.43%       | 2.07x         |
|  1 | MD       | 2025-05-06 | Before market open | Healthcare         | $1.1B        | $12.94  | 45.01%       | 78.54%       | 1.74x         |
|  2 | AHCO     | 2025-05-06 | Before market open | Healthcare         | $1.2B        | $8.78   | 61.46%       | 90.88%       | 1.48x         |
|  3 | ADUS     | 2025-05-05 | After market close | Healthcare         | $1.9B        | $105.00 | 29.69%       | 43.34%       | 1.46x         |
|  4 | CELH     | 2025-05-06 | Before market open | Consumer Defensive | $8.7B        | $34.46  | 50.54%       | 73.30%       | 1.45x         |
|  5 | KLG      | 2025-05-06 | Before market open | Consumer Defensive | $1.5B        | $17.93  | 36.74%       | 52.66%       | 1.43x         |
|  6 | AORT     | 2025-05-05 | After market close | Healthcare         | $1.0B        | $23.33  | 35.50%       | 49.79%       | 1.40x         |
|  7 | ENR      | 2025-05-06 | Before market open | Industrials        | $1.9B        | $26.44  | 30.04%       | 40.21%       | 1.34x         |
|  8 | VRTX     | 2025-05-05 | After market close | Healthcare         | $128.6B      | $501.15 | 23.87%       | 31.64%       | 1.33x         |
|  9 | LDOS     | 2025-05-06 | Before market open | Technology         | $19.0B       | $148.79 | 30.29%       | 39.97%       | 1.32x         |
| 10 | JJSF     | 2025-05-06 | Before market open | Consumer Defensive | $2.6B        | $129.28 | 28.87%       | 37.69%       | 1.31x         |
| 11 | KRYS     | 2025-05-06 | Before market open | Healthcare         | $4.7B        | $166.16 | 44.55%       | 57.64%       | 1.29x         |
| 12 | INSP     | 2025-05-05 | After market close | Healthcare         | $4.7B        | $159.81 | 56.13%       | 72.39%       | 1.29x         |
| 13 | CLX      | 2025-05-05 | After market close | Consumer Defensive | $17.0B       | $139.08 | 25.36%       | 31.93%       | 1.26x         |
| 14 | UFPT     | 2025-05-06 | Before market open | Healthcare         | $1.5B        | $202.21 | 56.55%       | 70.25%       | 1.24x         |
| 15 | INGR     | 2025-05-06 | Before market open | Consumer Defensive | $8.6B        | $132.44 | 26.97%       | 33.48%       | 1.24x         |
| 16 | OMCL     | 2025-05-06 | Before market open | Healthcare         | $1.4B        | $31.16  | 40.14%       | 49.49%       | 1.23x         |
| 17 | OGS      | 2025-05-05 | After market close | Utilities          | $4.7B        | $78.44  | 20.62%       | 25.17%       | 1.22x         |
| 18 | THS      | 2025-05-06 | Before market open | Consumer Defensive | $1.2B        | $23.72  | 49.72%       | 59.16%       | 1.19x         |
| 19 | XPEL     | 2025-05-06 | Before market open | Consumer Cyclical  | $826.0M      | $29.87  | 63.93%       | 75.74%       | 1.18x         |
| 20 | WEC      | 2025-05-06 | Before market open | Utilities          | $34.7B       | $108.62 | 19.35%       | 22.56%       | 1.17x         |
| 21 | NJR      | 2025-05-05 | After market close | Utilities          | $5.0B        | $49.52  | 19.86%       | 22.92%       | 1.15x         |
| 22 | HSII     | 2025-05-05 | After market close | Industrials        | $819.0M      | $39.71  | 39.28%       | 44.91%       | 1.14x         |
| 23 | NBIX     | 2025-05-05 | After market close | Healthcare         | $10.9B       | $109.68 | 52.28%       | 58.29%       | 1.11x         |
| 24 | BRBR     | 2025-05-05 | After market close | Consumer Defensive | $10.1B       | $78.92  | 37.71%       | 41.53%       | 1.10x         |
| 25 | OTTR     | 2025-05-05 | After market close | Industrials        | $3.4B        | $81.02  | 26.72%       | 29.38%       | 1.10x         |
| 26 | SBRA     | 2025-05-05 | After market close | Real Estate        | $4.1B        | $17.42  | 25.12%       | 27.47%       | 1.09x         |
| 27 | DORM     | 2025-05-05 | After market close | Consumer Cyclical  | $3.5B        | $115.27 | 37.43%       | 40.71%       | 1.09x         |
| 28 | LTC      | 2025-05-05 | After market close | Real Estate        | $1.6B        | $35.25  | 21.02%       | 22.42%       | 1.07x         |
| 29 | CBT      | 2025-05-05 | After market close | Basic Materials    | $4.2B        | $77.99  | 37.63%       | 39.92%       | 1.06x         |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
