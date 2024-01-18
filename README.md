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

## 
