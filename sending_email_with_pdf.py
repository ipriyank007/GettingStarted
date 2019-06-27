from os import environ
import smtplib
import imghdr
from email.message import EmailMessage

email = environ.get('EMAIL_USER')
password = environ.get('EMAIL_PASS')

msg = EmailMessage()
msg['Subject'] = "Meeting Report"
msg['From'] = email
msg['To'] = email
msg.set_content('Need to know the full report on how the meeting actually went. Image Attached!')
files = ['jane_austen.pdf']
for file in files:
    with open(file, 'rb') as f:
        file_data = f.read()
        file_name = f.name
        # print(file_type)

    msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

    smtp.login(email, password)

    smtp.send_message(msg)
