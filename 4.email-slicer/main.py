def main():
    # Display a welcome message and instructions to close the program
    print("Welcome to Email Slicer")
    print("Press ctrl+c to close this program")

    # Take user input for the email address
    emailInput = input("> Input your email address: ")

    # Split the email address into username and domain using "@" as the delimiter
    username, domain = emailInput.split("@")

    # Split the domain into domain name and extension using "." as the delimiter
    domain, extension = domain.split(".")

    # Print the sliced components of the email address
    print(f"Username: {username}")
    print(f"Domain: {domain}")
    print(f"Extension: {extension}")
    print("")

# Run the main function in an infinite loop
while True:
    main()
