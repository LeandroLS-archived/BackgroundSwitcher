import ctypes
import requests
from ClimaTempo import ClimaTempo
from Util import *
from ImageSwitcher import ImageSwitcher
import os 
import datetime

token = '77f38866b9b2a40baba7ac91486db242'
url = 'http://apiadvisor.climatempo.com.br/api/v1/weather/locale/3477/current?token={}'.format(token)

response = requests.get(url)
if(api_esta_funcionando(response)):
    jsonObj     = response.json()['data']
    temperatura = jsonObj['temperature']
    sensacao    = jsonObj['sensation']
    humidade    = jsonObj['humidity']
    condicao    = jsonObj['condition']
    data        = jsonObj['date']
    clima       = ClimaTempo(temperatura,sensacao,humidade,condicao,data)
    hora = datetime.datetime.now().hour
    ImageSwitcher = ImageSwitcher()
    ImageSwitcher.switch_image(hora,temperatura,sensacao,humidade)
else:
    print('algum problema na api')


