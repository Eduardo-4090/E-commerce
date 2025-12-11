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
    setTimeout(()=>{
            const msg = document.getElementById('messages');
            if (msg){
                 msg.style.display ='none'
            }
        },4000 );
});