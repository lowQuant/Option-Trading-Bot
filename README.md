# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-04-16 21:47:13 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector             | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | IIIN     | 2025-04-17 | Before market open | Industrials        | $521.9M      | $27.16  | 42.56%       | 58.02%       | 1.36x         |
|  1 | DHI      | 2025-04-17 | Before market open | Consumer Cyclical  | $37.7B       | $119.81 | 40.94%       | 46.75%       | 1.14x         |
|  2 | HOMB     | 2025-04-16 | After market close | Financial Services | $5.2B        | $26.10  | 41.70%       | 47.29%       | 1.13x         |
|  3 | CSX      | 2025-04-16 | After market close | Industrials        | $51.5B       | $27.90  | 36.46%       | 39.55%       | 1.08x         |
|  4 | TCBI     | 2025-04-17 | Before market open | Financial Services | $3.0B        | $64.21  | 52.04%       | 54.79%       | 1.05x         |
|  5 | UNH      | 2025-04-17 | Before market open | Healthcare         | $535.1B      | $583.59 | 29.11%       | 30.56%       | 1.05x         |
|  6 | SNA      | 2025-04-17 | Before market open | Industrials        | $17.4B       | $337.07 | 35.58%       | 35.01%       | 0.98x         |
|  7 | OZK      | 2025-04-16 | After market close | Financial Services | $4.5B        | $39.24  | 50.75%       | 49.83%       | 0.98x         |
|  8 | TFIN     | 2025-04-16 | After market close | Financial Services | $1.2B        | $51.20  | 61.33%       | 58.83%       | 0.96x         |
|  9 | MMC      | 2025-04-17 | Before market open | Financial Services | $114.5B      | $232.36 | 27.16%       | 25.76%       | 0.95x         |
| 10 | LBRT     | 2025-04-16 | After market close | Energy             | $1.9B        | $11.39  | 100.16%      | 94.81%       | 0.95x         |
| 11 | BMI      | 2025-04-17 | Before market open | Technology         | $5.4B        | $185.81 | 43.44%       | 39.37%       | 0.91x         |
| 12 | AA       | 2025-04-16 | After market close | Basic Materials    | $6.5B        | $24.68  | 81.27%       | 73.32%       | 0.90x         |
| 13 | KMI      | 2025-04-16 | After market close | Energy             | $59.9B       | $26.80  | 37.69%       | 33.82%       | 0.90x         |
| 14 | SLG      | 2025-04-16 | After market close | Real Estate        | $4.0B        | $51.50  | 54.80%       | 48.89%       | 0.89x         |
| 15 | REXR     | 2025-04-16 | After market close | Real Estate        | $8.0B        | $32.82  | 49.21%       | 43.85%       | 0.89x         |
| 16 | ALLY     | 2025-04-17 | Before market open | Financial Services | $9.9B        | $32.33  | 55.53%       | 48.41%       | 0.87x         |
| 17 | FR       | 2025-04-16 | After market close | Real Estate        | $6.4B        | $46.47  | 45.22%       | 38.52%       | 0.85x         |
| 18 | MAN      | 2025-04-17 | Before market open | Industrials        | $2.3B        | $50.34  | 49.23%       | 41.22%       | 0.84x         |
| 19 | BANR     | 2025-04-16 | After market close | Financial Services | $2.1B        | $58.12  | 41.51%       | 34.60%       | 0.83x         |
| 20 | STT      | 2025-04-17 | Before market open | Financial Services | $23.0B       | $80.91  | 49.64%       | 39.75%       | 0.80x         |
| 21 | RF       | 2025-04-17 | Before market open | Financial Services | $17.4B       | $19.43  | 51.75%       | 41.40%       | 0.80x         |
| 22 | CNS      | 2025-04-16 | After market close | Financial Services | $3.8B        | $74.44  | 47.92%       | 37.64%       | 0.79x         |
| 23 | KEY      | 2025-04-17 | Before market open | Financial Services | $15.4B       | $14.25  | 57.18%       | 43.08%       | 0.75x         |
| 24 | HBAN     | 2025-04-17 | Before market open | Financial Services | $19.4B       | $13.40  | 57.06%       | 42.56%       | 0.75x         |
| 25 | FITB     | 2025-04-17 | Before market open | Financial Services | $22.9B       | $35.07  | 49.88%       | 37.04%       | 0.74x         |
| 26 | FNB      | 2025-04-16 | After market close | Financial Services | $4.4B        | $12.31  | 54.60%       | 39.51%       | 0.72x         |
| 27 | BX       | 2025-04-17 | Before market open | Financial Services | $157.7B      | $133.54 | 69.07%       | 49.46%       | 0.72x         |
| 28 | SNV      | 2025-04-16 | After market close | Financial Services | $5.7B        | $40.05  | 70.19%       | 49.60%       | 0.71x         |
| 29 | TFC      | 2025-04-17 | Before market open | Financial Services | $47.0B       | $36.18  | 53.81%       | 37.21%       | 0.69x         |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
