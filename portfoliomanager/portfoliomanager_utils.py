"""
Utility functions for the PortfolioManager class.
This file is prepared for future code organization where parts of the PortfolioManager class
may be moved here for better maintainability.
"""

# Import statements will be added as needed when moving functions here
from datetime import datetime
import pytz

def is_market_open(ib, symbol='SPY', exchange='SMART', currency='USD'):
    """
    Check if the market is currently open based on US market hours.
    Returns True during regular market hours (9:30 AM - 4:00 PM ET)
    """
    # Get current time in ET
    et = pytz.timezone('America/New_York')
    now = datetime.now(et)
    
    # Check if it's a weekday
    if now.weekday() >= 5:  # Saturday = 5, Sunday = 6
        return False
    
    # Convert to time only for easier comparison
    market_time = now.time()
    
    # Regular market hours: 9:30 AM - 4:00 PM ET
    market_open = datetime.strptime('9:30', '%H:%M').time()
    market_close = datetime.strptime('16:00', '%H:%M').time()
    
    return market_open <= market_time <= market_close
