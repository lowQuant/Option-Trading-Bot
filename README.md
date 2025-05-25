# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-05-24 22:01:26 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close    | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:---------|:-------------|:-------------|:--------------|
|  0 | SKY      | 2025-05-27 | Before market open | Consumer Cyclical      | $4.8B        | $85.66   | 30.48%       | 56.69%       | 1.86x         |
|  1 | AZO      | 2025-05-27 | Before market open | Consumer Cyclical      | $64.0B       | $3859.25 | 20.72%       | 28.81%       | 1.39x         |
|  2 | BLRX     | 2025-05-27 | Before market open | Healthcare             | $13.6M       | $3.80    | nan%         | nan%         | nanx          |
|  3 | BNS      | 2025-05-27 | Before market open | Financial Services     | $65.0B       | $51.62   | nan%         | nan%         | nanx          |
|  4 | DLNG     | 2025-05-27 | Before market open | Energy                 | $133.7M      | $3.50    | nan%         | nan%         | nanx          |
|  5 | PDD      | 2025-05-27 | Before market open | Consumer Cyclical      | $169.3B      | $119.80  | nan%         | nan%         | nanx          |
|  6 | SHIP     | 2025-05-27 | Before market open | Industrials            | $125.8M      | $5.93    | nan%         | nan%         | nanx          |
|  7 | ZH       | 2025-05-27 | Before market open | Communication Services | $356.2M      | $4.01    | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
