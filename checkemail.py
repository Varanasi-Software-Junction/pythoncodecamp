import re


# r' means raw string
# \b forces matching in beginning or end
# any character except newline
# {number of characters}
# This is an escape character
def isValidEMail(email):
    emailregex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{1,}\b'
    return re.fullmatch(emailregex, email) != None


print(isValidEMail("jhjj@hjj.c"))
