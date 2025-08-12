# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-08-11 21:56:12 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | FWRD     | 2025-08-11 | After market close | Industrials            | $869.2M      | $30.25  | 44.88%       | 75.28%       | 1.68x         |
|  1 | CAH      | 2025-08-12 | Before market open | Healthcare             | $37.6B       | $157.41 | 18.93%       | 30.68%       | 1.62x         |
|  2 | MRCY     | 2025-08-11 | After market close | Industrials            | $3.2B        | $52.83  | 33.12%       | 50.32%       | 1.52x         |
|  3 | MSGS     | 2025-08-12 | Before market open | Communication Services | $4.9B        | $199.32 | 17.36%       | 26.34%       | 1.52x         |
|  4 | CE       | 2025-08-11 | After market close | Basic Materials        | $5.2B        | $48.05  | 48.65%       | 67.79%       | 1.39x         |
|  5 | HI       | 2025-08-11 | After market close | Industrials            | $1.4B        | $19.72  | 44.60%       | 58.40%       | 1.31x         |
|  6 | MAC      | 2025-08-11 | After market close | Real Estate            | $4.4B        | $16.69  | 30.01%       | 37.43%       | 1.25x         |
|  7 | ABOS     | 2025-08-12 | Before market open | Healthcare             | $86.0M       | $1.36   | nan%         | nan%         | nanx          |
|  8 | ABVX     | 2025-08-11 | After market close | Healthcare             | $5.3B        | $70.13  | nan%         | nan%         | nanx          |
|  9 | ACCS     | 2025-08-12 | Before market open | Communication Services | $46.6M       | $12.25  | nan%         | nan%         | nanx          |
| 10 | ACHR     | 2025-08-11 | After market close | Industrials            | $5.2B        | $9.72   | nan%         | nan%         | nanx          |
| 11 | ACVA     | 2025-08-11 | After market close | Consumer Cyclical      | $2.4B        | $13.62  | nan%         | nan%         | nanx          |
| 12 | ACXP     | 2025-08-12 | Before market open | Healthcare             | $6.9M        | $4.44   | nan%         | nan%         | nanx          |
| 13 | ADCT     | 2025-08-12 | Before market open | Healthcare             | $300.9M      | $2.68   | nan%         | nan%         | nanx          |
| 14 | AIV      | 2025-08-11 | After market close | Real Estate            | $1.1B        | $8.04   | nan%         | nan%         | nanx          |
| 15 | ALT      | 2025-08-12 | Before market open | Healthcare             | $274.1M      | $3.45   | nan%         | nan%         | nanx          |
| 16 | ALTI     | 2025-08-11 | After market close | Financial Services     | $651.0M      | $4.56   | nan%         | nan%         | nanx          |
| 17 | AMC      | 2025-08-11 | After market close | Communication Services | $1.3B        | $2.93   | nan%         | nan%         | nanx          |
| 18 | AQST     | 2025-08-11 | After market close | Healthcare             | $383.4M      | $3.90   | nan%         | nan%         | nanx          |
| 19 | ARCT     | 2025-08-11 | After market close | Healthcare             | $308.9M      | $11.91  | nan%         | nan%         | nanx          |
| 20 | ARIS     | 2025-08-11 | After market close | Utilities              | $1.4B        | $23.62  | nan%         | nan%         | nanx          |
| 21 | ARKR     | 2025-08-11 | After market close | Consumer Cyclical      | $25.3M       | $6.89   | nan%         | nan%         | nanx          |
| 22 | ARQ      | 2025-08-11 | After market close | Industrials            | $276.1M      | $6.62   | nan%         | nan%         | nanx          |
| 23 | ASIC     | 2025-08-11 | After market close | Financial Services     | $879.2M      | $19.09  | nan%         | nan%         | nanx          |
| 24 | ASRT     | 2025-08-11 | After market close | Healthcare             | $69.4M       | $0.73   | nan%         | nan%         | nanx          |
| 25 | AUTL     | 2025-08-12 | Before market open | Healthcare             | $657.4M      | $2.33   | nan%         | nan%         | nanx          |
| 26 | AVXL     | 2025-08-12 | Before market open | Healthcare             | $969.5M      | $11.08  | nan%         | nan%         | nanx          |
| 27 | BALY     | 2025-08-11 | After market close | Consumer Cyclical      | $487.7M      | $9.60   | nan%         | nan%         | nanx          |
| 28 | BBAI     | 2025-08-11 | After market close | Technology             | $2.1B        | $7.14   | nan%         | nan%         | nanx          |
| 29 | BBGI     | 2025-08-12 | Before market open | Communication Services | $7.7M        | $4.30   | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
