# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-03-20 21:44:42 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | SCHL     | 2025-03-20 | After market close | Communication Services | $528.3M      | $19.15  | 52.99%       | 95.87%       | 1.81x         |
|  1 | FDX      | 2025-03-20 | After market close | Industrials            | $59.3B       | $247.12 | 27.64%       | 45.94%       | 1.66x         |
|  2 | LEN      | 2025-03-20 | After market close | Consumer Cyclical      | $31.6B       | $120.30 | 30.21%       | 45.96%       | 1.52x         |
|  3 | NKE      | 2025-03-20 | After market close | Consumer Cyclical      | $106.3B      | $72.99  | 37.09%       | 45.27%       | 1.22x         |
|  4 | CCL      | 2025-03-21 | Before market open | Consumer Cyclical      | $28.7B       | $21.05  | 53.36%       | 55.34%       | 1.04x         |
|  5 | MU       | 2025-03-20 | After market close | Technology             | $114.8B      | $102.06 | 61.95%       | 61.67%       | 1.00x         |
|  6 | AMPX     | 2025-03-20 | After market close | Industrials            | $255.4M      | $2.20   | nan%         | nan%         | nanx          |
|  7 | BFRI     | 2025-03-21 | Before market open | Healthcare             | $9.1M        | $1.04   | nan%         | nan%         | nanx          |
|  8 | CBUS     | 2025-03-20 | After market close | Healthcare             | $74.3M       | $2.37   | nan%         | nan%         | nanx          |
|  9 | CUK      | 2025-03-21 | Before market open | Consumer Cyclical      | $23.9B       | $18.99  | nan%         | nan%         | nanx          |
| 10 | CURV     | 2025-03-20 | After market close | Consumer Cyclical      | $579.3M      | $5.60   | nan%         | nan%         | nanx          |
| 11 | FLUX     | 2025-03-20 | After market close | Industrials            | $27.1M       | $1.62   | nan%         | nan%         | nanx          |
| 12 | IDN      | 2025-03-20 | After market close | Technology             | $50.4M       | $2.60   | nan%         | nan%         | nanx          |
| 13 | KLC      | 2025-03-20 | After market close | Consumer Defensive     | $2.1B        | $17.26  | nan%         | nan%         | nanx          |
| 14 | LAZR     | 2025-03-20 | After market close | Consumer Cyclical      | $209.1M      | $7.24   | nan%         | nan%         | nanx          |
| 15 | LEN.B    | 2025-03-20 | After market close | nan                    | N/A          | $nan    | nan%         | nan%         | nanx          |
| 16 | MGNX     | 2025-03-20 | After market close | Healthcare             | $131.8M      | $2.18   | nan%         | nan%         | nanx          |
| 17 | MNSO     | 2025-03-21 | Before market open | Consumer Cyclical      | $6.5B        | $21.79  | nan%         | nan%         | nanx          |
| 18 | NIO      | 2025-03-21 | Before market open | Consumer Cyclical      | $10.0B       | $5.17   | nan%         | nan%         | nanx          |
| 19 | OUST     | 2025-03-20 | After market close | Technology             | $433.9M      | $8.30   | nan%         | nan%         | nanx          |
| 20 | PL       | 2025-03-20 | After market close | Industrials            | $1.3B        | $4.32   | nan%         | nan%         | nanx          |
| 21 | QUBT     | 2025-03-20 | After market close | Technology             | $1.0B        | $8.37   | nan%         | nan%         | nanx          |
| 22 | RKDA     | 2025-03-20 | After market close | Consumer Defensive     | $4.5M        | $3.49   | nan%         | nan%         | nanx          |
| 23 | RWAY     | 2025-03-20 | After market close | Financial Services     | $399.6M      | $10.75  | nan%         | nan%         | nanx          |
| 24 | SOWG     | 2025-03-21 | Before market open | Consumer Defensive     | $28.2M       | $2.78   | nan%         | nan%         | nanx          |
| 25 | STG      | 2025-03-21 | Before market open | Consumer Defensive     | $76.6M       | $5.38   | nan%         | nan%         | nanx          |
| 26 | TELA     | 2025-03-20 | After market close | Healthcare             | $92.2M       | $2.36   | nan%         | nan%         | nanx          |
| 27 | TNON     | 2025-03-20 | After market close | Healthcare             | $3.5M        | $1.18   | nan%         | nan%         | nanx          |
| 28 | VXRT     | 2025-03-20 | After market close | Healthcare             | $129.1M      | $0.58   | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
