import requests
import pandas as pd
import sys
import os

# Add the project root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.get_earnings import get_earnings, get_future_earnings

def get_vol_data(df_earnings: pd.DataFrame = None) -> pd.DataFrame:
    """
    Get volatility data for symbols in earnings DataFrame and merge with it.
    
    Args:
        df_earnings: DataFrame from get_earnings(). If None, will call get_earnings()
        
    Returns:
        DataFrame with earnings and volatility data
    """
    if df_earnings is None:
        df_earnings = get_earnings()
    
    # Get symbols from earnings DataFrame
    symbols = df_earnings['symbol'].tolist()
    
    # Build the query to get the max date from the volatility_history table
    query_max_date = """
    SELECT MAX(`date`) AS max_date
    FROM `volatility_history`
    """
    encoded_query_max_date = requests.utils.quote(query_max_date)
    endpoint_max_date = f"https://www.dolthub.com/api/v1alpha1/post-no-preference/options/master?q={encoded_query_max_date}"
    response_max_date = requests.get(endpoint_max_date)
    response_max_date.raise_for_status()

    # Get the maximum date
    data_max_date = response_max_date.json()
    if data_max_date.get('query_execution_status') == 'Success' and data_max_date.get('rows'):
        max_date = data_max_date['rows'][0]['max_date']
        print("Looking up vol data for:", max_date)
    else:
        print(f"Query Error: {data_max_date.get('query_execution_message')}")
        return df_earnings

    # Build the query to get the vol data for the max date
    symbols_str = ', '.join(f"'{symbol}'" for symbol in symbols)
    query_volatility = f"""
    SELECT *
    FROM `volatility_history`
    WHERE `date` = '{max_date}'
    AND `act_symbol` IN ({symbols_str})
    ORDER BY `act_symbol` ASC;
    """
    
    encoded_query_volatility = requests.utils.quote(query_volatility)
    endpoint_volatility = f"https://www.dolthub.com/api/v1alpha1/post-no-preference/options/master?q={encoded_query_volatility}"
    response_volatility = requests.get(endpoint_volatility)
    response_volatility.raise_for_status()

    # Convert the response to a DataFrame
    data_volatility = response_volatility.json()
    if not data_volatility.get('rows'):
        print("No volatility data found.")
        return df_earnings

    # Create volatility DataFrame with only needed columns
    df_vol = pd.DataFrame(data_volatility['rows'])
    df_vol = df_vol[['act_symbol', 'hv_current', 'iv_current']].astype({'hv_current': 'float', 'iv_current': 'float'})
    df_vol['vol_premium'] = df_vol['iv_current'] / df_vol['hv_current']
    
    # Rename column to match earnings DataFrame
    df_vol = df_vol.rename(columns={'act_symbol': 'symbol'})
    
    # Merge with earnings DataFrame
    df_merged = pd.merge(df_earnings, df_vol, on='symbol', how='left')
    
    # Sort by volatility premium
    return df_merged.sort_values('vol_premium', ascending=False)


if __name__ == "__main__":
    # df =get_vol_data(get_future_earnings())
    # print(df)
    # df.to_csv("future_earnings.csv", index=0)
    df = get_vol_data()
    print(df)
    df.to_csv("data/vol_premium.csv", index=0)