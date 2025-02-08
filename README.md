# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-02-07 20:27:01 EST

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector             | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | INCY     | 2025-02-10 | Before market open | Healthcare         | $14.4B       | $74.95  | 20.54%       | 55.95%       | 2.72x         |
|  1 | ROK      | 2025-02-10 | Before market open | Industrials        | $30.4B       | $268.72 | 17.69%       | 35.69%       | 2.02x         |
|  2 | MCD      | 2025-02-10 | Before market open | Consumer Cyclical  | $210.9B      | $294.36 | 14.78%       | 21.85%       | 1.48x         |
|  3 | ON       | 2025-02-10 | Before market open | Technology         | $22.3B       | $52.44  | 43.79%       | 55.69%       | 1.27x         |
|  4 | ROIV     | 2025-02-10 | Before market open | Healthcare         | $7.9B        | $10.87  | 33.69%       | 39.61%       | 1.18x         |
|  5 | L        | 2025-02-10 | Before market open | Financial Services | $18.8B       | $86.81  | 18.55%       | 19.48%       | 1.05x         |
|  6 | HAIN     | 2025-02-10 | Before market open | Consumer Defensive | $442.0M      | $4.90   | 60.90%       | 60.73%       | 1.00x         |
|  7 | TGI      | 2025-02-10 | Before market open | Industrials        | $1.9B        | $25.18  | 85.57%       | 5.28%        | 0.06x         |
|  8 | AIOT     | 2025-02-10 | Before market open | Technology         | $786.5M      | $6.10   | nan%         | nan%         | nanx          |
|  9 | ALX      | 2025-02-10 | Before market open | Real Estate        | $1.0B        | $196.47 | nan%         | nan%         | nanx          |
| 10 | CAN      | 2025-02-10 | Before market open | Technology         | $544.9M      | $1.87   | nan%         | nan%         | nanx          |
| 11 | CNA      | 2025-02-10 | Before market open | Financial Services | $13.3B       | $49.65  | nan%         | nan%         | nanx          |
| 12 | EPC      | 2025-02-10 | Before market open | Consumer Defensive | $1.6B        | $32.01  | 24.53%       | nan%         | nanx          |
| 13 | GCMG     | 2025-02-10 | Before market open | Financial Services | $2.5B        | $13.70  | nan%         | nan%         | nanx          |
| 14 | MNDY     | 2025-02-10 | Before market open | Technology         | $13.2B       | $265.33 | nan%         | nan%         | nanx          |
| 15 | TSEM     | 2025-02-10 | Before market open | Technology         | $5.6B        | $49.71  | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
