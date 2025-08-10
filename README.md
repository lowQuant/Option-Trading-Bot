# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-08-09 22:11:39 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | CEVA     | 2025-08-11 | Before market open | Technology             | $519.5M      | $21.18  | 35.57%       | 67.68%       | 1.90x         |
|  1 | OMI      | 2025-08-11 | Before market open | Healthcare             | $543.2M      | $6.31   | 65.20%       | 114.02%      | 1.75x         |
|  2 | ROIV     | 2025-08-11 | Before market open | Healthcare             | $7.8B        | $11.55  | 25.24%       | 42.43%       | 1.68x         |
|  3 | TDS      | 2025-08-11 | Before market open | Communication Services | $4.4B        | $38.27  | 40.14%       | 50.01%       | 1.25x         |
|  4 | AGEN     | 2025-08-11 | Before market open | Healthcare             | $131.6M      | $4.76   | nan%         | nan%         | nanx          |
|  5 | AIOT     | 2025-08-11 | Before market open | Technology             | $516.4M      | $3.97   | nan%         | nan%         | nanx          |
|  6 | B        | 2025-08-11 | Before market open | Basic Materials        | $40.3B       | $23.07  | nan%         | nan%         | nanx          |
|  7 | BHST     | 2025-08-11 | Before market open | Consumer Defensive     | $151.8M      | $8.10   | nan%         | nan%         | nanx          |
|  8 | BLDP     | 2025-08-11 | Before market open | Industrials            | $545.8M      | $1.85   | nan%         | nan%         | nanx          |
|  9 | CEPU     | 2025-08-11 | Before market open | Utilities              | $1.9B        | $12.96  | nan%         | nan%         | nanx          |
| 10 | DOLE     | 2025-08-11 | Before market open | Consumer Defensive     | $1.4B        | $14.59  | nan%         | nan%         | nanx          |
| 11 | EDRY     | 2025-08-11 | Before market open | Industrials            | $28.5M       | $10.52  | nan%         | nan%         | nanx          |
| 12 | EE       | 2025-08-11 | Before market open | Energy                 | $2.8B        | $24.42  | nan%         | nan%         | nanx          |
| 13 | FNV      | 2025-08-11 | Before market open | Basic Materials        | $33.1B       | $171.46 | nan%         | nan%         | nanx          |
| 14 | FSTR     | 2025-08-11 | Before market open | Industrials            | $233.1M      | $22.50  | nan%         | nan%         | nanx          |
| 15 | GPRE     | 2025-08-11 | Before market open | Basic Materials        | $484.0M      | $7.31   | nan%         | nan%         | nanx          |
| 16 | HBIO     | 2025-08-11 | Before market open | Healthcare             | $23.3M       | $0.51   | nan%         | nan%         | nanx          |
| 17 | HUMA     | 2025-08-11 | Before market open | Healthcare             | $384.7M      | $2.47   | nan%         | nan%         | nanx          |
| 18 | KGEI     | 2025-08-11 | Before market open | Energy                 | $215.6M      | $6.06   | nan%         | nan%         | nanx          |
| 19 | KPTI     | 2025-08-11 | Before market open | Healthcare             | $34.0M       | $3.97   | nan%         | nan%         | nanx          |
| 20 | KYMR     | 2025-08-11 | Before market open | Healthcare             | $2.8B        | $40.85  | nan%         | nan%         | nanx          |
| 21 | LAR      | 2025-08-11 | Before market open | Basic Materials        | $455.0M      | $2.69   | nan%         | nan%         | nanx          |
| 22 | LEGN     | 2025-08-11 | Before market open | Healthcare             | $6.8B        | $37.43  | nan%         | nan%         | nanx          |
| 23 | LINC     | 2025-08-11 | Before market open | Consumer Defensive     | $750.3M      | $23.54  | nan%         | nan%         | nanx          |
| 24 | MNDY     | 2025-08-11 | Before market open | Technology             | $12.8B       | $247.40 | nan%         | nan%         | nanx          |
| 25 | MPAA     | 2025-08-11 | Before market open | Consumer Cyclical      | $218.3M      | $11.25  | nan%         | nan%         | nanx          |
| 26 | NIU      | 2025-08-11 | Before market open | Consumer Cyclical      | $294.7M      | $3.74   | nan%         | nan%         | nanx          |
| 27 | PERI     | 2025-08-11 | Before market open | Communication Services | $459.8M      | $9.97   | nan%         | nan%         | nanx          |
| 28 | RUM      | 2025-08-11 | Before market open | Communication Services | $2.7B        | $8.05   | nan%         | nan%         | nanx          |
| 29 | SNDA     | 2025-08-11 | Before market open | Healthcare             | $459.9M      | $24.27  | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
