import streamlit as st
import re

st.title("📝 Text Analysis (Cloud-Compatible, No External Packages)")

# Text input
text = st.text_area("Enter text for analysis", height=200)

def simple_pos(word):
    if word.istitle():
        return "PROPN"
    elif re.match(r'^\d+$', word):
        return "NUM"
    elif word.endswith("ing"):
        return "VERB"
    elif word.lower() in ["is", "am", "are", "was", "were"]:
        return "AUX"
    else:
        return "NOUN"

def simple_ner(words):
    return [(w, "PROPN") for w in words if w.istitle()]

if text:
    # Tokenize words
    words = re.findall(r'\b\w+\b', text)

    # POS tagging
    pos_tags = [(w, simple_pos(w)) for w in words]
    st.subheader("Part-of-Speech (POS) Tags")
    st.table(pos_tags)

    # NER
    entities = simple_ner(words)
    st.subheader("Named Entities (NER)")
    if entities:
        st.table(entities)
    else:
        st.write("No named entities found.")
