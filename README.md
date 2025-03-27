# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-03-26 21:44:02 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | MLKN     | 2025-03-26 | After market close | Consumer Cyclical      | $1.3B        | $18.61  | 28.10%       | 67.81%       | 2.41x         |
|  1 | SNX      | 2025-03-27 | Before market open | Technology             | $10.7B       | $126.60 | 22.38%       | 36.39%       | 1.63x         |
|  2 | CNXC     | 2025-03-26 | After market close | Technology             | $2.9B        | $45.18  | 39.25%       | 62.81%       | 1.60x         |
|  3 | WGO      | 2025-03-27 | Before market open | Consumer Cyclical      | $987.1M      | $34.40  | 46.65%       | 68.37%       | 1.47x         |
|  4 | FUL      | 2025-03-26 | After market close | Basic Materials        | $2.9B        | $53.83  | 24.10%       | 26.94%       | 1.12x         |
|  5 | JEF      | 2025-03-26 | After market close | Financial Services     | $12.7B       | $61.70  | 40.50%       | 40.59%       | 1.00x         |
|  6 | AAPG     | 2025-03-27 | Before market open | Healthcare             | $1.6B        | $18.46  | nan%         | nan%         | nanx          |
|  7 | ADCT     | 2025-03-27 | Before market open | Healthcare             | $156.6M      | $1.62   | nan%         | nan%         | nanx          |
|  8 | ALVO     | 2025-03-26 | After market close | Healthcare             | $3.5B        | $11.66  | nan%         | nan%         | nanx          |
|  9 | BITF     | 2025-03-27 | Before market open | Financial Services     | $591.4M      | $1.06   | nan%         | nan%         | nanx          |
| 10 | BKTI     | 2025-03-27 | Before market open | Technology             | $104.4M      | $29.30  | nan%         | nan%         | nanx          |
| 11 | CATX     | 2025-03-26 | After market close | Healthcare             | $166.9M      | $2.47   | nan%         | nan%         | nanx          |
| 12 | DERM     | 2025-03-26 | After market close | Healthcare             | $135.4M      | $6.48   | nan%         | nan%         | nanx          |
| 13 | DRRX     | 2025-03-26 | After market close | Healthcare             | $26.3M       | $0.85   | nan%         | nan%         | nanx          |
| 14 | DYAI     | 2025-03-26 | After market close | Healthcare             | $40.8M       | $1.38   | nan%         | nan%         | nanx          |
| 15 | EDAP     | 2025-03-27 | Before market open | Healthcare             | $76.4M       | $2.18   | nan%         | nan%         | nanx          |
| 16 | ELA      | 2025-03-26 | After market close | Consumer Cyclical      | $154.4M      | $5.58   | nan%         | nan%         | nanx          |
| 17 | FGI      | 2025-03-26 | After market close | Consumer Cyclical      | $8.5M        | $0.89   | nan%         | nan%         | nanx          |
| 18 | GRDN     | 2025-03-26 | After market close | Healthcare             | $1.3B        | $20.33  | nan%         | nan%         | nanx          |
| 19 | IPHA     | 2025-03-27 | Before market open | Healthcare             | $165.5M      | $1.96   | nan%         | nan%         | nanx          |
| 20 | IVA      | 2025-03-26 | After market close | Healthcare             | $285.2M      | $2.89   | nan%         | nan%         | nanx          |
| 21 | JFIN     | 2025-03-27 | Before market open | Communication Services | $622.6M      | $11.74  | nan%         | nan%         | nanx          |
| 22 | MVIS     | 2025-03-26 | After market close | Technology             | $342.0M      | $1.52   | nan%         | nan%         | nanx          |
| 23 | PDSB     | 2025-03-27 | Before market open | Healthcare             | $58.9M       | $1.32   | nan%         | nan%         | nanx          |
| 24 | SCS      | 2025-03-26 | After market close | Consumer Cyclical      | $1.2B        | $10.58  | nan%         | nan%         | nanx          |
| 25 | SPRU     | 2025-03-26 | After market close | Technology             | $47.8M       | $2.57   | nan%         | nan%         | nanx          |
| 26 | TEN      | 2025-03-27 | Before market open | Energy                 | $491.6M      | $16.64  | nan%         | nan%         | nanx          |
| 27 | TLSI     | 2025-03-27 | Before market open | Healthcare             | $172.3M      | $5.65   | nan%         | nan%         | nanx          |
| 28 | UONE     | 2025-03-27 | Before market open | Communication Services | $44.0M       | $1.46   | nan%         | nan%         | nanx          |
| 29 | UONEK    | 2025-03-27 | Before market open | Communication Services | $44.0M       | $0.71   | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
