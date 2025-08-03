# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-08-02 22:21:56 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | TGTX     | 2025-08-04 | Before market open | Healthcare             | $5.6B        | $35.50  | 38.35%       | 81.16%       | 2.12x         |
|  1 | KRYS     | 2025-08-04 | Before market open | Healthcare             | $4.5B        | $153.87 | 30.71%       | 56.25%       | 1.83x         |
|  2 | TSN      | 2025-08-04 | Before market open | Consumer Defensive     | $18.7B       | $52.30  | 19.99%       | 31.17%       | 1.56x         |
|  3 | FRPT     | 2025-08-04 | Before market open | Consumer Defensive     | $3.2B        | $68.32  | 52.73%       | 79.08%       | 1.50x         |
|  4 | L        | 2025-08-04 | Before market open | Financial Services     | $18.9B       | $90.54  | 15.93%       | 23.53%       | 1.48x         |
|  5 | IDXX     | 2025-08-04 | Before market open | Healthcare             | $43.1B       | $534.31 | 26.20%       | 38.65%       | 1.48x         |
|  6 | ENR      | 2025-08-04 | Before market open | Industrials            | $1.6B        | $22.52  | 37.01%       | 53.83%       | 1.45x         |
|  7 | ON       | 2025-08-04 | Before market open | Technology             | $23.7B       | $56.36  | 41.57%       | 56.27%       | 1.35x         |
|  8 | SPNT     | 2025-08-04 | Before market open | Financial Services     | $2.3B        | $19.61  | 32.87%       | 44.34%       | 1.35x         |
|  9 | BRKR     | 2025-08-04 | Before market open | Healthcare             | $5.8B        | $38.43  | 62.03%       | 66.00%       | 1.06x         |
| 10 | WAT      | 2025-08-04 | Before market open | Healthcare             | $17.3B       | $288.76 | 51.40%       | 42.24%       | 0.82x         |
| 11 | ALX      | 2025-08-04 | Before market open | Real Estate            | $1.3B        | $251.19 | nan%         | nan%         | nanx          |
| 12 | AXSM     | 2025-08-04 | Before market open | Healthcare             | $5.1B        | $101.38 | nan%         | nan%         | nanx          |
| 13 | BCRX     | 2025-08-04 | Before market open | Healthcare             | $1.7B        | $8.14   | nan%         | nan%         | nanx          |
| 14 | BNTX     | 2025-08-04 | Before market open | Healthcare             | $25.8B       | $107.50 | nan%         | nan%         | nanx          |
| 15 | CFBK     | 2025-08-04 | Before market open | Financial Services     | $152.3M      | $23.60  | nan%         | nan%         | nanx          |
| 16 | CNA      | 2025-08-04 | Before market open | Financial Services     | $11.9B       | $44.33  | nan%         | nan%         | nanx          |
| 17 | EEX      | 2025-08-04 | Before market open | Communication Services | $966.5M      | $4.97   | nan%         | nan%         | nanx          |
| 18 | HGTY     | 2025-08-04 | Before market open | Financial Services     | $3.4B        | $10.16  | nan%         | nan%         | nanx          |
| 19 | IEP      | 2025-08-04 | Before market open | Energy                 | $4.9B        | $9.13   | nan%         | nan%         | nanx          |
| 20 | KOS      | 2025-08-04 | Before market open | Energy                 | $932.1M      | $2.15   | nan%         | nan%         | nanx          |
| 21 | KSPI     | 2025-08-04 | Before market open | Technology             | $16.4B       | $78.90  | nan%         | nan%         | nanx          |
| 22 | LIND     | 2025-08-04 | Before market open | Consumer Cyclical      | $641.7M      | $11.95  | nan%         | nan%         | nanx          |
| 23 | RAND     | 2025-08-04 | Before market open | Financial Services     | $54.1M       | $18.34  | nan%         | nan%         | nanx          |
| 24 | SOHU     | 2025-08-04 | Before market open | Communication Services | $463.0M      | $15.54  | nan%         | nan%         | nanx          |
| 25 | TSEM     | 2025-08-04 | Before market open | Technology             | $5.3B        | $45.75  | nan%         | nan%         | nanx          |
| 26 | TWST     | 2025-08-04 | Before market open | Healthcare             | $2.0B        | $33.57  | nan%         | nan%         | nanx          |
| 27 | W        | 2025-08-04 | Before market open | Consumer Cyclical      | $8.4B        | $65.64  | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
