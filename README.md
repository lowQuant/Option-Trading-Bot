# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-03-05 20:42:14 EST

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | WLY      | 2025-03-06 | Before market open | Communication Services | $2.0B        | $37.96  | 27.97%       | 58.42%       | 2.09x         |
|  1 | VSCO     | 2025-03-05 | After market close | Consumer Cyclical      | $1.7B        | $23.38  | 47.20%       | 97.27%       | 2.06x         |
|  2 | GMS      | 2025-03-06 | Before market open | Industrials            | $3.1B        | $78.19  | 24.07%       | 44.80%       | 1.86x         |
|  3 | BURL     | 2025-03-06 | Before market open | Consumer Cyclical      | $15.0B       | $230.27 | 34.27%       | 58.80%       | 1.72x         |
|  4 | KR       | 2025-03-06 | Before market open | Consumer Defensive     | $45.2B       | $63.18  | 20.80%       | 33.05%       | 1.59x         |
|  5 | TTC      | 2025-03-06 | Before market open | Industrials            | $7.8B        | $75.41  | 25.17%       | 39.71%       | 1.58x         |
|  6 | M        | 2025-03-06 | Before market open | Consumer Cyclical      | $3.7B        | $13.36  | 36.68%       | 57.43%       | 1.57x         |
|  7 | BJ       | 2025-03-06 | Before market open | Consumer Defensive     | $13.2B       | $101.09 | 27.93%       | 43.10%       | 1.54x         |
|  8 | CBRL     | 2025-03-06 | Before market open | Consumer Cyclical      | $896.8M      | $39.91  | 61.63%       | 69.28%       | 1.12x         |
|  9 | ACDC     | 2025-03-06 | Before market open | Energy                 | $1.0B        | $6.50   | nan%         | nan%         | nanx          |
| 10 | ACR      | 2025-03-05 | After market close | Real Estate            | $155.8M      | $20.50  | nan%         | nan%         | nanx          |
| 11 | ALNT     | 2025-03-05 | After market close | Technology             | $399.9M      | $23.22  | nan%         | nan%         | nanx          |
| 12 | ALTG     | 2025-03-05 | After market close | Industrials            | $169.6M      | $4.76   | nan%         | nan%         | nanx          |
| 13 | ALTO     | 2025-03-05 | After market close | Basic Materials        | $112.7M      | $1.44   | nan%         | nan%         | nanx          |
| 14 | ALXO     | 2025-03-06 | Before market open | Healthcare             | $54.9M       | $1.00   | nan%         | nan%         | nanx          |
| 15 | AMPY     | 2025-03-05 | After market close | Energy                 | $177.3M      | $4.55   | nan%         | nan%         | nanx          |
| 16 | AQST     | 2025-03-05 | After market close | Healthcare             | $254.4M      | $2.73   | nan%         | nan%         | nanx          |
| 17 | ARQ      | 2025-03-05 | After market close | Industrials            | $208.1M      | $4.69   | nan%         | nan%         | nanx          |
| 18 | AWRE     | 2025-03-05 | After market close | Technology             | $32.0M       | $1.49   | nan%         | nan%         | nanx          |
| 19 | BBAR     | 2025-03-05 | After market close | Financial Services     | $4.5B        | $18.36  | nan%         | nan%         | nanx          |
| 20 | BKSY     | 2025-03-06 | Before market open | Technology             | $406.3M      | $12.63  | nan%         | nan%         | nanx          |
| 21 | BTSG     | 2025-03-06 | Before market open | Healthcare             | $3.2B        | $18.15  | nan%         | nan%         | nanx          |
| 22 | CLMB     | 2025-03-05 | After market close | Technology             | $547.3M      | $117.75 | nan%         | nan%         | nanx          |
| 23 | CMPO     | 2025-03-05 | After market close | Industrials            | $1.2B        | $12.08  | nan%         | nan%         | nanx          |
| 24 | CNQ      | 2025-03-06 | Before market open | Energy                 | $58.0B       | $26.93  | nan%         | nan%         | nanx          |
| 25 | CRMT     | 2025-03-06 | Before market open | Consumer Cyclical      | $316.6M      | $38.00  | nan%         | nan%         | nanx          |
| 26 | CYN      | 2025-03-05 | After market close | Technology             | $11.2M       | $6.69   | nan%         | nan%         | nanx          |
| 27 | DCTH     | 2025-03-06 | Before market open | Healthcare             | $486.2M      | $13.77  | nan%         | nan%         | nanx          |
| 28 | DSGR     | 2025-03-06 | Before market open | Industrials            | $1.3B        | $28.09  | nan%         | nan%         | nanx          |
| 29 | DSGX     | 2025-03-05 | After market close | Technology             | $9.5B        | $108.88 | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
