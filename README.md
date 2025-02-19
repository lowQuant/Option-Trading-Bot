# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-02-18 20:38:12 EST

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | GRMN     | 2025-02-19 | Before market open | Technology             | $41.2B       | $212.62 | 15.41%       | 44.45%       | 2.88x         |
|  1 | MBC      | 2025-02-18 | After market close | Consumer Cyclical      | $2.1B        | $16.88  | 26.87%       | 66.65%       | 2.48x         |
|  2 | CLH      | 2025-02-19 | Before market open | Industrials            | $12.2B       | $229.78 | 16.02%       | 36.97%       | 2.31x         |
|  3 | IFF      | 2025-02-18 | After market close | Basic Materials        | $22.1B       | $85.58  | 17.07%       | 35.02%       | 2.05x         |
|  4 | CNK      | 2025-02-19 | Before market open | Communication Services | $4.0B        | $32.56  | 20.06%       | 40.45%       | 2.02x         |
|  5 | ROCK     | 2025-02-19 | Before market open | Industrials            | $1.8B        | $58.85  | 30.59%       | 57.65%       | 1.88x         |
|  6 | TRMB     | 2025-02-19 | Before market open | Technology             | $18.5B       | $74.29  | 19.52%       | 36.77%       | 1.88x         |
|  7 | RBA      | 2025-02-18 | After market close | Industrials            | $17.8B       | $96.30  | 18.07%       | 33.86%       | 1.87x         |
|  8 | ETSY     | 2025-02-19 | Before market open | Consumer Cyclical      | $6.4B        | $57.20  | 35.69%       | 62.74%       | 1.76x         |
|  9 | KRYS     | 2025-02-19 | Before market open | Healthcare             | $4.5B        | $153.24 | 33.26%       | 57.99%       | 1.74x         |
| 10 | GNW      | 2025-02-18 | After market close | Financial Services     | $3.1B        | $7.29   | 21.29%       | 36.90%       | 1.73x         |
| 11 | PEN      | 2025-02-18 | After market close | Healthcare             | $10.4B       | $268.67 | 30.25%       | 51.60%       | 1.71x         |
| 12 | PRG      | 2025-02-19 | Before market open | Industrials            | $1.8B        | $42.82  | 26.91%       | 45.12%       | 1.68x         |
| 13 | CSGP     | 2025-02-18 | After market close | Real Estate            | $30.9B       | $74.06  | 24.92%       | 41.75%       | 1.68x         |
| 14 | CE       | 2025-02-18 | After market close | Basic Materials        | $7.6B        | $68.06  | 34.67%       | 57.99%       | 1.67x         |
| 15 | NPO      | 2025-02-19 | Before market open | Industrials            | $4.1B        | $192.96 | 22.24%       | 36.20%       | 1.63x         |
| 16 | WING     | 2025-02-19 | Before market open | Consumer Cyclical      | $8.9B        | $304.69 | 31.91%       | 51.71%       | 1.62x         |
| 17 | THRM     | 2025-02-19 | Before market open | Consumer Cyclical      | $1.1B        | $35.44  | 27.55%       | 44.59%       | 1.62x         |
| 18 | ADEA     | 2025-02-18 | After market close | Technology             | $1.5B        | $13.28  | 28.50%       | 46.09%       | 1.62x         |
| 19 | FOUR     | 2025-02-18 | After market close | Technology             | $11.3B       | $121.28 | 36.65%       | 57.55%       | 1.57x         |
| 20 | WWW      | 2025-02-19 | Before market open | Consumer Cyclical      | $1.5B        | $18.53  | 44.91%       | 68.73%       | 1.53x         |
| 21 | HALO     | 2025-02-18 | After market close | Healthcare             | $7.4B        | $58.29  | 25.76%       | 38.47%       | 1.49x         |
| 22 | LPX      | 2025-02-19 | Before market open | Industrials            | $7.9B        | $112.36 | 30.60%       | 44.86%       | 1.47x         |
| 23 | HR       | 2025-02-19 | Before market open | Real Estate            | $6.1B        | $16.49  | 22.37%       | 32.36%       | 1.45x         |
| 24 | CRL      | 2025-02-19 | Before market open | Healthcare             | $7.9B        | $151.99 | 33.45%       | 47.59%       | 1.42x         |
| 25 | RUSHA    | 2025-02-18 | After market close | Consumer Cyclical      | $4.8B        | $60.47  | 25.27%       | 34.45%       | 1.36x         |
| 26 | PSN      | 2025-02-19 | Before market open | Technology             | $7.8B        | $73.46  | 38.93%       | 52.85%       | 1.36x         |
| 27 | TNL      | 2025-02-19 | Before market open | Consumer Cyclical      | $3.9B        | $56.42  | 24.18%       | 32.57%       | 1.35x         |
| 28 | ANDE     | 2025-02-18 | After market close | Consumer Defensive     | $1.4B        | $40.55  | 30.01%       | 40.25%       | 1.34x         |
| 29 | LZB      | 2025-02-18 | After market close | Consumer Cyclical      | $1.9B        | $45.46  | 30.26%       | 39.48%       | 1.30x         |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
