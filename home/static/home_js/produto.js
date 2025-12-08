
    document.addEventListener('DOMContentLoaded', function() {
        const imagemPrincipal = document.querySelector('.img-principal img');
        const miniaturas = document.querySelectorAll('.mini-img img');
        
        // Função para alternar a classe 'ativo'
        function setActive(element) {
            document.querySelectorAll('.mini-img').forEach(div => {
                div.classList.remove('ativo');
            });
            element.parentNode.classList.add('ativo');
        }

        // Define o evento de clique para cada miniatura
        miniaturas.forEach(miniatura => {
            miniatura.addEventListener('click', function() {
                // Troca a imagem principal pela URL da miniatura clicada
                imagemPrincipal.src = this.src;
                
                // Adiciona o destaque visual
                setActive(this);
            });
        });

        // Garante que a primeira miniatura (a capa) esteja ativa ao carregar
        const primeiraMinia = document.querySelector('.mini-img');
        if (primeiraMinia) {
            primeiraMinia.classList.add('ativo');
        }
    });