# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-03-13 21:41:35 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | DOCU     | 2025-03-13 | After market close | Technology             | $15.1B       | $80.13  | 25.82%       | 67.21%       | 2.60x         |
|  1 | BKE      | 2025-03-14 | Before market open | Consumer Cyclical      | $1.8B        | $36.13  | 25.31%       | 47.14%       | 1.86x         |
|  2 | GOGO     | 2025-03-14 | Before market open | Communication Services | $898.5M      | $6.95   | 59.70%       | 95.56%       | 1.60x         |
|  3 | ULTA     | 2025-03-13 | After market close | Consumer Cyclical      | $14.6B       | $329.23 | 33.70%       | 52.54%       | 1.56x         |
|  4 | SMTC     | 2025-03-13 | After market close | Technology             | $2.8B        | $33.85  | 138.77%      | 94.18%       | 0.68x         |
|  5 | AIRS     | 2025-03-14 | Before market open | Healthcare             | $170.2M      | $3.13   | nan%         | nan%         | nanx          |
|  6 | ALLO     | 2025-03-13 | After market close | Healthcare             | $396.3M      | $2.06   | nan%         | nan%         | nanx          |
|  7 | ALTI     | 2025-03-13 | After market close | Financial Services     | $423.7M      | $3.11   | nan%         | nan%         | nanx          |
|  8 | ATYR     | 2025-03-13 | After market close | Healthcare             | $334.9M      | $3.55   | nan%         | nan%         | nanx          |
|  9 | AUID     | 2025-03-13 | After market close | Technology             | $52.0M       | $4.77   | nan%         | nan%         | nanx          |
| 10 | AVD      | 2025-03-14 | Before market open | Basic Materials        | $135.3M      | $4.69   | nan%         | nan%         | nanx          |
| 11 | BEAT     | 2025-03-13 | After market close | Healthcare             | $68.1M       | $2.08   | nan%         | nan%         | nanx          |
| 12 | BLNK     | 2025-03-13 | After market close | Industrials            | $91.1M       | $0.98   | nan%         | nan%         | nanx          |
| 13 | EEX      | 2025-03-14 | Before market open | Communication Services | $740.9M      | $3.69   | nan%         | nan%         | nanx          |
| 14 | EGY      | 2025-03-13 | After market close | Energy                 | $398.3M      | $3.96   | nan%         | nan%         | nanx          |
| 15 | EVCM     | 2025-03-13 | After market close | Technology             | $1.6B        | $9.18   | nan%         | nan%         | nanx          |
| 16 | EVOK     | 2025-03-13 | After market close | Healthcare             | $5.7M        | $3.68   | nan%         | nan%         | nanx          |
| 17 | GRWG     | 2025-03-13 | After market close | Consumer Cyclical      | $57.6M       | $1.03   | nan%         | nan%         | nanx          |
| 18 | HGBL     | 2025-03-13 | After market close | Financial Services     | $76.0M       | $2.10   | nan%         | nan%         | nanx          |
| 19 | ILLM     | 2025-03-14 | Before market open | nan                    | N/A          | $nan    | nan%         | nan%         | nanx          |
| 20 | JYNT     | 2025-03-13 | After market close | Healthcare             | $157.9M      | $10.52  | nan%         | nan%         | nanx          |
| 21 | KINS     | 2025-03-13 | After market close | Financial Services     | $168.8M      | $14.27  | nan%         | nan%         | nanx          |
| 22 | KRT      | 2025-03-13 | After market close | Consumer Cyclical      | $579.7M      | $29.54  | nan%         | nan%         | nanx          |
| 23 | LI       | 2025-03-14 | Before market open | Consumer Cyclical      | $29.6B       | $29.73  | nan%         | nan%         | nanx          |
| 24 | LRFC     | 2025-03-13 | After market close | Financial Services     | $65.8M       | $24.40  | nan%         | nan%         | nanx          |
| 25 | MAPS     | 2025-03-13 | After market close | Technology             | $196.4M      | $1.18   | nan%         | nan%         | nanx          |
| 26 | NOTE     | 2025-03-13 | After market close | Technology             | $139.7M      | $1.04   | nan%         | nan%         | nanx          |
| 27 | NYXH     | 2025-03-13 | After market close | Healthcare             | $376.1M      | $9.75   | nan%         | nan%         | nanx          |
| 28 | OPAL     | 2025-03-13 | After market close | Utilities              | $375.0M      | $2.34   | nan%         | nan%         | nanx          |
| 29 | ORGN     | 2025-03-13 | After market close | Basic Materials        | $124.3M      | $0.81   | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
