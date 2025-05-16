# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-05-15 21:53:39 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | DOCS     | 2025-05-15 | After market close | Healthcare             | $11.0B       | $59.50  | 54.41%       | 75.97%       | 1.40x         |
|  1 | BRC      | 2025-05-16 | Before market open | Industrials            | $3.6B        | $74.28  | 31.32%       | 37.51%       | 1.20x         |
|  2 | FLO      | 2025-05-16 | Before market open | Consumer Defensive     | $3.6B        | $16.87  | 27.21%       | 28.97%       | 1.06x         |
|  3 | CAVA     | 2025-05-15 | After market close | Consumer Cyclical      | $11.5B       | $99.54  | 76.10%       | 69.29%       | 0.91x         |
|  4 | TTWO     | 2025-05-15 | After market close | Communication Services | $41.0B       | $229.50 | 44.29%       | 37.76%       | 0.85x         |
|  5 | RBC      | 2025-05-16 | Before market open | Industrials            | $11.5B       | $364.46 | 42.77%       | 29.56%       | 0.69x         |
|  6 | AMAT     | 2025-05-15 | After market close | Technology             | $142.0B      | $174.14 | 72.61%       | 42.32%       | 0.58x         |
|  7 | ACOG     | 2025-05-15 | After market close | Healthcare             | $109.9M      | $6.87   | nan%         | nan%         | nanx          |
|  8 | BAP      | 2025-05-15 | After market close | Financial Services     | $16.6B       | $207.91 | nan%         | nan%         | nanx          |
|  9 | BFRI     | 2025-05-15 | After market close | Healthcare             | $6.6M        | $0.70   | nan%         | nan%         | nanx          |
| 10 | BHST     | 2025-05-15 | After market close | Consumer Defensive     | $111.4M      | $6.55   | nan%         | nan%         | nanx          |
| 11 | BNZI     | 2025-05-15 | After market close | Technology             | $14.9M       | $1.01   | nan%         | nan%         | nanx          |
| 12 | CDRO     | 2025-05-16 | Before market open | Consumer Cyclical      | $369.7M      | $8.10   | nan%         | nan%         | nanx          |
| 13 | CWD      | 2025-05-15 | After market close | Financial Services     | $5.3M        | $4.02   | nan%         | nan%         | nanx          |
| 14 | DUOT     | 2025-05-15 | After market close | Technology             | $86.0M       | $7.25   | nan%         | nan%         | nanx          |
| 15 | FLD      | 2025-05-15 | After market close | Financial Services     | $188.0M      | $4.13   | nan%         | nan%         | nanx          |
| 16 | FTLF     | 2025-05-15 | After market close | Consumer Defensive     | $135.7M      | $14.86  | nan%         | nan%         | nanx          |
| 17 | GLOB     | 2025-05-15 | After market close | Technology             | $5.9B        | $133.67 | nan%         | nan%         | nanx          |
| 18 | IPW      | 2025-05-15 | After market close | Consumer Cyclical      | $19.2M       | $0.62   | nan%         | nan%         | nanx          |
| 19 | KORE     | 2025-05-15 | After market close | Communication Services | $36.0M       | $2.23   | nan%         | nan%         | nanx          |
| 20 | KULR     | 2025-05-15 | After market close | Technology             | $420.9M      | $1.61   | nan%         | nan%         | nanx          |
| 21 | LGCY     | 2025-05-15 | After market close | Consumer Defensive     | $96.3M       | $7.42   | nan%         | nan%         | nanx          |
| 22 | LPTH     | 2025-05-15 | After market close | Technology             | $107.7M      | $2.65   | nan%         | nan%         | nanx          |
| 23 | MHH      | 2025-05-16 | Before market open | Industrials            | $100.0M      | $8.21   | nan%         | nan%         | nanx          |
| 24 | NVVE     | 2025-05-15 | After market close | Consumer Cyclical      | $3.4M        | $1.10   | nan%         | nan%         | nanx          |
| 25 | ORGN     | 2025-05-15 | After market close | Basic Materials        | $101.1M      | $0.68   | nan%         | nan%         | nanx          |
| 26 | PLBY     | 2025-05-15 | After market close | Consumer Cyclical      | $109.9M      | $1.20   | nan%         | nan%         | nanx          |
| 27 | PRPO     | 2025-05-15 | After market close | Healthcare             | $10.8M       | $7.28   | nan%         | nan%         | nanx          |
| 28 | QSI      | 2025-05-15 | After market close | Healthcare             | $271.1M      | $1.52   | nan%         | nan%         | nanx          |
| 29 | QUBT     | 2025-05-15 | After market close | Technology             | $1.3B        | $8.93   | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
