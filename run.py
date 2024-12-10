from app import app

# Este bloco garante que o código abaixo seja executado apenas se este arquivo for executado diretamente,
# Essa condição verifica se o script está sendo executado diretamente ou se está sendo importado como um módulo em outro script.
# Apenas quando o script é executado diretamente, o servidor Flask é iniciado.
if __name__ == '__main__':
    app.run(debug=True) # "app.run" Inicia o servidor Flask. 
    
    # O argumento debug=Trueé muito útil durante o desenvolvimento:
    # Atualiza o servidor automaticamente para salvar alterações.
    # Mostra informações relacionadas a erros no navegador.