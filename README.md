# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-05-22 21:52:43 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector             | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | CVCO     | 2025-05-22 | After market close | Consumer Cyclical  | $4.0B        | $516.02 | 33.62%       | 41.32%       | 1.23x         |
|  1 | DECK     | 2025-05-22 | After market close | Consumer Cyclical  | $19.1B       | $123.36 | 55.59%       | 67.30%       | 1.21x         |
|  2 | WDAY     | 2025-05-22 | After market close | Technology         | $72.8B       | $268.54 | 39.74%       | 43.80%       | 1.10x         |
|  3 | ROST     | 2025-05-22 | After market close | Consumer Cyclical  | $50.1B       | $152.68 | 30.64%       | 32.15%       | 1.05x         |
|  4 | CPRT     | 2025-05-22 | After market close | Industrials        | $58.6B       | $61.09  | 28.23%       | 29.02%       | 1.03x         |
|  5 | ADSK     | 2025-05-22 | After market close | Technology         | $63.1B       | $292.93 | 34.98%       | 34.42%       | 0.98x         |
|  6 | INTU     | 2025-05-22 | After market close | Technology         | $186.2B      | $659.98 | 35.34%       | 33.27%       | 0.94x         |
|  7 | STEP     | 2025-05-22 | After market close | Financial Services | $6.8B        | $56.24  | 59.37%       | 39.87%       | 0.67x         |
|  8 | BAH      | 2025-05-23 | Before market open | Industrials        | $16.0B       | $128.42 | nan%         | nan%         | nanx          |
|  9 | BULL     | 2025-05-22 | After market close | Technology         | $6.2B        | $12.59  | nan%         | nan%         | nanx          |
| 10 | ICG      | 2025-05-22 | After market close | Technology         | $162.4M      | $2.43   | nan%         | nan%         | nanx          |
| 11 | LION     | 2025-05-22 | After market close | nan                | $1.9B        | $6.73   | nan%         | nan%         | nanx          |
| 12 | MNSO     | 2025-05-23 | Before market open | Consumer Cyclical  | $6.8B        | $20.77  | nan%         | nan%         | nanx          |
| 13 | SVM      | 2025-05-22 | After market close | Basic Materials    | $841.4M      | $3.91   | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
