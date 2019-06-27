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

msg.add_alternative('''\

<!DOCTYPE html>
<html>
    <body>
        <h1 style="color:blue;"> This is a Heading</h1>
    </body>
</html>
''', subtype='html')


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

    smtp.login(email, password)

    smtp.send_message(msg)
