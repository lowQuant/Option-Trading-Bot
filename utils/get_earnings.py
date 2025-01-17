from datetime import datetime, timedelta
import pandas_market_calendars as mcal
import pytz, requests
import pandas as pd

try:
    from .get_sector import get_sector
except:
    from get_sector import get_sector

def get_last_full_trading_day(current_datetime=None):
    # Create NYSE calendar
    nyse = mcal.get_calendar('NYSE')
    
    # Get NYSE timezone
    nyse_tz = pytz.timezone('America/New_York')
    
    # Use provided datetime or current time if none provided
    if current_datetime is None:
        current_datetime = datetime.now(pytz.timezone('Europe/Berlin'))
    elif current_datetime.tzinfo is None:
        current_datetime = pytz.timezone('Europe/Berlin').localize(current_datetime)
    
    # Convert to NYSE time
    nyse_time = current_datetime.astimezone(nyse_tz)
    
    # Get market schedule for the current day and the previous few days
    schedule = nyse.schedule(start_date=nyse_time.date() - timedelta(days=5), end_date=nyse_time.date())
    
    if not schedule.empty:
        # Get the last row of the schedule (should be today or the most recent trading day)
        last_day = schedule.iloc[-1]
        market_close = last_day['market_close'].tz_convert(nyse_tz)
        
        # If current time is before the market close of the last day in the schedule,
        # we need to look at the previous trading day
        if nyse_time < market_close:
            if len(schedule) > 1:
                return schedule.index[-2].date()
            else:
                # If there's only one day in the schedule, find the previous trading day
                previous_trading_days = nyse.valid_days(end_date=nyse_time.date() - timedelta(days=1), start_date=nyse_time.date() - timedelta(days=5))
                return previous_trading_days[-1].date()
        else:
            # If current time is after market close, the last day in the schedule is the last full trading day
            return last_day.name.date()
    else:
        # If there's no schedule for the recent days (e.g., long weekend), 
        # find the last trading day
        previous_trading_days = nyse.valid_days(end_date=nyse_time.date() - timedelta(days=1), start_date=nyse_time.date() - timedelta(days=5))
        return previous_trading_days[-1].date()

def get_current_or_next_trading_day(current_datetime=None):
    # Create NYSE calendar
    nyse = mcal.get_calendar('NYSE')
    
    # Get NYSE timezone
    nyse_tz = pytz.timezone('America/New_York')
    
    # Use provided datetime or current time if none provided
    if current_datetime is None:
        current_datetime = datetime.now(pytz.timezone('Europe/Berlin'))
    elif current_datetime.tzinfo is None:
        current_datetime = pytz.timezone('Europe/Berlin').localize(current_datetime)
    
    # Convert to NYSE time
    nyse_time = current_datetime.astimezone(nyse_tz)
    
    # Get market schedule for today and the next few days
    schedule = nyse.schedule(start_date=nyse_time.date(), end_date=nyse_time.date() + timedelta(days=10))
    
    if not schedule.empty:
        today_schedule = schedule.loc[schedule.index.date == nyse_time.date()]
        if not today_schedule.empty:
            market_open = today_schedule.iloc[0]['market_open'].tz_convert(nyse_tz)
            market_close = today_schedule.iloc[0]['market_close'].tz_convert(nyse_tz)
            
            # If the current time is before market close, return today
            if nyse_time <= market_close:
                return nyse_time.date()
    
    # If we're here, it means today is not a trading day or the market has closed
    # Find the next trading day
    next_trading_days = nyse.valid_days(start_date=nyse_time.date() + timedelta(days=1), end_date=nyse_time.date() + timedelta(days=10))
    return next_trading_days[0].date()

