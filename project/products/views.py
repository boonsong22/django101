from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView

from .seriazliers import ProductSerializer, CustomSerializer
from .models import Product
from rest_framework.views import APIView
from rest_framework.response import Response
class ProductListView(ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductDetailView(RetrieveDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

class CustomProductView(APIView):
    def get(self , rq):
        return Response(True)
    def post(self,rq):
        serializer = CustomSerializer(data=rq.data)
        serializer.is_valid(raise_exception=True)
        return Response()    

