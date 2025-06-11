# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-06-10 21:56:13 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | CHWY     | 2025-06-11 | Before market open | Consumer Cyclical      | $19.0B       | $46.51  | 29.04%       | 56.27%       | 1.94x         |
|  1 | GME      | 2025-06-10 | After market close | Consumer Cyclical      | $13.6B       | $30.34  | 59.60%       | 82.80%       | 1.39x         |
|  2 | PLAY     | 2025-06-10 | After market close | Communication Services | $894.1M      | $25.57  | 70.46%       | 90.39%       | 1.28x         |
|  3 | VSCO     | 2025-06-11 | Before market open | Consumer Cyclical      | $1.8B        | $22.72  | 58.23%       | 72.32%       | 1.24x         |
|  4 | CGNT     | 2025-06-11 | Before market open | Technology             | $805.9M      | $11.20  | nan%         | nan%         | nanx          |
|  5 | GTLB     | 2025-06-10 | After market close | Technology             | $8.0B        | $48.64  | nan%         | nan%         | nanx          |
|  6 | JILL     | 2025-06-11 | Before market open | Consumer Cyclical      | $262.1M      | $17.15  | nan%         | nan%         | nanx          |
|  7 | MIND     | 2025-06-10 | After market close | Technology             | $55.1M       | $6.91   | nan%         | nan%         | nanx          |
|  8 | PETS     | 2025-06-10 | After market close | Healthcare             | $86.6M       | $4.12   | nan%         | nan%         | nanx          |
|  9 | SAIL     | 2025-06-11 | Before market open | Technology             | $10.9B       | $19.18  | nan%         | nan%         | nanx          |
| 10 | SFIX     | 2025-06-10 | After market close | Consumer Cyclical      | $609.2M      | $4.73   | nan%         | nan%         | nanx          |
| 11 | VRA      | 2025-06-11 | Before market open | Consumer Cyclical      | $72.0M       | $2.58   | nan%         | nan%         | nanx          |
| 12 | YQ       | 2025-06-10 | After market close | Consumer Defensive     | $18.5M       | $2.09   | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
