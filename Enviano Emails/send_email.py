import smtplib
from email.mime.multipart import *
from email.mime.text import *
from email.mime.base import *
from email import encoders

fromaddr = 'rauldearaujolima@gmail.com'
toaddrs  = 'rauldearaujolima@gmail.com'

msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddrs
msg['Subject'] = 'SUBJECT OF THE MAIL'
 
body = 'YOUR MESSAGE HERE'
msg.attach(MIMEText(body, 'plain'))

filename = 'jp2b16.jpg'
attachment = open('jp2b16.jpg', 'rb')

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment; filename= %s' % filename)
 
msg.attach(part)

username = 'rauldearaujolima@gmail.com'
password = open('senha.txt', 'r').readline()
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login(username, password)
server.sendmail(fromaddr, toaddrs, msg.as_string())
server.quit()
