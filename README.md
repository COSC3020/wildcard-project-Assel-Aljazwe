[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/tTztJ7yI)
# Wildcard Project

You have a cool idea for an algorithms project? Use this repository. Make sure
to explain what problem you're solving, how you're doing it, and that you test
your code.

# Overview of the Project Approach:

**Objective**: Throughout completing the coursework, I frequently found myself double or triple checking for spelling mistakes or perhaps grammatical issues in the analysis to ensure smooth readability. This process was often annoying and time-consuming. Drawing inspiration from the automated code testing workflows, I decided to implement a similar system for README files to improve documentation review and enhance user convenience.

## Key Components of the Implementation: 
- Spell Checking Script (spell_check.py):
  - Uses the $SpellChecker$ library to identify misspelled words within markdown files.
  - Properly handles punctuation and does not wrongly identify words that utilize it as wrong.
  - Iterates through all Markdown (.md) files in the repository, then prints a list of misspelled words found in each file for the user to later review in error details. This ensures comprehensive coverage of all documentation.
- Github Actions Workflow (spellcheck_workflow.yml):
  - Triggered on every push and pull request event, the workflow executes the spell-checking script, and provides feedback.
  - Configured with steps for setting up Python, installing dependencies or libraries and executing the $spell_check.py$ script.
- Pull Request Template: 
