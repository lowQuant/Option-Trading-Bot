# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-11-17 20:52:28 EST

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | BRBR     | 2025-11-18 | Before market open | Consumer Defensive     | $3.3B        | $26.96  | 31.22%       | 82.67%       | 2.65x         |
|  1 | ENR      | 2025-11-18 | Before market open | Industrials            | $1.7B        | $23.88  | 27.73%       | 58.08%       | 2.09x         |
|  2 | HD       | 2025-11-18 | Before market open | Consumer Cyclical      | $356.4B      | $362.36 | 16.62%       | 28.97%       | 1.74x         |
|  3 | ACM      | 2025-11-17 | After market close | Industrials            | $17.5B       | $133.52 | 19.97%       | 31.10%       | 1.56x         |
|  4 | MDT      | 2025-11-18 | Before market open | Healthcare             | $123.5B      | $95.87  | 16.25%       | 24.48%       | 1.51x         |
|  5 | HP       | 2025-11-17 | After market close | Energy                 | $2.7B        | $27.83  | 45.72%       | 57.52%       | 1.26x         |
|  6 | AS       | 2025-11-18 | Before market open | Consumer Cyclical      | $17.1B       | $30.37  | nan%         | nan%         | nanx          |
|  7 | BIDU     | 2025-11-18 | Before market open | Communication Services | $39.8B       | $116.00 | nan%         | nan%         | nanx          |
|  8 | BZ       | 2025-11-18 | Before market open | Communication Services | $9.5B        | $20.56  | nan%         | nan%         | nanx          |
|  9 | CAN      | 2025-11-18 | Before market open | Technology             | $400.1M      | $0.89   | nan%         | nan%         | nanx          |
| 10 | CISS     | 2025-11-18 | Before market open | Industrials            | $4.6M        | $1.65   | nan%         | nan%         | nanx          |
| 11 | DAC      | 2025-11-17 | After market close | Industrials            | $1.7B        | $94.61  | nan%         | nan%         | nanx          |
| 12 | ELTK     | 2025-11-18 | Before market open | Technology             | $76.6M       | $11.40  | nan%         | nan%         | nanx          |
| 13 | ESEA     | 2025-11-18 | Before market open | Industrials            | $431.3M      | $59.73  | nan%         | nan%         | nanx          |
| 14 | ESLT     | 2025-11-18 | Before market open | Industrials            | $23.3B       | $473.03 | nan%         | nan%         | nanx          |
| 15 | FUTU     | 2025-11-18 | Before market open | Financial Services     | $23.5B       | $165.77 | nan%         | nan%         | nanx          |
| 16 | GLAD     | 2025-11-17 | After market close | Financial Services     | $419.1M      | $19.30  | nan%         | nan%         | nanx          |
| 17 | GRRR     | 2025-11-18 | Before market open | Technology             | $286.1M      | $12.94  | nan%         | nan%         | nanx          |
| 18 | IIIV     | 2025-11-17 | After market close | Technology             | $953.4M      | $28.85  | nan%         | nan%         | nanx          |
| 19 | IQ       | 2025-11-18 | Before market open | Communication Services | $2.0B        | $2.08   | nan%         | nan%         | nanx          |
| 20 | ITRN     | 2025-11-18 | Before market open | Technology             | $734.7M      | $36.62  | nan%         | nan%         | nanx          |
| 21 | JHX      | 2025-11-18 | Before market open | Basic Materials        | $9.7B        | $16.69  | nan%         | nan%         | nanx          |
| 22 | KLAR     | 2025-11-18 | Before market open | Technology             | $13.2B       | $34.27  | nan%         | nan%         | nanx          |
| 23 | LFMD     | 2025-11-17 | After market close | Healthcare             | $224.3M      | $4.63   | nan%         | nan%         | nanx          |
| 24 | NMM      | 2025-11-18 | Before market open | Industrials            | $1.6B        | $52.48  | nan%         | nan%         | nanx          |
| 25 | NTIC     | 2025-11-18 | Before market open | Basic Materials        | $75.3M       | $8.08   | nan%         | nan%         | nanx          |
| 26 | OCSL     | 2025-11-18 | Before market open | Financial Services     | $1.2B        | $13.61  | nan%         | nan%         | nanx          |
| 27 | PDCC     | 2025-11-18 | Before market open | Financial Services     | $106.5M      | $15.78  | nan%         | nan%         | nanx          |
| 28 | PDD      | 2025-11-18 | Before market open | Consumer Cyclical      | $183.2B      | $130.95 | nan%         | nan%         | nanx          |
| 29 | TCOM     | 2025-11-17 | After market close | Consumer Cyclical      | $46.3B       | $72.03  | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
