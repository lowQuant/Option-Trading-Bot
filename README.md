# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-02-10 20:37:18 EST

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector             | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | HLIT     | 2025-02-10 | After market close | Technology         | $1.3B        | $11.13  | 30.80%       | 73.92%       | 2.40x         |
|  1 | ACLS     | 2025-02-10 | After market close | Technology         | $2.2B        | $63.87  | 31.32%       | 61.35%       | 1.96x         |
|  2 | MEDP     | 2025-02-10 | After market close | Healthcare         | $11.0B       | $354.10 | 28.59%       | 55.85%       | 1.95x         |
|  3 | CXW      | 2025-02-10 | After market close | Industrials        | $2.1B        | $18.43  | 35.89%       | 69.56%       | 1.94x         |
|  4 | LSCC     | 2025-02-10 | After market close | Technology         | $7.5B        | $53.29  | 34.00%       | 65.10%       | 1.91x         |
|  5 | SSD      | 2025-02-10 | After market close | Basic Materials    | $7.0B        | $165.42 | 19.72%       | 35.37%       | 1.79x         |
|  6 | COTY     | 2025-02-10 | After market close | Consumer Defensive | $5.9B        | $6.76   | 30.00%       | 52.47%       | 1.75x         |
|  7 | DD       | 2025-02-11 | Before market open | Basic Materials    | $31.9B       | $75.78  | 17.10%       | 29.58%       | 1.73x         |
|  8 | AMKR     | 2025-02-10 | After market close | Technology         | $6.0B        | $24.33  | 33.06%       | 55.96%       | 1.69x         |
|  9 | WCC      | 2025-02-11 | Before market open | Industrials        | $9.1B        | $185.91 | 36.95%       | 60.03%       | 1.62x         |
| 10 | FIS      | 2025-02-11 | Before market open | Technology         | $44.5B       | $83.42  | 16.92%       | 27.35%       | 1.62x         |
| 11 | HUM      | 2025-02-11 | Before market open | Healthcare         | $32.1B       | $274.33 | 32.04%       | 51.65%       | 1.61x         |
| 12 | ECL      | 2025-02-11 | Before market open | Basic Materials    | $69.6B       | $247.40 | 16.86%       | 26.39%       | 1.57x         |
| 13 | AN       | 2025-02-11 | Before market open | Consumer Cyclical  | $7.6B        | $191.14 | 23.22%       | 35.10%       | 1.51x         |
| 14 | MAR      | 2025-02-11 | Before market open | Consumer Cyclical  | $84.6B       | $303.97 | 16.89%       | 25.19%       | 1.49x         |
| 15 | ACGL     | 2025-02-10 | After market close | Financial Services | $34.4B       | $93.50  | 21.59%       | 31.36%       | 1.45x         |
| 16 | IPGP     | 2025-02-11 | Before market open | Technology         | $2.9B        | $68.91  | 35.49%       | 50.45%       | 1.42x         |
| 17 | CARR     | 2025-02-11 | Before market open | Industrials        | $59.4B       | $64.17  | 25.28%       | 35.56%       | 1.41x         |
| 18 | UTL      | 2025-02-10 | After market close | Utilities          | $887.2M      | $54.59  | 22.96%       | 32.05%       | 1.40x         |
| 19 | VNO      | 2025-02-10 | After market close | Real Estate        | $8.8B        | $42.96  | 33.61%       | 46.17%       | 1.37x         |
| 20 | LCII     | 2025-02-11 | Before market open | Consumer Cyclical  | $2.6B        | $100.92 | 31.75%       | 43.53%       | 1.37x         |
| 21 | WTS      | 2025-02-10 | After market close | Industrials        | $7.0B        | $205.05 | 19.16%       | 26.23%       | 1.37x         |
| 22 | SPGI     | 2025-02-11 | Before market open | Financial Services | $159.9B      | $519.15 | 16.39%       | 22.10%       | 1.35x         |
| 23 | ARI      | 2025-02-10 | After market close | Real Estate        | $1.3B        | $9.11   | 20.73%       | 27.40%       | 1.32x         |
| 24 | CG       | 2025-02-11 | Before market open | Financial Services | $18.4B       | $52.49  | 30.64%       | 40.05%       | 1.31x         |
| 25 | ARWR     | 2025-02-10 | After market close | Healthcare         | $2.5B        | $20.24  | 52.12%       | 67.89%       | 1.30x         |
| 26 | MAS      | 2025-02-11 | Before market open | Industrials        | $16.7B       | $77.25  | 22.19%       | 28.79%       | 1.30x         |
| 27 | CINF     | 2025-02-10 | After market close | Financial Services | $21.2B       | $136.96 | 21.95%       | 27.64%       | 1.26x         |
| 28 | SPSC     | 2025-02-10 | After market close | Technology         | $6.7B        | $178.31 | 28.47%       | 35.55%       | 1.25x         |
| 29 | LDOS     | 2025-02-11 | Before market open | Technology         | $19.1B       | $142.27 | 34.20%       | 40.16%       | 1.17x         |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
