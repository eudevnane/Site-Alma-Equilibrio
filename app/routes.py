from app import app #Está importando o objeto app do módulo app. Representa a aplicação.
from flask import render_template #Está importando a função para carregar e renderizar arquivos html.

# Cria uma rota para a URL base ("/"), que será a página inicial do site.
@app.route('/') #Essa linha cria uma rota, uma url onde a página está acessível.
def home(): #Define uma função chamada ()home. Será executada quando o usuário acessar a página inicial.
    return render_template('home.html') #Diz ao flask para renderizar o arquivo home.html e enviar ao navegador do usuário. 
 
# Cria uma rota para a URL "/sobre".
@app.route('/sobre')  # Define a função `sobre`, que será executada ao acessar a página Sobre.
def sobre():
    return render_template('sobre.html')

# Cria uma rota para a URL "/produtos", que será a página de demonstração dos produtos.
@app.route('/produtos')
def produtos():
    return render_template('produtos.html')

@app.route('/carrinho')
def carrinho():
    return render_template('carrinho.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

# Este bloco garante que o código seja executado apenas quando o script for executado diretamente.
if __name__ == '__main__':
    app.run(debug=True)