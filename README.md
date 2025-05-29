# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-05-28 21:53:53 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector             | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | PSTG     | 2025-05-28 | After market close | Technology         | $18.2B       | $55.59  | 40.80%       | 67.23%       | 1.65x         |
|  1 | HPQ      | 2025-05-28 | After market close | Technology         | $26.7B       | $28.34  | 26.94%       | 43.00%       | 1.60x         |
|  2 | ELF      | 2025-05-28 | After market close | Consumer Defensive | $5.2B        | $91.72  | 56.70%       | 84.97%       | 1.50x         |
|  3 | HRL      | 2025-05-29 | Before market open | Consumer Defensive | $16.6B       | $30.20  | 20.15%       | 29.32%       | 1.46x         |
|  4 | SPTN     | 2025-05-29 | Before market open | Consumer Defensive | $661.5M      | $19.54  | 28.73%       | 41.45%       | 1.44x         |
|  5 | SNPS     | 2025-05-28 | After market close | Technology         | $79.1B       | $511.79 | 29.31%       | 42.20%       | 1.44x         |
|  6 | AMWD     | 2025-05-29 | Before market open | Consumer Cyclical  | $857.0M      | $57.77  | 35.54%       | 49.85%       | 1.40x         |
|  7 | BBY      | 2025-05-29 | Before market open | Consumer Cyclical  | $15.3B       | $72.22  | 33.04%       | 45.75%       | 1.38x         |
|  8 | ROIV     | 2025-05-29 | Before market open | Healthcare         | $7.7B        | $10.76  | 31.42%       | 41.92%       | 1.33x         |
|  9 | CRM      | 2025-05-28 | After market close | Technology         | $266.0B      | $277.19 | 33.58%       | 43.23%       | 1.29x         |
| 10 | CAL      | 2025-05-29 | Before market open | Consumer Cyclical  | $564.9M      | $16.57  | 66.79%       | 82.36%       | 1.23x         |
| 11 | KSS      | 2025-05-29 | Before market open | Consumer Cyclical  | $901.7M      | $7.91   | 81.99%       | 97.34%       | 1.19x         |
| 12 | HLNE     | 2025-05-29 | Before market open | Financial Services | $9.8B        | $172.60 | 42.76%       | 47.43%       | 1.11x         |
| 13 | BURL     | 2025-05-29 | Before market open | Consumer Cyclical  | $15.2B       | $240.71 | 49.34%       | 54.33%       | 1.10x         |
| 14 | NDSN     | 2025-05-28 | After market close | Industrials        | $11.3B       | $198.01 | 27.30%       | 29.88%       | 1.09x         |
| 15 | A        | 2025-05-28 | After market close | Healthcare         | $31.7B       | $111.26 | 36.00%       | 38.62%       | 1.07x         |
| 16 | NVDA     | 2025-05-28 | After market close | Technology         | $3.3tr       | $135.50 | 45.33%       | 48.40%       | 1.07x         |
| 17 | BBWI     | 2025-05-29 | Before market open | Consumer Cyclical  | $6.5B        | $30.54  | 51.73%       | 50.58%       | 0.98x         |
| 18 | FL       | 2025-05-29 | Before market open | Consumer Cyclical  | $2.3B        | $23.90  | 188.61%      | 20.54%       | 0.11x         |
| 19 | AI       | 2025-05-28 | After market close | Technology         | $3.2B        | $23.92  | nan%         | nan%         | nanx          |
| 20 | ALAR     | 2025-05-29 | Before market open | Technology         | $59.2M       | $8.24   | nan%         | nan%         | nanx          |
| 21 | BBW      | 2025-05-29 | Before market open | Consumer Cyclical  | $565.0M      | $42.62  | nan%         | nan%         | nanx          |
| 22 | BOSC     | 2025-05-29 | Before market open | Technology         | $23.3M       | $3.93   | nan%         | nan%         | nanx          |
| 23 | CM       | 2025-05-29 | Before market open | Financial Services | $64.7B       | $68.41  | nan%         | nan%         | nanx          |
| 24 | DOOO     | 2025-05-29 | Before market open | Consumer Cyclical  | $2.7B        | $36.60  | nan%         | nan%         | nanx          |
| 25 | DSX      | 2025-05-29 | Before market open | Industrials        | $170.2M      | $1.47   | nan%         | nan%         | nanx          |
| 26 | DXLG     | 2025-05-29 | Before market open | Consumer Cyclical  | $63.2M       | $1.15   | nan%         | nan%         | nanx          |
| 27 | FUTU     | 2025-05-29 | Before market open | Financial Services | $14.9B       | $106.88 | nan%         | nan%         | nanx          |
| 28 | JG       | 2025-05-29 | Before market open | Technology         | $67.2M       | $11.30  | nan%         | nan%         | nanx          |
| 29 | LI       | 2025-05-29 | Before market open | Consumer Cyclical  | $28.9B       | $28.24  | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
