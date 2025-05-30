# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-05-29 21:51:19 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector             | market_cap   | close    | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-------------------|:-------------|:---------|:-------------|:-------------|:--------------|
|  0 | NTAP     | 2025-05-29 | After market close | Technology         | $20.6B       | $99.67   | 26.32%       | 46.05%       | 1.75x         |
|  1 | COO      | 2025-05-29 | After market close | Healthcare         | $16.0B       | $80.12   | 24.45%       | 41.15%       | 1.68x         |
|  2 | GAP      | 2025-05-29 | After market close | Consumer Cyclical  | $10.6B       | $28.24   | 41.34%       | 67.23%       | 1.63x         |
|  3 | ULTA     | 2025-05-29 | After market close | Consumer Cyclical  | $19.0B       | $417.01  | 28.39%       | 41.54%       | 1.46x         |
|  4 | DELL     | 2025-05-29 | After market close | Technology         | $77.8B       | $113.77  | 39.29%       | 56.33%       | 1.43x         |
|  5 | COST     | 2025-05-29 | After market close | Consumer Defensive | $449.5B      | $1013.14 | 19.83%       | 26.05%       | 1.31x         |
|  6 | AEO      | 2025-05-29 | After market close | Consumer Cyclical  | $1.9B        | $11.09   | 53.44%       | 65.66%       | 1.23x         |
|  7 | SCVL     | 2025-05-30 | Before market open | Consumer Cyclical  | $521.8M      | $19.09   | 53.34%       | 64.70%       | 1.21x         |
|  8 | AMBA     | 2025-05-29 | After market close | Technology         | $2.6B        | $62.40   | nan%         | nan%         | nanx          |
|  9 | CGC      | 2025-05-30 | Before market open | Healthcare         | $323.6M      | $1.77    | nan%         | nan%         | nanx          |
| 10 | ESTC     | 2025-05-29 | After market close | Technology         | $9.6B        | $92.37   | nan%         | nan%         | nanx          |
| 11 | MRVL     | 2025-05-29 | After market close | Technology         | $55.8B       | $64.59   | nan%         | nan%         | nanx          |
| 12 | NGL      | 2025-05-29 | After market close | Energy             | $455.4M      | $3.45    | nan%         | nan%         | nanx          |
| 13 | PATH     | 2025-05-29 | After market close | Technology         | $6.9B        | $12.94   | nan%         | nan%         | nanx          |
| 14 | PD       | 2025-05-29 | After market close | Technology         | $1.5B        | $16.00   | nan%         | nan%         | nanx          |
| 15 | RRGB     | 2025-05-29 | After market close | Consumer Cyclical  | $59.2M       | $3.34    | nan%         | nan%         | nanx          |
| 16 | TIGR     | 2025-05-30 | Before market open | Financial Services | $1.5B        | $8.54    | nan%         | nan%         | nanx          |
| 17 | YTRA     | 2025-05-30 | Before market open | Consumer Cyclical  | $56.3M       | $0.90    | nan%         | nan%         | nanx          |
| 18 | ZS       | 2025-05-29 | After market close | Technology         | $39.2B       | $253.65  | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
