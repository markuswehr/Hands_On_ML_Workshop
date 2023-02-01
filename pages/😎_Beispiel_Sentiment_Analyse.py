"""
Page with an example for sentiment analysis.

author: Markus Wehr
date: 2023-02-02
"""

import pandas as pd
import streamlit as st

from src.sentiment.sentiment import get_sentiment


st.header("Sentiment Analyse von Texten: Emotionen messbar machen")

st.subheader("*Kann man Emotionen messen? Mit diesem Modell kann man es zumindest versuchen.*")
st.write("Füge einen Text ein und finde heraus, ob dieser negativ, positiv oder neutral assoziiert ist.")

input_txt = st.text_area("**Text, der analysiert werden soll:**", height=300)
sentiment_class, probability = None, [[[None, None], [None, None], [None, None]]]
submit = st.button("Sentiment Analyse durchführen")  
if submit:
    sentiment_class, probability = get_sentiment(text=[input_txt])

sentiment_df = pd.DataFrame(data={
    "Sentiment Klasse": [sentiment_class],
    "Wahrscheinlichkeit Positiv": [probability[0][0][1]],
    "Wahrscheinlichkeit Negativ": [probability[0][1][1]],
    "Wahrscheinlichkeit Neutral": [probability[0][2][1]],
})
st.table(sentiment_df)


if __name__ == "__main__":
    pass
