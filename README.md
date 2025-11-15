# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-11-14 20:48:44 EST

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector             | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | JJSF     | 2025-11-17 | Before market open | Consumer Defensive | $1.6B        | $82.57  | 20.71%       | 40.69%       | 1.96x         |
|  1 | BRC      | 2025-11-17 | Before market open | Industrials        | $3.5B        | $75.25  | 18.61%       | 28.95%       | 1.56x         |
|  2 | ARMK     | 2025-11-17 | Before market open | Industrials        | $10.1B       | $38.53  | 22.20%       | 34.44%       | 1.55x         |
|  3 | ARBE     | 2025-11-17 | Before market open | Technology         | $164.1M      | $1.51   | nan%         | nan%         | nanx          |
|  4 | BNZI     | 2025-11-14 | After market close | Technology         | $8.7M        | $1.40   | nan%         | nan%         | nanx          |
|  5 | CDRO     | 2025-11-17 | Before market open | Consumer Cyclical  | $259.7M      | $5.55   | nan%         | nan%         | nanx          |
|  6 | CSAN     | 2025-11-14 | After market close | Energy             | $5.0B        | $5.08   | nan%         | nan%         | nanx          |
|  7 | DFLI     | 2025-11-14 | After market close | Industrials        | $97.9M       | $0.77   | nan%         | nan%         | nanx          |
|  8 | FORA     | 2025-11-14 | After market close | Healthcare         | $68.4M       | $2.15   | nan%         | nan%         | nanx          |
|  9 | HTHT     | 2025-11-17 | Before market open | Consumer Cyclical  | $14.0B       | $44.99  | nan%         | nan%         | nanx          |
| 10 | JKS      | 2025-11-17 | Before market open | Technology         | $1.4B        | $26.32  | nan%         | nan%         | nanx          |
| 11 | MDV      | 2025-11-14 | After market close | Real Estate        | $149.2M      | $14.60  | nan%         | nan%         | nanx          |
| 12 | NIU      | 2025-11-17 | Before market open | Consumer Cyclical  | $311.1M      | $3.99   | nan%         | nan%         | nanx          |
| 13 | NKLR     | 2025-11-17 | Before market open | Utilities          | $289.4M      | $4.76   | nan%         | nan%         | nanx          |
| 14 | QUBT     | 2025-11-14 | After market close | Technology         | $2.4B        | $10.03  | nan%         | nan%         | nanx          |
| 15 | SY       | 2025-11-17 | Before market open | Healthcare         | $364.5M      | $3.63   | nan%         | nan%         | nanx          |
| 16 | TIVC     | 2025-11-14 | After market close | Healthcare         | $3.2M        | $2.07   | nan%         | nan%         | nanx          |
| 17 | VENU     | 2025-11-14 | After market close | Consumer Cyclical  | $481.4M      | $11.38  | nan%         | nan%         | nanx          |
| 18 | XPEV     | 2025-11-17 | Before market open | Consumer Cyclical  | $24.6B       | $26.38  | nan%         | nan%         | nanx          |
| 19 | YMM      | 2025-11-17 | Before market open | Technology         | $12.9B       | $12.56  | nan%         | nan%         | nanx          |
| 20 | ZK       | 2025-11-17 | Before market open | Consumer Cyclical  | $7.0B        | $27.54  | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
