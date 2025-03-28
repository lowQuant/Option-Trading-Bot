# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-03-27 21:44:40 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | AIR      | 2025-03-27 | After market close | Industrials            | $2.5B        | $69.70  | 25.26%       | 42.24%       | 1.67x         |
|  1 | LULU     | 2025-03-27 | After market close | Consumer Cyclical      | $41.1B       | $337.79 | 37.47%       | 56.28%       | 1.50x         |
|  2 | OXM      | 2025-03-27 | After market close | Consumer Cyclical      | $981.9M      | $61.77  | 42.61%       | 46.93%       | 1.10x         |
|  3 | ABL      | 2025-03-27 | After market close | Financial Services     | $696.8M      | $7.21   | nan%         | nan%         | nanx          |
|  4 | AGX      | 2025-03-27 | After market close | Industrials            | $1.6B        | $119.52 | nan%         | nan%         | nanx          |
|  5 | BCAB     | 2025-03-27 | After market close | Healthcare             | $22.8M       | $0.37   | nan%         | nan%         | nanx          |
|  6 | BODI     | 2025-03-27 | After market close | Communication Services | $52.2M       | $7.54   | nan%         | nan%         | nanx          |
|  7 | BRFH     | 2025-03-27 | After market close | Consumer Defensive     | $53.9M       | $3.33   | nan%         | nan%         | nanx          |
|  8 | BRZE     | 2025-03-27 | After market close | Technology             | $3.9B        | $37.33  | nan%         | nan%         | nanx          |
|  9 | BTTR     | 2025-03-27 | After market close | Consumer Defensive     | $3.8M        | $1.90   | nan%         | nan%         | nanx          |
| 10 | BZAI     | 2025-03-27 | After market close | Technology             | $282.6M      | $2.76   | nan%         | nan%         | nanx          |
| 11 | CAAS     | 2025-03-28 | Before market open | Consumer Cyclical      | $158.8M      | $4.82   | nan%         | nan%         | nanx          |
| 12 | CCG      | 2025-03-28 | Before market open | Communication Services | $103.3M      | $1.04   | nan%         | nan%         | nanx          |
| 13 | CLSD     | 2025-03-27 | After market close | Healthcare             | $78.1M       | $1.02   | nan%         | nan%         | nanx          |
| 14 | CODX     | 2025-03-27 | After market close | Healthcare             | $13.3M       | $0.41   | nan%         | nan%         | nanx          |
| 15 | FORA     | 2025-03-27 | After market close | Healthcare             | $63.9M       | $2.04   | nan%         | nan%         | nanx          |
| 16 | FTLF     | 2025-03-27 | After market close | Consumer Defensive     | $128.2M      | $13.96  | nan%         | nan%         | nanx          |
| 17 | GOVX     | 2025-03-27 | After market close | Healthcare             | $12.9M       | $1.37   | nan%         | nan%         | nanx          |
| 18 | HQI      | 2025-03-27 | After market close | Industrials            | $188.5M      | $13.18  | nan%         | nan%         | nanx          |
| 19 | IPA      | 2025-03-28 | Before market open | Healthcare             | $20.2M       | $0.43   | nan%         | nan%         | nanx          |
| 20 | IRIX     | 2025-03-27 | After market close | Healthcare             | $15.0M       | $0.90   | nan%         | nan%         | nanx          |
| 21 | KPLT     | 2025-03-28 | Before market open | Technology             | $64.8M       | $14.77  | nan%         | nan%         | nanx          |
| 22 | KULR     | 2025-03-27 | After market close | Technology             | $373.3M      | $1.56   | nan%         | nan%         | nanx          |
| 23 | LTRN     | 2025-03-27 | After market close | Healthcare             | $40.1M       | $3.65   | nan%         | nan%         | nanx          |
| 24 | LVLU     | 2025-03-27 | After market close | Consumer Cyclical      | $18.5M       | $0.44   | nan%         | nan%         | nanx          |
| 25 | MDAI     | 2025-03-27 | After market close | Healthcare             | $29.7M       | $1.34   | nan%         | nan%         | nanx          |
| 26 | NUTX     | 2025-03-27 | After market close | Healthcare             | $306.3M      | $56.33  | nan%         | nan%         | nanx          |
| 27 | PIII     | 2025-03-27 | After market close | Healthcare             | $98.9M       | $0.18   | nan%         | nan%         | nanx          |
| 28 | PLSE     | 2025-03-27 | After market close | Healthcare             | $972.0M      | $15.80  | nan%         | nan%         | nanx          |
| 29 | PSTV     | 2025-03-27 | After market close | Healthcare             | $9.0M        | $1.47   | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
