# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-08-08 21:56:48 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | CEVA     | 2025-08-11 | Before market open | Technology             | $519.5M      | $21.18  | 35.94%       | 73.54%       | 2.05x         |
|  1 | ROIV     | 2025-08-11 | Before market open | Healthcare             | $7.8B        | $11.55  | 25.70%       | 35.68%       | 1.39x         |
|  2 | TDS      | 2025-08-11 | Before market open | Communication Services | $4.4B        | $38.27  | 40.11%       | 51.76%       | 1.29x         |
|  3 | AGEN     | 2025-08-11 | Before market open | Healthcare             | $131.6M      | $4.76   | nan%         | nan%         | nanx          |
|  4 | AIOT     | 2025-08-11 | Before market open | Technology             | $529.1M      | $3.97   | nan%         | nan%         | nanx          |
|  5 | B        | 2025-08-11 | Before market open | Basic Materials        | $40.3B       | $23.07  | nan%         | nan%         | nanx          |
|  6 | BLDP     | 2025-08-11 | Before market open | Industrials            | $554.2M      | $1.85   | nan%         | nan%         | nanx          |
|  7 | DOLE     | 2025-08-11 | Before market open | Consumer Defensive     | $1.4B        | $14.59  | nan%         | nan%         | nanx          |
|  8 | EE       | 2025-08-11 | Before market open | Energy                 | $2.8B        | $24.42  | nan%         | nan%         | nanx          |
|  9 | FNV      | 2025-08-11 | Before market open | Basic Materials        | $33.1B       | $171.46 | nan%         | nan%         | nanx          |
| 10 | KGEI     | 2025-08-11 | Before market open | Energy                 | $215.6M      | $6.06   | nan%         | nan%         | nanx          |
| 11 | LAR      | 2025-08-11 | Before market open | Basic Materials        | $454.9M      | $2.69   | nan%         | nan%         | nanx          |
| 12 | LEGN     | 2025-08-11 | Before market open | Healthcare             | $6.9B        | $37.43  | nan%         | nan%         | nanx          |
| 13 | LINC     | 2025-08-11 | Before market open | Consumer Defensive     | $750.3M      | $23.54  | nan%         | nan%         | nanx          |
| 14 | MNDY     | 2025-08-11 | Before market open | Technology             | $12.8B       | $247.40 | nan%         | nan%         | nanx          |
| 15 | NIU      | 2025-08-11 | Before market open | Consumer Cyclical      | $294.7M      | $3.74   | nan%         | nan%         | nanx          |
| 16 | PERI     | 2025-08-11 | Before market open | Communication Services | $459.8M      | $9.97   | nan%         | nan%         | nanx          |
| 17 | SNDA     | 2025-08-11 | Before market open | Healthcare             | $459.9M      | $24.27  | nan%         | nan%         | nanx          |
| 18 | TLS      | 2025-08-11 | Before market open | Technology             | $174.9M      | $2.47   | nan%         | nan%         | nanx          |
| 19 | USM      | 2025-08-11 | Before market open | Communication Services | $6.3B        | $74.60  | nan%         | nan%         | nanx          |
| 20 | VFF      | 2025-08-11 | Before market open | Consumer Defensive     | $193.2M      | $1.67   | nan%         | nan%         | nanx          |
| 21 | WHG      | 2025-08-08 | After market close | Financial Services     | $153.6M      | $17.47  | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
