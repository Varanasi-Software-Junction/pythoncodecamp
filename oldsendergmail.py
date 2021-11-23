import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

mail_content = '''The film is being released tomorrow
'''
# The mail addresses and password
sender_address = 'Unknown@unknown.com'
sender_pass = 'hjh76^%&^%PP'
receiver_address = 'champaksworld@gmail.com'
# Setup the MIME
message = MIMEMultipart()
message['From'] = "Unknown <Unknown@unknown.com>"
message['To'] = 'microsoft.prime1@gmail.com,champaksworld@gmail.com,varanasisoftwarejunction@gmail.com'.split(",")
message.add_header('reply-to', sender_address)
message['Subject'] = 'Arriving on Tuesday'  # The subject line
# The body and the attachments for the mail
message.attach(MIMEText(mail_content, 'plain'))
# Create SMTP session for sending the mail
session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
session.starttls()  # enable security
session.login('aventtesttech@gmail.com', sender_pass)  # login with mail_id and password
text = message.as_string()
session.sendmail(sender_address, receiver_address, text)
session.quit()
print('Mail Sent')
