# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-07-21 22:04:20 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector             | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | BMI      | 2025-07-22 | Before market open | Technology         | $7.2B        | $244.37 | 14.96%       | 33.96%       | 2.27x         |
|  1 | CCK      | 2025-07-21 | After market close | Consumer Cyclical  | $12.2B       | $106.23 | 15.14%       | 32.59%       | 2.15x         |
|  2 | AGYS     | 2025-07-21 | After market close | Technology         | $3.3B        | $115.21 | 32.99%       | 68.90%       | 2.09x         |
|  3 | VMI      | 2025-07-22 | Before market open | Industrials        | $6.7B        | $335.65 | 19.01%       | 38.19%       | 2.01x         |
|  4 | CALX     | 2025-07-21 | After market close | Technology         | $3.5B        | $53.67  | 24.88%       | 48.75%       | 1.96x         |
|  5 | DGX      | 2025-07-22 | Before market open | Healthcare         | $18.6B       | $166.91 | 14.52%       | 28.22%       | 1.94x         |
|  6 | MEDP     | 2025-07-21 | After market close | Healthcare         | $8.9B        | $311.87 | 30.39%       | 56.12%       | 1.85x         |
|  7 | ABR      | 2025-07-21 | After market close | Real Estate        | $2.3B        | $11.21  | 26.76%       | 48.25%       | 1.80x         |
|  8 | EFX      | 2025-07-22 | Before market open | Industrials        | $32.2B       | $263.09 | 21.68%       | 38.69%       | 1.78x         |
|  9 | GPC      | 2025-07-22 | Before market open | Consumer Cyclical  | $17.2B       | $122.91 | 19.84%       | 33.73%       | 1.70x         |
| 10 | PM       | 2025-07-22 | Before market open | Consumer Defensive | $280.9B      | $178.73 | 19.32%       | 32.05%       | 1.66x         |
| 11 | IQV      | 2025-07-22 | Before market open | Healthcare         | $27.5B       | $160.63 | 26.98%       | 44.31%       | 1.64x         |
| 12 | PCAR     | 2025-07-22 | Before market open | Industrials        | $48.8B       | $93.68  | 20.40%       | 32.16%       | 1.58x         |
| 13 | MSCI     | 2025-07-22 | Before market open | Financial Services | $44.7B       | $577.94 | 20.93%       | 31.79%       | 1.52x         |
| 14 | GM       | 2025-07-22 | Before market open | Consumer Cyclical  | $51.2B       | $53.22  | 24.20%       | 36.73%       | 1.52x         |
| 15 | TRST     | 2025-07-21 | After market close | Financial Services | $670.8M      | $35.24  | 22.43%       | 33.91%       | 1.51x         |
| 16 | DHR      | 2025-07-22 | Before market open | Healthcare         | $134.6B      | $190.05 | 24.26%       | 36.17%       | 1.49x         |
| 17 | THC      | 2025-07-22 | Before market open | Healthcare         | $16.2B       | $175.06 | 29.80%       | 43.30%       | 1.45x         |
| 18 | WRB      | 2025-07-21 | After market close | Financial Services | $25.7B       | $68.75  | 18.89%       | 27.09%       | 1.43x         |
| 19 | NXPI     | 2025-07-21 | After market close | Technology         | $57.7B       | $225.90 | 30.48%       | 42.86%       | 1.41x         |
| 20 | PNR      | 2025-07-22 | Before market open | Industrials        | $17.3B       | $106.07 | 18.91%       | 26.45%       | 1.40x         |
| 21 | SYF      | 2025-07-22 | Before market open | Financial Services | $26.4B       | $70.04  | 24.18%       | 33.20%       | 1.37x         |
| 22 | KO       | 2025-07-22 | Before market open | Consumer Defensive | $301.6B      | $69.85  | 14.23%       | 19.50%       | 1.37x         |
| 23 | ZION     | 2025-07-21 | After market close | Financial Services | $8.4B        | $56.80  | 25.96%       | 34.50%       | 1.33x         |
| 24 | AVY      | 2025-07-22 | Before market open | Consumer Cyclical  | $14.0B       | $178.60 | 20.74%       | 27.55%       | 1.33x         |
| 25 | KEY      | 2025-07-22 | Before market open | Financial Services | $20.0B       | $18.50  | 22.43%       | 29.50%       | 1.32x         |
| 26 | RTX      | 2025-07-22 | Before market open | Industrials        | $202.5B      | $151.50 | 19.68%       | 25.72%       | 1.31x         |
| 27 | CBU      | 2025-07-22 | Before market open | Financial Services | $3.1B        | $58.43  | 26.25%       | 33.87%       | 1.29x         |
| 28 | RLI      | 2025-07-21 | After market close | Financial Services | $6.4B        | $70.25  | 19.16%       | 24.68%       | 1.29x         |
| 29 | HOPE     | 2025-07-22 | Before market open | Financial Services | $1.5B        | $11.39  | 28.65%       | 34.84%       | 1.22x         |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
