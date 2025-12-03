from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    nome = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.nome

class Produtos(models.Model):
    category = models.ForeignKey( Category , on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)
    descrition = models.TextField(blank=True)
    valor = models.DecimalField(max_digits=10 , decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    imagem = models.ImageField(upload_to='produtos/')
    slug = models.SlugField( unique=True)
    creat_data = models.DateField(auto_now_add=True)
    update_data = models.DateField(auto_now=True)

    def __str__(self):
        return self.nome

class Cart(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    creat_data = models.DateField(auto_now_add=True)
    update_data = models.DateField(auto_now=True)

    def __str__(self):
        return f"Carrinho de {self.user.username}"
    
class CartItem(models.Model):
    cart = models.ForeignKey(Cart , on_delete= models.CASCADE)
    produtos = models.ForeignKey(Produtos , on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)

    def __init__(self):
        return self.quantidade * self.produtos.valor
    
class Order(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    creat_data = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ('PENDING', 'Pendente'),
            ('PAID', 'Pago'),
            ('SHIPPED', 'Enviado'),
            ('DELIVERED', 'Entregue'),
        ],
        default='PENDING'
    )
    
    def __str__(self):
        return f"Pedido {self.id} de {self.user.username}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Produtos, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def subtotal(self):
        return self.quantity * self.price

