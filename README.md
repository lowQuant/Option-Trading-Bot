# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-10-22 21:47:46 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | LNN      | 2025-10-23 | Before market open | Industrials            | $1.3B        | $128.85 | 18.59%       | 38.48%       | 2.07x         |
|  1 | VLY      | 2025-10-23 | Before market open | Financial Services     | $5.7B        | $10.26  | 36.80%       | 73.88%       | 2.01x         |
|  2 | WST      | 2025-10-23 | Before market open | Healthcare             | $19.9B       | $279.39 | 27.03%       | 54.22%       | 2.01x         |
|  3 | MEDP     | 2025-10-22 | After market close | Healthcare             | $15.4B       | $545.63 | 34.18%       | 65.53%       | 1.92x         |
|  4 | LUV      | 2025-10-22 | After market close | Industrials            | $17.7B       | $34.68  | 26.74%       | 51.03%       | 1.91x         |
|  5 | RS       | 2025-10-22 | After market close | Basic Materials        | $14.4B       | $278.65 | 18.75%       | 35.49%       | 1.89x         |
|  6 | DOV      | 2025-10-23 | Before market open | Industrials            | $23.0B       | $173.04 | 17.67%       | 33.36%       | 1.89x         |
|  7 | SMPL     | 2025-10-23 | Before market open | Consumer Defensive     | $2.5B        | $25.44  | 31.55%       | 58.98%       | 1.87x         |
|  8 | TMUS     | 2025-10-23 | Before market open | Communication Services | $256.2B      | $229.08 | 16.27%       | 30.16%       | 1.85x         |
|  9 | GGG      | 2025-10-22 | After market close | Industrials            | $13.5B       | $83.86  | 15.26%       | 27.98%       | 1.83x         |
| 10 | ALLE     | 2025-10-23 | Before market open | Industrials            | $15.1B       | $179.47 | 16.98%       | 30.91%       | 1.82x         |
| 11 | GSHD     | 2025-10-22 | After market close | Financial Services     | $2.5B        | $68.25  | 39.77%       | 72.03%       | 1.81x         |
| 12 | AN       | 2025-10-23 | Before market open | Consumer Cyclical      | $8.2B        | $218.70 | 21.34%       | 38.49%       | 1.80x         |
| 13 | WDFC     | 2025-10-22 | After market close | Basic Materials        | $2.7B        | $198.58 | 20.92%       | 37.68%       | 1.80x         |
| 14 | MRP      | 2025-10-23 | Before market open | Real Estate            | $5.4B        | $33.05  | 21.20%       | 37.48%       | 1.77x         |
| 15 | CCI      | 2025-10-22 | After market close | Real Estate            | $42.5B       | $98.65  | 16.24%       | 28.55%       | 1.76x         |
| 16 | TSCO     | 2025-10-23 | Before market open | Consumer Cyclical      | $29.3B       | $54.77  | 19.60%       | 34.10%       | 1.74x         |
| 17 | EEFT     | 2025-10-23 | Before market open | Technology             | $3.5B        | $89.12  | 25.52%       | 44.15%       | 1.73x         |
| 18 | MSM      | 2025-10-23 | Before market open | Industrials            | $4.8B        | $88.03  | 20.21%       | 34.63%       | 1.71x         |
| 19 | PKG      | 2025-10-22 | After market close | Consumer Cyclical      | $18.8B       | $208.13 | 17.66%       | 29.84%       | 1.69x         |
| 20 | UNP      | 2025-10-23 | Before market open | Industrials            | $133.6B      | $226.54 | 16.06%       | 27.05%       | 1.68x         |
| 21 | MOH      | 2025-10-22 | After market close | Healthcare             | $10.6B       | $196.80 | 35.30%       | 59.22%       | 1.68x         |
| 22 | POOL     | 2025-10-23 | Before market open | Industrials            | $11.1B       | $302.63 | 22.69%       | 37.01%       | 1.63x         |
| 23 | ELS      | 2025-10-22 | After market close | Real Estate            | $12.7B       | $62.94  | 13.77%       | 22.46%       | 1.63x         |
| 24 | CACI     | 2025-10-22 | After market close | Technology             | $11.4B       | $533.69 | 24.08%       | 38.71%       | 1.61x         |
| 25 | ORLY     | 2025-10-22 | After market close | Consumer Cyclical      | $86.1B       | $101.31 | 17.89%       | 28.73%       | 1.61x         |
| 26 | EPRT     | 2025-10-22 | After market close | Real Estate            | $6.2B        | $31.63  | 16.42%       | 26.28%       | 1.60x         |
| 27 | HAS      | 2025-10-23 | Before market open | Consumer Cyclical      | $10.5B       | $74.83  | 25.94%       | 41.45%       | 1.60x         |
| 28 | VC       | 2025-10-23 | Before market open | Consumer Cyclical      | $3.1B        | $116.86 | 26.93%       | 43.00%       | 1.60x         |
| 29 | RHI      | 2025-10-22 | After market close | Industrials            | $3.1B        | $30.98  | 34.55%       | 54.86%       | 1.59x         |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
