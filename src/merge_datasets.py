import pandas as pd

def merge_price_headlines(price_data, news_data):
    """
    Merges cleaned price data with cleaned news headline data on the date.

    Parameters:
    price_data (pd.DataFrame): Cleaned price data with 'Date' column.
    news_data (pd.DataFrame): Cleaned news headline data with 'Date' column.

    Returns:
    pd.DataFrame: Merged DataFrame containing both price and headline data.
    """
    merged_data = pd.merge(news_data, price_data, on='Date', how='inner')
    return merged_data