# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-08-27 21:46:53 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | BILL     | 2025-08-27 | After market close | Technology             | $4.3B        | $40.63  | 37.08%       | 80.41%       | 2.17x         |
|  1 | CRWD     | 2025-08-27 | After market close | Technology             | $105.3B      | $417.60 | 27.85%       | 51.21%       | 1.84x         |
|  2 | NTAP     | 2025-08-27 | After market close | Technology             | $22.4B       | $109.41 | 22.77%       | 40.99%       | 1.80x         |
|  3 | FIVE     | 2025-08-27 | After market close | Consumer Cyclical      | $8.0B        | $141.98 | 31.78%       | 56.66%       | 1.78x         |
|  4 | DG       | 2025-08-28 | Before market open | Consumer Defensive     | $24.5B       | $110.50 | 24.40%       | 43.46%       | 1.78x         |
|  5 | NVDA     | 2025-08-27 | After market close | Technology             | $4.4tr       | $181.77 | 26.15%       | 44.31%       | 1.69x         |
|  6 | BURL     | 2025-08-28 | Before market open | Consumer Cyclical      | $17.7B       | $279.05 | 29.01%       | 46.21%       | 1.59x         |
|  7 | COO      | 2025-08-27 | After market close | Healthcare             | $14.8B       | $73.66  | 25.88%       | 41.04%       | 1.59x         |
|  8 | OLLI     | 2025-08-28 | Before market open | Consumer Defensive     | $8.0B        | $130.49 | 30.99%       | 48.71%       | 1.57x         |
|  9 | PSTG     | 2025-08-27 | After market close | Technology             | $19.9B       | $58.56  | 42.29%       | 63.66%       | 1.51x         |
| 10 | DKS      | 2025-08-28 | Before market open | Consumer Cyclical      | $18.1B       | $226.81 | 29.51%       | 44.39%       | 1.50x         |
| 11 | URBN     | 2025-08-27 | After market close | Consumer Cyclical      | $7.0B        | $76.26  | 39.52%       | 59.44%       | 1.50x         |
| 12 | HRL      | 2025-08-28 | Before market open | Consumer Defensive     | $16.0B       | $28.76  | 18.66%       | 27.85%       | 1.49x         |
| 13 | HPQ      | 2025-08-27 | After market close | Technology             | $25.5B       | $27.01  | 27.43%       | 40.66%       | 1.48x         |
| 14 | BBWI     | 2025-08-28 | Before market open | Consumer Cyclical      | $6.7B        | $31.35  | 39.92%       | 56.15%       | 1.41x         |
| 15 | BBY      | 2025-08-28 | Before market open | Consumer Cyclical      | $15.9B       | $73.67  | 31.52%       | 43.70%       | 1.39x         |
| 16 | BF.B     | 2025-08-28 | Before market open | nan                    | N/A          | $nan    | 33.42%       | 44.71%       | 1.34x         |
| 17 | GEF      | 2025-08-27 | After market close | Consumer Cyclical      | $3.2B        | $66.33  | 22.96%       | 30.40%       | 1.32x         |
| 18 | VSCO     | 2025-08-28 | Before market open | Consumer Cyclical      | $1.8B        | $21.99  | 58.45%       | 76.01%       | 1.30x         |
| 19 | PAHC     | 2025-08-27 | After market close | Healthcare             | $1.3B        | $32.64  | 37.77%       | 45.97%       | 1.22x         |
| 20 | A        | 2025-08-27 | After market close | Healthcare             | $33.7B       | $118.30 | 33.57%       | 34.95%       | 1.04x         |
| 21 | ALAR     | 2025-08-28 | Before market open | Technology             | $119.3M      | $16.82  | nan%         | nan%         | nanx          |
| 22 | ARX      | 2025-08-28 | Before market open | Financial Services     | $6.4B        | $29.23  | nan%         | nan%         | nanx          |
| 23 | BBW      | 2025-08-28 | Before market open | Consumer Cyclical      | $773.5M      | $57.32  | nan%         | nan%         | nanx          |
| 24 | BF.A     | 2025-08-28 | Before market open | nan                    | N/A          | $nan    | nan%         | nan%         | nanx          |
| 25 | BZUN     | 2025-08-28 | Before market open | Consumer Cyclical      | $176.5M      | $3.01   | nan%         | nan%         | nanx          |
| 26 | CCG      | 2025-08-28 | Before market open | Communication Services | $69.2M       | $0.86   | nan%         | nan%         | nanx          |
| 27 | CLCO     | 2025-08-28 | Before market open | Energy                 | $412.4M      | $7.87   | nan%         | nan%         | nanx          |
| 28 | CM       | 2025-08-28 | Before market open | Financial Services     | $70.3B       | $73.81  | nan%         | nan%         | nanx          |
| 29 | CMBT     | 2025-08-28 | Before market open | Energy                 | $2.3B        | $8.54   | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
