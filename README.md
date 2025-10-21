# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-10-20 21:48:44 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector             | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | LMT      | 2025-10-21 | Before market open | Industrials        | $118.1B      | $495.15 | 14.01%       | 29.63%       | 2.11x         |
|  1 | GPC      | 2025-10-21 | Before market open | Consumer Cyclical  | $18.5B       | $133.10 | 16.95%       | 30.70%       | 1.81x         |
|  2 | MMM      | 2025-10-21 | Before market open | Industrials        | $82.4B       | $152.64 | 21.22%       | 38.34%       | 1.81x         |
|  3 | GE       | 2025-10-21 | Before market open | Industrials        | $321.0B      | $300.14 | 21.48%       | 38.46%       | 1.79x         |
|  4 | BMI      | 2025-10-21 | Before market open | Technology         | $5.5B        | $179.94 | 24.41%       | 43.44%       | 1.78x         |
|  5 | GM       | 2025-10-21 | Before market open | Consumer Cyclical  | $55.6B       | $58.38  | 22.94%       | 40.72%       | 1.78x         |
|  6 | ELV      | 2025-10-21 | Before market open | Healthcare         | $79.7B       | $348.77 | 26.03%       | 45.88%       | 1.76x         |
|  7 | CCK      | 2025-10-20 | After market close | Consumer Cyclical  | $11.0B       | $93.84  | 19.23%       | 33.61%       | 1.75x         |
|  8 | KO       | 2025-10-21 | Before market open | Consumer Defensive | $294.5B      | $68.44  | 12.35%       | 20.41%       | 1.65x         |
|  9 | PM       | 2025-10-21 | Before market open | Consumer Defensive | $246.0B      | $158.06 | 21.68%       | 35.39%       | 1.63x         |
| 10 | PNR      | 2025-10-21 | Before market open | Industrials        | $17.9B       | $108.79 | 19.81%       | 32.15%       | 1.62x         |
| 11 | GATX     | 2025-10-21 | Before market open | Industrials        | $6.2B        | $172.02 | 17.70%       | 28.23%       | 1.59x         |
| 12 | PFBC     | 2025-10-20 | After market close | Financial Services | $1.1B        | $85.31  | 23.62%       | 36.54%       | 1.55x         |
| 13 | NOC      | 2025-10-21 | Before market open | Industrials        | $86.2B       | $594.50 | 20.26%       | 28.89%       | 1.43x         |
| 14 | PCAR     | 2025-10-21 | Before market open | Industrials        | $51.2B       | $94.69  | 25.68%       | 35.83%       | 1.40x         |
| 15 | RLI      | 2025-10-20 | After market close | Financial Services | $5.5B        | $59.63  | 25.62%       | 34.82%       | 1.36x         |
| 16 | PHM      | 2025-10-21 | Before market open | Consumer Cyclical  | $24.6B       | $124.45 | 30.41%       | 41.26%       | 1.36x         |
| 17 | RTX      | 2025-10-21 | Before market open | Industrials        | $215.1B      | $157.95 | 22.12%       | 29.54%       | 1.34x         |
| 18 | VMI      | 2025-10-21 | Before market open | Industrials        | $8.1B        | $404.86 | 29.37%       | 38.75%       | 1.32x         |
| 19 | DGX      | 2025-10-21 | Before market open | Healthcare         | $21.3B       | $189.51 | 20.82%       | 27.21%       | 1.31x         |
| 20 | BCPC     | 2025-10-21 | Before market open | Basic Materials    | $4.9B        | $147.59 | 22.53%       | 29.44%       | 1.31x         |
| 21 | WTFC     | 2025-10-20 | After market close | Financial Services | $8.5B        | $122.74 | 29.47%       | 36.72%       | 1.25x         |
| 22 | CBU      | 2025-10-21 | Before market open | Financial Services | $3.0B        | $55.63  | 28.80%       | 35.82%       | 1.24x         |
| 23 | SFBS     | 2025-10-20 | After market close | Financial Services | $4.2B        | $75.21  | 30.88%       | 37.52%       | 1.22x         |
| 24 | HAL      | 2025-10-21 | Before market open | Energy             | $19.3B       | $22.27  | 37.23%       | 44.45%       | 1.19x         |
| 25 | NDAQ     | 2025-10-21 | Before market open | Financial Services | $51.0B       | $88.59  | 23.05%       | 27.11%       | 1.18x         |
| 26 | STLD     | 2025-10-20 | After market close | Basic Materials    | $21.5B       | $142.75 | 33.98%       | 39.50%       | 1.16x         |
| 27 | WRB      | 2025-10-20 | After market close | Financial Services | $28.1B       | $74.05  | 20.88%       | 24.02%       | 1.15x         |
| 28 | EFX      | 2025-10-21 | Before market open | Industrials        | $28.5B       | $226.91 | 36.41%       | 40.91%       | 1.12x         |
| 29 | DHR      | 2025-10-21 | Before market open | Healthcare         | $149.7B      | $209.06 | 36.15%       | 38.08%       | 1.05x         |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
