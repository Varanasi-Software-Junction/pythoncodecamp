# Program to send emails


"""
Program to send email after logging in to a GMail Account.

You require a gmail account with less security.
Connect to the SMTP Server and send mails
"""

import smtplib


# smtplib dpcumentation https://docs.python.org/3/library/smtplib.html


def mailSend(currentsession, receiver, subject, mail_content, mailfrom):
    # Function for sending mail.
    # The function takes a receiver emailid, subject, mail content and a sender
    # The first parameter is a SMTP Session that is already connected to GMail

    from email.message import EmailMessage
    receiver = receiver.strip()
    mailfrom = mailfrom.strip()
    # Setup the MIME
    msg = EmailMessage()  # Documentation on https://docs.python.org/3.9/library/email.message.html#email.message
    # .EmailMessage
    msg.add_header('Content-Type', 'text/html')
    mail_content = mail_content.encode('utf-8')
    msg.set_payload(mail_content)

    # msg.set_content(mail_content)
    msg['Subject'] = subject
    msg['From'] = mailfrom
    msg['To'] = receiver
    # msg['Cc'] = ''
    # Add Cc addresses if you want
    # msg['Bcc'] = ''
    # Add Bcc addresses
    currentsession.send_message(msg)  # Send the message

'''
receivers = ["microsoft.prime1@gmail.com", "avinfra.ajeet@gmail.com", "oneshoptechsolutions@gmail.com",
             "avinfra.raiajit@gmail.com", "rneo1921@gmail.com", "johnrobertusa0@gmail.com", "champaksworld@gmail.com"]
receivercount = len(receivers)
subjects = ["One", "Two", "Three"]
subjectcount = len(subjects)
content = ""
try:
    sender_pass = 'aajtak@ndtv'
    session = smtplib.SMTP('smtpout.secureserver.net', 587)  # use gmail with port
    session.starttls()  # enable security
    session.login('info@urgent.business', sender_pass)  # login with mail_id and password
    mailcount = 0
    subnumber = 0
    receivernumber = 0
    while True:
        currentreceiver = receivers[receivernumber]
        currentsubject = subjects[subnumber]
        content = "new data " + str(mailcount)
        receivernumber = (receivernumber + 1) % receivercount
        subnumber = (subnumber + 1) % subjectcount
        mailcount += 1
        mailSend(session, currentreceiver, currentsubject, content,
                 "From Sender<info@urgent.business>")
        if mailcount > 1000:
            exit(0)
except Exception as e:
    print("Connection Error ", e)
# End Program
'''
