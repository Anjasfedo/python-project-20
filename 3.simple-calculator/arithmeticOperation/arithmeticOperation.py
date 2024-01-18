# Function to perform addition of two numbers
def add(a, b):
    result = a + b
    print(f"{a} + {b} = {result}\n")

# Function to perform subtraction of two numbers
def subtract(a, b):
    result = a - b
    print(f"{a} - {b} = {result}\n")

# Function to perform multiplication of two numbers
def multiply(a, b):
    result = a * b
    print(f"{a} * {b} = {result}\n")

# Function to perform division of two numbers with error handling for division by zero
def divide(a, b):
    if b != 0:
        result = a / b
        print(f"{a} / {b} = {result}\n")
    else:
        print("Error: Cannot divide by zero.\n")
