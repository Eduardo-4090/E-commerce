
    document.addEventListener('DOMContentLoaded', function() {
        const imagemPrincipal = document.querySelector('.img-principal img');
        const miniaturas = document.querySelectorAll('.mini-img img');
        
   
        function setActive(element) {
            document.querySelectorAll('.mini-img').forEach(div => {
                div.classList.remove('ativo');
            });
            element.parentNode.classList.add('ativo');
        }


        miniaturas.forEach(miniatura => {
            miniatura.addEventListener('click', function() {
                
                imagemPrincipal.src = this.src;
                
                setActive(this);
            });
        });

        const primeiraMinia = document.querySelector('.mini-img');
        if (primeiraMinia) {
            primeiraMinia.classList.add('ativo');
        }
        const add_carrinho = document.querySelector('.btn-carrinho')
        const form = document.getElementById('add-carrinho-form')

        add_carrinho.addEventListener('click', function(){
            form.submit();
        });
        setTimeout(()=>{
            const msg = document.getElementById('messages');
            if (msg){
                 msg.style.display ='none'
            }
        },4000 );
    })