"""
Page with an example for text classification.

author: Markus Wehr
date: 2023-01-31
"""

import pandas as pd
import streamlit as st

from src.classification.zero_shot import get_classification


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
        <b>Möglicher Use Case:</b> Automatische Klassifizierung von Kundenemails in jeweilige Kategorien,
        sodass diese sofort dem/der relevanten Mitarbeiter/-in weitergeleitet werden können.
        <br><br>
        <b>Vorteile:</b> Zeitersparnis; Fokussierung auf für Mitarbeiter relevanten Emails
        <br><br>
    </div>
    """,
    unsafe_allow_html=True,
)
st.subheader("**2. 📥 Datenbeschaffung und -aufbereitung**")
st.write(
    """
    <div style='text-align: justify;'>
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

st.subheader("**3. 👩‍💻 Entwicklung**")
st.write(
    """
    **WIP: Text über Textklassifizierung**
    """
)
st.subheader("**4. ✅ Implementierung**")
st.write(
    """
    Nun kann das fertige Modell in Deinen Arbeitsprozess eingebunden und die Emails automatisch klassifiziert werden.
    Probiere es selbst aus: Kopiere einen Text Deiner Wahl in die Textbox und lass das Modell den Rest erledigen!
    """
)
input_txt = st.text_area("**Text, der klassifiziert werden soll:**", height=300)
preds_df = pd.DataFrame({
    "Kategorien": [None],
    "Wahrscheinlichkeit pro Label": [None],
})
submit = st.button("Text klassifizieren")  
if submit:
    preds_df = get_classification(text=input_txt, candidate_labels=candidate_labels)
st.table(preds_df)
st.write(
    """
    Beachte, dass das Modell keine absoluten Vorhersagen trifft, sondern jeder Klasse eine Wahrscheinlichkeit zuteilt.
    Die Summe aller Wahrscheinlichkeiten der verschiedenen Klassen wiederum ergibt 100%.
    """
)

if __name__ == "__main__":
    pass
