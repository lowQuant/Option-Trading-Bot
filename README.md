# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-03-18 21:43:49 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector             | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | SIG      | 2025-03-19 | Before market open | Consumer Cyclical  | $2.1B        | $48.35  | 48.61%       | 75.91%       | 1.56x         |
|  1 | OLLI     | 2025-03-19 | Before market open | Consumer Defensive | $6.1B        | $103.32 | 38.75%       | 56.71%       | 1.46x         |
|  2 | HQY      | 2025-03-18 | After market close | Healthcare         | $8.8B        | $100.72 | 33.74%       | 46.72%       | 1.38x         |
|  3 | GIS      | 2025-03-19 | Before market open | Consumer Defensive | $33.3B       | $60.94  | 32.60%       | 30.96%       | 0.95x         |
|  4 | ABSI     | 2025-03-18 | After market close | Healthcare         | $353.8M      | $3.21   | nan%         | nan%         | nanx          |
|  5 | ATER     | 2025-03-18 | After market close | Consumer Cyclical  | $18.5M       | $2.17   | nan%         | nan%         | nanx          |
|  6 | BETR     | 2025-03-18 | After market close | Financial Services | $174.2M      | $11.63  | nan%         | nan%         | nanx          |
|  7 | CAAP     | 2025-03-19 | Before market open | Industrials        | $3.1B        | $19.35  | nan%         | nan%         | nanx          |
|  8 | GDS      | 2025-03-19 | Before market open | Technology         | $6.7B        | $35.45  | nan%         | nan%         | nanx          |
|  9 | HCM      | 2025-03-19 | Before market open | Healthcare         | $2.7B        | $15.14  | nan%         | nan%         | nanx          |
| 10 | INO      | 2025-03-18 | After market close | Healthcare         | $76.5M       | $2.11   | nan%         | nan%         | nanx          |
| 11 | JILL     | 2025-03-19 | Before market open | Consumer Cyclical  | $285.5M      | $18.87  | nan%         | nan%         | nanx          |
| 12 | KC       | 2025-03-19 | Before market open | Technology         | $4.3B        | $18.03  | nan%         | nan%         | nanx          |
| 13 | LQDA     | 2025-03-19 | Before market open | Healthcare         | $1.2B        | $14.79  | nan%         | nan%         | nanx          |
| 14 | LX       | 2025-03-18 | After market close | Financial Services | $1.7B        | $10.53  | nan%         | nan%         | nanx          |
| 15 | MDWD     | 2025-03-19 | Before market open | Healthcare         | $207.9M      | $19.09  | nan%         | nan%         | nanx          |
| 16 | NYC      | 2025-03-19 | Before market open | Real Estate        | $26.6M       | $10.00  | nan%         | nan%         | nanx          |
| 17 | OABI     | 2025-03-18 | After market close | Healthcare         | $386.0M      | $3.17   | nan%         | nan%         | nanx          |
| 18 | OSS      | 2025-03-19 | Before market open | Technology         | $64.6M       | $2.97   | nan%         | nan%         | nanx          |
| 19 | SRAD     | 2025-03-19 | Before market open | Technology         | $6.0B        | $20.36  | nan%         | nan%         | nanx          |
| 20 | SRFM     | 2025-03-18 | After market close | Industrials        | $70.5M       | $4.16   | nan%         | nan%         | nanx          |
| 21 | STNE     | 2025-03-18 | After market close | Technology         | $3.0B        | $10.19  | nan%         | nan%         | nanx          |
| 22 | TRVI     | 2025-03-18 | After market close | Healthcare         | $586.2M      | $6.54   | nan%         | nan%         | nanx          |
| 23 | WALD     | 2025-03-18 | After market close | Consumer Defensive | $391.9M      | $3.19   | nan%         | nan%         | nanx          |
| 24 | ZTO      | 2025-03-18 | After market close | Industrials        | $17.0B       | $20.73  | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
