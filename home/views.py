from django.shortcuts import render , get_object_or_404
from .models import Produtos , Category


def home (request):
    categorias = Category.objects.all()
    produtos = Produtos.objects.all()

    contexto = {
        'produtos':produtos,
        'categorias':categorias
    }

    return render(request,'home.html', contexto )

def filtro(request , slug_categoria):
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