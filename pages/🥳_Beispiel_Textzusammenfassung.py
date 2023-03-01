"""
Page with an example for text summarization.

author: Markus Wehr
date: 2023-01-31
"""

from PIL import Image
import streamlit as st

from src.summarization.summarize import load_summarization_model, summarize
from src.password.check_password import check_password


if check_password():

    # Clear cache
    #st.cache_resource.clear()
    #classification_model = st.empty()
    #sentiment_model = st.empty()

    col1, col2, col3 = st.columns([3,3,2])
    with col1:
        st.write("")
    with col2:
        st.write("")
    with col3:
        st.image("images/ing_logo.png")

    # Sidebar parameters
    st.sidebar.write("**Veränderbare Parameter:**")
    summary_length = st.sidebar.slider(label="Wie lang soll die Zusammenfassung maximal werden?*", min_value=25, max_value=150, value=60)
    st.sidebar.write(
        """
        *Je länger die Antwort, desto länger wird die Bearbeitung dauern. 
        Wir haben mit 60 Wörtern in diesem Fall die besten Erfahrugen gemacht.
        """
    )
    #model_string = st.sidebar.selectbox(
    #    label="Welches Modell möchtest Du nutzen?",
    #    options=(
    #        "Einmalumdiewelt/T5-Base_GNAD",
    #        "Einmalumdiewelt/PegasusXSUM_GNAD",
    #        "Einmalumdiewelt/BART_large_CNN_GNAD",
    #        "Einmalumdiewelt/MT5_small_sum-de_GNAD",
    #        "Einmalumdiewelt/DistilBART_CNN_GNAD",
    #    )
    #)

    st.header("Schneller verstehen, worum es geht - mit Text Summarization")
    st.write(
        """
        Text Summarization Modelle basierend auf Machine Learning sind in der Lage, 
        Texte automatisch zu lesen und wichtige Informationen aus diesen Texten 
        herauszufiltern und zu extrahieren.
        """
    )

    st.subheader("**1. 💡 Ideenfindung und Problemdefinition**")
    st.write(
        """
        <div style='text-align: justify;'>
            Text Summarization kann auf vielfältige Weise genutzt werden. Ein konkretes Beispiel wäre die
            Zusammenfassung von Kundenanfragen, die die ING per Email oder über andere Kanäle erreichen.
            Ein Text Summarization-Modell kann diese Anfragen automatisch lesen und eine Zusammenfassung 
            der wichtigsten Informationen extrahieren. Dies kann dabei helfen, 
            schneller auf die Anfragen zu reagieren und effizienter zu arbeiten.
        <br><br>
        """,
        unsafe_allow_html=True,
    )
    st.subheader("**2. 📥 Datenbeschaffung und -aufbereitung**")
    st.write(
        """
        <div style='text-align: justify;'>
            <b>Datenbeschaffung:</b><br>
            Die Daten für Kundenanfragen können entweder aus dem Datawarehouse oder direkt aus Systemen (z.B. Emmie) kommen,
            je nachdem welcher Use Case verfolgt wird.
        <br><br>
            <b>Datenaufbereitung:</b><br>
            Um ein solches Modell zu trainieren, werden große Mengen an Texten und ihren Zusammenfassungen benötigt. 
            Diese Texte müssen in einer bestimmten Form vorbereitet werden, um vom Modell verarbeitet werden zu können. 
            Die Texte sollten in Sätze oder Absätze aufgeteilt und markiert werden, um dem Modell zu zeigen, wo ein 
            Satz oder Absatz beginnt und endet.
        <br><br>
            Außerdem müssen die Texte bereinigt werden, um unerwünschte Informationen wie Sonderzeichen, 
            URLs oder HTML-Tags zu entfernen. Die Zusammenfassungen sollten ebenfalls bereinigt werden, 
            um sicherzustellen, dass sie nur die wichtigsten Informationen enthalten.
        </div>
        <br><br>
        """,
        unsafe_allow_html=True,
    )

    st.subheader("**3. 👩‍💻 Entwicklung**")
    st.write(
        """
        <div style='text-align: justify;'>
            In diesem Abschnitt gehen wir auf vier Bereiche ein: den Tech Stack,
            die Erkundung und Reinigung der Daten, das Model und die Erfolgsmessung des Models.
        <br><br>
        <b>Tech Stack:</b><br>
            Für die Entwicklung eines solchen Modells setzen wir typischerweise verschiendene Tools ein.
            Unter anderem, Python als Programmiersprache, in welcher wir das Modell entwickeln, trainieren, testen usw.
            SQL, um Daten aus der Datenbank zu extrahieren. 
            Eine interne Machine Learning Plattform (z.B., DAP, INGs interne Plattform), eine Umgebung die große
            Rechenleistung sowie Datensicherheit bietet.
        <br><br>
        <b>Daten erkunden und verstehen:</b><br>
            Um Textdaten besser zu verstehen, bietet es sich an die Länge der Texte zu untersuchen, sowie
            Wörter die häufig auftauchen. Eine Art der Visualisierung kann z.B. ein Wortwolke sein, die
            häufig vorkommende Wörter besonder hervorhebt und so einen schnellen Überblick über dominierende Themen liefert
            (siehe unten für ein Beispiel).
        <br><br>
         """,
        unsafe_allow_html=True,
    )
    st.image("images/sentiment_wordcloud.png", caption="Beispiel einer Wortwolke")
    st.write(
        """
        <div style='text-align: justify;'>
        <b>Das Model:</b><br>
            Ein Machine Learning Modell für Text Summarization verwendet in der Regel eine Variante 
            des Sequence-to-Sequence (Seq2Seq) Modells. Sequence-to-Sequence Modelle sind eine Art 
            von künstlicher Intelligenz, die darauf spezialisiert sind, einen Text oder eine Sequenz 
            von Wörtern in eine andere Sequenz zu übersetzen oder eine Zusammenfassung der ursprünglichen 
            Sequenz zu generieren.
        <br><br>    
            Dieses Modell besteht aus zwei Hauptkomponenten: einem Encoder und einem Decoder. Der Encoder 
            ist wie ein Leser, der den ursprünglichen Text liest und versucht, alle wichtigen Informationen
            zu verstehen. Der Encoder zerlegt den Text in kleinere Teile, z.B. in einzelne Wörter oder Sätze 
            und kodiert diese Informationen in eine Art von Zahlencode, den das Modell besser verstehen kann. 
            Der Encoder speichert diesen Zahlencode in seinem Gedächtnis ab.
        <br><br>
            Der Decoder ist wie ein Schriftsteller, der den verschlüsselten Text im Gedächtnis des Encoders 
            liest und eine Zusammenfassung oder Übersetzung schreibt. Der Decoder versteht den kodierten Text 
            im Gedächtnis des Encoders und beginnt, eine Zusammenfassung oder Übersetzung zu schreiben. 
            Der Decoder kann die Informationen aus dem Gedächtnis des Encoders verwenden, um zu entscheiden, 
            was am besten in die Zusammenfassung oder Übersetzung passt.
        <br><br>
        """,
        unsafe_allow_html=True,
    )
    st.image("images/encoder_decoder_example.png", caption="Konzept eines Decoders und Encoders")   
    st.write(
        """
        <div style='text-align: justify;'>
        <b>Erfolgsmessung:</b><br>
            Um die Performance eines solchen Modells zu messen, 
            werden üblicherweise Metriken wie ROUGE (Recall-Oriented Understudy for Gisting Evaluation) verwendet. 
            Diese Metriken vergleichen die generierte Zusammenfassung mit der Referenz-Zusammenfassung und bewerten 
            die Qualität der Zusammenfassung anhand der Ähnlichkeit zwischen den beiden.
        <br><br>
        """,
        unsafe_allow_html=True,
    )

    st.subheader("**4. ✅ Implementierung**")
    st.write(
        """
        <div style='text-align: justify;'>
            Die Implementierung ist sehr individuell und hängt vom jeweiligen Use Case ab.
            Denkbar wäre z.B., Emails aus einem System per API and eine virtuelle Maschine zu senden,
            auf welcher das Modell dann die Zusammenfassung erstellt. Diese kann dan per API wieder
            bereitgestellt werden.
        <br><br>
            Aber mache dir am besten selbst ein Bild unf probiere es aus. Lasse die KI einen Text Deiner Wahl 
            für Dich zusammenfassen, indem du diesen in die Box unten kopierst.
        """,
        unsafe_allow_html=True,
    )
    input_txt = st.text_area("**Text, der zusammengefasst werden soll:**", height=300)
    summary = None
    submit = st.button("Zusammenfassung erstellen")  
    if submit:
        summarization_tokenizer, summarization_model = load_summarization_model(model="Einmalumdiewelt/T5-Base_GNAD")
        summary = summarize(model=summarization_model, tokenizer=summarization_tokenizer, input=input_txt, summary_length=summary_length)
    st.text_area(label="**Deine Zusammenfassung:**", value=summary, height=200)


if __name__ == "__main__":
    pass
