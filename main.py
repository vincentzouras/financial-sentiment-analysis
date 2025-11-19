
#importing all necessary functions from each file
from src.clean_prices import clean_price_data
# from src.clean_headlines
# from src.model

def main():

    print("Welcome to the Financial Sentiment Analysis Tool!")
    print("-------------------------------------------------\n\n")

    # Companies we are focusing on
    companies = ['AAPL', 'MSFT', 'GOOGL']  # Apple, Microsoft, Alphabet
    # Clean price data
    for company in companies:
        clean_price_data(company, '2020-01-01', '2023-01-01')


if __name__ == '__main__':
    main()