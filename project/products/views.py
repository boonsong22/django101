from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView

from .seriazliers import ProductSerializer
from .models import Product


class ProductListView(ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductDetailView(RetrieveDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
