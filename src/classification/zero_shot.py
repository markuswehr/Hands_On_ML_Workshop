"""
Define function for transformer-based zero-shot classification.

author: Markus Wehr
date: 2023-02-01
"""

import pandas as pd
from typing import List
from transformers import pipeline
import streamlit as st


@st.cache_resource(ttl=180, max_entries=1)
def load_zero_shot() -> pipeline:
    """
    Load zero shot pipeline and cache for re-runs.

    Output:
        classifier -- Zero shot classification pipeline
    """
    classifier = pipeline("zero-shot-classification", model="Sahajtomar/German_Zeroshot")

    return classifier

def get_classification(classifier: pipeline, text: str, candidate_labels: List[str]) -> pd.DataFrame:
    """
    Function to load zero-shot model and perform classification.

    input:
        text-- Text to be classified
        candidate_labels -- Classes in which the text should be classified
    output:
        preds_df -- Labels, probability scores and the original text sequence
    """
    # Since this is a monolingual model,its sensitive to hypothesis template
    hypothesis_template = "In diesem Text geht es um {}."
    preds = classifier(text, candidate_labels, hypothesis_template=hypothesis_template)
    preds_df = pd.DataFrame(data=preds)
    preds_df = preds_df.rename(
        {
            "sequence": "Text",
            "labels": "Kategorien",
            "scores": "Wahrscheinlichkeit pro Label"
        },
        axis=1
    )

    return preds_df[["Kategorien", "Wahrscheinlichkeit pro Label"]]


if __name__ == "__main__":
    pass
