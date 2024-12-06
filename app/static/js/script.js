// Selecionando o botão e o parágrafo
const button = document.getElementById('magicButton');
const description = document.getElementById('description');

// Adicionando evento de clique ao botão
button.addEventListener('click', () => {
    // Alterar texto do parágrafo
    description.innerHTML = "A magia aconteceu! Sinta o equilíbrio e a tranquilidade.";
    
    // Alterar estilos da página
    document.body.style.backgroundColor = "#f0f8ff"; // Cor de fundo azul claro
    document.body.style.transition = "background-color 0.5s ease";

    // Alterar estilo do botão
    button.style.backgroundColor = "#f4b9b8";
    button.style.color = "3543855";
    button.style.border = "none";
    button.style.padding = "10px 20px";
    button.style.borderRadius = "5px";
    button.
  
innerHTML = "Transformação completa!";
});