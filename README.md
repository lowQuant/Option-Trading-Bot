# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-05-02 21:47:46 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector             | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | FRPT     | 2025-05-05 | Before market open | Consumer Defensive | $3.7B        | $72.72  | 54.59%       | 80.18%       | 1.47x         |
|  1 | ZBH      | 2025-05-05 | Before market open | Healthcare         | $20.3B       | $101.82 | 25.74%       | 37.71%       | 1.47x         |
|  2 | IART     | 2025-05-05 | Before market open | Healthcare         | $1.3B        | $16.44  | 57.01%       | 79.63%       | 1.40x         |
|  3 | HSIC     | 2025-05-05 | Before market open | Healthcare         | $8.0B        | $64.46  | 32.63%       | 37.00%       | 1.13x         |
|  4 | TSN      | 2025-05-05 | Before market open | Consumer Defensive | $21.7B       | $60.61  | 28.08%       | 31.66%       | 1.13x         |
|  5 | JBTM     | 2025-05-05 | Before market open | Industrials        | $5.6B        | $105.49 | 58.19%       | 53.65%       | 0.92x         |
|  6 | PK       | 2025-05-05 | Before market open | Real Estate        | $2.1B        | $10.04  | 60.35%       | 42.63%       | 0.71x         |
|  7 | CMI      | 2025-05-05 | Before market open | Industrials        | $41.3B       | $294.88 | 51.33%       | 36.09%       | 0.70x         |
|  8 | ON       | 2025-05-05 | Before market open | Technology         | $17.7B       | $39.60  | 96.86%       | 61.71%       | 0.64x         |
|  9 | L        | 2025-05-05 | Before market open | Financial Services | $18.5B       | $86.31  | 37.70%       | 23.60%       | 0.63x         |
| 10 | AOMR     | 2025-05-05 | Before market open | Real Estate        | $224.4M      | $9.49   | nan%         | nan%         | nanx          |
| 11 | ARES     | 2025-05-05 | Before market open | Financial Services | $51.3B       | $152.27 | nan%         | nan%         | nanx          |
| 12 | AXSM     | 2025-05-05 | Before market open | Healthcare         | $5.5B        | $112.24 | nan%         | nan%         | nanx          |
| 13 | BCRX     | 2025-05-05 | Before market open | Healthcare         | $1.9B        | $8.71   | nan%         | nan%         | nanx          |
| 14 | BNTX     | 2025-05-05 | Before market open | Healthcare         | $25.2B       | $102.43 | nan%         | nan%         | nanx          |
| 15 | CNA      | 2025-05-05 | Before market open | Financial Services | $12.9B       | $47.44  | nan%         | nan%         | nanx          |
| 16 | RAND     | 2025-05-05 | Before market open | Financial Services | $55.6M       | $18.94  | nan%         | nan%         | nanx          |
| 17 | RLJ      | 2025-05-05 | Before market open | Real Estate        | $1.1B        | $7.11   | nan%         | nan%         | nanx          |
| 18 | TWST     | 2025-05-05 | Before market open | Healthcare         | $2.3B        | $37.71  | nan%         | nan%         | nanx          |
| 19 | XGN      | 2025-05-05 | Before market open | Healthcare         | $107.7M      | $6.14   | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
