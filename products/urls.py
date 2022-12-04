from django.urls import path

from .views import CategorysAPIView, CategoryAPIView

urlpatterns = [
    path('categorys/', CategorysAPIView.as_view(), name='categorys'),
    path('category/<int:pk>/', CategoryAPIView.as_view(), name='category'),
]
