from datetime import datetime

from imbox import Imbox

# SSL Context docs https://docs.python.org/3/library/ssl.html#ssl.create_default_context

with Imbox('imap.gmail.com',
        username='vsjtestmail@gmail.com',
        password='TestMa1lPass',
        ssl=True,
        ssl_context=None,
        starttls=False) as imbox:

    # Get all folders
    status, folders_with_additional_info = imbox.folders()

    # Gets all messages from the inbox
    all_inbox_messages = imbox.messages()
    print(all_inbox_messages,type(all_inbox_messages))
    for uid,message in all_inbox_messages:
        print(message.subject)
        print(message.body)
        messagebody=message.body.get("plain")
        print(messagebody)