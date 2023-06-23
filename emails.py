import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

class SendEmail:
    def __init__(self,text,city):
        self.email_password = os.environ.get("EMAIL_PASSWORD")
        self.email_username = os.environ.get("EMAIL_USERNAME")
        self.emails_to = "quiquemonroy@gmail.com"
        self.server = "smtp.gmail.com"
        self.port = 587

        self.s = smtplib.SMTP(host=self.server, port=self.port)
        self.s.starttls()
        self.s.login(self.email_username, self.email_password)

        self.msg = MIMEMultipart()  # Creates the message
        self.msg['To'] = self.emails_to  # Sets the receiver's email address
        self.msg['From'] = self.email_username  # Sets the sender's email address
        self.msg['Subject'] = f"Hay un vuelo barato a {city}!"  # Sets the subject of the message
        self.msg.attach(MIMEText(text, 'html'))  # Attaches the email content to the message as html

        self.s.send_message(self.msg)  # Sends the message
        del self.msg  # Deletes the message from memory
        # print("Email Sent.")