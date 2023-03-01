"""
Streamlit app's landing page.

author: Markus Wehr
date: 2023-01-31
"""

import streamlit as st

from src.password.check_password import check_password


if check_password():
    col1, col2, col3 = st.columns([3,3,2])
    with col1:
        st.write("")
    with col2:
        st.write("")
    with col3:
        st.image("images/ing_logo.png")

    st.header("Willkommen zum Machine Learning Workshop!")
    st.markdown(
        """
        <div style='text-align: justify;'>
            In diesem Workshop möchten wir die typischerweise notwendigen Schritte zur Umsetzung eines Machine Learning Projektes für Dich etwas greifbarer machen.
            Dazu findest Du unten eine kurze Zusammenfassung der jeweiligen Schritte.
            Außerdem zeigen wir Dir anhand von interaktiven Beispielen, wie das ganze praktisch aussieht und wie KI Deinen Alltag erleichtern kann.
            <br><br>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.subheader(
        """
        Welche Schritte sind notwendig, damit Du Machine Learning nutzen kannst?
        """
    )
    st.markdown(
        """
        <div style='text-align: justify;'>
            Der Prozess von der Ideenfindung bis zum Endprodukt ist mannigfaltig (siehe Schaubild), kann jedoch grob in vier Schritte unterteilt werden:
            <br><br>
            <ol>
                <li>💡 Ideenfindung und Problemdefinition ("Ideate")</li>
                <li>📥 Datenbeschaffung und -aufbereitung ("Experiment")</li>
                <li>👩‍💻 Entwicklung ("Model Improvement Loop")</li>
                <li>✅ Implementierung ("Industrialize")</li>
            </ol>
            <br><br>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.image("images/analytics_snail.png", caption="Der 'ING Use Case' Ansatz")
    st.markdown(
        """
        <div style='text-align: justify;'>
            In den Beispielen (siehe linke Seite), findest Du diese vier Schritte bezogen auf das jeweilige Beispiel wieder.
            Liese auf dieser Seite weiter, für eine kurze Übersicht dazu, was die einzelnen Schritte beinhalten.
            <br><br>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.subheader("**1. 💡 Ideenfindung und Problemdefinition**")
    st.write("")
    st.write(
        """
        **Welche Fragen kann Analytics/ML beantworten?**
        """
    )
    st.markdown(
        """
        <div style='text-align: justify;'>
            Im Rahmen der Ideenfindung sollte man sich zunächst bewusst machen, dass vier grundsätzliche Fragen mithilfe von Analytics beantwortet werden können:
            <ul>
                <li><i><b>Was</i></b> ist passiert? (deskriptive Analysen; z.B., wie viele Kreditanträge hatten wir in 2022?)</li>
                <li><i><b>Warum</i></b> ist etwas passiert? (diagnostische Analysen; z.B., welche Faktoren haben dazu geführt, dass wir mehr Kreditanträge hatten als im Vorjahr?)</li>
                <li><i><b>Was</i></b> wird <i><b>zukünftig</i></b> passieren? (prädiktive Analysen; z.B., wie viele Kreditanträge können wir in 2023 erwarten?)</li>
                <li><i><b>Wie</i></b> können wir dafür sorgen, dass <i><b>etwas Bestimmtes</i></b> in <i><b>Zukunft</i></b> passiert? (präskriptive Analysen; z.B., welche Kunden sollten wir bevorzugt kontaktieren, um in 2023 mehr Kreditabschlüsse zu erzielen?)</li>
            <ul>
            <br><br>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.write(
        """
        **Wann ergibt es Sinn über Machine Learning als Lösung nachzudenken?**
        """
    )
    st.markdown(
        """
        <div style='text-align: justify;'>
            Für folgende Probleme bietet sich Machine Learning als Lösung an:
            <ul>
                <li>Eine Aufgabe kann von Dir recht einfach ausgeführt werden, kommt aber in großen Volumina vor</li>
                <li>Wenn es schwer fällt, klare wenn/dann Regeln für eine Aufgabe festzulegen</li>
                <li>Aufgaben, für die viele Beispiele in Form von Daten (z.B., Emails, Dokumente, Datentabellen) vorliegen</li>
            <ul>
            Die unterstützung durch Machine Learning bei solchen Aufgaben führt idealerweise dazu, dass
            neue <i><b>Erkenntnisse</i></b> generiert werden, wir alle unsere <i><b>Aufgaben schneller und besser erledigen</i></b> können und
            unsere <i><b>Produkte langfristig noch innovativer werden</i></b>.
            <br><br>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.write(
        """
            **Ich habe eine Idee - was nun?**
        """
    )
    st.markdown(
        """
            Komme mit Ideen immer gerne auf den Tribe Analytics zu. Ob ein Projekt dann letztlich umgesetzt wird, hängt von verschiedenen Faktoren ab.
            Zum Beispiel:
            <ul>
                <li>Wie groß wären die Vorteile eines Machine Learning Modells (z.B. Zeitersparnis, Risikoreduktion, ...)</li>
                <li>Wie Komplex wäre der Prozess/die Lösung (einfach geht vor komplex)</li>
                <li>Sind ausreichend Daten vorhanden (z.B. Datenbanken, Dokumenten, Emails)</li>
            <ul>
            <br><br>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.subheader("**2. 📥 Datenbeschaffung und -aufbereitung**")
    st.write("")
    st.write(
        """
        **Welche Daten benötige ich und wie werden sie beschafft?**
        """
    )
    st.markdown(
        """
        <div style='text-align: justify;'>
            Daten sind überall - welche Daten kommen aber in Frage für einen potenziellen Use Case?
            Zunächst natürlich alle quantitativen und qualitativen Daten, die Informationen über das zu lösende Problem enthalten.
            Daten mit denen wir erfahrungsgemäß viel zu tun haben in der ING, sind etwa Tabellen im
            Datawarehouse, Dokumente (z.B., gescannte PDFs) oder Emails.
            <br><br>
            In dem Schaubild unter diesem Text kannst Du sehen, wie Datenflüsse typischerweise ablaufen.
            Meist kann in drei Schritte unterschieden werden:<br><br>
            <ol>
                <li>Finde die richtigen Daten für Deinen Use Case im Data Warehouse</li>
                <li>
                Die Daten werden verarbeitet und ein Modell erstellt
                (dafür nutzen wir sogennante Machine Learning Plattformen - das sind sicherer Umgebungen mit großer Rechenleistung)
                </li>
                <li>
                Einbindung der generierten Erkenntnisse/Vorhersagen als statischer Report,
                in einem Dashboard oder direkt im Endsystem
                </li>
            </ol>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.image("images/slides_process.png", caption="Übersicht typischer Datenflüsse")
    st.write(
        """
        **Wie müssen die Daten aufbereitet werden?**
        """
    )
    st.markdown(
        """
        <div style='text-align: justify;'>
            Insbesondere, wenn etwas Bestimmtes vorhergesagt werden soll (sog. "supervised learning"), werden gelabelte Daten benötigt.
            Das bedeutet, parallel zu dem, was in das Machine Learning Modell hineinfliesst und basierend worauf Vorhersagen getroffen werden, 
            benötigt das Modell "korrekte" Lösungen für einen Teil der Daten. Diese korrekten Lösungen vergleicht das Modell mit seinen Vorhersagen
            und lernt aus seinen Fehlern, um schlussendlich auch für Daten, für die wir die Lösung nicht kennen, möglichst genaue Vorhersagen zu treffen.
            <br><br>
            Meist liegen diese Labels für die Daten jedoch nicht vor und müssen für einen Teil der Daten manuell angelegt werden.
            Wie das aussehen kann, siehst du hier. Angenommen, wir wollten ein Machine Learning Modell entwickeln, das automatisch
            Spam Emails von normalen Emails unterscheiden kann. Damit das Modell den Unterschied lernen kann, müssen wir zunächst selbst für
            eine Hand voll Emails diese Unterscheidung treffen und die jeweilige Email als "Spam" oder "kein Spam" labeln. Anhand dieser
            Labels und der Email-Texte wird das Modell später lernen, diese Unterscheidung zu treffen. 
            <br><br>
            Lies Dir die unten stehenden Emails durch und entscheide selbst, ob es sich um Spam handelt oder nicht. Wähle Deine Entscheidung
            jeweils in der Selectbox aus.
        </div>
        """,
        unsafe_allow_html=True,
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
    st.markdown(
        """
        <div style='text-align: justify;'>
            <br><br>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.write("")

    st.subheader("**3. 👩‍💻 Entwicklung**")
    st.markdown(
        """
        <div style='text-align: justify;'>
            <b>Daten erkunden und verstehen:</b><br><br>
            Datenexploration ist ein wichtiger Schritt in Machine Learning Projekten, 
            da sie dazu beiträgt, das Verständnis der Daten und des zugrundeliegenden 
            Problems zu verbessern. Eine gründliche Datenexploration kann dazu beitragen, 
            potenzielle Fehler oder Anomalien in den Daten aufzudecken und somit eine solide Grundlage 
            für die weitere Analyse zu schaffen.
            <br><br>
            Visualisierungen und deskriptive Statistiken (siehe Auswahl typischer Techniken unten) helfen dabei,
            ein solche Verständnis zu erlangen. So kann ein erster Eindruck z.B. über den Zusammenhang verschiedener Variablen,
            deren Verteilung oder Veränderung im Zeitverlauf erlangt werden.
            <br><br>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.image("images/slides_data_exploration.png", caption="Visualisierungen und deskriptive Statistiken für ein besseres Verständnis der Daten")
    st.markdown(
        """
        <div style='text-align: justify;'>
            <b>Modellauswahl und -entwicklung:</b><br><br>
            Ein Machine Learning Modell ist nichts anderes als ein mathematische Funktion, die quantitative oder qualitative
            Daten als Input erhält, transformiert und eine Vorhersage zurückgibt.
            Die Auswahl des richtigen Machine Learning Modells für ein Problem ist ein entscheidender Schritt. 
            Es gibt viele verschiedene Modelle, die für verschiedene Arten 
            von Daten und Problemen geeignet sind. Ein wichtiger Aspekt bei der Modellauswahl ist der Trade-off 
            zwischen einfachen, aber weniger performanten Modellen und komplexeren, aber performanteren Modellen.
            <br><br>
            Einfache Modelle, wie beispielsweise lineare Regression oder logistische Regression, sind in der Regel 
            leicht zu verstehen und zu interpretieren. Sie können schnell implementiert werden und erfordern 
            nur wenige Parameter. Diese Modelle sind oft gut geeignet für Probleme mit wenigen Variablen 
            oder wenn die Daten eine lineare Beziehung aufweisen.
            <br><br>
            Komplexere Modelle, wie beispielsweise neuronale Netze oder Support Vector Machines, 
            können dagegen sehr performant sein, aber auch schwieriger zu verstehen und zu interpretieren. 
            Sie erfordern oft mehr Daten und können viele Parameter haben, die optimiert werden müssen. 
            Diese Modelle sind oft gut geeignet für komplexe Probleme mit vielen Variablen oder wenn die 
            Beziehung zwischen den Variablen nicht linear ist.
            <br><br>
            Untestehend findest Du eine Auflistung gängiger Machine Learning Modelle, sortiert nach ihrer Komplexität.
            Zusammen mit Dir identifizieren wir die Anforderungen, die sich aus einem Use Case ergeben und wählen dann
            ein passendes Modell aus.
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.image("images/slides_different_models.png", caption="Übersicht typischer Machine Learning Modelle")
    st.write(
        """
        <div style='text-align: justify;'>
        <b>Erfolgsmessung (Beispielhaft für Klassifikationsmodelle):</b>
        <br><br>
        Um objektiv quantifizieren zu können, ob ein Modell gute oder schlechte Vorhersagen trifft, können
        verschiedene Metriken genutzt werden. Welche Metrik genutzt werden soll, hängt unter anderem davon ab,
        ob es sich bei dem Modell um ein Klassifikations- oder Regressionsmodell handelt. Zudem spielt auch
        das Business Problem selbst eine Rolle. So kann z.B. die leichtere Interpretation im Business Kontext 
        für eine bestimmte Metrik und gegen eine andere sprechen.
        <br><br>
        Beispiele für sehr häufig genutzte Metriken sind die ROC-Kurve und der AUC (Area Under the Curve).
        Die ROC-Kurve (Receiver Operating Characteristic) ist ein Diagramm, das zeigt, 
        wie gut ein Modell in der Lage ist, zwischen positiven und negativen Beispielen zu unterscheiden.
        Die ROC-Kurve wird erstellt, indem man die wahren positiven Raten (TPR) den 
        falsch positiven Raten (FPR) gegenüberstellt. Die TPR gibt an,
        wie oft das Modell eine bestimmte Klasse - nennen wir sie Klasse A - auch als Klasse A erkennt,
        während die FPR angibt, wie oft das Modell eine andere Klasse - nennen wir sie Klasse B - 
        fälschlicherweise als Klasse A erkennt. Diese Werte werden für alle Wahrscheinlichkeits-Schwellenwerte
        zwischen 0% und 100% verglichen, wodurch eine Kurve zustande kommt, wie sie in der unteren Abbildung zu sehen ist.
        Je weiter oben links die Kurve, desto besser das Modell.
        <br><br>
        Die Area Under the Curve (AUC) ist ein Maß für die Leistungsfähigkeit eines Klassifikators,
        das auf der ROC-Kurve basiert. Die AUC gibt an, wie gut das Modell in der Lage ist,
        zwischen positiven und negativen Beispielen zu unterscheiden, unabhängig von der Wahl des Schwellenwerts.
        Eine AUC von 1 bedeutet, dass das Modell perfekt zwischen positiven und negativen Beispielen unterscheiden kann,
        während eine AUC von 0,5 bedeutet, dass das Modell keine Unterscheidung treffen kann und damit gleich 
        gut wie ein Zufallsklassifikator ist.
        <br><br>
        Zusammenfassend zeigt die ROC-Kurve die Leistung eines Klassifikators in Abhängigkeit 
        von verschiedenen Schwellenwerten, während die AUC die Gesamtleistung des Klassifikators 
        unabhängig von der Wahl des Schwellenwerts misst. Je höher die AUC, desto besser ist die 
        Leistung des Klassifikators.
        <br><br>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.image("images/slides_auc.png", caption="Erfolgsmessung anhand des ROC und der Area Under the Curve")

    st.subheader("**4. ✅ Implementierung**")
    st.write(
        """
        <div style='text-align: justify;'>
        Die Implementierung von Machine Learning Modellen ist ein wichtiger Schritt in der Entwicklung
        von Machine Learning Anwendungen. Dabei geht es darum, ein trainiertes Modell in der
        Produktionsumgebung einzusetzen, damit es für Vorhersagen genutzt werden kann.
        <br><br>
        Zunächst muss das Modell mit den richtigen Datenquellen verbunden werden. Das bedeutet, 
        dass die Daten, die für die Vorhersage benötigt werden, aus verschiedenen Quellen wie Datenbanken,
        APIs oder anderen Datenquellen abgerufen werden müssen. Es ist wichtig sicherzustellen, dass die
        Daten auf dem neuesten Stand und für das Modell geeignet sind.
        <br><br>
        Sobald das Modell mit den Datenquellen verbunden ist, kann es für Vorhersagen genutzt werden. Dabei
        werden neue Daten, die in Echtzeit oder in einem bestimmten Intervall eintreffen, vom Modell verarbeitet
        und Vorhersagen getroffen. Es ist wichtig sicherzustellen, dass das Modell dabei den Anforderungen 
        des Geschäftsprozesses gerecht wird (z.B. Anfragen schnell genung verarbeitet oder mit großen Datenmengen 
        umgehen kann).
        <br><br>
        Die Einbindung der Vorhersagen in den Geschäftsprozess ist ein weiterer wichtiger Schritt.
        Dazu müssen die Vorhersagen in einem Format bereitgestellt werden, das vom Geschäftsprozess verarbeitet
        werden kann. Beispielsweise können Vorhersagen in eine Datenbank geschrieben werden, die von anderen
        Systemen abgerufen wird, oder sie können direkt in ein System integriert werden.
        <br><br>
        Technische Voraussetzungen für die Implementierung ist eine robuste Produktionsumgebung (z.B. im
        Sinne nutzbarer APIs oder Datenbankanbindungen). Auch die Verfügbarkeit von Ressourcen 
        wie Rechenleistung und Speicherplatz ist wichtig, um sicherzustellen, dass das Modell schnell genug arbeiten kann, 
        um den Anforderungen des Geschäftsprozesses gerecht zu werden.
        <br><br>
        Untestehend siehst Du ein Beispiel, wie eine solche Implementierung konzeptionell aussehen kann. Dieses Beispiel
        stammt von einem tatsächlichen in der ING implementierten Projekt. Zunächst wurden Daten aus einer Testdatenbank
        extrahiert, um ein Modell zu trainieren. In Produktion werden nun zweimal monatlich Daten aus dem Data Warehouse
        extrahiert, vorbereitet und an das Modell geschickt. Das Modell wiederum spielt die Vorhersagen als csv Datei an
        das Data Warehouse zurück, von wo aus diese dann in die Reports der Business Line gelangen.
        <br><br>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.image("images/slides_early_collections_process.png", caption="Beispiel für einen Machine Learning Prozess in Produktion")

# Run the main function
if __name__ == '__main__':
    pass
