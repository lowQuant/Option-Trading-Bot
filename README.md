# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-02-11 20:37:14 EST

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | HCSG     | 2025-02-12 | Before market open | Healthcare             | $799.2M      | $10.70  | 21.32%       | 75.35%       | 3.53x         |
|  1 | UFCS     | 2025-02-11 | After market close | Financial Services     | $635.1M      | $24.78  | 27.69%       | 88.96%       | 3.21x         |
|  2 | TDC      | 2025-02-11 | After market close | Technology             | $3.0B        | $30.93  | 23.03%       | 59.71%       | 2.59x         |
|  3 | SW       | 2025-02-12 | Before market open | Consumer Cyclical      | $27.9B       | $53.53  | 21.96%       | 51.69%       | 2.35x         |
|  4 | ALKS     | 2025-02-12 | Before market open | Healthcare             | $5.2B        | $31.23  | 25.38%       | 55.91%       | 2.20x         |
|  5 | CHEF     | 2025-02-12 | Before market open | Consumer Defensive     | $2.2B        | $54.29  | 21.81%       | 45.88%       | 2.10x         |
|  6 | GNRC     | 2025-02-12 | Before market open | Industrials            | $8.4B        | $145.07 | 25.13%       | 48.65%       | 1.94x         |
|  7 | IAC      | 2025-02-11 | After market close | Communication Services | $3.5B        | $41.37  | 23.93%       | 45.80%       | 1.91x         |
|  8 | THC      | 2025-02-12 | Before market open | Healthcare             | $13.2B       | $139.45 | 28.87%       | 51.17%       | 1.77x         |
|  9 | ST       | 2025-02-11 | After market close | Technology             | $3.9B        | $25.81  | 26.43%       | 46.22%       | 1.75x         |
| 10 | SLVM     | 2025-02-12 | Before market open | Basic Materials        | $3.1B        | $76.48  | 29.07%       | 49.35%       | 1.70x         |
| 11 | PBI      | 2025-02-11 | After market close | Industrials            | $1.6B        | $8.82   | 51.51%       | 83.62%       | 1.62x         |
| 12 | WAT      | 2025-02-12 | Before market open | Healthcare             | $24.1B       | $407.58 | 24.29%       | 39.30%       | 1.62x         |
| 13 | SPTN     | 2025-02-12 | Before market open | Consumer Defensive     | $635.6M      | $18.51  | 22.61%       | 35.58%       | 1.57x         |
| 14 | R        | 2025-02-12 | Before market open | Industrials            | $6.7B        | $157.51 | 20.51%       | 32.14%       | 1.57x         |
| 15 | BL       | 2025-02-11 | After market close | Technology             | $4.0B        | $64.41  | 32.61%       | 51.05%       | 1.57x         |
| 16 | MCRI     | 2025-02-11 | After market close | Consumer Cyclical      | $1.6B        | $85.41  | 17.04%       | 26.49%       | 1.55x         |
| 17 | LAD      | 2025-02-12 | Before market open | Consumer Cyclical      | $9.8B        | $369.47 | 28.52%       | 44.21%       | 1.55x         |
| 18 | SMCI     | 2025-02-11 | After market close | Technology             | $22.6B       | $42.65  | 97.29%       | 148.30%      | 1.52x         |
| 19 | GILD     | 2025-02-11 | After market close | Healthcare             | $119.8B      | $95.48  | 18.94%       | 28.31%       | 1.49x         |
| 20 | EW       | 2025-02-11 | After market close | Healthcare             | $41.8B       | $71.10  | 24.58%       | 36.26%       | 1.48x         |
| 21 | BIIB     | 2025-02-12 | Before market open | Healthcare             | $20.3B       | $142.54 | 24.85%       | 36.35%       | 1.46x         |
| 22 | MLM      | 2025-02-12 | Before market open | Basic Materials        | $32.3B       | $530.97 | 18.88%       | 27.44%       | 1.45x         |
| 23 | WAB      | 2025-02-12 | Before market open | Industrials            | $35.8B       | $208.37 | 18.77%       | 27.18%       | 1.45x         |
| 24 | CVS      | 2025-02-12 | Before market open | Healthcare             | $69.2B       | $54.29  | 30.90%       | 43.81%       | 1.42x         |
| 25 | DIOD     | 2025-02-11 | After market close | Technology             | $2.4B        | $53.30  | 40.15%       | 56.44%       | 1.41x         |
| 26 | PRI      | 2025-02-11 | After market close | Financial Services     | $9.7B        | $293.16 | 16.30%       | 22.81%       | 1.40x         |
| 27 | AIZ      | 2025-02-11 | After market close | Financial Services     | $10.9B       | $212.53 | 20.69%       | 28.90%       | 1.40x         |
| 28 | WELL     | 2025-02-11 | After market close | Real Estate            | $89.3B       | $143.11 | 22.80%       | 31.45%       | 1.38x         |
| 29 | SAH      | 2025-02-12 | Before market open | Consumer Cyclical      | $2.6B        | $73.10  | 27.51%       | 37.20%       | 1.35x         |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
