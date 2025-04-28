# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-04-27 21:52:31 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | DPZ      | 2025-04-28 | Before market open | Consumer Cyclical      | $16.7B       | $487.97 | 37.79%       | 41.04%       | 1.09x         |
|  1 | RVTY     | 2025-04-28 | Before market open | Healthcare             | $11.4B       | $95.13  | 53.47%       | 47.17%       | 0.88x         |
|  2 | BKU      | 2025-04-28 | Before market open | Financial Services     | $2.5B        | $33.67  | 57.78%       | 50.31%       | 0.87x         |
|  3 | ROP      | 2025-04-28 | Before market open | Technology             | $60.1B       | $559.66 | 34.68%       | 28.45%       | 0.82x         |
|  4 | ARLP     | 2025-04-28 | Before market open | Energy                 | $3.5B        | $27.45  | nan%         | nan%         | nanx          |
|  5 | BEDU     | 2025-04-28 | Before market open | Consumer Defensive     | $49.0M       | $1.65   | nan%         | nan%         | nanx          |
|  6 | BMRC     | 2025-04-28 | Before market open | Financial Services     | $340.7M      | $21.03  | nan%         | nan%         | nanx          |
|  7 | FMX      | 2025-04-28 | Before market open | Consumer Defensive     | $184.6B      | $105.91 | nan%         | nan%         | nanx          |
|  8 | INMD     | 2025-04-28 | Before market open | Healthcare             | $1.1B        | $16.13  | nan%         | nan%         | nanx          |
|  9 | OPRA     | 2025-04-28 | Before market open | Communication Services | $1.4B        | $15.37  | nan%         | nan%         | nanx          |
| 10 | PERF     | 2025-04-28 | Before market open | Technology             | $193.5M      | $1.77   | nan%         | nan%         | nanx          |
| 11 | PROV     | 2025-04-28 | Before market open | Financial Services     | $98.0M       | $14.65  | nan%         | nan%         | nanx          |
| 12 | RPT      | 2025-04-28 | Before market open | Real Estate            | $138.3M      | $2.75   | nan%         | nan%         | nanx          |
| 13 | SILC     | 2025-04-28 | Before market open | Technology             | $80.0M       | $13.88  | nan%         | nan%         | nanx          |
| 14 | VLRS     | 2025-04-28 | Before market open | Industrials            | $546.4M      | $4.69   | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
