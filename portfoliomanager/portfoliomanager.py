from ib_async import *
import pandas as pd
import numpy as np
from datetime import datetime, timezone
import pytz
import os
import sys

# Add the project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.get_sector import get_sector
from utils.get_index_composition import get_index_composition
import portfoliomanager_utils

class PortfolioManager:
    def __init__(self, ib_client=None, client_id=None, arctic=None):
        self.ib = self.connect_to_ib(client_id) if ib_client is None else ib_client
        self.arctic = arctic if arctic is not None else None
        
    def connect_to_ib(self, client_id):
        util.startLoop()
        self.ib = IB()
        clientid = client_id if client_id is not None else 0
        try:
            self.ib.connect('127.0.0.1', 7497, clientId=clientid)
            print(f'IB Connection established with clientId={clientid}')
        except ConnectionError:
            print('Failed to connect to IB API')
            self.ib = None
        return self.ib

    def get_latest_stock_prices(self, symbols, exchanges=None, currency=None):
        if isinstance(symbols, str):
            symbols = [symbols]
        
        self.ib.reqMarketDataType(1) if portfoliomanager_utils.is_market_open(self.ib) else self.ib.reqMarketDataType(2)

        # Prepare exchanges dictionary
        if exchanges is None:
            exchanges = {symbol: 'SMART' for symbol in symbols}
        
        # Prepare currencies dictionary
        if currency is None:
            currencies = {symbol: 'USD' for symbol in symbols}
        
        contracts = {}
        market_data = {}
        for symbol in symbols:
            exchange = exchanges.get(symbol, 'SMART')
            currency = currencies.get(symbol, 'USD')
            contracts[symbol] = Stock(symbol, exchange, currency)
            market_data[symbol] = self.ib.reqMktData(contracts[symbol], '', False, False)
        
        self.ib.sleep(2)
        
        prices = {}
        for ticker, data in market_data.items():
            # Extract last price, using close as fallback
            price = data.last if data.last is not None else data.close
            prices[ticker] = price

        return prices

    def get_portfolio_data(self):
        self.portfolio = pd.DataFrame(self.ib.portfolio())
        self.portfolio['symbol'] = self.portfolio['contract'].apply(lambda x: x.symbol)
        self.portfolio['asset_class'] = self.portfolio['contract'].apply(lambda x: type(x))
        return self.portfolio
    
    def get_short_put_portfolio(self):
        if not hasattr(self, 'portfolio'):
            self.get_portfolio_data()
        put_option_rows = [row for _, row in self.portfolio.iterrows() if isinstance(row['contract'], Option) and row['contract'].right == 'P' and np.sign(row['position']) == -1]
        df = pd.DataFrame(put_option_rows)
        symbols = df['symbol'].unique().tolist()

        # Add Sector and Market Cap information
        info_dict = get_sector(symbols)
        df['sector'] = df['symbol'].apply(lambda x: info_dict[x]['sector'])
        df['market_cap'] = df['symbol'].apply(lambda x: info_dict[x]['mcap'])

        # Add Underlying Price
        prices = self.get_latest_stock_prices(df['symbol'].unique().tolist())
        df['px_underlying'] = df['symbol'].apply(lambda x: prices[x])

        # Extract a custom option name from contract object
        df['strike'] = df['contract'].apply(lambda x: x.strike)
        df['expiry'] = df['contract'].apply(lambda x: x.lastTradeDateOrContractMonth)
        df['option'] = 'P' + df['strike'].astype(str) + ' ' + df['expiry']

        # Add Safety Margin & other risk informations
        df['safety_margin'] = (df['px_underlying'] - df['strike']) / df['px_underlying']
        df['cap_at_risk_lvl1'] = df['strike'] * 100
        df['cap_at_risk_lvl2'] = np.where(df['safety_margin'] < 0.05, df['strike'] * 100, 0)
        df['cap_at_risk_lvl3'] = np.where(df['safety_margin'] < 0, df['strike'] * 100, 0)

        df = df.copy()
        df = df[['symbol', 'option', 'position', 'averageCost', 'marketValue', 'unrealizedPNL', 'sector', 'px_underlying', 'safety_margin', 'market_cap', 'cap_at_risk_lvl1', 'cap_at_risk_lvl2', 'cap_at_risk_lvl3']]
        return df

    def recommend_sectors(self, index='SPY', risk_level=1):
        """
        Recommend sectors for trading based on comparison with index composition.
        
        Args:
            index: Index to compare against ('SPY' or 'QQQ')
            risk_level: Risk level for capital at risk calculation (1, 2, or 3)
                1: All positions
                2: Positions with safety margin < 5%
                3: Positions in the money
        
        Returns:
            DataFrame with sector recommendations sorted by most underweight
        """
        # Get index composition
        index_composition = get_index_composition(index=index)
        
        # Get current portfolio
        portfolio = self.get_short_put_portfolio()
        if portfolio.empty:
            return pd.DataFrame({'sector': list(index_composition.keys()),
                               'index_weight': [v/sum(index_composition.values())*100 for v in index_composition.values()],
                               'portfolio_weight': 0,
                               'deviation': [-v/sum(index_composition.values())*100 for v in index_composition.values()]
                              }).sort_values('deviation')
        
        # Calculate portfolio exposure by sector
        risk_col = f'cap_at_risk_lvl{risk_level}'
        portfolio_exposure = portfolio.groupby('sector')[risk_col].sum()
        total_exposure = portfolio_exposure.sum()
        
        # Calculate weights and deviations
        result = pd.DataFrame({
            'sector': list(index_composition.keys()),
            'index_weight': [v/sum(index_composition.values())*100 for v in index_composition.values()],
            'portfolio_weight': [portfolio_exposure.get(sector, 0)/total_exposure*100 if total_exposure else 0 
                               for sector in index_composition.keys()]
        })
        
        # Calculate deviations (negative means underweight)
        result['deviation'] = result['portfolio_weight'] - result['index_weight']
        
        # Sort by deviation (most underweight first)
        result = result.sort_values('deviation')
        
        # Add recommendations
        def get_recommendation(row):
            if abs(row['deviation']) < 2:
                return "Neutral (within ±2% of index weight)"
            elif row['deviation'] < 0:
                return f"Underweight by {abs(row['deviation']):.1f}% - Consider increasing exposure"
            else:
                return f"Overweight by {row['deviation']:.1f}% - Consider reducing exposure"
        
        result['recommendation'] = result.apply(get_recommendation, axis=1)
        
        return result

if __name__ == '__main__':
    portfolio_manager = PortfolioManager(client_id=10)
    recommendations = portfolio_manager.recommend_sectors()
    print("\nSector Recommendations:")
    print(recommendations.to_string(index=False))
