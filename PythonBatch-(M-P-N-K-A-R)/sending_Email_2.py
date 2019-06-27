from os import environ
import smtplib

email = environ.get('EMAIL_USER')
password = environ.get('EMAIL_PASS')

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

    smtp.login(email, password)

    subject = "Meeting Report"
    body = 'Need to know the full report on how the meeting actually went.'

    msg = f'Subject: {subject}\n\n{body}'

    smtp.sendmail(email, email, msg)
