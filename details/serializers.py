from rest_framework import serializers
from details.models import Product,Collection
from decimal import Decimal

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','title','Price','Category','description','image']