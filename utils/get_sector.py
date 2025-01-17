import yfinance as yf
import asyncio
from typing import Union, List

async def fetch_ticker_info(symbol: str) -> dict:
    """Fetch ticker information asynchronously using yfinance."""
    try:
        # Run yfinance in a thread pool to not block the event loop
        loop = asyncio.get_event_loop()
        ticker = await loop.run_in_executor(None, lambda: yf.Ticker(symbol))
        info = await loop.run_in_executor(None, lambda: ticker.info)
        
        sector = info.get('sector', None)
        mcap = info.get('marketCap', None)
        mcap = mcap / 1000000 if mcap is not None else None
        close = info.get('previousClose', None)
        close = close if close is not None else None
        return {'symbol': symbol, 'sector': sector, 'mcap': mcap, 'close': close}
    except Exception as e:
        print(f"Error fetching {symbol}: {str(e)}")
        return {'symbol': symbol, 'sector': None, 'mcap': None, 'close': None}

async def get_sector_async(symbols: Union[str, List[str]]) -> dict:
    """
    Asynchronously get sector information for one or multiple symbols.
    """
    if isinstance(symbols, str):
        symbols = [symbols]
    
    tasks = [fetch_ticker_info(symbol) for symbol in symbols]
    results = await asyncio.gather(*tasks)
    return {result['symbol']: result for result in results}

def get_sector(symbols: Union[str, List[str]]) -> dict:
    """
    Get sector information for one or multiple symbols.
    
    Args:
        symbols: Single symbol string or list of symbol strings
        
    Returns:
        Dictionary mapping symbols to their sectors
    """
    return asyncio.run(get_sector_async(symbols))
