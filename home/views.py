from django.shortcuts import render ,  redirect ,get_object_or_404
from .models import Produtos , Category , Cart , CartItem
from django.contrib.auth.decorators import login_required
from django.contrib import messages



def home (request):
    categorias = Category.objects.all()
    produtos = Produtos.objects.all()

    contexto = {
        'produtos':produtos,
        'categorias':categorias
    }
    return render(request,'home.html', contexto )

def filtro (request , slug_categoria):
    categoria_objeto = get_object_or_404(Category , slug = slug_categoria)
    produtos_filtro = Produtos.objects.filter(category = categoria_objeto)

    categorias = Category.objects.all()
    contexto = {
        'produtos':produtos_filtro,
        'categorias': categorias
    }
    return render(request , 'home.html', contexto)

def detalhe_produto(request , produto_slug):
    slug_url = get_object_or_404(Produtos, slug=produto_slug)
    return render(request,'produto.html',{'slug_url':slug_url})

@login_required
def add_carrinho(request):
    if request.method == 'POST':
        produto_id = request.POST.get('produto_id')
        quantidade = int(request.POST.get('quantidade',1))
        produto_slug = request.POST.get('produto_slug')

        produto = get_object_or_404(Produtos , id=produto_id)

        cart , existe = Cart.objects.get_or_create(user=request.user)
        cart_item_existe = CartItem.objects.filter( cart=cart , produtos=produto_id)

        if cart_item_existe.exists():
            cart_item = cart_item_existe.first()
            cart_item.quantidade += quantidade
            cart_item.save()
            messages.success(request,'Item adicionado ao carrinho')
            return redirect('detalhe_produto', produto_slug = produto_slug)
        else:
            CartItem.objects.create(
                cart = cart,
                produtos = produto,
                quantidade = quantidade
            )
            messages.success(request,'Item adicionado ao carrinho')
            return redirect('detalhe_produto', produto_slug = produto_slug)
    else:
        messages.error(request, 'Erro ao adicionar ao carrinho')
        return redirect('home')

@login_required 
def carrinho(request):

    cart , existe = Cart.objects.get_or_create(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart).select_related('produtos')

    contexto={
        'cart_items':cart_items
    }

    return render(request,'carrinho.html',contexto)