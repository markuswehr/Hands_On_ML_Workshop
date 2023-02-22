"""
Page with an example for text summarization.

author: Markus Wehr
date: 2023-01-31
"""

from PIL import Image
import streamlit as st

from src.summarization.summarize import load_summarization_model, summarize


# Clear cache
#st.cache_resource.clear()
classification_model = st.empty()
sentiment_model = st.empty()

col1, col2, col3 = st.columns([3,3,2])
with col1:
    st.write("")
with col2:
    st.write("")
with col3:
    st.image("images/ing_logo.png")

# Sidebar parameters
st.sidebar.write("**Veränderbare Parameter:**")
summary_length = st.sidebar.slider(label="Wie lang soll die Zusammenfassung maximal werden?", min_value=25, max_value=150, value=60)
model_string = st.sidebar.selectbox(
    label="Welches Modell möchtest Du nutzen?",
    options=(
        "Einmalumdiewelt/T5-Base_GNAD",
        "Einmalumdiewelt/PegasusXSUM_GNAD",
        "Einmalumdiewelt/BART_large_CNN_GNAD",
        "Einmalumdiewelt/MT5_small_sum-de_GNAD",
        "Einmalumdiewelt/DistilBART_CNN_GNAD",
    )
)

st.header("Schneller verstehen, worum es geht - mit Text Summarization")

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
    
    Probiere es aus und lasse die KI einen Text Deiner Wahl für Dich zusammenfassen.
    """
)
input_txt = st.text_area("**Text, der zusammengefasst werden soll:**", height=300)
summary = None
submit = st.button("Zusammenfassung erstellen")  
if submit:
    summarization_tokenizer, summarization_model = load_summarization_model(model=model_string)
    summary = summarize(model=summarization_model, tokenizer=summarization_tokenizer, input=input_txt, summary_length=summary_length)
st.text_area(label="**Deine Zusammenfassung:**", value=summary, height=200)


if __name__ == "__main__":
    pass
