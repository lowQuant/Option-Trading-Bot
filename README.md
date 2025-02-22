# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-02-21 20:35:18 EST

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | FDP      | 2025-02-24 | Before market open | Consumer Defensive     | $1.5B        | $30.61  | 18.82%       | 41.64%       | 2.21x         |
|  1 | OC       | 2025-02-24 | Before market open | Industrials            | $14.2B       | $172.10 | 26.44%       | 35.18%       | 1.33x         |
|  2 | WLK      | 2025-02-24 | Before market open | Basic Materials        | $14.1B       | $111.40 | 25.01%       | 33.14%       | 1.33x         |
|  3 | DPZ      | 2025-02-24 | Before market open | Consumer Cyclical      | $16.0B       | $471.76 | 30.51%       | 35.94%       | 1.18x         |
|  4 | BCRX     | 2025-02-24 | Before market open | Healthcare             | $1.9B        | $9.39   | nan%         | nan%         | nanx          |
|  5 | CCO      | 2025-02-24 | Before market open | Communication Services | $660.3M      | $1.40   | nan%         | nan%         | nanx          |
|  6 | HE       | 2025-02-21 | After market close | Utilities              | $1.9B        | $10.97  | nan%         | nan%         | nanx          |
|  7 | HOV      | 2025-02-24 | Before market open | Consumer Cyclical      | $714.0M      | $126.96 | nan%         | nan%         | nanx          |
|  8 | KOS      | 2025-02-24 | Before market open | Energy                 | $1.5B        | $3.35   | nan%         | nan%         | nanx          |
|  9 | KSPI     | 2025-02-24 | Before market open | Technology             | $19.8B       | $104.00 | nan%         | nan%         | nanx          |
| 10 | WLKP     | 2025-02-24 | Before market open | Basic Materials        | $853.5M      | $24.14  | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
