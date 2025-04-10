# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-04-09 21:46:03 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector             | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | PSMT     | 2025-04-09 | After market close | Consumer Defensive | $2.6B        | $82.12  | 25.64%       | 56.31%       | 2.20x         |
|  1 | STZ      | 2025-04-09 | After market close | Consumer Defensive | $33.2B       | $170.96 | 27.99%       | 52.97%       | 1.89x         |
|  2 | KMX      | 2025-04-10 | Before market open | Consumer Cyclical  | $12.3B       | $73.31  | 40.24%       | 67.92%       | 1.69x         |
|  3 | BSVN     | 2025-04-10 | Before market open | Financial Services | $351.1M      | $35.79  | nan%         | nan%         | nanx          |
|  4 | BYRN     | 2025-04-10 | Before market open | Industrials        | $375.8M      | $15.07  | nan%         | nan%         | nanx          |
|  5 | LAKE     | 2025-04-09 | After market close | Consumer Cyclical  | $174.3M      | $16.52  | nan%         | nan%         | nanx          |
|  6 | LOVE     | 2025-04-10 | Before market open | Consumer Cyclical  | $245.8M      | $12.47  | nan%         | nan%         | nanx          |
|  7 | PCYO     | 2025-04-09 | After market close | Utilities          | $259.5M      | $9.95   | nan%         | nan%         | nanx          |
|  8 | RELL     | 2025-04-09 | After market close | Technology         | $141.1M      | $9.14   | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
