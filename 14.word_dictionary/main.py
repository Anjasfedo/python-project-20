def main():
    word_dictionary = {
        "hai": "menyapa",
        "mata": "indra pengelihatan",
        'bumi': "planet dengan kehidupan"
    }
    
    while True:
        word = input("> Enter the word: ")
        if word == "":
            break
        
        if word in word_dictionary:
            print(f"{word}: {word_dictionary[word]}")
    
main()