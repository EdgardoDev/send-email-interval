from dotenv import load_dotenv
import yagmail
import os
import time

load_dotenv()

# Create initial variables.
sender_email = os.getenv("SENDER_EMAIL")
receiver_email = os.getenv("RECEIVER_EMAIL")

# Email subject.
email_subject = "Hello from Python! 👋"

# Email body.
email_body = """
Hello! 
This is the body content of the email.
Best regards,
The Python Script. 🤖
"""
while True:
    # Create an SMTP object instance
    smtp = yagmail.SMTP(user=sender_email, password=os.getenv("APP_PASSWORD"))
    # Send email.
    smtp.send(to=receiver_email, subject=email_subject, contents=email_body)
    print("The Email Was Successfully Sent!")
    # Add a time interval, after the script runs it'll sleep for 60 seconds
    # then send a new email.
    time.sleep(60)