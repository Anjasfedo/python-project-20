import string

import random

import os


characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generatePassword():
    passwordLength = int(input("> How long the password would be? "))

    random.shuffle(characters)

    password = []

    for _ in range(passwordLength):
        password.append(random.choice(characters))

    random.shuffle(password)
    
    password = "".join(password)
    
    print(f"The password is: {password}")
    
    save_directory = os.path.abspath("texts")
    os.makedirs(save_directory, exist_ok=True)
        
    # Specify the text file path and save the result to a text file
    text_path = os.path.join(save_directory, "password.txt")

    # Save the result to a text file named "password.txt"
    with open(text_path, "w") as file:
        file.write(password)

option = input("> Do you want to generate password: (Y/N)")

if option.upper() == "Y":
    generatePassword()
elif option.upper() == "N":
    print("Program ended")
    quit()
else:
    print("Invalid Input, please input Y/N")
