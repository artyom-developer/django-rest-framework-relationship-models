from rest_framework import serializers
from product.models import ProductModel
from category.serializers import CategorySerializer
from category.models import CategoryModel


class ProductSerializer(serializers.ModelSerializer): 
    category = CategorySerializer() 

    class Meta:
        model = ProductModel
        fields = ['id', 'name', 'description', 'price', 'published', 'category']

    def create(self, validated_data):
        category_post = validated_data.pop("category")
        category_data = CategoryModel.objects.get(pk=category_post['id'])
        product = ProductModel.objects.create(category=category_data,**validated_data)
       
        return product
    def update(self, instance, validated_data):
         
        instance.name = validated_data.pop('name', instance.name)
        instance.description = validated_data.pop('description', instance.description)
        instance.price = validated_data.pop('price', instance.price)
        instance.published = validated_data.pop('published', instance.published)
         
        category_post = validated_data.pop("category")
        category_data = CategoryModel.objects.get(pk=category_post['id'])
        instance.category = category_data
        instance.save()
        return instance     
        