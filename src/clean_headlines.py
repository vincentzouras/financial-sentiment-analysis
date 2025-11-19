import re
import pandas as pd
from nltk.corpus import stopwords


# stop words
stop_words = set(stopwords.words("english"))


def clean_text(text):
    if pd.isna(text):
        return ""
    text = text.lower()
    text = re.sub(r"http\S+", "", text)              # remove URLs
    text = re.sub(r"[^a-zA-Z ]", " ", text)          # remove digits/punctuation
    text = " ".join([w for w in text.split()
                     if w not in stop_words])        # remove stopwords
    return text

def clean_news_data(input_path, output_path):
    df = pd.read_csv(input_path)

    # Combine fields for strongest NLP signal
    df["combined_text"] = (
        df["headline"].fillna("") + " " +
        df["summary"].fillna("") + " " +
        df["article"].fillna("")
    )

    df["clean_text"] = df["combined_text"].apply(clean_text)

    df.to_csv(output_path, index=False)
    return df

