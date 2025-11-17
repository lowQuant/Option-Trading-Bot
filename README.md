# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-11-16 20:54:12 EST

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | BRC      | 2025-11-17 | Before market open | Industrials            | $3.5B        | $75.25  | 18.64%       | 41.05%       | 2.20x         |
|  1 | JJSF     | 2025-11-17 | Before market open | Consumer Defensive     | $1.6B        | $82.57  | 20.93%       | 44.04%       | 2.10x         |
|  2 | ARMK     | 2025-11-17 | Before market open | Industrials            | $10.1B       | $38.53  | 22.18%       | 34.60%       | 1.56x         |
|  3 | ARBE     | 2025-11-17 | Before market open | Technology             | $164.1M      | $1.51   | nan%         | nan%         | nanx          |
|  4 | BNZI     | 2025-11-14 | After market close | Technology             | $8.7M        | $1.40   | nan%         | nan%         | nanx          |
|  5 | CDRO     | 2025-11-17 | Before market open | Consumer Cyclical      | $259.7M      | $5.55   | nan%         | nan%         | nanx          |
|  6 | CRGO     | 2025-11-17 | Before market open | Industrials            | $205.1M      | $4.00   | nan%         | nan%         | nanx          |
|  7 | CSAN     | 2025-11-14 | After market close | Energy                 | $7.3B        | $5.08   | nan%         | nan%         | nanx          |
|  8 | DFLI     | 2025-11-14 | After market close | Industrials            | $97.9M       | $0.77   | nan%         | nan%         | nanx          |
|  9 | EHLD     | 2025-11-17 | Before market open | Industrials            | $20.0M       | $7.08   | nan%         | nan%         | nanx          |
| 10 | FORA     | 2025-11-14 | After market close | Healthcare             | $66.9M       | $2.15   | nan%         | nan%         | nanx          |
| 11 | HTHT     | 2025-11-17 | Before market open | Consumer Cyclical      | $14.0B       | $44.99  | nan%         | nan%         | nanx          |
| 12 | JKS      | 2025-11-17 | Before market open | Technology             | $1.4B        | $26.32  | nan%         | nan%         | nanx          |
| 13 | MDV      | 2025-11-14 | After market close | Real Estate            | $149.2M      | $14.60  | nan%         | nan%         | nanx          |
| 14 | NIU      | 2025-11-17 | Before market open | Consumer Cyclical      | $311.1M      | $3.99   | nan%         | nan%         | nanx          |
| 15 | NKLR     | 2025-11-17 | Before market open | Utilities              | $300.1M      | $4.76   | nan%         | nan%         | nanx          |
| 16 | QUBT     | 2025-11-14 | After market close | Technology             | $2.4B        | $10.03  | nan%         | nan%         | nanx          |
| 17 | SOHU     | 2025-11-17 | Before market open | Communication Services | $444.7M      | $14.79  | nan%         | nan%         | nanx          |
| 18 | SY       | 2025-11-17 | Before market open | Healthcare             | $361.0M      | $3.63   | nan%         | nan%         | nanx          |
| 19 | TIVC     | 2025-11-14 | After market close | Healthcare             | $3.5M        | $2.07   | nan%         | nan%         | nanx          |
| 20 | VENU     | 2025-11-14 | After market close | Consumer Cyclical      | $495.8M      | $11.38  | nan%         | nan%         | nanx          |
| 21 | XPEV     | 2025-11-17 | Before market open | Consumer Cyclical      | $26.0B       | $26.38  | nan%         | nan%         | nanx          |
| 22 | YMM      | 2025-11-17 | Before market open | Technology             | $13.1B       | $12.56  | nan%         | nan%         | nanx          |
| 23 | YSG      | 2025-11-17 | Before market open | Consumer Defensive     | $623.2M      | $6.64   | nan%         | nan%         | nanx          |
| 24 | ZK       | 2025-11-17 | Before market open | Consumer Cyclical      | $7.1B        | $27.54  | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
