# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-06-05 21:53:49 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector             | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | ABM      | 2025-06-06 | Before market open | Industrials        | $3.3B        | $52.32  | 17.02%       | 39.64%       | 2.33x         |
|  1 | DOCU     | 2025-06-05 | After market close | Technology         | $19.0B       | $93.84  | 35.71%       | 56.41%       | 1.58x         |
|  2 | LULU     | 2025-06-05 | After market close | Consumer Cyclical  | $40.3B       | $335.19 | 35.76%       | 54.56%       | 1.53x         |
|  3 | AVGO     | 2025-06-05 | After market close | Technology         | $1.2tr       | $261.08 | 33.01%       | 49.60%       | 1.50x         |
|  4 | NX       | 2025-06-05 | After market close | Industrials        | $810.0M      | $17.13  | 55.09%       | 61.48%       | 1.12x         |
|  5 | MTN      | 2025-06-05 | After market close | Consumer Cyclical  | $5.8B        | $154.22 | 34.91%       | 38.67%       | 1.11x         |
|  6 | AVO      | 2025-06-05 | After market close | Consumer Defensive | $751.9M      | $10.58  | nan%         | nan%         | nanx          |
|  7 | BBCP     | 2025-06-05 | After market close | Industrials        | $377.7M      | $7.10   | nan%         | nan%         | nanx          |
|  8 | BRZE     | 2025-06-05 | After market close | Technology         | $3.8B        | $36.61  | nan%         | nan%         | nanx          |
|  9 | CURV     | 2025-06-05 | After market close | Consumer Cyclical  | $534.4M      | $5.11   | nan%         | nan%         | nanx          |
| 10 | FCEL     | 2025-06-06 | Before market open | Industrials        | $128.0M      | $5.64   | nan%         | nan%         | nanx          |
| 11 | HUIZ     | 2025-06-06 | Before market open | Financial Services | $20.3M       | $2.01   | nan%         | nan%         | nanx          |
| 12 | IOT      | 2025-06-05 | After market close | Technology         | $26.6B       | $46.72  | nan%         | nan%         | nanx          |
| 13 | RBRK     | 2025-06-05 | After market close | Technology         | $19.1B       | $98.56  | nan%         | nan%         | nanx          |
| 14 | RENT     | 2025-06-05 | After market close | Consumer Cyclical  | $26.1M       | $6.50   | nan%         | nan%         | nanx          |
| 15 | TTAN     | 2025-06-05 | After market close | Technology         | $10.4B       | $114.71 | nan%         | nan%         | nanx          |
| 16 | WOOF     | 2025-06-05 | After market close | Consumer Cyclical  | $985.0M      | $3.56   | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
