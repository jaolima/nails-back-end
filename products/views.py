from rest_framework import generics
from .serializers import CategorySerializer, ProductSerializer

from .models import Category, Products


class CategorysAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
