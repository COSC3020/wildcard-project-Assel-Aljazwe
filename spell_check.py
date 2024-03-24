from spellchecker import SpellChecker
import glob
import re

spell = SpellChecker()

# Define a function to clean words by removing punctuation
def clean_word(word):
    return re.sub(r'[^\w\s]', '', word)

# Find all markdown files
files = glob.glob('**/*.md', recursive=True)

# Initialize a flag to indicate if misspelled words were found
misspelled_words_found = False

# Loop through each file
for file_path in files:
    with open(file_path, 'r') as file:
        text = file.read()
        words = [clean_word(word) for word in text.split()]
        # Find misspelled words
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

