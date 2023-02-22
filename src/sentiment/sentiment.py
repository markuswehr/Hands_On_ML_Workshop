"""
Define function for loading pre-trained transformer.

author: Markus Wehr
date: 2023-02-01
"""

from typing import List
from germansentiment import SentimentModel
import streamlit as st


@st.cache_resource(ttl=180, max_entries=2)
def load_sentiment_model() -> SentimentModel:
    """
    Load and cache sentiment model.

    Output:
        model -- Sentiment model for re-use
    """
    model = SentimentModel()

    return model

def get_sentiment(model: SentimentModel, text: str) -> List:
    """
    Function to predict sentiment and probability score for that sentiment for a given text.

    input:
        model -- Pre-loaded sentiment model
        text -- Input text
    output:
        sentiment_class -- Positive, Negative, or Neutral class
        probability -- Probability score for each of the three classes
    """
    sentiment_class, probability = model.predict_sentiment(text, output_probabilities = True)
    
    return sentiment_class, probability


if __name__ == "__main__":
    pass
