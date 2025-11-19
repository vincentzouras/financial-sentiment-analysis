
#importing all necessary functions from each file
import pandas as pd

from src.clean_prices import clean_price_data
from src.clean_headlines import clean_news_data
from src.features_text import create_tfidf_features
from src.merge_datasets import merge_price_headlines

from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

def main():

    print("Welcome to the Financial Sentiment Analysis Tool!")
    print("-------------------------------------------------\n\n")

    # datasets = ["cnbc_headlines", "reuters_headlines", "guardian_headlines"]\
    datasets = ["cnbc_headlines"]
    companies = ['AAPL', 'MSFT', 'GOOGL']  # Apple, Microsoft, Alphabet

    # Clean price data and merge into single DataFrame
    price_frames = []
    for company in companies:
        prices_df = clean_price_data(company, '2020-01-01', '2023-01-01')
        price_frames.append(prices_df)

    all_prices = pd.concat(price_frames, ignore_index=True)


    # cleaning headlines data
    news_frames = []
    for news in datasets:
        news_df = clean_news_data(
            input_path=f"data/raw/{news}.csv",
            output_path=f"data/clean/{news}_clean.csv"
        )
        news_frames.append(news_df)

    news_frames = pd.concat(news_frames, ignore_index=True)

    # Merging headlines and prices
    print("Merging price and headline data...")
    merged_df = merge_price_headlines(all_prices, news_frames)
    print(f"Merged dataset shape: {merged_df.head()}")

    # create TF-IDF features with cleaned merged data
    X_text, tfidf_vectorizer = create_tfidf_features(
        merged_df,
        save_vectorizer_path="models/tfidf.pkl"
    )


if __name__ == '__main__':
    main()