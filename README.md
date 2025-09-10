# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-09-09 21:42:36 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector             | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | GME      | 2025-09-09 | After market close | Consumer Cyclical  | $10.6B       | $23.22  | 25.68%       | 65.93%       | 2.57x         |
|  1 | AVAV     | 2025-09-09 | After market close | Industrials        | $11.5B       | $236.91 | 35.84%       | 66.70%       | 1.86x         |
|  2 | ORCL     | 2025-09-09 | After market close | Technology         | $678.4B      | $238.48 | 37.39%       | 53.47%       | 1.43x         |
|  3 | CHWY     | 2025-09-10 | Before market open | Consumer Cyclical  | $17.4B       | $41.62  | 39.97%       | 56.31%       | 1.41x         |
|  4 | SNPS     | 2025-09-09 | After market close | Technology         | $111.8B      | $609.23 | 30.48%       | 37.74%       | 1.24x         |
|  5 | ALMU     | 2025-09-09 | After market close | Technology         | $289.0M      | $17.70  | nan%         | nan%         | nanx          |
|  6 | AMBR     | 2025-09-10 | Before market open | Technology         | $401.0M      | $4.43   | nan%         | nan%         | nanx          |
|  7 | AMRK     | 2025-09-09 | After market close | Financial Services | $602.1M      | $24.58  | nan%         | nan%         | nanx          |
|  8 | CVGW     | 2025-09-09 | After market close | Consumer Defensive | $491.2M      | $27.21  | nan%         | nan%         | nanx          |
|  9 | DAKT     | 2025-09-10 | Before market open | Technology         | $856.2M      | $17.62  | nan%         | nan%         | nanx          |
| 10 | INNV     | 2025-09-09 | After market close | Healthcare         | $576.5M      | $4.03   | nan%         | nan%         | nanx          |
| 11 | LAKE     | 2025-09-09 | After market close | Consumer Cyclical  | $137.4M      | $15.00  | nan%         | nan%         | nanx          |
| 12 | LE       | 2025-09-09 | After market close | Consumer Cyclical  | $432.4M      | $14.47  | nan%         | nan%         | nanx          |
| 13 | LMNR     | 2025-09-09 | After market close | Consumer Defensive | $284.2M      | $15.72  | nan%         | nan%         | nanx          |
| 14 | MEI      | 2025-09-09 | After market close | Technology         | $260.6M      | $7.25   | nan%         | nan%         | nanx          |
| 15 | MIND     | 2025-09-09 | After market close | Technology         | $76.2M       | $9.48   | nan%         | nan%         | nanx          |
| 16 | MTRX     | 2025-09-09 | After market close | Industrials        | $393.4M      | $14.71  | nan%         | nan%         | nanx          |
| 17 | RBRK     | 2025-09-09 | After market close | Technology         | $19.1B       | $95.61  | nan%         | nan%         | nanx          |
| 18 | SKIL     | 2025-09-09 | After market close | Consumer Defensive | $128.6M      | $15.03  | nan%         | nan%         | nanx          |
| 19 | TEN      | 2025-09-10 | Before market open | Energy             | $675.8M      | $22.91  | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
