# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-11-01 21:56:31 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | MD       | 2025-11-03 | Before market open | Healthcare             | $1.5B        | $17.39  | 31.60%       | 67.84%       | 2.15x         |
|  1 | IDXX     | 2025-11-03 | Before market open | Healthcare             | $50.4B       | $628.54 | 22.80%       | 46.57%       | 2.04x         |
|  2 | KRYS     | 2025-11-03 | Before market open | Healthcare             | $5.7B        | $189.08 | 35.15%       | 60.02%       | 1.71x         |
|  3 | FRPT     | 2025-11-03 | Before market open | Consumer Defensive     | $2.4B        | $50.60  | 55.10%       | 85.16%       | 1.55x         |
|  4 | PNW      | 2025-11-03 | Before market open | Utilities              | $10.6B       | $89.55  | 16.57%       | 25.29%       | 1.53x         |
|  5 | KTB      | 2025-11-03 | Before market open | Consumer Cyclical      | $4.5B        | $81.15  | 38.04%       | 57.71%       | 1.52x         |
|  6 | L        | 2025-11-03 | Before market open | Financial Services     | $20.7B       | $99.53  | 16.00%       | 23.84%       | 1.49x         |
|  7 | PEG      | 2025-11-03 | Before market open | Utilities              | $40.2B       | $80.75  | 19.37%       | 28.29%       | 1.46x         |
|  8 | BRKR     | 2025-11-03 | Before market open | Healthcare             | $5.9B        | $36.40  | 52.26%       | 76.14%       | 1.46x         |
|  9 | MSEX     | 2025-10-31 | After market close | Utilities              | $1.0B        | $56.92  | 29.16%       | 37.55%       | 1.29x         |
| 10 | ON       | 2025-11-03 | Before market open | Technology             | $20.5B       | $50.85  | 55.03%       | 69.76%       | 1.27x         |
| 11 | AMG      | 2025-11-03 | Before market open | Financial Services     | $6.8B        | $236.68 | 27.20%       | 34.36%       | 1.26x         |
| 12 | ALX      | 2025-11-03 | Before market open | Real Estate            | $1.1B        | $218.54 | nan%         | nan%         | nanx          |
| 13 | ARES     | 2025-11-03 | Before market open | Financial Services     | $48.6B       | $147.29 | nan%         | nan%         | nanx          |
| 14 | AXSM     | 2025-11-03 | Before market open | Healthcare             | $6.7B        | $133.15 | nan%         | nan%         | nanx          |
| 15 | BCRX     | 2025-11-03 | Before market open | Healthcare             | $1.5B        | $7.25   | nan%         | nan%         | nanx          |
| 16 | BNTX     | 2025-11-03 | Before market open | Healthcare             | $25.0B       | $104.67 | nan%         | nan%         | nanx          |
| 17 | CIFR     | 2025-11-03 | Before market open | Financial Services     | $7.3B        | $19.07  | nan%         | nan%         | nanx          |
| 18 | CNA      | 2025-11-03 | Before market open | Financial Services     | $12.1B       | $44.61  | nan%         | nan%         | nanx          |
| 19 | ECX      | 2025-11-03 | Before market open | Consumer Cyclical      | $874.5M      | $2.38   | nan%         | nan%         | nanx          |
| 20 | FSTR     | 2025-11-03 | Before market open | Industrials            | $290.4M      | $27.09  | nan%         | nan%         | nanx          |
| 21 | FUBO     | 2025-11-03 | Before market open | Communication Services | $4.9B        | $3.66   | nan%         | nan%         | nanx          |
| 22 | GNE      | 2025-11-03 | Before market open | Utilities              | $402.0M      | $14.74  | nan%         | nan%         | nanx          |
| 23 | HESM     | 2025-11-03 | Before market open | Energy                 | $7.1B        | $34.14  | nan%         | nan%         | nanx          |
| 24 | III      | 2025-11-03 | Before market open | Technology             | $265.6M      | $5.47   | nan%         | nan%         | nanx          |
| 25 | IRMD     | 2025-11-03 | Before market open | Healthcare             | $977.0M      | $76.42  | nan%         | nan%         | nanx          |
| 26 | KOS      | 2025-11-03 | Before market open | Energy                 | $750.9M      | $1.55   | nan%         | nan%         | nanx          |
| 27 | KPTI     | 2025-11-03 | Before market open | Healthcare             | $92.4M       | $5.96   | nan%         | nan%         | nanx          |
| 28 | LQDA     | 2025-11-03 | Before market open | Healthcare             | $2.1B        | $23.20  | nan%         | nan%         | nanx          |
| 29 | NSSC     | 2025-11-03 | Before market open | Industrials            | $1.6B        | $43.78  | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
