from rest_framework import serializers

from .models import Products, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'name'
        )


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = (
            'id',
            'color',
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
            'category'
        )
