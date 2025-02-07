import sys
import os

# Ensure the script can find dependencies
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    import pandas as pd
    from datetime import datetime
    import pytz
    from tabulate import tabulate
except ImportError as e:
    print(f"Dependency error: {e}")
    print("Please install required packages: pandas, pytz, tabulate")
    sys.exit(1)

def format_table(df, headers='keys'):
    """Convert DataFrame to markdown table string"""
    return tabulate(df, headers=headers, tablefmt='pipe', floatfmt=".4f")

def format_currency(value):
    """Format large numbers with currency-like formatting"""
    if pd.isna(value):
        return 'N/A'
    if value >= 1_000_000:
        return f'${value/1_000_000:.1f}tr'
    elif value >= 1_000:
        return f'${value/1_000:.1f}B'
    elif value <= 1_000:
        return f'${value:.1f}M'
    return f'${value:.1f}M'

def update_readme():
    # Ensure data directory exists
    os.makedirs('data', exist_ok=True)
    
    # Read the volatility data
    vol_df = pd.read_csv("data/vol_premium.csv")
    
    # Format the update time
    ny_tz = pytz.timezone('America/New_York')
    update_time = datetime.now(ny_tz).strftime('%Y-%m-%d %H:%M:%S %Z')
    
    # Prepare vol_df for display
    display_vol_df = vol_df.copy()
    display_vol_df['market_cap'] = display_vol_df['market_cap'].apply(format_currency)
    display_vol_df['close'] = display_vol_df['close'].apply(lambda x: f'${x:.2f}')
    display_vol_df['hv_current'] = display_vol_df['hv_current'].apply(lambda x: f'{x*100:.2f}%')
    display_vol_df['iv_current'] = display_vol_df['iv_current'].apply(lambda x: f'{x*100:.2f}%')
    
    # Create a formatted column for display while keeping original numeric column
    display_vol_df['vol_premium_display'] = display_vol_df['vol_premium'].apply(lambda x: f'{x:.2f}x')
    
    # Use nlargest on the numeric column
    top_30_vol_premium = display_vol_df.nlargest(30, 'vol_premium')
    
    # Replace the display column for formatting in the table
    top_30_vol_premium['vol_premium'] = top_30_vol_premium['vol_premium_display']
    top_30_vol_premium.drop(columns=['vol_premium_display'], inplace=True)
    
    # Create README content
    readme_content = f"""# Options Trading Bot Analysis

## 🚀 Project Overview
Work in progress. This project is focused on identifying trading opportunities with a statistical edge.
We are selling volatility after earnings announcements and buying volatility before earnings.
Both strategies can be explained by behavioral finance and are likely anomalies with a chance to persist over time.

### Strategies
- 📉 **Short Put Options**: Post earnings announcements
- 📈 **Long Straddles**: Prior to earnings when IV is low
- 📦 **Box Spreads**: Between earnings seasons

## 🕒 Last Updated: {update_time}

### Top 30 Upcoming Earnings by Volatility Premium

{format_table(top_30_vol_premium, headers='keys')}

## 📝 Data Interpretation

- **Volatility Premium**: 
  - Ratio of current implied volatility to historical volatility
  - Higher values indicate potential candidates for short puts
  - Values above 2x suggest significant overpricing of options

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