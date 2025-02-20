# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-02-19 20:38:52 EST

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | KAR      | 2025-02-19 | After market close | Consumer Cyclical      | $2.1B        | $20.12  | 23.98%       | 64.26%       | 2.68x         |
|  1 | RGR      | 2025-02-19 | After market close | Industrials            | $595.4M      | $35.11  | 15.44%       | 40.07%       | 2.60x         |
|  2 | MD       | 2025-02-20 | Before market open | Healthcare             | $1.2B        | $14.29  | 37.20%       | 91.97%       | 2.47x         |
|  3 | LOPE     | 2025-02-19 | After market close | Consumer Defensive     | $5.4B        | $185.52 | 13.84%       | 33.98%       | 2.46x         |
|  4 | SABR     | 2025-02-20 | Before market open | Technology             | $1.3B        | $3.52   | 33.19%       | 80.49%       | 2.43x         |
|  5 | OII      | 2025-02-19 | After market close | Energy                 | $2.5B        | $25.69  | 31.11%       | 68.83%       | 2.21x         |
|  6 | EPAM     | 2025-02-20 | Before market open | Technology             | $14.6B       | $260.91 | 23.09%       | 49.11%       | 2.13x         |
|  7 | LKQ      | 2025-02-20 | Before market open | Consumer Cyclical      | $10.2B       | $39.51  | 18.11%       | 38.01%       | 2.10x         |
|  8 | PRAA     | 2025-02-19 | After market close | Financial Services     | $932.8M      | $23.95  | 26.38%       | 55.13%       | 2.09x         |
|  9 | FCN      | 2025-02-20 | Before market open | Industrials            | $6.8B        | $188.39 | 19.66%       | 39.27%       | 2.00x         |
| 10 | KALU     | 2025-02-19 | After market close | Basic Materials        | $1.1B        | $71.30  | 26.72%       | 51.61%       | 1.93x         |
| 11 | TRUP     | 2025-02-19 | After market close | Financial Services     | $2.0B        | $48.69  | 44.37%       | 85.47%       | 1.93x         |
| 12 | HAS      | 2025-02-20 | Before market open | Consumer Cyclical      | $8.5B        | $61.25  | 21.00%       | 40.28%       | 1.92x         |
| 13 | MCW      | 2025-02-19 | After market close | Consumer Cyclical      | $2.4B        | $7.69   | 31.07%       | 58.74%       | 1.89x         |
| 14 | WMT      | 2025-02-20 | Before market open | Consumer Defensive     | $835.5B      | $103.78 | 16.28%       | 30.03%       | 1.84x         |
| 15 | UPBD     | 2025-02-20 | Before market open | Technology             | $1.6B        | $29.77  | 24.73%       | 44.00%       | 1.78x         |
| 16 | ANSS     | 2025-02-19 | After market close | Technology             | $29.4B       | $338.58 | 19.71%       | 34.61%       | 1.76x         |
| 17 | ITGR     | 2025-02-20 | Before market open | Healthcare             | $4.8B        | $141.15 | 18.43%       | 32.23%       | 1.75x         |
| 18 | CHDN     | 2025-02-19 | After market close | Consumer Cyclical      | $8.8B        | $121.58 | 17.86%       | 31.18%       | 1.75x         |
| 19 | ROG      | 2025-02-19 | After market close | Technology             | $1.7B        | $90.79  | 29.88%       | 50.94%       | 1.70x         |
| 20 | RGEN     | 2025-02-20 | Before market open | Healthcare             | $8.4B        | $145.18 | 35.72%       | 57.89%       | 1.62x         |
| 21 | JXN      | 2025-02-19 | After market close | Financial Services     | $6.9B        | $97.88  | 32.09%       | 50.92%       | 1.59x         |
| 22 | RS       | 2025-02-19 | After market close | Basic Materials        | $15.9B       | $299.38 | 20.83%       | 32.46%       | 1.56x         |
| 23 | BMRN     | 2025-02-19 | After market close | Healthcare             | $12.5B       | $64.86  | 26.02%       | 39.21%       | 1.51x         |
| 24 | SHEN     | 2025-02-20 | Before market open | Communication Services | $645.4M      | $11.97  | 40.05%       | 60.17%       | 1.50x         |
| 25 | VAL      | 2025-02-20 | Before market open | Energy                 | $3.0B        | $44.80  | 35.68%       | 52.86%       | 1.48x         |
| 26 | VTLE     | 2025-02-19 | After market close | Energy                 | $1.3B        | $34.87  | 41.41%       | 60.86%       | 1.47x         |
| 27 | CHH      | 2025-02-20 | Before market open | Consumer Cyclical      | $6.9B        | $149.19 | 21.24%       | 30.80%       | 1.45x         |
| 28 | NDSN     | 2025-02-19 | After market close | Industrials            | $12.4B       | $219.52 | 19.42%       | 27.98%       | 1.44x         |
| 29 | NVRI     | 2025-02-20 | Before market open | Industrials            | $699.6M      | $8.73   | 40.13%       | 57.70%       | 1.44x         |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
