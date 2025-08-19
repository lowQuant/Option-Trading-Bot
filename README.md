# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-08-18 21:52:36 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | MDT      | 2025-08-19 | Before market open | Healthcare             | $118.9B      | $93.02  | 14.64%       | 26.03%       | 1.78x         |
|  1 | FN       | 2025-08-18 | After market close | Technology             | $11.7B       | $329.80 | 36.77%       | 64.96%       | 1.77x         |
|  2 | PINC     | 2025-08-19 | Before market open | Healthcare             | $2.0B        | $24.95  | 20.95%       | 36.03%       | 1.72x         |
|  3 | HD       | 2025-08-19 | Before market open | Consumer Cyclical      | $392.7B      | $399.38 | 20.30%       | 24.15%       | 1.19x         |
|  4 | PANW     | 2025-08-18 | After market close | Technology             | $117.7B      | $177.09 | 41.96%       | 43.78%       | 1.04x         |
|  5 | API      | 2025-08-18 | After market close | Technology             | $343.2M      | $3.67   | nan%         | nan%         | nanx          |
|  6 | AS       | 2025-08-19 | Before market open | Consumer Cyclical      | $21.5B       | $38.71  | nan%         | nan%         | nanx          |
|  7 | BLNK     | 2025-08-18 | After market close | Industrials            | $105.8M      | $0.94   | nan%         | nan%         | nanx          |
|  8 | EVGN     | 2025-08-19 | Before market open | Healthcare             | $11.6M       | $1.35   | nan%         | nan%         | nanx          |
|  9 | FFAI     | 2025-08-18 | After market close | Consumer Cyclical      | $270.4M      | $2.77   | nan%         | nan%         | nanx          |
| 10 | FLX      | 2025-08-19 | Before market open | Industrials            | $223.1M      | $3.15   | nan%         | nan%         | nanx          |
| 11 | FLXS     | 2025-08-18 | After market close | Consumer Cyclical      | $192.7M      | $35.21  | nan%         | nan%         | nanx          |
| 12 | ITRN     | 2025-08-19 | Before market open | Technology             | $801.3M      | $40.73  | nan%         | nan%         | nanx          |
| 13 | KNDI     | 2025-08-19 | Before market open | Consumer Cyclical      | $117.3M      | $1.28   | nan%         | nan%         | nanx          |
| 14 | NYXH     | 2025-08-18 | After market close | Healthcare             | $246.9M      | $6.22   | nan%         | nan%         | nanx          |
| 15 | OPRA     | 2025-08-19 | Before market open | Communication Services | $1.5B        | $16.32  | nan%         | nan%         | nanx          |
| 16 | SFL      | 2025-08-19 | Before market open | Industrials            | $1.2B        | $9.04   | nan%         | nan%         | nanx          |
| 17 | VIK      | 2025-08-19 | Before market open | Consumer Cyclical      | $26.7B       | $60.72  | nan%         | nan%         | nanx          |
| 18 | XP       | 2025-08-18 | After market close | Financial Services     | $9.2B        | $17.56  | nan%         | nan%         | nanx          |
| 19 | XPEV     | 2025-08-19 | Before market open | Consumer Cyclical      | $19.0B       | $19.70  | nan%         | nan%         | nanx          |
| 20 | XYF      | 2025-08-19 | Before market open | Financial Services     | $542.8M      | $13.48  | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
