import smtplib
import getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

logmail=str(input("Enter your email to login : "))
loginPass=getpass.getpass()
s=smtplib.SMTP(host='smtp.gmail.com',port=587)

s.starttls()
s.login(logmail,loginPass)


