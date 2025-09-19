# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-09-18 21:45:03 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | SCHL     | 2025-09-18 | After market close | Communication Services | $691.3M      | $27.21  | 33.53%       | 67.95%       | 2.03x         |
|  1 | FDX      | 2025-09-18 | After market close | Industrials            | $53.4B       | $225.78 | 25.98%       | 44.02%       | 1.69x         |
|  2 | LEN      | 2025-09-18 | After market close | Consumer Cyclical      | $34.2B       | $132.97 | 32.87%       | 43.87%       | 1.33x         |
|  3 | LEN.B    | 2025-09-18 | After market close | nan                    | N/A          | $nan    | nan%         | nan%         | nanx          |
|  4 | MNY      | 2025-09-19 | Before market open | Communication Services | $94.5M       | $1.95   | nan%         | nan%         | nanx          |
|  5 | RSSS     | 2025-09-18 | After market close | Technology             | $127.6M      | $3.70   | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
