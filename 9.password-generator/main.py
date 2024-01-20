import string
import random
import os

# Define the characters that can be used in the password
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generatePassword():
    # Input the desired length of the password
    passwordLength = int(input("> How long the password should be? "))

    # Shuffle the characters to add randomness
    random.shuffle(characters)

    # Create an empty list to store the password characters
    password = []

    # Choose random characters for the password
    for _ in range(passwordLength):
        password.append(random.choice(characters))

    # Shuffle the password characters for additional randomness
    random.shuffle(password)

    # Convert the list of characters into a string
    password = "".join(password)

    # Display the generated password
    print(f"The password is: {password}")

    # Specify the text file directory and create it if it doesn't exist
    save_directory = os.path.abspath("texts")
    os.makedirs(save_directory, exist_ok=True)
        
    # Specify the text file path and save the result to a text file
    text_path = os.path.join(save_directory, "password.txt")

    # Save the result to a text file named "password.txt"
    with open(text_path, "w") as file:
        file.write(password)

# Ask the user if they want to generate a password
option = input("> Do you want to generate a password? (Y/N)")

# Check the user's input and call the generatePassword function accordingly
if option.upper() == "Y":
    generatePassword()
elif option.upper() == "N":
    print("Program ended")
    quit()
else:
    print("Invalid input. Please input Y/N")
