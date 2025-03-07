# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-03-06 20:42:46 EST

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close    | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:---------|:-------------|:-------------|:--------------|
|  0 | GAP      | 2025-03-06 | After market close | Consumer Cyclical      | $7.3B        | $19.84   | 37.89%       | 73.38%       | 1.94x         |
|  1 | GWRE     | 2025-03-06 | After market close | Technology             | $15.6B       | $197.41  | 39.30%       | 58.91%       | 1.50x         |
|  2 | HPE      | 2025-03-06 | After market close | Technology             | $23.6B       | $18.89   | 35.95%       | 51.79%       | 1.44x         |
|  3 | COO      | 2025-03-06 | After market close | Healthcare             | $18.2B       | $91.33   | 26.54%       | 36.34%       | 1.37x         |
|  4 | COST     | 2025-03-06 | After market close | Consumer Defensive     | $455.7B      | $1047.75 | 21.84%       | 29.30%       | 1.34x         |
|  5 | AVGO     | 2025-03-06 | After market close | Technology             | $843.8B      | $191.58  | 72.96%       | 60.04%       | 0.82x         |
|  6 | ADV      | 2025-03-07 | Before market open | Communication Services | $757.0M      | $2.39    | nan%         | nan%         | nanx          |
|  7 | AKA      | 2025-03-06 | After market close | Consumer Cyclical      | $161.8M      | $14.47   | nan%         | nan%         | nanx          |
|  8 | AOUT     | 2025-03-06 | After market close | Consumer Cyclical      | $192.6M      | $15.53   | nan%         | nan%         | nanx          |
|  9 | APEI     | 2025-03-06 | After market close | Consumer Defensive     | $341.0M      | $20.28   | nan%         | nan%         | nanx          |
| 10 | AQN      | 2025-03-07 | Before market open | Utilities              | $3.7B        | $4.82    | nan%         | nan%         | nanx          |
| 11 | ARCT     | 2025-03-06 | After market close | Healthcare             | $432.6M      | $16.05   | nan%         | nan%         | nanx          |
| 12 | ASLE     | 2025-03-06 | After market close | Industrials            | $376.2M      | $6.97    | nan%         | nan%         | nanx          |
| 13 | ASUR     | 2025-03-06 | After market close | Technology             | $257.3M      | $9.94    | nan%         | nan%         | nanx          |
| 14 | AVIR     | 2025-03-06 | After market close | Healthcare             | $253.4M      | $3.01    | nan%         | nan%         | nanx          |
| 15 | BBAI     | 2025-03-06 | After market close | Technology             | $1.1B        | $4.80    | nan%         | nan%         | nanx          |
| 16 | CLAR     | 2025-03-06 | After market close | Consumer Cyclical      | $163.4M      | $4.30    | nan%         | nan%         | nanx          |
| 17 | COOK     | 2025-03-06 | After market close | Consumer Cyclical      | $282.1M      | $2.24    | nan%         | nan%         | nanx          |
| 18 | CTMX     | 2025-03-06 | After market close | Healthcare             | $48.3M       | $0.62    | nan%         | nan%         | nanx          |
| 19 | CTSO     | 2025-03-06 | After market close | Healthcare             | $65.5M       | $1.14    | nan%         | nan%         | nanx          |
| 20 | DOMO     | 2025-03-06 | After market close | Technology             | $275.7M      | $7.73    | nan%         | nan%         | nanx          |
| 21 | ELUT     | 2025-03-06 | After market close | Healthcare             | $102.2M      | $2.81    | nan%         | nan%         | nanx          |
| 22 | ERO      | 2025-03-06 | After market close | Basic Materials        | $1.3B        | $12.36   | nan%         | nan%         | nanx          |
| 23 | FDUS     | 2025-03-06 | After market close | Financial Services     | $739.7M      | $22.22   | nan%         | nan%         | nanx          |
| 24 | FLL      | 2025-03-06 | After market close | Consumer Cyclical      | $147.7M      | $4.17    | nan%         | nan%         | nanx          |
| 25 | FNKO     | 2025-03-06 | After market close | Consumer Cyclical      | $561.6M      | $11.25   | nan%         | nan%         | nanx          |
| 26 | GCO      | 2025-03-07 | Before market open | Consumer Cyclical      | $363.3M      | $32.61   | nan%         | nan%         | nanx          |
| 27 | GENK     | 2025-03-06 | After market close | Consumer Cyclical      | $167.0M      | $5.33    | nan%         | nan%         | nanx          |
| 28 | GEVO     | 2025-03-06 | After market close | Basic Materials        | $299.3M      | $1.32    | nan%         | nan%         | nanx          |
| 29 | GHLD     | 2025-03-06 | After market close | Financial Services     | $810.7M      | $13.33   | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
