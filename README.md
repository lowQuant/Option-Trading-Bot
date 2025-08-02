# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-08-01 22:01:17 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | TSN      | 2025-08-04 | Before market open | Consumer Defensive     | $18.6B       | $52.30  | 20.00%       | 31.58%       | 1.58x         |
|  1 | IDXX     | 2025-08-04 | Before market open | Healthcare             | $43.1B       | $534.31 | 26.21%       | 39.16%       | 1.49x         |
|  2 | FRPT     | 2025-08-04 | Before market open | Consumer Defensive     | $3.2B        | $68.32  | 51.74%       | 73.26%       | 1.42x         |
|  3 | ON       | 2025-08-04 | Before market open | Technology             | $23.7B       | $56.36  | 41.78%       | 58.83%       | 1.41x         |
|  4 | SPNT     | 2025-08-04 | Before market open | Financial Services     | $2.3B        | $19.61  | 32.87%       | 44.08%       | 1.34x         |
|  5 | ENR      | 2025-08-04 | Before market open | Industrials            | $1.6B        | $22.52  | 37.45%       | 48.54%       | 1.30x         |
|  6 | L        | 2025-08-04 | Before market open | Financial Services     | $19.0B       | $90.54  | 15.90%       | 20.48%       | 1.29x         |
|  7 | BRKR     | 2025-08-04 | Before market open | Healthcare             | $5.8B        | $38.43  | 62.25%       | 69.76%       | 1.12x         |
|  8 | WAT      | 2025-08-04 | Before market open | Healthcare             | $17.3B       | $288.76 | 51.31%       | 37.94%       | 0.74x         |
|  9 | ALX      | 2025-08-04 | Before market open | Real Estate            | $1.3B        | $251.19 | nan%         | nan%         | nanx          |
| 10 | AXSM     | 2025-08-04 | Before market open | Healthcare             | $5.1B        | $101.38 | nan%         | nan%         | nanx          |
| 11 | BCRX     | 2025-08-04 | Before market open | Healthcare             | $1.7B        | $8.14   | nan%         | nan%         | nanx          |
| 12 | BNTX     | 2025-08-04 | Before market open | Healthcare             | $25.8B       | $107.50 | nan%         | nan%         | nanx          |
| 13 | CFBK     | 2025-08-04 | Before market open | Financial Services     | $152.3M      | $23.60  | nan%         | nan%         | nanx          |
| 14 | CNA      | 2025-08-04 | Before market open | Financial Services     | $11.9B       | $44.33  | nan%         | nan%         | nanx          |
| 15 | EEX      | 2025-08-04 | Before market open | Communication Services | $988.3M      | $4.97   | nan%         | nan%         | nanx          |
| 16 | HGTY     | 2025-08-04 | Before market open | Financial Services     | $3.5B        | $10.16  | nan%         | nan%         | nanx          |
| 17 | IEP      | 2025-08-04 | Before market open | Energy                 | $4.9B        | $9.13   | nan%         | nan%         | nanx          |
| 18 | KOS      | 2025-08-04 | Before market open | Energy                 | $1.0B        | $2.15   | nan%         | nan%         | nanx          |
| 19 | KSPI     | 2025-08-04 | Before market open | Technology             | $16.5B       | $78.90  | nan%         | nan%         | nanx          |
| 20 | LIND     | 2025-08-04 | Before market open | Consumer Cyclical      | $653.2M      | $11.95  | nan%         | nan%         | nanx          |
| 21 | RAND     | 2025-08-04 | Before market open | Financial Services     | $54.5M       | $18.34  | nan%         | nan%         | nanx          |
| 22 | TSEM     | 2025-08-04 | Before market open | Technology             | $5.3B        | $45.75  | nan%         | nan%         | nanx          |
| 23 | TWST     | 2025-08-04 | Before market open | Healthcare             | $2.0B        | $33.57  | nan%         | nan%         | nanx          |
| 24 | W        | 2025-08-04 | Before market open | Consumer Cyclical      | $8.4B        | $65.64  | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
