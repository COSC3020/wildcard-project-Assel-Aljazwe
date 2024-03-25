from spellchecker import SpellChecker
import glob
import re

spell = SpellChecker()

def clean_word(word):
    # Remove punctuation at the beginning and end of the word, retain apostrophes and hyphens within words
    return re.sub(r"(^\W+|\W+$)", "", word)

# Find all markdown files
files = glob.glob("**/*.md", recursive=True)

# Initialize a flag to indicate if misspelled words were found
misspelled_words_found = False

# Loop through each file
for file_path in files:
    with open(file_path, "r") as file:
        text = file.read()
        words = re.findall(r"\b[\w'-]+\b", text)
        misspelled = spell.unknown(words)
        if misspelled:
            misspelled_words_found = True
            print(f"Misspelled words in {file_path}:")
            for word in misspelled:
                print(f"- {word}")
            print("\n")

# Exit with a non-zero status code if misspellings were found
if misspelled_words_found:
    exit(1)





