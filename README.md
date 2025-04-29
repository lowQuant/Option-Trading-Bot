# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-04-28 21:50:21 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector             | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | HLIT     | 2025-04-28 | After market close | Technology         | $1.1B        | $9.21   | 51.52%       | 89.55%       | 1.74x         |
|  1 | OPCH     | 2025-04-29 | Before market open | Healthcare         | $5.4B        | $32.90  | 31.04%       | 50.35%       | 1.62x         |
|  2 | EZPW     | 2025-04-28 | After market close | Financial Services | $898.8M      | $16.32  | 31.42%       | 42.06%       | 1.34x         |
|  3 | NEO      | 2025-04-29 | Before market open | Healthcare         | $1.3B        | $10.27  | 56.69%       | 75.31%       | 1.33x         |
|  4 | NSP      | 2025-04-29 | Before market open | Industrials        | $3.0B        | $79.00  | 39.82%       | 50.95%       | 1.28x         |
|  5 | CDP      | 2025-04-28 | After market close | Real Estate        | $3.0B        | $26.36  | 25.72%       | 29.96%       | 1.16x         |
|  6 | MO       | 2025-04-29 | Before market open | Consumer Defensive | $98.9B       | $58.26  | 22.17%       | 24.36%       | 1.10x         |
|  7 | AOS      | 2025-04-29 | Before market open | Industrials        | $9.3B        | $64.99  | 30.12%       | 31.92%       | 1.06x         |
|  8 | REGN     | 2025-04-29 | Before market open | Healthcare         | $66.5B       | $602.64 | 39.60%       | 41.18%       | 1.04x         |
|  9 | LEG      | 2025-04-28 | After market close | Consumer Cyclical  | $998.6M      | $7.29   | 63.66%       | 65.37%       | 1.03x         |
| 10 | ETR      | 2025-04-29 | Before market open | Utilities          | $36.8B       | $84.61  | 31.92%       | 32.73%       | 1.03x         |
| 11 | CVLT     | 2025-04-29 | Before market open | Technology         | $7.3B        | $165.51 | 68.90%       | 69.64%       | 1.01x         |
| 12 | FOUR     | 2025-04-29 | Before market open | Technology         | $7.1B        | $80.28  | 61.45%       | 61.63%       | 1.00x         |
| 13 | SSD      | 2025-04-28 | After market close | Basic Materials    | $6.5B        | $153.54 | 43.45%       | 43.49%       | 1.00x         |
| 14 | PFE      | 2025-04-29 | Before market open | Healthcare         | $130.7B      | $22.92  | 30.93%       | 30.87%       | 1.00x         |
| 15 | SYY      | 2025-04-29 | Before market open | Consumer Defensive | $35.2B       | $70.93  | 32.13%       | 31.93%       | 0.99x         |
| 16 | WM       | 2025-04-28 | After market close | Industrials        | $92.2B       | $228.31 | 23.95%       | 23.77%       | 0.99x         |
| 17 | LGIH     | 2025-04-29 | Before market open | Consumer Cyclical  | $1.4B        | $59.45  | 62.51%       | 61.60%       | 0.99x         |
| 18 | EAT      | 2025-04-29 | Before market open | Consumer Cyclical  | $7.1B        | $159.65 | 62.93%       | 61.81%       | 0.98x         |
| 19 | KHC      | 2025-04-29 | Before market open | Consumer Defensive | $34.6B       | $29.49  | 30.39%       | 29.67%       | 0.98x         |
| 20 | INCY     | 2025-04-29 | Before market open | Healthcare         | $11.5B       | $59.16  | 45.45%       | 44.36%       | 0.98x         |
| 21 | UFPI     | 2025-04-28 | After market close | Basic Materials    | $6.6B        | $106.74 | 36.91%       | 35.22%       | 0.95x         |
| 22 | PJT      | 2025-04-29 | Before market open | Financial Services | $5.3B        | $134.67 | 45.44%       | 43.26%       | 0.95x         |
| 23 | ECL      | 2025-04-29 | Before market open | Basic Materials    | $68.2B       | $238.14 | 29.54%       | 27.98%       | 0.95x         |
| 24 | FFIV     | 2025-04-28 | After market close | Technology         | $15.3B       | $270.03 | 46.77%       | 44.11%       | 0.94x         |
| 25 | FELE     | 2025-04-29 | Before market open | Industrials        | $4.1B        | $89.17  | 37.93%       | 35.74%       | 0.94x         |
| 26 | CBU      | 2025-04-29 | Before market open | Financial Services | $2.9B        | $55.23  | 39.60%       | 37.26%       | 0.94x         |
| 27 | ABG      | 2025-04-29 | Before market open | Consumer Cyclical  | $4.4B        | $223.54 | 50.12%       | 46.72%       | 0.93x         |
| 28 | WELL     | 2025-04-28 | After market close | Real Estate        | $97.6B       | $146.96 | 30.49%       | 28.25%       | 0.93x         |
| 29 | CCK      | 2025-04-28 | After market close | Consumer Cyclical  | $10.5B       | $89.31  | 38.05%       | 35.19%       | 0.92x         |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
