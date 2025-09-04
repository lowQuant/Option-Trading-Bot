# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-09-03 21:41:55 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | GIII     | 2025-09-04 | Before market open | Consumer Cyclical      | $1.2B        | $27.03  | 26.38%       | 66.88%       | 2.54x         |
|  1 | WLY      | 2025-09-04 | Before market open | Communication Services | $2.1B        | $39.78  | 22.75%       | 50.15%       | 2.20x         |
|  2 | SAIC     | 2025-09-04 | Before market open | Technology             | $5.3B        | $118.27 | 18.63%       | 36.70%       | 1.97x         |
|  3 | CRM      | 2025-09-03 | After market close | Technology             | $245.2B      | $252.86 | 27.29%       | 44.85%       | 1.64x         |
|  4 | HPE      | 2025-09-03 | After market close | Technology             | $29.9B       | $22.68  | 28.22%       | 45.55%       | 1.61x         |
|  5 | CIEN     | 2025-09-04 | Before market open | Technology             | $13.4B       | $93.59  | 39.39%       | 60.75%       | 1.54x         |
|  6 | CAL      | 2025-09-04 | Before market open | Consumer Cyclical      | $505.3M      | $14.80  | 52.85%       | 79.59%       | 1.51x         |
|  7 | TTC      | 2025-09-04 | Before market open | Industrials            | $7.9B        | $81.44  | 26.84%       | 36.51%       | 1.36x         |
|  8 | SCVL     | 2025-09-04 | Before market open | Consumer Cyclical      | $588.5M      | $21.44  | 50.59%       | 67.78%       | 1.34x         |
|  9 | BRC      | 2025-09-04 | Before market open | Industrials            | $3.7B        | $77.79  | 17.73%       | 23.44%       | 1.32x         |
| 10 | AEO      | 2025-09-03 | After market close | Consumer Cyclical      | $2.4B        | $13.51  | 90.17%       | 74.40%       | 0.83x         |
| 11 | AI       | 2025-09-03 | After market close | Technology             | $2.3B        | $16.82  | nan%         | nan%         | nanx          |
| 12 | ASAN     | 2025-09-03 | After market close | Technology             | $3.3B        | $13.92  | nan%         | nan%         | nanx          |
| 13 | CHPT     | 2025-09-03 | After market close | Consumer Cyclical      | $251.8M      | $10.72  | nan%         | nan%         | nanx          |
| 14 | CRDO     | 2025-09-03 | After market close | Technology             | $21.6B       | $124.27 | nan%         | nan%         | nanx          |
| 15 | CRMT     | 2025-09-04 | Before market open | Consumer Cyclical      | $369.6M      | $45.09  | nan%         | nan%         | nanx          |
| 16 | DAVA     | 2025-09-04 | Before market open | Technology             | $855.0M      | $14.34  | nan%         | nan%         | nanx          |
| 17 | DLTH     | 2025-09-04 | Before market open | Consumer Cyclical      | $88.7M       | $2.37   | nan%         | nan%         | nanx          |
| 18 | DSGX     | 2025-09-03 | After market close | Technology             | $8.5B        | $98.40  | nan%         | nan%         | nanx          |
| 19 | FIG      | 2025-09-03 | After market close | Technology             | $33.4B       | $65.57  | nan%         | nan%         | nanx          |
| 20 | FLWS     | 2025-09-04 | Before market open | Consumer Cyclical      | $338.8M      | $5.58   | nan%         | nan%         | nanx          |
| 21 | GTLB     | 2025-09-03 | After market close | Technology             | $7.7B        | $47.69  | nan%         | nan%         | nanx          |
| 22 | MEI      | 2025-09-03 | After market close | Technology             | $274.0M      | $7.78   | nan%         | nan%         | nanx          |
| 23 | PD       | 2025-09-03 | After market close | Technology             | $1.4B        | $16.12  | nan%         | nan%         | nanx          |
| 24 | TLYS     | 2025-09-03 | After market close | Consumer Cyclical      | $54.0M       | $1.79   | nan%         | nan%         | nanx          |
| 25 | VBNK     | 2025-09-04 | Before market open | Financial Services     | $369.4M      | $11.02  | nan%         | nan%         | nanx          |
| 26 | WDH      | 2025-09-04 | Before market open | Financial Services     | $636.5M      | $1.76   | nan%         | nan%         | nanx          |
| 27 | WLYB     | 2025-09-04 | Before market open | Communication Services | $2.1B        | $39.43  | nan%         | nan%         | nanx          |
| 28 | YQ       | 2025-09-03 | After market close | Consumer Defensive     | $18.1M       | $1.99   | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
