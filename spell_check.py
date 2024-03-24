from spellchecker import SpellChecker
import glob
import re

spell = SpellChecker()

def clean_word(word):
    return re.sub(r'[^\w\s]', '', word)

# Initialize a list to hold all misspelled words and their occurrences.
misspellings = []

for file_path in glob.glob('**/*.md', recursive=True):
    with open(file_path, 'r') as file:
        text = file.read()
        words = [clean_word(word) for word in text.split()]
        misspelled = spell.unknown(words)
        if misspelled:
            print(f"::error file={file_path}::Found misspelled words.")
            for word in misspelled:
                misspellings.append(f"{word} in {file_path}")

if misspellings:
    print("::error ::Spelling check failed. Misspelled words detected:")
    for misspelling in misspellings:
        print(misspelling)
    exit(1)


