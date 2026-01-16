
import streamlit as st
from spellchecker import SpellChecker

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
            lower_word = word.lower()
            corrected_word = spell.correction(lower_word)

            # If no correction is found, keep the original word
            if corrected_word is None:
                corrected_words.append(word)
            else:
                # If correction is different, note it
                if corrected_word != lower_word:
                    corrections.append(f'{word} → {corrected_word}')
                corrected_words.append(corrected_word)

        corrected_text = " ".join(corrected_words).capitalize()

        # Output
        st.subheader("Corrected Text")
        st.success(corrected_text)

        if corrections:
            st.subheader("Corrections Made")
            for c in corrections:
                st.write(c)
        else:
            st.info("No spelling mistakes found.")
