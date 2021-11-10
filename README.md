Flashcard Utility
====

Make, edit, and study flashcard decks, *effiently*.


Goals
====

1. Make flashcard decks
2. Ablility to combine flashcard decks and remove duplicates
3. Study by matching term to definition and definiton to term
4. Study by spelling term based off of definiton

Requirements
====

These can simply be installed with pip

- colorama

Deck File Syntax
====

.deck files are the files used to store deck data.
These files are designed to be human readable/writable.

Each card is contain in one line.
The term and definition are seperated by a comma.
A forwards slash is used to allow for multiple terms/definitions in a card. 

Example deck file:
```
term1/another name for term1,definition1
term2,just a definition there
this is the term for card 3,this is its defintion/this is a seperate defintion
fun,coding
```
