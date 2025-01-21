from collections import defaultdict
import matplotlib.pyplot as plt
import yfinance as yf
import numpy as np
import pandas as pd
import os
from datetime import datetime

from .get_sector import get_sector

def get_index_composition(symbols=None, index='SPY', chunk_size=30, show=False):
    """
    Get the sector composition of an index or list of symbols.
    
    Args:
        symbols: Optional list of symbols to analyze
        index: Either 'SPY' for S&P 500 or 'QQQ' for NASDAQ-100
        chunk_size: Number of symbols to process in each chunk
        show: If True, display the pie chart. If False, save it to data directory (default: False)
    """
    print(f"Fetching {'index composition' if symbols is None else 'symbol information'}...")
    
    if symbols is None:
        if index.lower() == 'spy':
            print("Loading S&P 500 components...")
            spx = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')[0]
            symbols = spx['Symbol'].tolist()
        elif index.lower() == 'qqq':
            print("Loading NASDAQ-100 components...")
            qqq = pd.read_html('https://en.wikipedia.org/wiki/Nasdaq-100')[4]
            symbols = qqq['Ticker'].tolist()
        else:
            raise ValueError("Invalid index name. Please use 'spy' or 'qqq'.")
    
    print(f"\nFetching data for {len(symbols)} symbols...")
    print("(Data will be cached locally to avoid repeated API calls)")
    info_dict = get_sector(symbols, chunk_size=chunk_size)
    
    # Filter out failed requests
    valid_data = {k: v for k, v in info_dict.items() if v['sector'] is not None}
    failed_count = len(info_dict) - len(valid_data)
    if failed_count > 0:
        print(f"\nWarning: Failed to fetch data for {failed_count} symbols")
    
    mktcap_by_sector = defaultdict(float)
    for _, data in valid_data.items():
        if data['sector'] and data['mcap']:  # Only count if we have both sector and market cap
            mktcap_by_sector[data['sector']] += data['mcap']
    
    if not mktcap_by_sector:
        raise ValueError("No valid sector data found. Please try again later.")
    
    # Prepare data for the pie chart
    labels = list(mktcap_by_sector.keys())
    sizes = list(mktcap_by_sector.values())
    
    # Sort sectors by size for better visualization
    sorted_data = sorted(zip(sizes, labels), reverse=True)
    sizes, labels = zip(*sorted_data)
    
    # Create the pie chart
    plt.figure(figsize=(12, 8))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title(f"{'S&P 500' if index.lower() == 'spy' else 'NASDAQ-100'} Sector Composition")
    plt.axis('equal')
    
    # Add total market cap information
    total_mcap = sum(sizes)
    plt.figtext(0.95, 0.05, f'Total Market Cap: ${total_mcap:,.0f}M', 
                horizontalalignment='right')
    
    # Save or show the plot
    if show:
        plt.show()
    else:
        # Create filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{index.lower()}_sector_composition_{timestamp}.png"
        
        # Get path to data directory
        data_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
        filepath = os.path.join(data_dir, filename)
        
        # Save the plot
        plt.savefig(filepath, bbox_inches='tight', dpi=300)
        plt.close()
        print(f"\nChart saved to: {filepath}")
    
    return mktcap_by_sector

if __name__ == "__main__":
    get_index_composition(chunk_size=30, show=True)  # Show the chart when running directly