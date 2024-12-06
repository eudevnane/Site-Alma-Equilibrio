from flask import Flask #Flask é uma classe importada do framework flask 
#Flask é um microframework para criar aplicações web. Ele permite criar sites e apis de maneira simples e rápida.

app = Flask(__name__) #Cria uma instância da classe flask chamada app.

from app import routes #Importa o arquivo routes.py dentro da pasta app. 