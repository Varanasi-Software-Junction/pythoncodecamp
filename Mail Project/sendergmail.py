import smtplib


def mailSend(session, receiver, subject, mail_content, mailfrom):
    from email.message import EmailMessage
    receiver = receiver.strip()
    mailfrom = mailfrom.strip()

    # The mail addresses and password
    sender_address = 'Unknown@unknown.com'

    receiver_address = receiver
    # Setup the MIME
    msg = EmailMessage()
    msg.add_header('Content-Type', 'text/html')
    mail_content = mail_content + "<img src='http://test.itrplus.com/getimg?detail=" + receiver + "' style='display" \
                                                                                                  ":none;'> "
    mail_content = mail_content.encode('utf-8')
    msg.set_payload(mail_content)

    # msg.set_content(mail_content)
    msg['Subject'] = subject
    msg['From'] = mailfrom
    msg['To'] = receiver
    # msg['Cc'] = ''
    # msg['Bcc'] = ''
    session.send_message(msg)

    print('Mail Sent to ', receiver)
