from spellchecker import SpellChecker
import glob
import re

spell = SpellChecker()

def clean_word(word):
    return re.sub(r'[^\w\s]', '', word)

misspelled_words_found = False
results_path = "spell_check_results.txt"

with open(results_path, "w") as results_file:
    for file_path in glob.glob('**/*.md', recursive=True):
        with open(file_path, 'r') as file:
            text = file.read()
            words = [clean_word(word) for word in text.split()]
            misspelled = spell.unknown(words)
            if misspelled:
                misspelled_words_found = True
                results_file.write(f"Misspelled words in {file_path}:\n")
                print(f"::error file={file_path}::Found misspelled words.")
                for word in misspelled:
                    results_file.write(f"- {word}\n")

if misspelled_words_found:
    print("::error ::Spelling check failed. Please review the misspelled words listed in the results file.")
    exit(1)



