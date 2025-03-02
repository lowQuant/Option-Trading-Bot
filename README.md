# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-03-01 20:45:02 EST

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | FTRE     | 2025-03-03 | Before market open | Healthcare             | $1.2B        | $14.05  | 45.30%       | 94.96%       | 2.10x         |
|  1 | NABL     | 2025-03-03 | Before market open | Technology             | $1.9B        | $10.09  | 21.68%       | 42.04%       | 1.94x         |
|  2 | BLFS     | 2025-03-03 | Before market open | Healthcare             | $1.1B        | $23.58  | 37.69%       | 72.99%       | 1.94x         |
|  3 | TGTX     | 2025-03-03 | Before market open | Healthcare             | $4.7B        | $28.53  | 46.57%       | 79.25%       | 1.70x         |
|  4 | RC       | 2025-03-03 | Before market open | Real Estate            | $1.1B        | $6.80   | 25.50%       | 36.64%       | 1.44x         |
|  5 | CRC      | 2025-03-03 | Before market open | Energy                 | $4.1B        | $44.68  | 29.50%       | 41.95%       | 1.42x         |
|  6 | MSEX     | 2025-02-28 | After market close | Utilities              | $895.1M      | $51.05  | 29.67%       | 33.49%       | 1.13x         |
|  7 | AVDL     | 2025-03-03 | Before market open | Healthcare             | $762.2M      | $7.68   | nan%         | nan%         | nanx          |
|  8 | BUR      | 2025-03-03 | Before market open | Financial Services     | $3.4B        | $15.57  | nan%         | nan%         | nanx          |
|  9 | HUT      | 2025-03-03 | Before market open | Financial Services     | $1.4B        | $14.41  | nan%         | nan%         | nanx          |
| 10 | MITT     | 2025-03-03 | Before market open | Real Estate            | $223.4M      | $7.49   | nan%         | nan%         | nanx          |
| 11 | MRSN     | 2025-03-03 | Before market open | Healthcare             | $64.7M       | $0.50   | nan%         | nan%         | nanx          |
| 12 | NOMD     | 2025-03-03 | Before market open | Consumer Defensive     | $3.0B        | $18.61  | nan%         | nan%         | nanx          |
| 13 | NOVA     | 2025-03-03 | Before market open | Technology             | $207.4M      | $1.72   | nan%         | nan%         | nanx          |
| 14 | OCUL     | 2025-03-03 | Before market open | Healthcare             | $1.1B        | $6.94   | nan%         | nan%         | nanx          |
| 15 | SGRY     | 2025-03-03 | Before market open | Healthcare             | $3.1B        | $24.62  | nan%         | nan%         | nanx          |
| 16 | SNDX     | 2025-03-03 | Before market open | Healthcare             | $1.3B        | $15.28  | nan%         | nan%         | nanx          |
| 17 | SPHR     | 2025-03-03 | Before market open | Communication Services | $1.6B        | $43.00  | nan%         | nan%         | nanx          |
| 18 | STXS     | 2025-03-03 | Before market open | Healthcare             | $174.5M      | $2.17   | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
