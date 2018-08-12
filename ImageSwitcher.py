import ctypes
import os
import datetime
from PIL import Image, ImageDraw, ImageFont

class ImageSwitcher:
    def __init__(self):
        self.pasta_manha = os.getcwd()+'\\imagens\\Manhã'
        self.pasta_tarde = os.getcwd()+'\\imagens\\Tarde'
        self.pasta_noite = os.getcwd()+'\\imagens\\Noite'
        self.pasta_imagem_desenhada = os.getcwd()+'\\imagens\\Imagem Desenhada'
        self.SPI_SETDESKWALLPAPER = 20 
        print(__file__)
    
    def pega_imagem(self, hour):
        if(hour < 12):
            return self.pasta_manha+'\\manhã.jpeg'
        elif(hour >= 12 and hour < 18):
            return self.pasta_tarde+'\\tarde.jpg'
        elif(hour >= 18):
            return self.pasta_noite+'\\noite.jpeg'

    def desenha_na_imagem(self, imagem, hora, temperatura, sensacao, humidade):
        imagem = Image.open(imagem)
        draw = ImageDraw.Draw(imagem)
        font = ImageFont.truetype('arial.ttf',size=50)
        (x, y) = (900, 150)
        message = ("Temperatura: {0} º C\n" 
                   "Sensação: {1} º C\n"
                   "Humidade: {2}%".format(temperatura, sensacao, humidade))
        color = '#FFFF33'
        draw.text((x,y),message,font=font, fill=color)
        imagem.save(self.pasta_imagem_desenhada+'\\imagem_desenhada.jpg')
        return self.pasta_imagem_desenhada+'\\imagem_desenhada.jpg'

    def switch_image(self, hour, temperatura, sensacao, humidade):   
        imagem = self.pega_imagem(hour)
        caminho_imagem_desenhada = self.desenha_na_imagem(imagem,hour,temperatura,sensacao,humidade)
        ctypes.windll.user32.SystemParametersInfoW(20, 0, caminho_imagem_desenhada, 0)
