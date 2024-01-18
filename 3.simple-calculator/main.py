
def add(a, b):
    result = a + b
    print(f"{str(a)} + {str(b)} = {result}")
    
def subtarct(a, b):
    result = a - b
    print(f"{str(a)} - {str(b)} = {result}")
    
def multiply(a, b):
    result = a * b
    print(f"{str(a)} * {str(b)} = {result}")
    
def divide(a, b):
    result = a / b
    print(f"{str(a)} / {str(b)} = {result}")
    
def checkInput():
    a = int(input("> First Number: "))
    b = int(input("> Second Number: "))
    
    return a, b
    
print("A. Addition")
print("B. Subtraction")
print("C. Multuplication")
print("D. Division")
print("E. Exit")

