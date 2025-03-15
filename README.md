# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-03-14 21:40:42 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | SAIC     | 2025-03-17 | Before market open | Technology             | $5.1B        | $104.26 | 41.76%       | 59.12%       | 1.42x         |
|  1 | CODA     | 2025-03-17 | Before market open | Industrials            | $74.3M       | $6.71   | nan%         | nan%         | nanx          |
|  2 | FF       | 2025-03-14 | After market close | Basic Materials        | $181.2M      | $4.36   | nan%         | nan%         | nanx          |
|  3 | INSE     | 2025-03-17 | Before market open | Consumer Cyclical      | $222.5M      | $8.03   | nan%         | nan%         | nanx          |
|  4 | LNZA     | 2025-03-17 | Before market open | Industrials            | $107.0M      | $0.50   | nan%         | nan%         | nanx          |
|  5 | NIU      | 2025-03-17 | Before market open | Consumer Cyclical      | $211.1M      | $2.57   | nan%         | nan%         | nanx          |
|  6 | NXPL     | 2025-03-17 | Before market open | Technology             | $26.0M       | $1.03   | nan%         | nan%         | nanx          |
|  7 | QFIN     | 2025-03-17 | Before market open | Financial Services     | $6.8B        | $39.97  | nan%         | nan%         | nanx          |
|  8 | SNDA     | 2025-03-17 | Before market open | Healthcare             | $449.5M      | $22.83  | nan%         | nan%         | nanx          |
|  9 | TE       | 2025-03-17 | Before market open | Industrials            | $237.0M      | $1.39   | nan%         | nan%         | nanx          |
| 10 | TSQ      | 2025-03-17 | Before market open | Communication Services | $121.1M      | $7.61   | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
