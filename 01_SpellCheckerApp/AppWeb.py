import streamlit as st
from spellchecker import SpellChecker
import string

# Initialize spell checker
spell = SpellChecker()

st.set_page_config(page_title="Spell Checker App")

st.title("Spell Checker App")
st.write("Enter text below to check spelling mistakes.")

# Input box
text = st.text_area("Enter text to check", height=150)

if st.button("Check Spelling"):

    if text.strip() == "":
        st.warning("Please enter some text.")

    else:
        words = text.split()
        corrected_words = []
        corrections = []

        for word in words:

            #removing punctuations
            clean_word = word.strip(string.punctuation)

            #handling symbols and numbers
            if not clean_word.isalpha():
                corrected_words.append(word)
                continue

            #skip proper nouns

            lower_word = clean_word.lower()

            if lower_word in spell:
                corrected_words.append(word)
                continue

            corrected_word = spell.correction(lower_word)

            if corrected_word is None:
                corrected_words.append(word)
                continue

            if word[0].isupper():
                corrected_word = corrected_word.capitalize()

            corrections.append(f'{word} -> {corrected_word}')
            corrected_words.append(corrected_word)

        corrected_text = " ".join(corrected_words)  


        # Output
        st.subheader("Corrected Text")
        st.success(corrected_text)

        if corrections:
            st.subheader("Corrections Made")
            for c in corrections:
                st.write(c)
        else:
            st.info("No spelling mistakes found.")
