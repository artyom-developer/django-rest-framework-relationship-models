import django_filters 
from product.models import ProductModel
 
from django_filters import rest_framework as filters

class ProductFilter(filters.FilterSet):
    class Meta:
        model = ProductModel
        fields = ('name', 'price')