import pandas as pd
from datetime import datetime
import pytz
from tabulate import tabulate
import os

def format_table(df, headers='keys'):
    """Convert DataFrame to markdown table string"""
    return tabulate(df, headers=headers, tablefmt='pipe', floatfmt=".4f")

def update_readme():
    # Ensure data directory exists
    os.makedirs('data', exist_ok=True)
    
    # Read the analysis results
    vol_df = pd.read_csv("data/future_earnings.csv")
    analysis_df = pd.read_csv("data/hist_iv_analysis.csv")
    
    # Format the update time
    ny_tz = pytz.timezone('America/New_York')
    update_time = datetime.now(ny_tz).strftime('%Y-%m-%d %H:%M:%S %Z')
    
    # Create README content
    readme_content = f"""# Options Trading Bot Analysis

Last updated: {update_time}

## Upcoming Earnings and Current Volatility

Top 10 stocks by volatility premium (current IV / historical volatility):

{format_table(vol_df.nlargest(10, 'vol_premium'))}

## Historical IV Analysis

Top 10 stocks with largest negative deviation from historical pre-earnings IV:

{format_table(analysis_df.head(10))}

Top 10 stocks with largest positive deviation from historical pre-earnings IV:

{format_table(analysis_df.tail(10).iloc[::-1])}

## Data Interpretation

- **Negative deviation**: Current IV is lower than historical pre-earnings IV
- **Positive deviation**: Current IV is higher than historical pre-earnings IV
- **Count**: Number of historical earnings events analyzed
- **Std**: Standard deviation of historical IVs, indicating consistency of the pattern
"""
    
    # Write to README.md
    with open("README.md", "w") as f:
        f.write(readme_content)

if __name__ == "__main__":
    update_readme()