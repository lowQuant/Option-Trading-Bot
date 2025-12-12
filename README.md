# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-12-11 20:59:05 EST

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector             | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | NX       | 2025-12-11 | After market close | Industrials        | $691.8M      | $14.50  | 46.06%       | 123.48%      | 2.68x         |
|  1 | LULU     | 2025-12-11 | After market close | Consumer Cyclical  | $22.4B       | $187.62 | 38.67%       | 64.59%       | 1.67x         |
|  2 | COST     | 2025-12-11 | After market close | Consumer Defensive | $392.7B      | $874.41 | 17.62%       | 25.75%       | 1.46x         |
|  3 | AVGO     | 2025-12-11 | After market close | Technology         | $1.9tr       | $412.97 | 47.27%       | 49.53%       | 1.05x         |
|  4 | JOUT     | 2025-12-12 | Before market open | Consumer Cyclical  | $446.3M      | $42.76  | nan%         | nan%         | nanx          |
|  5 | KMTS     | 2025-12-11 | After market close | Healthcare         | $1.5B        | $24.52  | nan%         | nan%         | nanx          |
|  6 | MITK     | 2025-12-11 | After market close | Technology         | $421.8M      | $9.23   | nan%         | nan%         | nanx          |
|  7 | NTSK     | 2025-12-11 | After market close | Technology         | $9.0B        | $22.50  | nan%         | nan%         | nanx          |
|  8 | RENT     | 2025-12-12 | Before market open | Consumer Cyclical  | $188.9M      | $6.33   | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
