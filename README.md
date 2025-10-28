# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-10-27 21:48:15 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector             | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | INCY     | 2025-10-28 | Before market open | Healthcare         | $18.2B       | $91.28  | 21.71%       | 53.03%       | 2.44x         |
|  1 | AGYS     | 2025-10-27 | After market close | Technology         | $3.3B        | $116.53 | 26.50%       | 64.61%       | 2.44x         |
|  2 | BMRN     | 2025-10-27 | After market close | Healthcare         | $10.5B       | $54.48  | 20.55%       | 48.07%       | 2.34x         |
|  3 | UPS      | 2025-10-28 | Before market open | Industrials        | $73.9B       | $87.22  | 17.81%       | 41.48%       | 2.33x         |
|  4 | XYL      | 2025-10-28 | Before market open | Industrials        | $36.4B       | $148.25 | 13.69%       | 30.38%       | 2.22x         |
|  5 | AWI      | 2025-10-28 | Before market open | Industrials        | $8.8B        | $203.32 | 16.05%       | 34.41%       | 2.14x         |
|  6 | CAR      | 2025-10-27 | After market close | Industrials        | $5.5B        | $157.01 | 28.22%       | 57.39%       | 2.03x         |
|  7 | LEG      | 2025-10-27 | After market close | Consumer Cyclical  | $1.2B        | $9.12   | 29.75%       | 58.09%       | 1.95x         |
|  8 | SHW      | 2025-10-28 | Before market open | Basic Materials    | $83.8B       | $334.00 | 15.07%       | 28.96%       | 1.92x         |
|  9 | KRC      | 2025-10-27 | After market close | Real Estate        | $4.9B        | $40.89  | 17.10%       | 32.53%       | 1.90x         |
| 10 | CR       | 2025-10-27 | After market close | Industrials        | $11.0B       | $191.76 | 23.25%       | 43.85%       | 1.89x         |
| 11 | PHIN     | 2025-10-28 | Before market open | Consumer Cyclical  | $2.1B        | $54.70  | 19.98%       | 37.04%       | 1.85x         |
| 12 | WM       | 2025-10-27 | After market close | Industrials        | $86.5B       | $214.66 | 13.40%       | 24.68%       | 1.84x         |
| 13 | RCL      | 2025-10-28 | Before market open | Consumer Cyclical  | $87.0B       | $316.45 | 25.95%       | 47.18%       | 1.82x         |
| 14 | UNH      | 2025-10-28 | Before market open | Healthcare         | $331.5B      | $362.50 | 22.15%       | 39.68%       | 1.79x         |
| 15 | VFC      | 2025-10-28 | Before market open | Consumer Cyclical  | $6.5B        | $16.31  | 46.37%       | 80.60%       | 1.74x         |
| 16 | WHR      | 2025-10-27 | After market close | Consumer Cyclical  | $4.1B        | $73.66  | 30.02%       | 52.18%       | 1.74x         |
| 17 | UHS      | 2025-10-27 | After market close | Healthcare         | $13.4B       | $210.68 | 22.68%       | 39.41%       | 1.74x         |
| 18 | JBLU     | 2025-10-28 | Before market open | Industrials        | $1.7B        | $4.57   | 41.18%       | 71.05%       | 1.73x         |
| 19 | GPI      | 2025-10-28 | Before market open | Consumer Cyclical  | $5.4B        | $423.96 | 26.21%       | 44.98%       | 1.72x         |
| 20 | ALKS     | 2025-10-28 | Before market open | Healthcare         | $4.9B        | $29.80  | 34.34%       | 58.30%       | 1.70x         |
| 21 | SSD      | 2025-10-27 | After market close | Basic Materials    | $7.3B        | $175.32 | 21.12%       | 35.51%       | 1.68x         |
| 22 | GLW      | 2025-10-28 | Before market open | Technology         | $76.6B       | $87.41  | 30.05%       | 49.80%       | 1.66x         |
| 23 | HUBB     | 2025-10-28 | Before market open | Industrials        | $23.1B       | $434.39 | 23.56%       | 39.01%       | 1.66x         |
| 24 | THC      | 2025-10-28 | Before market open | Healthcare         | $19.1B       | $210.38 | 28.26%       | 45.42%       | 1.61x         |
| 25 | AXTA     | 2025-10-28 | Before market open | Basic Materials    | $6.3B        | $29.04  | 26.13%       | 41.96%       | 1.61x         |
| 26 | CARR     | 2025-10-28 | Before market open | Industrials        | $49.6B       | $57.84  | 26.02%       | 41.13%       | 1.58x         |
| 27 | LH       | 2025-10-28 | Before market open | Healthcare         | $23.2B       | $279.49 | 17.80%       | 27.34%       | 1.54x         |
| 28 | NXRT     | 2025-10-28 | Before market open | Real Estate        | $1.6B        | $31.48  | 22.67%       | 34.64%       | 1.53x         |
| 29 | HIG      | 2025-10-27 | After market close | Financial Services | $35.2B       | $125.11 | 17.66%       | 26.92%       | 1.52x         |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
