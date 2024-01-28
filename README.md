# 20 Python Project :rocket:

## 1. Email Sender :email:

The `main.py` script demonstrates how to send an email using Gmail's SMTP server securely. The script utilizes the `smtplib` library for SMTP communication and the `ssl` library for creating a secure context.

### Functionality :gear:

1. **Import Libraries :arrow_forward:**

   - Imports necessary libraries such as `sys`, `ssl`, `smtplib`, `EmailMessage`, and the custom `helpers` module.

2. **Set Email Configuration :email:**

   - Sets up the email configuration, including the sender's email address (`emailSender`), receiver's email address (`emailReceiver`), subject of the email (`subject`), and the email body (`body`).

3. **Read App Password :closed_lock_with_key:**

   - Reads the Gmail app password from the `config.json` file using the `readJson` function from the custom `helpers` module.

4. **Compose Email :pencil2:**

   - Creates an instance of the `EmailMessage` class and sets its properties, including sender, receiver, subject, and body.

5. **Secure Connection :lock:**

   - Establishes a secure connection to Gmail's SMTP server using the `smtplib.SMTP_SSL` class.

6. **Login to Email Account :key:**

   - Logs in to the sender's Gmail account using the provided email address (`emailSender`) and app password (`emailPassword`).

7. **Send Email :mailbox:**

   - Sends the composed email using the `smtp.sendmail` method.

8. **Print Success Message :white_check_mark:**
   - Prints "Email sent successfully!" to the console if the email is sent without errors.

### Usage :wrench:

1. Update the script with your Gmail sender email address, receiver email address, and Gmail app password.
2. Run the script using `python main.py`.
3. Check the console for the success message.

#

## 2. Word Replacement Function :pencil2:

The `replaceWord` function demonstrates a simple word replacement mechanism in a string.

### Functionality :gear:

1. **Initialize String :page_facing_up:**

   - Initializes a string with the content "Anjasfedo hi hi hi hi hi".

2. **Get User Input for Word Replacement :keyboard:**

   - Takes user input for the word to be replaced using the `input` function.

3. **Get User Input for Word Replacement :keyboard:**

   - Takes user input for the replacement word using the `input` function.

4. **Replace Word in String :arrows_counterclockwise:**

   - Uses the `replace` method to replace occurrences of the specified word with the replacement word in the string.

5. **Return Modified String :arrow_right:**

   - Returns the modified string after the word replacement.

6. **Print Modified String :page_with_curl:**
   - Prints the result of the `replaceWord` function, showcasing the string after word replacement.

### Usage :wrench:

1. Modify the initial string or run the function as is to see the word replacement in action.

#

## 3. Simple Calculator :123:

The `arithmeticOperation` module contains functions for basic arithmetic operations.

### Functionality :gear:

1. **Addition :heavy_plus_sign:**

   - Adds two numbers and prints the result.

2. **Subtraction :heavy_minus_sign:**

   - Subtracts the second number from the first and prints the result.

3. **Multiplication :heavy_multiplication_x:**

   - Multiplies two numbers and prints the result.

4. **Division :heavy_division_sign:**
   - Divides the first number by the second (with error handling for division by zero) and prints the result or an error message.

### Usage :wrench:

1. Modify the numbers in the function calls or run the functions as is to perform basic arithmetic operations.

#

## 4. Email Slicer :scissors:

The `main.py` script slices an email address into its components, including the username, domain, and extension.

### Functionality :gear:

1. **Display Welcome Message :wave:**

   - Displays a welcome message and instructions to close the program.

2. **User Input for Email Address :keyboard:**

   - Takes user input for the email address.

3. **Slice Email Components :scissors:**

   - Slices the email address into username, domain, and extension.

4. **Print Sliced Components :page_with_curl:**
   - Prints the sliced components of the email address.

### Usage :wrench:

1. Run the script using `python main.py`.
2. Input your email address when prompted.
3. View the sliced components displayed on the console.

#

## 5. Binary Search Algorithm :mag_right:

The `binarySearch` function demonstrates a binary search algorithm to find an element in a sorted list.

### Functionality :gear:

1. **Binary Search Function :arrow_binary:**

   - The main binary search function that takes a sorted list (`myList`) and an element to search for (`element`).

2. **Initialize variables :1234:**

   - `middle`, `start`, and `end` represent indices, and `steps` counts the iterations.

