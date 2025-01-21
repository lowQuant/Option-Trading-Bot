import yfinance as yf
import asyncio
from typing import Union, List
import time
import random
from asyncio import Semaphore
import json
import os
from datetime import datetime, timedelta

# Update cache file path to use data directory
CACHE_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "stock_data_cache.json")
CACHE_EXPIRY_DAYS = 7  # Cache data for 7 days

def load_cache():
    """Load cached stock data if available."""
    if os.path.exists(CACHE_FILE):
        try:
            with open(CACHE_FILE, 'r') as f:
                cache_data = json.load(f)
                # Filter out expired entries
                current_time = datetime.now()
                valid_cache = {}
                for symbol, data in cache_data.items():
                    cache_time = datetime.fromisoformat(data['cache_time'])
                    if current_time - cache_time < timedelta(days=CACHE_EXPIRY_DAYS):
                        valid_cache[symbol] = data
                return valid_cache
        except Exception as e:
            print(f"Warning: Could not load cache: {e}")
    return {}

def save_cache(cache_data):
    """Save stock data to cache."""
    try:
        with open(CACHE_FILE, 'w') as f:
            json.dump(cache_data, f)
    except Exception as e:
        print(f"Warning: Could not save cache: {e}")

async def fetch_ticker_info_with_retry(symbol: str, semaphore: Semaphore, cache: dict) -> dict:
    """Fetch ticker information asynchronously using yfinance with retry logic."""
    # Check cache first
    if symbol in cache:
        return cache[symbol]['data']
    
    try:
        async with semaphore:  # Limit concurrent requests
            # Add delay between requests
            await asyncio.sleep(0.7)  # Reduced delay for faster processing
            
            # Run yfinance in a thread pool to not block the event loop
            loop = asyncio.get_event_loop()
            ticker = await loop.run_in_executor(None, lambda: yf.Ticker(symbol))
            info = await loop.run_in_executor(None, lambda: ticker.info)
            
            result = {
                'symbol': symbol,
                'sector': info.get('sector', None),
                'mcap': info.get('marketCap', None) / 1000000 if info.get('marketCap') else None,
                'close': info.get('previousClose', None)
            }
            
            # Update cache
            cache[symbol] = {
                'data': result,
                'cache_time': datetime.now().isoformat()
            }
            return result
            
    except Exception as e:
        print(f"Error fetching {symbol}: {str(e)}")
        return {'symbol': symbol, 'sector': None, 'mcap': None, 'close': None}

async def process_symbol_chunk(symbols: List[str], cache: dict, batch_size: int = 5) -> dict:
    """Process a chunk of symbols with rate limiting."""
    semaphore = Semaphore(batch_size)
    tasks = [fetch_ticker_info_with_retry(symbol, semaphore, cache) for symbol in symbols]
    results = await asyncio.gather(*tasks)
    return {result['symbol']: result for result in results}

def get_sector(symbols: Union[str, List[str]], chunk_size: int = 30) -> dict:
    """
    Get sector information for one or multiple symbols.
    
    Args:
        symbols: Single symbol string or list of symbol strings
        chunk_size: Number of symbols to process in each chunk (default: 30)
        
    Returns:
        Dictionary mapping symbols to their sectors
    """
    if isinstance(symbols, str):
        symbols = [symbols]
    
    # Load cache
    cache = load_cache()
    all_results = {}
    
    # Process symbols in chunks
    for i in range(0, len(symbols), chunk_size):
        chunk = symbols[i:i + chunk_size]
        print(f"Processing symbols {i+1}-{min(i+chunk_size, len(symbols))} of {len(symbols)}...")
        
        # Check which symbols need to be fetched
        to_fetch = [s for s in chunk if s not in cache]
        if to_fetch:
            results = asyncio.run(process_symbol_chunk(to_fetch, cache, batch_size=5))
            all_results.update(results)
        
        # Add cached results
        for s in chunk:
            if s in cache:
                all_results[s] = cache[s]['data']
    
    # Save updated cache
    save_cache(cache)
    
    return all_results
