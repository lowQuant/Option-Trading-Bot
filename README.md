# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-12-03 20:56:58 EST

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | GWRE     | 2025-12-03 | After market close | Technology             | $18.3B       | $214.72 | 25.37%       | 54.49%       | 2.15x         |
|  1 | FIVE     | 2025-12-03 | After market close | Consumer Cyclical      | $9.0B        | $158.90 | 31.90%       | 60.72%       | 1.90x         |
|  2 | SAIC     | 2025-12-04 | Before market open | Technology             | $4.1B        | $87.56  | 27.98%       | 47.46%       | 1.70x         |
|  3 | HQY      | 2025-12-03 | After market close | Healthcare             | $8.5B        | $98.88  | 31.26%       | 49.83%       | 1.59x         |
|  4 | BF.B     | 2025-12-04 | Before market open | nan                    | N/A          | $nan    | 27.96%       | 43.31%       | 1.55x         |
|  5 | REX      | 2025-12-04 | Before market open | Basic Materials        | $1.1B        | $33.69  | 27.67%       | 42.49%       | 1.54x         |
|  6 | DG       | 2025-12-04 | Before market open | Consumer Defensive     | $24.2B       | $110.03 | 29.84%       | 44.96%       | 1.51x         |
|  7 | DCI      | 2025-12-04 | Before market open | Industrials            | $10.2B       | $88.16  | 18.27%       | 27.43%       | 1.50x         |
|  8 | CRM      | 2025-12-03 | After market close | Technology             | $228.2B      | $234.71 | 30.81%       | 44.72%       | 1.45x         |
|  9 | PVH      | 2025-12-03 | After market close | Consumer Cyclical      | $4.2B        | $84.74  | 39.70%       | 56.04%       | 1.41x         |
| 10 | WLY      | 2025-12-04 | Before market open | Communication Services | $2.0B        | $36.85  | 32.96%       | 44.82%       | 1.36x         |
| 11 | KR       | 2025-12-04 | Before market open | Consumer Defensive     | $43.9B       | $67.03  | 24.19%       | 32.29%       | 1.33x         |
| 12 | HRL      | 2025-12-04 | Before market open | Consumer Defensive     | $12.8B       | $23.09  | 32.10%       | 30.51%       | 0.95x         |
| 13 | AI       | 2025-12-03 | After market close | Technology             | $2.1B        | $14.37  | nan%         | nan%         | nanx          |
| 14 | BBW      | 2025-12-04 | Before market open | Consumer Cyclical      | $758.2M      | $52.42  | nan%         | nan%         | nanx          |
| 15 | BETA     | 2025-12-04 | Before market open | Industrials            | $7.0B        | $28.37  | nan%         | nan%         | nanx          |
| 16 | BF.A     | 2025-12-04 | Before market open | nan                    | N/A          | $nan    | nan%         | nan%         | nanx          |
| 17 | BMO      | 2025-12-04 | Before market open | Financial Services     | $91.7B       | $125.74 | nan%         | nan%         | nanx          |
| 18 | CM       | 2025-12-04 | Before market open | Financial Services     | $80.7B       | $86.59  | nan%         | nan%         | nanx          |
| 19 | CRMT     | 2025-12-04 | Before market open | Consumer Cyclical      | $193.5M      | $21.92  | nan%         | nan%         | nanx          |
| 20 | CURV     | 2025-12-03 | After market close | Consumer Cyclical      | $129.9M      | $1.32   | nan%         | nan%         | nanx          |
| 21 | DOOO     | 2025-12-04 | Before market open | Consumer Cyclical      | $5.2B        | $69.41  | nan%         | nan%         | nanx          |
| 22 | DSGX     | 2025-12-03 | After market close | Technology             | $7.1B        | $82.51  | nan%         | nan%         | nanx          |
| 23 | DXLG     | 2025-12-04 | Before market open | Consumer Cyclical      | $57.7M       | $0.96   | nan%         | nan%         | nanx          |
| 24 | GCO      | 2025-12-04 | Before market open | Consumer Cyclical      | $380.5M      | $35.40  | nan%         | nan%         | nanx          |
| 25 | HOV      | 2025-12-04 | Before market open | Consumer Cyclical      | $789.4M      | $129.48 | nan%         | nan%         | nanx          |
| 26 | NCNO     | 2025-12-03 | After market close | Technology             | $3.0B        | $24.46  | nan%         | nan%         | nanx          |
| 27 | NOTV     | 2025-12-03 | After market close | Healthcare             | $32.3M       | $0.87   | nan%         | nan%         | nanx          |
| 28 | PATH     | 2025-12-03 | After market close | Technology             | $8.0B        | $14.30  | nan%         | nan%         | nanx          |
| 29 | SNOW     | 2025-12-03 | After market close | Technology             | $89.8B       | $259.68 | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
