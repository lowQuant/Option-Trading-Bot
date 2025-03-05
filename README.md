# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-03-04 20:41:53 EST

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | JWN      | 2025-03-04 | After market close | Consumer Cyclical      | $4.0B        | $24.24  | 2.90%        | 10.93%       | 3.77x         |
|  1 | ANF      | 2025-03-05 | Before market open | Consumer Cyclical      | $4.8B        | $96.71  | 36.30%       | 78.41%       | 2.16x         |
|  2 | FL       | 2025-03-05 | Before market open | Consumer Cyclical      | $1.6B        | $17.88  | 40.45%       | 82.83%       | 2.05x         |
|  3 | BOX      | 2025-03-04 | After market close | Technology             | $4.8B        | $32.76  | 21.50%       | 43.99%       | 2.05x         |
|  4 | ROST     | 2025-03-04 | After market close | Consumer Cyclical      | $44.9B       | $136.81 | 19.73%       | 38.80%       | 1.97x         |
|  5 | THO      | 2025-03-05 | Before market open | Consumer Cyclical      | $5.1B        | $99.71  | 28.88%       | 52.38%       | 1.81x         |
|  6 | AVAV     | 2025-03-04 | After market close | Industrials            | $4.0B        | $142.63 | 47.93%       | 70.58%       | 1.47x         |
|  7 | BF.B     | 2025-03-05 | Before market open | nan                    | N/A          | $nan    | 27.81%       | 40.91%       | 1.47x         |
|  8 | CPB      | 2025-03-05 | Before market open | Consumer Defensive     | $12.0B       | $41.29  | 27.02%       | 33.69%       | 1.25x         |
|  9 | CRWD     | 2025-03-04 | After market close | Technology             | $96.1B       | $382.73 | 47.95%       | 58.65%       | 1.22x         |
| 10 | ACNT     | 2025-03-04 | After market close | Basic Materials        | $111.3M      | $11.07  | nan%         | nan%         | nanx          |
| 11 | ARBE     | 2025-03-05 | Before market open | Technology             | $158.6M      | $1.71   | nan%         | nan%         | nanx          |
| 12 | ATNI     | 2025-03-04 | After market close | Communication Services | $256.6M      | $16.66  | nan%         | nan%         | nanx          |
| 13 | ATRO     | 2025-03-04 | After market close | Industrials            | $694.5M      | $19.96  | nan%         | nan%         | nanx          |
| 14 | BF.A     | 2025-03-05 | Before market open | nan                    | N/A          | $nan    | nan%         | nan%         | nanx          |
| 15 | BTE      | 2025-03-04 | After market close | Energy                 | $1.6B        | $2.08   | nan%         | nan%         | nanx          |
| 16 | BWEN     | 2025-03-05 | Before market open | Industrials            | $33.2M       | $1.50   | nan%         | nan%         | nanx          |
| 17 | CDXC     | 2025-03-04 | After market close | Consumer Defensive     | $427.7M      | $5.50   | nan%         | nan%         | nanx          |
| 18 | CHPT     | 2025-03-04 | After market close | Consumer Cyclical      | $292.0M      | $0.60   | nan%         | nan%         | nanx          |
| 19 | CLPS     | 2025-03-05 | Before market open | Technology             | $34.8M       | $1.12   | nan%         | nan%         | nanx          |
| 20 | CPIX     | 2025-03-04 | After market close | Healthcare             | $85.0M       | $5.14   | nan%         | nan%         | nanx          |
| 21 | CRCT     | 2025-03-04 | After market close | Technology             | $1.1B        | $5.44   | nan%         | nan%         | nanx          |
| 22 | CRDO     | 2025-03-04 | After market close | Technology             | $9.1B        | $50.42  | nan%         | nan%         | nanx          |
| 23 | CSTE     | 2025-03-05 | Before market open | Industrials            | $126.4M      | $3.65   | nan%         | nan%         | nanx          |
| 24 | CTOS     | 2025-03-04 | After market close | Industrials            | $905.7M      | $4.14   | nan%         | nan%         | nanx          |
| 25 | CXDO     | 2025-03-04 | After market close | Communication Services | $156.4M      | $5.91   | nan%         | nan%         | nanx          |
| 26 | CYRX     | 2025-03-04 | After market close | Industrials            | $250.1M      | $4.79   | nan%         | nan%         | nanx          |
| 27 | DAKT     | 2025-03-05 | Before market open | Technology             | $722.5M      | $14.60  | nan%         | nan%         | nanx          |
| 28 | DIN      | 2025-03-05 | Before market open | Consumer Cyclical      | $357.8M      | $23.98  | nan%         | nan%         | nanx          |
| 29 | EC       | 2025-03-04 | After market close | Energy                 | $19.5B       | $9.47   | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
