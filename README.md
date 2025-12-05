# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-12-04 20:56:42 EST

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | DOCU     | 2025-12-04 | After market close | Technology             | $14.4B       | $70.62  | 31.37%       | 57.00%       | 1.82x         |
|  1 | COO      | 2025-12-04 | After market close | Healthcare             | $15.4B       | $75.98  | 26.06%       | 45.49%       | 1.75x         |
|  2 | ULTA     | 2025-12-04 | After market close | Consumer Cyclical      | $24.0B       | $544.52 | 26.08%       | 43.85%       | 1.68x         |
|  3 | HPE      | 2025-12-04 | After market close | Technology             | $30.2B       | $22.26  | 35.84%       | 51.88%       | 1.45x         |
|  4 | VSCO     | 2025-12-05 | Before market open | Consumer Cyclical      | $3.3B        | $42.51  | 57.45%       | 80.09%       | 1.39x         |
|  5 | AGX      | 2025-12-04 | After market close | Industrials            | $4.9B        | $351.09 | nan%         | nan%         | nanx          |
|  6 | CHPT     | 2025-12-04 | After market close | Consumer Cyclical      | $199.0M      | $8.35   | nan%         | nan%         | nanx          |
|  7 | DOMO     | 2025-12-04 | After market close | Technology             | $477.0M      | $11.71  | nan%         | nan%         | nanx          |
|  8 | IDT      | 2025-12-04 | After market close | Communication Services | $1.3B        | $50.05  | nan%         | nan%         | nanx          |
|  9 | IOT      | 2025-12-04 | After market close | Technology             | $23.4B       | $39.01  | nan%         | nan%         | nanx          |
| 10 | KNOP     | 2025-12-05 | Before market open | Energy                 | $352.9M      | $10.03  | nan%         | nan%         | nanx          |
| 11 | MNY      | 2025-12-05 | Before market open | Communication Services | $69.2M       | $1.45   | nan%         | nan%         | nanx          |
| 12 | RBRK     | 2025-12-04 | After market close | Technology             | $13.9B       | $71.41  | nan%         | nan%         | nanx          |
| 13 | S        | 2025-12-04 | After market close | Technology             | $5.7B        | $16.96  | nan%         | nan%         | nanx          |
| 14 | SFIX     | 2025-12-04 | After market close | Consumer Cyclical      | $629.3M      | $4.56   | nan%         | nan%         | nanx          |
| 15 | SPWH     | 2025-12-04 | After market close | Consumer Cyclical      | $94.2M       | $2.41   | nan%         | nan%         | nanx          |
| 16 | SWBI     | 2025-12-04 | After market close | Industrials            | $395.1M      | $8.88   | nan%         | nan%         | nanx          |
| 17 | TOUR     | 2025-12-05 | Before market open | Consumer Cyclical      | $90.2M       | $0.72   | nan%         | nan%         | nanx          |
| 18 | TTAN     | 2025-12-04 | After market close | Technology             | $8.9B        | $93.31  | nan%         | nan%         | nanx          |
| 19 | ZUMZ     | 2025-12-04 | After market close | Consumer Cyclical      | $467.6M      | $27.75  | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
