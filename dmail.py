import smtplib
from email.message import EmailMessage

def sendmail(to,subject,body):
    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login('sanobarshaik61@gmail.com','htyr obpz xmmf rfck')
    msg = EmailMessage()
    msg['From']='sanobarshaik61@gmail.com'
    msg['To'] = to
    msg['Subject'] = subject
    msg.set_content(body)
    server.send_message(msg)
    server.quit()

