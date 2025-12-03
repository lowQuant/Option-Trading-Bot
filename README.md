# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-12-02 20:55:28 EST

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector             | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | CXM      | 2025-12-03 | Before market open | Technology         | $1.8B        | $7.27   | 22.23%       | 51.95%       | 2.34x         |
|  1 | AEO      | 2025-12-02 | After market close | Consumer Cyclical  | $3.6B        | $21.25  | 36.61%       | 78.87%       | 2.15x         |
|  2 | OKTA     | 2025-12-02 | After market close | Technology         | $14.4B       | $80.64  | 27.34%       | 58.43%       | 2.14x         |
|  3 | BOX      | 2025-12-02 | After market close | Technology         | $4.4B        | $29.36  | 26.09%       | 47.67%       | 1.83x         |
|  4 | THO      | 2025-12-03 | Before market open | Consumer Cyclical  | $5.8B        | $107.62 | 32.83%       | 51.37%       | 1.56x         |
|  5 | M        | 2025-12-03 | Before market open | Consumer Cyclical  | $6.1B        | $22.82  | 43.11%       | 65.36%       | 1.52x         |
|  6 | PSTG     | 2025-12-02 | After market close | Technology         | $31.1B       | $88.55  | 46.34%       | 68.22%       | 1.47x         |
|  7 | DLTR     | 2025-12-03 | Before market open | Consumer Defensive | $22.7B       | $109.89 | 34.60%       | 48.69%       | 1.41x         |
|  8 | CRWD     | 2025-12-02 | After market close | Technology         | $129.6B      | $504.13 | 34.83%       | 47.65%       | 1.37x         |
|  9 | ASAN     | 2025-12-02 | After market close | Technology         | $3.2B        | $12.77  | nan%         | nan%         | nanx          |
| 10 | GTLB     | 2025-12-02 | After market close | Technology         | $7.2B        | $41.15  | nan%         | nan%         | nanx          |
| 11 | LESL     | 2025-12-02 | After market close | Consumer Cyclical  | $33.3M       | $2.95   | nan%         | nan%         | nanx          |
| 12 | MRVL     | 2025-12-02 | After market close | Technology         | $80.1B       | $91.10  | nan%         | nan%         | nanx          |
| 13 | RY       | 2025-12-03 | Before market open | Financial Services | $217.8B      | $152.89 | nan%         | nan%         | nanx          |
| 14 | WDH      | 2025-12-03 | Before market open | Financial Services | $689.9M      | $1.85   | nan%         | nan%         | nanx          |
| 15 | YB       | 2025-12-03 | Before market open | Technology         | $951.6M      | $20.61  | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
