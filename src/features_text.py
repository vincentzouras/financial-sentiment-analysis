from sklearn.feature_extraction.text import TfidfVectorizer
import pickle

def create_tfidf_features(df, save_vectorizer_path="models/tfidf.pkl"):
    tfidf = TfidfVectorizer(
        max_features=5000,        # good size for NB
        ngram_range=(1,2),        # unigrams + bigrams improve accuracy
        stop_words='english'
    )

    X_text = tfidf.fit_transform(df["clean_text"])

    # save the TF-IDF vectorizer for future inference
    with open(save_vectorizer_path, "wb") as f:
        pickle.dump(tfidf, f)

    return X_text, tfidf
