from django.urls import path
from . import views
urlpatterns =[
    path('', views.home, name='home'),
    path('produto/<slug:produto_slug>/', views.detalhe_produto , name='detalhe_produto'),
    path('categira/<slug:slug_categoria>/', views.filtro ,name='filtro')
]