def is_leap_year(year):
    # Define a function named 'is_leap_year' that takes a 'year' as an argument.

    if year % 4 == 0:
        # Check if the year is divisible by 4.

        if year % 100 == 0:
            # If divisible by 4, check if it's also divisible by 100.

            if year % 400 == 0:
                # If divisible by 100, check if it's also divisible by 400.
                print("Leap year")
            else:
                print("Not leap year")
        else:
            print("Leap year")
    else:
        print("Not leap year")
    # If not divisible by 4, it's not a leap year.

is_leap_year(2000)
# Call the 'is_leap_year' function with the argument 2000 to check if it's a leap year.
