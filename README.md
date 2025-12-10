# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-12-09 20:58:23 EST

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | GME      | 2025-12-09 | After market close | Consumer Cyclical      | $10.4B       | $23.35  | 26.71%       | 61.58%       | 2.31x         |
|  1 | PLAB     | 2025-12-10 | Before market open | Technology             | $1.5B        | $25.25  | 45.34%       | 76.98%       | 1.70x         |
|  2 | CHWY     | 2025-12-10 | Before market open | Consumer Cyclical      | $14.5B       | $34.62  | 33.07%       | 55.89%       | 1.69x         |
|  3 | CASY     | 2025-12-09 | After market close | Consumer Cyclical      | $20.9B       | $566.52 | 24.12%       | 37.53%       | 1.56x         |
|  4 | AVAV     | 2025-12-09 | After market close | Industrials            | $14.1B       | $282.47 | 49.24%       | 74.85%       | 1.52x         |
|  5 | CBRL     | 2025-12-09 | After market close | Consumer Cyclical      | $601.3M      | $26.62  | 53.92%       | 71.97%       | 1.33x         |
|  6 | PLAY     | 2025-12-09 | After market close | Communication Services | $623.0M      | $17.77  | 78.71%       | 100.14%      | 1.27x         |
|  7 | ALOT     | 2025-12-10 | Before market open | Technology             | $54.8M       | $7.01   | nan%         | nan%         | nanx          |
|  8 | AOUT     | 2025-12-09 | After market close | Consumer Cyclical      | $98.2M       | $7.20   | nan%         | nan%         | nanx          |
|  9 | BLLN     | 2025-12-09 | After market close | Healthcare             | $5.0B        | $104.66 | nan%         | nan%         | nanx          |
| 10 | BRZE     | 2025-12-09 | After market close | Technology             | $3.4B        | $30.03  | nan%         | nan%         | nanx          |
| 11 | DAKT     | 2025-12-10 | Before market open | Technology             | $882.7M      | $17.91  | nan%         | nan%         | nanx          |
| 12 | GNSS     | 2025-12-09 | After market close | Technology             | $107.9M      | $2.36   | nan%         | nan%         | nanx          |
| 13 | JILL     | 2025-12-10 | Before market open | Consumer Cyclical      | $252.0M      | $16.28  | nan%         | nan%         | nanx          |
| 14 | LAKE     | 2025-12-09 | After market close | Consumer Cyclical      | $143.7M      | $15.01  | nan%         | nan%         | nanx          |
| 15 | MIND     | 2025-12-09 | After market close | Technology             | $84.8M       | $10.57  | nan%         | nan%         | nanx          |
| 16 | MOMO     | 2025-12-10 | Before market open | Communication Services | $1.1B        | $7.06   | nan%         | nan%         | nanx          |
| 17 | UEC      | 2025-12-10 | Before market open | Energy                 | $6.7B        | $13.65  | nan%         | nan%         | nanx          |
| 18 | VBNK     | 2025-12-10 | Before market open | Financial Services     | $412.8M      | $12.39  | nan%         | nan%         | nanx          |
| 19 | YQ       | 2025-12-09 | After market close | Consumer Defensive     | $39.8M       | $4.79   | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
