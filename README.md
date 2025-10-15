# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-10-14 21:47:40 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | BAC      | 2025-10-15 | Before market open | Financial Services     | $371.0B      | $48.86  | 15.46%       | 32.04%       | 2.07x         |
|  1 | HWC      | 2025-10-14 | After market close | Financial Services     | $5.3B        | $60.49  | 20.83%       | 40.94%       | 1.97x         |
|  2 | PGR      | 2025-10-15 | Before market open | Financial Services     | $141.0B      | $236.28 | 15.55%       | 28.73%       | 1.85x         |
|  3 | ABT      | 2025-10-15 | Before market open | Healthcare             | $232.0B      | $131.38 | 15.51%       | 26.83%       | 1.73x         |
|  4 | SYF      | 2025-10-15 | Before market open | Financial Services     | $27.1B       | $70.14  | 25.44%       | 41.60%       | 1.64x         |
|  5 | MS       | 2025-10-15 | Before market open | Financial Services     | $248.0B      | $155.13 | 19.57%       | 31.95%       | 1.63x         |
|  6 | FHN      | 2025-10-15 | Before market open | Financial Services     | $11.7B       | $22.45  | 24.17%       | 39.40%       | 1.63x         |
|  7 | PNC      | 2025-10-15 | Before market open | Financial Services     | $74.4B       | $185.22 | 17.48%       | 27.83%       | 1.59x         |
|  8 | PLD      | 2025-10-15 | Before market open | Real Estate            | $107.2B      | $112.72 | 20.06%       | 28.29%       | 1.41x         |
|  9 | CFG      | 2025-10-15 | Before market open | Financial Services     | $22.3B       | $50.25  | 24.11%       | 32.76%       | 1.36x         |
| 10 | AMX      | 2025-10-14 | After market close | Communication Services | $64.3B       | $21.34  | nan%         | nan%         | nanx          |
| 11 | ASML     | 2025-10-15 | Before market open | Technology             | $381.6B      | $984.66 | nan%         | nan%         | nanx          |
| 12 | BSVN     | 2025-10-15 | Before market open | Financial Services     | $428.4M      | $43.95  | nan%         | nan%         | nanx          |
| 13 | EQBK     | 2025-10-14 | After market close | Financial Services     | $812.3M      | $40.46  | nan%         | nan%         | nanx          |
| 14 | KARO     | 2025-10-14 | After market close | Technology             | $1.7B        | $52.51  | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
