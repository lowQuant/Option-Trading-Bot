# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-10-31 21:54:06 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector             | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | MD       | 2025-11-03 | Before market open | Healthcare         | $1.5B        | $17.39  | 31.28%       | 69.73%       | 2.23x         |
|  1 | IDXX     | 2025-11-03 | Before market open | Healthcare         | $50.4B       | $628.54 | 22.79%       | 44.62%       | 1.96x         |
|  2 | KRYS     | 2025-11-03 | Before market open | Healthcare         | $5.7B        | $189.08 | 33.54%       | 58.56%       | 1.75x         |
|  3 | BRKR     | 2025-11-03 | Before market open | Healthcare         | $5.9B        | $36.40  | 48.86%       | 81.08%       | 1.66x         |
|  4 | KTB      | 2025-11-03 | Before market open | Consumer Cyclical  | $4.5B        | $81.15  | 38.46%       | 56.81%       | 1.48x         |
|  5 | FRPT     | 2025-11-03 | Before market open | Consumer Defensive | $2.4B        | $50.60  | 54.66%       | 80.52%       | 1.47x         |
|  6 | PNW      | 2025-11-03 | Before market open | Utilities          | $10.7B       | $89.55  | 16.26%       | 23.62%       | 1.45x         |
|  7 | L        | 2025-11-03 | Before market open | Financial Services | $20.7B       | $99.53  | 16.06%       | 22.93%       | 1.43x         |
|  8 | PEG      | 2025-11-03 | Before market open | Utilities          | $40.3B       | $80.75  | 19.43%       | 27.44%       | 1.41x         |
|  9 | ON       | 2025-11-03 | Before market open | Technology         | $20.8B       | $50.85  | 55.02%       | 63.22%       | 1.15x         |
| 10 | MSEX     | 2025-10-31 | After market close | Utilities          | $1.0B        | $56.92  | 29.18%       | 30.82%       | 1.06x         |
| 11 | ALX      | 2025-11-03 | Before market open | Real Estate        | $1.1B        | $218.54 | nan%         | nan%         | nanx          |
| 12 | ARES     | 2025-11-03 | Before market open | Financial Services | $48.6B       | $147.29 | nan%         | nan%         | nanx          |
| 13 | AXSM     | 2025-11-03 | Before market open | Healthcare         | $6.7B        | $133.15 | nan%         | nan%         | nanx          |
| 14 | BCRX     | 2025-11-03 | Before market open | Healthcare         | $1.5B        | $7.25   | nan%         | nan%         | nanx          |
| 15 | BNTX     | 2025-11-03 | Before market open | Healthcare         | $25.2B       | $104.67 | nan%         | nan%         | nanx          |
| 16 | CIFR     | 2025-11-03 | Before market open | Financial Services | $7.3B        | $19.07  | nan%         | nan%         | nanx          |
| 17 | CNA      | 2025-11-03 | Before market open | Financial Services | $12.1B       | $44.61  | nan%         | nan%         | nanx          |
| 18 | ECX      | 2025-11-03 | Before market open | Consumer Cyclical  | $841.2M      | $2.38   | nan%         | nan%         | nanx          |
| 19 | GNE      | 2025-11-03 | Before market open | Utilities          | $393.7M      | $14.74  | nan%         | nan%         | nanx          |
| 20 | HESM     | 2025-11-03 | Before market open | Energy             | $7.2B        | $34.14  | nan%         | nan%         | nanx          |
| 21 | III      | 2025-11-03 | Before market open | Technology         | $265.6M      | $5.47   | nan%         | nan%         | nanx          |
| 22 | KOS      | 2025-11-03 | Before market open | Energy             | $750.9M      | $1.55   | nan%         | nan%         | nanx          |
| 23 | OXLC     | 2025-11-03 | Before market open | Financial Services | $1.5B        | $15.19  | nan%         | nan%         | nanx          |
| 24 | RYAAY    | 2025-11-03 | Before market open | Industrials        | $33.0B       | $61.55  | nan%         | nan%         | nanx          |
| 25 | VERX     | 2025-11-03 | Before market open | Technology         | $3.6B        | $22.60  | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
