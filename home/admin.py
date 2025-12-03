from django.contrib import admin
from .models import Category, Produtos, Cart, CartItem, Order, OrderItem

@admin.register(Produtos)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('nome', 'category', 'valor', 'stock', 'creat_data')
    list_filter = ('category',)
    search_fields = ('nome',)
    prepopulated_fields = {'slug': ('nome',)}

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('nome', 'slug')
    prepopulated_fields = {'slug': ('nome',)}

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'status', 'creat_data')
    list_filter = ('status',)
    search_fields = ('user__username',)

admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(OrderItem)
