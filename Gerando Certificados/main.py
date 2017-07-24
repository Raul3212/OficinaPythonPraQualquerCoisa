from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import pandas as pd

def main():

    dados = pd.read_excel('dados.xlsx')

    for i in range(len(dados)):
        img = Image.open('certificado.jpg')
        (width, height) = img.size
        font = ImageFont.truetype('arial.ttf', 80)
        draw = ImageDraw.Draw(img)
        (fontWidth, fontHeight) = font.getsize(dados.loc[i, 'Nome'])
        draw.text((width/2 - fontWidth/2, 1000), dados.loc[i, 'Nome'], (0, 0, 0), font=font)
        img.save('./Certificado_{}.jpg'.format(dados.loc[i, 'Nome'].replace(' ', '_')))

if __name__ == '__main__':
    main()

