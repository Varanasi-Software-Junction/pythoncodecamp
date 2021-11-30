import tkinter.filedialog
import smtplib
from tkinter import *
from tkinter import ttk, scrolledtext
import MailThread as mt
import sendergmail as mailer
from cefpython3 import cefpython as cef
import ctypes

receivers = []


def sendMail():
    sender_pass = 'hjh76^%&^%PP'
    session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
    session.starttls()  # enable security
    session.login('aventtesttech@gmail.com', sender_pass)  # login with mail_id and password

    subject = subjecttext.get()
    content = contenttext.get("1.0", tkinter.END)
    fromaddress = fromtext.get()
    mailaddresses = receiverstext.get("1.0", tkinter.END)
    mailaddresses = mailaddresses.split()
    print(mailaddresses, subject, content, fromaddress)
    for receiver in mailaddresses:
        mailer.mailSend(session,receiver,subject,content,fromaddress)



    """
    for receiver in mailaddresses:
        mailer = mt.MailThread(session, fromaddress, receiver, subject, content)
        mailer.start()
    session.quit()
    """
    # mailer.mailSend(receiverstext.get("1.0", tkinter.END),subjecttext.get(),contenttext.get("1.0", tkinter.END),fromtext.get())


def readTheFile(filepath):
    f = open(filepath)
    return f.read()


def getTheFile(txt):
    # print("Called")
    filedialog = tkinter.filedialog
    filepath = filedialog.askopenfilename()
    print(filepath)
    filecontents = readTheFile(filepath)
    txt.insert(1.0, filecontents)


# mailer.mailSend()
root = Tk()

root.title("Mail Sender")
root.minsize(width=500, height=400)
frm = ttk.Frame(root, padding=10)
frm.grid()
# Design the Interface


ttk.Label(frm, text="Mailer").grid(column=3, row=1)
statuslabel = ttk.Label(frm, text="Status")
statuslabel.grid(column=4, row=1)
ttk.Label(frm, text="To").grid(column=3, row=2)
receiverstext = scrolledtext.ScrolledText(frm, wrap=tkinter.WORD, width=40, height=10, font=("Times New Roman", 15))
receiverstext.grid(row=3, column=4)
ttk.Label(frm, text="From").grid(column=3, row=4)
fromtext = ttk.Entry(frm, width=50)
fromtext.grid(row=4, column=4)
ttk.Button(frm, text="Receivers", command=lambda: getTheFile(receiverstext)).grid(column=5, row=2)
ttk.Label(frm, text="Subject").grid(column=3, row=5)
subjecttext = ttk.Entry(frm, width=50)
subjecttext.grid(row=5, column=4)
ttk.Label(frm, text="Content").grid(column=3, row=6)
contenttext = scrolledtext.ScrolledText(frm, wrap=tkinter.WORD, width=40, height=10, font=("Times New Roman", 15))
contenttext.grid(row=7, column=4)
ttk.Button(frm, text="Content", command=lambda: getTheFile(contenttext)).grid(column=5, row=6)
ttk.Button(frm, text="Mail", command=lambda: sendMail()).grid(column=3, row=8)
# Design the Interface


root.mainloop()
