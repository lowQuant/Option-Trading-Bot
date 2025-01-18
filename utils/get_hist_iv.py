import pandas as pd
import requests
from datetime import datetime, timedelta
import pandas_market_calendars as mcal

try:
    from .get_earnings import get_earnings, get_future_earnings
    from .get_vol_data import get_vol_data
except:
    from get_earnings import get_earnings, get_future_earnings
    from get_vol_data import get_vol_data

def get_trading_day(date, offset=0):
    """Get the next or previous trading day."""
    nyse = mcal.get_calendar('NYSE')
    if offset > 0:
        trading_days = nyse.valid_days(start_date=date, end_date=date + timedelta(days=5))
        return trading_days[offset].date() if len(trading_days) > offset else None
    else:
        trading_days = nyse.valid_days(start_date=date - timedelta(days=5), end_date=date)
        return trading_days[offset-1].date() if len(trading_days) >= abs(offset) else None

def get_earnings_dates(symbol):
    """Get earnings dates for a given symbol."""
    today = datetime.now().date().isoformat()
    query_earnings = f"""
    SELECT act_symbol, date, `when`
    FROM earnings_calendar
    WHERE act_symbol = '{symbol}'
    ORDER BY date DESC;
    """
    
    encoded_query = requests.utils.quote(query_earnings)
    endpoint = f"https://www.dolthub.com/api/v1alpha1/post-no-preference/earnings/master?q={encoded_query}"
    
    response = requests.get(endpoint)
    response.raise_for_status()
    
    data = response.json()
    if not data.get('rows'):
        return None
    
    df_earnings = pd.DataFrame(data['rows'])
    df_earnings = df_earnings.rename(columns={'act_symbol': 'symbol'})
    df_earnings['date'] = pd.to_datetime(df_earnings['date'])
    
    return df_earnings

def get_iv_data(symbol, date1, date2):
    """Get IV data for a given symbol and dates."""
    query_iv = f"""
    SELECT act_symbol, date, iv_current
    FROM volatility_history
    WHERE act_symbol = '{symbol}'
    AND date IN ('{date1}', '{date2}')
    ORDER BY date ASC;
    """
    
    encoded_query = requests.utils.quote(query_iv)
    endpoint = f"https://www.dolthub.com/api/v1alpha1/post-no-preference/options/master?q={encoded_query}"
    
    response = requests.get(endpoint)
    if response.status_code != 200:
        return None
    
    data = response.json()
    if not data.get('rows'):
        return None
    
    df_iv = pd.DataFrame(data['rows'])
    df_iv['date'] = pd.to_datetime(df_iv['date']).dt.date  # Convert to date for comparison
    
    return df_iv

def get_hist_iv_around_earnings(symbols, debug=False):
    """Get historical implied volatility around earnings dates"""
    results = []
    
    for symbol in symbols:
        # Get earnings dates
        earnings_dates = get_earnings_dates(symbol)
        
        if earnings_dates is None or earnings_dates.empty:
            print(f"No earnings dates found for {symbol}")
            continue
            
        for _, row in earnings_dates.iterrows():
            earnings_date = row['date'].date()
            earnings_time = row['when']
            
            if debug:
                print(f"\n{symbol} reports {earnings_time} on {earnings_date}")
            
            # Get IV for the day before and after earnings
            if earnings_time == 'Before market open':
                date1 = get_trading_day(earnings_date, -1)
                date2 = earnings_date
            else:  # After market close
                date1 = earnings_date
                date2 = get_trading_day(earnings_date, 1)
                
            if debug:
                print(f"Looking for IV on {date1} (same day) and {date2} (next trading day)")
            
            # Get IV data
            df_iv = get_iv_data(symbol, date1, date2)
            
            if df_iv is None or df_iv.empty:
                if debug:
                    print(f"No IV data found for {symbol}")
                continue
                
            if debug:
                if len(df_iv) < 2:
                    print(f"❌ Only found {len(df_iv)} IV data points for {symbol}:")
                    for _, iv_row in df_iv.iterrows():
                        print(f"  - {iv_row['date']}: {iv_row['iv_current']}")
                else:
                    print(f"✅ Found both IV data points for {symbol}:")
                    for _, iv_row in df_iv.iterrows():
                        print(f"  - {iv_row['date']}: {iv_row['iv_current']}")
            
            # Add to results even if we only have one data point
            iv_before = float('nan')
            iv_after = float('nan')
            
            # Process available data points
            for _, iv_row in df_iv.iterrows():
                try:
                    if iv_row['date'] == date1 and iv_row['iv_current'] is not None:
                        iv_before = float(iv_row['iv_current'])
                    elif iv_row['date'] == date2 and iv_row['iv_current'] is not None:
                        iv_after = float(iv_row['iv_current'])
                except (ValueError, TypeError):
                    continue
            
            # Calculate change percentage if we have both points
            if not pd.isna(iv_before) and not pd.isna(iv_after):
                iv_change_pct = ((iv_after - iv_before) / iv_before) * 100
            else:
                iv_change_pct = float('nan')
            
            # Only add to results if we have at least one valid IV value
            if not (pd.isna(iv_before) and pd.isna(iv_after)):
                results.append({
                    'symbol': symbol,
                    'earnings_date': earnings_date,
                    'earnings_time': earnings_time,
                    'iv_before': iv_before,
                    'iv_after': iv_after,
                    'iv_change_pct': iv_change_pct
                })
    
    if not results:
        return pd.DataFrame()
        
    df = pd.DataFrame(results)
    
    if debug:
        print("\nSuccessfully processed earnings events:")
        print(df.to_string())
    
    return df

