import streamlit as st
import spacy
from spacy.cli import download

st.title("📝 Text Analysis: NER & POS (Cloud-Compatible)")

# Ensure SpaCy model is downloaded
try:
    nlp = spacy.load("en_core_web_sm")
except:
    download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

# Text input
text = st.text_area("Enter text for analysis", height=200)

if text:
    doc = nlp(text)

    # POS tagging
    st.subheader("Part-of-Speech (POS) Tags")
    pos_list = [(token.text, token.pos_) for token in doc]
    st.table(pos_list)

    # Named Entity Recognition (NER)
    st.subheader("Named Entities (NER)")
    if doc.ents:
        ents_list = [(ent.text, ent.label_) for ent in doc.ents]
        st.table(ents_list)
    else:
        st.write("No named entities found.")
