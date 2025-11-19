# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-11-18 20:52:05 EST

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector             | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | LZB      | 2025-11-18 | After market close | Consumer Cyclical  | $1.2B        | $29.34  | 25.78%       | 69.99%       | 2.71x         |
|  1 | LOW      | 2025-11-19 | Before market open | Consumer Cyclical  | $123.1B      | $225.00 | 17.23%       | 32.07%       | 1.86x         |
|  2 | TGT      | 2025-11-19 | Before market open | Consumer Defensive | $40.2B       | $88.48  | 29.57%       | 52.16%       | 1.76x         |
|  3 | DY       | 2025-11-19 | Before market open | Industrials        | $8.6B        | $293.77 | 32.60%       | 54.79%       | 1.68x         |
|  4 | TJX      | 2025-11-19 | Before market open | Consumer Cyclical  | $162.4B      | $145.18 | 16.02%       | 26.48%       | 1.65x         |
|  5 | WSM      | 2025-11-19 | Before market open | Consumer Cyclical  | $22.0B       | $181.32 | 34.56%       | 55.49%       | 1.61x         |
|  6 | DLB      | 2025-11-18 | After market close | Industrials        | $6.2B        | $64.55  | 23.36%       | 35.87%       | 1.54x         |
|  7 | GFF      | 2025-11-19 | Before market open | Industrials        | $3.1B        | $66.79  | 24.60%       | 35.61%       | 1.45x         |
|  8 | POWL     | 2025-11-18 | After market close | Industrials        | $3.9B        | $317.81 | 61.68%       | 85.14%       | 1.38x         |
|  9 | VVV      | 2025-11-19 | Before market open | Consumer Cyclical  | $4.0B        | $31.32  | 28.89%       | 32.82%       | 1.14x         |
| 10 | BLSH     | 2025-11-19 | Before market open | Technology         | $5.5B        | $36.75  | nan%         | nan%         | nanx          |
| 11 | CCIF     | 2025-11-18 | After market close | Financial Services | $101.1M      | $4.90   | nan%         | nan%         | nanx          |
| 12 | FLX      | 2025-11-19 | Before market open | Industrials        | $207.7M      | $3.13   | nan%         | nan%         | nanx          |
| 13 | GBDC     | 2025-11-18 | After market close | Financial Services | $3.6B        | $13.61  | nan%         | nan%         | nanx          |
| 14 | GDS      | 2025-11-19 | Before market open | Technology         | $5.6B        | $29.35  | nan%         | nan%         | nanx          |
| 15 | GLBE     | 2025-11-19 | Before market open | Consumer Cyclical  | $6.3B        | $35.13  | nan%         | nan%         | nanx          |
| 16 | HSDT     | 2025-11-18 | After market close | Financial Services | $161.2M      | $4.30   | nan%         | nan%         | nanx          |
| 17 | ICCM     | 2025-11-19 | Before market open | Healthcare         | $49.8M       | $0.71   | nan%         | nan%         | nanx          |
| 18 | KC       | 2025-11-19 | Before market open | Technology         | $3.7B        | $12.20  | nan%         | nan%         | nanx          |
| 19 | KULR     | 2025-11-18 | After market close | Technology         | $114.9M      | $2.54   | nan%         | nan%         | nanx          |
| 20 | LUXE     | 2025-11-19 | Before market open | Consumer Cyclical  | $1.3B        | $9.08   | nan%         | nan%         | nanx          |
| 21 | NYAX     | 2025-11-19 | Before market open | Technology         | $1.5B        | $40.75  | nan%         | nan%         | nanx          |
| 22 | QFIN     | 2025-11-18 | After market close | Financial Services | $3.1B        | $22.21  | nan%         | nan%         | nanx          |
| 23 | SBLK     | 2025-11-18 | After market close | Industrials        | $2.3B        | $19.15  | nan%         | nan%         | nanx          |
| 24 | SQM      | 2025-11-18 | After market close | Basic Materials    | $17.0B       | $59.47  | nan%         | nan%         | nanx          |
| 25 | VIK      | 2025-11-19 | Before market open | Consumer Cyclical  | $25.8B       | $57.26  | nan%         | nan%         | nanx          |
| 26 | VREX     | 2025-11-18 | After market close | Healthcare         | $492.4M      | $11.43  | nan%         | nan%         | nanx          |
| 27 | WIX      | 2025-11-19 | Before market open | Technology         | $7.1B        | $124.22 | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
