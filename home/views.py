from django.shortcuts import render , get_object_or_404
from .models import Produtos


def home (request):
    produtos = Produtos.objects.all()
    return render(request,'home.html', {'produtos':produtos})

def detalhe_produto(request , produto_slug):
    slug_url = get_object_or_404(Produtos, slug=produto_slug)
    return render(request,'produto.html',{'slug_url':slug_url})