"""
Streamlit app's landing page.

author: Markus Wehr
date: 2023-01-31
"""

import streamlit as st


st.header("Willkommen zum Machine Learning Workshop!")
st.write(
    """
    In diesem Workshop möchten wir die typischerweise notwendigen Schritte zur Umsetzung eines Machine Learning Projektes für Dich etwas greifbarer machen.
    Dazu findest Du unten eine kurze Zusammenfassung der jeweiligen Schritte.
    Außerdem zeigen wir Dir anhand von interaktiven Beispielen, wie das ganze praktisch aussieht und wie KI Deinen Alltag erleichtern kann.
    """
)

st.subheader(
    """
    Welche Schritte sind notwendig, damit Du Machine Learning nutzen kannst?

    Der Prozess von der Ideenfindung bis zum Endprodukt ist mannigfaltig (siehe Schaubild), kann jedoch grob in vier Schritte unterteilt werden:
    1. 💡 Ideenfindung und Problemdefinition ("Ideate")
    2. 📥 Datenbeschaffung und -aufbereitung ("Experiment")
    3. 👩‍💻 Entwicklung ("Model Improvement Loop")
    4. ✅ Implementierung ("Industrialize")

    """
)
st.image("images/analytics_snail.png", caption="Der 'ING Use Case' Ansatz")
st.write(
    """
    In den Beispielen (siehe linke Seite), findest Du diese vier Schritte bezogen auf das jeweilige Beispiel wieder.
    Liese auf dieser Seite weiter, für eine kurze Übersicht dazu, was die einzelnen Schritte beinhalten.
    """
)

st.subheader("**1. 💡 Ideenfindung und Problemdefinition**")
st.write(
    """
    **Welche Fragen kann Analytics/ML beantworten?**

    Im Rahmen der Ideenfindung sollte man sich zunächst bewusst machen, dass vier grundsätzliche Fragen mithilfe von Analytics beantwortet werden können:
    - ***Was*** ist passiert? (deskriptive Analysen; z.B., wie viele Kreditanträge hatten wir in 2022?)
    - ***Warum*** ist etwas passiert? (diagnostische Analysen; z.B., welche Faktoren haben dazu geführt, dass wir mehr Kreditanträge hatten als im Vorjahr?)
    - ***Was*** wird ***zukünftig*** passieren? (prädiktive Analysen; z.B., wie viele Kreditanträge können wir in 2023 erwarten?)
    - ***Wie*** können wir dafür sorgen, dass ***etwas Bestimmtes*** in ***Zukunft*** passiert? (präskriptive Analysen; z.B., welche Kunden sollten wir bevorzugt kontaktieren, um in 2023 mehr Kreditabschlüsse zu erzielen?)

    **Wann ergibt es Sinn über Machine Learning als Lösung nachzudenken?**

    Für folgende Probleme bietet sich Machine Learning als Lösung an:
    - Eine Aufgabe kann von Dir recht einfach ausgeführt werden, kommt aber in großen Volumina vor
    - Wenn es schwer fällt, klare wenn/dann Regeln für eine Aufgabe festzulegen
    - Aufgaben, für die viele Beispiele in Form von Daten (z.B., Emails, Dokumente, Datentabellen) vorliegen
    
    Die unterstützung durch Machine Learning bei solchen Aufgaben führt idealerweise dazu, dass
    neue ***Erkenntnisse*** generiert werden, wir alle unsere ***Aufgaben schneller und besser erledigen*** können und
    unsere ***Produkte langfristig noch innovativer werden***.

    **Ich habe eine Idee - was nun?**

    Komme mit Ideen immer gerne auf den Tribe Analytics zu. Ob ein Projekt dann letztlich umgesetzt wird, hängt von verschiedenen Faktoren ab.
    Zum Beispiel:
    - Wie groß wären die Vorteile eines Machine Learning Modells (z.B. Zeitersparnis, Risikoreduktion, ...)
    - Wie Komplex wäre der Prozess/die Lösung (einfach geht vor komplex)
    - Sind ausreichend Daten vorhanden (z.B. Datenbanken, Dokumenten, Emails)
    """
)

