# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-07-23 22:04:51 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | IRDM     | 2025-07-24 | Before market open | Communication Services | $3.5B        | $31.88  | 25.90%       | 55.08%       | 2.13x         |
|  1 | FCN      | 2025-07-24 | Before market open | Industrials            | $5.7B        | $165.24 | 17.71%       | 37.36%       | 2.11x         |
|  2 | MAT      | 2025-07-23 | After market close | Consumer Cyclical      | $6.5B        | $19.89  | 23.40%       | 48.86%       | 2.09x         |
|  3 | WST      | 2025-07-24 | Before market open | Healthcare             | $16.3B       | $218.90 | 27.73%       | 57.52%       | 2.07x         |
|  4 | DCOM     | 2025-07-24 | Before market open | Financial Services     | $1.3B        | $28.37  | 32.06%       | 65.29%       | 2.04x         |
|  5 | WAB      | 2025-07-24 | Before market open | Industrials            | $36.7B       | $211.89 | 13.72%       | 27.76%       | 2.02x         |
|  6 | MXL      | 2025-07-23 | After market close | Technology             | $1.3B        | $15.44  | 45.07%       | 89.08%       | 1.98x         |
|  7 | ROL      | 2025-07-23 | After market close | Consumer Cyclical      | $26.7B       | $55.51  | 14.66%       | 28.70%       | 1.96x         |
|  8 | IBM      | 2025-07-23 | After market close | Technology             | $262.1B      | $281.96 | 18.40%       | 35.34%       | 1.92x         |
|  9 | DOV      | 2025-07-24 | Before market open | Industrials            | $26.2B       | $189.54 | 16.40%       | 30.55%       | 1.86x         |
| 10 | OII      | 2025-07-23 | After market close | Energy                 | $2.3B        | $21.13  | 29.34%       | 51.92%       | 1.77x         |
| 11 | GOOG     | 2025-07-23 | After market close | Communication Services | $2.3tr       | $192.11 | 22.38%       | 38.38%       | 1.71x         |
| 12 | RS       | 2025-07-23 | After market close | Basic Materials        | $18.1B       | $340.20 | 16.78%       | 28.76%       | 1.71x         |
| 13 | TXT      | 2025-07-24 | Before market open | Industrials            | $15.7B       | $86.04  | 16.19%       | 27.57%       | 1.70x         |
| 14 | NOW      | 2025-07-23 | After market close | Technology             | $198.1B      | $962.37 | 25.81%       | 43.62%       | 1.69x         |
| 15 | PHIN     | 2025-07-24 | Before market open | Consumer Cyclical      | $1.9B        | $47.77  | 25.95%       | 43.63%       | 1.68x         |
| 16 | FLEX     | 2025-07-24 | Before market open | Technology             | $20.1B       | $52.45  | 25.19%       | 41.87%       | 1.66x         |
| 17 | GSHD     | 2025-07-23 | After market close | Financial Services     | $3.9B        | $100.79 | 40.48%       | 66.53%       | 1.64x         |
| 18 | PLXS     | 2025-07-23 | After market close | Technology             | $3.6B        | $133.62 | 20.67%       | 33.87%       | 1.64x         |
| 19 | GOOGL    | 2025-07-23 | After market close | Communication Services | $2.3tr       | $191.34 | 23.17%       | 37.87%       | 1.63x         |
| 20 | HON      | 2025-07-24 | Before market open | Industrials            | $153.9B      | $236.58 | 14.96%       | 24.44%       | 1.63x         |
| 21 | EGBN     | 2025-07-23 | After market close | Financial Services     | $652.8M      | $21.35  | 39.76%       | 64.12%       | 1.61x         |
| 22 | NDAQ     | 2025-07-24 | Before market open | Financial Services     | $50.7B       | $88.93  | 14.64%       | 23.53%       | 1.61x         |
| 23 | KDP      | 2025-07-24 | Before market open | Consumer Defensive     | $45.5B       | $33.78  | 15.24%       | 24.49%       | 1.61x         |
| 24 | CNP      | 2025-07-24 | Before market open | Utilities              | $24.2B       | $37.76  | 14.19%       | 22.80%       | 1.61x         |
| 25 | ASGN     | 2025-07-23 | After market close | Technology             | $2.2B        | $49.73  | 37.78%       | 60.55%       | 1.60x         |
| 26 | ITGR     | 2025-07-24 | Before market open | Healthcare             | $4.0B        | $114.32 | 20.68%       | 33.09%       | 1.60x         |
| 27 | WEX      | 2025-07-23 | After market close | Technology             | $5.6B        | $160.68 | 27.95%       | 44.71%       | 1.60x         |
| 28 | RJF      | 2025-07-23 | After market close | Financial Services     | $32.5B       | $160.61 | 16.79%       | 26.85%       | 1.60x         |
| 29 | UNP      | 2025-07-24 | Before market open | Industrials            | $138.0B      | $229.24 | 15.31%       | 24.43%       | 1.60x         |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
