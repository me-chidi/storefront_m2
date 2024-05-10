from decimal import Decimal
from .models import Product, Collection
from rest_framework import serializers

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title', 'products']

    products = serializers.SerializerMethodField(method_name='no_of_products')

    def no_of_products(self, collection):
        # what method is count?
        # its a queryset method to be used wherever theres a query
        # luckily there's one here
        return collection.products.count()

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'slug', 'inventory', 'unit_price', 'price_with_tax', 'collection']

    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')
   
    def calculate_tax(self, product: Product):
        return product.unit_price * Decimal(1.1)
    
    