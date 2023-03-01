"""
Page with an example for sentiment analysis.

author: Markus Wehr
date: 2023-02-02
"""

import pandas as pd
import streamlit as st

from src.sentiment.sentiment import load_sentiment_model, get_sentiment
from src.password.check_password import check_password


if check_password():

    # Clear cache
    #st.cache_resource.clear()
    #summarization_tokenizer = st.empty()
    #summarization_model = st.empty()
    #classification_model = st.empty()

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
        """
    )
    st.subheader("**1. 💡 Ideenfindung und Problemdefinition**")
    st.write(
        """
            <div style='text-align: justify;'>
                Sentimentanalysen können in verschiedenen Use Cases angewendet werden, 
                um Einblicke in die Meinungen, Stimmungen und Haltungen der Kunden zu gewinnen. 
                Hier sind einige konkrete Ideen für mögliche Use Cases:
            <br><br>
            <ol>
                <li>
                    <b>Kundenservice:</b><br>
                    Sentiment-Analysen können helfen, die Kundenzufriedenheit zu messen.
                    Banken können beispielsweise ihre Social-Media-Präsenz überwachen, um zu sehen, 
                    wie Kunden auf ihre Posts reagieren. Sie können auch Kundenbewertungen und Feedbacks 
                    von verschiedenen Plattformen analysieren, um herauszufinden, welche Probleme und 
                    Bedenken Kunden haben und welche Bereiche des Kundenservice verbessert werden müssen.
                </li>
                <li>
                    <b>Produktentwicklung:</b><br>
                    Banken können Sentiment-Analysen nutzen, um die Meinungen und Bedürfnisse ihrer Kunden
                    bezüglich bestehender Produkte zu verstehen und mögliche Verbesserungen oder neue Produkte zu identifizieren.
                    Dies kann durch die Analyse von Kundenfeedback, Social-Media-Kommentaren oder Umfragen erreicht werden.
                </li>
                <li>
                    <b>Risikomanagement:</b><br>
                    Sentiment-Analysen können verwendet werden, um potenzielle Risiken zu erkennen.
                    Beispielsweise können negative Kommentare über bestimmte Finanzprodukte auf Social-Media-Plattformen 
                    ein Hinweis auf Probleme mit diesen Produkten sein.
                </li>
                <li>
                    <b>Marktforschung:</b><br>
                    Sentiment-Analysen können auch helfen, die Marktstimmung und Trends zu verstehen, 
                    die für die Bank relevant sein könnten. Banken können beispielsweise analysieren, 
                    wie Kunden auf neue regulatorische Änderungen oder Trends im Zahlungsverkehr reagieren, 
                    um besser auf die Bedürfnisse ihrer Kunden und die Veränderungen im Markt reagieren zu können.
                </li>
            </ol>
            <br>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.image("images/slides_pros_sentiment_analysis.png")
    st.subheader("**2. 📥 Datenbeschaffung und -aufbereitung**")
    st.write(
        """
        <div style='text-align: justify;'>
        <b>Datenbeschaffung:</b><br>
            Zunächst müssen Daten gesammelt werden, die für die Analyse relevant sind.
            Einige Ideen für solche Daten und wo man sie findet sind:<br>
        <ul>
            <li>
                Direktes Kundenfeedback (aus Umfragen, IBBR oder Social Media)
            </li>
            <li>
                Kundenbewertungen (im Web, z.B. App-Store, Social Media, Trustpilot)
            </li>
        </ul>
            Zudem ist es wichtig, dass die Daten für die Sentiment-Analyse ausgewogen sind,
            d.h. dass es eine ähnliche Anzahl von positiven, negativen und neutralen Datensätzen gibt.
            Eine ungleichmäßige Verteilung der Daten kann dazu führen, dass das Modell in einer bestimmten Richtung verzerrt ist
            und schlechte Ergebnisse liefert.
        <br><br>
        <b>Datenaufbereitung:</b><br>
            Beim maschinellen Lernen ist es wichtig, dass die Trainingsdaten gelabelt sind, um das Modell zu trainieren. 
            Dies bedeutet, dass jeder Datensatz mit einem entsprechenden Sentiment-Label versehen werden muss
            (z.B. "positiv", "negativ" oder "neutral"). Auch wenn es automatische/halb-automatische Methoden gibt, die das Labeln
            erleichtern können (z.B. anhand von Schlüsselwörtern), ist hier meist noch einiger manueller Aufwand gefragt. 
            Wie der Prozess des Labelns für Sentiment Analysen aussehen kann, siehst Du unten. Selektiere das Label, welches Du
            für das jeweilige Feedback für am angemessensten hältst.
        <br><br>
        """,
        unsafe_allow_html=True,
    )
    candidate_labels=("positiv", "negativ", "neutral")
    st.text_area(
        label="1. Feedback",
        value=
        """
        Ich war sehr enttäuscht von der Servicequalität bei meiner letzten Banktransaktion.
        Der Kundenservice war unkooperativ und unfreundlich und ich musste lange warten,
        um mein Problem zu lösen. Ich denke darüber nach, meine Bankverbindung zu wechseln.
        """,
        height=125,
    )
    st.selectbox(label="Dein Label:", options=candidate_labels, key=1)
    st.text_area(
        label="2. Feedback",
        value=
        """
        Ich habe kürzlich eine Banküberweisung durchgeführt und alles ist reibungslos verlaufen.
        Ich hatte keine Probleme und der Prozess war schnell und einfach.
        Ich habe nichts Besonderes zu bemerken, aber auch keine Beschwerden.
        """,
        height=125,
    )
    st.selectbox(label="Dein Label:", options=candidate_labels, key=2)
    st.text_area(
        label="3. Feedback",
        value=
        """
        Ich wollte nur ein kurzes Feedback geben und mich bei Ihrer Bank bedanken.
        Der Kundenservice war sehr hilfreich bei der Lösung meines Problems und ich war
        angenehm überrascht von der Schnelligkeit und Effizienz der Transaktion. 
        Ich bin sehr zufrieden mit Ihrem Service und werde Ihre Bank meinen Freunden und Familienmitgliedern empfehlen.
        """,
        height=125,
    )
    st.selectbox(label="Dein Label:", options=candidate_labels, key=3)
    st.write(
        """
        <div style='text-align: justify;'>
            Beachte, wie im 2. Feedback die Wörter 'Probleme' und 'Beschwerden' vorkommen. 
            Ein einfacherer Ansatz, der Feedback anhand von Schlüsselwörtern analysiert, hättet dieses Feedback vermutlich als
            ein negatives einsortiert. Mit maschinellem Lernen jedoch, kann die Semantik einbezogen und feinere Unterscheidungen
            getroffen werden.
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
            Zudem hilft es gewisse vorbereitende Schritte zu treffen, bevor mit der Modellierung begonnen wird. 
            Solche Schritte sind z.B.:
        <ul>
            <li>
                Entfernen irrelevanter Feedbacks (z.B., von Doppelungen)
            </li>
            <li>
                Entfernen von Wörtern, die häufig vorkommen, aber für den kontext relativ irrelevant sind (z.B. der, die, das)
            </li>
            <li>
                Aufteilen der Daten in ein Training-Set (Daten, von denen das Modell lernt) und ein Test-Set
                (Daten, anhand welcher die Genauigkeit des Modells auf ungesehene Daten gemessen wird)
            </li>
        </ul>
        <br><br>
        """,
        unsafe_allow_html=True,
    )
    st.image("images/sentiment_wordcloud.png", caption="Beispiel einer Wortwolke")
    st.write(
        """
        <div style='text-align: justify;'>
        <br><br>
        <b>Das Model:</b><br>
            Machine Learning Modelle zur Textverarbeitung haben die Fähigkeit,
            Textinformationen in einer Art und Weise zu verarbeiten, die es ihnen ermöglicht, 
            das Kontextverständnis von Sätzen zu verbessern und komplexe Beziehungen zwischen Wörtern zu erkennen.
        <br><br>
            Das Modell wird mit einer großen Menge von Textdaten trainiert, um zu lernen, welche Wörter und Sätze 
            typischerweise mit positiven oder negativen Stimmungen in Verbindung stehen. Das Modell erzeugt dabei 
            sogenannte "Embeddings" für jedes Wort im Text (siehe unten für eine Visualisierung solcher Embeddings).
            Das sind Vektoren, die die Bedeutung des Wortes im Kontext des Textes darstellen.
        <br><br>
            Sobald das Modell trainiert ist, kann es verwendet werden, um das Sentiment von neuen Texten vorherzusagen. 
            Der Text wird in das Modell eingegeben, welches dann die Bedeutungen der Wörter im Text versteht und 
            eine Vorhersage darüber trifft, ob der Text eine positive, negative oder neutrale Stimmung ausdrückt.
        <br><br>
        """,
        unsafe_allow_html=True,
    )
    st.image("images/slides_embeddings.png", caption="Mithilfe von 'Embeddings' kann die Bedeutung von Wörtern quantifiziert werden")
    st.write(
        """
        <div style='text-align: justify;'>
        <b>Erfolgsmessung:</b><br>
            Die Genauigkeit des Modells wird üblicherweise durch die Confusion Matrix gemessen.
            Die Confusion Matrix stellt eine Tabelle dar, in der die Anzahl der korrekt und inkorrekt 
            klassifizierten Beispiele für jede Klasse aufgeführt ist. In einer Sentiment-Analyse sind 
            dies typischerweise die positiven, negativen und neutralen Klassen. Basierend auf der 
            Confusion Matrix können verschiedene Metriken berechnet werden, unter anderem die ROC-Kurve und
            die Area Under the Curve (siehe Punkt 3 unter "Home").
        <br><br>
            Zudem kann je nach Anwendungsfall auch die Geschwindigkeit des Modells eine Rolle spielen.
            Geht es z.B. darum Kundenfeedback live zu messen (z.B. im Call Center), ist die Geschwindigkeit,
            mit der eine Vorhersage produziert werden kann wichtig. Geht es um einen monatlichen Report, ist sie 
            vermutlich eher nachrangig. Die Geschwindigkeit wird üblicherweise durch die Inferenzzeit gemessen. 
            Die Inferenzzeit gibt an, wie lange das Modell benötigt, um Vorhersagen für neue Beispiele 
            zu treffen.
        <br><br>
        """,
        unsafe_allow_html=True,
    )
    st.subheader("**4. ✅ Implementierung**")
    st.write(
        """
        <div style='text-align: justify;'>
            Bei der Implementierung kommt es ganz auf den Use Case an. Geht es z.B. darum eine Sentiment Analyse
            in die tägliche Arbeit im Call Center einzubinden, sollte versucht werden die Vorhersagen in 
            bestehende Systeme einzubinden. Geht es aber um einen regelmässigen Report über die Zufriedenheit
            der Kunden, kann ein solches Dashboard auch unabhängig von bestehenden Systemen bereitgestellt werden.
        <br><br>
            Doch "probieren geht über studieren" - wir haben an diese Website ein Modell zur Sentiment Analyse angebunden.
            Füge einen Text in die Box unten ein und finde heraus, ob dieser negativ, positiv oder neutral assoziiert ist.
            So bekommst du eine Idee davon, wie der Ouput eines Sentiment Modells aussehen kann.
        <br><br>
        """,
        unsafe_allow_html=True,
    )
    input_txt = st.text_area("**Text, der analysiert werden soll:**", height=300)
    sentiment_class, probability = None, [[[None, None], [None, None], [None, None]]]
    submit = st.button("Sentiment Analyse durchführen")  
    if submit:
        sentiment_model = load_sentiment_model()
        sentiment_class, probability = get_sentiment(model=sentiment_model, text=[input_txt])

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
