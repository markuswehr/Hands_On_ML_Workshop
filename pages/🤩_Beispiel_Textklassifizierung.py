"""
Page with an example for text classification.

author: Markus Wehr
date: 2023-01-31
"""

import pandas as pd
import streamlit as st

from src.classification.zero_shot import load_zero_shot, get_classification
from src.password.check_password import check_password


if check_password():

    # Clear cache
    #st.cache_resource.clear()
    #summarization_tokenizer = st.empty()
    #summarization_model = st.empty()
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
    candidate_labels = st.sidebar.multiselect(
        label="Wähle für Dich relevante Kategorien (Default=alle)",
        options=(
            "Beschwerde",
            "Girokonto",
            "Baufinanzierung",
            "Privatkredit",
            "Online-Banking",
            "Depot"
        ),
        default=(
            "Beschwerde",
            "Girokonto",
            "Baufinanzierung",
            "Privatkredit",
            "Online-Banking",
            "Depot"
        ),
    )

    st.header("Schneller zuordnen mithilfe von Textklassifizierung")

    st.subheader("**1. 💡 Ideenfindung und Problemdefinition**")
    st.write(
        """
        <div style='text-align: justify;'>
            Die Textklassifizierung in einer Bank kann in verschiedenen Use Cases eingesetzt werden. 
            Einige mögliche Anwendungsfälle sind:<br><br>
            <ul>
                <li>
                    <b>Klassifizierung von Kundenanfragen:</b> Durch die Analyse von Kundenanfragen kann das Modell 
                    automatisch entscheiden, welcher Bereich der Bank für die Anfrage zuständig ist und die 
                    Anfrage entsprechend weiterleiten. So kann die Effizienz im Kundensupport gesteigert werden.
                </li>
                <li>
                    <b>Klassifizierung von Dokumenten:</b> Das Modell kann Dokumente, wie beispielsweise Verträge oder 
                    Kreditanträge, automatisch in verschiedene Kategorien einordnen, um eine schnellere 
                    Verarbeitung und Überprüfung zu ermöglichen.
                </li>
            </ul>
            <br>
            Mögliche Vorteile des Einsatzes von Machine Learning für Textklassifizerung sind:<br><br>
            <ul>
                <li>
                    Zeitersparnis
                </li>
                <li>    
                    Möglichkeit sich auf relevante Anfragen/Dokumente zu fokussieren
                </li>
            <br>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.subheader("**2. 📥 Datenbeschaffung und -aufbereitung**")
    st.write(
        """
        <div style='text-align: justify;'>
            <b>Datenbeschaffung:</b><br>
            Die Daten für Kundenanfragen können entweder aus dem Datawarehouse oder direkt aus Systemen (z.B. Emmie) kommen.
            Dokumente werden üblicherweise im Datawarehouse abgelegt. Je nach Art der Dokumente, muss auf verschiedene 
            Marts zugegriffen werden.
            <br><br>
            <b>Datenaufbereitung:</b><br>
            Damit das Machine Learning Modell lernen kann, die Emails in verschiedene Gruppen zu klassifizieren, benötigt es Beispiele.
            Dafür müssen einige Emails gelabelt werden. Wie das aussehen kann, siehst du unten. Lies Dir die Emails durch und entscheide,
            welches Label du der jeweiligen Email geben würdest (Achtung! Einer Email können mehrere Labels gegeben werden).
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.text_area(
        label="1. Email",
        value="""
        Sehr geehrte Damen und Herren,
        ich bin ein unzufriedener Kunde Ihrer Bank und möchte mich über einige Probleme beschweren, die ich in letzter Zeit erlebt habe.
        Zunächst möchte ich erwähnen, dass ich seit vielen Jahren Kunde Ihrer Bank bin und bisher immer zufrieden war. Allerdings hat sich das in letzter Zeit geändert.
        Ich habe Schwierigkeiten bei der Nutzung der Online-Banking-Plattform.
        Ich habe mehrere Male versucht, mit dem Kundenservice Kontakt aufzunehmen, aber es war jedes Mal eine Herausforderung, jemanden zu erreichen, der mir helfen kann.
        Die Wartezeiten sind unzumutbar lang und es fühlt sich so an, als ob ich keine Priorität für Ihr Unternehmen bin.
        Ich bin sehr enttäuscht von dieser Erfahrung und erwarte, dass sich die Dinge schnell ändern.
        Mit freundlichen Grüßen,
        Ihr Kunde""",
        height=175,
    )
    st.multiselect(label="Dein Label:", options=candidate_labels)
    st.text_area(
        label="2. Email",
        value="""
        Sehr geehrte Damen und Herren,
        ich bin ein langjähriger Kunde Ihrer Bank und bin an einer Verlängerung meiner Baufinanzierung interessiert.
        Könnten Sie mir bitte Informationen darüber zukommen lassen, wie ich meine bestehende Baufinanzierung verlängern kann?
        Ich bin besonders an den Anforderungen und den zu erwartenden Kosten interessiert.
        Ich danke Ihnen im Voraus für Ihre Hilfe. Ich freue mich darauf, von Ihnen zu hören.
        Mit freundlichen Grüßen,
        Ihr Kunde""",
        height=175,
    )
    st.multiselect(label="Dein Label: ", options=("Beschwerde", "Girokonto", "Baufinanzierung", "Privatkredit", "Online-Banking", "Depot"))
    st.text_area(
        label="3. Email",
        value="""
        Sehr geehrte Damen und Herren,
        ich bin ein Kunde Ihrer Bank und habe einige Fragen zu meinem Depot.
        Könnten Sie mir bitte Informationen darüber zukommen lassen, 
        wie ich den aktuellen Stand meines Depots einsehen und verwalten kann? 
        Außerdem würde ich gerne wissen, ob es Möglichkeiten gibt, meine Anlagestrategie anzupassen oder neue Anlageoptionen hinzuzufügen.
        Ich danke Ihnen im Voraus für Ihre Hilfe.
        Mit freundlichen Grüßen,
        [Dein Name]""",
        height=175,
    )
    st.multiselect(label="Dein Label:  ", options=("Beschwerde", "Girokonto", "Baufinanzierung", "Privatkredit", "Online-Banking", "Depot"))
    st.write("")
    st.write(
        """
        <div style='text-align: justify;'>
            <b>Sonderfall (gescannte) Dokumente:</b><br>
            Im Falle von Dokumenten und insbesondere gescannten Dokumenten ist oftmals noch ein weiterer Schritt von Nöten.
            Gerade gescannte Dokumente sind oftmals eine Bilddatei. Das bedeutet, der Text ist nicht einfach so für 
            Analysen oder Modellierungen verwendbar. Stattdessen muss zunächst eine Software eingesetzt werden, 
            mithilfe derer Text auf dem Dokument erkannt und dann in eine Textdatei umgewandelt wird. Wie so etwas 
            aussieht, siehst Du im unteren Beispiel. 
        <br><br>
        """,
        unsafe_allow_html=True,
    )
    st.image("images/slides_salary_slip_example.png", caption="Mithilfe von Erkennungssoftware kann Text teilweise von gescannten Dokumenten extrahiert werden")
        
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
            eine Vorhersage darüber trifft, in welche Kategorie ein gewisser Text einzusortieren ist.
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
            klassifizierten Beispiele für jede Klasse aufgeführt ist. Basierend auf der 
            Confusion Matrix können verschiedene Metriken berechnet werden, unter anderem die ROC-Kurve und
            die Area Under the Curve (siehe Punkt 3 unter "Home"). Außerdem kann mithilfe der ROC-Kurve und 
            des AUC die Performanz verschiedener Modelle und für verschiedene Klassen gemessen und verglichen werden,
            um am Ende das bestmögliche Modell auszuwählen.
        <br><br>
        """,
        unsafe_allow_html=True,
    )

    st.subheader("**4. ✅ Implementierung**")
    st.write(
        """
        <div style='text-align: justify;'>
            Die Einbindung des Textklassifikationsmodells und der Vorhersagen hängt ganz vom konkreten Use Case ab.
            Eine mögliche Variante wäre z.B. Daten aus dem Data Warehouse zu beziehen, diese an eine Virtual Machine 
            (ein Server, auf dem das Modell abgelegt wurde) zu schicken und die Vorhersagen von der Virtual Machine
            wieder an das Data Warehouse zu schicken. Von dort können die Vorhersagen dann von der Fachabteilung genutzt werden.
            Auf der Seite "Home" in Abschnitt 4. findet Du ein Schaubild, wie so etwas praktisch aussehen kann.
        <br><br>
            Sind alle Schritte abgeschlossen, kann das fertige Modell in Deinen Arbeitsprozess eingebunden und die 
            Emails oder Dokumente automatisch klassifiziert werden.
            Probiere es selbst aus: Kopiere einen Text Deiner Wahl in die Textbox und lass das Modell den Rest erledigen!
        <br><br>
        """,
        unsafe_allow_html=True,
    )
    input_txt = st.text_area("**Text, der klassifiziert werden soll:**", height=300)
    preds_df = pd.DataFrame({
        "Kategorien": [None],
        "Wahrscheinlichkeit pro Label": [None],
    })
    submit = st.button("Text klassifizieren")  
    if submit:
        classification_model = load_zero_shot()
        preds_df = get_classification(classifier=classification_model, text=input_txt, candidate_labels=candidate_labels)
    st.table(preds_df)
    st.write(
        """
        Beachte, dass das Modell keine absoluten Vorhersagen trifft, sondern jeder Klasse eine Wahrscheinlichkeit zuteilt.
        Die Summe aller Wahrscheinlichkeiten der verschiedenen Klassen wiederum ergibt 100%.
        """
    )

if __name__ == "__main__":
    pass
