# financial-sentiment-analysis

- OUTPUT (y): binary target
  - 1: stock goes up the next day
  - 0: stock goes down or neutral the next day

- INPUT (X): two types of features
  - X1: vector of text-based features (high-dimensional)
    - we convert raw text to TF-IDF vectors
    - each word/token becomes a number in the vector
    - so we have thousands of features
  - X2: vector of numerical stock features (2-dimensional)
    1. Daily volume
    1. Daily percent change
