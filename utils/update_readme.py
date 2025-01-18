import pandas as pd
from datetime import datetime
import pytz
from tabulate import tabulate
import os

def format_table(df, headers='keys'):
    """Convert DataFrame to markdown table string"""
    return tabulate(df, headers=headers, tablefmt='pipe', floatfmt=".4f")

def format_currency(value):
    """Format large numbers with currency-like formatting"""
    if pd.isna(value):
        return 'N/A'
    if value >= 1_000_000_000:
        return f'${value/1_000_000_000:.1f}B'
    elif value >= 1_000_000:
        return f'${value/1_000_000:.1f}M'
    elif value >= 1_000:
        return f'${value/1_000:.1f}K'
    return f'${value:.2f}'

def update_readme():
    # Ensure data directory exists
    os.makedirs('data', exist_ok=True)
    
    # Read the analysis results
    vol_df = pd.read_csv("data/vol_premium.csv")
    analysis_df = pd.read_csv("data/hist_iv_analysis.csv")
    
    # Format the update time
    ny_tz = pytz.timezone('America/New_York')
    update_time = datetime.now(ny_tz).strftime('%Y-%m-%d %H:%M:%S %Z')
    
    # Prepare vol_df for display
    display_vol_df = vol_df.copy()
    display_vol_df['market_cap'] = display_vol_df['market_cap'].apply(format_currency)
    display_vol_df['close'] = display_vol_df['close'].apply(lambda x: f'${x:.2f}')
    display_vol_df['hv_current'] = display_vol_df['hv_current'].apply(lambda x: f'{x*100:.2f}%')
    display_vol_df['iv_current'] = display_vol_df['iv_current'].apply(lambda x: f'{x*100:.2f}%')
    display_vol_df['vol_premium'] = display_vol_df['vol_premium'].apply(lambda x: f'{x:.2f}x')
    
    # Create README content
    readme_content = f"""# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies are based on risk premia 

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: {update_time}

### 🔥 Top 10 Upcoming Earnings by Volatility Premium

{format_table(display_vol_df.nlargest(10, 'vol_premium'), headers='keys')}

### 📊 Historical Implied Volatility Analysis

#### Top 10Stocks with Low IV compared to their historical values before earnings

{format_table(analysis_df.head(10), headers='keys')}

## 📝 Data Interpretation

- **Volatility Premium (Vol Premium)**: 
  - Ratio of current implied volatility to historical volatility
  - Potential candidates for short puts

- **Historical IV Deviation**: 
  - Measures difference between current and historical pre-earnings implied volatility
  - Negative values indicate current IV is lower than historical pre-earnings IV
  - Potential candidates for long straddles

## ⚠️ Disclaimer
- This is an experimental trading bot
- Always perform your own financial research
- Past performance does not guarantee future results
"""
    
    # Write to README.md
    with open("README.md", "w") as f:
        f.write(readme_content)

if __name__ == "__main__":
    update_readme()