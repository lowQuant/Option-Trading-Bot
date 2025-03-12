# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-03-11 21:41:51 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | CXM      | 2025-03-12 | Before market open | Technology             | $2.1B        | $8.19   | 30.52%       | 67.69%       | 2.22x         |
|  1 | ABM      | 2025-03-12 | Before market open | Industrials            | $3.1B        | $51.25  | 27.58%       | 49.14%       | 1.78x         |
|  2 | CASY     | 2025-03-11 | After market close | Consumer Cyclical      | $13.8B       | $381.68 | 28.04%       | 44.46%       | 1.59x         |
|  3 | PRSU     | 2025-03-11 | After market close | Industrials            | $1.0B        | $37.85  | 32.88%       | 47.35%       | 1.44x         |
|  4 | AMRN     | 2025-03-12 | Before market open | Healthcare             | $193.5M      | $0.47   | nan%         | nan%         | nanx          |
|  5 | ARCO     | 2025-03-12 | Before market open | Consumer Cyclical      | $1.6B        | $7.91   | nan%         | nan%         | nanx          |
|  6 | ASM      | 2025-03-11 | After market close | Basic Materials        | $199.4M      | $1.30   | nan%         | nan%         | nanx          |
|  7 | BBCP     | 2025-03-11 | After market close | Industrials            | $321.0M      | $5.96   | nan%         | nan%         | nanx          |
|  8 | BIRD     | 2025-03-11 | After market close | Consumer Cyclical      | $48.9M       | $6.41   | nan%         | nan%         | nanx          |
|  9 | BWMN     | 2025-03-11 | After market close | Industrials            | $329.6M      | $18.39  | nan%         | nan%         | nanx          |
| 10 | CDRE     | 2025-03-11 | After market close | Industrials            | $1.4B        | $33.85  | nan%         | nan%         | nanx          |
| 11 | CURI     | 2025-03-11 | After market close | Communication Services | $117.1M      | $2.11   | nan%         | nan%         | nanx          |
| 12 | DTC      | 2025-03-12 | Before market open | Consumer Cyclical      | $38.4M       | $0.65   | nan%         | nan%         | nanx          |
| 13 | EH       | 2025-03-12 | Before market open | Industrials            | $1.4B        | $21.36  | nan%         | nan%         | nanx          |
| 14 | EML      | 2025-03-11 | After market close | Industrials            | $170.0M      | $27.68  | nan%         | nan%         | nanx          |
| 15 | FLX      | 2025-03-12 | Before market open | Industrials            | $618.2M      | $8.93   | nan%         | nan%         | nanx          |
| 16 | FOA      | 2025-03-11 | After market close | Financial Services     | $210.4M      | $20.74  | nan%         | nan%         | nanx          |
| 17 | GROV     | 2025-03-11 | After market close | Consumer Defensive     | $65.3M       | $1.62   | nan%         | nan%         | nanx          |
| 18 | GRPN     | 2025-03-11 | After market close | Communication Services | $388.5M      | $9.83   | nan%         | nan%         | nanx          |
| 19 | HBIO     | 2025-03-12 | Before market open | Healthcare             | $33.2M       | $0.77   | nan%         | nan%         | nanx          |
| 20 | HRTG     | 2025-03-11 | After market close | Financial Services     | $364.5M      | $11.30  | nan%         | nan%         | nanx          |
| 21 | IRBT     | 2025-03-12 | Before market open | Consumer Cyclical      | $192.8M      | $6.48   | nan%         | nan%         | nanx          |
| 22 | LDI      | 2025-03-11 | After market close | Financial Services     | $526.5M      | $1.70   | nan%         | nan%         | nanx          |
| 23 | MOMO     | 2025-03-12 | Before market open | Communication Services | $1.3B        | $7.31   | nan%         | nan%         | nanx          |
| 24 | MX       | 2025-03-12 | Before market open | Technology             | $150.3M      | $4.00   | nan%         | nan%         | nanx          |
| 25 | MXCT     | 2025-03-11 | After market close | Healthcare             | $376.8M      | $3.42   | nan%         | nan%         | nanx          |
| 26 | NATR     | 2025-03-11 | After market close | Consumer Defensive     | $267.9M      | $14.74  | nan%         | nan%         | nanx          |
| 27 | NESR     | 2025-03-12 | Before market open | Energy                 | $725.4M      | $7.52   | nan%         | nan%         | nanx          |
| 28 | NSPR     | 2025-03-12 | Before market open | Healthcare             | $72.8M       | $2.82   | nan%         | nan%         | nanx          |
| 29 | NVGS     | 2025-03-12 | Before market open | Energy                 | $957.8M      | $13.78  | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
