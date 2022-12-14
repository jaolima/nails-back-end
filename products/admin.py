from django.contrib import admin

from .models import Category, Products


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'active')


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'active',
        'alias_color',
        'description',
        'qtd',
        'type',
        'size',
        'barcode',
        'uri_image',
        'price',
        'top_products',
        'discount',
    )
