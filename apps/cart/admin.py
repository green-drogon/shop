from django.contrib import admin
from .models import CartItem


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'product_variant',
        'quantity',
        'created_at',
    )

    list_filter = (
        'user',
    )

    search_fields = (
        'user__phone',
        'product_variant__product__name',
    )

    list_editable = (
        'quantity',
    )