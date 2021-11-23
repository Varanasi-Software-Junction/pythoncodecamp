import smtplib

sender = 'info@aventtech.in'
receivers = ['champaksworld@gmail.com']

message = """From: From Person <info@aventtech.in>
To: To Person <champaksworld@gmail.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
    print("Sending email")
    smtpObj = smtplib.SMTP('smtpout.secureserver.net', 465)
    smtpObj.sendmail(sender, receivers, message)
    print("Successfully sent email")
except:
    print("Error: unable to send email")
