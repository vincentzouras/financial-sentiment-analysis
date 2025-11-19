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

     # Make copies so we don't mutate originals
    price = price_data.copy()
    news = news_data.copy()

    # Ensure both Date columns are datetime and stripped to date level
    price["Date"] = pd.to_datetime(price["Date"]).dt.normalize()
    news["Date"] = pd.to_datetime(news["Date"]).dt.normalize()


    merged_data = pd.merge(news, price, on='Date', how='inner')
    return merged_data