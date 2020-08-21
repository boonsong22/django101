from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class CustomSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=10, required=True)
