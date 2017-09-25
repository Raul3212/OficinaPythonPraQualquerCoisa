from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import pandas as pd
import smtplib
from email.mime.multipart import *
from email.mime.text import *
from email.mime.base import *
from email import encoders

dados = pd.read_excel("dados.xlsx")

for i in range(len(dados)):
    for cont_certificado in range(1, 5):
        image = Image.open("Python {}.jpg".format(cont_certificado))
        #image.show()
        font = ImageFont.truetype("arial.ttf", 120)
        draw = ImageDraw.Draw(image)
        width_img = image.size[0]
        width = draw.textsize(dados.loc[i, "Nome"], font)[0]
        draw.text((width_img/2 - width/2, 870), dados.loc[i, "Nome"], (0,0,0), font=font)
        
        filename = "{}_{}.jpg".format(dados.loc[i, "Nome"].replace(' ', '_'), cont_certificado)
        image.save(filename)

        print("Enviando {} para {}".format(filename, dados.loc[i, "E-mail"]))

        fromaddr = 'rauldearaujolima@gmail.com'
        toaddrs  = dados.loc[i, 'E-mail']

        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddrs
        msg['Subject'] = 'Minicurso de Python'
        msg.attach(MIMEText("Obrigado por participar do minicurso de 'Python pra qualquer coisa!\nSeu certificado segue em anexo.'", 'plain'))

        attachment = open(filename, 'rb')

        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename=Certificado.jpg')
        
        msg.attach(part)

        username = 'rauldearaujolima@gmail.com'
        password = open('senha.txt', 'r').readline()
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(username, password)
        server.sendmail(fromaddr, toaddrs, msg.as_string())
        server.quit()