st.subheader("**2. 📥 Datenbeschaffung und -aufbereitung**")
st.write(
    """
    **Welche und wie viele Daten benötige ich?**

    Daten sind überall - welche Daten kommen aber in Frage für einen potenziellen Use Case?
    Zunächst natürlich alle quantitativen und qualitativen Daten, die Informationen über das zu lösende Problem enthalten.
    Daten mit denen wir erfahrungsgemäß viel zu tun haben in der ING, sind etwa Tabellen im
    Datawarehouse, Dokumente (z.B., gescannte PDFs) oder Emails.

    Grundsätzlich ist es besser möglichst viele Daten zur Verfügung zu haben, allerdings ist
    eine Grenze schwer zu definieren und problemabhängig. Komme auf uns zu und wir evaluieren dies gerne mit Dir gemeinsam.

    **Wie müssen die Daten aufbereitet werden?**

    Insbesondere, wenn etwas Bestimmtes vorhergesagt werden soll (sog. "supervised learning"), werden gelabelte Daten benötigt.
    Das bedeutet, parallel zu dem, was in das Machine Learning Modell hineinfliesst und basierend worauf Vorhersagen getroffen werden, 
    benötigt das Modell "korrekte" Lösungen für einen Teil der Daten. Diese korrekten Lösungen vergleicht das Modell mit seinen Vorhersagen
    und lernt aus seinen Fehlern, um schlussendlich auch für Daten, für die wir die Lösung nicht kennen, möglichst genaue Vorhersagen zu treffen.

    Meist liegen diese Labels für die Daten jedoch nicht vor und müssen für einen Teil der Daten manuell angelegt werden.
    Wie das aussehen kann, siehst du hier. Angenommen, wir wollten ein Machine Learning Modell entwickeln, das automatisch
    Spam Emails von normalen Emails unterscheiden kann. Damit das Modell den Unterschied lernen kann, müssen wir zunächst selbst für
    eine Hand voll Emails diese Unterscheidung treffen und die jeweilige Email als "Spam" oder "kein Spam" labeln. Anhand dieser
    Labels und der Email-Texte wird das Modell später lernen diese Unterscheidung zu treffen. 

    Lies Dir die unten stehenden Emails aus und entscheide selbst, ob es sich um Spam handelt oder nicht. Wähle Deine Entscheidung
    jeweils in der Selectbox aus.
    """
)
st.text_area(
    label="1. Email",
    value="""
    Betreff: Verbessern Sie Ihre Kreditwürdigkeit jetzt!
    Sehr geehrter Empfänger,
    Sie können jetzt Ihre Kreditwürdigkeit verbessern und einen besseren Kredit bekommen!
    Klicken Sie auf den folgenden Link, um mehr zu erfahren: [Link].
    Mit freundlichen Grüßen,
    [Name des Absenders]""",
    height=175,
)
st.selectbox(label="Dein Label:", options=["Spam", "kein Spam"])
st.text_area(
    label="2. Email",
    value="""
    Betreff: Einladung zur wöchentlichen Teambesprechung
    Sehr geehrte Kollegen,
    ich lade Euch alle herzlich zu unserer wöchentlichen Teambesprechung ein.
    Die Besprechung findet am Freitag um 10 Uhr im Konferenzraum statt.
    Wir werden die aktuellen Projektfortschritte und Pläne für die kommende Woche besprechen.
    Bitte bereitet alle relevanten Unterlagen vor.
    Mit freundlichen Grüßen,
    [Name des Absenders]""",
    height=175,
)
st.selectbox(label="Dein Label: ", options=["Spam", "kein Spam"])
st.text_area(
    label="3. Email",
    value="""
    Betreff: Gewinnen Sie eine Million Dollar!
    Sehr geehrter Empfänger,
    Sie haben gerade die Chance gewonnen,
    eine Million Dollar zu gewinnen! Klicken Sie auf den folgenden Link,
    um Ihren Preis zu beanspruchen: [Link].
    Viel Glück!
    Mit freundlichen Grüßen,
    [Name des Absenders]""",
    height=175,
)
st.selectbox(label="Dein Label:  ", options=["Spam", "kein Spam"])

st.subheader("**3. 👩‍💻 Entwicklung**")
st.write(
    """
    ???
    """
)

st.subheader("**4. ✅ Implementierung**")
st.write(
    """
    ???
    """
)

# Run the main function
if __name__ == '__main__':
    pass
