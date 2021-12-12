# Program to read Gmail using IMAP. Internet Mail Access Protocol


"""
We use the Imbox library to read email from Gmail

"""

from imbox import Imbox

# documentation of Imbox https://pypi.org/project/imbox/

try:  # Call the constructor of Imbox
    myinbox = Imbox('imap.gmail.com', username='vsjtestmail@gmail.com', password='TestMa1lPass',
                    ssl=True,
                    ssl_context=None,
                    starttls=False)
except Exception as e:
    print("Error in connecting to Gmail: ", e)
    exit(1)  # End the program if you cannot connect
inboxmessages = myinbox.messages()  # Get all inbox messages
count = 1
for uid, message in inboxmessages:  # Loop through the inbox messages and print
    print(count, ") Mail\nSubject:", message.subject)
    count += 1
    messagebody = message.body.get("plain")[0]
    print(messagebody)

# End Program
