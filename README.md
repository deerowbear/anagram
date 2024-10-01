# Anagram

To run this program clone the repo and run a command like this:

```
/bin/python3 ~/projects/python/anagram/anagram_challange.py --path ~/projects/python/anagram/words.txt
```

## Tech Stack

**Python version:** 3.8.10

## Description
This project takes in a single argument that will be used to parse a file into a dictionary. The key will be the word and the value will be a sorted array of the word. After parsing the input file, the program will ask the user for some input. Once the input has been given by the user it will sort the input and see if there is a match in the dictionary. If there is a match found then we have found an anagram. If no anagram is found, a message will be printed out saying no anagram is found, and new input will be requested. If an anagram is found, the input and the anagram will be printed out, and new input will be requested. If ".quit" is entered, the application will terminate.