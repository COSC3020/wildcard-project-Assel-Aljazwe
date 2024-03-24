from spellchecker import SpellChecker
import glob

spell = SpellChecker()

# Find all markdown files
files = glob.glob('**/*.md', recursive=True)

# Loop through each file
for file_path in files:
    with open(file_path, 'r') as file:
        text = file.read()
        # Find misspelled words
        misspelled = spell.unknown(text.split())
        if misspelled:
            print(f"Misspelled words in {file_path}:")
            for word in misspelled:
                print(f"- {word}")
            print("\n")
