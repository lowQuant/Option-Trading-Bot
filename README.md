# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-04-25 21:45:20 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | DPZ      | 2025-04-28 | Before market open | Consumer Cyclical      | $16.7B       | $487.97 | 38.60%       | 40.78%       | 1.06x         |
|  1 | BKU      | 2025-04-28 | Before market open | Financial Services     | $2.5B        | $33.67  | 57.88%       | 60.73%       | 1.05x         |
|  2 | ROP      | 2025-04-28 | Before market open | Technology             | $59.9B       | $559.66 | 34.72%       | 27.97%       | 0.81x         |
|  3 | RVTY     | 2025-04-28 | Before market open | Healthcare             | $11.3B       | $95.13  | 53.48%       | 39.81%       | 0.74x         |
|  4 | ARLP     | 2025-04-28 | Before market open | Energy                 | $3.5B        | $27.45  | nan%         | nan%         | nanx          |
|  5 | BMRC     | 2025-04-28 | Before market open | Financial Services     | $337.3M      | $21.03  | nan%         | nan%         | nanx          |
|  6 | FMX      | 2025-04-28 | Before market open | Consumer Defensive     | $184.6B      | $105.91 | nan%         | nan%         | nanx          |
|  7 | INMD     | 2025-04-28 | Before market open | Healthcare             | $1.1B        | $16.13  | nan%         | nan%         | nanx          |
|  8 | OPRA     | 2025-04-28 | Before market open | Communication Services | $1.4B        | $15.37  | nan%         | nan%         | nanx          |
|  9 | PERF     | 2025-04-28 | Before market open | Technology             | $192.5M      | $1.77   | nan%         | nan%         | nanx          |
| 10 | RPT      | 2025-04-28 | Before market open | Real Estate            | $138.3M      | $2.75   | nan%         | nan%         | nanx          |
| 11 | SILC     | 2025-04-28 | Before market open | Technology             | $78.1M       | $13.88  | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
