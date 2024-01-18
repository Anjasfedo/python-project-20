def replaceWord():
    # Initial string
    str = "Anjasfedo hi hi hi hi hi"

    # Get user input for word to replace
    wordToReplace = input("> Enter word to replace: ")

    # Get user input for word replacement
    wordReplacement = input("> Enter word replacement: ")

    # Replace the specified word in the string
    replacedWord = str.replace(wordToReplace, wordReplacement)

    # Return the modified string
    return replacedWord


# Print the result of the replaceWord function
print(replaceWord())
