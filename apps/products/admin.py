from django.contrib import admin
from .models import (
    Category,
    Color,
    Size,
    Product,
    ProductImage,
    ProductVariant,
)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'slug',
        'parent',
        'created_at',
    )

    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'hex_code',
    )

    search_fields = ('name',)


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'sort_order',
    )

    ordering = ('sort_order',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'category',
        'is_active',
        'created_at',
    )

    list_filter = (
        'category',
        'is_active',
    )

    search_fields = (
        'name',
        'description',
    )

    list_editable = (
        'is_active',
    )

    prepopulated_fields = {
        'slug': ('name',)
    }


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'product',
        'is_primary',
        'sort_order',
        'created_at',
    )

    list_filter = (
        'product',
        'is_primary',
    )

    list_editable = (
        'is_primary',
        'sort_order',
    )


@admin.register(ProductVariant)
class ProductVariantAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'product',
        'color',
        'size',
        'price',
        'stock',
        'sku',
        'is_active',
    )

    list_filter = (
        'product',
        'color',
        'size',
        'is_active',
    )

    search_fields = (
        'product__name',
        'sku',
        'color__name',
        'size__name',
    )

    list_editable = (
        'price',
        'stock',
        'is_active',
    )