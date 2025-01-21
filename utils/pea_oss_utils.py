import asyncio
import math
import numpy as np
import pandas as pd
from datetime import datetime
from ib_insync import *

async def process_get_filtered_put_options(ib, symbol, min_dte=0, max_dte=60, strike_range_percent=0.25):
    """Process a single symbol to get filtered put options."""
    try:
        stock = Stock(symbol, 'SMART', 'USD')
        await ib.qualifyContractsAsync(stock)
        
        [ticker] = await ib.reqTickersAsync(stock)
        stock_price = ticker.marketPrice() if not math.isnan(ticker.marketPrice()) else ticker.close

        if math.isnan(stock_price) or stock_price is None:
            print(f"Unable to get valid stock price for {symbol}")
            return None

        # Calculate strike range
        lower_strike = stock_price * (1 - strike_range_percent)  
        upper_strike = stock_price * (1 + strike_range_percent) 
        
        chains = await ib.reqSecDefOptParamsAsync(stock.symbol, '', stock.secType, stock.conId)
        chain = next((c for c in chains if c.exchange == 'SMART'), None)
        
        if not chain:
            print(f"No SMART chain found for {symbol}")
            return None
        
        today = datetime.now().date()
        
        # Filter valid expirations and strikes
        valid_expirations = [exp for exp in chain.expirations 
                           if min_dte <= (datetime.strptime(exp, '%Y%m%d').date() - today).days <= max_dte]
        valid_strikes = [strike for strike in chain.strikes 
                       if lower_strike <= strike <= upper_strike]
        
        if not valid_expirations or not valid_strikes:
            print(f"No valid expirations or strikes found for {symbol}")
            return None

        # Create option contracts
        contracts = [Option(symbol, exp, strike, 'P', 'SMART') 
                    for exp in valid_expirations 
                    for strike in valid_strikes]
        
        # Qualify contracts and get market data
        contracts = await ib.qualifyContractsAsync(*contracts)
        tickers = await ib.reqTickersAsync(*contracts)
        
        # Process option data
        data = []
        for ticker in tickers:
            contract = ticker.contract
            expiration = datetime.strptime(contract.lastTradeDateOrContractMonth, '%Y%m%d').date()
            dte = (expiration - today).days
            data.append({
                'Symbol': symbol,
                'StockPrice': stock_price,
                'Strike': contract.strike,
                'Expiration': expiration,
                'DTE': dte,
                'Bid': ticker.bid,
                'BidSize': ticker.bidSize,
                'Ask': ticker.ask,
                'AskSize': ticker.askSize,
                'Last': ticker.close,
                'Contract': contract
            })
        
        return pd.DataFrame(data) if data else None
        
    except Exception as e:
        print(f"Error processing {symbol}: {str(e)}")
        return None

def filter_options(df, min_premium=0.01, min_annualized_premium=0.1, min_safety_margin=0.05):
    """Apply PEA-OSS filtering criteria to options DataFrame."""
    if df is None or df.empty:
        return pd.DataFrame()
        
    df = df.copy()
    df['Premium'] = np.where(df['Bid'] == -1.0,
                            df['Last'] / df['Strike'],
                            df['Bid'] / df['Strike'])
    df['Annualized Premium'] = df['Premium'] * (365 / df['DTE'])
    df['Safety Margin in %'] = (df['StockPrice'] - df['Strike']) / df['StockPrice']
    
    filtered_df = df[
        (df['Premium'] > min_premium) & 
        (df['Annualized Premium'] > min_annualized_premium) & 
        (df['Safety Margin in %'] > min_safety_margin)
    ]
    
    return filtered_df.sort_values('Annualized Premium', ascending=False)

async def process_symbols(ib, symbols, min_dte=0, max_dte=60, strike_range_percent=0.25):
    """Process symbols sequentially to avoid overwhelming the connection."""
    all_options = []
    for symbol in symbols:
        try:
            df = await process_get_filtered_put_options(
                ib, symbol, min_dte, max_dte, strike_range_percent
            )
            if df is not None and not df.empty:
                all_options.append(df)
            await asyncio.sleep(1)  # Add delay between symbols
        except Exception as e:
            print(f"Error processing {symbol}: {str(e)}")
            continue
    return all_options

def pea_oss(ib, symbols, min_dte=0, max_dte=60, strike_range_percent=0.25,
            min_premium=0.01, min_annualized_premium=0.1, min_safety_margin=0.05):
    """
    Process PEA-OSS strategy for a list of symbols using the existing IB connection.
    
    Args:
        ib: IB connection instance
        symbols: List of symbols to process
        min_dte: Minimum days to expiration
        max_dte: Maximum days to expiration
        strike_range_percent: Range around current price to consider strikes (0.25 = ±25%)
        min_premium: Minimum premium required (as fraction of strike)
        min_annualized_premium: Minimum annualized premium required
        min_safety_margin: Minimum safety margin required (as fraction of stock price)
    
    Returns:
        DataFrame with filtered options data meeting PEA-OSS criteria
    """
    try:
        # Process symbols using the existing event loop
        all_options = ib.run(
            process_symbols(
                ib,
                symbols,
                min_dte=min_dte,
                max_dte=max_dte,
                strike_range_percent=strike_range_percent
            )
        )
        
        if not all_options:
            return pd.DataFrame()
        
        # Combine all results and apply filtering
        combined_df = pd.concat(all_options, ignore_index=True)
        return filter_options(
            combined_df,
            min_premium=min_premium,
            min_annualized_premium=min_annualized_premium,
            min_safety_margin=min_safety_margin
        )
        
    except Exception as e:
        print(f"Error in PEA-OSS processing: {str(e)}")
        return pd.DataFrame()
