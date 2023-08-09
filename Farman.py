import smtplib
import ssl
from email.message import EmailMessage
email_sender = 'abcd123456@gmail.com'
email_receiver = ('abcd112233@gmail.com', 'abcd1234@gmail.com')
email_password = 'passward'
subject = 'Check out my new project'
body = """
That is project where I am working,
https://docs.google.com/document/d/1-PaHrrOkLHMLN2CqRdmwGvXySn8Vvamj690n-STwFTI/edit?usp=sharing
"""
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver

# Set the subject and body of the email
subject = 'Inform you about my project'
body = 'Hello, this is my project update!'
em['Subject'] = subject
em.set_content(body)
context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender,email_receiver, em.as_string())
