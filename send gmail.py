import yagmail

# Replace with your Gmail address and app password
sender_email = "your_gmail@gmail.com"
sender_password = "your_app_password"

# Replace with the recipient's email address
receiver_email = "recipient_email@example.com"

# Set up the yagmail object
y = yagmail.SMTP(sender_email, sender_password)

# Send the email
y.send(to=receiver_email, subject="Test Email", contents="This is a test email sent using Python and Gmail.")