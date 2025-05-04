# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-05-03 21:59:11 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector             | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | IART     | 2025-05-05 | Before market open | Healthcare         | $1.3B        | $16.44  | 57.91%       | 92.22%       | 1.59x         |
|  1 | TGTX     | 2025-05-05 | Before market open | Healthcare         | $6.8B        | $45.37  | 47.96%       | 73.25%       | 1.53x         |
|  2 | FRPT     | 2025-05-05 | Before market open | Consumer Defensive | $3.7B        | $72.72  | 56.70%       | 73.11%       | 1.29x         |
|  3 | HSIC     | 2025-05-05 | Before market open | Healthcare         | $8.0B        | $64.46  | 32.95%       | 39.12%       | 1.19x         |
|  4 | ZBH      | 2025-05-05 | Before market open | Healthcare         | $20.3B       | $101.82 | 25.79%       | 30.05%       | 1.17x         |
|  5 | TSN      | 2025-05-05 | Before market open | Consumer Defensive | $21.7B       | $60.61  | 28.03%       | 30.63%       | 1.09x         |
|  6 | JBTM     | 2025-05-05 | Before market open | Industrials        | $5.6B        | $105.49 | 58.53%       | 50.88%       | 0.87x         |
|  7 | PK       | 2025-05-05 | Before market open | Real Estate        | $2.1B        | $10.04  | 60.83%       | 43.77%       | 0.72x         |
|  8 | CMI      | 2025-05-05 | Before market open | Industrials        | $41.3B       | $294.88 | 51.66%       | 36.59%       | 0.71x         |
|  9 | ON       | 2025-05-05 | Before market open | Technology         | $17.7B       | $39.60  | 98.38%       | 63.84%       | 0.65x         |
| 10 | L        | 2025-05-05 | Before market open | Financial Services | $18.5B       | $86.31  | 38.18%       | 21.89%       | 0.57x         |
| 11 | ALX      | 2025-05-05 | Before market open | Real Estate        | $1.1B        | $208.72 | nan%         | nan%         | nanx          |
| 12 | AOMR     | 2025-05-05 | Before market open | Real Estate        | $224.4M      | $9.49   | nan%         | nan%         | nanx          |
| 13 | ARES     | 2025-05-05 | Before market open | Financial Services | $51.3B       | $152.27 | nan%         | nan%         | nanx          |
| 14 | AXSM     | 2025-05-05 | Before market open | Healthcare         | $5.5B        | $112.24 | nan%         | nan%         | nanx          |
| 15 | BCRX     | 2025-05-05 | Before market open | Healthcare         | $1.9B        | $8.71   | nan%         | nan%         | nanx          |
| 16 | BNTX     | 2025-05-05 | Before market open | Healthcare         | $25.2B       | $102.43 | nan%         | nan%         | nanx          |
| 17 | CNA      | 2025-05-05 | Before market open | Financial Services | $12.9B       | $47.44  | nan%         | nan%         | nanx          |
| 18 | ESCA     | 2025-05-05 | Before market open | Consumer Cyclical  | $209.1M      | $14.69  | nan%         | nan%         | nanx          |
| 19 | IRMD     | 2025-05-05 | Before market open | Healthcare         | $679.9M      | $52.94  | nan%         | nan%         | nanx          |
| 20 | NSSC     | 2025-05-05 | Before market open | Industrials        | $865.6M      | $23.00  | nan%         | nan%         | nanx          |
| 21 | OCUL     | 2025-05-05 | Before market open | Healthcare         | $1.4B        | $8.53   | nan%         | nan%         | nanx          |
| 22 | RAND     | 2025-05-05 | Before market open | Financial Services | $55.6M       | $18.94  | nan%         | nan%         | nanx          |
| 23 | RLJ      | 2025-05-05 | Before market open | Real Estate        | $1.1B        | $7.11   | nan%         | nan%         | nanx          |
| 24 | RXRX     | 2025-05-05 | Before market open | Healthcare         | $2.3B        | $5.50   | nan%         | nan%         | nanx          |
| 25 | TWST     | 2025-05-05 | Before market open | Healthcare         | $2.3B        | $37.71  | nan%         | nan%         | nanx          |
| 26 | XGN      | 2025-05-05 | Before market open | Healthcare         | $107.7M      | $6.14   | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
