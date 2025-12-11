# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-12-10 21:00:04 EST

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector             | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | NDSN     | 2025-12-10 | After market close | Industrials        | $13.4B       | $233.44 | 16.31%       | 31.38%       | 1.92x         |
|  1 | OXM      | 2025-12-10 | After market close | Consumer Cyclical  | $604.1M      | $39.78  | 52.71%       | 86.11%       | 1.63x         |
|  2 | CIEN     | 2025-12-11 | Before market open | Technology         | $31.4B       | $214.35 | 55.89%       | 81.40%       | 1.46x         |
|  3 | ADBE     | 2025-12-10 | After market close | Technology         | $145.6B      | $344.32 | 31.87%       | 43.86%       | 1.38x         |
|  4 | SNPS     | 2025-12-10 | After market close | Technology         | $90.7B       | $465.85 | 37.48%       | 51.00%       | 1.36x         |
|  5 | ORCL     | 2025-12-10 | After market close | Technology         | $635.8B      | $221.53 | 46.02%       | 62.06%       | 1.35x         |
|  6 | MTN      | 2025-12-10 | After market close | Consumer Cyclical  | $5.1B        | $145.46 | 33.64%       | 41.97%       | 1.25x         |
|  7 | ASYS     | 2025-12-10 | After market close | Technology         | $133.7M      | $8.81   | nan%         | nan%         | nanx          |
|  8 | DLHC     | 2025-12-10 | After market close | Industrials        | $84.4M       | $5.95   | nan%         | nan%         | nanx          |
|  9 | DXLG     | 2025-12-11 | Before market open | Consumer Cyclical  | $58.2M       | $1.10   | nan%         | nan%         | nanx          |
| 10 | ELVA     | 2025-12-10 | After market close | Industrials        | $244.9M      | $5.38   | nan%         | nan%         | nanx          |
| 11 | KEQU     | 2025-12-10 | After market close | Consumer Cyclical  | $117.9M      | $38.78  | nan%         | nan%         | nanx          |
| 12 | LOVE     | 2025-12-11 | Before market open | Consumer Cyclical  | $200.7M      | $13.95  | nan%         | nan%         | nanx          |
| 13 | PL       | 2025-12-10 | After market close | Industrials        | $4.0B        | $12.84  | nan%         | nan%         | nanx          |
| 14 | SKIL     | 2025-12-10 | After market close | Consumer Defensive | $67.2M       | $7.54   | nan%         | nan%         | nanx          |
| 15 | VRA      | 2025-12-11 | Before market open | Consumer Cyclical  | $60.1M       | $2.20   | nan%         | nan%         | nanx          |
| 16 | XZO      | 2025-12-10 | After market close | Financial Services | $1.6B        | $17.45  | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
