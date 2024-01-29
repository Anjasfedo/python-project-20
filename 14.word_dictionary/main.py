from PyDictionary import PyDictionary

dictionaries = PyDictionary()

while True:
    word = input("> Enter the word: ")

    if word == "":
        break

    print(dictionaries.meaning(word))
