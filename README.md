# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-12-16 20:55:22 EST

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector             | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | WOR      | 2025-12-16 | After market close | Industrials        | $2.8B        | $57.74  | 23.21%       | 40.96%       | 1.76x         |
|  1 | TTC      | 2025-12-17 | Before market open | Industrials        | $7.2B        | $73.48  | 23.79%       | 40.01%       | 1.68x         |
|  2 | GIS      | 2025-12-17 | Before market open | Consumer Defensive | $25.1B       | $47.06  | 17.29%       | 28.15%       | 1.63x         |
|  3 | ABM      | 2025-12-17 | Before market open | Industrials        | $2.8B        | $47.18  | 25.21%       | 38.88%       | 1.54x         |
|  4 | JBL      | 2025-12-17 | Before market open | Technology         | $22.7B       | $221.21 | 40.32%       | 48.32%       | 1.20x         |
|  5 | LEN      | 2025-12-16 | After market close | Consumer Cyclical  | $29.0B       | $119.73 | 40.97%       | 38.38%       | 0.94x         |
|  6 | LEN.B    | 2025-12-16 | After market close | nan                | N/A          | $nan    | nan%         | nan%         | nanx          |
|  7 | SPIR     | 2025-12-17 | Before market open | Industrials        | $303.4M      | $9.08   | nan%         | nan%         | nanx          |
|  8 | VERU     | 2025-12-17 | Before market open | Healthcare         | $39.2M       | $2.39   | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