3. **Iterate while the search range is valid :arrows_counterclockwise:**

   - The while loop continues until the start index is greater than the end index.

4. **Display the current search range :scroll:**

   - Prints the current sub-list being considered in each iteration.

5. **Update step count and calculate middle index :1234:**

   - Increments the step count and calculates the middle index of the current range.

6. **Check if the element is found :white_check_mark:**

   - Compares the middle element with the target element and returns the index if found.

7. **Update the start and end based on element comparison :arrows_counterclockwise:**

   - If the target element is less than the middle, updates the end index; if greater, updates the start index.

8. **If the element is not found :warning:**
   - Prints a message indicating that the element is not present in the list.

### Usage :wrench:

1.  Calls the `binarySearch` function with an example list and element and prints the result.
2.  Run the script using `python main.py`.

#

## 6. Quiz Program :question:

The `main.py` script implements a simple quiz program using questions stored in the `questions.py` module.

### Functionality :gear:

1. **Quiz Loop :repeat:**

   - Iterates through each question in the quiz.

2. **Display Question :speech_balloon:**

   - Prints the current question.

3. **User Input for Answer :keyboard:**

   - Takes user input for the answer.

4. **Check Answer :white_check_mark:**

   - Compares the user's answer with the correct answer.

5. **Score Tracking :1234:**

   - Updates the user's score based on correct answers.

6. **Display Results :trophy:**
   - Prints whether each answer is correct or wrong.
   - Displays the final score at the end of the quiz.

### Usage :wrench:

1. Run the script using `python main.py`.
2. Answer each quiz question prompted.
3. View the correctness of your answers and your final score at the end.

#

# 7. QR Code Generator :qr_code:

The `main.py` script generates a QR code for a given URL using the `qrcode` library.

### Functionality :gear:

1. **Import Libraries :arrow_forward:**

   - Imports necessary libraries, including `qrcode` and `os`.

2. **Generate QR Code :barcode:**

   - Utilizes the `qrcode` library to create a QR code for a given URL.
   - The `os` library is used to handle directory operations.

3. **Save QR Code Image :floppy_disk:**

   - The generated QR code image is saved in the `images` directory.
   - The directory is created if it doesn't exist.

4. **Display Image Path :file_folder:**
   - Prints the path where the QR code image is saved.

### Usage :wrench:

1. Run the script using `python main.py`.
2. Enter the URL when prompted.
3. Check the `images` directory for the saved QR code image.

#

# 8. Interest Payment Calculator :currency_exchange:

The `main.py` script calculates the monthly payment for a loan based on the loan amount, annual interest rate, and the number of years.

### Functionality :gear:

1. **Display Welcome Message :wave:**

   - Displays a welcome message introducing the monthly payment loan calculator.

2. **User Input for Loan Details :keyboard:**

   - Takes user input for the loan amount, annual interest rate, and the number of years.

3. **Calculate Monthly Interest Rate :1234:**

   - Calculates the monthly interest rate based on the annual interest rate.

4. **Calculate Total Number of Months :calendar:**

   - Calculates the total number of months for the loan based on the number of years.

5. **Calculate Monthly Payment :money_with_wings:**

   - Uses the loan formula to calculate the monthly payment.

6. **Display Monthly Payment :computer:**

   - Prints the calculated monthly payment with 2 decimal places on the console.

7. **Save Result to Text File :floppy_disk:**
   - Saves the calculated monthly payment to a text file named "interest_payment_calculator_result.txt" inside the "texts" directory.

### Usage :wrench:

1. Run the script using `python main.py`.
2. Input the loan amount, annual interest rate, and the number of years when prompted.
3. View the calculated monthly payment on the console.
4. Check the "texts/interest_payment_calculator_result.txt" file for the saved result.

#

# 9. Password Generator :key:

The `password_generator.py` script generates a random password based on user input and saves it to a text file.

### Functionality :gear:

1. **Generate Password :key:**

   - Asks the user for the desired length of the password.
   - Creates a random password using a combination of uppercase letters, lowercase letters, digits, and special characters.
   - Shuffles the characters to add randomness to the password.
   - Displays the generated password on the console.

2. **Save Password to Text File :floppy_disk:**

   - Saves the generated password to a text file named "password.txt" in the "texts" directory.
   - Creates the "texts" directory if it doesn't exist.

