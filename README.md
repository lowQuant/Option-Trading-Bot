# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-06-25 21:56:29 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector             | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | WBA      | 2025-06-26 | Before market open | Healthcare         | $9.8B        | $11.35  | 9.87%        | 18.36%       | 1.86x         |
|  1 | LNN      | 2025-06-26 | Before market open | Industrials        | $1.5B        | $138.22 | 18.57%       | 32.43%       | 1.75x         |
|  2 | MLKN     | 2025-06-25 | After market close | Consumer Cyclical  | $1.2B        | $17.72  | 36.94%       | 58.34%       | 1.58x         |
|  3 | MU       | 2025-06-25 | After market close | Technology         | $142.2B      | $127.91 | 37.32%       | 54.17%       | 1.45x         |
|  4 | MKC      | 2025-06-26 | Before market open | Consumer Defensive | $20.0B       | $74.71  | 19.87%       | 27.39%       | 1.38x         |
|  5 | AYI      | 2025-06-26 | Before market open | Industrials        | $8.9B        | $284.44 | 28.33%       | 38.36%       | 1.35x         |
|  6 | FUL      | 2025-06-25 | After market close | Basic Materials    | $3.1B        | $56.88  | 29.92%       | 34.45%       | 1.15x         |
|  7 | JEF      | 2025-06-25 | After market close | Financial Services | $11.5B       | $55.34  | 38.11%       | 37.67%       | 0.99x         |
|  8 | HIVE     | 2025-06-26 | Before market open | Financial Services | $330.9M      | $1.85   | nan%         | nan%         | nanx          |
|  9 | KEQU     | 2025-06-25 | After market close | Consumer Cyclical  | $115.5M      | $38.53  | nan%         | nan%         | nanx          |
| 10 | MKC.V    | 2025-06-26 | Before market open | nan                | N/A          | $nan    | nan%         | nan%         | nanx          |
| 11 | OESX     | 2025-06-26 | Before market open | Consumer Cyclical  | $19.5M       | $0.59   | nan%         | nan%         | nanx          |
| 12 | SCS      | 2025-06-25 | After market close | Consumer Cyclical  | $1.2B        | $10.83  | nan%         | nan%         | nanx          |
| 13 | WS       | 2025-06-25 | After market close | Basic Materials    | $1.3B        | $25.69  | 38.92%       | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
