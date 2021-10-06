import smtplib
from getpass import getpass


gmail_user = input('gmail:')
gmail_password = getpass('password:')


to = [input('send to:')]
subject = input('subject:')

email_text = input('message text:')

server = smtplib.SMTP_SSL('smtp.gmail.com', 465) # this invokes the secure SMTP protocol
# server.ehlo() # Identify yourself to an ESMTP server using EHLO.
server.login(gmail_user, gmail_password) # login with creds
server.sendmail(gmail_user, to, email_text) # send mail
server.close() # close conection
