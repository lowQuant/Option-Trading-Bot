# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-08-28 21:46:48 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector             | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | GAP      | 2025-08-28 | After market close | Consumer Cyclical  | $8.3B        | $22.30  | 29.62%       | 58.22%       | 1.97x         |
|  1 | ULTA     | 2025-08-28 | After market close | Consumer Cyclical  | $23.8B       | $533.81 | 20.77%       | 37.92%       | 1.83x         |
|  2 | ADSK     | 2025-08-28 | After market close | Technology         | $61.7B       | $285.95 | 22.59%       | 33.38%       | 1.48x         |
|  3 | DELL     | 2025-08-28 | After market close | Technology         | $89.6B       | $132.50 | 37.62%       | 49.50%       | 1.32x         |
|  4 | AFRM     | 2025-08-28 | After market close | Technology         | $25.8B       | $77.59  | nan%         | nan%         | nanx          |
|  5 | AMBA     | 2025-08-28 | After market close | Technology         | $3.0B        | $71.93  | nan%         | nan%         | nanx          |
|  6 | BABA     | 2025-08-29 | Before market open | Consumer Cyclical  | $297.3B      | $122.23 | nan%         | nan%         | nanx          |
|  7 | BULL     | 2025-08-28 | After market close | Technology         | $7.1B        | $14.44  | nan%         | nan%         | nanx          |
|  8 | CARL     | 2025-08-28 | After market close | Healthcare         | $363.0M      | $13.90  | nan%         | nan%         | nanx          |
|  9 | DOMO     | 2025-08-28 | After market close | Technology         | $616.4M      | $17.57  | nan%         | nan%         | nanx          |
| 10 | DOOO     | 2025-08-29 | Before market open | Consumer Cyclical  | $4.2B        | $57.03  | nan%         | nan%         | nanx          |
| 11 | ESTC     | 2025-08-28 | After market close | Technology         | $9.3B        | $83.30  | nan%         | nan%         | nanx          |
| 12 | IREN     | 2025-08-28 | After market close | Financial Services | $5.6B        | $22.36  | nan%         | nan%         | nanx          |
| 13 | LANV     | 2025-08-29 | Before market open | Consumer Cyclical  | $262.0M      | $2.02   | nan%         | nan%         | nanx          |
| 14 | LOT      | 2025-08-29 | Before market open | Consumer Cyclical  | $1.4B        | $2.19   | nan%         | nan%         | nanx          |
| 15 | MRVL     | 2025-08-28 | After market close | Technology         | $66.6B       | $74.79  | nan%         | nan%         | nanx          |
| 16 | S        | 2025-08-28 | After market close | Technology         | $5.9B        | $17.15  | nan%         | nan%         | nanx          |
| 17 | WOOF     | 2025-08-28 | After market close | Consumer Cyclical  | $892.8M      | $3.20   | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
