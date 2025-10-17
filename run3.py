import streamlit as st
import nltk
from nltk import word_tokenize, pos_tag

# Download NLTK data if not already
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

st.title("📝 Text Analysis: POS & Simple NER (Cloud-Compatible)")

# Text input
text = st.text_area("Enter text for analysis", height=200)

if text:
    words = word_tokenize(text)
    pos_tags = pos_tag(words)

    # Display POS tags
    st.subheader("Part-of-Speech (POS) Tags")
    st.table(pos_tags)

    # Simple NER: capitalized words as entities
    st.subheader("Named Entities (NER)")
    entities = [(w, "PROPN") for w in words if w.istitle()]
    if entities:
        st.table(entities)
    else:
        st.write("No named entities found.")
