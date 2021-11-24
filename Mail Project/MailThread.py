import threading
import time
import sendergmail

exitFlag = 0


class MailThread(threading.Thread):
    def __init__(self,fromaddress,toaddress,subject,content):
        threading.Thread.__init__(self)
        self.fromaddress=fromaddress
        self.subject=subject
        self.toaddress=toaddress
        self.content=content

    def run(self):
        sendergmail.mailSend(self.toaddress,self.subject,self.content,self.fromaddress)


# Create new threads
#thread1 = MailThread("Champak Roy","champaksworld@gmail.com","Hello Champak","Please meet me today")

# Start new Threads
#thread1.start()


#print("Exiting Main Thread")
