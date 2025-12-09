# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-12-08 20:56:37 EST

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close    | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:---------|:-------------|:-------------|:--------------|
|  0 | GIII     | 2025-12-09 | Before market open | Consumer Cyclical      | $1.3B        | $30.38   | 30.47%       | 68.48%       | 2.25x         |
|  1 | CNM      | 2025-12-09 | Before market open | Industrials            | $10.0B       | $50.23   | 30.20%       | 49.38%       | 1.64x         |
|  2 | CPB      | 2025-12-09 | Before market open | Consumer Defensive     | $9.0B        | $29.60   | 23.94%       | 35.09%       | 1.47x         |
|  3 | AZO      | 2025-12-09 | Before market open | Consumer Cyclical      | $62.8B       | $3822.66 | 20.74%       | 29.71%       | 1.43x         |
|  4 | OLLI     | 2025-12-09 | Before market open | Consumer Defensive     | $7.3B        | $121.33  | 31.80%       | 44.60%       | 1.40x         |
|  5 | ASO      | 2025-12-09 | Before market open | Consumer Cyclical      | $3.3B        | $50.23   | 40.53%       | 56.34%       | 1.39x         |
|  6 | TOL      | 2025-12-08 | After market close | Consumer Cyclical      | $13.4B       | $138.94  | 29.49%       | 39.68%       | 1.35x         |
|  7 | KFY      | 2025-12-09 | Before market open | Industrials            | $3.4B        | $66.07   | 26.45%       | 33.92%       | 1.28x         |
|  8 | ARQQ     | 2025-12-09 | Before market open | Technology             | $453.1M      | $30.43   | nan%         | nan%         | nanx          |
|  9 | CAL      | 2025-12-09 | Before market open | Consumer Cyclical      | $456.5M      | $13.33   | nan%         | nan%         | nanx          |
| 10 | CGNT     | 2025-12-09 | Before market open | Technology             | $654.5M      | $8.65    | nan%         | nan%         | nanx          |
| 11 | CMP      | 2025-12-08 | After market close | Basic Materials        | $860.0M      | $20.28   | nan%         | nan%         | nanx          |
| 12 | DBI      | 2025-12-09 | Before market open | Consumer Cyclical      | $240.3M      | $4.88    | nan%         | nan%         | nanx          |
| 13 | ELWT     | 2025-12-08 | After market close | Communication Services | $38.9M       | $6.65    | nan%         | nan%         | nanx          |
| 14 | FERG     | 2025-12-09 | Before market open | Industrials            | $49.4B       | $248.38  | nan%         | nan%         | nanx          |
| 15 | LE       | 2025-12-09 | Before market open | Consumer Cyclical      | $487.0M      | $16.51   | nan%         | nan%         | nanx          |
| 16 | MAMA     | 2025-12-08 | After market close | Consumer Defensive     | $454.5M      | $11.47   | nan%         | nan%         | nanx          |
| 17 | ODC      | 2025-12-08 | After market close | Basic Materials        | $773.7M      | $53.59   | nan%         | nan%         | nanx          |
| 18 | OOMA     | 2025-12-08 | After market close | Technology             | $343.1M      | $11.74   | nan%         | nan%         | nanx          |
| 19 | PHR      | 2025-12-08 | After market close | Healthcare             | $1.2B        | $20.29   | nan%         | nan%         | nanx          |
| 20 | SAIL     | 2025-12-09 | Before market open | Technology             | $11.3B       | $20.24   | nan%         | nan%         | nanx          |
| 21 | SGU      | 2025-12-08 | After market close | Energy                 | $416.5M      | $11.79   | nan%         | nan%         | nanx          |
| 22 | THCH     | 2025-12-09 | Before market open | Consumer Cyclical      | $84.8M       | $2.68    | nan%         | nan%         | nanx          |
| 23 | VNCE     | 2025-12-09 | Before market open | Consumer Cyclical      | $41.5M       | $2.98    | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
