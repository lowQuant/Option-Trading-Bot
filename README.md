# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-09-08 21:45:48 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | CASY     | 2025-09-08 | After market close | Consumer Cyclical      | $19.4B       | $505.64 | 12.65%       | 37.85%       | 2.99x         |
|  1 | CNM      | 2025-09-09 | Before market open | Industrials            | $13.1B       | $66.98  | 20.01%       | 43.99%       | 2.20x         |
|  2 | KFY      | 2025-09-09 | Before market open | Industrials            | $3.8B        | $73.23  | 24.07%       | 32.18%       | 1.34x         |
|  3 | AVO      | 2025-09-08 | After market close | Consumer Defensive     | $908.9M      | $12.63  | nan%         | nan%         | nanx          |
|  4 | BIOX     | 2025-09-09 | Before market open | Basic Materials        | $161.0M      | $2.71   | nan%         | nan%         | nanx          |
|  5 | CGNT     | 2025-09-09 | Before market open | Technology             | $695.4M      | $9.01   | nan%         | nan%         | nanx          |
|  6 | DBI      | 2025-09-09 | Before market open | Consumer Cyclical      | $230.9M      | $4.73   | nan%         | nan%         | nanx          |
|  7 | FCEL     | 2025-09-09 | Before market open | Industrials            | $96.2M       | $4.05   | nan%         | nan%         | nanx          |
|  8 | GMHS     | 2025-09-09 | Before market open | Communication Services | $92.7M       | $1.92   | nan%         | nan%         | nanx          |
|  9 | MAMA     | 2025-09-08 | After market close | Consumer Defensive     | $373.9M      | $9.44   | nan%         | nan%         | nanx          |
| 10 | MOMO     | 2025-09-09 | Before market open | Communication Services | $1.3B        | $8.52   | nan%         | nan%         | nanx          |
| 11 | SAIL     | 2025-09-09 | Before market open | Technology             | $12.5B       | $21.98  | nan%         | nan%         | nanx          |
| 12 | SI       | 2025-09-09 | Before market open | nan                    | $321.6M      | $14.85  | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
