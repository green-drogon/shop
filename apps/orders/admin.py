from django.contrib import admin
from .models import Order, OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'receiver_name',
        'receiver_phone',
        'total_price',
        'payment_status',
        'order_status',
        'created_at',
    )

    list_filter = (
        'payment_status',
        'order_status',
        'created_at',
    )

    search_fields = (
        'id',
        'user__phone',
        'receiver_name',
        'receiver_phone',
        'payment_code',
    )

    readonly_fields = (
        'created_at',
        'updated_at',
    )


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'order',
        'product_variant',
        'quantity',
        'price',
        'created_at',
    )

    search_fields = (
        'order__id',
        'product_variant__product__name',
        'product_variant__sku',
    )

    readonly_fields = (
        'created_at',
    )