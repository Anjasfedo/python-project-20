import urllib.request as urllib
# Import the 'urllib.request' module and alias it as 'urllib' for easier reference.

def main(url):
    # Define a function named 'main' that takes a URL as a parameter.

    print("Checking connectivity")

    res = urllib.urlopen(url)
    # Open a connection to the specified URL using 'urllib.urlopen' and store the result in 'res'.

    print(f"Connected to {url} successfully")

    print(f"With response code {res.getcode()}")
    # Display the response code obtained from the connection.

print("Site connectivity checker")
# Display a message indicating the purpose of the script.

domain = input("> Input domain of the site (e.g., google.com): ")
# Prompt the user to input the domain of the site.

full_domain = f"https://www.{domain}"
# Create a full URL by adding "https://www." as a prefix to the user-provided domain.

main(full_domain)
# Call the 'main' function, passing the constructed full URL, to check the site's connectivity.
