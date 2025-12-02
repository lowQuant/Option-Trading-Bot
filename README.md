# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-12-01 20:55:43 EST

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector             | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | UNFI     | 2025-12-02 | Before market open | Consumer Defensive | $2.1B        | $37.31  | 38.41%       | 68.62%       | 1.79x         |
|  1 | SIG      | 2025-12-02 | Before market open | Consumer Cyclical  | $3.9B        | $100.16 | 37.54%       | 66.06%       | 1.76x         |
|  2 | VSTS     | 2025-12-01 | After market close | Industrials        | $886.0M      | $6.48   | 44.62%       | 66.50%       | 1.49x         |
|  3 | BNS      | 2025-12-02 | Before market open | Financial Services | $85.6B       | $69.29  | nan%         | nan%         | nanx          |
|  4 | BWLP     | 2025-12-02 | Before market open | Industrials        | $1.9B        | $12.69  | nan%         | nan%         | nanx          |
|  5 | CANG     | 2025-12-01 | After market close | Financial Services | $514.1M      | $1.50   | nan%         | nan%         | nanx          |
|  6 | CRDO     | 2025-12-01 | After market close | Technology         | $29.6B       | $177.60 | nan%         | nan%         | nanx          |
|  7 | CTRN     | 2025-12-02 | Before market open | Consumer Cyclical  | $366.0M      | $45.29  | nan%         | nan%         | nanx          |
|  8 | HERE     | 2025-12-02 | Before market open | Consumer Cyclical  | $258.9M      | $5.04   | nan%         | nan%         | nanx          |
|  9 | MDB      | 2025-12-01 | After market close | Technology         | $26.9B       | $332.37 | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
