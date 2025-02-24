# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-02-23 20:41:06 EST

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | FDP      | 2025-02-24 | Before market open | Consumer Defensive     | $1.5B        | $30.61  | 18.88%       | 45.77%       | 2.42x         |
|  1 | OC       | 2025-02-24 | Before market open | Industrials            | $14.2B       | $172.10 | 28.55%       | 42.35%       | 1.48x         |
|  2 | WLK      | 2025-02-24 | Before market open | Basic Materials        | $14.1B       | $111.40 | 24.92%       | 35.59%       | 1.43x         |
|  3 | DPZ      | 2025-02-24 | Before market open | Consumer Cyclical      | $16.0B       | $471.76 | 29.43%       | 39.85%       | 1.35x         |
|  4 | BCRX     | 2025-02-24 | Before market open | Healthcare             | $1.9B        | $9.39   | nan%         | nan%         | nanx          |
|  5 | CCO      | 2025-02-24 | Before market open | Communication Services | $660.3M      | $1.40   | nan%         | nan%         | nanx          |
|  6 | CRGO     | 2025-02-24 | Before market open | Industrials            | $200.4M      | $4.10   | nan%         | nan%         | nanx          |
|  7 | EDRY     | 2025-02-24 | Before market open | Industrials            | $29.3M       | $10.79  | nan%         | nan%         | nanx          |
|  8 | GTE      | 2025-02-24 | Before market open | Energy                 | $203.9M      | $5.89   | nan%         | nan%         | nanx          |
|  9 | HE       | 2025-02-21 | After market close | Utilities              | $1.9B        | $10.97  | nan%         | nan%         | nanx          |
| 10 | HOV      | 2025-02-24 | Before market open | Consumer Cyclical      | $717.7M      | $126.96 | nan%         | nan%         | nanx          |
| 11 | KOS      | 2025-02-24 | Before market open | Energy                 | $1.5B        | $3.35   | nan%         | nan%         | nanx          |
| 12 | KSPI     | 2025-02-24 | Before market open | Technology             | $20.3B       | $104.00 | nan%         | nan%         | nanx          |
| 13 | LINC     | 2025-02-24 | Before market open | Consumer Defensive     | $506.5M      | $17.63  | nan%         | nan%         | nanx          |
| 14 | SMMT     | 2025-02-24 | Before market open | Healthcare             | $16.3B       | $23.06  | nan%         | nan%         | nanx          |
| 15 | WLKP     | 2025-02-24 | Before market open | Basic Materials        | $853.5M      | $24.14  | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
