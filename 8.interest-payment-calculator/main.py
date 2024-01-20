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

    # Save the result to a text file named "interest_payment_calculator_result.txt"
    with open("interest_payment_calculator_result.txt", "w") as file:
        file.write(f"The monthly payment for this loan is: ${monthlyPayment:.2f}")

if __name__ == "__main__":
    # Run the main function in a loop
    while True:
        main()
