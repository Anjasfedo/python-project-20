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
