def main():
    print("Convert US dollars to Pound Sterling")
    print()

    dollars = eval(input("> Input dollar amount: "))

    pounds = conver_to_pounds(dollars)

    print(f"{dollars} dollars is {pounds} pounds sterling")

conver_to_pounds = lambda dollars: dollars * 0.82

main()