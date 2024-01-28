def main():
    # Define a function named 'main'.

    print("Convert US dollars to Pound Sterling")
    print()
    # Display a message indicating the purpose of the script.

    dollars = eval(input("> Input dollar amount: "))
    # Prompt the user to input a dollar amount and use 'eval' to evaluate the input as a Python expression.

    pounds = convert_to_pounds(dollars)
    # Call the 'convert_to_pounds' function to convert dollars to pounds.

    print(f"{dollars} dollars is {pounds} pounds sterling")
    # Display the result of the conversion.

convert_to_pounds = lambda dollars: dollars * 0.82
# Define a lambda function 'convert_to_pounds' that converts dollars to pounds using a fixed exchange rate.

main()
# Call the 'main' function to execute the currency conversion.
