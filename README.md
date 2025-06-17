# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-06-16 21:56:48 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | WLY      | 2025-06-17 | Before market open | Communication Services | $2.0B        | $37.73  | 20.43%       | 49.62%       | 2.43x         |
|  1 | JBL      | 2025-06-17 | Before market open | nan                    | $19.4B       | $nan    | 22.53%       | 43.31%       | 1.92x         |
|  2 | LEN      | 2025-06-16 | After market close | Consumer Cyclical      | $28.5B       | $108.61 | 32.30%       | 44.45%       | 1.38x         |
|  3 | ANTA     | 2025-06-17 | Before market open | Financial Services     | $295.4M      | $12.20  | nan%         | nan%         | nanx          |
|  4 | APPS     | 2025-06-16 | After market close | nan                    | $505.1M      | $nan    | nan%         | nan%         | nanx          |
|  5 | GLBS     | 2025-06-16 | After market close | Industrials            | $27.8M       | $1.35   | nan%         | nan%         | nanx          |
|  6 | HITI     | 2025-06-16 | After market close | Healthcare             | $184.5M      | $2.28   | nan%         | nan%         | nanx          |
|  7 | KIRK     | 2025-06-17 | Before market open | Consumer Cyclical      | $28.5M       | $1.19   | nan%         | nan%         | nanx          |
|  8 | LEN.B    | 2025-06-16 | After market close | nan                    | N/A          | $nan    | nan%         | nan%         | nanx          |
|  9 | RFIL     | 2025-06-16 | After market close | Industrials            | $47.7M       | $4.12   | nan%         | nan%         | nanx          |
| 10 | TEN      | 2025-06-17 | Before market open | Energy                 | $591.7M      | $19.64  | nan%         | nan%         | nanx          |
| 11 | VNCE     | 2025-06-17 | Before market open | Consumer Cyclical      | $21.6M       | $1.46   | nan%         | nan%         | nanx          |
| 12 | WLYB     | 2025-06-17 | Before market open | nan                    | $2.0B        | $nan    | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