def analyze_iv_patterns(hist_df, vol_df, fut_earnings):
    """Analyze historical IV patterns and compare with current IV levels"""
    if hist_df.empty:
        return None
        
    # Calculate mean historical IVs by symbol
    hist_stats = hist_df.groupby('symbol').agg({
        'iv_before': ['mean', 'std', 'count'],
        'iv_after': ['mean', 'std', 'count']
    }).round(4)
    
    # Flatten column names
    hist_stats.columns = [f"{col[0]}_{col[1]}" for col in hist_stats.columns]
    hist_stats = hist_stats.reset_index()
    
    # Merge with current IV data and future earnings date
    analysis_df = pd.merge(hist_stats, 
                          vol_df[['symbol', 'iv_current', 'sector', 'market_cap']], 
                          on='symbol', 
                          how='inner')
    
    # Add future earnings date
    earnings_dates = fut_earnings[['symbol', 'date', 'when']].copy()
    earnings_dates.columns = ['symbol', 'next_earnings_date', 'earnings_time']
    analysis_df = pd.merge(analysis_df, earnings_dates, on='symbol', how='left')
    
    # Calculate deviations from historical means
    analysis_df['deviation_from_before'] = (analysis_df['iv_current'] - analysis_df['iv_before_mean'])
    analysis_df['deviation_from_after'] = (analysis_df['iv_current'] - analysis_df['iv_after_mean'])
    
    # Sort by deviation from historical pre-earnings IV
    analysis_df = analysis_df.sort_values('deviation_from_before', ascending=True)
    
    # Reorder columns for better readability
    cols = ['symbol', 'next_earnings_date', 'earnings_time', 'sector', 'market_cap',
            'iv_current', 'iv_before_mean', 'deviation_from_before',
            'iv_after_mean', 'deviation_from_after',
            'iv_before_std', 'iv_before_count',
            'iv_after_std', 'iv_after_count']
    
    return analysis_df[cols]

if __name__ == "__main__":
    # Example usage
    fut_earnings = get_future_earnings(days_ahead=11)
    vol_df = get_vol_data(fut_earnings)
    print(vol_df)
    print("\nSaving results to data/future_earnings.csv")
    vol_df.to_csv("data/future_earnings.csv", index=False)
    
    # Get historical IV data
    test_symbols = fut_earnings['symbol'].tolist()
    hist_df = get_hist_iv_around_earnings(test_symbols, debug=True)
    
    # Analyze patterns
    analysis_df = analyze_iv_patterns(hist_df, vol_df, fut_earnings)
    
    if analysis_df is not None:
        print("\nAnalysis of Current IV vs Historical Earnings IV:")
        print(analysis_df.to_string())
        
        # Save results
        print("\nSaving results to data/hist_iv_analysis.csv")
        analysis_df.to_csv("data/hist_iv_analysis.csv", index=False)
        
        print("\nSaving raw historical data to data/hist_iv_earnings.csv")
        hist_df.to_csv("data/hist_iv_earnings.csv", index=False)
