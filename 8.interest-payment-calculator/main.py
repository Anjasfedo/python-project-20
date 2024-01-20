import os

def main():
    # Display a welcome message
    print("This is a monthly payment loan calculator")
    print("")

    # Input the loan amount, annual interest rate, and amount of years
    principal = float(input("> Input the loan amount: "))
    apr = float(input("> Input the annual interest rate: "))
    years = int(input("> Input amount of years: "))

    # Calculate monthly interest rate and total number of months
    monthlyInterestRate = apr / 1200
    amountOfMonths = years * 12

    # Calculate monthly payment using the loan formula
    monthlyPayment = principal * monthlyInterestRate / (1 - (1 + monthlyInterestRate) ** (-amountOfMonths))

    # Display the monthly payment with 2 decimal places
    print(f"The monthly payment for this loan is: ${monthlyPayment:.2f}")
    print("")
    print("")
    
    # Specify the text file directory and create it if it doesn't exist
    save_directory = os.path.abspath("texts")
    os.makedirs(save_directory, exist_ok=True)
        
    # Specify the text file path and save the result to a text file
    text_path = os.path.join(save_directory, "interest_payment_calculator_result.txt")

    # Save the result to a text file named "interest_payment_calculator_result.txt"
    with open(text_path, "w") as file:
        file.write(f"The monthly payment for this loan is: ${monthlyPayment:.2f}")

if __name__ == "__main__":
    # Run the main function in a loop
    while True:
        main()
