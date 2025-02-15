# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-02-14 20:36:07 EST

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | GPC      | 2025-02-18 | Before market open | Consumer Cyclical      | $17.4B       | $124.68 | 19.43%       | 39.84%       | 2.05x         |
|  1 | BLKB     | 2025-02-18 | Before market open | Technology             | $4.1B        | $80.79  | 18.02%       | 33.82%       | 1.88x         |
|  2 | WSO      | 2025-02-18 | Before market open | Industrials            | $19.5B       | $476.50 | 18.46%       | 34.05%       | 1.84x         |
|  3 | TPH      | 2025-02-18 | Before market open | Consumer Cyclical      | $3.4B        | $35.98  | 29.75%       | 53.45%       | 1.80x         |
|  4 | VC       | 2025-02-18 | Before market open | Consumer Cyclical      | $2.3B        | $81.62  | 26.08%       | 44.04%       | 1.69x         |
|  5 | VMI      | 2025-02-18 | Before market open | Industrials            | $6.4B        | $323.04 | 23.97%       | 35.21%       | 1.47x         |
|  6 | VMC      | 2025-02-18 | Before market open | Basic Materials        | $35.7B       | $269.33 | 20.50%       | 29.31%       | 1.43x         |
|  7 | FELE     | 2025-02-18 | Before market open | Industrials            | $4.6B        | $100.86 | 17.43%       | 24.34%       | 1.40x         |
|  8 | CC       | 2025-02-18 | Before market open | Basic Materials        | $2.7B        | $17.79  | 46.98%       | 64.15%       | 1.37x         |
|  9 | ALLE     | 2025-02-18 | Before market open | Industrials            | $11.6B       | $133.15 | 21.69%       | 29.31%       | 1.35x         |
| 10 | ETR      | 2025-02-18 | Before market open | Utilities              | $35.7B       | $83.25  | 23.75%       | 27.98%       | 1.18x         |
| 11 | DFIN     | 2025-02-18 | Before market open | Technology             | $1.9B        | $66.54  | 31.05%       | 33.20%       | 1.07x         |
| 12 | MDT      | 2025-02-18 | Before market open | Healthcare             | $119.0B      | $92.20  | 22.03%       | 21.62%       | 0.98x         |
| 13 | FLR      | 2025-02-18 | Before market open | Industrials            | $7.7B        | $44.93  | 59.84%       | 54.92%       | 0.92x         |
| 14 | NEO      | 2025-02-18 | Before market open | Healthcare             | $1.9B        | $13.91  | 94.97%       | 55.03%       | 0.58x         |
| 15 | AXSM     | 2025-02-18 | Before market open | Healthcare             | $6.4B        | $131.68 | nan%         | nan%         | nanx          |
| 16 | BIDU     | 2025-02-18 | Before market open | Communication Services | $34.2B       | $96.59  | nan%         | nan%         | nanx          |
| 17 | HLMN     | 2025-02-18 | Before market open | Industrials            | $2.1B        | $10.43  | nan%         | nan%         | nanx          |
| 18 | IHG      | 2025-02-18 | Before market open | Consumer Cyclical      | $21.1B       | $134.91 | nan%         | nan%         | nanx          |
| 19 | IQ       | 2025-02-18 | Before market open | Communication Services | $2.4B        | $2.52   | nan%         | nan%         | nanx          |
| 20 | SPNS     | 2025-02-18 | Before market open | Technology             | $1.5B        | $26.85  | nan%         | nan%         | nanx          |
| 21 | WAY      | 2025-02-18 | Before market open | Healthcare             | $7.8B        | $44.70  | nan%         | nan%         | nanx          |
| 22 | WGS      | 2025-02-18 | Before market open | Healthcare             | $2.1B        | $78.00  | nan%         | nan%         | nanx          |
| 23 | WSO.B    | 2025-02-18 | Before market open | nan                    | N/A          | $nan    | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
