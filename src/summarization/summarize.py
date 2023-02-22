"""
Define function for loading pre-trained transformer.

author: Markus Wehr
date: 2023-01-31
"""

from typing import Tuple

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import streamlit as st


@st.cache_resource(ttl=180, max_entries=2)
def load_summarization_model(model: str) -> Tuple[AutoModelForSeq2SeqLM, AutoModelForSeq2SeqLM]:
    """
    Load and cache tokenizer and model.

    Args:
        model -- Model to be loaded from huggingface
    Output:
        tokenizer -- Pre-trained tokenizer
        model -- Pre-trained model
    """
    tokenizer = AutoTokenizer.from_pretrained(model)
    model = AutoModelForSeq2SeqLM.from_pretrained(model)

    return tokenizer, model

def summarize(model: AutoModelForSeq2SeqLM, tokenizer: AutoTokenizer, input: str, summary_length: int=25) -> str:
    """
    Function that loads tokenizer and model and summarizes input.

    input:
        model -- Pre-trained model and tokenizer to load from huggingface
        tokenizer -- Pre-trained tokenizer from huggingface
        input -- Text to summarize
        summary_length -- Length of the final summary in words
    output:
        decoded_summary -- Summarized text
    """
    # "cuda" if torch.cuda.is_available() else "CPU"
    device = "cpu"
    model.to(device)
  
    #define model inputs          
    tokens = tokenizer(
        input,
        truncation=True,
        padding="longest",
        return_tensors="pt"
    ).to(device)

    # Generate predictions
    encoded_summary = model.generate(**tokens, max_new_tokens=summary_length)
    
    # Decode the predictions to store them
    decoded_summary = tokenizer.decode(encoded_summary[0], skip_special_tokens=True)

    return decoded_summary


if __name__ == "__main__":
    pass
