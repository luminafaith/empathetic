
import os.path
import sys

import nltk 
nltk.download('vader_lexicon')
from nltk.sentiment import SentimentIntensityAnalyzer


def vader(texts):
    sia = SentimentIntensityAnalyzer()
    results = []
    for text in texts:
        scores = sia.polarity_scores(text)
        compound_score = scores['compound']
        if compound_score > 0.05:
            sentiment = 'positive'
        elif compound_score < -0.05:
            sentiment = 'negative'
        else:
            sentiment = 'neutral'
        results.append(sentiment)
    return results

