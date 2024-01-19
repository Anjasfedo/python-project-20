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
