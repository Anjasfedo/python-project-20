def add(a, b):
    result = a + b
    print(f"{a} + {b} = {result}\n")


def subtract(a, b):
    result = a - b
    print(f"{a} - {b} = {result}\n")


def multiply(a, b):
    result = a * b
    print(f"{a} * {b} = {result}\n")


def divide(a, b):
    if b != 0:
        result = a / b
        print(f"{a} / {b} = {result}\n")
    else:
        print("Error: Cannot divide by zero.\n")


def checkInput():
    a = int(input("> First Number: "))
    b = int(input("> Second Number: "))
    return a, b


while True:
    print("A. Addition")
    print("B. Subtraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Exit")

    choice = input("> Input your choice: ")

    if choice.upper() == "A":
        print("Addition")
        a, b = checkInput()
        add(a, b)
    elif choice.upper() == "B":
        print("Subtraction")
        a, b = checkInput()
        subtract(a, b)
    elif choice.upper() == "C":
        print("Multiplication")
        a, b = checkInput()
        multiply(a, b)
    elif choice.upper() == "D":
        print("Division")
        a, b = checkInput()
        divide(a, b)
    elif choice.upper() == "E":
        print("Program Ended")
        quit()
    else:
        print("Invalid choice. Please choose A, B, C, D, or E.")
