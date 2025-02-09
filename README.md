# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-02-08 20:40:39 EST

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector             | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | INCY     | 2025-02-10 | Before market open | Healthcare         | $14.3B       | $74.95  | 20.61%       | 57.06%       | 2.77x         |
|  1 | ROK      | 2025-02-10 | Before market open | Industrials        | $30.3B       | $268.72 | 17.70%       | 35.45%       | 2.00x         |
|  2 | EPC      | 2025-02-10 | Before market open | Consumer Defensive | $1.5B        | $32.01  | 24.59%       | 44.29%       | 1.80x         |
|  3 | NSP      | 2025-02-10 | Before market open | Industrials        | $2.6B        | $71.43  | 34.10%       | 51.71%       | 1.52x         |
|  4 | ROIV     | 2025-02-10 | Before market open | Healthcare         | $7.9B        | $10.87  | 31.94%       | 48.03%       | 1.50x         |
|  5 | MCD      | 2025-02-10 | Before market open | Consumer Cyclical  | $210.9B      | $294.36 | 14.71%       | 21.87%       | 1.49x         |
|  6 | ON       | 2025-02-10 | Before market open | Technology         | $21.8B       | $52.44  | 43.38%       | 58.25%       | 1.34x         |
|  7 | L        | 2025-02-10 | Before market open | Financial Services | $18.8B       | $86.81  | 18.55%       | 20.44%       | 1.10x         |
|  8 | HAIN     | 2025-02-10 | Before market open | Consumer Defensive | $423.0M      | $4.90   | 61.41%       | 66.39%       | 1.08x         |
|  9 | AIOT     | 2025-02-10 | Before market open | Technology         | $786.5M      | $6.10   | nan%         | nan%         | nanx          |
| 10 | ALX      | 2025-02-10 | Before market open | Real Estate        | $1.0B        | $196.47 | nan%         | nan%         | nanx          |
| 11 | CAN      | 2025-02-10 | Before market open | Technology         | $544.9M      | $1.87   | nan%         | nan%         | nanx          |
| 12 | CNA      | 2025-02-10 | Before market open | Financial Services | $13.3B       | $49.65  | nan%         | nan%         | nanx          |
| 13 | CSPI     | 2025-02-10 | Before market open | Technology         | $194.2M      | $20.82  | nan%         | nan%         | nanx          |
| 14 | GCMG     | 2025-02-10 | Before market open | Financial Services | $2.5B        | $13.70  | nan%         | nan%         | nanx          |
| 15 | ISPR     | 2025-02-10 | Before market open | Consumer Defensive | $264.5M      | $4.71   | nan%         | nan%         | nanx          |
| 16 | MNDY     | 2025-02-10 | Before market open | Technology         | $12.9B       | $265.33 | nan%         | nan%         | nanx          |
| 17 | MPAA     | 2025-02-10 | Before market open | Consumer Cyclical  | $114.1M      | $5.66   | nan%         | nan%         | nanx          |
| 18 | TSEM     | 2025-02-10 | Before market open | Technology         | $5.6B        | $49.71  | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
