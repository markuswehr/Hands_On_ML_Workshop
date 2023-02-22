"""
Page with an example for sentiment analysis.

author: Markus Wehr
date: 2023-02-02
"""

import pandas as pd
import streamlit as st

from src.sentiment.sentiment import load_sentiment_model, get_sentiment


# Clear cache
st.cache_resource.clear()

col1, col2, col3 = st.columns([3,3,2])
with col1:
    st.write("")
with col2:
    st.write("")
with col3:
    st.image("images/ing_logo.png")

st.header("Sentiment Analyse von Texten: Emotionen messbar machen")
st.write(
    """
    Sentiment Analyse ist eine Technik, die es ermöglicht,
    die emotionale Tendenz oder Meinung ("positiv", "negativ", "neutral") in einem Stück Text oder einer Stimme zu erkennen und zu klassifizieren.
    Dies kann auf der Ebene eines einzelnen Wortes oder einer ganzen Äußerung geschehen.
    
    So können zum Beispiel große Mengen an Kundenfeedback aus verschiedensten Kanälen (z.B. Emails, soziale Medien, App) quantifiziert
    und Zufriedenheit messbar gemacht werden.
    
    Algorithmen, die für Sentiment Analysen genutzt werden, lernen anhand von Beispieltexten, die zuvor von Menschen
    als "positive", "negative" oder "neutral" klassifiziert wurden.
    Das Modell nutzt dann diese Informationen, um die sentimentale Tendenz in neuen, ungesehenen Texten zu erkennen.
    """
)
st.subheader("**1. 💡 Ideenfindung und Problemdefinition**")
st.write(
    """
    **WIP**
    """
)
st.subheader("**2. 📥 Datenbeschaffung und -aufbereitung**")
st.write(
    """
    **WIP**
    """
)
st.subheader("**3. 👩‍💻 Entwicklung**")
st.write(
    """
    **WIP: Text über Textklassifizierung**
    """
)
st.subheader("**4. ✅ Implementierung**")
st.write(
    """
    **WIP**
    
    Füge einen Text ein und finde heraus, ob dieser negativ, positiv oder neutral assoziiert ist.
    """
)
input_txt = st.text_area("**Text, der analysiert werden soll:**", height=300)
sentiment_class, probability = None, [[[None, None], [None, None], [None, None]]]
submit = st.button("Sentiment Analyse durchführen")  
if submit:
    model = load_sentiment_model()
    sentiment_class, probability = get_sentiment(model=model, text=[input_txt])

sentiment_df = pd.DataFrame(data={
    "Sentiment Klasse": [sentiment_class],
    "Wahrscheinlichkeit Positiv": [probability[0][0][1]],
    "Wahrscheinlichkeit Negativ": [probability[0][1][1]],
    "Wahrscheinlichkeit Neutral": [probability[0][2][1]],
})
st.table(sentiment_df)
st.write(
    """
    Beachte, dass das Modell keine absoluten Vorhersagen trifft,
    sondern jeder Klasse eine Wahrscheinlichkeit zuteilt.
    Die Summe aller Wahrscheinlichkeiten der verschiedenen Klassen wiederum ergibt 100%.
    """
)


if __name__ == "__main__":
    pass
