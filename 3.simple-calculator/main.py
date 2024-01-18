from arithmeticOperation import arithmeticOperation as aOpt


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
        aOpt.add(a, b)
    elif choice.upper() == "B":
        print("Subtraction")
        a, b = checkInput()
        aOpt.subtract(a, b)
    elif choice.upper() == "C":
        print("Multiplication")
        a, b = checkInput()
        aOpt.multiply(a, b)
    elif choice.upper() == "D":
        print("Division")
        a, b = checkInput()
        aOpt.divide(a, b)
    elif choice.upper() == "E":
        print("Program Ended")
        quit()
    else:
        print("Invalid choice. Please choose A, B, C, D, or E.")
