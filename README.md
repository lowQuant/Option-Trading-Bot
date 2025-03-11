# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-03-10 21:42:38 EDT

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | KSS      | 2025-03-11 | Before market open | Consumer Cyclical      | $1.4B        | $12.21  | 39.22%       | 93.05%       | 2.37x         |
|  1 | NX       | 2025-03-10 | After market close | Industrials            | $964.0M      | $20.22  | 46.07%       | 89.59%       | 1.94x         |
|  2 | DKS      | 2025-03-11 | Before market open | Consumer Cyclical      | $17.5B       | $214.26 | 31.05%       | 55.90%       | 1.80x         |
|  3 | KFY      | 2025-03-11 | Before market open | Industrials            | $3.4B        | $65.78  | 19.59%       | 33.57%       | 1.71x         |
|  4 | MTN      | 2025-03-10 | After market close | Consumer Cyclical      | $5.9B        | $157.51 | 26.24%       | 43.32%       | 1.65x         |
|  5 | UNFI     | 2025-03-11 | Before market open | Consumer Defensive     | $1.6B        | $26.91  | 49.42%       | 80.06%       | 1.62x         |
|  6 | ORCL     | 2025-03-10 | After market close | Technology             | $434.0B      | $155.16 | 60.53%       | 54.89%       | 0.91x         |
|  7 | CIEN     | 2025-03-11 | Before market open | Technology             | $9.8B        | $68.93  | 85.31%       | 73.46%       | 0.86x         |
|  8 | ACHV     | 2025-03-11 | Before market open | Healthcare             | $107.8M      | $3.14   | nan%         | nan%         | nanx          |
|  9 | AGEN     | 2025-03-11 | Before market open | Healthcare             | $55.5M       | $2.35   | nan%         | nan%         | nanx          |
| 10 | ASAN     | 2025-03-10 | After market close | Technology             | $4.2B        | $18.25  | nan%         | nan%         | nanx          |
| 11 | AUNA     | 2025-03-10 | After market close | Healthcare             | $606.1M      | $8.20   | nan%         | nan%         | nanx          |
| 12 | AVO      | 2025-03-10 | After market close | Consumer Defensive     | $849.3M      | $11.96  | nan%         | nan%         | nanx          |
| 13 | BEEP     | 2025-03-10 | After market close | Industrials            | $152.1M      | $3.58   | nan%         | nan%         | nanx          |
| 14 | BVS      | 2025-03-11 | Before market open | Healthcare             | $601.4M      | $9.20   | nan%         | nan%         | nanx          |
| 15 | BWAY     | 2025-03-11 | Before market open | Healthcare             | $176.7M      | $9.41   | nan%         | nan%         | nanx          |
| 16 | BZ       | 2025-03-11 | Before market open | Communication Services | $7.4B        | $17.86  | nan%         | nan%         | nanx          |
| 17 | CHRS     | 2025-03-10 | After market close | Healthcare             | $120.5M      | $1.04   | nan%         | nan%         | nanx          |
| 18 | CMT      | 2025-03-11 | Before market open | Basic Materials        | $123.2M      | $13.76  | nan%         | nan%         | nanx          |
| 19 | CVGI     | 2025-03-10 | After market close | Consumer Cyclical      | $69.3M       | $2.03   | nan%         | nan%         | nanx          |
| 20 | DOUG     | 2025-03-10 | After market close | Real Estate            | $152.5M      | $1.71   | nan%         | nan%         | nanx          |
| 21 | ECX      | 2025-03-11 | Before market open | Consumer Cyclical      | $959.0M      | $2.80   | nan%         | nan%         | nanx          |
| 22 | ELTK     | 2025-03-11 | Before market open | Technology             | $75.7M       | $11.20  | nan%         | nan%         | nanx          |
| 23 | EWCZ     | 2025-03-11 | Before market open | Consumer Defensive     | $315.5M      | $5.55   | nan%         | nan%         | nanx          |
| 24 | EXK      | 2025-03-11 | Before market open | Basic Materials        | $1.0B        | $3.98   | nan%         | nan%         | nanx          |
| 25 | FCEL     | 2025-03-11 | Before market open | Industrials            | $138.7M      | $6.59   | nan%         | nan%         | nanx          |
| 26 | FERG     | 2025-03-11 | Before market open | Industrials            | $33.6B       | $168.19 | nan%         | nan%         | nanx          |
| 27 | FTK      | 2025-03-10 | After market close | Energy                 | $222.9M      | $7.48   | nan%         | nan%         | nanx          |
| 28 | FWRG     | 2025-03-11 | Before market open | Consumer Cyclical      | $1.2B        | $19.00  | nan%         | nan%         | nanx          |
| 29 | GAIA     | 2025-03-10 | After market close | Communication Services | $100.8M      | $4.10   | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
