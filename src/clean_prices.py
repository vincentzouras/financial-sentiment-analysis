import yfinace as yf
import pandas as pd


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
    # Fetch historical price data
    data = yf.download(ticker, start=start_date, end=end_date)

    # Reset index to have 'Date' as a column
    data.reset_index(inplace=True)

    # Handle missing values by forward filling
    data.fillna(method='ffill', inplace=True)

    # Ensure correct data types
    data['Date'] = pd.to_datetime(data['Date'])
    numeric_cols = ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
    for col in numeric_cols:
        data[col] = pd.to_numeric(data[col], errors='coerce')

    return data