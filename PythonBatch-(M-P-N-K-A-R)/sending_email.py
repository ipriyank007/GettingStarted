from os import environ
import smtplib

username = environ.get('EMAIL_USER')
password = environ.get('EMAIL_PASS')

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(username, password)

    subject = 'About the meeting'
    body = 'The meeting went totally fine, thanks for support.'

    msg = f'Subject: {subject}\n\n{body}'

    smtp.sendmail(username, 'priyank.p@red18tech.com', msg)
