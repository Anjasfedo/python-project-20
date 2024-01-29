from PyDictionary import PyDictionary
# Import the PyDictionary class from the PyDictionary module.

dictionaries = PyDictionary()
# Create an instance of the PyDictionary class named 'dictionaries'.

while True:
    # Start an infinite loop.

    word = input("> Enter the word: ")
    # Prompt the user to enter a word.

    if word == "":
        # Check if the entered word is an empty string.

        break
        # If the word is empty, exit the loop.

    print(dictionaries.meaning(word))
    # Display the meaning of the entered word using the PyDictionary class.
