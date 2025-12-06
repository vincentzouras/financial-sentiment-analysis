# financial-sentiment-analysis

- OUTPUT: y (binary target)
  - 1: positive sentiment, stock goes up the next day
  - 0: negative sentiment, stock goes down or neutral the next day

- INPUT: X (we have two kinds of features)
  - X1: (1-dimensional) text based features from news
    - we convert raw text to TF-IDF vectors
  - X2: (2-dimensional) numerical features from stock prices
    1. Daily volume
    1. Daily percent change
