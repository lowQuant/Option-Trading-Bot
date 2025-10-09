# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-10-08 21:44:03 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector             | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | DAL      | 2025-10-09 | Before market open | Industrials        | $37.3B       | $56.63  | 21.34%       | 51.63%       | 2.42x         |
|  1 | HELE     | 2025-10-09 | Before market open | Consumer Defensive | $633.8M      | $27.01  | 41.90%       | 95.22%       | 2.27x         |
|  2 | NEOG     | 2025-10-09 | Before market open | Healthcare         | $1.3B        | $5.59   | 44.31%       | 79.89%       | 1.80x         |
|  3 | AZZ      | 2025-10-08 | After market close | Industrials        | $3.2B        | $105.08 | 24.27%       | 40.90%       | 1.69x         |
|  4 | PEP      | 2025-10-09 | Before market open | Consumer Defensive | $190.1B      | $140.79 | 17.39%       | 27.22%       | 1.57x         |
|  5 | BSET     | 2025-10-08 | After market close | Consumer Cyclical  | $146.1M      | $15.90  | nan%         | nan%         | nanx          |
|  6 | BYRN     | 2025-10-09 | Before market open | Industrials        | $517.6M      | $22.61  | nan%         | nan%         | nanx          |
|  7 | RELL     | 2025-10-08 | After market close | Technology         | $153.7M      | $9.84   | nan%         | nan%         | nanx          |
|  8 | RGP      | 2025-10-08 | After market close | Industrials        | $165.2M      | $4.85   | nan%         | nan%         | nanx          |
|  9 | TLRY     | 2025-10-09 | Before market open | Healthcare         | $1.9B        | $1.71   | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
