# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-08-26 21:47:33 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | BOX      | 2025-08-26 | After market close | Technology             | $4.5B        | $31.42  | 18.55%       | 43.18%       | 2.33x         |
|  1 | OKTA     | 2025-08-26 | After market close | Technology             | $16.0B       | $91.36  | 34.75%       | 63.67%       | 1.83x         |
|  2 | PVH      | 2025-08-26 | After market close | Consumer Cyclical      | $4.0B        | $81.60  | 33.99%       | 54.91%       | 1.62x         |
|  3 | REX      | 2025-08-27 | Before market open | Basic Materials        | $1.0B        | $60.68  | 26.50%       | 40.37%       | 1.52x         |
|  4 | WSM      | 2025-08-27 | Before market open | Consumer Cyclical      | $24.3B       | $197.96 | 36.85%       | 53.38%       | 1.45x         |
|  5 | ANF      | 2025-08-27 | Before market open | Consumer Cyclical      | $4.6B        | $99.76  | 50.34%       | 71.90%       | 1.43x         |
|  6 | PLAB     | 2025-08-27 | Before market open | Technology             | $1.3B        | $22.07  | 41.27%       | 57.73%       | 1.40x         |
|  7 | DCI      | 2025-08-27 | Before market open | Industrials            | $8.8B        | $75.34  | 17.78%       | 23.04%       | 1.30x         |
|  8 | SJM      | 2025-08-27 | Before market open | Consumer Defensive     | $11.8B       | $111.55 | 23.52%       | 28.83%       | 1.23x         |
|  9 | KSS      | 2025-08-27 | Before market open | Consumer Cyclical      | $1.5B        | $13.95  | 127.88%      | 90.37%       | 0.71x         |
| 10 | GES      | 2025-08-27 | Before market open | Consumer Cyclical      | $876.5M      | $16.80  | 78.11%       | 31.20%       | 0.40x         |
| 11 | DXLG     | 2025-08-27 | Before market open | Consumer Cyclical      | $70.0M       | $1.33   | nan%         | nan%         | nanx          |
| 12 | ELMD     | 2025-08-26 | After market close | Healthcare             | $173.3M      | $20.20  | nan%         | nan%         | nanx          |
| 13 | HAFN     | 2025-08-27 | Before market open | Industrials            | $2.9B        | $5.91   | nan%         | nan%         | nanx          |
| 14 | JOYY     | 2025-08-26 | After market close | Communication Services | $2.7B        | $52.54  | nan%         | nan%         | nanx          |
| 15 | MCFT     | 2025-08-27 | Before market open | Consumer Cyclical      | $347.0M      | $21.35  | nan%         | nan%         | nanx          |
| 16 | MDB      | 2025-08-26 | After market close | Technology             | $17.5B       | $218.44 | nan%         | nan%         | nanx          |
| 17 | NCNO     | 2025-08-26 | After market close | Technology             | $3.3B        | $28.37  | nan%         | nan%         | nanx          |
| 18 | OOMA     | 2025-08-26 | After market close | Technology             | $337.3M      | $11.98  | nan%         | nan%         | nanx          |
| 19 | RY       | 2025-08-27 | Before market open | Financial Services     | $194.7B      | $136.23 | nan%         | nan%         | nanx          |
| 20 | TIGR     | 2025-08-27 | Before market open | Financial Services     | $2.3B        | $12.70  | nan%         | nan%         | nanx          |
| 21 | TUYA     | 2025-08-26 | After market close | Technology             | $1.6B        | $2.56   | nan%         | nan%         | nanx          |
| 22 | YB       | 2025-08-27 | Before market open | Technology             | $1.3B        | $29.43  | nan%         | nan%         | nanx          |
| 23 | ZH       | 2025-08-27 | Before market open | Communication Services | $409.9M      | $4.80   | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
