"""
Page with an example for text classification.

author: Markus Wehr
date: 2023-01-31
"""

import pandas as pd
import streamlit as st

from src.classification.zero_shot import get_classification


# Sidebar parameters
st.sidebar.write("**Veränderbare Parameter:**")
candidate_labels = st.sidebar.multiselect(
    label="Wähle für Dich relevante Kategorien",
    options=(
        "Beschwerde",
        "Girokonto",
        "Kredit",
        "Online-Banking",
    ),
    default=(
        "Beschwerde",
        "Girokonto",
        "Kredit",
        "Online-Banking",
    ),
)

st.header("Schneller zuordnen mithilfe von Textklassifizierung")
st.subheader("*Lege fest, nach welchen Kategorien Du klassifizieren möchtest und lasse die KI den Rest erledigen*")

input_txt = st.text_area("**Text, der klassifiziert werden soll:**", height=300)
preds_df = pd.DataFrame({
    "Kategorien": [None],
    "Wahrscheinlichkeit pro Label": [None],
})
submit = st.button("Text klassifizieren")  
if submit:
    preds_df = get_classification(text=input_txt, candidate_labels=candidate_labels)
st.table(preds_df)


if __name__ == "__main__":
    pass
