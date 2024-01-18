import sys
sys.path.append('../../python-project-20')

from helpers import helpers as hh
from email.message import EmailMessage
import ssl
import smtplib

emailSender = "fedohyou@gmail.com"
emailPassword = hh.readJson(path="../config.json", value="GMAIL_APP_PASSWORD")

emailReceiver = "hiyas68683@grassdev.com"

subject = "Anjas Gantenk"

body = """
Anjasfedo Gantenks
"""

em = EmailMessage()

em["From"] = emailSender

em["To"] = emailReceiver

em["Subject"] = subject

em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    smtp.login(emailSender, emailPassword)
    
    smtp.sendmail(emailSender, [emailReceiver], em.as_string())
