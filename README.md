# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-08-13 21:58:30 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector             | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | SPTN     | 2025-08-14 | Before market open | Consumer Defensive | $899.3M      | $26.56  | 1.96%        | 17.42%       | 8.89x         |
|  1 | COHR     | 2025-08-13 | After market close | Technology         | $17.7B       | $116.56 | 37.07%       | 60.39%       | 1.63x         |
|  2 | CSCO     | 2025-08-13 | After market close | Technology         | $278.8B      | $71.38  | 17.95%       | 28.19%       | 1.57x         |
|  3 | AMCR     | 2025-08-14 | Before market open | Consumer Cyclical  | $22.8B       | $9.77   | 21.18%       | 32.13%       | 1.52x         |
|  4 | TPR      | 2025-08-14 | Before market open | Consumer Cyclical  | $23.6B       | $110.86 | 31.66%       | 46.44%       | 1.47x         |
|  5 | AIT      | 2025-08-14 | Before market open | Industrials        | $10.5B       | $270.68 | 22.56%       | 28.66%       | 1.27x         |
|  6 | DE       | 2025-08-14 | Before market open | Industrials        | $139.1B      | $505.85 | 24.15%       | 30.51%       | 1.26x         |
|  7 | AAP      | 2025-08-14 | Before market open | Consumer Cyclical  | $3.7B        | $59.11  | 59.53%       | 69.34%       | 1.16x         |
|  8 | AEMD     | 2025-08-13 | After market close | Healthcare         | $2.5M        | $1.26   | nan%         | nan%         | nanx          |
|  9 | AFCG     | 2025-08-14 | Before market open | Real Estate        | $103.0M      | $4.78   | nan%         | nan%         | nanx          |
| 10 | AG       | 2025-08-14 | Before market open | Basic Materials    | $4.3B        | $8.95   | nan%         | nan%         | nanx          |
| 11 | ALLT     | 2025-08-14 | Before market open | Technology         | $365.7M      | $7.64   | nan%         | nan%         | nanx          |
| 12 | ALVO     | 2025-08-13 | After market close | Healthcare         | $2.8B        | $8.65   | nan%         | nan%         | nanx          |
| 13 | AQMS     | 2025-08-13 | After market close | Industrials        | $4.2M        | $4.16   | nan%         | nan%         | nanx          |
| 14 | ARAY     | 2025-08-13 | After market close | Healthcare         | $153.5M      | $1.48   | nan%         | nan%         | nanx          |
| 15 | ASM      | 2025-08-13 | After market close | Basic Materials    | $564.9M      | $3.91   | nan%         | nan%         | nanx          |
| 16 | ATER     | 2025-08-13 | After market close | Consumer Cyclical  | $12.9M       | $1.30   | nan%         | nan%         | nanx          |
| 17 | BEAT     | 2025-08-13 | After market close | Healthcare         | $40.6M       | $1.20   | nan%         | nan%         | nanx          |
| 18 | BFRI     | 2025-08-13 | After market close | Healthcare         | $9.6M        | $0.93   | nan%         | nan%         | nanx          |
| 19 | BIRK     | 2025-08-14 | Before market open | Consumer Cyclical  | $9.2B        | $49.14  | nan%         | nan%         | nanx          |
| 20 | BKTI     | 2025-08-14 | Before market open | Technology         | $162.2M      | $41.71  | nan%         | nan%         | nanx          |
| 21 | BLRX     | 2025-08-14 | Before market open | Healthcare         | $14.7M       | $3.65   | nan%         | nan%         | nanx          |
| 22 | BORR     | 2025-08-13 | After market close | Energy             | $747.0M      | $2.37   | nan%         | nan%         | nanx          |
| 23 | BRAG     | 2025-08-14 | Before market open | Consumer Cyclical  | $97.2M       | $4.01   | nan%         | nan%         | nanx          |
| 24 | BRFH     | 2025-08-13 | After market close | Consumer Defensive | $48.6M       | $3.03   | nan%         | nan%         | nanx          |
| 25 | CAN      | 2025-08-14 | Before market open | Technology         | $375.3M      | $0.75   | nan%         | nan%         | nanx          |
| 26 | CAPR     | 2025-08-13 | After market close | Healthcare         | $379.5M      | $8.04   | nan%         | nan%         | nanx          |
| 27 | CCAP     | 2025-08-13 | After market close | Financial Services | $546.7M      | $14.60  | nan%         | nan%         | nanx          |
| 28 | CDXS     | 2025-08-13 | After market close | Healthcare         | $252.7M      | $2.86   | nan%         | nan%         | nanx          |
| 29 | CIG      | 2025-08-14 | Before market open | Utilities          | $6.3B        | $1.99   | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
