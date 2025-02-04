import traceback
import spacy
from textblob import TextBlob

def analyse_sentiment(text):
    try: 
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(text)
        blob = TextBlob(doc.text)
        polarity = blob.sentiment.polarity

        if polarity > 0.1:
            sentiment_label = "Positive"
        elif polarity < -0.1:
            sentiment_label = "Negative"
        else:
            sentiment_label = "Neutral"

        return sentiment_label
    except Exception as e:
        print(str(e))
        print(traceback.format_exc())
        return {"error": "Something went wrong!", "status_code": 500}