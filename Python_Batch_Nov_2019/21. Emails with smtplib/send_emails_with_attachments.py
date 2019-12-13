from os import environ, listdir, path
import smtplib
from email.message import EmailMessage
import imghdr

user_email = environ.get('USER_EMAIL')
user_pass = environ.get('USER_PASS')

msg = EmailMessage()
msg['To'] = ['priyank.p@red18tech.com', 'factscred@gmail.com']
msg['From'] = user_email
msg['Subject'] = 'This is subject of this mail...'

msg.set_content('This is message body!!!')

# for image in listdir('images_to_attach'):
with open('20150421094316171.pdf', 'rb') as f:
    print(f.name)
    file_name = f.name
    file_content = f.read()
    file_subtype = imghdr.what(f.name)
    print(file_subtype)
    msg.add_attachment(file_content, maintype='application', subtype = 'octet-stream', filename = file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(user_email, user_pass)
    smtp.send_message(msg)