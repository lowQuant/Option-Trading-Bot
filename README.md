# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-03-03 20:42:05 EST

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close    | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:---------|:-------------|:-------------|:--------------|
|  0 | NATL     | 2025-03-03 | After market close | Technology             | $1.9B        | $28.44   | 20.76%       | 52.64%       | 2.54x         |
|  1 | ADMA     | 2025-03-03 | After market close | Healthcare             | $3.7B        | $16.39   | 33.27%       | 77.36%       | 2.33x         |
|  2 | HSII     | 2025-03-03 | After market close | Industrials            | $808.4M      | $40.99   | 17.83%       | 37.58%       | 2.11x         |
|  3 | BBY      | 2025-03-04 | Before market open | Consumer Cyclical      | $18.5B       | $89.91   | 26.44%       | 48.05%       | 1.82x         |
|  4 | TGT      | 2025-03-04 | Before market open | Consumer Defensive     | $55.3B       | $124.24  | 27.47%       | 45.71%       | 1.66x         |
|  5 | AZO      | 2025-03-04 | Before market open | Consumer Cyclical      | $58.4B       | $3493.01 | 17.65%       | 27.40%       | 1.55x         |
|  6 | CON      | 2025-03-03 | After market close | Healthcare             | $2.8B        | $22.58   | 30.61%       | 43.55%       | 1.42x         |
|  7 | WSR      | 2025-03-03 | After market close | Real Estate            | $696.6M      | $13.57   | 15.50%       | 20.99%       | 1.35x         |
|  8 | AMLX     | 2025-03-04 | Before market open | Healthcare             | $257.1M      | $3.28    | nan%         | nan%         | nanx          |
|  9 | AOMR     | 2025-03-04 | Before market open | Real Estate            | $224.8M      | $9.97    | nan%         | nan%         | nanx          |
| 10 | BDSX     | 2025-03-03 | After market close | Healthcare             | $103.7M      | $0.79    | nan%         | nan%         | nanx          |
| 11 | BRCC     | 2025-03-03 | After market close | Consumer Defensive     | $198.6M      | $2.58    | nan%         | nan%         | nanx          |
| 12 | CGEN     | 2025-03-04 | Before market open | Healthcare             | $165.9M      | $1.92    | nan%         | nan%         | nanx          |
| 13 | CRD.A    | 2025-03-03 | After market close | nan                    | N/A          | $nan     | nan%         | nan%         | nanx          |
| 14 | CRD.B    | 2025-03-03 | After market close | nan                    | N/A          | $nan     | nan%         | nan%         | nanx          |
| 15 | DAVE     | 2025-03-03 | After market close | Technology             | $1.2B        | $100.66  | nan%         | nan%         | nanx          |
| 16 | DSP      | 2025-03-03 | After market close | Technology             | $1.2B        | $19.99   | nan%         | nan%         | nanx          |
| 17 | EBS      | 2025-03-03 | After market close | Healthcare             | $370.1M      | $7.48    | nan%         | nan%         | nanx          |
| 18 | EKSO     | 2025-03-03 | After market close | Healthcare             | $10.6M       | $0.52    | nan%         | nan%         | nanx          |
| 19 | ESPR     | 2025-03-04 | Before market open | Healthcare             | $311.3M      | $1.70    | nan%         | nan%         | nanx          |
| 20 | EVGO     | 2025-03-04 | Before market open | Consumer Cyclical      | $732.1M      | $2.65    | nan%         | nan%         | nanx          |
| 21 | EXOD     | 2025-03-03 | After market close | Technology             | $1.1B        | $42.20   | nan%         | nan%         | nanx          |
| 22 | FSCO     | 2025-03-03 | After market close | Financial Services     | $1.4B        | $6.98    | nan%         | nan%         | nanx          |
| 23 | FSTR     | 2025-03-04 | Before market open | Industrials            | $281.1M      | $27.45   | nan%         | nan%         | nanx          |
| 24 | GCT      | 2025-03-03 | After market close | Technology             | $657.1M      | $16.93   | nan%         | nan%         | nanx          |
| 25 | GENI     | 2025-03-04 | Before market open | Communication Services | $1.9B        | $8.68    | nan%         | nan%         | nanx          |
| 26 | GTLB     | 2025-03-03 | After market close | Technology             | $9.1B        | $60.21   | nan%         | nan%         | nanx          |
| 27 | GUTS     | 2025-03-03 | After market close | Healthcare             | $75.0M       | $1.56    | nan%         | nan%         | nanx          |
| 28 | HGTY     | 2025-03-04 | Before market open | Financial Services     | $3.4B        | $10.12   | nan%         | nan%         | nanx          |
| 29 | INFU     | 2025-03-04 | Before market open | Healthcare             | $154.4M      | $7.98    | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
