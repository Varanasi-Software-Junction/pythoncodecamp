import tkinter.filedialog
import smtplib
from tkinter import *
from tkinter import ttk, scrolledtext
import godaddymailer as mailer

receivers = []


def getSession(smtpserver, portno, email, sender_pass):
    # sender_pass = 'hjh76^%&^%PP'
    session = smtplib.SMTP(smtpserver, portno)  # use gmail with port
    session.starttls()  # enable security
    session.login(email, sender_pass)  # login with mail_id and password
    return session


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
        mailer.mailSend(session, receiver, subject, content, fromaddress)

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
receiverstext = scrolledtext.ScrolledText(frm, wrap=tkinter.WORD, width=40, height=5, font=("Times New Roman", 15))
receiverstext.grid(row=3, column=4)
ttk.Label(frm, text="From").grid(column=3, row=4)
fromtext = scrolledtext.ScrolledText(frm, wrap=tkinter.WORD, width=40, height=5, font=("Times New Roman", 15))
fromtext.grid(row=4, column=4)
ttk.Button(frm, text="From", command=lambda: getTheFile(fromtext)).grid(column=5, row=4)

ttk.Button(frm, text="Receivers", command=lambda: getTheFile(receiverstext)).grid(column=5, row=2)
ttk.Label(frm, text="Subject").grid(column=3, row=5)
subjecttext = scrolledtext.ScrolledText(frm, wrap=tkinter.WORD, width=40, height=5, font=("Times New Roman", 15))
subjecttext.grid(row=5, column=4)
ttk.Button(frm, text="Subjects", command=lambda: getTheFile(subjecttext)).grid(column=5, row=5)
ttk.Label(frm, text="Content").grid(column=3, row=6)
contenttext = scrolledtext.ScrolledText(frm, wrap=tkinter.WORD, width=40, height=5, font=("Times New Roman", 15))
contenttext.grid(row=7, column=4)
ttk.Button(frm, text="Content", command=lambda: getTheFile(contenttext)).grid(column=5, row=6)
ttk.Button(frm, text="Mail", command=lambda: sendMail()).grid(column=3, row=8)


def runThis():
    subjects = subjecttext.get("1.0", tkinter.END)
    subjects = subjects.split()
    froms = fromtext.get("1.0", tkinter.END)
    froms = froms.split()
    mailaddresses = receiverstext.get("1.0", tkinter.END)
    mailaddresses = mailaddresses.split()
    print("receivers", mailaddresses)
    print("subjects", subjects)
    print("froms", froms)
    subjectcount = 0
    maxsubject = len(subjects)
    mailcount = 10
    fromscount = 0
    maxfrom = len(froms)
    tocount = 0
    maxto = len(mailaddresses)
    frommail = froms[fromscount]
    frompassword = froms[fromscount + 1]
    fromport = int(froms[fromscount + 2])
    fromsmtp = froms[fromscount + 3]
    content = contenttext.get("1.0", tkinter.END)
    session = getSession(fromsmtp, fromport, frommail, frompassword)

    for i in range(1, mailcount + 1):
        try:
            mailer.mailSend(session, mailaddresses[tocount], subjects[subjectcount] + str(i), content, frommail)
            print("Mail sent from ", frommail, " to ", mailaddresses[tocount])
        except Exception as e:
            fromscount = (fromscount + 4) % maxfrom
            frommail = froms[fromscount]
            frompassword = froms[fromscount + 1]
            fromport = int(froms[fromscount + 2])
            fromsmtp = froms[fromscount + 3]
            session = getSession(fromsmtp, fromport, frommail, frompassword)
        tocount = (tocount + 1) % maxto
        subjectcount = (subjectcount + 1) % maxsubject
        print(i)


ttk.Button(frm, text="Mail", command=lambda: runThis()).grid(column=3, row=8)
# Design the Interface


root.mainloop()
