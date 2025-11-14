# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-11-13 20:53:39 EST

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | SR       | 2025-11-14 | Before market open | Utilities              | $5.3B        | $90.55  | 16.44%       | 18.80%       | 1.14x         |
|  1 | AMAT     | 2025-11-13 | After market close | Technology             | $177.8B      | $230.73 | 44.19%       | 47.47%       | 1.07x         |
|  2 | ABTC     | 2025-11-14 | Before market open | Financial Services     | $4.4B        | $4.93   | nan%         | nan%         | nanx          |
|  3 | ACOG     | 2025-11-13 | After market close | Healthcare             | $128.1M      | $6.12   | nan%         | nan%         | nanx          |
|  4 | AMPG     | 2025-11-14 | Before market open | Technology             | $54.9M       | $2.60   | nan%         | nan%         | nanx          |
|  5 | ANGX     | 2025-11-13 | After market close | Communication Services | $843.5M      | $5.36   | nan%         | nan%         | nanx          |
|  6 | ARAI     | 2025-11-14 | Before market open | Technology             | $126.5M      | $4.02   | nan%         | nan%         | nanx          |
|  7 | AREN     | 2025-11-13 | After market close | Communication Services | $189.9M      | $4.19   | nan%         | nan%         | nanx          |
|  8 | ATER     | 2025-11-13 | After market close | Consumer Cyclical      | $8.3M        | $0.85   | nan%         | nan%         | nanx          |
|  9 | AYTU     | 2025-11-13 | After market close | Healthcare             | $21.0M       | $2.06   | nan%         | nan%         | nanx          |
| 10 | BAP      | 2025-11-13 | After market close | Financial Services     | $20.0B       | $262.52 | nan%         | nan%         | nanx          |
| 11 | BCAB     | 2025-11-13 | After market close | Healthcare             | $38.7M       | $0.69   | nan%         | nan%         | nanx          |
| 12 | BEAT     | 2025-11-13 | After market close | Healthcare             | $53.9M       | $1.67   | nan%         | nan%         | nanx          |
| 13 | BHST     | 2025-11-13 | After market close | Consumer Defensive     | $163.8M      | $7.90   | nan%         | nan%         | nanx          |
| 14 | BNGO     | 2025-11-13 | After market close | Healthcare             | $14.2M       | $1.60   | nan%         | nan%         | nanx          |
| 15 | BZAI     | 2025-11-13 | After market close | Technology             | $274.0M      | $2.61   | nan%         | nan%         | nanx          |
| 16 | BZH      | 2025-11-13 | After market close | Consumer Cyclical      | $636.1M      | $21.78  | nan%         | nan%         | nanx          |
| 17 | CBUS     | 2025-11-13 | After market close | Healthcare             | $67.8M       | $1.35   | nan%         | nan%         | nanx          |
| 18 | CODX     | 2025-11-13 | After market close | Healthcare             | $22.4M       | $0.40   | nan%         | nan%         | nanx          |
| 19 | CTSO     | 2025-11-13 | After market close | Healthcare             | $41.8M       | $0.64   | nan%         | nan%         | nanx          |
| 20 | CV       | 2025-11-13 | After market close | Healthcare             | $265.2M      | $5.54   | nan%         | nan%         | nanx          |
| 21 | CWD      | 2025-11-13 | After market close | Financial Services     | $15.3M       | $3.02   | nan%         | nan%         | nanx          |
| 22 | DARE     | 2025-11-13 | After market close | Healthcare             | $25.5M       | $1.98   | nan%         | nan%         | nanx          |
| 23 | DGXX     | 2025-11-13 | After market close | Utilities              | $164.1M      | $4.09   | nan%         | nan%         | nanx          |
| 24 | DTST     | 2025-11-14 | Before market open | Technology             | $29.3M       | $4.11   | nan%         | nan%         | nanx          |
| 25 | EC       | 2025-11-13 | After market close | Energy                 | $20.6B       | $10.17  | nan%         | nan%         | nanx          |
| 26 | ETHZ     | 2025-11-14 | Before market open | Healthcare             | $258.5M      | $17.01  | nan%         | nan%         | nanx          |
| 27 | EVLV     | 2025-11-13 | After market close | Industrials            | $1.1B        | $6.72   | nan%         | nan%         | nanx          |
| 28 | FFAI     | 2025-11-13 | After market close | Consumer Cyclical      | $156.0M      | $1.11   | nan%         | nan%         | nanx          |
| 29 | FIGR     | 2025-11-13 | After market close | Financial Services     | $7.4B        | $37.31  | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
