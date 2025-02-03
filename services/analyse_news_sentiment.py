import spacy
from textblob import TextBlob

def analyse_news_sentiment(text):
    # Load spacy model
    nlp = spacy.load("en_core_web_sm")

    # Process the text
    doc = nlp(text)

    # Get sentiment using TextBlob
    blob = TextBlob(doc.text)
    # Get the sentiment polarity
    polarity = blob.sentiment.polarity

    # Define sentiment based on polarity score
    if polarity > 0.1:
        sentiment_label = "Positive"
    elif polarity < -0.1:
        sentiment_label = "Negative"
    else:
        sentiment_label = "Neutral"

    return sentiment_label