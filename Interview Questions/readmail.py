# Importing libraries
import imaplib, email

user = 'vsjtestmail@gmail.com'
password = 'TestMa1lPass'
imap_url = 'imap.gmail.com'

# Function to get email content part i.e its body part
def get_body(msg):
	if msg.is_multipart():
		return get_body(msg.get_payload(0))
	else:
		return msg.get_payload(None, True)

# Function to search for a key value pair
def search(key, value, con):
	result, data = con.search(None, key, '"{}"'.format(value))
	return data

# Function to get the list of emails under this label
def get_emails(result_bytes):
	msgs = [] # all the email data are pushed inside an array
	
	for num in result_bytes[0].split():
		typ, data = con.fetch(num, '(RFC822)')
		msgs.append(data)

	return msgs

# this is done to make SSL connection with GMAIL
con = imaplib.IMAP4_SSL(imap_url)

# logging the user in
con.login(user, password)

# calling function to check for email under this label
con.select('Inbox')

# fetching emails from this user "tu**h*****1@gmail.com"
msgs = get_emails(search('FROM', 'champaksworld@gmail.com', con))

# Uncomment this to see what actually comes as data
print(msgs)
print(type(msgs))
print(len(msgs))
