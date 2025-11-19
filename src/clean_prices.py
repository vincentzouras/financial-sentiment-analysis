import yfinance as yf
import pandas as pd
import warnings

def clean_price_data(ticker, start_date, end_date):
    """
    Fetches and cleans historical price data for a given ticker symbol
    between specified start and end dates.

    Parameters:
    - ticker (str): The stock ticker symbol.
    - start_date (str): The start date in 'YYYY-MM-DD' format.
    - end_date (str): The end date in 'YYYY-MM-DD' format.

    Returns:
    - pd.DataFrame: Cleaned DataFrame containing historical price data.
    """
    warnings.simplefilter(action='ignore', category=FutureWarning)
    # Fetch historical price data
    data = yf.download(ticker, start=start_date, end=end_date)

    if isinstance(data.columns, pd.MultiIndex):
        # Join the two levels of the index (e.g., ('Close', 'AAPL') -> 'Close_AAPL')
        # OR simply select the first level if the data is only for one ticker
        # We will reset the columns to be simple, single names
        data.columns = data.columns.get_level_values(0)

    print(f"Data Header for {ticker}:\n", data.head())

    # Reset index to have 'Date' as a column
    data.reset_index(inplace=True)

    # Handle missing values by forward filling
    data.fillna(method='ffill', inplace=True)

    # Ensure correct data types
    data['Date'] = pd.to_datetime(data['Date'])
    numeric_cols = ['Open', 'High', 'Low', 'Close', 'Volume']
    for col in numeric_cols:
        data[col] = pd.to_numeric(data[col], errors='coerce')

    return data
