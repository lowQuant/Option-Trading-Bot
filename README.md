# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-09-02 21:41:10 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector             | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | DLTR     | 2025-09-03 | Before market open | Consumer Defensive | $23.2B       | $109.17 | 17.27%       | 41.64%       | 2.41x         |
|  1 | CPB      | 2025-09-03 | Before market open | Consumer Defensive | $9.4B        | $31.93  | 24.52%       | 35.85%       | 1.46x         |
|  2 | CXM      | 2025-09-03 | Before market open | Technology         | $2.2B        | $8.64   | 41.36%       | 58.39%       | 1.41x         |
|  3 | HQY      | 2025-09-02 | After market close | Healthcare         | $7.7B        | $89.33  | 31.94%       | 43.52%       | 1.36x         |
|  4 | M        | 2025-09-03 | Before market open | Consumer Cyclical  | $3.7B        | $13.23  | 43.51%       | 54.37%       | 1.25x         |
|  5 | GEG      | 2025-09-02 | After market close | Financial Services | $75.0M       | $2.41   | nan%         | nan%         | nanx          |
|  6 | JILL     | 2025-09-03 | Before market open | Consumer Cyclical  | $257.8M      | $16.76  | nan%         | nan%         | nanx          |
|  7 | REVG     | 2025-09-03 | Before market open | Industrials        | $2.5B        | $53.21  | nan%         | nan%         | nanx          |
|  8 | RGS      | 2025-09-03 | Before market open | Consumer Cyclical  | $53.9M       | $22.15  | nan%         | nan%         | nanx          |
|  9 | ZS       | 2025-09-02 | After market close | Technology         | $42.7B       | $277.05 | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
