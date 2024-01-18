# Import the sys module to manipulate Python runtime settings
import smtplib
import ssl
from email.message import EmailMessage
from helpers import helpers as hh
import sys

# Append the path of the project directory to the system path
sys.path.append('../../python-project-20')

# Import the readJson function from the helpers module and alias it as hh

# Import the EmailMessage class from the email.message module

# Import the ssl and smtplib modules for secure email communication

# Set the email sender's address
emailSender = "fedohyou@gmail.com"

# Retrieve the GMAIL_APP_PASSWORD from the configuration file using the readJson function
emailPassword = hh.readJson(path="../config.json", value="GMAIL_APP_PASSWORD")

# Set the email receiver's address
emailReceiver = "hiyas68683@grassdev.com"

# Set the subject of the email
subject = "Anjas Gantenk"

# Set the body (content) of the email
body = """
Anjasfedo Gantenks
"""

# Create an instance of the EmailMessage class
em = EmailMessage()

# Set the 'From' field of the email
em["From"] = emailSender

# Set the 'To' field of the email
em["To"] = emailReceiver

# Set the 'Subject' field of the email
em["Subject"] = subject

# Set the content (body) of the email
em.set_content(body)

# Create a default SSL context for secure communication
context = ssl.create_default_context()

# Use the SMTP_SSL class to connect to the Gmail SMTP server securely
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:

    # Log in to the email account using the provided credentials
    smtp.login(emailSender, emailPassword)

    # Send the email by converting the EmailMessage instance to a string using as_string()
    smtp.sendmail(emailSender, [emailReceiver], em.as_string())

    # Print a success message if the email is sent successfully
    print("Email sent successfully!")
