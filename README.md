# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-05-14 21:50:17 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | NXT      | 2025-05-14 | After market close | Technology             | $8.1B        | $54.09  | 60.06%       | 63.71%       | 1.06x         |
|  1 | JACK     | 2025-05-14 | After market close | Consumer Cyclical      | $484.1M      | $26.07  | 69.33%       | 66.57%       | 0.96x         |
|  2 | STE      | 2025-05-14 | After market close | Healthcare             | $22.4B       | $231.15 | 30.93%       | 29.24%       | 0.95x         |
|  3 | DXC      | 2025-05-14 | After market close | Technology             | $3.0B        | $16.94  | 61.88%       | 55.83%       | 0.90x         |
|  4 | WMT      | 2025-05-15 | Before market open | Consumer Defensive     | $774.7B      | $95.88  | 37.74%       | 33.64%       | 0.89x         |
|  5 | HWKN     | 2025-05-14 | After market close | Basic Materials        | $2.5B        | $120.29 | 44.57%       | 37.36%       | 0.84x         |
|  6 | WMS      | 2025-05-15 | Before market open | Industrials            | $9.4B        | $123.55 | 53.60%       | 43.84%       | 0.82x         |
|  7 | DE       | 2025-05-15 | Before market open | Industrials            | $135.0B      | $498.57 | 42.78%       | 32.10%       | 0.75x         |
|  8 | CSCO     | 2025-05-14 | After market close | Technology             | $245.8B      | $61.78  | 42.59%       | 27.26%       | 0.64x         |
|  9 | BOOT     | 2025-05-14 | After market close | Consumer Cyclical      | $4.1B        | $135.10 | 86.07%       | 55.08%       | 0.64x         |
| 10 | AEVA     | 2025-05-14 | After market close | Technology             | $794.9M      | $13.54  | nan%         | nan%         | nanx          |
| 11 | ATER     | 2025-05-14 | After market close | Consumer Cyclical      | $18.5M       | $2.10   | nan%         | nan%         | nanx          |
| 12 | AYTU     | 2025-05-14 | After market close | Healthcare             | $8.3M        | $1.31   | nan%         | nan%         | nanx          |
| 13 | BABA     | 2025-05-15 | Before market open | Consumer Cyclical      | $319.8B      | $131.65 | nan%         | nan%         | nanx          |
| 14 | BCLI     | 2025-05-15 | Before market open | Healthcare             | $7.4M        | $1.21   | nan%         | nan%         | nanx          |
| 15 | BEKE     | 2025-05-15 | Before market open | Real Estate            | $23.7B       | $20.00  | nan%         | nan%         | nanx          |
| 16 | BIRK     | 2025-05-15 | Before market open | Consumer Cyclical      | $10.2B       | $54.08  | nan%         | nan%         | nanx          |
| 17 | BLTE     | 2025-05-14 | After market close | Healthcare             | $2.0B        | $60.89  | nan%         | nan%         | nanx          |
| 18 | BNGO     | 2025-05-14 | After market close | Healthcare             | $11.6M       | $3.95   | nan%         | nan%         | nanx          |
| 19 | BODI     | 2025-05-14 | After market close | Communication Services | $33.0M       | $5.16   | nan%         | nan%         | nanx          |
| 20 | BRAG     | 2025-05-15 | Before market open | Consumer Cyclical      | $113.8M      | $4.63   | nan%         | nan%         | nanx          |
| 21 | BTDR     | 2025-05-15 | Before market open | Technology             | $2.7B        | $14.43  | nan%         | nan%         | nanx          |
| 22 | BTM      | 2025-05-15 | Before market open | Financial Services     | $38.4M       | $1.77   | nan%         | nan%         | nanx          |
| 23 | BZAI     | 2025-05-14 | After market close | Technology             | $287.8M      | $2.83   | nan%         | nan%         | nanx          |
| 24 | CCAP     | 2025-05-14 | After market close | Financial Services     | $621.5M      | $16.77  | nan%         | nan%         | nanx          |
| 25 | CDXS     | 2025-05-14 | After market close | Healthcare             | $204.6M      | $2.56   | nan%         | nan%         | nanx          |
| 26 | CELC     | 2025-05-14 | After market close | Healthcare             | $410.9M      | $10.82  | nan%         | nan%         | nanx          |
| 27 | CLSD     | 2025-05-14 | After market close | Healthcare             | $66.0M       | $0.90   | nan%         | nan%         | nanx          |
| 28 | CRWV     | 2025-05-14 | After market close | Technology             | $29.4B       | $63.26  | nan%         | nan%         | nanx          |
| 29 | CSIQ     | 2025-05-15 | Before market open | Technology             | $677.0M      | $10.15  | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
