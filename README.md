# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-07-16 22:03:42 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector             | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | OFG      | 2025-07-17 | Before market open | Financial Services | $2.0B        | $43.29  | 21.90%       | 61.55%       | 2.81x         |
|  1 | AIR      | 2025-07-16 | After market close | Industrials        | $2.7B        | $73.39  | 19.15%       | 50.01%       | 2.61x         |
|  2 | IIIN     | 2025-07-17 | Before market open | Industrials        | $749.1M      | $38.59  | 22.88%       | 47.97%       | 2.10x         |
|  3 | SNA      | 2025-07-17 | Before market open | Industrials        | $16.4B       | $313.07 | 16.61%       | 28.29%       | 1.70x         |
|  4 | CTAS     | 2025-07-17 | Before market open | Industrials        | $86.4B       | $213.24 | 17.58%       | 29.53%       | 1.68x         |
|  5 | MCRI     | 2025-07-16 | After market close | Consumer Cyclical  | $1.6B        | $85.86  | 18.83%       | 31.24%       | 1.66x         |
|  6 | REXR     | 2025-07-16 | After market close | Real Estate        | $8.9B        | $36.20  | 20.19%       | 32.87%       | 1.63x         |
|  7 | TCBI     | 2025-07-17 | Before market open | Financial Services | $3.9B        | $84.91  | 27.05%       | 42.06%       | 1.55x         |
|  8 | PEP      | 2025-07-17 | Before market open | Consumer Defensive | $185.6B      | $133.81 | 18.13%       | 28.15%       | 1.55x         |
|  9 | GE       | 2025-07-17 | Before market open | Industrials        | $283.9B      | $264.67 | 25.33%       | 37.75%       | 1.49x         |
| 10 | ABT      | 2025-07-17 | Before market open | Healthcare         | $229.2B      | $131.49 | 16.99%       | 24.90%       | 1.47x         |
| 11 | MAN      | 2025-07-17 | Before market open | Industrials        | $2.0B        | $42.33  | 41.36%       | 58.81%       | 1.42x         |
| 12 | FITB     | 2025-07-17 | Before market open | Financial Services | $28.7B       | $42.77  | 22.36%       | 30.89%       | 1.38x         |
| 13 | WBS      | 2025-07-17 | Before market open | Financial Services | $9.8B        | $57.91  | 26.14%       | 36.05%       | 1.38x         |
| 14 | MMC      | 2025-07-17 | Before market open | Financial Services | $104.4B      | $210.90 | 17.75%       | 24.45%       | 1.38x         |
| 15 | KMI      | 2025-07-16 | After market close | Energy             | $62.0B       | $27.94  | 20.46%       | 26.77%       | 1.31x         |
| 16 | CFG      | 2025-07-17 | Before market open | Financial Services | $20.4B       | $46.69  | 23.33%       | 30.23%       | 1.30x         |
| 17 | TRV      | 2025-07-17 | Before market open | Financial Services | $57.1B       | $250.62 | 21.21%       | 26.82%       | 1.26x         |
| 18 | SNV      | 2025-07-16 | After market close | Financial Services | $7.3B        | $52.53  | 27.25%       | 33.96%       | 1.25x         |
| 19 | BANR     | 2025-07-16 | After market close | Financial Services | $2.3B        | $66.71  | 23.79%       | 29.49%       | 1.24x         |
| 20 | AA       | 2025-07-16 | After market close | Basic Materials    | $7.4B        | $28.49  | 44.39%       | 54.51%       | 1.23x         |
| 21 | SLG      | 2025-07-16 | After market close | Real Estate        | $4.9B        | $62.34  | 32.56%       | 39.46%       | 1.21x         |
| 22 | USB      | 2025-07-17 | Before market open | Financial Services | $71.2B       | $45.69  | 22.61%       | 26.69%       | 1.18x         |
| 23 | TFIN     | 2025-07-16 | After market close | Financial Services | $1.5B        | $62.15  | 45.96%       | 53.64%       | 1.17x         |
| 24 | ELV      | 2025-07-17 | Before market open | Healthcare         | $77.8B       | $336.21 | 39.88%       | 44.22%       | 1.11x         |
| 25 | UAL      | 2025-07-16 | After market close | Industrials        | $28.9B       | $86.38  | 59.84%       | 53.48%       | 0.89x         |
| 26 | BSVN     | 2025-07-17 | Before market open | Financial Services | $430.7M      | $45.55  | nan%         | nan%         | nanx          |
| 27 | FR       | 2025-07-16 | After market close | Real Estate        | $6.7B        | $49.05  | 18.72%       | nan%         | nanx          |
| 28 | GSBC     | 2025-07-16 | After market close | Financial Services | $678.7M      | $59.02  | nan%         | nan%         | nanx          |
| 29 | HOMB     | 2025-07-16 | After market close | Financial Services | $5.6B        | $28.50  | 21.66%       | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
