from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr,formataddr
import smtplib

from_addr='addr'
password='password'
to_addr='@qq.com'
smtp_server='smtp.163.com'

msg=MIMEText('testemail','plain','utf-8')
msg['From']=from_addr
msg['To']=to_addr
msg['Subject']=Header('hello,wm','utf-8')

server=smtplib.SMTP(smtp_server)
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()