def get_earnings(start_date=None, end_date=None):
    # Get the last full trading day and the current or next trading day
    last_trading_day = get_last_full_trading_day()
    next_trading_day = get_current_or_next_trading_day()

    if not start_date and not end_date:
        # Define the SQL query with the specific dates and conditions
        query = f"""
        WITH LatestEarnings AS (
            SELECT *,
                ROW_NUMBER() OVER (PARTITION BY act_symbol ORDER BY `date` DESC) AS rn
            FROM `earnings_calendar`
            WHERE `when` IS NOT NULL
        )
        SELECT *
        FROM LatestEarnings
        WHERE rn = 1
        AND (
            (`date` = '{last_trading_day}' AND `when` = 'After market close') OR
            (`date` = '{next_trading_day}' AND `when` = 'Before market open')
        )
        ORDER BY `act_symbol` ASC;
        """
    else:
        query = f"""
        WITH LatestEarnings AS (
            SELECT *,
                ROW_NUMBER() OVER (PARTITION BY act_symbol ORDER BY `date` DESC) AS rn
            FROM `earnings_calendar`
            WHERE `when` IS NOT NULL
        )
        SELECT *
        FROM LatestEarnings
        WHERE rn = 1
        AND (
            (`date` >= '{start_date}' AND `date` <= '{end_date}')
        )
        ORDER BY `date` ASC, `act_symbol` ASC;
        """
    # URL encode the query
    encoded_query = requests.utils.quote(query)
    
    # Set the DoltHub API endpoint and parameters
    endpoint = f"https://www.dolthub.com/api/v1alpha1/post-no-preference/earnings/master?q={encoded_query}"
    
    # Make the API request
    response = requests.get(endpoint)
    response.raise_for_status()  # Check for errors

    # Check the content of the response
    data = response.json()

    # Handle the response and convert to a pandas DataFrame if successful
    if data.get('query_execution_status') == 'Success':
        df = pd.DataFrame(data['rows'])
        df = df.rename(columns={'act_symbol': 'symbol'})
        df = df[['symbol', 'date', 'when']]
        
        # Get additional info (sector, mcap, close) for all symbols
        info_dict = get_sector(df['symbol'].tolist())
        
        # Add new columns from the info dictionary
        df['sector'] = df['symbol'].map(lambda x: info_dict[x]['sector'])
        df['market_cap'] = df['symbol'].map(lambda x: info_dict[x]['mcap'])
        df['close'] = df['symbol'].map(lambda x: info_dict[x]['close'])
        
        return df
    else:
        print(f"Query Error: {data.get('query_execution_message')}")

def get_earnings_history(symbols=None) -> pd.DataFrame:
    """
    Get all available historical earnings data for specified symbols.
    
    Args:
        symbols: Symbol string or list of symbols (if None, gets all symbols)
        
    Returns:
        DataFrame with historical earnings data
    """
    # Build base query
    query = """
    SELECT *
    FROM earnings_calendar
    WHERE `when` IS NOT NULL
    """
    
    # Add symbol filter if provided
    if symbols:
        # Convert single symbol to list
        if isinstance(symbols, str):
            symbols = [symbols]
            
        symbols_str = ', '.join(f"'{symbol}'" for symbol in symbols)
        query += f"AND act_symbol IN ({symbols_str})"
    
    query += "ORDER BY `date` ASC, `act_symbol` ASC;"
    
    # URL encode the query
    encoded_query = requests.utils.quote(query)
    
    # Set the DoltHub API endpoint
    endpoint = f"https://www.dolthub.com/api/v1alpha1/post-no-preference/earnings/master?q={encoded_query}"
    
    # Make the API request
    response = requests.get(endpoint)
    response.raise_for_status()
    
    # Parse response
    data = response.json()
    if data.get('query_execution_status') == 'Success':
        if not data.get('rows'):
            print("No earnings data found")
            return pd.DataFrame()
            
        df = pd.DataFrame(data['rows'])
        
        # Rename columns for consistency
        df = df.rename(columns={'act_symbol': 'symbol'})
        
        # Convert date to datetime
        df['date'] = pd.to_datetime(df['date'])
        
        return df
    else:
        print(f"Query Error: {data.get('query_execution_message')}")
        return None

def get_future_earnings(days_ahead: int = 11) -> pd.DataFrame:
    """
    Get earnings happening n days ahead from tomorrow.
    
    Args:
        days_ahead: Number of days ahead from tomorrow to look for earnings
        
    Returns:
        DataFrame with earnings and sector information
    """
    # Get tomorrow's date
    tomorrow = datetime.now().date() + timedelta(days=1)
    target_date = tomorrow + timedelta(days=days_ahead)
    
    # Get earnings for the target date
    df = get_earnings(start_date=target_date, end_date=target_date)
    if df is None or df.empty:
        print(f"No earnings found for {target_date}")
        return pd.DataFrame()
        
    # Get additional info from get_sector
    info_dict = get_sector(df['symbol'].tolist())
    
    # Add new columns from the info dictionary
    df['sector'] = df['symbol'].map(lambda x: info_dict[x]['sector'])
    df['market_cap'] = df['symbol'].map(lambda x: info_dict[x]['mcap'])
    df['close'] = df['symbol'].map(lambda x: info_dict[x]['close'])
    
    return df

if __name__ == "__main__":
    # Example usage with single symbol
    print("\nTesting with single symbol:")
    df1 = get_earnings_history('AAPL')
    if df1 is not None and not df1.empty:
        print(df1)
        
    # Example usage with list of symbols
    print("\nTesting with multiple symbols:")
    df2 = get_earnings_history(['MSFT', 'GOOGL'])
    if df2 is not None and not df2.empty:
        print(df2[['symbol', 'date', 'when']].head().to_string())
