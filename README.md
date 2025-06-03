# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-06-02 21:55:40 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector             | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | SIG      | 2025-06-03 | Before market open | Consumer Cyclical  | $2.8B        | $66.51  | 49.06%       | 73.66%       | 1.50x         |
|  1 | DG       | 2025-06-03 | Before market open | Consumer Defensive | $21.4B       | $97.22  | 36.59%       | 47.74%       | 1.30x         |
|  2 | OLLI     | 2025-06-03 | Before market open | Consumer Defensive | $6.9B        | $111.45 | 42.23%       | 52.49%       | 1.24x         |
|  3 | DCI      | 2025-06-03 | Before market open | Industrials        | $8.3B        | $69.51  | 23.67%       | 24.56%       | 1.04x         |
|  4 | CRDO     | 2025-06-02 | After market close | Technology         | $10.6B       | $60.96  | nan%         | nan%         | nanx          |
|  5 | CTRN     | 2025-06-03 | Before market open | Consumer Cyclical  | $223.6M      | $26.48  | nan%         | nan%         | nanx          |
|  6 | FERG     | 2025-06-03 | Before market open | Industrials        | $36.2B       | $182.23 | nan%         | nan%         | nanx          |
|  7 | NESR     | 2025-06-03 | Before market open | Energy             | $609.6M      | $6.18   | nan%         | nan%         | nanx          |
|  8 | NIO      | 2025-06-03 | Before market open | Consumer Cyclical  | $7.9B        | $3.54   | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
