# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-10-29 21:54:59 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | VRRM     | 2025-10-29 | After market close | Technology             | $3.8B        | $24.00  | 18.31%       | 50.24%       | 2.74x         |
|  1 | VIAV     | 2025-10-29 | After market close | Technology             | $3.1B        | $14.00  | 22.28%       | 60.13%       | 2.70x         |
|  2 | IRT      | 2025-10-29 | After market close | Real Estate            | $3.6B        | $15.79  | 14.38%       | 38.34%       | 2.67x         |
|  3 | DAY      | 2025-10-29 | After market close | Technology             | $10.8B       | $68.40  | 4.76%        | 12.61%       | 2.65x         |
|  4 | AMH      | 2025-10-29 | After market close | Real Estate            | $13.5B       | $32.61  | 14.88%       | 39.15%       | 2.63x         |
|  5 | INVH     | 2025-10-29 | After market close | Real Estate            | $16.8B       | $28.19  | 13.06%       | 34.27%       | 2.62x         |
|  6 | NSIT     | 2025-10-30 | Before market open | Technology             | $3.3B        | $105.00 | 19.31%       | 49.80%       | 2.58x         |
|  7 | EHC      | 2025-10-29 | After market close | Healthcare             | $12.7B       | $126.28 | 14.10%       | 35.89%       | 2.55x         |
|  8 | LKQ      | 2025-10-30 | Before market open | Consumer Cyclical      | $7.7B        | $30.96  | 20.96%       | 50.70%       | 2.42x         |
|  9 | PATK     | 2025-10-30 | Before market open | Consumer Cyclical      | $3.3B        | $104.75 | 20.73%       | 50.14%       | 2.42x         |
| 10 | ALGN     | 2025-10-29 | After market close | Healthcare             | $9.6B        | $133.14 | 27.77%       | 64.32%       | 2.32x         |
| 11 | MTG      | 2025-10-29 | After market close | Financial Services     | $6.1B        | $26.77  | 17.78%       | 40.39%       | 2.27x         |
| 12 | MAA      | 2025-10-29 | After market close | Real Estate            | $15.2B       | $130.71 | 11.12%       | 24.79%       | 2.23x         |
| 13 | DVA      | 2025-10-29 | After market close | Healthcare             | $9.0B        | $129.61 | 20.95%       | 45.31%       | 2.16x         |
| 14 | CNXN     | 2025-10-29 | After market close | Technology             | $1.5B        | $62.45  | 16.53%       | 35.60%       | 2.15x         |
| 15 | WAY      | 2025-10-29 | After market close | Healthcare             | $7.6B        | $39.49  | 25.47%       | 54.16%       | 2.13x         |
| 16 | CMCSA    | 2025-10-30 | Before market open | Communication Services | $105.3B      | $29.28  | 18.40%       | 38.87%       | 2.11x         |
| 17 | CALX     | 2025-10-29 | After market close | Technology             | $4.1B        | $61.78  | 25.77%       | 53.98%       | 2.09x         |
| 18 | JBSS     | 2025-10-29 | After market close | Consumer Defensive     | $692.8M      | $60.19  | 15.83%       | 33.10%       | 2.09x         |
| 19 | APTV     | 2025-10-30 | Before market open | Consumer Cyclical      | $18.7B       | $86.64  | 20.77%       | 42.69%       | 2.06x         |
| 20 | SCI      | 2025-10-29 | After market close | Consumer Cyclical      | $11.2B       | $80.84  | 15.52%       | 31.55%       | 2.03x         |
| 21 | TMDX     | 2025-10-29 | After market close | Healthcare             | $4.6B        | $129.71 | 41.31%       | 82.94%       | 2.01x         |
| 22 | MSFT     | 2025-10-29 | After market close | Technology             | $4.0tr       | $542.07 | 14.69%       | 29.28%       | 1.99x         |
| 23 | FMC      | 2025-10-29 | After market close | Basic Materials        | $3.6B        | $30.54  | 31.10%       | 61.34%       | 1.97x         |
| 24 | IP       | 2025-10-30 | Before market open | Consumer Cyclical      | $23.4B       | $47.13  | 21.65%       | 42.53%       | 1.96x         |
| 25 | PBI      | 2025-10-29 | After market close | Industrials            | $1.9B        | $11.79  | 29.23%       | 56.83%       | 1.94x         |
| 26 | OMCL     | 2025-10-30 | Before market open | Healthcare             | $1.4B        | $29.94  | 30.07%       | 58.29%       | 1.94x         |
| 27 | STAG     | 2025-10-29 | After market close | Real Estate            | $7.2B        | $38.12  | 17.83%       | 34.50%       | 1.93x         |
| 28 | NOW      | 2025-10-29 | After market close | Technology             | $189.2B      | $937.91 | 24.89%       | 48.09%       | 1.93x         |
| 29 | ITRI     | 2025-10-30 | Before market open | Technology             | $6.3B        | $133.95 | 27.45%       | 52.70%       | 1.92x         |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
