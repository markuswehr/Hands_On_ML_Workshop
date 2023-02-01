"""
Define function for loading pre-trained transformer.

author: Markus Wehr
date: 2023-02-01
"""

from typing import List, Tuple
from germansentiment import SentimentModel


def get_sentiment(text: str) -> List:
    """
    Function to predict sentiment and probability score for that sentiment for a given text.

    input:
        text -- Input text
    output:
        sentiment_class -- Positive, Negative, or Neutral class
        probability -- Probability score for each of the three classes
    """
    model = SentimentModel()
    sentiment_class, probability = model.predict_sentiment(text, output_probabilities = True)
    
    return sentiment_class, probability


if __name__ == "__main__":
    pass
