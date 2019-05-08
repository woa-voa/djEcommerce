from django.contrib import admin
from e_comapp.models import Category, Brand, Product, Cart, CartItem, Order

# Register your models here.

admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)