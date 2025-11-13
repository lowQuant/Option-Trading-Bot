# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-11-12 20:54:21 EST

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | DIS      | 2025-11-13 | Before market open | Communication Services | $209.7B      | $114.85 | 16.87%       | 40.54%       | 2.40x         |
|  1 | TTEK     | 2025-11-12 | After market close | Industrials            | $8.5B        | $31.99  | 25.59%       | 52.83%       | 2.06x         |
|  2 | CSCO     | 2025-11-12 | After market close | Technology             | $291.5B      | $71.71  | 21.32%       | 35.39%       | 1.66x         |
|  3 | DGII     | 2025-11-12 | After market close | Technology             | $1.3B        | $35.69  | 30.19%       | 43.68%       | 1.45x         |
|  4 | SBH      | 2025-11-13 | Before market open | Consumer Cyclical      | $1.5B        | $14.57  | 47.89%       | 60.89%       | 1.27x         |
|  5 | HZO      | 2025-11-13 | Before market open | Consumer Cyclical      | $504.0M      | $23.53  | 63.37%       | 75.92%       | 1.20x         |
|  6 | ABSI     | 2025-11-12 | After market close | Healthcare             | $508.4M      | $3.45   | nan%         | nan%         | nanx          |
|  7 | AEBI     | 2025-11-13 | Before market open | Industrials            | $829.5M      | $10.56  | nan%         | nan%         | nanx          |
|  8 | AEG      | 2025-11-13 | Before market open | Financial Services     | $12.3B       | $7.74   | nan%         | nan%         | nanx          |
|  9 | AENT     | 2025-11-12 | After market close | Communication Services | $338.2M      | $6.75   | nan%         | nan%         | nanx          |
| 10 | AIRG     | 2025-11-12 | After market close | Technology             | $45.5M       | $3.99   | nan%         | nan%         | nanx          |
| 11 | ALH      | 2025-11-13 | Before market open | Consumer Cyclical      | $5.4B        | $26.58  | nan%         | nan%         | nanx          |
| 12 | ALMU     | 2025-11-12 | After market close | Technology             | $250.8M      | $14.40  | nan%         | nan%         | nanx          |
| 13 | ALVO     | 2025-11-12 | After market close | Healthcare             | $1.7B        | $5.58   | nan%         | nan%         | nanx          |
| 14 | AMS      | 2025-11-13 | Before market open | Healthcare             | $13.5M       | $2.08   | nan%         | nan%         | nanx          |
| 15 | AP       | 2025-11-12 | After market close | Industrials            | $38.8M       | $2.04   | nan%         | nan%         | nanx          |
| 16 | AQMS     | 2025-11-12 | After market close | Industrials            | $22.7M       | $6.58   | nan%         | nan%         | nanx          |
| 17 | ARDT     | 2025-11-12 | After market close | Healthcare             | $2.0B        | $14.05  | nan%         | nan%         | nanx          |
| 18 | ARX      | 2025-11-13 | Before market open | Financial Services     | $2.8B        | $12.54  | nan%         | nan%         | nanx          |
| 19 | ASND     | 2025-11-12 | After market close | Healthcare             | $12.1B       | $201.16 | nan%         | nan%         | nanx          |
| 20 | ATEX     | 2025-11-12 | After market close | Communication Services | $343.9M      | $18.00  | nan%         | nan%         | nanx          |
| 21 | AUID     | 2025-11-12 | After market close | Technology             | $37.2M       | $2.53   | nan%         | nan%         | nanx          |
| 22 | AVIR     | 2025-11-12 | After market close | Healthcare             | $277.8M      | $3.38   | nan%         | nan%         | nanx          |
| 23 | BCDA     | 2025-11-12 | After market close | Healthcare             | $13.8M       | $1.33   | nan%         | nan%         | nanx          |
| 24 | BETR     | 2025-11-13 | Before market open | Financial Services     | $908.1M      | $63.45  | nan%         | nan%         | nanx          |
| 25 | BILI     | 2025-11-13 | Before market open | Communication Services | $11.4B       | $27.14  | nan%         | nan%         | nanx          |
| 26 | BIOX     | 2025-11-13 | Before market open | Basic Materials        | $118.2M      | $1.93   | nan%         | nan%         | nanx          |
| 27 | BITF     | 2025-11-13 | Before market open | Financial Services     | $1.8B        | $3.37   | nan%         | nan%         | nanx          |
| 28 | BLDP     | 2025-11-13 | Before market open | Industrials            | $1.0B        | $3.57   | nan%         | nan%         | nanx          |
| 29 | BN       | 2025-11-13 | Before market open | Financial Services     | $105.2B      | $46.16  | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
