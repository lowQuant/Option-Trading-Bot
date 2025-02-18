# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-02-17 20:37:16 EST

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | BLKB     | 2025-02-18 | Before market open | Technology             | $4.1B        | $80.79  | 18.50%       | 35.92%       | 1.94x         |
|  1 | GPC      | 2025-02-18 | Before market open | Consumer Cyclical      | $17.4B       | $124.68 | 19.36%       | 34.62%       | 1.79x         |
|  2 | WSO      | 2025-02-18 | Before market open | Industrials            | $19.5B       | $476.50 | 18.94%       | 32.40%       | 1.71x         |
|  3 | VC       | 2025-02-18 | Before market open | Consumer Cyclical      | $2.3B        | $81.62  | 26.83%       | 42.32%       | 1.58x         |
|  4 | VMI      | 2025-02-18 | Before market open | Industrials            | $6.4B        | $323.04 | 24.09%       | 36.00%       | 1.49x         |
|  5 | FELE     | 2025-02-18 | Before market open | Industrials            | $4.6B        | $100.86 | 17.66%       | 25.32%       | 1.43x         |
|  6 | VMC      | 2025-02-18 | Before market open | Basic Materials        | $35.7B       | $269.33 | 20.46%       | 28.52%       | 1.39x         |
|  7 | TPH      | 2025-02-18 | Before market open | Consumer Cyclical      | $3.4B        | $35.98  | 29.82%       | 40.19%       | 1.35x         |
|  8 | ALLE     | 2025-02-18 | Before market open | Industrials            | $11.6B       | $133.15 | 21.68%       | 28.13%       | 1.30x         |
|  9 | CC       | 2025-02-18 | Before market open | Basic Materials        | $2.5B        | $17.79  | 49.82%       | 61.82%       | 1.24x         |
| 10 | EXPD     | 2025-02-18 | Before market open | Industrials            | $15.9B       | $112.74 | 20.92%       | 25.39%       | 1.21x         |
| 11 | ETR      | 2025-02-18 | Before market open | Utilities              | $35.4B       | $83.25  | 24.01%       | 27.29%       | 1.14x         |
| 12 | FLR      | 2025-02-18 | Before market open | Industrials            | $7.4B        | $44.93  | 60.53%       | 66.23%       | 1.09x         |
| 13 | DFIN     | 2025-02-18 | Before market open | Technology             | $1.9B        | $66.54  | 31.21%       | 33.42%       | 1.07x         |
| 14 | MDT      | 2025-02-18 | Before market open | Healthcare             | $119.0B      | $92.20  | 22.03%       | 20.80%       | 0.94x         |
| 15 | NEO      | 2025-02-18 | Before market open | Healthcare             | $1.9B        | $13.91  | 95.56%       | 55.72%       | 0.58x         |
| 16 | AXSM     | 2025-02-18 | Before market open | Healthcare             | $6.4B        | $131.68 | nan%         | nan%         | nanx          |
| 17 | BIDU     | 2025-02-18 | Before market open | Communication Services | $34.8B       | $96.59  | nan%         | nan%         | nanx          |
| 18 | GLDD     | 2025-02-18 | Before market open | Industrials            | $740.0M      | $11.12  | nan%         | nan%         | nanx          |
| 19 | HLMN     | 2025-02-18 | Before market open | Industrials            | $2.0B        | $10.43  | nan%         | nan%         | nanx          |
| 20 | IHG      | 2025-02-18 | Before market open | Consumer Cyclical      | $21.1B       | $134.91 | nan%         | nan%         | nanx          |
| 21 | IQ       | 2025-02-18 | Before market open | Communication Services | $2.4B        | $2.52   | nan%         | nan%         | nanx          |
| 22 | SOHU     | 2025-02-18 | Before market open | Communication Services | $484.8M      | $14.88  | nan%         | nan%         | nanx          |
| 23 | SPNS     | 2025-02-18 | Before market open | Technology             | $1.5B        | $26.85  | nan%         | nan%         | nanx          |
| 24 | WAY      | 2025-02-18 | Before market open | Healthcare             | $7.8B        | $44.70  | nan%         | nan%         | nanx          |
| 25 | WGS      | 2025-02-18 | Before market open | Healthcare             | $2.1B        | $78.00  | nan%         | nan%         | nanx          |
| 26 | WSO.B    | 2025-02-18 | Before market open | nan                    | N/A          | $nan    | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
