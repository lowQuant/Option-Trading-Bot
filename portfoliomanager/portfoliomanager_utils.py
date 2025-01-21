"""
Utility functions for the PortfolioManager class.
This file is prepared for future code organization where parts of the PortfolioManager class
may be moved here for better maintainability.
"""

# Import statements will be added as needed when moving functions here
from datetime import datetime
import pytz
from ib_async import Stock

def is_market_open(ib, symbol='SPY', exchange='SMART', currency='USD'):
    """
    Check if the market is currently open for a given symbol.
    
    Args:
        ib: IB client instance
        symbol: Stock symbol to check
        exchange: Exchange to check (default: SMART)
        currency: Currency of the stock (default: USD)
        
    Returns:
        bool: True if market is open, False otherwise
    """
    contract = Stock(symbol, exchange, currency)
    
    try:
        details = ib.reqContractDetails(contract)
        
        if not details:
            print(f"No contract details found for {symbol}")
            return False
        
        # Extract trading hours
        trading_hours = details[0].tradingHours
        timezone_exchange = details[0].timeZoneId
        
        # Convert to exchange timezone
        exchange_tz = pytz.timezone(timezone_exchange)
        now = datetime.now(exchange_tz)

        for period in trading_hours.split(';'):
            if not period.strip():  # Skip empty periods
                continue
            
            try:
                start, end = period.split('-')
                start_time = datetime.fromisoformat(start).replace(tzinfo=exchange_tz)
                end_time = datetime.fromisoformat(end).replace(tzinfo=exchange_tz)
                
                if start_time <= now <= end_time:
                    return True
            except ValueError as e:
                print(f"Skipping invalid period format: {period}")
                continue
        
        return False
    
    except Exception as e:
        print(f"Error checking market hours: {e}")
        return False
