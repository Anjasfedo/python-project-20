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
