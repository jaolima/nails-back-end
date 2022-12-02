from rest_framework import generics, viewsets, mixins
from rest_framework.generics import get_object_or_404

from .models import Category, Products

"""
API V1
"""

# class CategoryAPIView(generics.ListCreatAPIView):
#     queryset = Category.objects.all()
#     serializer_class =