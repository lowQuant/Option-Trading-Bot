# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-04-01 21:46:35 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               |   sector | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|---------:|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | ANGO     | 2025-04-02 | Before market open |      nan | N/A          | $nan    | nan%         | nan%         | nanx          |
|  1 | BB       | 2025-04-02 | Before market open |      nan | N/A          | $nan    | nan%         | nan%         | nanx          |
|  2 | CGNT     | 2025-04-02 | Before market open |      nan | N/A          | $nan    | nan%         | nan%         | nanx          |
|  3 | NCNO     | 2025-04-01 | After market close |      nan | N/A          | $nan    | nan%         | nan%         | nanx          |
|  4 | SPWH     | 2025-04-01 | After market close |      nan | N/A          | $nan    | nan%         | nan%         | nanx          |
|  5 | UNF      | 2025-04-02 | Before market open |      nan | N/A          | $nan    | 50.22%       | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
