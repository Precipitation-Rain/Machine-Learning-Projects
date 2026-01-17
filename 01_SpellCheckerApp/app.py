# step - 1 : importing spellchecker library
from spellchecker import SpellChecker

# step - 2 : making a class
class SpellcheckerApp:

    def __init__(self):
        self.spell = SpellChecker()

    def correct_text(self , text):
        words = text.split()
        corrected_words = []

        for word in words:
            word = word.lower()
            corrected_word = self.spell.correction(word)

            if corrected_word != word :
                print(f'Correcting "{word}" to "{corrected_word}" \n')
                corrected_words.append(corrected_word)

            else:
                print(f'Word "{word}" is already correct \n')
                corrected_words.append(word)

#step - 3 : Returning the corrected word

        return " ".join(corrected_words).capitalize()
    
# step - 4 :  Running the app

    def run(self):
        print('\n -------Spell Checker-------')

        while True:

            text = input("Enter text to check (or enter 'exit' to quit) : ")

            if text.lower() == 'exit':
                print("Closing The Program.........")
                break

            corrected_text = self.correct_text(text)
            print(f'Corrected text "{corrected_text}"')

# step - 5 : Running the main Program

if __name__ == "__main__":
    SpellcheckerApp().run()