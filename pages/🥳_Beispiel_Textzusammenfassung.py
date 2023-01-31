"""
Page with an example for text summarization.

author: Markus Wehr
date: 2023-01-31
"""

import streamlit as st

from src.summarization.summarize import summarize


# Sidebar parameters
st.sidebar.write("**Veränderbare Parameter:**")
summary_length = st.sidebar.slider(label="Wie lang soll die Zusammenfassung maximal werden?", min_value=25, max_value=150, value=60)


st.header("Text Summarization mit Machine Learning: Eine kurze Einführung")

st.subheader("*Probiere es aus und lasse die KI einen Text Deiner Wahl für Dich zusammenfassen*")
input_txt = st.text_area("**Text der zusammengefasst werden soll:**", height=350)
summary = None
submit = st.button("Zusammenfassung erstellen")  
if submit:
    summary = summarize(input=input_txt, model="Einmalumdiewelt/T5-Base_GNAD", summary_length=summary_length)
st.text_area(label="**Deine Zusammenfassung:**", value=summary, height=200)

st.subheader("*Und so funktioniert's hinter der Kulisse:*")
st.write(
    """
    Text Summarization ist der Prozess, bei dem ein längerer Text in eine kürzere und zusammengefasste Version umgewandelt wird. Ein Machine Learning Algorithmus kann hierbei helfen, den Text automatisch zusammenzufassen. Verschiedene Schritte müssen durchgeführt werden, um einen Machine Learning Algorithmus für Text Summarization zu trainieren und zu nutzen.

    **1. Datenbeschaffung:** 
    
    Besorge Dir eine große Menge an Texten, die Du als Trainingsdaten für Ihren Algorithmus nutzen möchtest. Diese Texte sollten bereits zusammengefasst sein, damit der Algorithmus lernen kann, wie er Texte zusammenfassen soll.
    
    **2. Datenaufbereitung:**
    
    Bereite Deine Trainingsdaten auf, indem Du sie in ein geeignetes Format bringst und überflüssige Informationen entfernst. Dies ist ein wichtiger Schritt, da schlecht vorbereitete Daten einen negativen Einfluss auf die Leistung des Algorithmus haben können.
    
    **3. Modellauswahl:**
    
    Wähle einen geeigneten Machine Learning Algorithmus aus, der für Text Summarization geeignet ist. Einige der gängigen Algorithmen sind unter anderem encoder-decoder-Netzwerke, transformers und reinforcement learning.
    
    **4. Modelltraining:**
    
    Trainiere Dein Modell, indem Du es mit den Trainingsdaten fütterst. Hierbei musst Du auch eine geeignete Loss-Funktion auswählen, die das Modell bewertet.
    
    **5. Modellbewertung:**
    
    Überprüfe die Leistung Deines Modells, indem Du es auf eine Testdatenmenge anwendest und dessen Leistung mit der der Trainingsdaten vergleichen.
    
    **6. Modelloptimierung:**
    
    Optimiere Dein Modell, indem Du die Hyperparameter anpasst oder das Modell erneut trainierst, bis Du mit seiner Leistung zufrieden sind.
    
    **7. Modelleinsatz:**
    
    Verwende Dein trainiertes Modell, um Texte zusammenzufassen, indem Du es mit einem neuen Text fütterst.
    
    Dies sind die grundlegenden Schritte, die Du durchführen musst, um einen Machine Learning Algorithmus für Text Summarization zu trainieren und zu nutzen. Beachte jedoch, dass es ein komplexer Prozess ist und dass Du möglicherweise mehrere Versuche benötigst.
    """
)


if __name__ == "__main__":
    pass
