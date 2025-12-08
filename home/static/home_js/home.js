document.addEventListener('DOMContentLoaded', function() {

    const campoBusca = document.getElementById('campo-busca');
 
    const linksProduto = document.querySelectorAll('.link-produto');

    campoBusca.addEventListener('keyup', function() {
        const termoBusca = campoBusca.value.toLowerCase();

        linksProduto.forEach(link => {

            const cardProduto = link.querySelector('.card-produto');
            
            const nomeProduto = cardProduto.getAttribute('data-nome-produto');

            if (nomeProduto.includes(termoBusca)) {
                link.style.display = ''; 
            } else {
                link.style.display = 'none';
            }
        });
    });
});