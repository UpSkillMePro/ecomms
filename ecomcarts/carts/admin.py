from django.contrib import admin

from carts.models import Cart, Items


# Register your models here.
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    pass

@admin.register(Items)
class ItemsAdmin(admin.ModelAdmin):
    pass