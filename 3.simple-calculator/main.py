# Import the arithmeticOperation module and alias it as aOpt
from arithmeticOperation import arithmeticOperation as aOpt

# Function to take user input for two numbers and return them
def checkInput():
    a = int(input("> First Number: "))
    b = int(input("> Second Number: "))
    return a, b

# Infinite loop for the calculator program
while True:
    # Display menu options
    print("A. Addition")
    print("B. Subtraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Exit")

    # Take user input for the choice
    choice = input("> Input your choice: ")

    # Check the user's choice and perform the corresponding operation
    if choice.upper() == "A":
        print("Addition")
        a, b = checkInput()
        # Call the add function from the arithmeticOperation module
        aOpt.add(a, b)
    elif choice.upper() == "B":
        print("Subtraction")
        a, b = checkInput()
        # Call the subtract function from the arithmeticOperation module
        aOpt.subtract(a, b)
    elif choice.upper() == "C":
        print("Multiplication")
        a, b = checkInput()
        # Call the multiply function from the arithmeticOperation module
        aOpt.multiply(a, b)
    elif choice.upper() == "D":
        print("Division")
        a, b = checkInput()
        # Call the divide function from the arithmeticOperation module
        aOpt.divide(a, b)
    elif choice.upper() == "E":
        print("Program Ended")
        # Exit the program
        quit()
    else:
        # Display an error message for an invalid choice
        print("Invalid choice. Please choose A, B, C, D, or E.")
