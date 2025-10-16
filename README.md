# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-10-15 21:46:46 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector             | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | BK       | 2025-10-16 | Before market open | Financial Services | $76.8B       | $107.11 | 15.94%       | 33.38%       | 2.09x         |
|  1 | SNV      | 2025-10-15 | After market close | Financial Services | $6.5B        | $47.84  | 26.23%       | 47.05%       | 1.79x         |
|  2 | IIIN     | 2025-10-16 | Before market open | Industrials        | $728.6M      | $37.12  | 24.64%       | 42.97%       | 1.74x         |
|  3 | MAN      | 2025-10-16 | Before market open | Industrials        | $1.8B        | $37.97  | 36.02%       | 62.43%       | 1.73x         |
|  4 | UAL      | 2025-10-15 | After market close | Industrials        | $33.7B       | $103.15 | 33.02%       | 56.03%       | 1.70x         |
|  5 | MMC      | 2025-10-16 | Before market open | Financial Services | $100.2B      | $207.02 | 14.74%       | 25.00%       | 1.70x         |
|  6 | CMC      | 2025-10-16 | Before market open | Basic Materials    | $6.8B        | $60.43  | 28.43%       | 46.20%       | 1.63x         |
|  7 | PNFP     | 2025-10-15 | After market close | Financial Services | $7.0B        | $91.88  | 26.82%       | 42.72%       | 1.59x         |
|  8 | EPAC     | 2025-10-15 | After market close | Industrials        | $2.2B        | $40.31  | 25.58%       | 39.73%       | 1.55x         |
|  9 | MTB      | 2025-10-16 | Before market open | Financial Services | $28.9B       | $187.04 | 20.05%       | 31.05%       | 1.55x         |
| 10 | SNA      | 2025-10-16 | Before market open | Industrials        | $17.3B       | $337.02 | 20.44%       | 30.41%       | 1.49x         |
| 11 | TFIN     | 2025-10-15 | After market close | Financial Services | $1.1B        | $48.34  | 39.14%       | 58.02%       | 1.48x         |
| 12 | CBSH     | 2025-10-16 | Before market open | Financial Services | $7.5B        | $58.88  | 18.36%       | 26.57%       | 1.45x         |
| 13 | KEY      | 2025-10-16 | Before market open | Financial Services | $19.4B       | $18.01  | 23.67%       | 34.03%       | 1.44x         |
| 14 | USB      | 2025-10-16 | Before market open | Financial Services | $72.3B       | $47.09  | 20.64%       | 29.26%       | 1.42x         |
| 15 | JBHT     | 2025-10-15 | After market close | Industrials        | $13.4B       | $139.37 | 31.09%       | 43.51%       | 1.40x         |
| 16 | TRV      | 2025-10-16 | Before market open | Financial Services | $60.7B       | $275.64 | 19.16%       | 26.68%       | 1.39x         |
| 17 | SCHW     | 2025-10-16 | Before market open | Financial Services | $171.2B      | $93.39  | 27.85%       | 37.37%       | 1.34x         |
| 18 | REXR     | 2025-10-15 | After market close | Real Estate        | $10.0B       | $40.94  | 23.29%       | 31.12%       | 1.34x         |
| 19 | SLG      | 2025-10-15 | After market close | Real Estate        | $4.3B        | $56.03  | 37.24%       | 41.86%       | 1.12x         |
| 20 | BANR     | 2025-10-15 | After market close | Financial Services | $2.2B        | $64.03  | 24.46%       | 27.44%       | 1.12x         |
| 21 | FR       | 2025-10-15 | After market close | Real Estate        | $7.3B        | $51.93  | 17.33%       | nan%         | nanx          |
| 22 | GSBC     | 2025-10-15 | After market close | Financial Services | $705.3M      | $62.40  | nan%         | nan%         | nanx          |
| 23 | HOMB     | 2025-10-15 | After market close | Financial Services | $5.4B        | $28.34  | 24.09%       | nan%         | nanx          |
| 24 | INFY     | 2025-10-16 | Before market open | Technology         | $69.5B       | $16.48  | nan%         | nan%         | nanx          |
| 25 | MMLP     | 2025-10-15 | After market close | Energy             | $120.7M      | $3.16   | nan%         | nan%         | nanx          |
| 26 | TSM      | 2025-10-16 | Before market open | Technology         | $1.6tr       | $295.94 | nan%         | nan%         | nanx          |
| 27 | WIT      | 2025-10-16 | Before market open | Technology         | $29.4B       | $2.73   | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
