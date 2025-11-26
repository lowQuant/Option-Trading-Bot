# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: 2025-11-25 20:53:50 EST

### Top 30 Upcoming Earnings by Volatility Premium

|    | symbol   | date       | when               | sector                 | market_cap   | close   | hv_current   | iv_current   | vol_premium   |
|---:|:---------|:-----------|:-------------------|:-----------------------|:-------------|:--------|:-------------|:-------------|:--------------|
|  0 | URBN     | 2025-11-25 | After market close | Consumer Cyclical      | $6.1B        | $62.22  | 32.73%       | 70.78%       | 2.16x         |
|  1 | NTNX     | 2025-11-25 | After market close | Technology             | $15.9B       | $58.32  | 32.95%       | 62.53%       | 1.90x         |
|  2 | ADSK     | 2025-11-25 | After market close | Technology             | $63.0B       | $289.85 | 21.42%       | 38.72%       | 1.81x         |
|  3 | DE       | 2025-11-26 | Before market open | Industrials            | $134.7B      | $487.23 | 17.65%       | 31.72%       | 1.80x         |
|  4 | NTAP     | 2025-11-25 | After market close | Technology             | $22.3B       | $108.96 | 26.36%       | 44.20%       | 1.68x         |
|  5 | WDAY     | 2025-11-25 | After market close | Technology             | $62.4B       | $226.64 | 31.10%       | 46.53%       | 1.50x         |
|  6 | GES      | 2025-11-25 | After market close | Consumer Cyclical      | $889.2M      | $16.91  | 5.25%        | 7.22%        | 1.38x         |
|  7 | ARWR     | 2025-11-25 | After market close | Healthcare             | $6.5B        | $44.26  | 59.12%       | 80.17%       | 1.36x         |
|  8 | DELL     | 2025-11-25 | After market close | Technology             | $84.7B       | $127.22 | 44.33%       | 58.77%       | 1.33x         |
|  9 | HPQ      | 2025-11-25 | After market close | Technology             | $22.8B       | $24.38  | 41.66%       | 44.57%       | 1.07x         |
| 10 | CLSK     | 2025-11-25 | After market close | Financial Services     | $3.2B        | $11.48  | 109.25%      | 101.71%      | 0.93x         |
| 11 | ALAR     | 2025-11-26 | Before market open | Technology             | $84.0M       | $11.72  | nan%         | nan%         | nanx          |
| 12 | AMBA     | 2025-11-25 | After market close | Technology             | $3.9B        | $89.57  | nan%         | nan%         | nanx          |
| 13 | AMBR     | 2025-11-26 | Before market open | Technology             | $148.0M      | $1.36   | nan%         | nan%         | nanx          |
| 14 | BBAR     | 2025-11-25 | After market close | Financial Services     | $3.0B        | $13.99  | nan%         | nan%         | nanx          |
| 15 | CLGN     | 2025-11-26 | Before market open | Healthcare             | $28.5M       | $2.22   | nan%         | nan%         | nanx          |
| 16 | CMBT     | 2025-11-26 | Before market open | Energy                 | $3.1B        | $10.15  | nan%         | nan%         | nanx          |
| 17 | CMCM     | 2025-11-26 | Before market open | Communication Services | $261.2M      | $7.89   | nan%         | nan%         | nanx          |
| 18 | EH       | 2025-11-26 | Before market open | Industrials            | $966.8M      | $14.15  | nan%         | nan%         | nanx          |
| 19 | GOTU     | 2025-11-26 | Before market open | Consumer Defensive     | $646.4M      | $2.65   | nan%         | nan%         | nanx          |
| 20 | HDL      | 2025-11-26 | Before market open | Consumer Cyclical      | $1.1B        | $17.83  | nan%         | nan%         | nanx          |
| 21 | LEE      | 2025-11-26 | Before market open | Communication Services | $27.2M       | $4.25   | nan%         | nan%         | nanx          |
| 22 | LI       | 2025-11-26 | Before market open | Consumer Cyclical      | $18.6B       | $18.12  | nan%         | nan%         | nanx          |
| 23 | LWLG     | 2025-11-25 | After market close | Basic Materials        | $600.0M      | $4.36   | nan%         | nan%         | nanx          |
| 24 | NOAH     | 2025-11-25 | After market close | Financial Services     | $781.4M      | $10.44  | nan%         | nan%         | nanx          |
| 25 | PD       | 2025-11-25 | After market close | Technology             | $1.4B        | $14.86  | nan%         | nan%         | nanx          |
| 26 | SB       | 2025-11-25 | After market close | Industrials            | $500.3M      | $4.91   | nan%         | nan%         | nanx          |
| 27 | SNT      | 2025-11-25 | After market close | Industrials            | $102.2M      | $4.31   | nan%         | nan%         | nanx          |
| 28 | WOOF     | 2025-11-25 | After market close | Consumer Cyclical      | $832.4M      | $2.79   | nan%         | nan%         | nanx          |
| 29 | ZS       | 2025-11-25 | After market close | Technology             | $46.2B       | $280.35 | nan%         | nan%         | nanx          |

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