3. **User Interaction :computer:**
   - Asks the user if they want to generate a password.
   - Ends the program if the user chooses not to generate a password.

### Usage :wrench:

1. Run the script using `python main.py`.
2. Input the desired length of the password when prompted.
3. View the generated password on the console.
4. Check the "texts" directory for the saved password in the "password.txt" file.

#

# 10. Dice Rolling :game_die:

The `main.py` script simulates rolling two six-sided dice and displays the results using ASCII art.

### Functionality :gear:

1. **Dice Representation :art:**

   - Defines ASCII art representations for each possible face of a six-sided die.
   - ASCII art is stored in a dictionary (`diceDrawing`) with keys representing the numbers 1 to 6.

2. **Roll Dice Function :game_die:**

   - Prompts the user if they want to roll the dice.
   - Continues rolling as long as the user responds with 'Yes'.
   - Generates random numbers for two dice rolls.
   - Displays the result of the dice rolls and the corresponding ASCII art.
   - Prompts the user if they want to roll again.

3. **Random Number Generation :game_die:**
   - Utilizes the `random` module to generate random numbers for dice rolls.

### Usage :wrench:

1. Run the script using `python main.py`.
2. Input 'Yes' when prompted to roll the dice.
3. View the results of the dice rolls and corresponding ASCII art.
4. Choose to roll again or end the program.

#

# 11. Site Connectivity Checker :globe_with_meridians:

The `main.py` script checks the connectivity of a specified website by attempting to open a connection to the provided URL.

### Functionality :gear:

1. **Main Function :mag_right:**

   - Defines a function named `main` that takes a URL as a parameter.
   - Opens a connection to the specified URL using `urllib.urlopen`.
   - Displays a message indicating successful connection along with the response code.

2. **Site Connectivity Check :globe_with_meridians:**
   - Prompts the user to input the domain of the site (e.g., "google.com").
   - Constructs a full URL by adding "https://www." as a prefix to the user-provided domain.
   - Calls the `main` function, passing the constructed full URL, to check the site's connectivity.

### Usage :wrench:

1. Run the script using `python main.py`.
2. Input the domain of the site when prompted.
3. View the messages indicating the site's connectivity and response code.

#

# 12. Currency Converter :money_exchange:

The `main.py` script converts US dollars to Pound Sterling using a fixed exchange rate.

### Functionality :gear:

1. **Main Function :money_with_wings:**

   - Defines a function named `main`.
   - Displays a message indicating the purpose of the script.
   - Prompts the user to input a dollar amount using `eval` to evaluate the input as a Python expression.
   - Calls the `convert_to_pounds` function to convert dollars to pounds.
   - Displays the result of the conversion.

2. **Conversion Function :currency_exchange:**
   - Uses a lambda function named `convert_to_pounds` to convert dollars to pounds using a fixed exchange rate.

### Usage :wrench:

1. Run the script using `python main.py`.
2. Input the dollar amount when prompted.
3. View the converted amount in pounds sterling.

#

# Helpers

## Helpers Function for Reading JSON Configuration :file_folder:

The `readJson` function serves as a helper to read values from a JSON configuration file.

### Functionality :gear:

1. **Read JSON Configuration :file_folder:**

   - Takes two parameters: `path` for the path to the JSON file and `value` for the key to retrieve.
   - Uses the `open` function to open the specified JSON file in read mode.
   - Utilizes `json.load` to load the JSON content from the file.

2. **Retrieve Specific Value :arrow_right:**

   - Returns the value associated with the specified key (`value`) in the JSON file.

3. **Error Handling :warning:**
   - The function assumes that the key (`value`) exists in the JSON file. Error handling can be added to handle cases where the key is not present.

### Usage :wrench:

1. **Configure JSON File :pencil2:**
   - Ensure that the `config.json` file is properly configured with the required key-value pairs. For example:
     ```json
     {
       "GMAIL_APP_PASSWORD": "your_gmail_app_password"
     }
     ```
2. **Use `readJson` Function :calling:**

   - Call the `readJson` function in your main script to retrieve specific values from the configuration file.

     ```python
        # Example usage in the main script
        email_password = readJson("path/to/config.json", "GMAIL_APP_PASSWORD")
     ```
