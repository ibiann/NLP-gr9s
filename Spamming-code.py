""" write a python program to check e-mail spamming check
"""

from curses import raw
import email
from functools import total_ordering
from inspect import _SourceObjectType
import os
import sys
import smtplib
import getpass

try:
    from email.mime.text import MIMEText
except ImportError:
    from email.MIMEText import MIMEText

    os.system('pip3 install email')

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(input('Enter your email address: '), getpass.getpass())
    msg = MIMEText(input('Enter your message: '))
    msg['Subject'] = input('Enter your subject: ')
    msg['From'] = input('Enter your email address: ')
    msg['To'] = input('Enter the recipient\'s email address: ')
    server.send_message(msg)
    server.quit()
    print('Email sent successfully')

   if __name__ == '__main__':
        main()
        smtp_server = 'smtp.gmail.com'
        port = 587
        set_server = "gmail"

    elif set_server == "yahoo":
        smtp_server = 'smtp.mail.yahoo.com'
        port = 465
    else:
        print("Invalid server")
        sys.exit()
email_user = input('Email: ')
password = getpass.getpass('Password: ')
email_to   = input('To: ')
subject = input('Subject: ')
body = input('Message: ')
total = len(body)

msg = MIMEText(body)
msg['Subject'] = subject
msg['From'] = email_user
msg['To'] = email_to

try:
    server = smtplib.SMTP(smtp_server, port)
    server.ehlo()
    server.starttls()
    server.login(email_user, password)
    server.sendmail(email_user, email_to, msg.as_string())
    server.quit()
    print('Email sent successfully')
except:
    print('Something went wrong...')

sys.exit()